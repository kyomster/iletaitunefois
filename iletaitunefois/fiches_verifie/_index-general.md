# *Il était une fois…* — index général du dossier

> **Document source** : `fiches/_index-general.md` · **Vérifié le** : 2026-08-07 · **Audit** : `_audit/transverses/_index-general.audit.md`
> ⚠️ Document **transverse réactualisé** : la description du corpus est inchangée et fait toujours autorité ; les renvois pointent désormais vers les fiches vérifiées, et une section de vérification a été ajoutée en fin de document. Le document d'origine est conservé dans `fiches/`, inchangé.

Point d'entrée. **208 fiches d'épisode** couvrant **six séries**, plus quinze documents transverses. **Ce répertoire est la version réactualisée à l'état des connaissances de 2026** : la description du corpus vient des transcriptions audio des épisodes, les faits sur le monde ont été vérifiés et corrigés, et **le propos littéral des épisodes est conservé intact dans `fiches/`**.

---

## À quoi sert ce dossier

Donner à un scénariste tout ce qu'il faut pour **écrire un nouvel épisode dans l'univers** : qui parle, ce qu'on apprend, comment c'est raconté, ce qui fait rire, et ce que chaque série ne fait jamais.

Un transcript brut n'est pas exploitable : les locuteurs y sont anonymes (`LOCUTEUR 3`), les faits pédagogiques sont noyés dans le dialogue, et la structure du format n'apparaît pas. Chaque fiche reconstitue tout cela.

---

## Les six séries

| Série | Année | Épisodes | Fiches | Index | Fiche de série |
|---|---|---|---|---|---|
| **l'Homme** | 1978 | 26 × ~26 min | `homme/` — 26 | [index](_index-homme.md) | [série](_serie-homme.md) |
| **la Vie** | 1987 | 26 × ~25 min | `vie/` — 26 | [index](_index-vie.md) | [série](_serie-vie.md) |
| **les Découvreurs** | 1994 | 26 × ~26 min | `decouvreurs/` — 26 | [index](_index-decouvreurs.md) | [série](_serie-decouvreurs.md) |
| **les Explorateurs** | 1996 | 26 × ~26 min | `explorateurs/` — 26 | [index](_index-explorateurs.md) | [série](_serie-explorateurs.md) |
| **ces drôles d'objets** | — | 26 × 3 sujets de 6 min 40 | `objets/` — 78 | [index](_index-objets.md) | [série](_serie-objets.md) |
| **notre Terre** | 2008 | 26 × ~24 min | `terre/` — 26 | [index](_index-terre.md) | [série](_serie-terre.md) |

---

## Les documents transverses

| Fichier | Contenu |
|---|---|
| [`_index-general.md`](_index-general.md) | **Ce document** — entrée générale |
| [`_bible-personnages.md`](_bible-personnages.md) | Le cast récurrent des six séries : identité, fonction, tics, running gags, contraintes de continuité |
| [`_liens-entre-series.md`](_liens-entre-series.md) | Filiation des formats, sujets traités plusieurs fois, motifs partagés, **les cinq finals spatiaux** |
| `_index-<série>.md` × 6 | Tableau épisode par épisode, regroupements thématiques, dispositifs particuliers |
| `_serie-<série>.md` × 6 | Format, écosystème, état d'esprit, grammaire comique, check-list d'écriture |

---

## Comment est faite une fiche

Onze sections, dans cet ordre — les deux dernières sont conditionnelles. **Dans ce répertoire, une douzième a été ajoutée en fin de fiche : `## Ce que l'on sait depuis`.**

