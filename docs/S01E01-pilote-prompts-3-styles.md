# S01E01 — prompts du pilote, plans 1 à 6, trois styles

**22 août 2026.** Pilote de format. Il sert à trancher deux choses en une seule passe : **le style**, A, B ou C, et **le moteur de rendu vidéo**, ComfyUI local contre API. Rien d'autre n'est produit tant qu'il n'est pas validé.

Périmètre : plans 1 à 6, séquence d'ouverture froide, **81 secondes**, registre ÉPOQUE de bout en bout sauf le carton du plan 6. Par style : **18 images clés et 16 clips**. Pour les trois styles : **54 images et 48 clips**.

Le plan 6 est un POST, il ne se génère pas : il fige la dernière image du dernier clip du plan 5 et reçoit le carton titre au montage.

---

# 1. Règle d'assemblage

Un prompt d'image complet est la concaténation, dans cet ordre :

```
[BLOC DE STYLE version plan de scène]  +  [TRAITEMENT D'ÉPOQUE du style]  +  [brique de plan]  +  Avoid: [négatives de la brique] + [base négative du style] + [base négative personnages d'époque] + [négative universelle]
```

Un prompt de mouvement complet est la concaténation :

```
[BLOC DE STYLE version plan de scène]  +  [brique de mouvement]  +  NEGATIVE: [négatives de mouvement]
```

**Les blocs se copient octet pour octet. Ils ne se reformulent jamais.** Seules les briques des points 6 et 7 changent d'un plan à l'autre.

Réglages images : `nano_banana_pro`, 16:9, 2K, une image par requête, 2 crédits. Réglages vidéo : voir `PIPELINE-video-et-voix.md`.

**Sept références d'image au maximum par appel, dans l'ordre décor, personnages, accessoires.**

---

# 2. Les trois blocs de style, version plan de scène

Attention, ce ne sont pas les blocs des fiches. Les blocs de la fiche personnages se terminent par `on a plain flat light grey background`, parce qu'ils servent à produire des planches sur fond neutre. Ici les personnages sont **dans un décor**. La clause de fond neutre est donc remplacée par le traitement de fond du style, repris de l'ouvreur de décor de la fiche v3.4. Tout le reste est identique, mot pour mot.

## Style A — plan de scène

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:
```

## Style B — plan de scène

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:
```

En style B, **tous** les personnages sont des inkmen, sans exception, foule comprise. La règle des moufles s'applique à chaque main visible.

