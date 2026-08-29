#!/usr/bin/env python3
"""Assemble les prompts d'images clés d'un épisode, pour un ou plusieurs styles de la bibliothèque.

Générique depuis le 27 août 2026 : les blocs de style viennent de `styles/*/style.json`, tout ce qui est propre
à l'épisode (briques de plans, références, blocs identité, clauses, cadrages durcis) vient d'un module de briques
de la série, par exemple `iletaitunefois/S01E01/prompts/briques_pilote.py`.

Règle d'assemblage (inchangée depuis le runbook du 22 août) :
  [style.scene] + [traitement de lumière du bloc, si le style en a] + [style.epoque]
  + [brique, blocs identité substitués selon la variante du style] + [clauses du plan] + [cadrage durci]
  + (si un personnage est réinjecté) "same characters as reference, same art style as reference"
  + " Avoid: " + [négative de foule si bloc de foule] + [négatives du plan] + [style.negative] + [neg_epoque] + [neg_universelle]

Usage :
  python assembler_prompts.py <briques.py> <media_ids.json> <sortie.json> [--styles=StyleP,StyleK] [--plans=P02,P03] [--md=sortie.md]

<media_ids.json> : {"D01_StyleP.png": "<media_id>", ...} — les planches de référence déjà envoyées chez Higgsfield.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bibliotheque import charger_briques, charger_styles, options  # noqa: E402

SAME_AS_REF = "same characters as reference, same art style as reference"
GEN_PARAMS = {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1, "use_unlim": False}


def substituer(brique, ident, variant):
    body = brique
    for key, blocs in ident.items():
        body = body.replace(f"[{key}]", blocs.get(variant, blocs["AC"]))
    assert "[" not in body, f"substitution incomplète : {body[:80]}"
    return body


def assemble(name, bloc, brique, style, B, media_ids):
    variant = style["variante_identite"]
    body = substituer(brique, B.IDENT, variant)
    refs = B.REFS[name]
    for texte, plans, ref_requise in getattr(B, "CLAUSES", []):
        if name in plans and (ref_requise is None or ref_requise in refs):
            body += f" {texte}."
    if name in getattr(B, "CADRAGE_DURCI", {}):
        body += f" {B.CADRAGE_DURCI[name]}"
    lumiere = ""
    if style.get("lumiere"):
        lumiere = style["lumiere"].get(getattr(B, "REGISTRE_LUMIERE", {}).get(bloc, ""), "")
    positive = " ".join(x for x in (style["scene"], lumiere, style["epoque"], body) if x)
    if any(r in B.PERSONNAGES for r in refs):
        positive += f" {SAME_AS_REF}"
    negs = []
    if bloc in getattr(B, "BLOCS_FOULE", set()):
        if name not in getattr(B, "PLANS_SANS_NEG_FOULE", set()):
            negs.append(B.NEG_FOULE.get(variant, B.NEG_FOULE["defaut"]))
        elif f"{variant}_plans_nommes" in B.NEG_FOULE:
            negs.append(B.NEG_FOULE[f"{variant}_plans_nommes"])
    negs += getattr(B, "NEG_PLAN", {}).get(name, [])
    negs += [style["negative"], style["neg_epoque"], style["neg_universelle"]]
    prompt = f"{positive} Avoid: " + ", ".join(n.rstrip(". ") for n in negs)
    medias = [{"role": "image_references", "value": media_ids.get(f"{r}_{style['code']}.png", "A_ENVOYER")} for r in refs]
    return {
        "name": f"{name}_{style['code']}", "plan": name, "bloc": bloc, "style": style["code"],
        "references": [f"{r}_{style['code']}.png" for r in refs],
        "params": {**GEN_PARAMS, "prompt": prompt, "medias": medias},
    }


def main():
    args, opts, styles = options(sys.argv[1:])
    B = charger_briques(args[0])
    media_ids = json.loads(Path(args[1]).read_text(encoding="utf-8"))
    bib = charger_styles()
    plans = set(opts["plans"].split(",")) if isinstance(opts.get("plans"), str) else None
    jobs = []
    for code in styles:
        style = bib[code]
        for name, bloc, brique in B.BRIQUES:
            if plans and name not in plans:
                continue
            jobs.append(assemble(name, bloc, brique, style, B, media_ids))
    manquants = sorted({m for j in jobs for m in j["references"] if m not in media_ids})
    if manquants:
        print("PLANCHES SANS media_id (à envoyer chez Higgsfield d'abord) :", ", ".join(manquants))
    Path(args[2]).write_text(json.dumps(jobs, indent=1, ensure_ascii=False), encoding="utf-8")
    if isinstance(opts.get("md"), str):
        md = [f"# {B.SERIE} {B.EPISODE} — prompts d'images clés, tels qu'assemblés", "",
              "Générés par `atelier/scripts/assembler_prompts.py`. Un prompt = bloc de style + lumière + époque + brique + clauses + `Avoid:` négatives.", ""]
        for j in jobs:
            md += [f"## {j['name']}", "", f"Références : {', '.join(j['references'])}", "", "```", j["params"]["prompt"], "```", ""]
        Path(opts["md"]).write_text("\n".join(md), encoding="utf-8", newline="\n")
    print(f"{len(jobs)} prompts écrits dans {args[2]} ({', '.join(styles)})")


if __name__ == "__main__":
    main()