| Section | Ce qu'elle contient |
|---|---|
| **En-tête** | Série, durée, transcript source, avertissements ⚠️ *(titre reconstitué, générique hors périmètre, changement de registre)* |
| `## Sujet` | 2 à 4 phrases : l'angle retenu, ce que l'épisode veut faire comprendre |
| `## Personnages` | Tableau `Transcript · Personnage · Statut · Rôle · Traits`. Statut = **(nommé)** + timecode · **(récurrent)** + épisode de référence · *(non nommé)* |
| `## Histoire complète` | Le récit continu, avec les répliques dans l'ordre |
| `## Découpage séquentiel` | Tableau `Timecode · Séquence · Contenu` — donne le rythme du format |
| `## Faits énoncés` | Toutes les affirmations pédagogiques, **telles que l'épisode les énonce**, avec timecode |
| `## Dates clefs` | Tableau chronologique |
| `## Gags` *(conditionnel)* | Mécanique + timecode ; les gags de série sont marqués **[running gag]** |
| `## Répliques marquantes` | Citations **exactes**, avec locuteur et timecode |
| `## Procédés narratifs & ton` | Mécaniques récurrentes, registre, public visé |
| `## Pistes de réemploi` | Angles non traités, personnages sous-exploités, amorces de scénario |
| `## Réserves sur la source` *(conditionnel)* | Regroupements de diarisation, mots mal transcrits, incohérences internes |
| `## Ce que l'on sait depuis` **(ajout 2026)** | L'apport net de 2026 sur le sujet de l'épisode : découvertes, révisions, consensus déplacé. **La matière neuve, et la plus directement exploitable.** |

### Deux principes de méthode

**Fidélité — et sa révision dans ce dossier.** Dans `fiches/`, la fiche restitue ce que l'épisode *dit*, jamais ce qu'on sait par ailleurs. **Dans `fiches_verifie/`, cette règle a été volontairement inversée pour cinq sections sur onze** : `Sujet`, `Histoire complète`, `Faits énoncés`, `Dates clefs` et `Pistes de réemploi` sont réécrites à l'état des connaissances de 2026, et une douzième section, `Ce que l'on sait depuis`, a été ajoutée en fin de fiche.

**Les six autres sections restent la fidélité pure, à l'octet près** : `Personnages`, `Découpage séquentiel`, `Gags`, `Répliques marquantes`, `Procédés narratifs & ton`, `Réserves sur la source`. **Aucun caractère n'y a été changé.** C'est une nécessité et non une élégance : **les transcripts ne sont plus consultables en local**, et ces sections sont désormais la seule trace de ce que l'épisode dit littéralement.

Quand une correction est appliquée, la formulation d'origine est rappelée en incise — *[l'épisode dit X]* — pour que le scénariste sache exactement ce qu'il ne peut pas réutiliser tel quel. **Une correction n'est écrite que si elle a été confirmée par recherche et sourcée dans l'audit correspondant.**

**Étanchéité entre séries.** Chaque fiche analyse son épisode **comme s'il était seul au monde** — aucune référence aux autres séries. Tous les rapprochements sont rassemblés dans [`_liens-entre-series.md`](_liens-entre-series.md) et [`_bible-personnages.md`](_bible-personnages.md).

---

## Par où commencer

**Pour écrire un épisode dans une série donnée** → sa fiche de série (`_serie-*.md`), qui se termine par une check-list en dix points, puis son index pour choisir l'épisode de référence.

**Pour un personnage** → [`_bible-personnages.md`](_bible-personnages.md), section « Répartition des fonctions ».

**Pour un sujet déjà traité ailleurs** → [`_liens-entre-series.md`](_liens-entre-series.md), section 3.

**Pour une idée neuve** → les sections « Pistes de réemploi » des fiches, et la section 7 de `_liens-entre-series.md`.

---

## Le dossier en chiffres

| | |
|---|---|
| Fiches d'épisode | **208** |
| Documents transverses | **15** |
| Épisodes transcrits | **156** *(dont 26 découpés en 78 sujets)* |
| Volume de dialogue analysé | **~565 000 mots** |
| Série la plus muette | *l'Homme* — **12 min 30 sans parole** par épisode |
| Série la plus bavarde | *notre Terre* — **16 min de parole** sur 24 |
| Série au décor fixe | *la Vie* — 26 épisodes dans le même corps |
| Série la moins nommée | *les Explorateurs* — **2 noms de troupe** sur 26 épisodes |
| Seul épisode sans Maestro | *les Découvreurs* E20 (Ford) |
| Seul narrateur qui se dédit | *les Explorateurs* E09 (Colomb) |
| Morts de Maestro | **2** — *l'Homme* E02, *la Vie* E18 |
| Séries qui finissent dans l'espace | **5 sur 6** |

---

## Note commune sur les transcriptions

Les transcriptions regroupent les répliques **par voix de comédien**, pas par personnage. Un même `LOCUTEUR n` incarne couramment quatre à sept rôles dans un épisode, et la voix du narrateur migre d'un locuteur à l'autre en cours de route. **Un même locuteur porte régulièrement les deux côtés d'un dialogue** — cas d'école : *notre Terre* E15, où l'agriculteur industriel et l'agriculteur bio, les deux thèses opposées de l'épisode, sont sur la même voix.

***Les Explorateurs* sont la série la plus dégradée du dossier** : les rôles y **permutent en cours d'épisode** (Colomb devient Martín Pinzón sur le même locuteur en E09, Livingstone est porté par quatre locuteurs successifs en E21), les noms propres apparaissent sous plusieurs graphies dans un même épisode, et **aucun fichier source ne porte de titre** — tous les titres du dossier sont reconstitués et signalés comme tels.

Chaque fiche signale ces regroupements dans « Réserves sur la source » et reconstitue les rôles d'après le contenu des répliques.

**Le tableau « Personnages » de chaque fiche fait autorité sur le transcript brut.**

---

---

## Les deux versions du dossier

Ce dossier existe désormais en **deux versions parallèles, de même arborescence et de mêmes noms de fichiers**.

| | `fiches/` | `fiches_verifie/` |
|---|---|---|
| Ce qu'elle contient | **Ce que les épisodes disent** | **Ce que l'on sait en 2026** |
| Statut | **Lecture seule, jamais modifiée** | Version de travail du scénariste |
| Fait autorité sur | le propos littéral des épisodes | l'état des connaissances |
| Sections factuelles | telles que l'épisode les énonce | réécrites et sourcées |
| Sections descriptives de la source | l'original | **identiques à l'octet** |
| Section supplémentaire | — | `## Ce que l'on sait depuis` |
| Traçabilité | — | un audit par fiche dans `_audit/` |

