# -*- coding: utf-8 -*-
"""
Convertit iletaitunefois/S01E01/scenario.md en un manuscrit importable dans Novelcrafter.

CE QUE NOVELCRAFTER SAIT LIRE, et rien d'autre :
  * titre de niveau 1  -> un ACTE
  * titre de niveau 2  -> un CHAPITRE
  * la ligne « *** »   -> un separateur de SCENE a l'interieur du chapitre
  * tout le reste      -> de la prose, versee telle quelle dans la scene courante

CE QU'IL REFUSE OU DIGERE MAL, et que ce script retire donc du manuscrit :
  * un sommaire, qui fait rejeter le document entier
  * les images en ligne, non supportees
  * les tableaux, qui n'ont pas de place dans une scene
  * les titres de niveau 3 et plus, qui ne creent aucun niveau et se perdent

CARTOGRAPHIE RETENUE (arbitrage du 25 aout 2026)
  3 actes  = les trois mouvements du recit
  12 chapitres = les douze sequences du decoupage
  79 scenes = les 79 plans, separes par « *** »

Le titre du plan ne peut pas rester un titre : il deviendrait invisible.
Il devient donc la PREMIERE LIGNE EN GRAS de la scene, ce qui le rend
lisible dans la carte de scene de la vue Plan.

ZONE VERROUILLEE. Le texte dit n'est jamais reformate ni reindente : le
script le recopie a l'octet pres et verifie l'empreinte a la sortie.

  python ecriture/novelcrafter/build_novelcrafter.py
  python ecriture/novelcrafter/build_novelcrafter.py --verifier
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SOURCE = RACINE / "iletaitunefois" / "S01E01" / "scenario.md"
SORTIE = RACINE / "iletaitunefois" / "S01E01" / "novelcrafter" / "S01E01-manuscrit-novelcrafter.md"

DEBUT_DECOUPAGE = "## Découpage détaillé"
FIN_DECOUPAGE = "## Minutage récapitulatif"

# Les trois actes, par le premier plan de chaque acte.
# Acte I  : l'epreuve est posee et la regle du jeu est fixee.
# Acte II : l'inventaire, du sol vers le ciel puis vers le vide.
# Acte III: la corde peut casser, donc le parachute, donc le verdict, donc la morale.
ACTES = [
    (1, "Acte I — L'épreuve et la règle du jeu"),
    (16, "Acte II — L'inventaire"),
    (53, "Acte III — Le verdict et la morale"),
]

RE_SEQUENCE = re.compile(r"^### (.+)$")
RE_PLAN = re.compile(r"^#### Plan (\d+) — (.+)$")
RE_TEXTE_DIT = re.compile(r"^\*\*Texte dit \(verrouillé\)\*\*")


class Plan:
    def __init__(self, numero: int, titre: str):
        self.numero = numero
        self.titre = titre
        self.corps: list[str] = []


class Sequence:
    def __init__(self, titre: str):
        self.titre = titre
        self.plans: list[Plan] = []


def lire_decoupage(texte: str) -> list[Sequence]:
    """Isole la zone de decoupage et la decompose en sequences puis en plans."""
    lignes = texte.split("\n")

    depart = next(i for i, l in enumerate(lignes) if l.startswith(DEBUT_DECOUPAGE))
    arret = next(i for i, l in enumerate(lignes) if l.startswith(FIN_DECOUPAGE))
    zone = lignes[depart + 1 : arret]

    sequences: list[Sequence] = []
    plan_courant: Plan | None = None

    for ligne in zone:
        m_seq = RE_SEQUENCE.match(ligne)
        if m_seq:
            sequences.append(Sequence(m_seq.group(1).strip()))
            plan_courant = None
            continue

        m_plan = RE_PLAN.match(ligne)
        if m_plan:
            if not sequences:
                raise SystemExit("Plan rencontré avant toute séquence : structure inattendue.")
            plan_courant = Plan(int(m_plan.group(1)), m_plan.group(2).strip())
            sequences[-1].plans.append(plan_courant)
            continue

        # Hors d'un plan, on est dans la note de tete du decoupage : elle
        # appartient a la methode, pas au recit, donc elle ne part pas.
        if plan_courant is not None:
            plan_courant.corps.append(ligne)

    return sequences


def nettoyer(corps: list[str]) -> list[str]:
    """Retire les lignes vides de tete et de queue, et toute ligne de tableau."""
    propre = [l for l in corps if not l.lstrip().startswith("|")]
    while propre and not propre[0].strip():
        propre.pop(0)
    while propre and not propre[-1].strip():
        propre.pop()
    return propre


def titre_acte(numero_plan: int) -> str | None:
    for premier, titre in ACTES:
        if numero_plan == premier:
            return titre
    return None


def assembler(sequences: list[Sequence]) -> str:
    sortie: list[str] = []
    for sequence in sequences:
        if not sequence.plans:
            continue

        acte = titre_acte(sequence.plans[0].numero)
        if acte:
            sortie.append(f"# {acte}")
            sortie.append("")

        # Le titre de sequence porte deja sa plage de plans ; on la garde,
        # elle sert de reperage dans la barre laterale.
        sortie.append(f"## {sequence.titre}")
        sortie.append("")

        for rang, plan in enumerate(sequence.plans):
            if rang:
                sortie.append("***")
                sortie.append("")
            sortie.append(f"**Plan {plan.numero} — {plan.titre}**")
            sortie.append("")
            sortie.extend(nettoyer(plan.corps))
            sortie.append("")

    return "\n".join(sortie).rstrip("\n") + "\n"


def empreinte_zone_verrouillee(texte: str) -> tuple[str, int]:
    """Empreinte des seules lignes de texte dit, dans leur ordre d'apparition."""
    lignes = [l for l in texte.split("\n") if RE_TEXTE_DIT.match(l)]
    brut = "\n".join(lignes).encode("utf-8")
    return hashlib.sha256(brut).hexdigest(), len(lignes)


