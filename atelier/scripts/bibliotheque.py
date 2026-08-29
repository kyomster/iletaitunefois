#!/usr/bin/env python3
"""Charge la bibliothèque de styles (`styles/*/style.json`) et un module de briques de série.

Un style est un dictionnaire aux clés : code, lettre, nom, dossier, famille, variante_identite, scene,
personnage, personnage_epoque, epoque, negative, lumiere, clip, neg_epoque, neg_universelle.
Les blocs se copient tels quels ; aucun script ne les reformule (RÈGLE 13).

Un module de briques est un fichier Python propre à une série et à un épisode — par exemple
`iletaitunefois/S01E01/prompts/briques_pilote.py` — qui porte ce qui change d'une série à l'autre :
les plans, les références par plan, les blocs identité, les clauses, les cadrages durcis, les clips.
"""
import importlib.util
import json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
STYLES_DIR = RACINE / "styles"


def charger_styles():
    styles = {}
    for js in sorted(STYLES_DIR.glob("*/style.json")):
        s = json.loads(js.read_text(encoding="utf-8"))
        styles[s["code"]] = s
    return styles


def charger_briques(chemin):
    chemin = Path(chemin)
    spec = importlib.util.spec_from_file_location(chemin.stem, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def options(argv, defaut_styles=("StyleP",)):
    """Sépare les arguments positionnels des options `--cle=valeur` ; `--styles` est éclaté en tuple."""
    args = [a for a in argv if not a.startswith("--")]
    opts = {a.split("=", 1)[0].lstrip("-"): (a.split("=", 1)[1] if "=" in a else True) for a in argv if a.startswith("--")}
    styles = tuple(opts["styles"].split(",")) if isinstance(opts.get("styles"), str) else tuple(defaut_styles)
    return args, opts, styles