## Style C — plan de scène

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:
```

---

# 3. Traitement d'époque

À coller immédiatement après le bloc de style. Les six plans du pilote sont en registre ÉPOQUE, donc il s'applique partout.

* **Style A** : `historical period setting in desaturated muted earth tones, dusty beige, stone grey, earth brown, softened contrast, era accurate architecture and props,`
* **Style B** : `era accurate historical setting, moody atmospheric period palette,`
* **Style C** : `era accurate historical setting, palette shifted toward muted earth tones while keeping deep teal shadows,`

---

# 4. Négatives

## 4.1 Négative universelle, sur toute image sans exception

```
text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin
```

## 4.2 Base personnages d'époque, jamais optionnelle

```
dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing
```

## 4.3 Bases négatives par style

* **Style A** : `gradient shading, soft shading, airbrush, painterly, thin delicate linework, photorealism, photograph, realistic skin texture, 3D render, CGI, live action, anime style, manga, corporate flat vector art, extra characters.`
* **Style B** : `plain round ball hands, hollow circle hands, teardrop hands, pointed armless stumps, separate fingers, realistic hands, missing hand, missing arm, realistic human anatomy, detailed face, nose, photorealism, 3D render, anime, manga, extra inkman characters.`
* **Style C** : `gradient shading, soft shading, airbrush, painterly, rendered highlights, digital painting, muddy colors, cold blue palette, violet palette, purple palette, photorealism, photograph, 3D render, CGI, live action, anime, manga, flat vector art, extra characters.`

En style B, la clause `painted background, realistic painted scenery, interior decor` de la fiche est **retirée ici**, et seulement ici : le fond peint est voulu sur un plan de scène. Elle reste en vigueur sur les planches de personnage et sur les props.

## 4.4 Négative de foule, sur les plans 1a, 1b, 2 et 4a

```
readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures
```

## 4.5 Négatives de mouvement, sur tout prompt de clip

```
photorealistic rendering, skin texture, smooth gradients, cut, scene change, camera shake, morphing, text, watermark, lip sync, mouth articulation, extra characters appearing
```

---

# 5. Références à réinjecter

Sept au maximum par appel, dans l'ordre décor, personnages, accessoires. Toutes existent déjà dans le dépôt et sont validées.

| Brique | Fichier | Utilisée sur |
|---|---|---|
| Décor sol | `assets/S01E01/decors/Style{A,B,C}/D01_Style*.png` | 1a, 1b, 2, 3, 4a |
| Décor ciel | `assets/S01E01/decors/Style{A,B,C}/D02_Style*.png` | 4b, 5 |
| Foule | `assets/S01E01/personnages-episode/Style*/Foule_Style*.png` | 1a, 1b, 2, 4a |
| Garnerin | `assets/S01E01/personnages-episode/Style*/Garnerin_Style*.png` | 3, 4a, 4b, 5 |
| Parieurs | `assets/S01E01/personnages-episode/Style*/Parieurs_Style*.png` | 2 |

Consigne à ajouter en fin de prompt sur tout plan qui réinjecte un personnage :

```
same characters as reference, same art style as reference
```

**Rappel de la RÈGLE 1 du dépôt : la référence impose sa mise en page.** Une fiche personnage est un plan pied sur fond neutre ; réinjectée seule, elle ramène cette disposition. C'est pourquoi la plaque de décor se réinjecte **toujours en premier** et que le cadrage est nommé explicitement dans chaque brique.

## Blocs identité, à insérer dans la brique quand le personnage est nommé

**Garnerin**, styles A et C :

```
Garnerin, a French aeronaut of the Directoire era, resolute determined face with a calm set jaw, dark tailcoat, hair tied back, pale scarf at the neck, period breeches and buckled shoes, upright decided posture
```

**Garnerin**, style B :

```
Garnerin, an inkman stick figure character, a few ink strokes of hair tied back on his round head, simple black dot eyes with no eyebrows, resolute small mouth, wearing a dark Directoire tailcoat drawn as a simple flat shape, a pale scarf knotted at the neck, simple period shoes on his stick legs, upright decided posture
```

**Parieurs**, styles A et C :

```
the round onlooker wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; the thin onlooker leaning on a cane, threadbare coat, suspicious squint
```

**Parieurs**, style B :

```
the round bellied onlooker inkman with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his belly, peremptory raised chin; the thin onlooker inkman leaning on a cane, threadbare coat, suspicious half closed dot eyes
```

**Foule**, styles A et C :

```
a dozen Directoire crowd silhouettes, MOST OF THEM SEEN FROM BEHIND and the rest in three quarter view from behind, varied scales, NO FACE VISIBLE ON ANY FIGURE, no facial features at all: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, simplified figures less detailed than main characters
```

**Foule**, style B :

```
a dozen Directoire inkman crowd silhouettes, MOST OF THEM SEEN FROM BEHIND, varied scales, plain round BLANK heads with absolutely no facial features, NO EYES, no dots, no mouths, men with tall hats and simple flat tailcoats, women with high waisted dresses and shawls, a few small inkman children, simplified figures even less detailed than the main characters
```

**L'aide de Garnerin**, plan 3 seulement, figure au fil de l'eau, pas de planche dédiée. Styles A et C : `an assistant in a rough jacket with rolled up sleeves, seen from behind at the edge of frame`. Style B : `an inkman assistant in a rough flat jacket, seen from behind at the edge of frame`.

---

# 6. Briques d'image, un clip après l'autre

Seize images de départ, deux images de plan FIXE. Identiques dans les trois styles : **seul le bloc de style change**. C'est le principe même du pilote, comparer trois rendus du même contenu.

Nommage : `P<plan><bloc>-<clip>_Style<X>.png`, par exemple `P1a-3_StyleC.png`. Les plans FIXE : `P02_StyleA.png`.

## Plan 1a — 9 s, 4 clips

**1a-1** (0,0 à 2,5 s) · `Scene: dawn mist drifting low over the lawns of Parc Monceau, a large inflated gas balloon swaying in the middle ground, a Directoire crowd gathered at its foot. Framing: very wide establishing shot, slight high angle. Decor: D1. Characters: [FOULE]. Props: balloon, wicker basket, ropes trailing on the grass.`

**1a-2** (2,5 à 5,0 s) · `Scene: the inflated balloon swaying in the wind, mooring ropes pulling taut. Framing: medium shot on the balloon. Decor: D1. Characters: a few crowd figures at the lower edge, seen from behind. Props: balloon, taut ropes, stakes.`

**1a-3** (5,0 à 7,0 s) · `Scene: banners snapping at the top of the balloon. Framing: low angle from the ground toward the crown of the balloon. Decor: D1, sky and treetops only. Characters: none. Props: balloon crown, netting, banners.`

**1a-4** (7,0 à 9,0 s) · `Scene: the whole crowd turning their heads in one movement toward the wicker basket. Framing: very wide shot, slight high angle. Decor: D1. Characters: [FOULE]. Props: balloon, basket, ropes.`

## Plan 1b — 9 s, 3 clips

**1b-1** (0,0 à 3,0 s) · `Scene: the crowd parting into two lines, hats lifted. Framing: wide shot at eye level, down the axis of the lane. Decor: D1. Characters: [FOULE]. Props: hats, canes.`

**1b-2** (3,0 à 6,0 s) · `Scene: the wicker basket carried forward by assistants, ropes trailing. Framing: lateral medium shot. Decor: D1. Characters: two assistants in rough jackets, crowd behind them seen from behind. Props: wicker basket, ropes.`

**1b-3** (6,0 à 9,0 s) · `Scene: the basket being lashed under the balloon, hands knotting the ropes. Framing: close shot on the knots. Decor: D1, blurred behind. Characters: hands and forearms only. Props: ropes, wicker rim, iron ring.`

## Plan 2 — FIXE, 10 s, image unique

**P02** · `Scene: two Directoire onlookers in the foreground leaning toward each other to make a bet, the basket and the crowd behind them. Framing: medium close shot at chest height, slightly low angle. Decor: D1. Characters: [PARIEURS], [FOULE] far behind. Props: cane, cockaded hats.`

Mouvement de montage, appliqué au montage et non généré : **travelling latéral lent vers la droite, des badauds vers la nacelle.**

## Plan 3 — FIXE, 12 s, image unique

**P03** · `Scene: inside the basket, Garnerin checking a large folded bundle of silk, his assistant speaking to him from the rim. Framing: medium shot over the assistant's shoulder, the assistant in the foreground. Decor: D1 seen past the rim of the basket. Characters: [GARNERIN], [AIDE]. Props: folded silk bundle, ropes, a knife tucked at the side of the basket.`

