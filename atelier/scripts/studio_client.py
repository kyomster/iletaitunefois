#!/usr/bin/env python3
"""Client MCP de Studio (le socle qui détient la vérité des séries), sans dépendance hors stdlib.

Transport HTTP streamable : `initialize` → `notifications/initialized` (202 sans corps) → `tools/call`.
Les réponses arrivent en JSON ou en SSE (`data:` ; on prend le dernier événement). Un outil qui réussit rend
`result.structuredContent` (avec `_commit` sur les écritures) ; un refus rend `isError: true` et un JSON
`{erreur, message, details}` dans `content[0].text` — il est levé ici comme `RefusStudio`, jamais contourné.

Le jeton est lu dans le `.env` à la racine du dépôt (clé `MCP_TOKEN`) et n'est jamais imprimé ni journalisé.

Usage :
  python studio_client.py ping                       initialize + sync_status + next
  python studio_client.py tools                      la liste des outils (nom, paramètres)
  python studio_client.py call <outil> '<json>'      un appel ; ajouter --journal=<fichier.jsonl> pour le consigner
"""
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
URL = "https://vps-82e6879d.vps.ovh.net/api/mcp"
ENV = Path(__file__).resolve().parents[2] / ".env"
OUTILS_ECRITURE_PREFIXES = ("create_", "upsert_", "set_", "record_", "lock_", "link_", "answer_", "request_", "cancel_", "open_", "close_", "retire_")


def jeton():
    for line in ENV.read_text(encoding="utf-8").splitlines():
        if line.startswith("MCP_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("MCP_TOKEN absent du .env")


class RefusStudio(Exception):
    def __init__(self, code, message, details=None, outil=None, args=None):
        super().__init__(f"{outil}: {code} — {message}")
        self.code, self.message, self.details, self.outil, self.arguments = code, message, details, outil, args


def empreinte(outil, args):
    return hashlib.sha256((outil + "\n" + json.dumps(args, sort_keys=True, ensure_ascii=False)).encode("utf-8")).hexdigest()


class Studio:
    def __init__(self, url=URL, journal=None, timeout=120):
        self.url, self.timeout, self.sid, self._id = url, timeout, None, 0
        self.journal = Path(journal) if journal else None
        self._h = {"Authorization": f"Bearer {jeton()}", "Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        init = self._rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "iletaitunefois", "version": "1"}})
        self.serveur = init.get("result", {}).get("serverInfo", {})
        self._rpc("notifications/initialized", {}, notification=True)

    def _rpc(self, method, params, notification=False, tentatives=3):
        h = dict(self._h)
        if self.sid:
            h["Mcp-Session-Id"] = self.sid
        body = {"jsonrpc": "2.0", "method": method, "params": params}
        if not notification:
            self._id += 1
            body["id"] = self._id
        req = urllib.request.Request(self.url, data=json.dumps(body).encode("utf-8"), headers=h)
        for essai in range(1, tentatives + 1):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    raw = r.read().decode("utf-8", "replace")
                    self.sid = r.headers.get("Mcp-Session-Id") or self.sid
                    ctype = r.headers.get("Content-Type", "")
                break
            except urllib.error.HTTPError as e:
                if e.code in (401, 403):
                    raise RefusStudio("HTTP_AUTH", f"HTTP {e.code} : jeton refusé", outil=method)
                if e.code >= 500 and essai < tentatives:
                    time.sleep((2, 5, 10)[essai - 1]); continue
                raise RefusStudio(f"HTTP_{e.code}", e.read().decode("utf-8", "replace")[:500], outil=method)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                # une écriture en timeout a pu être commise : on ne la rejoue jamais à l'aveugle
                if essai < tentatives and (notification or not method == "tools/call" or not params.get("name", "").startswith(OUTILS_ECRITURE_PREFIXES)):
                    time.sleep((2, 5, 10)[essai - 1]); continue
                raise RefusStudio("RESEAU", str(e), outil=method)
        if not raw.strip():
            return {}
        if "text/event-stream" in ctype:
            data = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")]
            raw = data[-1] if data else "{}"
        return json.loads(raw)

    def appeler(self, outil, args=None):
        args = args or {}
        rep = self._rpc("tools/call", {"name": outil, "arguments": args})
        if "error" in rep:
            err = rep["error"]
            raise RefusStudio(str(err.get("code", "RPC")), err.get("message", ""), err.get("data"), outil, args)
        res = rep.get("result", {})
        texte = "".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text")
        if res.get("isError"):
            try:
                e = json.loads(texte)
            except json.JSONDecodeError:
                e = {"erreur": "ERREUR", "message": texte[:500]}
            raise RefusStudio(e.get("erreur", "ERREUR"), e.get("message", ""), e.get("details"), outil, args)
        out = res.get("structuredContent")
        if out is None:
            try:
                out = json.loads(texte) if texte else {}
            except json.JSONDecodeError:
                out = {"texte": texte}
        if isinstance(out, dict) and out.get("erreur"):
            raise RefusStudio(out["erreur"], out.get("message", ""), out.get("details"), outil, args)
        if self.journal and outil.startswith(OUTILS_ECRITURE_PREFIXES):
            with open(self.journal, "a", encoding="utf-8") as f:
                f.write(json.dumps({"date": datetime.now(timezone.utc).isoformat(timespec="seconds"), "outil": outil,
                                    "empreinte": empreinte(outil, args), "commit": (out or {}).get("_commit") if isinstance(out, dict) else None,
                                    "avertissement": (out or {}).get("_avertissementGit") if isinstance(out, dict) else None}, ensure_ascii=False) + "\n")
        return out

    def outils(self):
        return self._rpc("tools/list", {}).get("result", {}).get("tools", [])


def deja_journalise(journal, outil, args):
    p = Path(journal)
    if not p.exists():
        return False
    e = empreinte(outil, args)
    return any(json.loads(l).get("empreinte") == e for l in p.read_text(encoding="utf-8").splitlines() if l.strip())


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = {a.split("=", 1)[0].lstrip("-"): (a.split("=", 1)[1] if "=" in a else True) for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__); return
    s = Studio(journal=opts.get("journal"))
    if args[0] == "ping":
        print("serveur :", s.serveur)
        print(json.dumps(s.appeler("sync_status"), ensure_ascii=False, indent=1))
        print(json.dumps(s.appeler("next"), ensure_ascii=False, indent=1))
    elif args[0] == "tools":
        for t in s.outils():
            props = t.get("inputSchema", {}).get("properties", {})
            req = t.get("inputSchema", {}).get("required", [])
            print(f"- {t['name']}({', '.join(p + ('*' if p in req else '') for p in props)})")
    elif args[0] == "call":
        try:
            print(json.dumps(s.appeler(args[1], json.loads(args[2]) if len(args) > 2 else {}), ensure_ascii=False, indent=1))
        except RefusStudio as e:
            print("REFUS", e.code, "—", e.message, json.dumps(e.details, ensure_ascii=False) if e.details else "")
            sys.exit(2)


if __name__ == "__main__":
    main()
