# Fiche prompt — personnages de l'épisode S01E01

**Version 2, 8 août 2026.** Corrigée après l'audit visuel des 235 images. Les changements sont signalés par ⚠ et sont obligatoires.

Onze personnages ou groupes d'époque à planche dédiée, plus dix figures au fil de l'eau. Pour la troupe récurrente, voir `iletaitunefois/serie/troupe-recurrente.md`.

Un prompt complet est la concaténation `bloc de style` + `bloc identité` + `bloc de cadrage` + `Avoid:` + `négatives d'époque` + `base négative du style` + **`négative universelle`**.

**Réglages** : `nano_banana_pro`, 16:9, 2K, une image par requête.

---

# 0. ⚠ NÉGATIVE UNIVERSELLE — sur TOUTE image

```
text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin
```

**Pourquoi.** 24 fiches sur 49 portaient un lettrage jamais demandé : titres, étiquettes de rôle (« OLD MASTER », « YOUNG ASSISTANT », « PORTER A (FRONT) »), légendes de vues, nuanciers, échelles chiffrées, et jusqu'aux notes de direction artistique recopiées telles quelles (« MUTED EARTH TONES ONLY », « 2 TONE SHADING, HARD EDGED SHADOWS »). Le style C était le pire, 10 fichiers sur 12.

## ⚠ Mots bannis des prompts

Ne plus écrire `model sheet`, `character sheet`, `reference sheet`, `turnaround`. Décrire visuellement : `four drawings of the same character side by side in one row, seen from the front, from three quarters, from the side and from the back`, ou `the two characters standing side by side, full body, three quarter view, at the same scale`.

---

# A. Blocs de style, version personnage d'époque

## Style A

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period character in desaturated muted earth tones, era accurate costume, absolutely no photorealism, on a plain flat light grey background:
```

## Style B

```
inkman stick figure cartoon style, large round white head with bold black ink outline, simple dot eyes and expressive mouth, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costume in muted earth tones, on a plain flat light neutral background:
```

⚠ Le membre de phrase `and no separate fingers` a été ajouté au bloc de style lui même, pas seulement aux négatives. En style B, **tous** les personnages d'époque sont des inkmen, sans exception.

## Style C

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period character with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costume, crisp and graphic not painterly, on a plain flat light warm background:
```

---

# B. Bases négatives

**Commune à tous les personnages d'époque, jamais optionnelle** :

```
dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing
```

⚠ Renforcée. Trois fuites constatées sur des plans exposés : la tunique orange saturée du fermier 2 en style B, le cerf volant hibou style C entièrement orange vif cerné de sarcelle, et la sacoche givrée style C devenue sarcelle à sangle orange au lieu de cuir brun.

**Style A** : `gradient shading, soft shading, airbrush, painterly, thin delicate linework, photorealism, photograph, realistic skin texture, 3D render, CGI, live action, anime style, manga, corporate flat vector art, extra characters.`

**Style B** : `plain round ball hands, hollow circle hands, teardrop hands, pointed armless stumps, separate fingers, realistic hands, missing hand, missing arm, realistic human anatomy, detailed face, nose, painted background, realistic painted scenery, interior decor, photorealism, 3D render, anime, manga, extra inkman characters.`

⚠ Ajouts `teardrop hands, pointed armless stumps` : cinq fiches B sur douze avaient des mains en boules ou en gouttes noires pleines sans pouce. Ajouts `painted background, realistic painted scenery, interior decor` : les props B basculaient en peinture naturaliste avec bibliothèque et cheminée jamais demandées.

**Style C** : `gradient shading, soft shading, airbrush, painterly, rendered highlights, digital painting, muddy colors, cold blue palette, violet palette, purple palette, photorealism, photograph, 3D render, CGI, live action, anime, manga, flat vector art, extra characters.`

---

# C. Blocs identité

Chaque planche est générée sur fond neutre, **regardée et validée**, puis réinjectée sur tous les plans de ses scènes avec `same character as reference, same art style as reference`.

## 1. Garnerin — plans 3, 4, 63 ; clip du 5 réutilisé au 61

Styles A et C : `Garnerin, a French aeronaut of the Directoire era, resolute determined face with a calm set jaw, dark tailcoat, hair tied back, pale scarf at the neck, period breeches and buckled shoes, upright decided posture`