Mouvement de montage : **zoom avant lent sur le paquet de soie plié.**

## Plan 4a — 10 s, 3 clips

**4a-1** (0,0 à 3,0 s) · `Scene: the balloon tearing away from the ground, the released ropes falling back. Framing: very wide shot at crowd level, the backs of onlookers in the foreground. Decor: D1. Characters: [FOULE] from behind. Props: balloon, basket, falling ropes.`

**4a-2** (3,0 à 6,0 s) · `Scene: the crowd rocking backwards to follow the balloon with their eyes, hats held on with both hands. Framing: medium shot on the crowd from behind and slightly to the side. Decor: D1. Characters: [FOULE]. Props: hats, shawls.`

**4a-3** (6,0 à 10,0 s) · `Scene: the balloon rising and shrinking above the trees. Framing: wide low angle shot. Decor: D1, treetops and sky. Characters: none. Props: balloon, basket, trailing rope.`

## Plan 4b — 10 s, 3 clips

**4b-1** (0,0 à 3,5 s) · `Scene: seen from the basket, the rooftops of Paris sliding slowly below, chimney smoke streaming. Framing: very wide high angle shot, the rim of the basket in the foreground. Decor: D2. Characters: none. Props: wicker rim, rope, folded silk bundle.`

**4b-2** (3,5 à 7,0 s) · `Scene: the wicker rim vibrating in the wind, a gloved hand tightening on it. Framing: close shot on the hand and the rim. Decor: D2, blurred sky behind. Characters: [GARNERIN], gloved hand only. Props: wicker rim, glove, rope.`

**4b-3** (7,0 à 10,0 s) · `Scene: the whole city under the haze, the crowd reduced to a dark patch in the middle of the park. Framing: very wide high angle shot. Decor: D2. Characters: none. Props: none.`

## Plan 5 — 8 s, 3 clips

**5-1** (0,0 à 2,5 s) · `Scene: a hand taking hold of the knife tucked at the side of the basket. Framing: very close shot. Decor: D2, out of focus behind. Characters: [GARNERIN], hand only. Props: knife, wicker side, taut rope.`

**5-2** (2,5 à 5,5 s) · `Scene: the blade sawing the taut rope, fibres springing free one by one. Framing: very close shot at a raking angle along the rope. Decor: D2, out of focus behind. Characters: hand only. Props: knife, rope, loose fibres.`

**5-3** (5,5 à 8,0 s) · `Scene: the rope giving way at once, the strands whipping the air. Framing: very close frontal shot on the break. Decor: D2, out of focus behind. Characters: none. Props: severed rope, whipping strands.`

