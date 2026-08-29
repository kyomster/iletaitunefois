# -*- coding: utf-8 -*-
"""
Vérifie le manuscrit narratif iletaitunefois/S01E01/novelcrafter/S01E01-prose-novelcrafter.md.

Ce manuscrit est ÉCRIT, pas généré : aucun script ne peut le refabriquer. Il
n'existe donc qu'un seul filet de sécurité, celui ci. À lancer après toute
retouche du manuscrit, et après toute modification du scénario source.

CE QU'IL CONTRÔLE
  1. les 106 répliques verrouillées du scénario sont présentes VERBATIM ;
  2. elles apparaissent dans l'ordre du découpage, jamais permutées ;
  3. la structure que Novelcrafter sait lire : 3 actes, 12 chapitres, 79 scènes ;
  4. aucun titre de niveau 3, aucun tableau, aucune image, aucun sommaire ;
  5. aucun mot de fabrication hors des répliques verrouillées ;
  6. aucun tiret court, règle typographique de la maison ;
  7. la longueur des scènes, pour repérer un creux.

  python ecriture/novelcrafter/verifier_prose_novelcrafter.py
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SCENARIO = RACINE / "iletaitunefois" / "S01E01" / "scenario.md"
PROSE = RACINE / "iletaitunefois" / "S01E01" / "novelcrafter" / "S01E01-prose-novelcrafter.md"

MOTS_BANNIS = [
    "plan", "cadre", "hors cadre", "raccord", "contrechamp", "caméra",
    "contre plongée", "plongée", "gros plan", "vignette", "clip",
    "image clé", "décor", "interdits", "désaturé", "saturé", "palette",
    "registre", "champ contrechamp", "image fixe",
]


def repliques_du_scenario() -> list[tuple[int, str]]:
    lignes = SCENARIO.read_text(encoding="utf-8").split("\n")
    debut = next(i for i, l in enumerate(lignes) if l.startswith("## Découpage détaillé"))
    fin = next(i for i, l in enumerate(lignes) if l.startswith("## Minutage récapitulatif"))

    sortie: list[tuple[int, str]] = []
    numero = None
    for ligne in lignes[debut + 1 : fin]:
        m = re.match(r"^#### Plan (\d+) — ", ligne)
        if m:
            numero = int(m.group(1))
            continue
        if numero and ligne.startswith("**Texte dit (verrouillé)**"):
            dit = ligne.split(":", 1)[1].strip() if ":" in ligne else ""
            if dit.startswith("—"):
                continue
            for rep in re.findall(r"«[^»]*»", dit):
                sortie.append((numero, rep))
    return sortie


def main() -> int:
    if not PROSE.exists():
        raise SystemExit(f"Introuvable : {PROSE}")

    prose = PROSE.read_text(encoding="utf-8")
    lignes = prose.split("\n")
    anomalies: list[str] = []

    # 1 et 2 : la zone verrouillée
    attendues = repliques_du_scenario()
    manquantes = [(n, r) for n, r in attendues if r not in prose]
    for n, r in manquantes:
        anomalies.append(f"réplique du plan {n} absente ou altérée : {r[:70]}")

    # L'ordre se vérifie avec un curseur qui avance, jamais avec une recherche
    # depuis le début : une réplique courte comme « Gel. » revient cinq fois
    # dans l'épisode, et une recherche naïve retrouverait toujours la première.
    curseur = 0
    desordre: list[int] = []
    for n, rep in attendues:
        if rep not in prose:
            continue
        trouve = prose.find(rep, curseur)
        if trouve == -1:
            desordre.append(n)
        else:
            curseur = trouve + len(rep)
    if desordre:
        anomalies.append(f"répliques hors séquence, aux plans {sorted(set(desordre))}")

    # 3 : la structure Novelcrafter
    actes = [l for l in lignes if re.match(r"^# ", l)]
    chapitres = [l for l in lignes if re.match(r"^## ", l)]
    separateurs = [l for l in lignes if l.strip() == "***"]
    titres = [l for l in lignes if re.match(r"^\*\*[^*].*\*\*$", l)]
    scenes = len(separateurs) + len(chapitres)

    if len(actes) != 3:
        anomalies.append(f"{len(actes)} actes au lieu de 3")
    if len(chapitres) != 12:
        anomalies.append(f"{len(chapitres)} chapitres au lieu de 12")
    if scenes != 79:
        anomalies.append(f"{scenes} scènes au lieu de 79")
    if len(titres) != 79:
        anomalies.append(f"{len(titres)} titres de scène au lieu de 79")

    mal_isoles = [i + 1 for i, l in enumerate(lignes)
                  if l.strip() == "***" and (lignes[i - 1].strip() or lignes[i + 1].strip())]
    if mal_isoles:
        anomalies.append(f"séparateurs non entourés de lignes vides, lignes {mal_isoles[:5]}")

    # 4 : ce que Novelcrafter refuse
    for ligne in lignes:
        if re.match(r"^#{3,} ", ligne):
            anomalies.append(f"titre de niveau 3 ou plus : {ligne[:60]}")
        if ligne.lstrip().startswith("|"):
            anomalies.append(f"tableau : {ligne[:60]}")
    if "![" in prose:
        anomalies.append("image en ligne dans le manuscrit")

    # 5 : le jargon, hors verbatim
    hors_verbatim = prose
    for _, rep in attendues:
        hors_verbatim = hors_verbatim.replace(rep, "«»")
    trouves: collections.Counter = collections.Counter()
    for ligne in hors_verbatim.split("\n"):
        if ligne.strip().startswith("#"):
            continue
        for mot in MOTS_BANNIS:
            n = len(re.findall(r"\b" + re.escape(mot) + r"\b", ligne, re.I))
            if n:
                trouves[mot] += n
    for mot, n in trouves.items():
        anomalies.append(f"mot de fabrication « {mot} », {n} fois hors verbatim")

    # 6 : le tiret court
    if "-" in prose:
        lignes_tiret = [i + 1 for i, l in enumerate(lignes) if "-" in l]
        anomalies.append(f"tiret court présent, lignes {lignes_tiret[:8]}")

    # 7 : la longueur des scènes
    blocs = re.split(r"\n\*\*[^*\n]+\*\*\n", "\n" + prose)[1:]
    longueurs = sorted(len(b.split()) for b in blocs)

    print("Manuscrit narratif — vérification\n")
    print(f"  actes                 : {len(actes)}")
    print(f"  chapitres             : {len(chapitres)}")
    print(f"  scènes                : {scenes}")
    print(f"  répliques verrouillées : {len(attendues) - len(manquantes)} sur {len(attendues)}")
    print(f"  mots                  : {len(prose.split()):,}".replace(",", " "))
    if longueurs:
        med = longueurs[len(longueurs) // 2]
        print(f"  scènes, en mots       : min {longueurs[0]}, médiane {med}, max {longueurs[-1]}")

    if anomalies:
        print("\nANOMALIES :")
        for a in anomalies:
            print(f"  - {a}")
        return 1

    print("\nRien à signaler.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