⚠ `clenched jaw` remplacé par `calm set jaw` : il sortait en grimace dents serrées sur trois vues.

Style B : `Garnerin, an inkman stick figure character, a few ink strokes of hair tied back on his round head, simple black dot eyes with no eyebrows, resolute small mouth, wearing a dark Directoire tailcoat drawn as a simple flat shape, a pale scarf knotted at the neck, simple period shoes on his stick legs, upright decided posture`

⚠ `simple black dot eyes with no eyebrows` : il sortait avec des yeux dessinés et des sourcils, pas des points.

## 2. Yuan Huangtou — plans 44, 45, 47

Styles A et C : `Yuan Huangtou, a deposed prince of 6th century China, thin and dignified, long worn tunic, loose untied hair, gaunt face with a noble bearing and calm gaze, bare wrists`

⚠ `optional rope bindings at the wrists` remplacé par `bare wrists` : le mot « optional » produisait des cordes non voulues en style C.

Style B : `Yuan Huangtou, an inkman stick figure character, a deposed prince, long loose untied hair drawn as flowing ink strokes around his round head, calm quiet dot eyes, dignified straight posture despite a thin drooping silhouette, a long worn tunic drawn as one simple flat shape, bare wrists`

## 3. Parieurs, paire — plans 2, 64

Styles A et C : `the two Directoire onlookers standing side by side, full body, three quarter view, at the same scale: the round onlooker on the left wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; the thin onlooker on the right leaning on a cane, threadbare coat in muted brown and grey only, no blue and no green on any garment, suspicious squint`

⚠ **Couleur nommée en positif, 23 août 2026.** Sur les styles réalistes J et K, le manteau du maigre est sorti en **sarcelle désaturé** dans les deux tirages, vert olive en style D. Deux styles sur trois : la cause est dans le prompt (RÈGLE 7), qui ne nommait aucune couleur. Les négatives `dominant teal outfit, saturated teal clothing` n'y ont rien fait, le sarcelle obtenu étant désaturé : **il passe sous la négative tout en étant la couleur dominante du personnage**. C'est la RÈGLE 30 appliquée à un personnage nommé, et elle compte : le sarcelle vif appartient à Naya, et le maigre est présent aux plans 2 et 64.

⚠ Position et chapeaux verrouillés : les couvre chefs étaient inversés d'un style à l'autre, et le « haut chapeau » sortait en bicorne.

Style B : `the two Directoire onlooker inkman characters standing side by side, full body, three quarter view, at the same scale: the round bellied onlooker on the left with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his belly, peremptory raised chin; the thin onlooker on the right leaning on a cane, threadbare coat, suspicious half closed dot eyes`

## 4. Fermiers au semoir, paire — plans 21, 22

Styles A et C : `the two Chinese farmers of the Warring States period standing side by side, full body, three quarter view, at the same scale: one farmer covered in scattered seeds, wide straw hat, simple tunic in muted brown earth tones, baffled expression; one farmer at a wooden three row seed drill, cloth apron in muted grey brown, tied sleeves, quiet pride`

⚠ Les tons sont maintenant nommés dans le bloc identité, `muted brown earth tones` et `muted grey brown` : le fermier 2 sortait en tunique orange saturée, couleur réservée.

Style B : `the two Chinese farmer inkman characters of the Warring States period standing side by side, full body, three quarter view, at the same scale: one farmer inkman speckled with scattered seed dots, wide conical straw hat on his round head, simple tunic in muted brown, baffled open mouth, both mitten hands visible; one farmer inkman standing at a wooden three row seed drill, cloth apron in muted grey brown, quiet proud smile, both mitten hands visible`

## 5. Pilleurs, paire — plans 56, 57

Styles A et C : `the two Song dynasty looters standing side by side, full body, three quarter view, at the same scale: a stocky looter holding two large parasols, tight dark clothes, overconfident grin; a thin looter with loot sacks, nervous shifty eyes`

Style B : `the two Song dynasty looter inkman characters standing side by side, full body, three quarter view, at the same scale: a stocky looter inkman holding two large parasols in his mitten hands, tight dark clothes drawn as flat shapes, overconfident grin; a thin looter inkman with loot sacks, nervous shifty dot eyes`