**La dernière image de 5-3 est la source du plan 6.** Elle est figée au montage et reçoit le carton titre. Aucune génération.

---

# 7. Briques de mouvement, un clip après l'autre

Un clip = **un geste continu, aucune coupe**. Le gabarit complet est au point 6 de `PIPELINE-video-et-voix.md`. Ci dessous, seule la partie variable.

| Clip | Durée | Subject | Camera |
|---|---|---|---|
| 1a-1 | 2,5 s | the mist drifts slowly across the lawns, the crowd sways gently at the foot of the balloon | static |
| 1a-2 | 2,5 s | the balloon sways in the wind, the mooring ropes pull taut and slacken | static |
| 1a-3 | 2,0 s | the banners snap in the wind at the crown of the balloon | static |
| 1a-4 | 2,0 s | the crowd turns their heads in one movement toward the basket | static |
| 1b-1 | 3,0 s | the crowd parts into two lines, hats are lifted | static |
| 1b-2 | 3,0 s | the basket is carried forward, ropes trailing on the grass | slow lateral tracking to the right, following the basket |
| 1b-3 | 3,0 s | hands knot the ropes around the wicker rim | static |
| 2 | — | plan FIXE, mouvement au montage | — |
| 3 | — | plan FIXE, mouvement au montage | — |
| 4a-1 | 3,0 s | the balloon tears away from the ground, the released ropes fall back | static |
| 4a-2 | 3,0 s | the crowd rocks backwards, hats held on with both hands | static |
| 4a-3 | 4,0 s | the balloon rises and shrinks above the trees | very slow tilt upward, following the balloon |
| 4b-1 | 3,5 s | the rooftops slide slowly below, chimney smoke streams sideways | static |
| 4b-2 | 3,5 s | the wicker rim vibrates, the gloved hand tightens on it | static |
| 4b-3 | 3,0 s | the haze drifts over the city, the dark patch of the crowd stays still | very slow zoom out |
| 5-1 | 2,5 s | the hand takes hold of the knife | static |
| 5-2 | 3,0 s | the blade saws the rope, fibres spring free one by one | static |
| 5-3 | 2,5 s | the rope gives way at once, the strands whip the air | static |

Treize clips sur seize sont à caméra fixe. C'est voulu : en deux à trois secondes, un mouvement de caméra ajouté à un sujet qui bouge donne de la bouillie. Le mouvement de caméra est réservé aux plans FIXE, où il est fait au montage sur une image nette.

---

# 8. Table de génération

Par style : **18 images**, **16 clips**. Trois styles : **54 images, 48 clips**.

| Étape | Volume | Où | Coût |
|---|---|---|---|
| Images clés | 54 | Higgsfield, `nano_banana_pro`, 16:9, 2K | **108 crédits** |
| Clips | 48 | ComfyUI sur RunPod, Wan 2.2 I2V | environ 4 h de GPU, 4 à 8 $ |
| Contre épreuve | 16 clips d'un seul style | Higgsfield, Kling 3.0, image de départ et image de fin | environ **110 crédits** |

---

# 9. Contrôles avant de valider le pilote

Les treize points de la grille de contrôle visuel de `METHODE-generation-images.md` s'appliquent à chaque image. En plus, propres au pilote :

1. **Aucun visage lisible dans la foule**, sur aucun des quatre plans de foule, dans aucun des trois styles. C'est le défaut qui est déjà passé trois fois.
2. **Garnerin est le même homme** au plan 3, au plan 4a et au plan 4b. Le comparer côte à côte avant de lancer les clips.
3. **Les deux badauds du plan 2** ont bien le haut chapeau à cocarde sur le rond à gauche et la canne sur le maigre à droite. L'inversion est un défaut connu.
4. **Style B** : moufle noire arrondie à petit pouce sur chaque main visible, y compris les mains qui nouent du clip 1b-3 et la main gantée du 4b-2.
5. **Aucune couleur réservée dominante** : ni sable, ni sarcelle vif, ni orange vif sur un costume du Directoire.
6. **Aucun texte nulle part**, y compris sur les bannières du clip 1a-3, qui doivent rester des aplats.
7. **Continuité du raccord** : la dernière image de chaque clip doit pouvoir servir de première image du suivant à l'intérieur d'un même bloc. Vérifier sur 1a, 1b, 4a, 4b et 5.
8. **Les trois styles côte à côte** sur le même plan : est ce que le style C se distingue vraiment du style A sur ces cadrages ? La RÈGLE 15 dit qu'il ne se distingue que sur les plans rapprochés. Le pilote contient des très gros plans, plans 5-1 à 5-3, c'est l'occasion de trancher.
