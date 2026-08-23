# Épreuve de style D à K — audit des 24 images

**23 août 2026.** Grille : les 13 contrôles de `METHODE-generation-images.md` §20, plus les 8 contrôles de `PLAN-styles-D-E-F.md` §7. Images lues une par une en 1100 px de large, fichiers dans `assets/S01E01/pilote/images/Style*/`, toutes en 2752 × 1536.

Deux lots. Sections 1 à 9, les six premiers styles D à I. Section 10, les deux styles réalistes J et K, ajoutés après.

**Décision du 23 août, définitive** : E, F, H, puis G et I sont abandonnés, leurs images supprimées du dépôt. Leur audit reste ici, sections 3 à 7, pour ne pas repayer les mêmes constats. **Restent D, J et K.**

Ce que le trio retenu a en commun, et qui n'est dans aucune case de la grille : ce sont les **trois styles à visage crédible et lumière cinématographique** du lot. D en est la version dessinée, K la version animée en volume, J la version photographiée. Les cinq écartés étaient tous des styles à forme affirmée. Le choix penche donc vers le **récit** plutôt que vers le gag graphique, et cela déborde la question du style : le scénario, les quatorze gags et le découpage ont été écrits pour l'autre registre.

---

# 1. Le constat transversal, avant tout verdict de style

## 1.1 P1a-3 a raté dans les six styles, et la faute est dans le prompt, pas dans les styles

**Aucune des six images P1a-3 n'est une contre plongée sous la couronne du ballon.** Les six donnent un plan large ou un trois quarts du ballon entier, vu du sol ou de loin. Six styles sur six qui échouent sur le même plan : par la RÈGLE 7, la cause est dans le prompt.

Elle est identifiée. La brique dit `Framing: low angle from the ground toward the crown of the balloon` et `Decor: D1, sky and treetops only`. Dans les prompts A, B et C, `D1` est un **code**, et la plaque D01 est réinjectée à côté ; la clause `sky and treetops only` suffit alors à cadrer haut. Ici, faute de plaque D à I, j'ai développé le code en clair, et la description de D1 dit `very wide establishing shot with a slight high angle`. Le prompt contient donc **deux cadrages contradictoires**, un contre plongée serré et un plan large en légère plongée. Le modèle a tranché pour le second, six fois sur six.

C'est le mécanisme exact de la RÈGLE 23, une clause invariante qui contredit une clause variable. **Le développement d'un code de décor doit être amputé de sa clause de cadrage.** Proposition d'entrée en méthode :

> **RÈGLE 32** — quand on développe un code de décor en clair faute de plaque à réinjecter, on retire de la description toute clause de cadrage, d'axe et d'échelle. Une plaque de décor n'impose pas son cadrage quand elle est réinjectée comme image ; sa description, elle, l'impose comme texte.

Conséquence pratique : **P1a-3 n'est pas exploitable comme discriminant de cadrage**. Il reste exploitable comme discriminant de trait, de palette et de traitement des bannières, ce qui est déjà l'essentiel de ce qu'on lui demandait.

## 1.2 Ce qui est propre sur les 18

* **Aucun lettrage nulle part.** La négative universelle tient dans les six styles, y compris en H dont l'idiome d'imprimé appelait pourtant le texte.
* **Aucun visage vide.** Le défaut qui a tué le style C ne s'est reproduit dans aucun style, ni en D où j'avais changé la clause de foule, ni dans les cinq où je l'avais gardée telle quelle. **Résultat utile : la clause positive de foule des styles A, B et C est sûre quel que soit le style.** Le remplacement fait en D n'était pas nécessaire, et il n'a d'ailleurs pas pris : la foule D est nette et non floue.
* **Aucune couleur réservée en dominante**, à une réserve près, le gilet ocre du badaud rond en style I, section 7.
* **Aucun accessoire dupliqué**, canne unique et chapeau à cocarde unique dans les six P02.
* **Bouches fermées** sur les six P02, RÈGLE 31 respectée partout.

## 1.3 Deux défauts de forme à corriger avant l'étape suivante

* **Style F, bandes noires incrustées** en haut et en bas de P1a-3 et de P4b-1. Contrôle 10, plein cadre : l'image n'occupe pas le cadre. À corriger par une négative `letterbox bars, black bars, cinemascope bars` sur le style F.
* **Style I, cadre dessiné et marge crème** autour de P02. Violation directe de la négative universelle, qui contient déjà `border, frame, margin`. La négative n'a pas suffi : c'est l'idiome du roman graphique qui ramène la case. À corriger en positif, `the drawing bleeds to all four edges of the frame`, et non en allongeant la liste `Avoid:` (RÈGLE 3).