## 6. Porteurs du pont — plans 50, 51

Styles A et C : `the two Sichuan porters, full body, three quarter view, one slightly behind the other, each carrying a TALL basket loaded high on his back with shoulder straps, plus a carrying pole across the shoulders, rope sandals, worn cloth clothes in muted earth tones, calm assured stride`

⚠ **Les hautes hottes dorsales manquaient dans les trois styles**, seules les palanches à paniers sortaient. D'où `a TALL basket loaded high on his back with shoulder straps`.

Style B : `the two Sichuan porter inkman characters, full body, three quarter view, one slightly behind the other, each with a TALL basket loaded high on his back held by shoulder straps, plus a carrying pole across the shoulders, worn cloth clothes drawn as flat shapes in muted earth tones, simple strap sandals on their stick legs, both mitten hands visible, calm assured stride`

## 7. Moine Huaibing — plan 39

Styles A et C : `the monk Huaibing, a Song dynasty Buddhist monk, full body, three quarter view, simple plain robe in muted ochre, shaved head, serene face, calm open gesture with empty hands, quiet authority`

⚠ `with empty hands` : un bâton non demandé apparaissait.

Style B : `the monk Huaibing as an inkman stick figure character, a Song dynasty Buddhist monk, full body, three quarter view, bare round shaved head, serene curved closed eyes, gentle small smile, a simple plain robe drawn as one flat shape, calm open gesture, both mitten hands clearly visible with their small thumb`

## 8. Lenormand — plan 60

Styles A et C : `Lenormand, a young tousled French scientist of the 18th century, full body, three quarter view, PALE CREAM period coat, undone jabot, anxious enthusiasm, holding TWO large closed parasols, one in each hand, both parasols clearly visible`

⚠ Deux correctifs : l'habit sortait vert olive ou brun au lieu de clair, d'où `PALE CREAM` ; et une seule ombrelle sortait en style C, d'où `one in each hand, both parasols clearly visible`.

Style B : `Lenormand as a young inkman stick figure character, an 18th century French scientist, full body, three quarter view, tousled ink stroke hair on his round head, wide anxious enthusiastic dot eyes, a PALE CREAM period coat drawn flat with an undone jabot, holding TWO large closed parasols, one in each mitten hand, both mitten hands attached to his arms`

⚠ `both mitten hands attached to his arms` : sa planche B avait une moufle flottante détachée du corps et des ombrelles sans porteur.

## 9. Alchimistes taoïstes, paire — plan 71

Version propre, styles A et C : `the two Taoist alchemists standing side by side, full body, three quarter view, at the same scale: an old alchemist with a long thin grey beard, dark robe, cautious pose, holding a glass retort with both hands; a young assistant in a light robe, rolled sleeves, worried look`

Version propre, style B : `the two Taoist alchemist inkman characters standing side by side, full body, three quarter view, at the same scale: an old alchemist inkman with a long thin grey beard drawn as loose ink strokes, dark robe drawn as one flat shape, holding a glass retort with both mitten hands, each mitten hand showing its small thumb; a young assistant inkman in a light robe, rolled sleeves, worried tilted eyebrow strokes, both mitten hands showing their small thumb`

**Version suie** ⚠ reformulée. Reprendre le bloc et ajouter :

```
, BOTH characters equally covered in thick black soot from head to toe, BOTH with their hair blown straight upward, BOTH with dazed blinking expressions, soot on both faces and both robes
```

Générer avec la planche propre du même style en référence, prompt préfixé par `same characters as reference, same art style as reference`, négatives `different characters from the reference, different art style, only one character sooty, one clean character`.

⚠ En style C, **seul l'assistant avait subi l'explosion**, le vieux maître restant propre avec son chignon intact. D'où les `BOTH` répétés.

## 10. Charretier Han — plan 29

Styles A et C : `a Han dynasty carter, full body, three quarter view, stocky build, short crossed tunic, cloth trousers, flat hat, satisfied craftsman smile, holding a padded shoulder collar in both hands`

Style B : `a Han dynasty carter as an inkman stick figure character, full body, three quarter view, a slightly rounded stocky body shape, short crossed tunic drawn flat, flat hat on his round head, satisfied craftsman smile, holding a padded shoulder collar with both mitten hands, each mitten hand clearly showing its small thumb`

