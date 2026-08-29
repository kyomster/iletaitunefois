# Campagne de vérification 2026 — récapitulatif

> **Périmètre** : les **223 documents** de `fiches/` — 208 fiches d'épisode et 15 transverses — réactualisés à l'état des connaissances de 2026 dans `fiches_verifie/`, avec **223 audits** et **6 synthèses de série**.
> **Campagne** : du **4 août au 7 août 2026** · **Référentiel** : `.claude/workflows/REFERENTIEL.md`
> **Source** : `fiches/`, **jamais modifiée** — intégrité vérifiée à l'empreinte, **223 / 223**.

---

## 1. Ce qui a été produit

| | Documents | Lignes | Mots |
|---|---|---|---|
| **Fiches d'épisode réactualisées** | **208** | 42 849 → **49 115** (+14,6 %) | 1 041 322 → **1 717 439** (+64,9 %) |
| **Documents transverses réactualisés** | **15** | 3 008 → **3 524** (+17,2 %) | 40 070 → **47 482** (+18,5 %) |
| **Audits de fiche** | **208** | 17 936 | 712 582 |
| **Audits de transverse** | **15** | 673 | 8 334 |
| **Synthèses de série** | **6** | 1 573 | 31 679 |
| **Total produit** | **452 fichiers** | **72 020 lignes** | **2 517 516 mots** |

**Arborescence** :

```
fiches/                                   ← INTACTE, 223/223 empreintes identiques
fiches_verifie/
  <série>/<fiche>.md               × 208  ← fiches réactualisées, mêmes noms de fichiers
  _index-*.md  _serie-*.md  …      ×  15  ← transverses réactualisés
  _index-verification.md                  ← ce document
  _audit/
    <série>/<fiche>.audit.md       × 208
    transverses/<doc>.audit.md     ×  15
    _synthese-<série>.md           ×   6
```

---

## 2. Ce qui a été trouvé

**6 855 faits contrôlés** sur les six séries.

| Statut | Nombre | Part |
|---|---|---|
| ✅ **Confirmés** | 3 388 | **49,4 %** |
| ⚠️ **Imprécis ou simplifiés** | 1 715 | **25,0 %** |
| ❌ **Erronés** | 773 | **11,3 %** |
| 🕰️ **Dépassés depuis la diffusion** | 576 | **8,4 %** |
| ❓ **Non tranchés** | **406** | **5,9 %** |