---

# 2. Style D — anime d'aventure

| Contrôle | Verdict |
|---|---|
| Style conforme au bloc | ✔ trait fin brun, ombrage adouci, décor peint, profondeur de champ, grain |
| **Deux registres distincts** (contrôle 2) | ✔ **franchement**. P4b-1 en TENSION est ambre chaud à contre jour, sans rapport avec le bleu des deux images JOUR. Le traitement de lumière prend. |
| Foule | ✔ aucun visage, mais **de dos et nette**, pas en silhouettes floues comme prescrit |
| Personnages | ✔ visages détaillés, cocarde, canne, bouches fermées |
| Décor D1 | **✘ l'aube d'octobre et la brume ont disparu** : ciel bleu franc, gros cumulus, plein midi |

**Le défaut de fond de D** : le traitement de lumière JOUR a écrasé l'heure décrite par le décor. `bright daylight, saturated blue sky with tall billowing cumulus` bat `October dawn, low mist`. Sur un pilote dont les six plans sont à l'aube, c'est bloquant tel quel. Corrigeable en amputant le traitement JOUR de sa clause de ciel, ou en le réservant aux plans qui ne sont pas à l'aube.

**P4b-1 est la meilleure image D des trois**, et l'une des trois meilleures des dix huit.

**Verdict : validable, avec une correction du traitement JOUR à faire avant l'étape 4.**

---

# 3. Style E — 2D graphique angulaire

| Contrôle | Verdict |
|---|---|
| **Trois ou quatre couleurs** (contrôle 1) | ✔ ocre, ardoise, gris, crème. Rien d'autre. |
| **Pas de contour épais partout** | ✔ les aplats sont majoritairement sans cerne |
| Formes anguleuses | ✔ franchement, y compris les arbres et l'architecture réduits à des masses |
| Foule | ✔ **exemplaire**, silhouettes plates de dos, aucun visage |
| Grands vides | ✔ |

**E n'est pas le style A recoloré.** Le contrôle 1 est passé sans ambiguïté : c'est un style à part entière, et c'est visuellement le plus affirmé des six.

**Sa question de fond n'est pas dans la grille, et elle est sérieuse.** Sur P02, les deux badauds ont des yeux réduits à **une ligne fermée et une entaille sombre**. Ce n'est pas le défaut du style C, ce ne sont pas des ovales vides, c'est le bloc lui même qui prescrit `faces reduced to a few deliberate shapes with minimal interior detail`. Mais sur 79 plans dont quatorze gags et un dialogue continu, **un visage à ce degré de réduction ne portera pas l'expression**. C'est exactement le reproche fait au style B par le relecteur extérieur, sous une autre forme.

**Verdict : validable graphiquement, à ne pas avancer sans une épreuve d'expression** — les six têtes de la bible, joie, surprise, sceptique, inquiétude, rire, avant tout engagement.

---

# 4. Style F — 3D stylisé facetté

| Contrôle | Verdict |
|---|---|
| **Glissade vers le photoréalisme** (contrôle 3) | ✔ sur P02 : peau mate, aucun reflet spéculaire, plans facettés nets, trame du gilet visible. **✘ sur P1a-3** : arbres et château rendus, plus peints que facettés |
| Identité du style | **✘ n'existe que là où il y a des personnages.** P1a-3 et P4b-1 sans figure sont des rendus 3D quelconques, indiscernables d'un autre parti pris |
| Décor D1 | ✘ deux **hangars en bois** à gauche et à droite sur P02, absents de Parc Monceau |
| Plein cadre (contrôle 10) | ✘ bandes noires incrustées sur deux images sur trois |

**Verdict : le plus faible des six.** Sa marque distinctive tient dans les visages, donc dans une minorité des 79 plans, et deux images sur trois sortent avec un défaut de forme. À écarter, sauf si le parti pris marionnette vous tient à cœur pour des raisons qui ne sont pas dans ces images.

---

# 5. Style G — 3D cartoon rond

| Contrôle | Verdict |
|---|---|
| **F contre G se distinguent ils** (contrôle 4) | ✔ **sans la moindre ambiguïté**. Aucun angle vif nulle part, volumes ronds, surfaces lisses et mates |
| Photoréalisme | ✔ aucun pore, aucun reflet gras |
| Foule | ✔ de dos, aucun visage |
| **Décor D1** | ✔ **le seul des six styles à rendre l'aube d'octobre, la brume basse et les rotondes de Parc Monceau** |
| Personnages | ✔ cocarde, canne, bouches fermées, silhouettes contrastées et lisibles |

