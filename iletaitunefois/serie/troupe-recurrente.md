# Fiche prompt — troupe récurrente

**Version 2, 8 août 2026.** Corrigée après l'audit visuel des 235 images. Les changements par rapport à la v1 sont signalés par ⚠ et sont tous obligatoires : ce sont eux qui empêchent les défauts constatés de se reproduire.

Sam, Naya, Elio — trois récurrents, pas un de plus (bible §8) ; Sam Bis est l'incarnation contemporaine de Sam, même personnage, même voix. Ces trois personnages traversent tous les épisodes.

Un prompt complet est la concaténation `bloc de style` + `bloc identité` + `bloc de cadrage` + `Avoid:` + `négatives du personnage` + `négatives de cadrage` + `base négative du style` + **`négative universelle`**.

Pour les personnages d'époque de l'épisode 1, voir `iletaitunefois/S01E01/prompts/personnages-episode.md`.

**Réglages** : `nano_banana_pro`, 16:9, 2K, une image par requête, négatif en fin de prompt après `Avoid:`.

---

# 0. ⚠ NÉGATIVE UNIVERSELLE — à coller sur TOUTE image, sans exception

```
text, title, caption, lettering, words, letters, labels, annotations, color swatches, palette chips, size chart, watermark, signature, border, frame, margin
```

**Pourquoi.** Plus de 40 images sur 235 portaient un lettrage anglais jamais demandé. Deux causes : les mots `model sheet`, `character sheet`, `reference sheet` et `turnaround` sont lus comme « planche annotée de production » ; et les directives de style elles mêmes fuient dans l'image sous forme de légende, au point qu'on lisait « CEL SHADING - TWO TONES » imprimé sur des planches qui ne le respectaient pas.

## ⚠ Mots bannis des prompts

Ne plus jamais écrire `model sheet`, `character sheet`, `reference sheet`, `turnaround`, ni aucune formule de direction artistique qui ressemble à une note de production. Décrire la disposition **visuellement** :

* au lieu de `full body turnaround: front view, three quarter view, side profile, back view` → `four drawings of the same character standing side by side in one row, seen from the front, from three quarters, from the side, and from the back`
* au lieu de `character model sheet on plain light grey background` → `on a plain flat light grey background`
* au lieu de `expression sheet: six head and shoulders portraits` → `six drawings of the same head, two rows of three`

---

# A. Blocs de style

⚠ Les mentions `character model sheet on...` ont été retirées de tous les blocs.

## Style A — dessin animé YouTube

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, bright saturated colors, flat cel shading with a single hard edged shadow tone, absolutely no photorealism, on a plain flat light grey background:
```

Base négative : `gradient shading, soft shading, airbrush, painterly, thin delicate linework, photorealism, photograph, realistic skin texture, 3D render, CGI, live action, anime style, manga, corporate flat vector art, extra characters.`

⚠ Ajout de `flat cel shading with a single hard edged shadow tone` et des négatives `gradient shading, soft shading, airbrush, painterly, thin delicate linework` : les portraits cadre en style A dérivaient presque systématiquement vers un trait fin ombré en dégradé qui ne raccordait plus avec les turnarounds.

## Style B — inkman

```
inkman stick figure cartoon style, large round white head with bold black ink outline, simple dot eyes and expressive mouth, thin black stick limbs, flat graphic character design, hand drawn ink sketch feel with slightly wobbly brush lines, on a plain flat warm cream background:
```

Base négative : `plain round ball hands, circle hands, hollow white circle hands, separate fingers, realistic hands, missing hand, missing arm, realistic human anatomy on the main character, detailed face, nose, painted background, realistic painted scenery, photorealism, 3D render, anime, manga, extra inkman characters.`

⚠ Ajouts : `missing hand, missing arm` parce que plusieurs vues de profil perdaient purement et simplement un bras, et parce qu'une planche avait des avant bras terminés en pointe sans aucune main. Ajouts `painted background, realistic painted scenery` parce que les props en style B basculaient en peinture naturaliste avec des décors de bibliothèque jamais demandés.

Bloc de style en scène, pour les plans avec décor :

```
inkman stick figure cartoon character in a richly illustrated scene, the character drawn flat and graphic with bold black ink, the background painted with atmospheric depth and dramatic lighting
```

## Style C — animation 2D années 90

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, warm saturated palette of amber ochre and burnt orange with deep teal blue shadows, crisp and graphic not painterly, on a plain flat light warm background:
```

Pour Sam et Sam Bis, remplacer `appealing shape driven character design` par `strongly angular shape driven character design`.

