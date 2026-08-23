#!/usr/bin/env python3
"""Convertit un workflow ComfyUI au format « interface » (tel qu'exporté par l'éditeur ou livré en exemple :
nodes[] avec widgets_values et links[]) en prompt « API » (dict id -> {class_type, inputs}) exécutable par POST /prompt.

ComfyUI ne fournit pas cette conversion côté serveur ; on la fait avec /object_info du serveur cible : pour chaque
nœud, les entrées non reliées reçoivent, dans l'ordre de déclaration (required puis optional), les widgets_values
successifs ; les widgets « control_after_generate » (randomize/fixed après une graine) sont sautés.

Usage : python comfy_ui_to_api.py <workflow_ui.json> <url_comfy> <sortie_api.json> [--keep-muted]
  * les nœuds en mode 2 (muted) ou 4 (bypass) sont retirés (bypass : leurs liens sont court-circuités
    quand l'entrée et la sortie ont le même type) ;
  * les groupes/notes/reroutes/PrimitiveNode sont résolus ou ignorés.
Écrit aussi <sortie_api>.map.json : id de nœud -> titre, pour retrouver où brancher image/audio/masques/prompts.
Écrit le 23 août 2026 pour rejouer les exemples InfiniteTalk (WanVideoWrapper) et LTX-2.5 par l'API.
"""
import json
import sys
import urllib.request

WIDGET_TYPES = {"INT", "FLOAT", "STRING", "BOOLEAN", "COMBO"}


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())


def is_widget(spec):
    """spec = ["INT", {...}] ou [["a","b"], {...}] (combo) ; une entrée est un widget si son type est scalaire ou une liste de choix."""
    t = spec[0]
    if isinstance(t, list):
        return True
    if isinstance(t, str) and t in WIDGET_TYPES:
        return True
    return False


def main():
    src, base, out = sys.argv[1], sys.argv[2].rstrip("/"), sys.argv[3]
    wf = json.load(open(src, encoding="utf-8"))
    info = http_json(f"{base}/object_info")
    nodes = {n["id"]: n for n in wf["nodes"]}
    links = {l[0]: l for l in wf.get("links", [])}  # id -> [id, from_node, from_slot, to_node, to_slot, type]

    # résolution des Reroute / PrimitiveNode / bypass : on suit les liens jusqu'à un vrai nœud
    def resolve(link_id):
        l = links[link_id]
        src_node = nodes[l[1]]
        while src_node["type"] in ("Reroute",) or src_node.get("mode") == 4:
            # prendre la première entrée reliée du nœud traversé
            inc = [i for i in src_node.get("inputs", []) if i.get("link") is not None]
            if not inc:
                return None
            l = links[inc[0]["link"]]
            src_node = nodes[l[1]]
        return [str(l[1]), l[2]]

    api, names = {}, {}
    for nid, n in nodes.items():
        if n.get("mode") in (2, 4) or n["type"] in ("Reroute", "Note", "MarkdownNote", "PrimitiveNode"):
            continue
        if n["type"] not in info:
            print(f"ATTENTION : type inconnu du serveur : {n['type']} (nœud {nid})", file=sys.stderr)
            continue
        spec = info[n["type"]]["input"]
        order = list(spec.get("required", {}).items()) + list(spec.get("optional", {}).items())
        linked = {i["name"]: i.get("link") for i in n.get("inputs", []) if i.get("link") is not None}
        widget_names = {i["name"] for i in n.get("inputs", []) if i.get("widget")}
        wv = list(n.get("widgets_values") or [])
        inputs = {}
        wi = 0
        for name, sp in order:
            if name in linked:
                r = resolve(linked[name])
                if r:
                    inputs[name] = r
                # un widget converti en entrée reliée consomme quand même sa valeur dans widgets_values
                if is_widget(sp) or name in widget_names:
                    if wi < len(wv):
                        wi += 1
                        if name == "seed" or name == "noise_seed":
                            if wi < len(wv) and isinstance(wv[wi], str) and wv[wi] in ("fixed", "randomize", "increment", "decrement"):
                                wi += 1
                continue
            if is_widget(sp) or name in widget_names:
                if wi < len(wv):
                    inputs[name] = wv[wi]
                    wi += 1
                    if name in ("seed", "noise_seed") and wi < len(wv) and isinstance(wv[wi], str) and wv[wi] in ("fixed", "randomize", "increment", "decrement"):
                        wi += 1
                elif isinstance(sp, list) and len(sp) > 1 and isinstance(sp[1], dict) and "default" in sp[1]:
                    inputs[name] = sp[1]["default"]
        api[str(nid)] = {"class_type": n["type"], "inputs": inputs}
        names[str(nid)] = n.get("title") or n["type"]
    json.dump(api, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(names, open(out + ".map.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(api)} nœuds -> {out}")


if __name__ == "__main__":
    main()