## 11. Foule Directoire — plans 1, 2, 4, 63, 64

Styles A et C : `a dozen Directoire crowd silhouettes, MOST OF THEM SEEN FROM BEHIND and the rest in three quarter view from behind, varied scales, NO FACE VISIBLE ON ANY FIGURE, no facial features at all: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, one closed umbrella, simplified figures less detailed than main characters`

⚠ Deux correctifs. La foule sortait **majoritairement de face** dans les trois styles, d'où `MOST OF THEM SEEN FROM BEHIND`. Et en style C **deux visages entièrement lisibles** apparaissaient, d'où `NO FACE VISIBLE ON ANY FIGURE`.

Style B : `a dozen Directoire inkman crowd silhouettes, MOST OF THEM SEEN FROM BEHIND, varied scales, plain round BLANK heads with absolutely no facial features, NO EYES, no dots, no mouths, men with tall hats and simple flat tailcoats, women with high waisted dresses and shawls, a few small inkman children, one closed umbrella, simplified figures even less detailed than the main characters`

⚠ Une dizaine de figurants portaient des yeux points explicitement interdits. D'où `NO EYES, no dots`.

Négatives spécifiques : `readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures`

---

# D. Assets partagés

## INS-sacoche, insert main et sacoche

```
[bloc de style] a close up insert on a warm honey wood table, ONLY a hand and a forearm in frame, nothing else: the hand slipping a small object into the open aged brown leather satchel whose flap is covered with colorful travel labels, plain simple table surface, no room, no furniture, no background scenery, warm even light
```

⚠ En style B, la main est `a solid black rounded mitten hand with a small thumb at the end of a thin black stick wrist`, et il faut impérativement `no room, no furniture, no background scenery` : les deux inserts B sortaient plaqués sur une bibliothèque peinte à l'huile avec fauteuil et lampe à pétrole.

⚠ En style A, ajouter à la négative `inset panel, vignette, second image` : une vignette encadrée montrant l'épaule et le torse s'était ajoutée en haut à gauche.

## INS-sacoche-givre

Même bloc, en ajoutant : `a thick crust of white frost and pale blue ice crystals covering the whole flap, the travel labels frosted over, small icicles hanging from the edge of the flap, faint cold vapour rising, the satchel itself still clearly BROWN LEATHER under the frost`

⚠ `still clearly BROWN LEATHER under the frost` : en style C la sacoche était devenue sarcelle à sangle orange, double violation des couleurs réservées et rupture de continuité avec la version non givrée. Générer les deux versions en enchaînant, la propre en référence de la givrée.

## ELIO-gel, portrait détouré

```
[bloc de style] Elio, [bloc identité Elio du style], standing facing the viewer, the translucent glowing tablet RAISED HIGH at head height in one hand, the cap sitting firmly on his head with the flat brim pointing FORWARD, full vivid saturated colors, one single figure completely isolated on a plain flat neutral background, medium shot from the knees up
```

⚠ Trois correctifs. La tablette n'était **jamais levée** dans aucun style, toujours à hauteur de poitrine. En style A la casquette était **retournée et flottait au dessus du crâne**. En style C la planche est sortie en quatre vues au lieu d'un plan unique, d'où l'insistance sur `one single figure` et les négatives de sujet unique.

## KITE-hibou

```
[bloc de style, sans mention de personnage] a huge kite shaped like an owl, bamboo frame, stretched paper in muted brown and cream earth tones, spread wings, grip bars, the object alone on a plain flat neutral background
```

⚠ `in muted brown and cream earth tones` : en style C le hibou sortait entièrement orange vif cerné de sarcelle, deux couleurs réservées sur un accessoire d'époque. En style B il sortait en aquarelle naturaliste, d'où la négative `painted, watercolor, naturalistic illustration, feathers rendered in gradients`.

## PLATE-laloubere

```
an original engraving printed on aged paper, in the style of 17th century printed book illustration, fine hatched burin line work, sepia ink on cream aged paper, a flat printed page not an object: acrobats jumping and tumbling under large open parasols, a printed title banner at the top reading Du royaume de Siam, decorative rule lines
```

