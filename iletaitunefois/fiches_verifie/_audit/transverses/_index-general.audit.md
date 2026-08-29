# Audit — _index-general.md

> **Document source** : `fiches/_index-general.md` · **Document vérifié** : `fiches_verifie/_index-general.md`
> **Vérifié le** : 2026-08-07 · **Campagne** : réactualisation à l'état des connaissances de 2026 · **Nature** : document transverse, point d'entrée du dossier

## Bilan

| Faits sur le monde contrôlés | ✅ confirmés | ⚠️ imprécis ou simplifiés | ❌ erronés | 🕰️ dépassés | ❓ non tranchés |
|---|---|---|---|---|---|
| 0 — document descriptif du corpus | — | — | — | — | — |

## Corrections appliquées

**Aucune correction factuelle** : ce document décrit le dossier, pas le monde. **C'est en revanche le seul transverse dont le corps a dû être modifié**, parce qu'il énonce des règles de méthode qui **ne sont plus vraies dans ce répertoire**. Trois passages ont donc été remplacés, et deux sections ajoutées.

| # | Section | Texte d'origine | Nature | Nouveau texte |
|---|---|---|---|---|
| 1 | Chapeau | « Tout est établi à partir des transcriptions audio des épisodes, **et de rien d'autre**. » | **Devenu faux dans ce répertoire** | La description du corpus vient toujours des transcriptions ; **les faits sur le monde ont été vérifiés et corrigés**, et **le propos littéral des épisodes est conservé intact dans `fiches/`**. |
| 2 | Deux principes de méthode → *Fidélité* | « La fiche restitue ce que l'épisode *dit*, jamais ce qu'on sait par ailleurs. » | **Volontairement inversé pour cinq sections sur onze** | La règle est explicitée dans les deux sens : `Sujet`, `Histoire complète`, `Faits énoncés`, `Dates clefs` et `Pistes de réemploi` sont **réécrites à l'état 2026** ; `Personnages`, `Découpage séquentiel`, `Gags`, `Répliques marquantes`, `Procédés narratifs & ton` et `Réserves sur la source` restent **la fidélité pure, à l'octet près**. La nécessité est rappelée : **les transcripts n'étant plus consultables en local, ces six sections sont désormais la seule trace de ce que l'épisode dit littéralement.** |
| 3 | Comment est faite une fiche | « **Onze sections**, dans cet ordre » | **Douze dans ce répertoire** | Mention de l'ajout, et **une ligne de tableau supplémentaire décrivant `## Ce que l'on sait depuis`**. |
| 4 | État du dossier | Bilan de la campagne de rédaction initiale + l'avertissement sur `decouvreurs/S01E22_marie-curie.md` | **Remplacé** | **« État du dossier vérifié »** : volumétrie de la campagne 2026 (208 fiches, 6 855 faits contrôlés, répartition des statuts, conformité structurelle 208/208, intégrité de `fiches/` 223/223), liste des contrôles mécaniques passés, et rappel de la doctrine sur les points non tranchés. |
| 5 | *(nouvelle)* | — | **Ajout** | **« Les deux versions du dossier »** : tableau comparant `fiches/` et `fiches_verifie/`, règle pratique — **le récit vient de la première, les faits de la seconde** — et mode d'emploi d'une fiche vérifiée (en-tête, incises entre crochets, section finale, audit). |
| 6 | En-tête | — | **Ajout** | Blockquote de vérification sous le `# H1`. |

**L'avertissement sur `decouvreurs/S01E22_marie-curie.md`** — la mention de 1934 dans une correction entre crochets, année absente du transcript — **n'a plus lieu d'être dans ce répertoire** : la fiche vérifiée assume et généralise ce type d'annotation, qui y est devenu la règle et non l'exception. Il reste consigné dans la version d'origine.

### Ce qui n'a pas été touché

- Le tableau **des six séries** et celui **des documents transverses** : les chemins et les noms de fichiers sont identiques dans les deux répertoires, **les renvois résolvent donc sans réécriture**.
- La section **« À quoi sert ce dossier »**, la section **« Par où commencer »**, le tableau **« Le dossier en chiffres »** et la **« Note commune sur les transcriptions »** : inchangés.

### Propagation

- Ce document est le **point d'entrée** : c'est lui qui doit dire au lecteur qu'il se trouve dans la version réactualisée et non dans la version fidèle. C'est le seul endroit du dossier où cette distinction est posée en entier.
- Le renvoi vers `_index-verification.md` y est introduit ; ce récapitulatif de campagne reste à produire.

## Non tranché

- Le tableau **« Le dossier en chiffres »** repose sur des mesures faites depuis les transcripts — volume de dialogue analysé, temps sans parole, comptages. **Ces mesures n'ont pas pu être revérifiées**, les transcripts ayant été uploadés sur S3 puis supprimés en local. Elles sont reprises telles quelles.

## Apports 2026

- **La distinction entre les deux répertoires est désormais explicite**, avec sa règle d'usage : **le récit vient de `fiches/`, les faits de `fiches_verifie/`**.
- **La règle de fidélité est énoncée dans les deux sens**, section par section — ce qui était indispensable, puisqu'elle s'applique encore intégralement à six sections sur douze.
- **Le bilan chiffré de la campagne** est donné dès le point d'entrée : 208 fiches, 6 855 faits contrôlés, 49,4 % confirmés, 11,2 % erronés, conformité structurelle 208/208, et **223/223 empreintes intactes sur `fiches/`**.

## Recherches effectuées

**Aucune.** Document descriptif du dossier ; les chiffres proviennent de l'agrégation des 208 audits et des six synthèses de série.