Écart mineur au bloc : les têtes ne sont pas surdimensionnées, les proportions sont celles d'une caricature adulte plutôt que d'une grosse tête sur petit corps. Ce n'est pas un défaut, c'est même plutôt heureux pour le sujet.

**P02_StyleG est l'image la plus aboutie des dix huit** : c'est la seule qui ressemble à un plan de série finie plutôt qu'à une épreuve.

**Verdict : le plus solide des six.** Et c'est le seul où la troupe se transpose sans redessin, Sam, SamBis, Naya et Elio étant déjà construits en formes rondes.

---

# 6. Style H — 2D imprimé moderne

| Contrôle | Verdict |
|---|---|
| **Couleurs réservées** (contrôle 5) | ✔ aucun figurant en sable, sarcelle vif ou orange vif. Le risque anticipé ne s'est pas réalisé |
| Lettrage (contrôle 8) | ✔ aucun, malgré l'idiome |
| Trames de demi teinte | ✔ nettes dans les ombres |
| Décalage chromatique | ✔ présent, **mais trop appuyé sur P02** : le liseré magenta sur les deux personnages se lit comme un défaut d'impression, pas comme un parti pris |
| Palette | **✘ dérive** : P1a-3 sort en violet et orange saturés de bout en bout, alors que le bloc prescrit des tissus sourds et la couleur dans la lumière seule. P02 vire au mauve terne, que sa propre négative interdit (`muddy colours`) |

**P4b-1 est la meilleure H** : trames, liserés discrets, ciel pastel, très lisible.

**Verdict : identité forte et vraiment moderne, mais non calibrée.** Deux réglages avant toute suite : réduire le décalage chromatique d'un cran, et durcir la clause de palette pour que la saturation reste dans les sources et jamais dans le ciel entier.

---

# 7. Style I — roman graphique européen

| Contrôle | Verdict |
|---|---|
| Style conforme | ✔ ligne claire, gouache, grain de papier, palette sourde, lumière égale |
| **Platitude** (contrôle 6) | ✔ **contrôle passé.** P4b-1 est le Paris le plus lisible des dix huit et tient sa tension par la chute des toits, sans effet |
| Foule | ✔ de dos, aucun visage |
| **Plein cadre** (contrôle 10) | ✘ **cadre dessiné et marge crème sur P02** |
| Fidélité à la fiche Parieurs | ✘ **le maigre n'est ni maigre ni miteux** : deuxième gentilhomme correct, sans loucherie ni manteau râpé. Les deux badauds se ressemblent |
| Couleurs réservées | à surveiller : gilet **ocre orangé** sur le badaud rond. Sourd, donc non dominant, mais c'est la limite |
| Décor D1 | écart : le ballon est **dégonflé et affaissé**, alors que la brique le veut gonflé et se balançant |

**Verdict : validable, avec deux corrections.** Le cadre se supprime en positif, l'écart de la fiche Parieurs disparaîtra à l'étape 4 quand la fiche sera réinjectée.

---

# 8. Classement et recommandation

Sur ce que les images montrent, et **seulement** sur cela :

| Rang | Style | Ce qui le porte | Ce qui le retient |
|---|---|---|---|
| 1 | **G** | seul à rendre le décor juste, image la plus aboutie, troupe transposable sans redessin | rien de structurel. Les clauses de lumière douce de son bloc sont à doubler d'un traitement de tension pour les plans 4 et 5, section 8 bis |
| 2 | **I** | meilleur Paris, tenue documentaire, sert le registre CADRE | cadre à supprimer, troupe à redessiner |
| 3 | **D** | deux registres prouvés distincts, meilleure P4b-1 avec I | traitement JOUR à corriger, troupe à redessiner |
| 4 | **E** | identité graphique la plus forte du lot | expression des visages à prouver avant tout engagement |
| 5 | **H** | vraiment moderne, compatible avec la contrainte d'époque | palette non calibrée, liseré trop appuyé |
| 6 | **F** | — | identité absente hors personnages, bandes noires, dérive de décor |

**Recommandation : avancer G, I et D à l'étape 2**, l'épreuve de troupe, 4 images par style, 24 crédits. Écarter F. Garder E et H en réserve, E sous condition d'une épreuve d'expression, H sous condition d'un recalibrage de palette.

Ce classement mesure l'exécution, pas le public. **Si la série vise les 12 à 20 ans, H remonte ; si elle vise les 30 à 40 ans, I passe premier.** Cette décision là ne se lit sur aucune image.

---

# 8 bis. Un préjugé corrigé : la forme ne fait pas le registre