⚠ `printed on aged paper`, `a flat printed page not an object` : elle sortait comme une plaque de cuivre gravée photographiée sous cadre, ton cuivre rouge. Négatives à ajouter : `copper plate, metal plate, photographed object, picture frame, three dimensional object`.

---

# E. Blocs de cadrage

## Quatre vues, pour Garnerin et Yuan Huangtou seulement

```
four drawings of the same character side by side in one single row, seen from the front, from three quarters, from the side, and from the back, all at the same scale, the same character and the same costume in every drawing, flat even lighting.
```

## Fiche simple, pour tous les autres

```
full body, three quarter view, flat even lighting.
```

Le cadrage des paires est déjà porté par le bloc identité. Ne pas le doubler.

## ⚠ Négatives obligatoires sur toute fiche

```
multiple views, model sheet layout, repeated figure, ghost figures, duplicate limbs, extra heads, inset panels, vignettes, thumbnail sketches, close up detail callouts
```

---

# F. Personnages au fil de l'eau, sans planche dédiée

Décrits dans le prompt de la scène, dont ils héritent le style. En style B, préfixer par `an inkman stick figure` et garder la règle des moufles.

| Figure | Plan | Formule |
|---|---|---|
| Aide de Garnerin | 3 | `a helper in a rough jacket, rolled up sleeves` |
| Empereur Gao Yang | 44 | `an emperor in a sumptuous dark and gold robe, imperial headdress, cruel amused smile, leaning on the parapet` |
| Cavaliers antiques | 30 | `Greco Roman riders in short tunics, bare legs, riding with NO STIRRUPS AT ALL, nothing hanging under the saddles, nervous mounts` |
| Cavaliers avars | 32 | `Avar horsemen in caftans and felt caps, bows slung across their backs, gleaming iron stirrups clearly visible` |
| Passants de Ye | 46 | `6th century Chinese passersby in simple tunics, heads raised, mouths open` |
| Badauds du pont | 50 | `two Sichuan onlookers in cloth tunics, one peremptory, one placid` |
| Shun | 54 | `a vigorous legendary young man, plain archaic tunic, two large conical straw hats strapped to his arms` |
| Sentinelle et général | 66 | `a delighted sentry wearing a pale cuirass of folded paper sheets; an enemy general in dark metal armor, eyebrows raised with interest` |
| Faux monnayeurs | 67 | `two accomplices in patched tunics, greedy furtive faces, leaning toward each other` |
| Chevalier en armure | 34, décor D22 | `a western medieval knight in plate armor on horseback, raised lance, banner` |

⚠ Cavaliers antiques : `NO STIRRUPS AT ALL, nothing hanging under the saddles`. L'absence d'étrier est le point pédagogique de la séquence, et les étriers sortaient quand même sur le décor D12 en styles A et B.

**Cas du chevalier.** Catalogué décor D22 mais contient un personnage : se génère avec le bloc de style personnage, pas l'ouvreur de décor. En style B c'est un inkman à moufles sous un heaume à visière relevée. ⚠ En style C sa plaque sortait en gris bleu froid, hors charte, alors que c'est un plan signature : lui appliquer explicitement la palette ambre ocre orange brûlé à ombres sarcelle.

---

# G. Contrôle avant validation

1. **Aucun texte** dans l'image.
2. **Aucune couleur réservée en dominante** sur un personnage ou un accessoire d'époque.
3. **Style B** : moufle à pouce sur chaque main, aucune boule, aucune goutte, aucun moignon pointu. Foule sans le moindre trait de visage.
4. **Bon nombre de personnages** : une paire montre deux personnages, jamais un ni trois.
5. **Accessoires présents** : les deux ombrelles de Lenormand, les hottes hautes des porteurs, la cornue des alchimistes, le collier du charretier.
6. **Foule vue de dos**, aucun visage lisible.
7. **Version suie** : les deux alchimistes noircis, pas un seul.
8. **Tons de terre sourds** : un personnage d'époque ne doit jamais être aussi saturé qu'un héros.
9. **Style C** : ombres à bords durs, palette ambre ocre avec sarcelle, jamais de violet ni de bleu froid.
10. **Un seul sujet** sur les fiches, aucun fragment fantôme.