*(Les bilans de quelques audits anciens ne se totalisent pas exactement ; l'écart cumulé est de trois unités sur 6 855.)*

**Un énoncé sur deux est confirmé ; un sur cinq est faux ou dépassé.** C'est le résultat central de la campagne, et il vaut pour l'ensemble du corpus : **les six séries sont globalement fiables sur le récit et régulièrement fautives sur le détail.**

### Par série

| Série | Fiches | Faits | ✅ | ⚠️ | ❌ | 🕰️ | ❓ | Lignes |
|---|---|---|---|---|---|---|---|---|
| ***l'Homme*** (1978) | 26 | 1 044 | **56,9 %** | 21,6 % | 12,1 % | 6,4 % | 3,1 % | 6 415 → 7 230 |
| ***les Explorateurs*** (1996) | 26 | 839 | 54,0 % | 21,7 % | 11,2 % | 10,5 % | 2,6 % | 7 674 → 9 035 |
| ***la Vie*** (1987) | 26 | 846 | 52,1 % | 25,4 % | **9,8 %** | **6,0 %** | 6,6 % | 5 143 → 5 770 |
| ***ces drôles d'objets*** | **78** | **1 538** | 48,8 % | 23,3 % | **12,9 %** | **13,7 %** | **1,3 %** | 12 011 → 14 082 |
| ***les Découvreurs*** (1994) | 26 | 1 360 | 46,4 % | **30,8 %** | 10,8 % | **2,4 %** | 9,6 % | 5 775 → 6 376 |
| ***notre Terre*** (2008) | 26 | 1 228 | **42,3 %** | 25,7 % | 10,1 % | 10,3 % | **11,9 %** | 5 831 → 6 622 |

**Le classement contredit l'intuition, et c'est le résultat le plus intéressant de la campagne.** **La série la plus ancienne est la plus exacte** ; **la plus récente est la moins exacte** ; **et la série d'objets, la moins ancienne du corpus, affiche le plus fort taux d'erreur franche.**

L'explication tient à ce que chaque série avance comme savoir :

- ***l'Homme*** raconte de l'**histoire ancienne bien établie** — trente ans ne l'ont pas beaucoup déplacée, sauf sur la préhistoire de ses trois premiers épisodes, la partie la plus datée du corpus.
- ***la Vie*** raconte des **mécanismes**, qui se vérifient ou se réfutent : d'où le **taux d'erreur franche le plus bas**, mais aussi les fautes les plus graves — **des inversions de fonction**, où le personnage a joué l'inverse de son rôle pendant tout l'épisode.
- ***les Découvreurs*** raconte des **biographies avec une thèse**, et la thèse produit **le plus fort taux d'imprécisions** (30,8 %) : la série arrondit rarement à faux, souvent à peu près.
- ***les Explorateurs*** raconte des **textes anciens dans sa première moitié et de la science fraîche dans la seconde** — d'où un vieillissement par la fin, unique dans le corpus : 59,8 % de confirmations sur les treize premiers épisodes, 47,8 % sur les treize derniers.
- ***ces drôles d'objets*** raconte des **récits d'origine**, précisément le genre de matière où les légendes prospèrent. **Son défaut n'est pas l'âge, c'est la méthode : elle se trompe au présent.**
- ***notre Terre*** raconte de l'**actualité chiffrée**, la matière la plus périssable qui soit : d'où **le plus fort taux de non tranchés** (11,9 %).

> **Le taux de confirmation mesure la périssabilité de la matière, pas le soin de l'écriture.** *Notre Terre* est dernière parce qu'elle a choisi le sujet le plus mouvant.

---

## 3. Les deux motifs fautifs qui traversent tout le corpus

**Premier motif — le « premier » est presque toujours à repartager.** Le corpus entier repose sur des scènes de fondation, et une scène de fondation exige un fondateur. **Chaque fois qu'une série nomme un inventeur, il faut vérifier.**

Quelques cas parmi les plus nets :

- **Le microscope** — l'attribution à Zacharias Janssen repose sur une lettre de **1655** et sur le témoignage d'un fils **né en 1611** se souvenant d'événements de **1590**.
- **La longue-vue** — la demande de brevet de Lippershey, du **2 octobre 1608**, **a été refusée parce que deux autres revendiquaient l'invention**.
- **La caméra** — **Louis Le Prince a filmé à Leeds en octobre 1888**, avant Edison, et **a disparu d'un train en septembre 1890**.
- **L'ordinateur** — **l'ENIAC n'est pas le premier ordinateur électronique** : l'Atanasoff-Berry Computer l'a précédé (le brevet de l'ENIAC a été invalidé en **1973**), et les Colossus fonctionnaient dès **1943**, classés secret trente ans.
- **Les globules rouges** — **Jan Swammerdam les décrit en 1658**, seize ans avant van Leeuwenhoek.
- **Le haut-parleur** — **Siemens l'avait breveté en 1877**, quarante-sept ans avant Rice et Kellogg ; il était inutilisable faute d'amplification.
- **L'« école de Sagres »** — **elle n'a jamais existé** : ni institut, ni observatoire, ni équipe. C'est une construction érudite des XVIIIᵉ-XIXᵉ siècles.

**Second motif — l'effacement des seconds rôles réels.** C'est **le seul défaut que les six séries partagent**.

**Sacagawea** et **York** chez Lewis et Clark · **Ibn Machid**, le pilote qui conduit Vasco de Gama aux Indes · **les six programmeuses de l'ENIAC** — McNulty, Jennings, Snyder, Wescoff, Bilas, Lichterman · **William Dickson**, dont Edison a signé le travail · **Peggy Oki**, membre des Z-Boys et vainqueure à Del Mar en 1975 · **Bertha Benz**, qui invente la garniture de frein pendant son trajet de 1888 · **William Taynton**, garçon de bureau payé une demi-couronne pour être la première personne passée à la télévision.