Le plan de test affirmait d'abord que le style G, parce qu'il est rond, ferait un registre trop enfantin pour un épisode dont le sujet est un homme qui coupe une corde à mille mètres au dessus de Paris. **L'épreuve dit le contraire.** Le P4b-1 en style G a un vrai vertige, et le P02 a une tension de caricature qui n'a rien de tendre.

Ce qui détermine le registre d'un plan, ce n'est pas la géométrie des volumes, ce sont **la lumière, le cadrage et la palette**. Un personnage rond en contre jour dur, cadré serré, en palette désaturée, porte le drame. Un personnage anguleux éclairé à plat en couleurs vives ne fait pas sérieux pour autant. La preuve est d'ailleurs dans le lot : le style F, le plus anguleux des six, donne l'image la plus inoffensive de son propre style sur P1a-3, parce que sa lumière est molle.

**Conséquence sur le classement** : G n'a pas de handicap de forme. Son point de vigilance est dans son bloc, aux clauses `gentle rim light and warm bounce light, rich saturated colour, polished and playful`. Ce sont elles qui adouciraient les plans 4 et 5. Elles se doublent d'un **traitement de tension**, exactement comme le style D en a un :

```
hard directional key light, deep shadow on two thirds of every volume, desaturated palette pulled to cold grey and near black, high contrast, tight framing, no warm bounce light
```

À poser sur les plans 4b, 5 et 6, et à laisser le bloc de base tel quel partout ailleurs. Cette correction vaut aussi pour **G, I et H** : aucun des trois n'a de registre de tension distinct, contrairement à D. C'est un manque du plan de test, pas des styles.

1. **RÈGLE 32**, section 1.1, à verser dans `METHODE-generation-images.md`.
2. **Style D** : amputer le traitement JOUR de `saturated blue sky with tall billowing cumulus clouds`, qui écrase l'heure du décor.
3. **Style D** : revenir à la clause de foule des styles A, B et C, la formulation en silhouettes floues n'ayant rien changé.
4. **Style F** : ajouter `letterbox bars, black bars` à la base négative, si le style est repêché.
5. **Style I** : ajouter en positif `the drawing bleeds to all four edges of the frame`.
6. **Style H** : ramener le décalage chromatique à `a barely visible chromatic offset`, et déplacer la clause de saturation pour qu'elle ne porte que sur les sources lumineuses.
7. **Styles G, H et I** : leur donner un **traitement de tension**, section 8 bis. Seul le style D en avait un, et c'est le seul avantage qu'il conservait sur les autres à ce stade.

---

# 10. Deuxième lot — styles J et K, 23 août

## 10.1 Deux résultats de méthode, avant les verdicts

### La RÈGLE 32 est validée, deux fois sur deux

P1a-3 avait raté dans les six premiers styles : jamais de contre plongée. Le prompt J et le prompt K ont été corrigés selon la RÈGLE 32, développement du décor **amputé de sa clause de cadrage**, plus `the camera tilted steeply upward`. **Les deux sortent en contre plongée franche**, caméra basse, ciel et cimes, sommet du ballon et bannières. La règle entre en méthode sans réserve.

### Le lettrage est apparu, pour la première fois sur 24 images

Les bannières de P1a-3 portent **des lettres brodées et des couronnes de laurier**, en J comme en K. La négative universelle, qui tient depuis 319 images, a cédé.

La cause est lisible : dès que le rendu est réaliste, un fanion d'époque **veut** porter un emblème brodé, parce que c'est ce qu'est un fanion d'époque. La négative agit sur la présence d'un élément, pas contre la vraisemblance du matériau. C'est exactement le cas de figure de la troisième règle du README : un défaut de structure ne se corrige pas en allongeant `Avoid:`.

> **RÈGLE 33** — sur un style réaliste ou photoréaliste, un objet dont la fonction historique est de porter un signe (bannière, enseigne, drapeau, sceau, pièce) fait apparaître du lettrage malgré la négative universelle. Il se prescrit en positif : `plain undecorated banners with no emblem and no lettering, blank fabric only`.

### Les bandes noires ne se corrigent pas en négative

`letterbox bars, black bars` était présent dans la négative J. **P02_StyleJ sort quand même avec deux bandes noires latérales.** Même constat qu'en style F. Correction en positif : `the image fills the entire 16:9 frame edge to edge`.

## 10.2 Style J — cinéma réaliste