def verifier(source: str, manuscrit: str, sequences: list[Sequence]) -> list[str]:
    anomalies: list[str] = []

    nb_actes = manuscrit.count("\n# ") + (1 if manuscrit.startswith("# ") else 0)
    nb_chapitres = manuscrit.count("\n## ")
    nb_separateurs = len([l for l in manuscrit.split("\n") if l.strip() == "***"])
    nb_plans = sum(len(s.plans) for s in sequences)
    nb_scenes = nb_separateurs + nb_chapitres  # une scene de plus par chapitre

    if nb_actes != 3:
        anomalies.append(f"{nb_actes} actes au lieu de 3")
    if nb_chapitres != 12:
        anomalies.append(f"{nb_chapitres} chapitres au lieu de 12")
    if nb_plans != 79:
        anomalies.append(f"{nb_plans} plans lus au lieu de 79")
    if nb_scenes != 79:
        anomalies.append(f"{nb_scenes} scènes produites au lieu de 79")

    numeros = [p.numero for s in sequences for p in s.plans]
    if numeros != list(range(1, 80)):
        anomalies.append("la numérotation des plans n'est pas 1 à 79 dans l'ordre")

    for ligne in manuscrit.split("\n"):
        if re.match(r"^#{3,} ", ligne):
            anomalies.append(f"titre de niveau 3 ou plus resté dans le manuscrit : {ligne[:60]}")
        if ligne.lstrip().startswith("|"):
            anomalies.append(f"tableau resté dans le manuscrit : {ligne[:60]}")
        if "![" in ligne:
            anomalies.append(f"image restée dans le manuscrit : {ligne[:60]}")

    empreinte_source, compte_source = empreinte_zone_verrouillee(source)
    empreinte_sortie, compte_sortie = empreinte_zone_verrouillee(manuscrit)
    if empreinte_source != empreinte_sortie:
        anomalies.append("la zone verrouillée a changé, empreintes différentes")
    if compte_source != compte_sortie:
        anomalies.append(f"{compte_sortie} lignes de texte dit au lieu de {compte_source}")

    print(f"  actes           : {nb_actes}")
    print(f"  chapitres       : {nb_chapitres}")
    print(f"  scènes          : {nb_scenes}")
    print(f"  lignes verrouillées : {compte_sortie}")
    print(f"  empreinte SHA256    : {empreinte_sortie[:16]}…")

    return anomalies


def main() -> int:
    if not SOURCE.exists():
        raise SystemExit(f"Introuvable : {SOURCE}")

    source = SOURCE.read_text(encoding="utf-8")
    sequences = lire_decoupage(source)
    manuscrit = assembler(sequences)

    print("Vérification :")
    anomalies = verifier(source, manuscrit, sequences)

    if anomalies:
        print("\nANOMALIES :")
        for a in anomalies:
            print(f"  - {a}")
        return 1

    if "--verifier" in sys.argv:
        print("\nRien écrit, mode vérification.")
        return 0

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(manuscrit, encoding="utf-8")
    mots = len(manuscrit.split())
    print(f"\nÉcrit : {SORTIE.relative_to(RACINE)}")
    print(f"  {len(manuscrit.encode('utf-8')):,} octets, environ {mots:,} mots".replace(",", " "))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