> **Ce n'est pas de la malveillance : les séries reprennent les récits disponibles, et ces récits les avaient déjà effacés.** Mais le motif est si constant qu'il devient une piste : **la version qui parle n'a jamais été écrite.**

---

## 4. Les fautes les plus lourdes, série par série

| Série | La correction qui compte le plus |
|---|---|
| ***l'Homme*** | **Trois « documents d'archives » cités par la série sont des faux reconnus** : ils ne peuvent servir ni de citation ni de pièce à conviction. Et **le traité d'Utrecht est raconté à l'envers** — c'est la France qui cède. |
| ***la Vie*** | **Le tétanos est une paralysie spastique** : la toxine supprime le frein inhibiteur, elle ne coupe pas la ligne. **L'épisode E22 est construit sur le contresens du début à la fin.** Et **les plaquettes sont montrées deux fois comme fluidifiant le sang** — bloquer est leur métier. |
| ***les Découvreurs*** | **Henri le Navigateur n'a pas combattu la traite : il l'a organisée et il en a vécu** — quint des profits depuis 1433, licence de l'expédition de 1444. **L'épisode dit l'exact contraire.** |
| ***les Explorateurs*** | **L'épisode de clôture est le plus fautif du corpus** : huit énoncés confirmés sur trente-quatre. Tout ce qui était neuf en 1996 a bougé. |
| ***ces drôles d'objets*** | **Quatre légendes reconduites comme des faits** : les bagues à poison de la Renaissance, « hic sunt dracones », le papillon de l'ENIAC, l'étymologie de « drone » par le bourdonnement. **Aucune ne résiste.** |
| ***notre Terre*** | **Les confusions d'entités** : des léopards et des dauphins aveugles en Amazonie, des alligators en Asie du Sud-Est, un babiroussa à Bornéo, des mégalodons chez les dinosaures — quarante millions d'années trop tôt. |

---

## 5. Les 406 points non tranchés

**Ils n'ont pas été corrigés.** La doctrine de la campagne est explicite : *corriger à tort est pire que ne pas corriger*. Quand un doute n'a pas pu être levé, **la fiche conserve le propos de l'épisode** et l'audit consigne ce qui manque pour trancher.

Ils se répartissent très inégalement : **11,9 % des faits de *notre Terre*** contre **1,3 % de ceux de *ces drôles d'objets***. L'écart mesure la difficulté à réancrer, quinze ans après, des chiffres d'actualité que la série avançait sans les sourcer.

Les plus notables : **l'invention du microscope composé** ; **l'existence de la cuiller en magnétite antique** ; **la primauté d'Ada Lovelace comme « premier programmeur »** ; **la nocivité propre des bougies en paraffine** ; **la paternité de la première caméra**.

---

## 6. Contrôle et intégrité

| Contrôle | Résultat |
|---|---|
| Onze sections `##` dans l'ordre canonique | **208 / 208** |
| `Ce que l'on sait depuis` en douzième position, ≥ 4 lignes | **208 / 208** |
| Six sections préservées **identiques à l'octet** | **208 / 208** |
| En-tête de vérification présent et daté | **223 / 223** |
| Absence de `TODO`, `à compléter`, `XXX`, `[…]` hors citation | **223 / 223** |
| Absence d'URL et d'émoji de statut dans les fiches | **223 / 223** |
| Document vérifié jamais plus court que sa source | **223 / 223** |
| Audit présent, ≥ 500 octets, avec bilan chiffré | **223 / 223** |
| **Empreintes md5 de `fiches/`** | **223 / 223 identiques** |

**Les six sections préservées** — `Personnages`, `Découpage séquentiel`, `Gags`, `Répliques marquantes`, `Procédés narratifs & ton`, `Réserves sur la source` — **n'ont pas changé d'un caractère**.

Ce n'est pas une élégance mais une nécessité : **les transcriptions et les vidéos ont été uploadées sur OVH S3 puis supprimées en local**. **Aucune citation, aucun timecode ne peut plus être recoupé contre l'audio.** Ces six sections sont désormais la seule trace de ce que les épisodes disent littéralement, et le tableau `Personnages` reste l'autorité sur les regroupements de diarisation.

---

## 7. Méthode

