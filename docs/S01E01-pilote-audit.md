# S01E01 — audit visuel du pilote

Grille : les 13 points de `METHODE-generation-images.md` §20, plus les 8 contrôles de `S01E01-pilote-prompts-3-styles.md` §9. Une section par lot. Les fichiers audités sont dans `EpisodeModernise/pilote/images/Style*/`, les références dans `pilote/references/`.

---

## Lot 1 — les trois images d'épreuve, P02 (2026-08-22)

Prompts : `docs/prompts/S01E01-pilote-prompts-assembles.md`, entrées `P02_StyleA/B/C`. Références réinjectées dans l'ordre D01, Parieurs, Foule. Les trois fichiers font 2752 × 1536, rapatriés par `curl` depuis le CDN de résultat, qui est joignable depuis la machine de Guillaume (contrairement au conteneur Cowork).

| Contrôle | A | B | C |
|---|---|---|---|
| 1. Aucun texte | ✔ | ✔ | ✔ |
| 2. Bon nombre de sujets (deux badauds + foule) | ✔ | ✔ | ✔ |
| 3. Aucun fragment fantôme | ✔ | ✔ | ✔ |
| 4. Aucun accessoire dupliqué (une canne, un chapeau à cocarde) | ✔ | ✔ | ✔ |
| 5. Style B : moufles, deux bras, visage réduit | moufles noires pleines, **pas de pouce lisible** (résultat connu, RÈGLE 16, déjà absent sur la fiche de référence) ; sourcils présents sur les deux badauds, **comme sur la fiche Parieurs_StyleB validée** | | |
| 6. Style C : deux tons à bords durs, ambre/ocre, ombres sarcelle | | | ✔ et cette fois **nettement distinct du style A** (contrôle 8 de la fiche : positif sur ce cadrage rapproché) |
| 7. Style A : contours épais, aplats | ✔ | | |
| 8. Couleurs réservées non dominantes | ✔ (gilet moutarde du badaud rond = celui de la fiche validée) | ✔ | ✔ |
| 10. Plein cadre, rien qui touche le bord | ✔ | ✔ | ✔ |
| 13. Balayage libre | rien d'anormal | rien d'anormal | **les deux badauds du premier plan n'ont AUCUN visage** : ovales de peau vides, sans yeux ni bouche |
| Fiche §9‑1 : aucun visage lisible dans la foule | ✔ foule de dos | ✔ têtes rondes vierges, exemplaire | ✔ foule de dos |
| Fiche §9‑3 : chapeau à cocarde sur le rond à gauche, canne sur le maigre à droite | ✔ | ✔ | ✔ |
| Fidélité à la fiche Parieurs (même homme, même costume) | ✔ | ✔ | ✔ (costume et silhouette) |
| Fidélité au décor D01 (colonnade, allées d'arbres, ballon) | ✔ | ✔ parc sombre à l'aube, grand arbre à gauche, ballon hors champ mais nacelle présente, conforme à la brique | ✔ ciel ambre, ombres sarcelle, skyline |

### Verdict

* **A : validable.**
* **B : validable**, avec les deux réserves connues et déjà documentées du style B (pouce non obtenu, sourcils d'expression).
* **C : bloquant.** Les deux personnages nommés sortent sans visage.

### Diagnostic du défaut C

Le prompt de P02 est le seul du pilote où des **personnages nommés à visage** cohabitent avec la **négative de foule** du point 4.4 de la fiche : `readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures`. Une négative agit sur toute l'image, pas sur la foule seule. En A et en B le modèle a arbitré en faveur des visages des badauds ; en C il a obéi à la négative et les a effacés. C'est le mécanisme de la **RÈGLE 23** (une clause invariante qui contredit une clause variable : le modèle arbitre au hasard) et du chapitre 8 (une description qui contredit sa propre négative n'est pas reproductible).

### Correction proposée, à valider par Guillaume

Sur **P02 seulement**, retirer la négative de foule §4.4 de la liste `Avoid:` et s'en remettre au bloc positif `[FOULE]`, qui prescrit déjà `NO FACE VISIBLE ON ANY FIGURE, no facial features at all`. Rien d'autre ne change (RÈGLE 13 : on réécrit le prompt complet avec la correction dedans, sans empiler). Les plans 1a, 1b et 4a gardent la négative §4.4 : ils n'ont aucun personnage nommé à visage.

* Option recommandée : **relancer P02_StyleC seul** (2 crédits), garder A et B tels quels.
* Option de cohérence : relancer les trois P02 avec le prompt corrigé (6 crédits), pour que les trois styles partagent exactement le même prompt. Risque : un nouveau tirage A ou B moins bon que l'actuel.

Si la relance C confirme le diagnostic, la leçon entre dans `METHODE-generation-images.md` comme règle numérotée : *une négative de foule ne se pose jamais sur un plan où un personnage nommé montre son visage ; la foule sans visage se prescrit alors en positif seulement.*

---

## Lot 1 bis — P02_StyleC relancé sans la négative de foule (2026-08-22)

**Le diagnostic est confirmé** : avec le même prompt moins la négative §4.4, les deux badauds ont leur visage, costume et silhouette conformes à la fiche Parieurs_StyleC, cocarde à gauche et canne à droite. La foule reste de dos ou de trois quarts arrière sans visage lisible ; un homme en bicorne à gauche et une femme en bonnet à droite sont de profil, traits non lisibles à la taille affichée. Écart mineur : le maigre porte un chapeau mou absent de la fiche. **Validable.** P02_StyleC v1 (sans visages) est écrasé ; le prompt v2 est dans `prompts/S01E01-pilote-prompts-assembles.md`.

## Lot A1 — style A, 12 images hors P02 (2026-08-22), première lecture sur vignettes

| Image | Verdict | Observation |
|---|---|---|
| P1a-1 | **à reprendre** | trois figures à droite de la nacelle vues **de face**, visages visibles bien que petits (contrôle §9‑1, le défaut déjà passé trois fois). Le reste : brume, ballon gonflé, décor D01 fidèle, foule de dos. |
| P1a-2 | **à reprendre, bloquant** | au bord bas, une robe **orange vif** et une veste **sarcelle vif** : deux couleurs réservées (Elio, Naya) malgré la négative. C'est le seul plan de foule où la référence Foule n'est pas réinjectée (table §4.1 du runbook : D01 seul) ; les costumes ont dérivé. Ballon et amarres tendues par ailleurs corrects. |
| P1a-3 | ✔ | bannières en aplats sans lettrage, filet, contre‑plongée. |
| P1a-4 | à surveiller | foule qui se tourne vers la nacelle, de dos en majorité ; un homme et une femme près de la nacelle font face, visage esquissé. Vérifier en pleine résolution. |
| P1b-1 | **à reprendre** | la foule s'écarte en deux haies, chapeaux levés, de dos : conforme. Mais le décor n'est pas D01 : rue bordée de grilles et de maisons, ni colonnade ni ballon. Rupture de raccord avec 1b‑2. |
| P1b-2 | **à reprendre, bloquant** | les deux aides portent **l'enveloppe dégonflée du ballon** sur les épaules, avec **deux nacelles**, une dans chaque main extérieure. Contredit 1a (ballon gonflé) et double l'accessoire (grille point 4). Foule de dos et décor D01 corrects. À confronter aux styles B et C avant de toucher à la brique (RÈGLE 7). |
| P1b-3 | ✔ | mains et avant‑bras seuls, nœuds sur le rebord d'osier, anneaux de fer, D01 flou. Aucune paréidolie. |
| P03 | à surveiller | Garnerin conforme au bloc identité (habit sombre, cheveux noués, foulard pâle), paquet de soie, couteau glissé au flanc, aide de dos au premier plan : tout y est. Mais le ballon gonflé est posé **au loin dans le parc**, alors que la nacelle du premier plan devrait être sous lui. Logique de scène à trancher avec Guillaume. |
| P4a-1 | ✔ | ballon qui s'arrache, cordes qui retombent, foule de dos. |
| P4a-2 | ✔ | foule de dos, mains sur les chapeaux, basculée en arrière. |
| P4a-3 | ✔ | ballon qui rétrécit au‑dessus des cimes, corde traînante. |

Constat transversal : **aucun texte sur les 12**, style A tenu partout, décor D01 fidèle sur 10 images sur 11 où il est réinjecté. Les trois défauts de fond portent sur ce que le prompt ne nomme pas assez (couleurs des figurants sans référence, « basket » lu comme l'enveloppe, « lane » lu comme une rue).

## Lot A2 — style A, 6 images 4b et 5 (2026-08-22), première lecture sur vignettes

| Image | Verdict | Observation |
|---|---|---|
| P4b-1 | ✔ | toits de Paris en plongée, rebord d'osier au premier plan, corde, paquet de soie posé sur le rebord, fumées de cheminées. Tache verte du parc, non réservée. |
| P4b-2 | ✔ | main gantée serrée sur le rebord, Garnerin derrière (habit sombre, foulard pâle, cheveux noués), ciel D2 flou. Visage coupé par le bord haut, acceptable sur un gros plan de main. |
| P4b-3 | ✔ | ville sous la brume, tache sombre au milieu du parc, aucun personnage. |
| P5-1 | ✔ | main qui saisit le couteau glissé au flanc de la nacelle, D2 flou derrière. Pas de paréidolie sur la main. |
| P5-2 | **à reprendre** | la lame scie bien la corde, fibres qui jaillissent… mais la corde est **déjà tranchée en deux**, ce qui est le contenu de 5‑3. Le clip 5‑2 doit partir d'une corde encore tendue. |
| P5-3 | **à reprendre** | corde qui cède d'un coup, torons qui fouettent : conforme. Mais le fond n'est pas le ciel D2 flou : mur beige et pied de tabouret, lu comme un intérieur. C'est l'image figée du plan 6 avec carton titre, le fond compte. |

Bilan style A après 18 images : **12 validables**, 4 à reprendre (1a‑2, 1b‑2, 5‑2, 5‑3), 2 à reprendre probablement (1a‑1, 1b‑1), 2 à trancher (1a‑4, P03).

## Lot B1 — style B, 12 images hors P02 (2026-08-22), première lecture sur vignettes

| Image | Verdict | Observation |
|---|---|---|
| P1a-1 | ✔ | foule inkman de dos, têtes vierges (blanches ou noires de dos), ballon gonflé, nacelle, cordes, parc D01 à l'aube. |
| P1a-2 | **à reprendre** | les figurants du bord bas sont vus **de trois quarts face avec yeux points et bouches ouvertes**. Même plan que le 1a‑2 de style A fautif : c'est le seul plan de foule sans la référence Foule. **Deux styles sur trois échouent sur le même prompt (RÈGLE 7)** : la cause est dans la table de références, pas dans le tirage. |
| P1a-3 | à surveiller | contre‑plongée sous le ballon, cerceau, filet, cordages : très beau. Mais les bannières portent des **motifs héraldiques** (fiche §9‑6 : « des aplats »). Pas de lettrage. |
| P1a-4 | ✔ | foule nombreuse tournée vers la nacelle, têtes vierges, aucun visage. |
| P1b-1 | ✔ | deux haies de dos, chapeaux levés, parc D01 reconnaissable (contrairement au style A). |
| P1b-2 | à surveiller | **une seule** nacelle portée par deux aides inkmen, foule de dos derrière : conforme. Mais une **seconde nacelle** est posée au fond à droite, et les deux aides ont des sourcils froncés. À confronter au style C : A et B doublent tous deux la nacelle sur ce plan. |
| P1b-3 | ✔ | moufles noires nouant les cordes sur l'anneau de fer, rebord d'osier, D01 derrière. Aucun pouce (connu). Une manche sarcelle pâle, désaturée, non dominante. |
| P03 | ✔ | Garnerin inkman conforme (cheveux noués en traits, habit sombre, foulard pâle), paquet de soie plié, couteau au flanc, aide de dos au bord. Réserves : sourcils sur Garnerin (connu), tête de l'aide beige et non blanche. |
| P4a-1 | ✔ | ballon qui s'arrache, cordes qui retombent, dos de la foule. |
| P4a-2 | ✔ | foule mains aux chapeaux, basculée en arrière ; vue **de face** plutôt que de dos, mais têtes vierges donc aucun visage. |
| P4a-3 | à surveiller | ballon au‑dessus des cimes mais **encore bas**, cordes qui traînent jusqu'au sol : après 4a‑1 il devrait être plus haut. |
| P4b-1 | ✔ | toits de Paris, rebord d'osier, cordes, paquet de soie sombre dans la nacelle, fumées, parc vert. |

Constat transversal style B : **aucun visage lisible sur aucun plan de foule**, le principe « têtes vierges » tient partout ; décor D01 fidèle sur les 11 images où il est réinjecté ; aucun texte. Le style B est, à ce stade, le plus propre des trois sur la foule.

## Lot B2 — style B, 4b et 5 (2026-08-22), première lecture sur vignettes

| Image | Verdict | Observation |
|---|---|---|
| P4b-2 | ✔ | Garnerin inkman (yeux points, cheveux noués, foulard, habit sombre), moufle noire serrée sur le rebord, Paris flou derrière. |
| P4b-3 | — | refus `nsfw` du serveur sur un **paysage sans aucun personnage** : faux positif manifeste, resoumis à l'identique (voir index). |
| P5-1 | ✔ | moufle qui saisit le couteau au flanc de la nacelle, foulard et habit de Garnerin au‑dessus, toits flous. |
| P5-2 | ✔ | la lame scie une corde **encore entière**, fibres qui jaillissent : meilleur que le 5‑2 de style A. Décor net plutôt que flou, mineur. |
| P5-3 | ✔ | corde rompue, torons qui fouettent, ciel et toits D2 derrière : c'est l'image du carton titre, elle tient. |

Bilan style B après 17 images rendues : **15 validables**, 1 à reprendre (1a‑2, même cause qu'en A), 1 en cours (4b‑3 resoumis). Réserves transversales déjà connues : pas de pouce, sourcils d'expression.

## Lot C1 — style C, 11 images sur 12 rendues (2026-08-22), première lecture sur vignettes

| Image | Verdict | Observation |
|---|---|---|
| P1a-1 | à reprendre probable | plan large très réussi (brume, rotonde, arches, ballon) mais plusieurs figures du groupe central sont **de face ou de trois quarts face**, visages petits mais présents. Même famille que A. |
| P1a-2 | ✔ | ballon amarré aux piquets, cordes tendues, quelques figurants de dos au bord bas, costumes bruns et olive. **Le seul des trois 1a‑2 qui passe.** |
| P1a-3 | à surveiller | ballon entier et bannières : **écussons héraldiques** sur les bannières, comme en B. Pas de lettrage. Le mot `banners` appelle des armoiries dans deux styles sur trois. |
| P1a-4 | à surveiller | foule tournée vers la nacelle, décor D01 exemplaire ; un homme en bicorne et une femme **de profil**, traits visibles. À vérifier en pleine résolution. |
| P1b-1 | ✔ | deux haies de dos, chapeaux levés, château et rivière de D01, aucun visage. |
| P1b-2 | à trancher | **une seule** nacelle portée, foule de dos : conforme. Mais le ballon du fond garde **sa propre nacelle** (celle de la plaque D01). Trois styles sur trois montrent deux nacelles sur ce plan : la référence D01 impose un ballon **avec** nacelle, la brique demande une nacelle **portée vers** le ballon. Contradiction structurelle référence/brique (RÈGLE 1), pas un tirage. |
| P1b-3 | ✔ | mains nouant les cordes sur le rebord, anneau de fer, D01 derrière ; le ballon est loin au fond plutôt qu'au‑dessus, même logique que ci‑dessus. |
| P03 | à surveiller | Garnerin, soie pliée, couteau au flanc, aide de dos, parc D01 : tout y est. Son habit est **vert olive** et non sombre ; le ballon est au loin derrière et non au‑dessus de la nacelle (comme en A). À confronter à la fiche Garnerin_StyleC. |
| P4a-2 | ✔ | foule de dos mains aux chapeaux, ballon qui monte, aucun visage. |
| P4a-3 | ✔ | ballon au‑dessus des cimes, cordes traînantes, ciel ambre et nuages sarcelle. |
| P4b-1 | ✔ | toits, rebord, corde, soie, fumées, parc : style C net. |
| P4a-1 | — | job resté seul `in_progress` après la sortie de tout son lot ; traité selon la règle des trois minutes. |

Observations transversales style C : la palette ambre / sarcelle tient sur **tous** les plans, larges compris ; c'est la première campagne où le style C est discernable du style A sur des plans larges (RÈGLE 15 à réviser).

## P4b-3_StyleB resoumis

✔ ville sous la brume, la foule est une **tache sombre au milieu du parc**, lisible. Le refus `nsfw` initial était un faux positif pur ; la resoumission à l'identique a suffi (2 crédits).

## Lot C2 et P4a‑1_C resoumis (2026-08-22)

| Image | Verdict | Observation |
|---|---|---|
| P4a-1 (resoumis) | ✔ | ballon qui s'arrache, cordes qui retombent, dos de la foule, aucun visage. Le premier job était mort (seul en `in_progress` six minutes après la sortie du lot), la resoumission a abouti en 40 s. |
| P4b-2 | à surveiller | main gantée serrée sur le rebord, ville derrière ; Garnerin porte ici un **habit brun sombre** alors que la fiche `Garnerin_StyleC` validée et P03_C le montrent en **vert olive**. Le bloc identité dit `dark tailcoat`, la fiche de référence dit olive : contradiction entre deux sources, signalée. |
| P4b-3 | ✔ | ville sous la brume, tache sombre de la foule au milieu du parc. |
| P5-1 | ✔ | main sur le couteau au flanc de la nacelle, manche olive de Garnerin, ville derrière. |
| P5-2 | **à reprendre** | la corde est **déjà tranchée** de part et d'autre de la lame, comme en A. Deux styles sur trois (RÈGLE 7) : la brique « the blade sawing the taut rope » fait sauter le modèle au résultat. |
| P5-3 | ✔ | corde rompue, torons qui fouettent, toits et parc en ambre et sarcelle. |

## Vérification pleine résolution des « visages de face » (1a‑1, 1a‑4)

Recadrages à l'échelle 1 sur P1a‑1_A, P1a‑4_A, P1a‑1_C, P1a‑4_C : les figures vues de face ou de trois quarts **n'ont aucun trait de visage** (ovales de peau vides). Le contrôle §9‑1 « aucun visage lisible » est donc **respecté** sur les quatre plans de foule dans les trois styles. Ces quatre images passent de « à reprendre probable » à **validables**.

---

# Bilan des 54 images (2026-08-22, solde 920,44 crédits : 112 consommés, 56 images facturées, le refus nsfw et le job mort n'ont pas été débités)

## Validables en l'état : 45

* **A** (13/18) : P02, 1a‑1, 1a‑3, 1a‑4, 1b‑3, P03, 4a‑1, 4a‑2, 4a‑3, 4b‑1, 4b‑2, 4b‑3, 5‑1
* **B** (17/18) : tout sauf 1a‑2
* **C** (15/18) : tout sauf 1a‑1 (validable, voir ci‑dessus → 16/18), 5‑2, 4b‑2 à trancher

## À reprendre, et comment

| Image(s) | Défaut | Cause | Correction proposée | Crédits |
|---|---|---|---|---|
| 1a‑2 A et B | A : robe orange vif et veste sarcelle vif ; B : figurants de face avec yeux points | seul plan de foule **sans la référence Foule** (table §4.1 du runbook : D01 seul) | **ajouter la référence Foule** sur 1a‑2 (décor puis personnages), relancer A et B. C a passé avec l'ancien prompt, on le garde. | 4 |
| 1b‑2 A | enveloppe dégonflée portée + deux nacelles | tirage aberrant ; B et C ont une nacelle portée | relancer A à l'identique | 2 |
| 5‑2 A et C | corde déjà tranchée | brique lue comme un résultat (2/3 styles, RÈGLE 7) | **amender la brique 5‑2** : `the rope is still in ONE piece and taut, only a few outer fibres cut and springing free, the blade halfway through` (prompt complet réécrit, RÈGLE 13), relancer A et C. B a passé, on le garde. | 4 |
| 5‑3 A | fond d'intérieur au lieu du ciel D2 | tirage ; B et C ont le ciel | relancer A à l'identique | 2 |
| 1b‑1 A | rue au lieu du parc D01 | tirage ; B et C ont le parc | relancer A à l'identique | 2 |
| 4b‑2 C | habit brun au lieu d'olive | bloc identité `dark tailcoat` contre fiche olive | relancer C à l'identique et regarder ; si brun persiste, trancher la contradiction bloc/fiche | 2 |
| | | | **Total** | **16** |

## À trancher par Guillaume, sans relance proposée

1. **La seconde nacelle sous le ballon** (1b‑2 B et C, 1b‑3 C, P03 A et C) : la plaque D01 validée montre le ballon **avec** sa nacelle ; les briques 1b demandent qu'on la porte vers lui. La référence impose sa mise en page (RÈGLE 1). Option a : accepter, la nacelle du fond est petite et le clip dure 3 s. Option b : amender les briques 1b et P03 pour nommer « the balloon hanging above, its basket not yet attached », ce qui contredit la plaque. Recommandation : **a**.
2. **Les bannières à écussons** (1a‑3 B et C) : aucun lettrage, mais des armoiries. La fiche §9‑6 demande des aplats. Recommandation : **accepter pour le pilote**, et noter dans la fiche que `banners` appelle des armoiries.
3. **Le ballon loin derrière la nacelle** sur P03 (A, C) et 1b‑3 (C) : même mécanisme que le point 1. Recommandation : accepter.

## Ce que le pilote a déjà appris (à verser dans METHODE après validation)

* Une négative de foule (`facial features, eyes`) ne se pose jamais sur un plan où un personnage nommé montre son visage (P02 C). Règle candidate.
* Un plan de foule **sans** la référence Foule dérive (couleurs réservées en A, visages en B). Toujours réinjecter la fiche Foule dès qu'un figurant est nommé, même « a few crowd figures ».
* Le style C **tient sur les plans larges** dès qu'une plaque de décor C est réinjectée : la RÈGLE 15 vaut pour les planches personnages sur fond neutre, pas pour les plans de scène.
* Le style B est le plus robuste sur la foule : têtes vierges sans exception sur 6 plans × 1 style.
* Faux positif `nsfw` possible même sur un paysage vide ; resoumettre à l'identique suffit et n'est pas débité.

---

# Reprises (2026-08-22), décisions de Guillaume : les 8 reprises avec corrections de fiche, bannières acceptées, briques 1b-2 / 1b-3 / P03 amendées pour la seconde nacelle

| Image | Version | Verdict | Observation |
|---|---|---|---|
| P1a-2 A | v2, + réf Foule | ✔ | figurants de dos, bruns, verts, marine : plus aucune couleur réservée. |
| P1a-2 B | v2, + réf Foule | ✔ | figurants de dos, têtes noires ou vierges : plus aucun œil point. **La référence Foule règle le plan dans les deux styles.** |
| P1b-2 A | v2, identique | ✔ | une nacelle portée par deux aides, foule de dos, colonnade D01, ballon hors champ. Le tirage v1 (enveloppe dégonflée) était un accident. |
| P5-2 A | v2, brique « corde entière » | ✗ | corde entière et lame à mi‑chemin : la brique marche. Mais un **panneau portant le texte « D2 »** et un mur au lieu du ciel : le code `D2` seul, sur un très gros plan de style A, est lu comme une inscription. v3 relancée avec `Decor: D2, the sky and the rooftops of Paris far below, out of focus behind`. |
| P5-2 C | v2, brique « corde entière » | ✔ | corde en un seul morceau, lame à mi‑chemin, fibres, toits derrière. |
| P5-3 A | v2, identique | ✗ | mur de pierre à nouveau au lieu du ciel (2 tirages sur 2). Même cause que 5‑2 A : v3 relancée avec le décor explicité. |
| P1b-1 A | v2, identique | ✔ | deux haies de dos, chapeaux levés, parc D01 avec colonnade au fond. |
| P4b-2 C | v2, identique | ✔ | manche **vert olive**, conforme à la fiche Garnerin_StyleC ; main gantée sur le rebord, ville derrière. La contradiction bloc/fiche reste à noter dans la fiche personnages (le bloc dit `dark tailcoat`). |
| P1b-2 B | v2, brique amendée | ✔ | une seule nacelle, **le ballon au‑dessus n'a plus de nacelle** (cerceau nu), foule de dos. |
| P1b-2 C | v2, brique amendée | ✔ | idem, très propre. |
| P1b-3 C | v2, brique amendée | ✔ | mains sur l'anneau et le rebord, château D01, aucun ballon ni nacelle au fond. |
| P03 A | v2, brique amendée | ✔ | Garnerin en habit sombre, soie, couteau, aide de dos, cordes qui montent vers le cerceau hors champ ; plus de ballon au fond. |
| P03 C | v2, brique amendée | ✔ | Garnerin olive, rotonde D01, cordes vers le cerceau, plus de ballon au fond. |

Leçon nouvelle : **un code de décor (`D1`, `D2`) ne suffit pas sur un très gros plan** où la référence n'a presque pas de surface pour s'imposer ; il faut accoler au code une description en clair, sinon le modèle peut l'écrire. Devenue RÈGLE 28.

| P5-3 A | v3, décor D2 explicité | ✔ | corde rompue, torons qui fouettent, **ciel et toits de Paris** derrière : la description en clair a suffi là où le code seul échouait deux fois sur deux. |
| P5-2 A | v3, brique « corde entière », code D2 seul | ✗ | corde entière et lame à mi‑chemin : bien ; mais rue au sol au lieu du ciel. |
| P5-2 A | v4, décor D2 explicité | ✔ | corde en un morceau, lame qui entame, fibres, ciel et toits derrière. |

---

# Bilan final des 54 images, 2026-08-22, 11 h 40

**54 / 54 validables à l'audit, validées par Guillaume le 22 août 2026.** 73 jobs soumis, 71 débités (le refus nsfw et le job mort ne l'ont pas été), **142 crédits**, solde **890,44**. Planches : `pilote/_thumbs/planche_Style{A,B,C}.jpg`. Versions écartées conservées dans `pilote/_rebuts/`.

Réserves documentées, acceptées pour le pilote :
* style B : pas de pouce sur les moufles, sourcils d'expression sur les personnages nommés (connus, RÈGLE 16) ;
* bannières de 1a‑3 B et C à écussons héraldiques, sans lettrage (accepté par Guillaume) ;
* 4a‑3 B : ballon encore bas ; 4a‑2 B : foule vue de face mais têtes vierges ;
* bloc identité Garnerin `dark tailcoat` contre fiche `Garnerin_StyleC` olive : P03 C, 4b‑2 C et 5‑1 C suivent la fiche (olive), à corriger dans `prompts/fiche-prompts-personnages-episode-S01E01.md`.

Contrôles de la fiche §9, sur les 54 : 1 aucun visage lisible dans la foule ✔ (vérifié en pleine résolution sur A et C) · 2 Garnerin le même homme sur P03 / 4b‑2 / 5‑1 ✔ dans les trois styles · 3 cocarde à gauche, canne à droite ✔ ×3 · 4 moufles B sur 1b‑3 et 4b‑2 ✔ (sans pouce) · 5 aucune couleur réservée dominante ✔ après reprise de 1a‑2 A · 6 aucun texte ✔ (le « D2 » de 5‑2 A v2 a été écarté) · 7 raccords : à juger sur les clips · 8 le style C se distingue de A sur les plans larges **et** rapprochés ✔.

---

# Clips (phase D, RunPod / ComfyUI, Wan 2.2 I2V A14B fp8 + LightX2V 4 étapes, A100 80 Go)

Bandes de 5 images par clip dans `pilote/_thumbs/clips/`, mp4 dans `pilote/clips-runpod/Style*/`, versions écartées dans `_flf2v/` et `_v1/`.

## Lot 0 — chaîne FLF2V par images clés, style A (12 h 03, abandonné à 12 h 14)

Sept clips rendus. Les clés successives d'un bloc ont des cadrages différents : le FLF2V **morphe la caméra et la foule** d'un cadrage à l'autre (1a‑1 → 1a‑2 : le plan large glisse vers le plan moyen ; 1a‑2 → 1a‑3 : la foule se dissout dans la contre‑plongée). Conforme à ce que PIPELINE §5.2 prévoit : coupe nette = I2V. Décision consignée dans DECISIONS.

## Lot 1 — I2V, gabarit v1 (ligne « Characters gesture and react » sur tous les clips)

| Style A | Verdict | Observation |
|---|---|---|
| 1a‑1, 1a‑2, 1a‑3, 1a‑4, 1b‑1, 1b‑2, 1b‑3, 4a‑1, 4a‑2, 4a‑3, 5‑1, 5‑2, 5‑3 | ✔ 13 | cadrage stable, un seul geste, trait et aplats conservés : brume qui glisse, ballon qui oscille, bannières, têtes qui se tournent, haies qui s'ouvrent, nacelle portée avec cordes qui traînent, nœuds, ballon qui s'arrache et monte, main sur le couteau, lame qui scie, corde qui cède et sort du cadre (image finale : ciel vide, utilisable pour le carton). |
| 4b‑1 | ✗ | **deux hommes surgissent dans la nacelle** (plan « Characters: none »). |
| 4b‑2 | ~ | main qui serre le rebord : bien ; Garnerin ouvre la bouche (« they do not speak »). |
| 4b‑3 | ✗ | **un visage géant et une foule de têtes sortent de la brume**. |
| B 1a‑1, 1a‑2, 1a‑3, 5‑3 ; C 5‑3 | ✗ | inkman fantôme au premier plan (1a‑1 B), tête d'inkman qui agrippe la corde (5‑3 B), homme à chapeau sur la corde (5‑3 C). |

## Lot 2 — I2V, gabarit v2 (ligne de présence par clip + négatives de présence), mêmes graines

| Clip | Verdict | Observation |
|---|---|---|
| 4b‑1 A | ✔ | plus personne dans la nacelle ; une petite tête se devine sur un nœud de corde (paréidolie mineure). |
| 4b‑2 A | ✔ | bouche fermée, main qui serre. |
| 4b‑3 A | ✗ | **même homme moustachu qui sort de la brume** : même graine, même tirage ; la ligne de présence ne suffit pas ici. |
| 1a‑1 B | ✗ | même inkman fantôme au premier plan (même graine). |
| 1a‑2 B | ✗ | la foule de dos **se retourne face caméra** et des yeux points apparaissent. |
| 1a‑3 B | ✗ | une tête d'inkman **vole dans le ballon**. |
| 1a‑4 B | ✗ | foule retournée, visages. |
| 1b‑1 B | ✗ | foule retournée, visages et cheveux. |
| 1b‑2 B | ~ | les deux aides portent la nacelle, mais la foule derrière se retourne. |
| 1b‑3 B | ✗ | mains qui nouent… puis une tête d'inkman géante entre par la gauche. |
| 4a‑1 B | ✔ | foule de dos, ballon qui s'arrache. |
| 4a‑2 B | ✗ | foule retournée, visages. |
| 4a‑3 B | ✗ | un disque blanc géant avec une moufle noire surgit devant le ballon. |
| 4b‑1 B | ✗ | une tête d'inkman géante se dresse dans la nacelle. |

**Constat de fond sur le style B en mouvement.** Avec Wan 2.2 de base (sans LoRA), le bloc de style B, qui décrit des *têtes rondes blanches à yeux points*, fait fabriquer des têtes partout où il y a du blanc ou du vide : brume, ciel, nacelle, et il donne un visage aux têtes vierges de la foule dès qu'elles bougent. Sept clips sur neuf sont inutilisables. Le style A, dont le bloc décrit surtout un traitement graphique, tient à 15 sur 16. Le pilote répond donc à une question qu'il ne posait pas : **le style B demande soit un LoRA de style vidéo, soit un bloc de style vidéo qui ne décrive pas les personnages.** À essayer en lot 3 sur quelques clips B : bloc de style réduit à la facture (sans têtes, sans yeux), graine décalée.

## Lot 2 (suite) — style C, gabarit v2, mêmes graines

| Clip C | Verdict | Observation |
|---|---|---|
| 1a‑1, 1a‑2, 1a‑3, 1a‑4, 1b‑1, 1b‑2, 1b‑3, 4a‑1, 4a‑2, 4a‑3, 4b‑1, 4b‑2, 4b‑3, 5‑1, 5‑2, 5‑3 | ✔ 16 / 16 | foule de dos qui lève les bras, ballon qui oscille, bannières, haies qui s'ouvrent (quelques trois quarts, pas de visage lisible), nacelle portée en travelling, mains qui nouent, ballon qui s'arrache et monte, toits et fumées, poing qui serre, brume qui glisse sans visage, main sur le couteau, lame qui scie, corde qui cède. La palette ambre / sarcelle tient sur toute la durée. Réserve : 5‑2 fait apparaître une seconde main qui tient la corde, plausible. |

## Lot 3 — essai « bloc de style vidéo réduit » + graine décalée de 1 (12 clips B fautifs + 4b‑3 A)

Hypothèse : le bloc de style B décrit des têtes rondes blanches à yeux points ; sur un modèle **image vers vidéo**, l'image clé porte déjà le style, et ce bloc ne sert qu'à fabriquer des têtes. Bloc réduit à la facture (`flat graphic 2D cartoon animation on a richly painted atmospheric background, textured light, muted earth tones, limited animation`) ; A et C gardent leur bloc de la fiche sauf 4b‑3 A pour l'essai.

| Clip | Verdict | Observation |
|---|---|---|
| 4b‑3 A | ✔ | brume qui glisse, **plus de visage** ; une minuscule silhouette sur la tache sombre, négligeable. |
| 1a‑1 B | ✔ | foule de dos, plus de fantôme. |
| 1a‑2 B | ✔ | foule de dos qui lève les bras, têtes noires ou vierges. |
| 1a‑3 B | ✔ | bannières qui claquent, aucune tête. |
| 1a‑4 B | ✔ | foule tournée vers la nacelle, têtes vierges. |
| 1b‑1 B | ✔ | deux haies, chapeaux levés, têtes vierges. |
| 1b‑3 B | ~ | moufles qui nouent ; une moufle noire entre par le bas à la dernière image. |
| 4a‑2 B | ✔ | mains aux chapeaux, têtes vierges. |
| 4a‑3 B | ✔ | ballon qui monte et rétrécit. |
| 4b‑1 B | ✔ | toits et fumées, personne dans la nacelle. |
| 4b‑3 B | ✔ | brume, tache sombre de la foule, personne. |
| 5‑2 B | ✔ | lame qui scie, moufles plausibles. |
| 5‑3 B | ✔ | corde qui cède, torons, personne. |

**Le bloc réduit règle le style B du premier coup : 12 sur 12 exploitables.** Le style de l'image clé suffit au modèle vidéo ; le bloc de style verbal sert surtout à lui suggérer des personnages. Règle candidate pour PIPELINE §6 : *en image vers vidéo, le bloc de style se réduit à la facture (trait, aplats, palette, cadence), il ne décrit jamais les personnages.*

---

# Bilan des 48 clips, 2026-08-22, 13 h 55 UTC

| Style | Clips retenus | Composition | Défauts résiduels |
|---|---|---|---|
| **A** | 16 / 16 | 13 du lot 1 (gabarit v1), 4b‑1 et 4b‑2 du lot 2, 4b‑3 du lot 3 | 4b‑1 : petite tête sur un nœud de corde ; 4b‑3 : silhouette minuscule |
| **B** | 16 / 16 | 4a‑1, 4b‑2, 5‑1, 1b‑2 du lot 2 ; 12 du lot 3 (bloc vidéo réduit) | 1b‑3 : moufle qui entre à la dernière image ; foule parfois vue de face mais têtes vierges |
| **C** | 16 / 16 | lot 2 | 5‑2 : seconde main |

Montages de comparaison, 69 s chacun (16 clips + P02 tenu 10 s + P03 tenu 12 s, sans mouvement de caméra) : `pilote/montages/montage_Style{A,B,C}.mp4`. Versions écartées : `clips-runpod/_flf2v/`, `_v1/`, `_v2/`. Séquences PNG master : `clips-runpod/_png/pilote_output.tar` (toutes versions ; la version finale d'un clip est la dernière série de `length` images de son dossier, voir l'index).

Ce que le pilote vidéo a appris : 1) les coupes internes d'un bloc se rendent en I2V, le FLF2V morphe les cadrages ; 2) le gabarit doit dire ce qu'il y a à l'image (aucun personnage / mains / foule) ; 3) en image vers vidéo, le bloc de style ne doit pas décrire les personnages, surtout en B ; 4) une graine identique reproduit le même défaut, une reprise change la graine ; 5) Wan 2.2 de base, sans LoRA, tient le trait des trois styles sur 2 à 4 s : aucun clip ne ramollit les contours ni n'ajoute de volume. Coût : 3 lots, 96 rendus, ~2 h 10 d'A100 ≈ 3 $.


## Lot 4 — clips parlants et voix (2026-08-22, 14 h 20 à 14 h 55 UTC, second pod A100 `8vem2qbtwzbw4y`)

Demande de Guillaume : « pas de synchro labiale ne veut pas dire bouches immobiles ». Trois clips par style, ligne de présence `talking` (bouches qui s'ouvrent et se ferment, non synchronisées, gestes légers), négatives sans `lip sync` ni `mouth articulation`, bloc de style réduit pour B, 5 s (81 images) pour P02 et P03, 3 s pour 1b‑2.

| Clip | A | B | C |
|---|---|---|---|
| P02‑talk (les badauds parient) | ✔ les deux parlent, bouches ouvertes/fermées, le rond pointe vers la nacelle | ✔ inkmen qui discutent, bouches mobiles, foule vierge derrière | ✔ dispute animée, index levé, bouches mobiles |
| P03‑talk (l'aide et Garnerin) | ✔ Garnerin répond en parlant et gesticule, l'aide de dos s'anime | ~ Garnerin inkman parle ; l'aide beige se retourne à moitié vers la caméra (tête vierge) | ✔ Garnerin parle et gesticule sans lâcher la soie |
| P1b‑2‑talk (les aides se parlent en portant) | ✔ de profil, bouche discrète | ✔ les deux inkmen échangent en marchant | ✔ |

**Voix** (ElevenLabs `eleven_v3`, français, une seule piste pour les trois styles, `pilote/audio/`) : BADAUD 1 et GARNERIN sur la voix « Guillaume – Narration and voiceover » (grave), BADAUD 2 et L'AIDE sur « Curieux REM » (claire) ; quatre répliques du scénario à la ponctuation près, 1,0 / 1,8 / 3,4 / 0,7 s, 120 caractères. Montages parlants avec piste voix : `pilote/montages/montage_Style{A,B,C}_parlant.mp4` (P02 et P03 bouclés sur 10 et 12 s, répliques posées à +1 s).


## Lot 5 — dialogues découpés par locuteur, styles A et B (2026-08-22, 15 h 05 à 15 h 43 UTC, pod RTX 5090 `fpmrh7ovnt7szg`)

Retours de Guillaume sur les montages parlants : scènes en double (clip de 5 s bouclé), deux bouches qui parlent pendant tout le plan, audio décalé ; style C retiré. Nouveau découpage : **quatre sous-clips par plan** — P02 : attente 2 s, le rond parle 2,5 s, le maigre répond 3 s, silence 2,5 s ; P03 : attente 2 s, l'aide parle 4 s, Garnerin répond 2,5 s, silence 3,5 s — prompts « ONLY X speaks… Y keeps his mouth closed ».

* Première tentative, **FLF2V départ = fin = image clé** : 6 rendus quasi figés (piège n° 8), abandonnés (`clips-runpod/_fige/`).
* Deuxième, **chaîne par dernière image rendue** (`chain_dialogue_runpod.py`) : 16 sous-clips, 4 étages de ~2 min sur RTX 5090.

| Sous-clip | A | B |
|---|---|---|
| P02-1 attente | ✔ le rond ajuste son chapeau, bouches fermées | ✔ |
| P02-2 le rond parle | ✔ bouche mobile, index pointé vers la nacelle ; le maigre écoute bouche fermée | ✔ idem, le maigre fronce |
| P02-3 le maigre répond | ✔ bouche mobile, penché ; le rond écoute | ✔ |
| P02-4 silence | ✔ | ✔ |
| P03-1 attente | ✔ Garnerin vérifie la soie | ✔ Garnerin soulève la soie |
| P03-2 l'aide parle | ✔ l'aide de dos s'anime, Garnerin regarde, bouche fermée | ~ la tête beige de l'aide bouge, Garnerin sourit |
| P03-3 Garnerin répond | ✔ | ✔ |
| P03-4 silence | ✔ | ✔ |

Audio posé 0,3 s après le début du sous-clip du locuteur : `montages/montage_Style{A,B}_parlant_v2.mp4` (69,5 s). Reprise de 1b‑3 A (graine +2) sur la « tête dans un sac » signalée vers 16 s : même cadrage de mains et de nœuds, aucune tête identifiable dans l'un ni l'autre tirage ; v2 retenue, à confirmer par Guillaume.

Coût du lot : RTX 5090 secure, 38 min, ~0,6 $. Total RunPod du jour : 3 pods, ~4,6 $.


## Lot 6 — S2V (bouche pilotée par la voix) et continuité 4a‑2 / 5‑2 (2026-08-22, 16 h 20 à 17 h 05 UTC, pod RTX 5090 `eju7msjde2tn6s`)

* **Images** (Higgsfield, 8 crédits) : P4a‑2 A et B avec le ballon déjà haut dans le ciel ; P5‑2 A et B avec une seule personne (A : deux mains dans la même manche sombre, B : une moufle). Validables ; anciennes versions dans `_rebuts/*_avant-continuite.png`.
* **Clips I2V** 4a‑2 et 5‑2 en A et B rerendus depuis ces images.
* **S2V** : `wan2.2_s2v_14B_fp8_scaled` + LoRA LightX2V t2v 4 étapes (template officiel ComfyUI), 1280 × 720, 25 à 61 images selon la réplique (durée de la voix + 0,4 s), `ref_image` = image clé 720p, audio = mp3 ElevenLabs, prompt « ONLY X speaks, his mouth moving with the voice… ». **8 rendus, 25 à 97 s chacun, aucune erreur.** Sur les bandes : le locuteur ouvre et ferme la bouche (Garnerin en A, les deux inkmen en B nettement), l'autre reste bouche fermée, le décor et la foule tiennent ; l'aide de P03 étant de dos, S2V n'a que sa tête à animer. Le mp4 porte la voix (CreateVideo avec audio).
* Montages `montage_Style{A,B}_parlant_v4_s2v.mp4` (66 s) : P02 = attente 2 s + S2V badaud 1 (1,6 s) + S2V badaud 2 (2,3 s) + silence 2,5 s = 8,4 s (au lieu de 10), P03 = 2 + 3,8 + 1,3 + 3,5 = 10,6 s (au lieu de 12) : les plans de dialogue raccourcissent à la durée réelle des répliques ; à tenir à 10 / 12 s, on allonge les sous-clips de silence.

Coût du lot : RTX 5090, 45 min, ~0,75 $ ; Higgsfield 8 crédits (solde 882). Total RunPod du jour : 4 pods, ~5,4 $.


## Lot 7 — analyse de l'alignement et deux variantes de dialogue (2026-08-22, 17 h 15 à 18 h 30 UTC, pod A100 `6t4ajf75qe7gdc`)

**Analyse du montage v4 (S2V sur le plan à deux)**, à la demande de Guillaume : énergie audio par demi‑seconde + transcription horodatée ElevenLabs (Scribe v1) + images à 1 et 2 i/s. L'audio est exactement là où le montage le pose (20,56 s, 22,18 s, 29,12 s, 32,96 s). Le décalage est à l'image : **S2V anime la bouche du visage le plus visible, pas celle du locuteur** — pendant la réplique de l'aide (de dos), c'est Garnerin qui articule ; dans P02, le badaud rond chuchote la main devant la bouche sur l'image clé et la bouche du maigre bouge aussi. Bandes : `pilote/_analyse/A_P03_garnerin_28-34s.jpg`, `A_P02_visages_20-24s.jpg`.

**Règle posée par Guillaume** : pas besoin de contrechamp — on garde le plan à deux, mais **un clip par réplique, un seul personnage qui parle par clip**, et dans ce cas S2V n'est plus nécessaire. Deux variantes rendues pour comparaison :

| Variante | Méthode | Montages |
|---|---|---|
| **v5 — I2V, un locuteur par clip** | sous-clips chaînés par dernière image : attente 2 s → locuteur 1 (durée réplique + 0,4 s, « speaks continuously from the first frame to the last ; the other keeps his mouth firmly closed ») → locuteur 2 → silence ; réplique posée au début du sous-clip. Sur les bandes v3 : le rond parle seul puis le maigre seul, bouches ouvertes sur toute la durée du sous-clip. | `montage_Style{A,B}_v5_i2v_un_locuteur.mp4` |
| **v5b — S2V sur champ-contrechamp** | deux nouvelles images clés P02a (le rond seul, main baissée) et P02b (le maigre seul), S2V sur chacune avec sa réplique ; P03 : aide en I2V (de dos), Garnerin en S2V sur le plan à deux. | `montage_Style{A,B}_v5b_s2v_contrechamp.mp4` |

Images P02a/P02b (8 crédits + 1 faux positif nsfw resoumis) : bouches visibles, même décor, même personnage que la fiche ; la foule de fond a disparu sur les plans rapprochés (acceptable). Coût du lot : A100, 1 h 15, ~1,7 $ ; Higgsfield 10 crédits. **Total du jour : RunPod ~7,1 $ (5 pods), Higgsfield 160 crédits (solde 872), ElevenLabs ~120 caractères + 1 transcription.**

## Lot 8 — images clés bouches fermées, cadrages variés, vérification par extraction 1 image/s + Sonnet (2026-08-22 21 h → 2026-08-23 00 h 15 local, pod A100 `mytvzxvlu5mo4a`)

**Déclencheur** : analyse indépendante (agent Sonnet) des 69 images du montage v5 A : bouches de l'auditeur ouvertes (les clés P02/P03 avaient été générées bouches ouvertes), cadrages répétés (1a‑1/1a‑4/4a‑1 ; 1b‑1/4a‑2 ; 4b‑1/4b‑3), saut d'altitude 4a‑1 → 4a‑2, géants sur 4b‑3 A, tête dans un sac sur 4b‑1 A. Guillaume : « tout en un lot ».

**Images (Higgsfield, 16 jobs = 32 crédits, solde 842,44)** : P02, P03 (bouches fermées, mains baissées), 1a‑4 (plan moyen à hauteur de tête sur les dos), 4a‑1 (contre‑plongée du sol, ballon plein cadre, personne), 4a‑2 (trois badauds de dos, ballon juste au‑dessus des arbres), 4b‑3 (beaucoup plus haut, D2 explicité, personne) × A/B. Reprises : 4b‑3 A v2 (la v1 portait un lettrage « D2 » — RÈGLE 28), 4a‑2 A v2 puis v3 (v1 et v2 : les trois badauds en sable / sarcelle / orange vif malgré les négatives → **RÈGLE 30**, couleurs nommées en positif : brun, gris, vert sombre), 1 job failed côté serveur resoumis. Toutes vérifiées sur vignette ; copiées dans `assets/S01E01/pilote/images/`.

**Clips (Wan 2.2 I2V, pod A100 ~2 h 10, ~3 $)** : 16 sous‑clips de dialogue rechaînés depuis les nouvelles clés (`chain_dialogue_runpod.py`, gabarit `talking_solo`) ; clips 1a‑4, 4a‑1, 4a‑2, 4b‑3 × A/B ; 4b‑3 A re‑rendu depuis la v2 ; 4a‑2 A rendu trois fois (une par version d'image). 4b‑1 A relancé (graine décalée) a fait surgir un homme au premier plan : écarté, **version précédente conservée** (`_v3_avant_lot8/`). Montages `montage_Style{A,B}_v6.mp4` (69,5 s, P02 à 18,4 s, P03 à 28,7 s, répliques à 20,86 / 22,48 / 31,16 / 35,02 s).

**Vérification** : `docs/scripts/analyse_montage.py` (1 image/s 640×360 + piste audio + transcription ElevenLabs scribe_v1 horodatée + ligne de temps des plans), puis deux agents Sonnet indépendants, un par style, avec le scénario attendu et la consigne de tout dire. Rapports bruts : `pilote/_analyse/rapport_sonnet_v6A.md` et `rapport_sonnet_v6B.md` ; contrôlés ensuite image par image (planches `_analyse/A_v6_20-37s.jpg`, `B_v6_7-18s.jpg`, `B_v6_28-45s.jpg`).

### Ce que le lot 8 a réglé (vérifié sur les images)
* Sous‑clips d'attente et de silence (P02‑1, P02‑4, P03‑1, P03‑4) : bouches fermées dans les deux styles.
* Audio : les quatre répliques tombent 0,3 s après le début du sous‑clip de leur locuteur, et le locuteur a la bouche ouverte pendant sa réplique (rond A/B 21‑22 s, maigre A/B 22‑24 s, aide B 31‑34 s ; Garnerin A 35‑36 s ambigu à cette échelle).
* Cadrages : 1a‑4 (dos à hauteur de tête), 4a‑1 (contre‑plongée, ballon plein cadre, décollage lisible), 4a‑2 (ballon au‑dessus des arbres ; continuité 4a‑1 → 4a‑2 → 4a‑3 jugée « cohérente et progressive » en B), 4b‑3 (Paris sous la brume, personne) : plus de doublon 1a‑1/4a‑1 ni 1b‑1/4a‑2. Plus de lettrage, plus de géants, plus de tête dans un sac.
* 5‑2 B : une main, un couteau, une corde (conforme).

### Ce qui reste faux (les deux agents, confirmé à l'image)
1. **L'auditeur ouvre encore la bouche pendant que l'autre parle.** P02 : le maigre a la bouche ouverte pendant « Il va se tuer » (A f_021‑022, B f_022) ; en A le rond l'a aussi pendant « Dix francs » (f_023). P03 : le seul visage visible ouvre la bouche pendant la réplique de celui qui est de dos (A : Garnerin pendant l'aide, f_031‑035 ; B : l'aide pendant « Lâchez tout », f_036‑037). Les clés bouches fermées ont réglé l'attente et le silence, **pas la réplique** : la ligne `talking_solo` (« the other keeps his mouth firmly closed ») n'est pas obéie par Wan 2.2 quand un visage est animé dans le cadre. **Le contrôle par le texte ne suffit pas pour tenir une bouche fermée.**
2. **Sur P03, un des deux locuteurs est de dos dans chaque style** (A : l'aide ; B : Garnerin, donc « Lâchez tout » sans bouche visible) — c'est la composition des clés validées. Sur un plan à deux « un locuteur par clip », les deux visages doivent être visibles.
3. **P02‑4 A** : pendant la réaction, le rond se retourne complètement (dos à la caméra, f_028‑029), mouvement non demandé.
4. **P4a‑1 B** : au décollage, une foule surgit et court au premier plan (f_043‑044) malgré `Characters: none` et les négatives de présence ; P4a‑1 A : une main sort du buisson à droite (f_044). Le style B reste le plus sujet aux personnages surgis.
5. **4b‑1 / 4b‑3 A** restent voisins (même plongée, même parc vert à la même place) malgré le recadrage « beaucoup plus haut » : le modèle garde la composition de D02. Un vrai changement demanderait une autre plaque de décor (D02 bis, Paris dans la brume sans le parc).
6. **Plans FIXE lus comme figés** : 4b‑1, 4b‑2, 4b‑3 (A), 4a‑2, 4b‑3, 5‑1/5‑2 (B) : 3 s sans mouvement perceptible. C'est le découpage (plans FIXE, mouvements de caméra au montage final), mais un œil extérieur le lit comme une panne ; à traiter au montage final (travellings/zooms) ou par un peu de vie dans le prompt.
7. **Style B vu de l'extérieur** : « trois styles de visages » dans le même film (foule à têtes vierges, parieurs « rage comic », Garnerin/aide à visage rond) — parti pris de la fiche B, perçu comme une incohérence par un relecteur qui ne connaît pas la bible.
8. 5‑2 A : deux mains sur le couteau et 2‑3 brins de corde (la reprise du lot 6 avait accepté « deux mains dans la même manche ») ; 5‑3 A : petit signe en « 9 » près de la lame (à vérifier en HD).

### Erreurs des relecteurs, à ne pas reprendre
* Le scénario que j'ai donné aux agents disait « P5 : le parachute s'ouvre, descente » et « P1b : Garnerin dans la nacelle » : faux — dans le pilote, P5 = la corde coupée (5‑1 couteau, 5‑2 coupe, 5‑3 rupture, D2 derrière) et 1b‑1 = la foule qui s'ouvre en haie, 1b‑2/3 = la nacelle portée. Les verdicts « climax absent » et « P1b‑1 ne montre pas la nacelle » sont des erreurs de consigne, pas de rendu.
* Agent A : « f_023‑029 vus de dos, impossible de vérifier » — faux, f_023‑027 montrent les deux visages (seuls f_028‑029 sont de dos).
* Agent B : « P4a‑2 montre toute la foule, pas trois badauds » — la clé B montre trois badauds au premier plan et la foule derrière (conforme à la brique).

### Bilan
Le lot 8 a corrigé tout ce qui se corrigeait à l'image clé (bouches au repos, cadrages, altitude, lettrage, couleurs) ; le défaut qui reste est **structurel au procédé « I2V un locuteur par clip » : Wan 2.2 ne tient pas une bouche fermée sur commande textuelle**. Trois sorties, à trancher par Guillaume : (a) **compositing au montage** sur plan fixe — la moitié d'image de l'auditeur est prise dans le sous‑clip de silence (bouche fermée garantie), fondu vertical au milieu ; gratuit, déterministe, marche sur P02 et P03 où les deux personnages ne se chevauchent pas ; (b) **S2V en champ‑contrechamp** (v5b, déjà rendu) : la seule méthode qui anime la bonne bouche, au prix d'un contrechamp par réplique ; (c) accepter le défaut pour le pilote. Recommandation : (a) pour le pilote, avec P03 recadré pour que les deux visages soient visibles ; (b) pour l'épisode si le lipsync est finalement accepté.

Coût du lot : Higgsfield 32 crédits (solde 842,44) ; RunPod ~3 $ (pod terminé 20:14 UTC, aucun pod actif) ; ElevenLabs 2 transcriptions. **Totaux pilote : Higgsfield 190 crédits, RunPod ~10 $ (6 pods), ElevenLabs ~120 caractères TTS + 4 transcriptions.**

## Essais E1 à E4 — InfiniteTalk, trois samplers, LTX‑2.3, MiniMax H3 (2026-08-23, 00 h 30 → fin de nuit, pod A100 `vzplffsbl41u1m`)

Demande de Guillaume : « faisons les 3 tests » puis « ajoute un 4ᵉ test avec MiniMax H3 en I2V et R2V ». Livrables : quatre vidéos de comparaison dans `pilote/essais/_videos/` (`E1_infinitetalk_dialogues.mp4`, `E2_trois_samplers.mp4`, `E3_ltx23_vs_wan22.mp4`, `E4_minimax_h3.mp4`), assemblées par `pilote/essais/build_compare.py`. Scripts capitalisés : `docs/scripts/run_infinitetalk_runpod.py`, `run_e2_trois_samplers.py`, `run_ltx23_runpod.py`, `run_minimax_h3_runpod.py`, `comfy_ui_to_api.py` (convertisseur UI→API, non utilisé finalement : les templates à sous-graphes ont été réécrits à la main depuis leur dump), `docs/runpod/bootstrap_pod_essais_E123.sh`.

**Préparation** : P03 refait en A et B avec **les deux visages visibles** (brique v3 « medium two shot from the side… BOTH FACES FULLY VISIBLE », bloc `AIDE_FACE` ; 4 crédits, solde 838,44) ; pistes audio par locuteur pré‑alignées (silence là où l'autre parle : P02 = BADAUD1 à 2,0 s puis BADAUD2 à 3,64 s, total 7,9 s ; P03 = AIDE à 2,0 s puis GARNERIN à 5,96 s, total 9,18 s) ; masques rectangulaires par locuteur (`essais/E1/masques/`) ; pod A100 80 Go avec disque conteneur 250 Go (~170 Go de modèles : Wan 2.1 I2V 14B 720p fp8 + InfiniteTalk multi + Wan 2.2 + LTX‑2.3 + MiniMax H3).

### E1 — InfiniteTalk multi‑locuteurs (Wan 2.1 I2V 14B 720p, nœuds Kijai)
* Graphe : `WanVideoModelLoader` (fp8, LoRA lightx2v T2V rank32 force 1, `multitalk_model` InfiniteTalk‑Multi fp16) ; `MultiTalkWav2VecEmbeds` (wav2vec2 chinois, 2 pistes, **mode `para` avec pistes pré‑alignées**, `ref_target_masks` = 2 masques par `MaskBatchMulti`) ; `WanVideoImageToVideoMultiTalk` (1280×720, fenêtre 81, motion_frame 9, mode infinitetalk) ; `WanVideoSampler` 6 pas cfg 1 shift 11 dpm++_sde ; `CreateVideo` 25 i/s avec le mix audio.
* Temps : 197 images = 3 fenêtres × 6 pas × ~75 s ≈ **22 min par plan de 8 s** sur A100 (≈ 0,5 $ le plan). 229 images (P03) ≈ 26 min.
* **Résultat P02 A et B (planche 1 image/s)** : personne ne parle 0‑2 s bouches fermées ; **2‑3 s le rond parle, le maigre garde la bouche fermée ; 4‑5 s le maigre parle, le rond garde la bouche fermée** ; silence final bouches fermées. Les corps bougent (mains, tête), le décor et la foule tiennent, le style A et le style B tiennent (B : bouches inkman dessinées par le modèle, lisibles). C'est la première fois que l'auditeur se tait.
* **P03 A et B (clés v3, deux visages)** : premier rendu faux par ma faute (piste AIDE liée au masque de Garnerin : l'ordre des pistes doit suivre l'ordre des masques, pas la position à l'image) → refait avec les masques inversés ; résultat : l'aide (à droite) parle 2‑5 s bouche ouverte, Garnerin bouche fermée, puis Garnerin dit « Lâchez tout » 6‑7 s, l'aide bouche fermée, en A comme en B. **Défaut : sur P03 A une voiture moderne traverse le fond à partir de 4 s** (hallucination Wan 2.1 sur un fond de rue ; à bannir par la négative « car, vehicle, modern object ») ; P03 B : Garnerin porte une perruque blanche sur la clé v3 (dérive de la clé, pas du clip)
* Limites vues : base Wan 2.1 (rendu un peu plus doux que 2.2) ; 4 plans = 1 h 35 de GPU ; l'audio dans le mp4 est notre mix, pas une resynthèse.

### E2 — Wan 2.2 I2V, trois samplers (premier pas haut‑bruit sans LoRA)
* 8 pas : 0→1 haut‑bruit **sans LoRA**, 1→4 haut‑bruit LoRA 0,8, 4→8 bas‑bruit LoRA 1 ; deux variantes du cfg du premier pas : **3,5** (recommandation communautaire) et **2,0**. Temps ×3 (≈ 3 min par clip au lieu de 70 s).
* 4b‑2 A et 5‑2 A : **cfg 3,5 décale les couleurs** (osier jaune saturé sur 4b‑2, image qui s'assombrit sur 5‑2) ; **cfg 2,0 garde les couleurs** de la référence. Le gain de mouvement est faible sur ces deux plans (la main serre le rebord, la lame avance un peu plus) — à juger sur la vidéo côte à côte. Pas de personnage surgi.

### E3 — LTX‑2.3 I2V (LTX‑2.5 prévu : dépôt Hugging Face **gated**, fichiers vides ; LTX‑2.3 via les miroirs Comfy‑Org / Lightricks‑fp8, ouverts)
* Graphe = template officiel à deux passes (demi‑résolution 8 sigmas, upsampler latent ×2, 3 sigmas), checkpoint dev fp8 + LoRA distillée 0,5, gemma‑3‑12B fp4, négatif sans « cartoon » ; 1280×704, 25 i/s, 81 et 105 images ; LTX génère aussi une piste audio.
* **Premier lancement : ComfyUI s'est arrêté net** (processus mort sans traceback) au chargement/sampling de LTX (LTXAV 23,8 Go + encodeur 11,2 Go), la file a été perdue et tous les jobs en attente ont dû être resoumis. Relancé **en dernier** dans la file : relancé en dernier dans la file, les deux clips (1a‑2 : 81 images, 4a‑3 : 105 images, 1280×704, 25 i/s) sont sortis en ~1 min chacun sans incident ; le style A tient, le ballon bouge (1a‑2 se soulève un peu trop, 4a‑3 monte et s'éloigne), LTX ajoute une piste sonore d'ambiance ; à comparer côte à côte dans `E3_ltx23_vs_wan22.mp4`

### E4 — MiniMax H3 (poids ouverts, natif ComfyUI), I2V et R2V, 1344×768, 24 i/s, LoRA turbo
* I2V (`MiniMaxH3ImageToVideo`, 8 pas) : 1a‑2 (73 images, ~3 min), 4a‑3 (107 images, ~4 min), P02 (192 images, ~10 min) ; R2V (`MiniMaxH3ReferenceToVideo`, 4 pas) : P02 avec l'image clé en `ref_image_0` et **nos deux mp3 ElevenLabs en `ref_audio_0/1`** (~5 min). Les entrées « autogrow » s'écrivent `ref_images.ref_image_0` / `ref_audios.ref_audio_0` au format API.
* **Style** : H3 garde le dessin A (traits, palette, foule) sur les quatre clips ; 4a‑3 monte et s'éloigne, 1a‑2 balance le ballon et la foule frémit.
* **Dialogue I2V** (répliques écrites dans le prompt, H3 synthétise les voix) : transcription ElevenLabs du rendu = « Il va se tuer, va se tuer, je vous dis » (3,0‑4,8 s) puis « Dis Franck, il ne coupe pas la corde » (5,2‑6,7 s) **plus une phrase inventée** (« Love loves you, mais sa dent… », 1,1‑2,5 s) ; voix françaises plausibles mais texte approximatif ; à l'image le rond parle bouche ouverte pendant sa réplique, le maigre ensuite.
* **Dialogue R2V** (nos voix en référence) : H3 **ne recopie pas l'audio**, il **resynthétise** dans un timbre proche : « …vous dit : Il va se tuer. Je vous assure encore. » puis « …dix francs qui coupe pas la corde » ; le maigre ouvre la bouche pendant la seconde réplique (5‑7 s), le rond pendant la première. Pas de réplique inventée, mais le texte n'est pas exact.
* Donc : H3 est un vrai moteur **image + voix en une passe** qui tient notre style, mais **il ne garantit ni le texte ni la voix** (les répliques dérivent) ; InfiniteTalk garde notre audio tel quel.

### Synthèse pour Guillaume
| Essai | Ce qu'il apporte | Ce qu'il coûte | Verdict provisoire |
|---|---|---|---|
| E1 InfiniteTalk | l'auditeur se tait, le locuteur articule sur **notre** voix, un seul rendu par plan, A et B | ~22 min A100 par plan de 8 s (~0,5 $), base Wan 2.1 | **candidat pour tous les plans de dialogue** |
| E2 trois samplers | un peu plus de vie sur les plans fixes, couleurs tenues à cfg 2,0 | ×3 en temps | à adopter si la vidéo confirme, avec cfg 2,0 |
| E3 LTX‑2.3 | moteur alternatif avec audio | crash ComfyUI au premier essai | relancé en dernier dans la file, les deux clips (1a‑2 : 81 images, 4a‑3 : 105 images, 1280×704, 25 i/s) sont sortis en ~1 min chacun sans incident ; le style A tient, le ballon bouge (1a‑2 se soulève un peu trop, 4a‑3 monte et s'éloigne), LTX ajoute une piste sonore d'ambiance ; à comparer côte à côte dans `E3_ltx23_vs_wan22.mp4` |
| E4 MiniMax H3 | style tenu, voix générées, vitesse honnête (~1 min/s) | répliques et voix non fidèles, 1344×768 | moteur intéressant pour des plans muets ou d'ambiance ; pas pour nos dialogues écrits |

Coût de la nuit : pod A100 `vzplffsbl41u1m` créé 20:55 UTC le 22, terminé ~02:55 UTC le 23 : ~6 h à 1,39 $/h ≈ 8,3 $ (dont ~1 h de téléchargements et un rendu P03 perdu) ; total RunPod du pilote ≈ 18 $ (7 pods). Higgsfield : 4 crédits (solde 838,44). ElevenLabs : 2 transcriptions de contrôle.

## Deuxième série d'essais (2026-08-23, journée, pod A100 `sjj6j8nk2dbqk3` + Higgsfield)

Retours de Guillaume sur la première série : voiture sur P03 A ; « pourquoi une couverture ? » ; style B mal aligné ; parasites H3 en français ; LTX‑2.5 gated ; puis jeton Hugging Face fourni, « tente aussi Seedance 2.0 Mini, Wan 2.7, Veo 3.1 Lite, Kling 3.0 », et « utilise le skill du dépôt MiniMax‑H3 pour prompter correctement ».

### P03 réécrit autour de l'action (v4)
Brique, scénario, plan de production, sujets des sous‑clips et METHODE modifiés (commit `f2c4487`) : Garnerin **la main sur la corde de largage, regard vers le ballon**, l'aide au rebord qui supplie, la soie pliée **au sol**, les deux visages visibles, **bouches inkman dessinées en trait** (blocs B). Images v4 A et B rendues du premier coup (4 crédits) et validées ; copiées dans `assets/`.

### E1b — InfiniteTalk sur P03 v4 (A, B) et P02 B masques tête
* Négative enrichie (`car, cars, vehicle, carriage, modern object, anachronism, extra person`) ; masques : piste 1 (AIDE) → masque de l'aide à droite, piste 2 (GARNERIN) → masque de Garnerin à gauche (l'ordre des pistes suit l'ordre des masques).
* **P03 v4 A** : l'aide parle 2‑5 s bouche ouverte, Garnerin main sur la corde bouche fermée, puis Garnerin dit « Lâchez tout » ; **plus de voiture**. **P03 v4 B** (audio_scale 1,6, bouches en trait) : l'aide inkman ouvre une bouche « o » pendant sa réplique, Garnerin fermé, puis Garnerin ouvre la bouche sur « Lâchez tout » ; défaut : une petite sphère claire apparaît dans la main de l'aide à 7‑8 s (hallucination).
* **P02 B masques tête + audio_scale 2** : masques serrés sur les têtes + audio_scale 2 : les bouches inkman s'ouvrent nettement sur la réplique de chacun (le rond à 2‑3 s, le maigre à 4‑5 s) et restent fermées sinon ; c'est plus lisible que la v1 (masques tête+torse, audio_scale 1) — à confirmer à l'oreille sur E1b
* Temps : ~30 min par plan de 9 s (4 fenêtres), ~22 min pour 8 s.

### E3b — LTX‑2.5 I2V (jeton HF de Guillaume)
* Téléchargement avec `Authorization: Bearer` (transformer int8 21,5 Go, gemma4‑12b 15,4 Go, 2 VAE, upsampler spatial dans `latent_upscale_models/`) ; graphe = template officiel réécrit en API (`run_ltx25_runpod.py`, deux passes, `LTXVDualCFGGuider`, euler_ancestral).
* Résultat : 1a‑2 et 4a‑3 propres (le ballon monte, la foule frémit, audio d'ambiance généré) ; P02 parlé : voix françaises générées, « Il va se tuer, je vous dis » exact puis « Dis Frank qu'il ne coupe pas la corde » (même déformation de « Dix francs » que H3), et **LTX ajoute une coupe** vers 6 s (contre‑plongée derrière les badauds) malgré « single continuous shot » ; ~1 min par clip sur A100, aucun crash cette fois

### E4b / E4c — MiniMax H3 : la langue et la syntaxe
* **E4b, répliques en anglais** (prompt « timeline » de la veille) : transcription **exacte** « He is going to kill himself, I tell you. / Ten francs he does not cut the rope. », aucun parasite → les parasites de la veille venaient de la langue **et** de la syntaxe.
* **E4c, prompts réécrits selon le skill `h3-prompt-writing` du dépôt MiniMax‑H3** (format `integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music`, locuteurs `(S1)`/`(S2)` définis par timbre, dialogue `<d>[French] …</d>`, R2V en six sections avec `<Subject n>`, `<Picture 1>`, `<Audio n>` « referenced for voice timbre ») : **plus de phrase inventée** ; « Il va se tuer, je vous dis. » exact en I2V comme en R2V ; la seconde réplique reste déformée sur le chiffre (« Dis Franck, il ne coupe pas la corde » / « Dis‑toi qu'il ne coupe pas la corde ») — H3 bute sur « Dix francs » en français (nombre + nom propre), pas sur la phrase. Règle : **toujours écrire les prompts H3 dans le format du skill, dialogue entre `<d>[French] … </d>`, locuteurs (S1)/(S2) décrits par timbre** ; épeler les nombres en toutes lettres est à essayer (« dix francs » → « dix » est déjà un mot ; le problème est peut‑être la liaison « dix‑francs‑qu'il »).

### E6 — modèles fermés via Higgsfield (P02 A, 8 s, 720p, même image clé, même dialogue)
| Modèle | Crédits | Voix | Transcription de la sortie | Remarques |
|---|---|---|---|---|
| **Veo 3.1 Lite** (+audio) | 12 | générées | « Il va se tuer, je vous dis. » / « D'un franc qu'il ne coupe pas la corde » | bouches alternées propres, style A tenu, le plus fluide |
| **Wan 2.7** (start_image, `[Character n] says`) | 12 | générées | « Il va se tuer, je vous dis. Dix francs qu'il ne coupe pas la corde » — **exact** | accepte **au plus 1** référence audio ; l'essai avec 1 mp3 a **échoué côté serveur** (facturé), relancé sans référence |
| **Kling 3.0 std** (sound on) | 16 | générées | « Il va se tuer, je vous dis. Dis Franck qu'il ne coupait pas la corde » | bouches OK, 2ᵉ réplique déformée |
| **Seedance 2.0 Mini** (+audio) | 20 | générées | « Il va se tuer, je vous dis. Dix francs qu'il ne coupe pas la corde » — **exact** | l'essai avec 2 `audio_references` a **échoué côté serveur** (facturé), relancé sans référence |
Aucun des quatre n'a donc été testé **avec nos voix ElevenLabs en référence** : Wan 2.7 n'en prend qu'une, Seedance a planté avec les mp3 (à retenter en wav ?). Solde Higgsfield : 736,44 (−102 crédits sur cette série, dont ~32 pour les deux échecs).

### Bilan de la journée pour le dialogue
| Méthode | Voix = les nôtres (ElevenLabs) ? | Auditeur se tait ? | Texte exact ? | Coût P02 8 s | Défauts vus |
|---|---|---|---|---|---|
| InfiniteTalk (E1/E1b) | **oui** | oui | oui (c'est notre audio) | ~0,5 $ (22 min A100) | hallucinations de fond possibles (voiture, sphère) ; B moins net |
| MiniMax H3 (E4c, bon format) | non (timbre référencé seulement) | oui | presque (« Dix francs » déformé) | ~10 min A100 ≈ 0,25 $ | style tenu |
| Veo 3.1 Lite | non | oui | presque | 12 cr ≈ 0,6 $ | — |
| Wan 2.7 | non | oui | **oui** | 12 cr ≈ 0,6 $ | 1 seule réf audio |
| Seedance 2.0 Mini | non | oui | **oui** | 20 cr ≈ 1 $ | plante avec nos mp3 |
| Kling 3.0 | non | oui | non | 16 cr ≈ 0,8 $ | — |
| LTX‑2.5 | non | ? | 1a‑2 et 4a‑3 propres (le ballon monte, la foule frémit, audio d'ambiance généré) ; P02 parlé : voix françaises générées, « Il va se tuer, je vous dis » exact puis « Dis Frank qu'il ne coupe pas la corde » (même déformation de « Dix francs » que H3), et **LTX ajoute une coupe** vers 6 s (contre‑plongée derrière les badauds) malgré « single continuous shot » ; ~1 min par clip sur A100, aucun crash cette fois | ~0,1 $ | — |

Vidéos : `essais/_videos/E1b_infinitetalk_v4.mp4`, `E3b_ltx25.mp4`, `E6_modeles_fermes.mp4` (Veo, Wan 2.7, Kling, Seedance, H3 anglais), `E4c` dans `E4c_h3_francais.mp4`. Coût : pod A100 sjj6j8nk2dbqk3 (~4 h dont 40 min de téléchargements) ≈ 5,5 $ ; total RunPod du pilote ≈ 24 $ (9 pods) ; Higgsfield −106 crédits (4 + 102), solde 736,44.

## E7 — les plans muets les plus difficiles en Wan 2.2 | LTX‑2.5 | MiniMax H3, styles A et B (2026-08-23, soir, pod RTX PRO 6000 `ssl54yh5es66oo`)

Question de Guillaume : faut‑il encore garder Wan 2.2, ou tout basculer sur H3 ou LTX‑2.5 ? Essai sur les 6 plans muets qui ont le plus résisté à Wan 2.2 (1a‑1, 4a‑1, 4b‑1, 4b‑3, 5‑2, 5‑3) × A/B, mêmes clés, sujets et caméra repris des prompts Wan, prompts courts (LTX : texte libre + négative anti‑coupe/anti‑anachronisme ; H3 : format du skill, « Nobody speaks »). 24 clips, aucune erreur ; LTX‑2.5 ≈ 1 min le clip, H3 ≈ 1,5‑3 min (RTX PRO 6000 à 2,09 $/h, seule carte disponible ; ~1 h 40 de pod ≈ 3,5 $ dont 40 min de téléchargement). Vidéo : `essais/_videos/E7_muets_wan22_ltx25_h3.mp4` (A puis B, 3 colonnes par plan).

Ce que je vois sur les planches (à confirmer par Guillaume sur la vidéo) :
* **LTX‑2.5** : propre sur les 12 — 4a‑1 B : le ballon décolle, **personne ne surgit** (là où Wan 2.2 faisait courir une foule) ; 4b‑1 A : nacelle et toits nets (Wan 2.2 fait apparaître une petite tête au rebord) ; 5‑2 A : la lame scie, les fibres sautent ; 1a‑1 B : brume et foule de dos, rien d'inventé ; cadrages et style tenus ; audio d'ambiance généré (vent, murmure).
* **MiniMax H3** : style tenu mais **hallucine sur les plans muets** : 4a‑1 B, une tête d'inkman géante entre au premier plan et le ballon se déforme ; 5‑2 A, des débris de corde volent en l'air ; 4b‑1 A et 1a‑1 B propres. Plus lent que LTX.
* **Wan 2.2** (référence) : les défauts connus (foule surgie 4a‑1 B, tête au rebord 4b‑1 A), le reste correct.

Conclusion proposée : **LTX‑2.5 pour tous les plans muets** (vitesse, propreté, FLF2V natif, audio d'ambiance), Wan 2.2 n'est plus nécessaire ; pour les dialogues, H3 (timbre de nos voix en R2V) ou LTX‑2.5 (voix libres, parfois une coupe ajoutée) selon le choix de Guillaume. Le montage v7 peut donc être rendu entièrement sans Wan 2.2, à 24 i/s.

## E8 — voix cohérentes avec LTX‑2.5 : IA2V « audio gelé » et ID‑LoRA + LTXVReferenceAudio (2026-08-23, soir, pod A100 SXM `fkf9sa9mzl9r9b`)

Demande de Guillaume : « comment avoir des voix cohérentes avec LTX‑2.5, peut‑être via LTXVSetAudioRefTokens ? » puis « lance pour qu'on teste et valide ». Recherche en ETAT § 7 ; graphes dans `docs/scripts/run_ltx_voix_runpod.py` ; bootstrap `docs/runpod/bootstrap_pod_essais_E8.sh` (LTX‑2.5 + LTX‑2.3 + ID‑LoRA talkvid). **`LTXVSetAudioRefTokens` n'existe pas dans le cœur de ComfyUI** (nœud du paquet Lightricks) : la voie officielle « audio gelé » se fait avec `LTXVAudioVAEEncode → SetLatentNoiseMask (SolidMask à 0) → LTXVConcatAVLatent` dans les deux passes, euler, CFG 1/1 — c'est le template « LTX‑2.3 Image Audio to Video » transposé sur 2.5 ; `LTXVReferenceAudio` est natif.

### Résultats
* **IA2V audio gelé, P02 A et B, P03 A (nos mix ElevenLabs pré‑alignés)** : la piste audio de sortie **est exactement la nôtre** (transcription mot pour mot, mêmes horodatages : 2,00 s et 3,70 s sur P02 ; 2,06 / 6,06 s sur P03) ; à l'image, le rond ouvre la bouche sur sa réplique et le maigre sur la sienne (A et B), l'aide sur la sienne puis Garnerin sur « Lâchez tout » (P03 A). Donc **voix verrouillées + lèvres qui suivent, sur le moteur retenu** — c'est ce qu'InfiniteTalk promettait, en ~3,5 min par plan de 8 s sur A100 et sans masque. Défaut : **P02 B : LTX ajoute une coupe vers 5‑6 s** (plan de dos sur la foule) malgré « single continuous shot, no cut » + négative ; P02 A et P03 A : pas de coupe.
* **ID‑LoRA talkvid + `LTXVReferenceAudio` sur LTX‑2.5** (référence ElevenLabs de 6‑7 s, identity_guidance 2, LoRA et référence en première passe seulement) : **le graphe tourne sur 2.5 sans erreur** (le LoRA 2.3 s'applique) ; voix françaises générées (les deux répliques, timbre à juger à l'oreille — grave vs clair) ; **dans les deux rendus LTX ajoute une coupe vers 5‑6 s** ; une seule référence par rendu → une voix par génération (les deux personnages partagent le timbre, ou le modèle en invente un second).
* Témoin E3b (voix libres) : déjà vu, coupe aussi.

### Ce que ça établit
1. Pour garder **les voix ElevenLabs** (et leur verrouillage d'identité) avec LTX‑2.5 : **IA2V audio gelé** — validé techniquement sur trois plans ; à généraliser après l'avis de Guillaume.
2. Pour des voix **générées mais stables**, `LTXVReferenceAudio` + ID‑LoRA marche sur 2.5 mais une voix par rendu : utile pour un monologue, pas pour un plan à deux.
3. **LTX‑2.5 insère une coupe vers 5‑6 s sur P02 dans 4 rendus sur 5** (multishot natif) : à tenir par le prompt (moins de « then… then… », une seule phrase d'action continue), par la négative, ou en coupant les plans de dialogue en deux rendus plus courts ; à traiter avant le montage v7.

Coût : pod A100 SXM 1,59 $/h, ~1 h 15 dont 45 min de téléchargement ≈ 2 $ ; ElevenLabs 2 références (~230 caractères) ; 0 crédit Higgsfield. Vidéo : `essais/_videos/E8_voix_ltx25.mp4`.
