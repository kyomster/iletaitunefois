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