**Règle de réécriture.** Cinq sections décrivent **le monde** et ont été réactualisées : `Sujet`, `Histoire complète`, `Faits énoncés`, `Dates clefs`, `Pistes de réemploi`. Six décrivent **la source** et ont été préservées. Une douzième a été ajoutée : `Ce que l'on sait depuis`, qui rassemble l'apport net de 2026.

**Règle de sourçage.** **Une correction n'est écrite dans une fiche que si elle a été confirmée par recherche et qu'elle peut être sourcée dans l'audit.** Un doute non levé devient un ❓ et **le texte de la fiche reste inchangé**.

**Traçabilité.** Chaque audit porte un bilan chiffré, un tableau `# · Section · Énoncé de la fiche source · Statut · État 2026 · Source · Confiance`, la liste des points non tranchés, les apports 2026, et les requêtes de recherche effectuées.

**Recherches.** **2 712 requêtes consignées** au total. Le chiffre n'est pas comparable d'une série à l'autre : les trois premières séries traitées (`decouvreurs`, `terre`, `vie`) l'ont été par un workflow multi-agents qui consignait chaque sous-requête, les trois suivantes (`homme`, `explorateurs`, `objets`) en fil principal avec une requête consolidée par épisode. **Le volume de vérification est comparable ; la granularité de comptage ne l'est pas.**

**Coût.** Le pilote mesuré — `decouvreurs/S01E09_galilee.md`, 4 août 2026 — a demandé 34 minutes, 5 agents, environ 390 k tokens et 28 recherches web pour une fiche de 217 lignes, dont 54 faits contrôlés et 24 corrigés.

---

## 8. Comment se servir des deux versions

| | `fiches/` | `fiches_verifie/` |
|---|---|---|
| Ce qu'elle contient | **Ce que les épisodes disent** | **Ce que l'on sait en 2026** |
| Statut | **Lecture seule, jamais modifiée** | Version de travail du scénariste |
| Fait autorité sur | le propos littéral des épisodes | l'état des connaissances |
| Section supplémentaire | — | `## Ce que l'on sait depuis` |
| Traçabilité | — | un audit par document dans `_audit/` |

**La règle pratique est simple : le récit vient de la première, les faits de la seconde.**

Pour écrire *dans le ton* d'une série, il faut savoir ce qu'elle affirme — c'est `fiches/`. Pour ne pas reconduire ses erreurs, il faut savoir ce qui est vrai — c'est `fiches_verifie/`.