Base négative : `gradient shading, soft shading, airbrush, painterly, rendered highlights, digital painting, muddy colors, cold blue palette, violet palette, purple palette, cool grey palette, desaturated wash, photorealism, photograph, 3D render, CGI, live action, anime, manga, flat vector art, extra characters.`

⚠ **C'est le style qui a le plus mal tenu, et de loin.** Aucune planche personnage n'appliquait réellement les deux tons à bords durs. Pire, la charte de couleur avait éclaté en trois : Sam en ambre conforme, Sam Bis entièrement violet et bleu froid, Naya en sarcelle et marine, soit un simple recolor de son style A. D'où les négatives `cold blue palette, violet palette, purple palette, cool grey palette`.

⚠ **Référence de charte : `Sam_StyleC_turnaround` est la seule planche C qui tenait la palette.** C'est elle qui fait foi. Toute nouvelle planche C doit être comparée à elle avant validation.

---

# B. Règles verrouillées

1. **Sam n'a aucune lunette, nulle part.** Jamais portées, jamais sur le front, jamais tenues, jamais dans la sacoche. Règle la mieux tenue du projet, à ne pas relâcher.
2. **Règle des moufles, style B.** Toute main est une moufle noire arrondie avec un petit pouce. Formulation positive obligatoire `each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers`, doublée de la négative complète. Les deux ensemble.
3. **Couleurs réservées.** Sable pour Sam et Sam Bis, sarcelle vif pour Naya, orange vif pour Elio. Aucun personnage secondaire ni aucun accessoire d'époque ne les porte en dominante.
4. **Personnages originaux**, jamais de reproduction d'un design existant.
5. **Un seul changement par plan** : décor, pose, ou costume d'époque.
6. **Réinjection de référence.** Toute image dérivée se génère avec la planche turnaround validée du personnage et du style, prompt préfixé par `same character as reference, same art style as reference`.
7. ⚠ **Une planche de référence doit être regardée avant de servir.** Un défaut dans la référence se propage à toute la série. Le turnaround Sam style B avait des mains rondes non conformes et il a fallu tout reprendre. Ne jamais enchaîner sur une référence non validée à l'œil.
8. ⚠ **Continuité de costume à vérifier vue par vue.** Sur les turnarounds, le bandeau du chapeau de Sam, les étiquettes de sa sacoche, les deux bandes du survêtement d'Elio et sa tablette apparaissaient et disparaissaient selon les vues. Ajouter au positif `the same clothing details visible in every view` et vérifier à l'œil.

---

# C. Blocs identité

## SAM — explorateur pulp années 30

Styles A et C :

```
Sam, an original cartoon character in the classic 1930s pulp explorer archetype, a charismatic energetic man in his mid thirties, no eyewear, wide brim sand colored felt fedora with a dark ribbon band clearly visible in every view, worn tilted, short dark brown tousled hair showing under the hat, light stubble, strong jaw, warm confident face with an adventurous half smile and one raised eyebrow, worn sand colored canvas explorer jacket with sleeves pushed up to the elbows, open collar khaki shirt clearly distinct from the jacket underneath, wide brown leather belt with a square buckle, a large aged brown leather satchel worn on a strap across the chest hanging at his hip, its flap covered with colorful travel labels visible in every view, dark cargo trousers, brown hiking boots, both arms and both hands visible
```

Style B :

```
Sam, an inkman stick figure character with a large round white head outlined in bold black ink, simple black dot eyes, expressive cartoon mouth, thin black stick arms and legs, both arms and both mitten hands visible in every view, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, solid black simple boots on his stick legs, wearing a wide brim sand colored explorer fedora with a dark band clearly visible in every view, an open sand colored utility jacket with a raised collar, a dark brown leather satchel worn across his body, cheerful confident adventurous expression
```

Négatives propres : `whip, coiled rope, bullwhip, revolver, gun, glasses, eyeglasses, goggles, sunglasses, any eyewear, full beard, elderly man, walking stick, staff, cane`

⚠ Ajouts au positif : `clearly visible in every view` sur le bandeau et les étiquettes, `clearly distinct from the jacket` sur la chemise kaki qui était absorbée par la veste en style C, `both arms and both hands visible` contre les bras manquants de profil.

⚠ **Alerte `nsfw`** : sur une planche de portraits rapprochés, `light stubble` et `strong jaw` ont déclenché un faux positif. Les retirer pour ce cadrage là, garder le reste.

## SAM BIS — chasseur de trésor contemporain

Styles A et C :

