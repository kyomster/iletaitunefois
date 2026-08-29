#!/usr/bin/env python3
"""Assemble les prompts des PLANCHES DE RÉFÉRENCE d'un épisode — décors, personnages, objets de continuité —
pour un style de la bibliothèque.

Les planches sont ce qu'on réinjecte ensuite sur les plans (RÈGLE 1 : la référence impose sa mise en page et son
style). Elles se génèrent à sec, sans référence, sur fond neutre (RÈGLE 15 ; fond gris uni prescrit en positif sur
les styles à aplats), sans visage lisible dans la foule (RÈGLE 26), couleurs nommées en positif (RÈGLES 30 et 34).
Les objets de continuité (RÈGLE 36) se décrivent en entier et par leur nom (RÈGLES 38 et 42).

Le module de briques de la série fournit DECORS, IDENT_REFS, CADRAGE_REFS, OBJETS, FOND, FOND_DUR, REFS_DEFAUT.

Usage : python assembler_refs.py <briques.py> <sortie.json> [--styles=StyleP] [--refs=D01,Ballon]
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bibliotheque import charger_briques, charger_styles, options  # noqa: E402

GEN_PARAMS = {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1, "use_unlim": False}


def assemble_ref(nom, style, B):
    variant = style["variante_identite"]
    fond = B.FOND_DUR if variant == "P" else B.FOND
    negs = []
    if nom in B.DECORS:
        body = B.DECORS[nom]
    elif nom in B.OBJETS:
        body = B.OBJETS[nom].format(fond=fond)
    else:
        ident = B.IDENT_REFS[nom]
        body = f"Scene: {ident.get(variant, ident['AC'])}, {fond}. {B.CADRAGE_REFS[nom]}"
        if nom == "Foule":
            negs.append(B.NEG_FOULE.get(variant, B.NEG_FOULE["defaut"]))
    negs += [style["negative"], style["neg_epoque"], style["neg_universelle"]]
    positive = " ".join(x for x in (style["scene"], style["epoque"], body) if x)
    # les négatives se joignent par une virgule : collées par une espace, la dernière se soude à la suivante
    return {"name": f"{nom}_{style['code']}", "reference": nom, "style": style["code"],
            "params": {**GEN_PARAMS, "prompt": positive + " Avoid: " + ", ".join(n.rstrip(". ") for n in negs) + "."}}


def main():
    args, opts, styles = options(sys.argv[1:])
    B = charger_briques(args[0])
    bib = charger_styles()
    refs = opts["refs"].split(",") if isinstance(opts.get("refs"), str) else list(B.REFS_DEFAUT)
    out = [assemble_ref(n, bib[s], B) for s in styles for n in refs]
    Path(args[1]).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(out)} prompts de référence écrits dans {args[1]} ({', '.join(styles)})")


if __name__ == "__main__":
    main()
