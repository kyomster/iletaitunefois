# Importer un épisode dans Novelcrafter

Mode d'emploi générique, écrit sur S01E01 des *Découvreurs* (les manuscrits sont dans `iletaitunefois/S01E01/novelcrafter/`).

**25 août 2026.**

## Deux manuscrits, et lequel importer

Le dossier contient **deux** versions du même épisode. Elles ne servent pas à la même chose et l'une n'annule pas l'autre.

| Fichier | Ce que c'est | Quand l'importer |
|---|---|---|
| `S01E01-prose-novelcrafter.md` | **Le roman.** 27 000 mots de prose narrative, 79 scènes. Le texte dit y est intact, tout le reste est écrit. | **C'est celui qu'on importe pour travailler le texte.** |
| `S01E01-manuscrit-novelcrafter.md` | **Le document de fabrication.** Les 79 fiches techniques telles quelles, lieu, cadre, action, raccords, interdits. | Seulement si vous voulez le découpage image par image dans Novelcrafter. |

Les deux ont la même charpente : **3 actes, 12 chapitres, 79 scènes**, et la scène *n* est le plan *n* dans les deux. La concordance entre le roman et le découpage, c'est donc l'ordre lui même.

Les autres fichiers :

| Fichier | Rôle |
|---|---|
| `S01E01-codex-novelcrafter.md` | Ne s'importe pas. 19 entrées de Codex prêtes à coller à la main. |
| `CHARTE-prose-S01E01.md` | La voix du roman, en sept sections. À relire avant d'écrire une scène. |
| `build_novelcrafter.py` | Régénère le manuscrit **technique** depuis le scénario. |
| `verifier_prose_novelcrafter.py` | Contrôle le manuscrit **narratif**. |

---

## La procédure d'import

1. Page d'accueil de Novelcrafter, bouton **import**.
2. Format **markdown**.
3. Choisir `S01E01-prose-novelcrafter.md`.
4. Importer **comme prose**, pas comme résumés de scène. Les résumés ne prennent qu'un résumé par chapitre : le découpage en 79 scènes serait perdu.
5. **Preview Import**, puis vérifier le compte annoncé : **3 actes, 12 chapitres, 79 scènes**. Si le compte diffère, ne pas confirmer, lancer le vérificateur et lire les anomalies.
6. **Confirm Import**.
7. Saisir le Codex : les trois lieux d'abord, puis les personnages, puis les objets, puis le savoir.

Navigateur : Chrome ou Firefox. Safari en version 16.5 au moins.

---

## La cartographie

Novelcrafter ne connaît que trois marques.

| Novelcrafter | Marque | Ce qu'on y met |
|---|---|---|
| Acte | `#` | Les trois mouvements du récit |
| Chapitre | `##` | Les douze séquences |
| Scène | la ligne `***` | Les 79 plans, un par scène |

| Acte | Scènes | Ce qui s'y joue |
|---|---|---|
| I — L'épreuve et la règle du jeu | 1 à 15 | Garnerin monte, coupe, et le récit se dérobe. Sam renverse la sacoche, Elio impose la règle. |
| II — L'inventaire | 16 à 52 | Les premiers inventeurs, l'agriculture, le harnais, l'étrier, la liste vérifiée, le vol, le pont. Du sol au ciel puis au vide. |
| III — Le verdict et la morale | 53 à 79 | Et si la corde casse ? Le parachute, le retour au parc, le verdict, le papier, la poudre, la morale. |

Chaque scène s'ouvre sur son **titre en gras**, court, sans le mot plan ni numéro. Novelcrafter nommera les scènes « Scene 1, 2, 3 » ; le titre en gras reste lisible dans la carte de scène. Vous pouvez renommer dans l'application.

---

## Ce que garantit le roman

**Le texte dit est intact.** Les 106 répliques verrouillées du scénario sont reproduites à l'octet près entre guillemets français, dans l'ordre du découpage. Rien n'a été reformulé, rien n'a été coupé en deux, aucun personnage ne dit une phrase qui ne soit au scénario. **Les voix ElevenLabs déjà enregistrées restent donc valides.**

**Le jargon a disparu.** Aucune occurrence de plan, cadre, raccord, contrechamp, caméra, plongée, décor, désaturé, palette ou registre, hors des répliques verrouillées elles mêmes. La consigne technique est devenue sensation.

**La bible de plateau est respectée sans être récitée.** Naya reste à gauche, Elio à droite, Sam au fond au centre, la sacoche du côté d'Elio. Le pansement est sur la main droite. Il n'existe qu'une seule nacelle. Personne ne dit le mot parachute avant que Lenormand ne le forge.

**L'horloge des neuf objets tourne.** À chaque retour dans la pièce, la table porte exactement les objets non encore rangés, jusqu'au bois nu de l'avant dernière scène.

---

## Vérifier après une retouche

**Le roman est écrit, pas généré.** Aucun script ne peut le refabriquer : si vous l'éditez, la seule sécurité est le vérificateur.

```
python ecriture/novelcrafter/verifier_prose_novelcrafter.py
```

Il contrôle les 106 répliques, leur ordre, la charpente, l'absence de jargon, l'absence de tiret court, et signale les scènes trop courtes. Il rend un code d'erreur si quelque chose cloche.

Le manuscrit technique, lui, se régénère :

```
python ecriture/novelcrafter/build_novelcrafter.py
```

---

## Le point ouvert

L'alerte du plan 34 voyage avec les deux manuscrits : la réplique verrouillée range « l'étrier », qui n'est pas l'un des neuf objets. Traitement retenu dans le roman comme dans le découpage : **rien ne quitte la table à cette scène, la phrase est rhétorique.** Consigné aussi dans l'entrée de Codex **Le jeu de la sacoche**, en attendant votre arbitrage.