```
Sam, an original cartoon character, a modern day treasure hunter and field archaeologist in his mid thirties, no hat, no eyewear, dark brown tousled wavy hair, short trimmed stubble beard, warm intelligent face with a wry curious half smile and expressive raised eyebrows, faded indigo blue button up field shirt worn open at the collar with the sleeves rolled up to the forearms, soft olive green scarf loosely knotted around his neck, a wide brown leather strap running diagonally across his chest holding an aged sand colored canvas and leather satchel at his hip, brown leather belt, sand colored chino trousers, worn brown desert boots, both arms and both hands visible
```

Style B :

```
Sam, an inkman stick figure character with a large round white head outlined in bold black ink, no hat, a few loose ink strokes of dark tousled hair on top of his round head, simple black dot eyes, expressive cartoon mouth, thin black stick arms and legs, both arms and both mitten hands visible in every view, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, solid black simple boots on his stick legs, wearing a faded indigo blue field shirt with the sleeves rolled up, a soft olive green scarf knotted around his neck, a brown leather strap across his body holding a sand colored satchel at his hip, sand colored trousers, curious determined expression
```

Négatives propres : `hat, fedora, cap, helmet, glasses, eyeglasses, goggles, sunglasses, whip, gun, full thick beard, elderly man, walking stick, staff, cane`

⚠ En style C, ajouter aux négatives `cold blue palette, violet palette, purple palette` : c'est le personnage qui dérivait le plus, sa planche C était entièrement violette.

## NAYA — 10 ans

Styles A et C :

```
Naya, a cartoon character, a girl aged 10, big voluminous curly dark brown hair drawn as a cloud of many individually defined springy curls with visible highlights and separated locks, warm brown bright curious eyes, oversized vivid teal sweatshirt with long sleeves hanging down over her hands, dark navy leggings, small worn notebook and pencil in hand, blue and white sneakers
```

Style B :

```
Naya, an inkman stick figure character with a large round white head outlined in bold black ink, a big cloud of voluminous curly dark hair drawn as many separate loose black ink strokes with visible gaps between the locks, simple black dot eyes, expressive cartoon mouth, thin black stick arms and legs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, solid black simple shoes on her stick legs, wearing an oversized vivid teal sweatshirt with sleeves hanging past her hands, holding a small worn notebook, curious eager expression
```

Négatives propres : `flat solid black hair silhouette, hair drawn as one solid shape, solid black hair mass, bare legs, straight hair, pigtails, school uniform, pastel colors on her outfit, teenager proportions`

⚠ En style B, le positif a été renforcé en `many separate loose black ink strokes with visible gaps between the locks` et la négative en `solid black hair mass` : sa chevelure inkman sortait en masse noire compacte dont les boucles n'étaient que des bosselures du contour.

⚠ En style C, ajouter `warm amber and ochre palette with deep teal shadows` au positif : sa planche C était un simple recolor sarcelle et marine de son style A, sans aucune trace de la charte C.

## ELIO — 12 ans

⚠ **Refonte de l'expression.** L'ancienne formulation interdisait la tête de méchant sans jamais prescrire l'alternative, et Elio sortait hostile sur 7 planches sur 8, dans les trois styles. On prescrit désormais en positif.

Styles A et C :

```
Elio, a cartoon character, a likeable boy aged 12, open curious face, relaxed eyebrows, warm friendly half smile, playful and cheeky but never hostile, one eyebrow lifted in gentle amused doubt, flat brim cap in a solid vivid orange worn forward at all times, short dark hair visible at the sides, dark track jacket with two contrasting light side stripes visible on both sleeves in every view, translucent glowing tablet held raised at head height in one hand, dark trousers, high top sneakers
```

Style B :

```
Elio, an inkman stick figure character with a large round white head outlined in bold black ink, simple black dot eyes, open curious relaxed expression, gentle amused half smile, never hostile, thin black stick arms and legs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, solid black simple sneakers on his stick legs, wearing a flat brim cap in solid vivid orange sitting on his round head worn forward, a simple dark track jacket with two light side stripes, holding a small translucent glowing tablet raised at head height in every view
```

Négatives propres : `angry scowl, frowning glare, villain expression, mean face, sharp pointed angry eyebrows, sneer, smirk of contempt, backwards cap, removed cap, floating cap, bare head, glasses, smartphone, missing tablet`

⚠ Ajouts : `sharp pointed angry eyebrows, sneer, smirk of contempt` côté expression ; `floating cap` parce que sa casquette flottait au dessus du crâne et à l'envers sur un asset ; `missing tablet` parce que la tablette disparaissait des vues de profil et de dos. Et `raised at head height` parce qu'elle n'était jamais levée, toujours tenue à hauteur de poitrine.

---