**Dans une fiche vérifiée**, les **incises en italique entre crochets** — *[l'épisode dit X]* — signalent chaque endroit où la série diverge de l'état des connaissances : **ce sont les points à ne pas réutiliser tels quels**. La section finale rassemble la matière neuve. L'audit correspondant donne, pour chaque correction, l'énoncé d'origine, sa source et son degré de confiance.

---

## 9. Ce qui reste

- **Les 406 points non tranchés** demanderaient des recherches spécialisées, souvent en langue d'origine — néerlandais du XVIIᵉ siècle pour Janssen et van Leeuwenhoek, chinois ancien pour le *sinan*.
- ~~**Une lacune de traçabilité sur dix fiches de `terre`**~~ — **réparée le 2026-08-07** : les quatorze puces de `Procédés narratifs & ton` concernées portent désormais, dans leur audit, le renvoi à la ligne qui les source. Voir §6.3 de `_audit/_synthese-terre.md`.
- **Les mesures de format du dossier** — durées, volumes de dialogue, temps sans parole, comptages d'occurrences — **n'ont pas pu être revérifiées** et sont reprises telles quelles.

---

---

## 10. Reprise du 7 août 2026 — passe sur les non tranchés

Une seconde passe a porté sur les points restés indécidés de `terre` et de `decouvreurs`, avec **une méthode d'interrogation nouvelle** : appel programmatique à l'API de l'encyclopédie de référence, au lieu de la consultation d'articles devinés.

| Usage | Ce qu'il apporte |
|---|---|
| Recherche plein texte `insource:` | **Retrouve une formule où qu'elle se trouve**, au lieu de deviner l'article. C'est ainsi que le chiffre des cent mille mammifères marins a été localisé — pas dans l'article attendu. |
| Extraction du wikitexte | **Donne la citation d'origine**. C'est là qu'on voit qu'un chiffre planétaire repose sur une page de communication d'ONG. |
| `totalhits: 0` | **Un négatif certain**, portant sur l'encyclopédie entière et non sur un article. Le salaire de Faraday n'est pas absent de sa notice : il est absent du corpus. |

**Trente-cinq points ont été tranchés** — vingt sur `terre`, quinze sur `decouvreurs` — sous le seuil strict : correction écrite seulement si l'énoncé de remplacement est sourcé et non contesté, texte de l'épisode conservé sinon.

**La méthode a été corrigée en cours de passe.** Trois défauts ont été identifiés et redressés : `prop=extracts` **supprime tout appareil de citation**, si bien qu'on ne peut pas lui demander une référence — c'est `action=parse&prop=wikitext` qu'il faut ; une recherche `insource:"phrase"` **ne prouve l'absence que des formulations testées**, et cinq notes d'audit qui en tiraient une certitude excessive ont été reformulées ; enfin **les projets frères — bibliothèque de textes libres et recueil de citations — n'avaient pas été interrogés**, alors que c'est là que vivent les sources primaires que les audits réclamaient. **Deux des meilleures résolutions de la passe en sont venues** : la note de Becquerel de 1896 dans les *Comptes rendus de l'Académie des sciences*, et le texte des *Époques de la nature* de Buffon.

**Les plus lourds** : « les femmes produisent 60 à 80 % de l'alimentation » (`terre` E19) — **ce n'est pas la grandeur que l'on mesure**, la statistique établie étant la part des femmes dans la main-d'œuvre agricole, 37,8 % en 2021 ; **le chiffre des cent mille mammifères marins** (`terre` E08), dont la seule citation est une page d'ONG de 2021 ; **les rejets de pêche à 40-50 %** (`terre` E13), quand la FAO retient 10,8 % ; **le rotin en Amazonie** (`terre` E05), absent du continent américain ; **le cognac chinois** (`decouvreurs` E01), l'antériorité étant arabe de trois siècles.

**Un troisième élargissement a suivi** : l'interrogation des **éditions linguistiques les plus proches du sujet**, et non plus seulement l'anglaise et la française. Elle a produit trois résolutions qu'aucune autre voie n'atteignait — **le statut de protection d'*Echium wildpretii*** par l'ordonnance canarienne de 1991, trouvé en espagnol ; **l'ascendance maternelle de Marconi**, la famille des distillateurs Jameson, trouvée en italien, qui donne sa racine réelle à la distillerie clandestine de l'épisode ; et la confirmation que **les toits de Çatal Höyük sont documentés comme un réseau de circulation, non comme une défense**. En revanche, les éditions portugaise et néerlandaise n'ont rien donné sur Curitiba ni sur les façades d'Amsterdam : **le réflexe est bon, le rendement reste inégal**.

**Une distinction a par ailleurs été introduite dans les points restants.** Ceux dont la recherche a établi qu'ils **sont absents de la documentation généraliste** portent désormais la mention de la vérification effectuée : ce n'est pas une résolution, c'est un renseignement — ils ne se fermeront que sur archives primaires, et l'on sait maintenant lesquelles.

---

## Voir aussi

- Les six synthèses de série : [`_audit/_synthese-homme.md`](_audit/_synthese-homme.md) · [`_audit/_synthese-vie.md`](_audit/_synthese-vie.md) · [`_audit/_synthese-decouvreurs.md`](_audit/_synthese-decouvreurs.md) · [`_audit/_synthese-explorateurs.md`](_audit/_synthese-explorateurs.md) · [`_audit/_synthese-objets.md`](_audit/_synthese-objets.md) · [`_audit/_synthese-terre.md`](_audit/_synthese-terre.md)
- [`_index-general.md`](_index-general.md) — l'entrée générale du dossier
- [`_liens-entre-series.md`](_liens-entre-series.md) — **section 8** : ce que la vérification révèle en croisant les séries
- [`_bible-personnages.md`](_bible-personnages.md) — le cast récurrent, seul document du dossier qui n'a eu besoin d'aucune correction