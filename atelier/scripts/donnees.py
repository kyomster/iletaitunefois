#!/usr/bin/env python3
"""La couche de vérité du dépôt : des JSON adressables, avec statut et empreinte.

Chaque objet a une **adresse** stable (`S01E01/plan-2`, `S01E01/plan-2/ligne-0`, `fait/1.16`, `perso/garnerin`,
`asset/clip-P02`, `regle/36`, `decision/2026-08-29-style-p`), un **statut** — `propose` (écrit par l'agent, non
validé), `valide` (Guillaume a dit oui, date), `verrouille` (zone verrouillée : ne change que sur décision datée),
`ecarte` — et une **empreinte** (sha256 du contenu canonique, sans les champs de suivi).

Les fichiers :
  iletaitunefois/S01E01/donnees/{scenario,plans,repliques,decors,faits,personnages,continuite,assets,contrats,attendus,decisions}.json
  iletaitunefois/S01E01/donnees/production.json, son.json     (les blocs des documents générés)
  iletaitunefois/S01E01/donnees/etat.json                     (où on en est, lu au démarrage de chaque session)
  atelier/regles/regles.json                                  (les règles d'images et de vidéo, les moteurs écartés)

Les documents lisibles (scenario.md, plan-de-production.md, son-et-voix.md) sont GÉNÉRÉS par rendre.py : on ne les
édite jamais à la main. Une correction passe par le JSON, puis rendre.py, puis doctor.py, puis un commit.
"""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parents[2]
SERIE = RACINE / "iletaitunefois"
EP_CODE = "S01E01"
EP = SERIE / EP_CODE
DONNEES = EP / "donnees"
REGLES = RACINE / "atelier" / "regles" / "regles.json"
STATUTS = ("propose", "valide", "verrouille", "ecarte")
CHAMPS_SUIVI = {"empreinte", "statut", "valide_par", "valide_le", "decision", "_note"}


def lire(nom):
    p = DONNEES / f"{nom}.json" if not str(nom).endswith(".json") else Path(nom)
    return json.loads(p.read_text(encoding="utf-8"))


def ecrire(nom, obj):
    p = DONNEES / f"{nom}.json" if not str(nom).endswith(".json") else Path(nom)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")


def canonique(obj):
    """Le contenu qui compte : sans les champs de suivi, clés triées."""
    if isinstance(obj, dict):
        return {k: canonique(v) for k, v in sorted(obj.items()) if k not in CHAMPS_SUIVI}
    if isinstance(obj, list):
        return [canonique(x) for x in obj]
    return obj


def empreinte(obj):
    return hashlib.sha256(json.dumps(canonique(obj), ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def index(liste, cle="adresse"):
    return {x[cle]: x for x in liste}


def adresse_plan(n):
    return f"{EP_CODE}/plan-{n}"


def adresse_ligne(n, o):
    return f"{EP_CODE}/plan-{n}/ligne-{o}"


def mots(texte):
    return len(texte.split())


def texte_dit(plan, lignes):
    """La ligne « Texte dit » telle qu'écrite dans le scénario, reconstruite depuis les répliques."""
    mine = [l for l in lignes if l["plan"] == plan["numero"]]
    if not mine:
        return plan.get("muet") or "—"
    parts = []
    for l in sorted(mine, key=lambda x: x["ordre"]):
        did = f" ({l['didascalie']})" if l.get("didascalie") else ""
        parts.append(f"{l['locuteur']}{did} : « {l['texte']} »")
    return " ".join(parts)


def valider(obj, par="Guillaume", quand=None, statut="valide"):
    assert statut in STATUTS
    obj["statut"] = statut
    obj["valide_par"] = par
    obj["valide_le"] = quand or date.today().isoformat()
    obj["empreinte"] = empreinte(obj)
    return obj


def sceller(obj):
    """Recalcule l'empreinte ; signale si un objet validé a changé depuis sa validation."""
    e = empreinte(obj)
    change = obj.get("empreinte") not in (None, e) and obj.get("statut") in ("valide", "verrouille")
    obj["empreinte"] = e
    return change


if __name__ == "__main__":
    for nom in ("plans", "repliques", "faits", "personnages", "continuite", "assets", "decisions"):
        p = DONNEES / f"{nom}.json"
        if p.exists():
            d = lire(nom)
            liste = d if isinstance(d, list) else d.get("elements", [])
            print(f"{nom:12} {len(liste):4} objets · " + " · ".join(f"{s}={sum(1 for x in liste if x.get('statut') == s)}" for s in STATUTS))