# D. Totems par époque

| Époque | Sacoche de Sam | Carnet de Naya | Tablette d'Elio |
|---|---|---|---|
| Antiquité | fragment de miroir, astrolabe | tablette de cire | rouleau de papyrus |
| Renaissance | carnet taché d'encre, lentille | cahier de croquis | registre relié |
| XIXᵉ | anémomètre, ampoule, fiole | registre de laboratoire | procès verbal |
| XXᵉ | badge de mission, éprouvette | journal de bord | dossier à tampons |
| Futur, *Demain 2080* | échantillon martien | carnet holographique | la tablette, enfin chez elle |

---

# E. Blocs de cadrage

## Planche des quatre vues, dite turnaround

⚠ Reformulée sans le mot déclencheur.

```
four drawings of the same character standing side by side in one single row, seen from the front, from three quarters, from the side, and from the back, all at the same scale, the same character and the same clothing details in every drawing, flat even lighting.
```

Pour Sam ajouter `the same hat in every drawing`, pour Elio `the same orange cap in every drawing`.

## Planche des six têtes

⚠ Reformulée, et le comptage est verrouillé. Six planches sur douze sortaient avec sept ou huit têtes.

```
exactly six drawings of the same head and shoulders, no more and no less, laid out in two rows of three, three heads on the top row and three heads on the bottom row, all at the same scale, the same character design and the same colors in every head: neutral curious look, wide joyful smile, wide eyed surprise, skeptical raised eyebrow, worried concerned frown, laughing with eyes closed, flat even lighting.
```

En style B, remplacer `head and shoulders` par `head and neck`, `the same character design and the same colors` par `the same round head design`, et `laughing with eyes closed` par `laughing with curved closed eyes`.

Négatives à ajouter : `seven heads, eight heads, four columns, extra portraits, empty slot, incomplete grid, full body, legs, feet, four drawings in a row`

## Portrait cadre, registre CADRE

```
one single chest up portrait of the character in three quarter view, one pose only, the figure completely isolated on a plain flat neutral grey background, warm even lighting.
```

## Plein pied aventure

```
one single full body drawing of the character in three quarter view in a confident adventure pose, one pose only, weight on one leg, one hand resting on the satchel strap, looking off frame with intent, the figure completely isolated on a plain flat neutral grey background, flat even lighting.
```

Pour Naya : `one single full body drawing mid stride leaning forward eagerly, her small worn notebook and pencil held up in one hand, looking off frame with excitement`

Pour Elio : `one single full body drawing in three quarter view, leaning back slightly with the translucent glowing tablet raised at head height in one hand and the other hand gesturing`

## ⚠ Négatives obligatoires sur toute planche à sujet unique

```
multiple views, turnaround, model sheet layout, repeated figure, second figure, ghost figures, faint duplicate figures in the background, duplicate limbs, extra heads, floating heads, disembodied shoes, cropped body parts, background scenery, decor, ground, cast shadow on the background, vignettes, inset panels
```

**Pourquoi.** Neuf poses censées montrer un personnage seul contenaient des résidus de planche multi vues : têtes fantômes délavées, jambes et chaussures dupliquées, études de tête complètes. Un portrait était une tête géante sans corps posée au dessus de quatre paires de chaussures orphelines, et un plein pied était en réalité un turnaround.

---

# F. Contrôle avant validation

À faire à l'œil, sur chaque planche, avant de s'en servir comme référence.

1. **Aucun texte** nulle part dans l'image.
2. **Un seul personnage**, aucune silhouette fantôme, aucun membre dupliqué, aucun fragment flou en bord de cadre.
3. **Le bon nombre** de vues ou de têtes. Quatre pour un turnaround, exactement six pour une planche d'expressions.
4. **Style B** : moufles à pouce sur chaque main, deux bras présents sur chaque vue.
5. **Style C** : ombres à bords durs et palette ambre ocre orange brûlé avec sarcelle. Comparer à `Sam_StyleC_turnaround`, qui fait foi.
6. **Style A** : contours noirs épais et aplats. Si le trait est fin et l'ombre en dégradé, c'est à refaire.
7. **Aucune lunette** sur Sam.
8. **Elio** : visage ouvert, sourcils détendus, jamais hostile. Casquette posée sur le crâne, visière vers l'avant. Tablette levée à hauteur de tête.
9. **Naya** : boucles détachées avec des vides entre les mèches, leggings marine.
10. **Continuité** des détails de costume d'une vue à l'autre.
11. **Cohérence entre personnages d'un même style** : mettre les quatre planches côte à côte. Elles doivent avoir l'air d'appartenir à la même série.