| Contrôle | Verdict |
|---|---|
| Style conforme | ✔ grain, halation, faible profondeur de champ, étalonnage désaturé, lumière motivée |
| **Fidélité à la fiche Parieurs** | ✔ **la meilleure des huit styles.** Le maigre est enfin maigre, manteau râpé, écharpe grise, regard méfiant. Le rond est massif, redingote, gilet clair, cocarde |
| Bouches fermées, canne, cocarde | ✔ |
| Contre plongée P1a-3 | ✔ RÈGLE 32 |
| **Foule** | ✘ **plusieurs visages lisibles** au fond à droite. Le flou d'arrière plan n'a pas suffi |
| **Lettrage** | ✘ bannières brodées, RÈGLE 33 |
| **Plein cadre** | ✘ bandes noires latérales sur P02 |
| Décor D1 | écart : ciel blanc laiteux et feuillage d'été, pas d'aube brumeuse. Corrigé de lui même sur P1a-3, arbres d'octobre dépouillés |
| Mains | ✔ aucune main déformée sur les trois images, le risque annoncé ne s'est pas réalisé |

**P4b-1_StyleJ est la meilleure image des 24.** Vertige réel, matière d'osier, corde, Paris ancien sans un bâtiment moderne.

**Verdict : très fort visuellement, trois défauts de forme tous corrigeables en positif.** Le vrai obstacle n'est pas dans les images, il est dans ce que J coûte à la chaîne, §4.7 du plan.

## 10.3 Style K — 3D de long métrage, registre adulte

| Contrôle | Verdict |
|---|---|
| **Distinguable de J** | ✔ **oui.** Pas de grain photo, peau à texture lissée, silhouettes légèrement poussées, ventre et maigreur stylisés |
| **Distinguable de G** | ✔ **franchement.** G est rond, chaud, saturé, caricatural ; K est sobre, gris vert, proportions crédibles, longue focale |
| Style conforme | ✔ aucun reflet plastique, tissu à trame visible, étalonnage retenu, atmosphère volumétrique |
| Fidélité à la fiche Parieurs | ✔ bonne. Écart mineur, chapeau mou sur le maigre, comme en style A |
| Contre plongée P1a-3 | ✔ RÈGLE 32 |
| **Foule** | ✘ **le défaut le plus net de K** : une dizaine de figurants nets, alignés, visages lisibles. La foule pose au lieu de regarder le ballon |
| **Lettrage** | ✘ drapeaux tricolores brodés, RÈGLE 33 |
| Plein cadre | ✔ |
| Décor D1 | ✔ brume basse présente, allée de gravier, bosquets |

Réserve de fond : P4b-1_StyleK penche vers le rendu de jeu vidéo haut de gamme plutôt que vers le film d'animation. C'est le risque annoncé au §4.8, il est réel mais modéré, et il tient à l'absence de personnage dans le cadre.

**Verdict : K existe, et c'est le résultat le plus intéressant de la journée.** Il valide l'hypothèse née de la correction du §8 bis : même technique que G, registre entièrement différent, obtenu par la lumière, la focale et l'étalonnage, sans toucher à la géométrie.

## 10.4 Classement révisé, cinq styles en course

| Rang | Style | Ce qui le porte | Ce qui reste à corriger |
|---|---|---|---|
| 1 | **K** | registre adulte sans quitter l'animation, distinguable de G et de J, troupe redessinable en bible | foule qui pose, lettrage des bannières |
| 2 | **G** | seul à rendre le décor juste dès la première image, troupe transposable sans redessin | traitement de tension à écrire pour les plans 4b, 5, 6 |
| 3 | **J** | meilleure fidélité aux fiches, meilleure image des 24 | trois défauts de forme, et surtout l'abandon de la bible et du LoRA |
| 4 | **I** | meilleur Paris en 2D, tenue documentaire, sert le registre CADRE | cadre dessiné à supprimer, traitement de tension à écrire |
| 5 | **D** | deux registres prouvés distincts | traitement JOUR qui écrase l'heure du décor |

**G et K sont le même moteur à deux registres.** C'est le couple le plus instructif du test, et il pose la vraie question : la série est elle un divertissement chaleureux ou un récit sobre. Le reste suit.

## 10.5 Corrections à porter, mise à jour

8. **RÈGLE 33**, §10.1, à verser dans `METHODE-generation-images.md`.
9. **Tous les styles réalistes** : `plain undecorated banners with no emblem and no lettering, blank fabric only` en positif sur P1a-3.
10. **Style J** : `the image fills the entire 16:9 frame edge to edge` en positif ; la négative anti bandes ne suffit pas.
11. **Styles J et K** : durcir la foule en positif, `the crowd behind them all seen from behind, turned toward the balloon, no figure facing the camera`.