**Les deux sont nécessaires, et pour des raisons opposées.** Pour écrire *dans le ton* de la série, il faut savoir ce qu'elle affirme : c'est `fiches/`. Pour ne pas reconduire ses erreurs, il faut savoir ce qui est vrai : c'est `fiches_verifie/`. **La règle pratique est simple — le récit vient de la première, les faits de la seconde.**

### Comment lire une fiche vérifiée

- **L'en-tête** porte la date de vérification et le chemin de son audit.
- **Les incises en italique entre crochets** — *[l'épisode dit X]* — signalent chaque endroit où la série diverge de l'état des connaissances. **Ce sont les points à ne pas réutiliser tels quels.**
- **La section finale `Ce que l'on sait depuis`** rassemble l'apport net de 2026 sur le sujet : c'est la matière neuve, et la plus directement exploitable.
- **L'audit correspondant**, dans `_audit/<série>/`, donne pour chaque correction l'énoncé d'origine, le statut, l'état 2026, la source et le degré de confiance — ainsi que **les points restés non tranchés**, qui n'ont volontairement pas été corrigés.

---

## État du dossier vérifié

**Terminé** — **les 208 fiches réactualisées, les 208 audits, les 6 synthèses de série et les 15 documents transverses.**

| Indicateur | Valeur |
|---|---|
| Fiches réactualisées | **208 / 208** |
| Audits produits | **208** + **6 synthèses de série** |
| Faits contrôlés | **6 855** |
| ✅ Confirmés | **49,4 %** |
| ⚠️ Imprécis ou simplifiés | **24,6 %** |
| ❌ Erronés | **11,2 %** |
| 🕰️ Dépassés depuis la diffusion | **8,4 %** |
| ❓ Non tranchés | **6,4 %** |
| Volume | 42 849 → **49 115 lignes** (+14,6 %) |
| Conformité structurelle | **208 / 208**, zéro anomalie |
| Intégrité de `fiches/` | **223 / 223** empreintes identiques |

**Contrôle mécanique passé sur les 208 fiches** : les onze sections dans l'ordre canonique, `Ce que l'on sait depuis` en douzième position, les six sections préservées identiques à l'octet, l'en-tête de vérification présent et daté, aucune URL, aucun émoji de statut, aucun marqueur de remplissage, et aucune fiche plus courte que sa source.

**Les vingt-quatre points restés indécidables** — répartis sur les six séries — **n'ont pas été corrigés** : la fiche conserve alors le propos de l'épisode et l'audit consigne ce qui manque pour trancher. **Corriger à tort est pire que ne pas corriger.**

> Le récapitulatif complet de la campagne est dans [`_index-verification.md`](_index-verification.md) ; le détail série par série dans les six synthèses de `_audit/`.
