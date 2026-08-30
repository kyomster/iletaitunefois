#!/usr/bin/env python3
"""Ce qu'une session doit savoir avant d'agir — imprimé au démarrage par le hook SessionStart.

  python contexte.py          la page de contexte (état, ce qui attend Guillaume, doctor, prochaine action, règles à ne pas retenter)
  python contexte.py --next   seulement la prochaine action (next)
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import donnees as D  # noqa: E402
from doctor import controler  # noqa: E402


def prochaine_action(defaillances):
    """UNE action : la défaillance de plus haut rang ; sinon l'étape courante de etat.json ; sinon rien."""
    if defaillances:
        d = defaillances[0]
        if d["severite"] != "ATTENTION" or d["code"] not in ("TEASER_ATTEND_EPISODE",):
            return {"verbe": "réparer", "cible": d["adresse"], "quoi": d["reparation"], "motif": d["code"]}
    etat = D.lire("etat") if (D.DONNEES / "etat.json").exists() else {}
    if etat.get("prochaine_etape"):
        return {"verbe": "continuer", "cible": etat["prochaine_etape"], "quoi": etat.get("prochaine_etape_detail", ""), "motif": "etat.json"}
    return {"verbe": "rien", "cible": None, "quoi": "rien à faire : ne pas inventer de tâche", "motif": None}


def page():
    etat = D.lire("etat") if (D.DONNEES / "etat.json").exists() else {}
    plans = D.lire("plans")["elements"]; reps = D.lire("repliques")["elements"]
    total = sum(p["duree"] for p in plans)
    defs = controler()
    try:
        sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=D.RACINE, capture_output=True, text=True).stdout.strip()
        sale = subprocess.run(["git", "status", "--short"], cwd=D.RACINE, capture_output=True, text=True).stdout.strip()
    except Exception:
        sha, sale = "?", ""
    l = [f"## Contexte — {D.EP_CODE} · dépôt {sha}" + (" · MODIFICATIONS NON COMMITÉES" if sale else ""), ""]
    l.append(f"**Épisode** : {len(plans)} plans, {total // 60} min {total % 60:02d} s, {len(reps)} répliques. Vérité = `iletaitunefois/S01E01/donnees/*.json` ; les .md sont générés (`rendre.py`). Règles : `CLAUDE.md`.")
    if etat:
        l.append(f"**Où on en est** ({etat.get('date', '?')}) : {etat.get('resume', '')}")
        for x in etat.get("ouvert", []):
            l.append(f"- ouvert : {x}")
    prop = [x for coll in ("plans", "repliques", "faits", "personnages", "continuite", "assets", "decisions") for x in D.lire(coll)["elements"] if x.get("statut") == "propose"]
    l.append(f"**En attente du mot de Guillaume** : {len(prop)} objets « propose »" + (f" — {', '.join(x['adresse'] for x in prop[:6])}{'…' if len(prop) > 6 else ''}" if prop else ""))
    nb = {s: sum(1 for d in defs if d["severite"] == s) for s in ("BLOQUANT", "ERREUR", "ATTENTION")}
    l.append(f"**doctor** : {nb['BLOQUANT']} bloquant, {nb['ERREUR']} erreur, {nb['ATTENTION']} attention" + (" — " + " ; ".join(f"{d['code']} ({d['adresse']})" for d in defs[:4]) if defs else ""))
    a = prochaine_action(defs)
    l.append(f"**Prochaine action (next)** : {a['verbe']} {a['cible'] or ''} — {a['quoi']}")
    regles = D.lire(str(D.REGLES))["elements"] if D.REGLES.exists() else []
    nn = [r for r in regles if r.get("ne_pas_retenter")]
    if nn:
        l.append("**À ne pas retenter** : " + " ; ".join(r["titre"] for r in nn))
    l.append("**Les trois règles qui coûtent le plus cher** : la référence impose sa mise en page ; on regarde une planche avant d'en dériver ; ce qui doit rester identique est une image réinjectée, pas une description.")
    return "\n".join(l)


if __name__ == "__main__":
    if "--next" in sys.argv:
        print(json.dumps(prochaine_action(controler()), ensure_ascii=False, indent=1))
    else:
        print(page())
