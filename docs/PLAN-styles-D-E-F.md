# Styles D à K — plan de test

**23 août 2026.** Huit styles supplémentaires ont été mis à l'épreuve. **Trois sont retenus : D, J et K.** Le style C reste retiré (décision du 22 août, 15 h 05) ; A et B gardent leurs pilotes complets et ne sont pas régénérés.

| Style | En un mot | Sort |
|---|---|---|
| **D** | anime d'aventure moderne, deux registres de lumière. Cible d'ambiance : le fan film joint par Guillaume | **retenu** |
| ~~E~~ | 2D graphique angulaire à fort contraste | abandonné le 23 août |
| ~~F~~ | 3D stylisé mat, personnages taillés à facettes | abandonné le 23 août |
| ~~G~~ | 3D cartoon à formes rondes et souples, lumière chaude | abandonné le 23 août |
| ~~H~~ | 2D imprimé, trames, décalage chromatique | abandonné le 23 août |
| ~~I~~ | roman graphique européen, ligne claire, gouache | abandonné le 23 août |
| **J** | cinéma réaliste, prise de vue 35 mm, comédiens en costume | **retenu** |
| **K** | 3D de long métrage à registre adulte, proportions crédibles, étalonnage sobre | **retenu** |

**Décision du 23 août, en deux temps.** E, F et H écartés d'abord, puis G et I. **Restent D, J et K.** Les images des cinq styles écartés sont supprimées du dépôt ; leurs blocs, leurs négatives et leur audit restent consignés dans ce document et dans `S01E01-epreuve-styles-audit.md`, pour ne pas repayer les mêmes constats.

**Ce que ce trio dit du projet.** Les trois retenus sont les trois styles à **visage crédible et lumière cinématographique** du lot. D est leur version dessinée, K leur version animée en volume, J leur version photographiée. Les cinq écartés étaient tous des styles à forme affirmée, aplats, angles, rondeurs, trames. La série s'oriente donc vers un registre de **récit**, pas de gag graphique, ce qui a des conséquences au delà du style : le ton du scénario, le jeu des voix et le rythme du montage ont été écrits pour l'autre registre.

**Le rang des trois selon l'audit** : K premier, J troisième, D cinquième. Aucun n'est éliminé par ses images ; ce qui les sépare vraiment est en dessous, section 6, étape 2.

Ce document est le frère de `S01E01-pilote-prompts-3-styles.md`. Ce dernier n'est pas modifié : ses trois blocs sont verrouillés et se copient octet pour octet. Tout ce qui concerne D à K vit ici.

État de préparation des trois retenus, poste par poste : `ETAT-DE-PREPARATION-styles-D-J-K.md`.

---

# 1. Ce que veut dire « tester un style », en volume et en crédits

Un style n'est pas un prompt, c'est un jeu complet d'assets. Le dépôt compte **319 images actives réparties en trois styles**. Pour un style, le compte exact est :

| Poste | Volume par style |
|---|---|
| Bible, turnarounds | 4 |
| Bible, références de production | 4 |
| Bible, poses | 8 |
| Bible, têtes d'expression | 24 |
| Bible, planches d'expression | 4, assemblées en local, gratuites |
| Décors D01 à D33 et variantes | 46 |
| Personnages d'époque | 12 |
| Assets partagés | 4 |
| Images clés du pilote, plans 1 à 6 | 20 |
| **Total facturé** | **122 images, soit 244 crédits** |

Huit styles complets coûteraient **1 952 crédits** sur les **842** de départ : c'est hors d'atteinte, et même un seul style complet représente près du tiers du solde. On ne produit donc aucun style en entier avant que le choix soit fait. Le test procède par **épreuves discriminantes successives, avec un point d'arrêt dur à chaque palier**, et l'on ne paie le palier suivant que sur ce qui a survécu au précédent.

---

# 2. Trois avertissements de méthode, avant toute génération

## 2.1 Aucune marque ni aucun nom d'auteur dans un prompt

Ni titre de film, ni nom de série, ni nom de réalisateur, nulle part dans un prompt, un nom de fichier ou un nom de dossier. Deux raisons, également contraignantes : le modèle refuse ou renvoie des designs protégés, et une image dérivée d'un design protégé n'est pas exploitable dans la série. Ce que l'on décrit, ce sont des **procédés visuels** : nature du trait, construction des formes, palette, mode d'ombrage, mise en scène. Un procédé n'appartient à personne ; un personnage et un design appartiennent à quelqu'un. Les blocs de la section 4 sont écrits selon cette règle et ne se reformulent pas.

## 2.2 La vidéo jointe est une ambiance, pas une charte

Elle est elle même générée. Elle prouve que ce rendu est atteignable par une chaîne générative, mais son style **dérive d'un plan à l'autre** : extérieurs jour très peints, scènes de tension en contraste dur, et au moins un plan d'objet qui bascule en 3D quasi photographique. On en extrait un bloc de base et deux traitements de lumière, section 4.1, et l'on s'y tient. On ne cherche pas à reproduire le film.

## 2.3 Aucune image d'un style ne se réinjecte dans le prompt d'un autre

RÈGLE 1 du dépôt : **la référence impose sa mise en page, et elle impose son style**. Réinjecter une plaque `D01_StyleA` dans un prompt D ramènerait le style A. Chaque nouveau style repart sans référence, et ne se constitue les siennes qu'à l'étape 3. C'est la raison pour laquelle l'épreuve de l'étape 1 se fait à sec, et la raison pour laquelle **les images d'épreuve ne raccorderont pas avec le pilote** : elles ont été produites sans référence, les vingt du pilote en auront cinq.

## 2.4 Trois règles de la méthode ne s'appliquent pas aux nouveaux styles

Les RÈGLES **15** (le style C sur personnage en pied), **16** (le pouce des moufles) et **20** (en style B, une main qui touche un objet mange son bras) sont des résultats négatifs **propres aux styles B et C**. Elles ne portent sur aucun des styles D à K. Toutes les autres restent en vigueur, **sauf une nuance acquise le 23 août** : sur les styles réalistes J et K, la négative universelle anti lettrage ne suffit plus, voir la RÈGLE 33.

---

# 3. Nommage

Convention inchangée, `<Asset>_<Style>.png`, avec `Style` valant `StyleA`, `StyleB`, `StyleC`, `StyleD`, `StyleJ` ou `StyleK`. Dossiers `decors/StyleD`, `personnages-episode/StyleD`, `pilote/images/StyleD`, et ainsi de suite.

---

# 4. Les blocs de style, version plan de scène

Ils se collent en tête de prompt, suivis du traitement d'époque, puis de la brique de plan, puis de `Avoid:` et des négatives. **Ils se copient octet pour octet et ne se reformulent jamais.**

## 4.1 Style D — anime d'aventure moderne

Bloc de base, commun aux deux registres :

```
2D anime illustration, modern cinematic adventure anime style, clean thin dark brown ink linework with subtle weight variation, cel shaded characters with a soft airbrush gradient blending each shadow into its base tone, warm natural skin with a faint blush on the cheeks, adult realistic body proportions and grounded facial features, expressive eyes with a single specular highlight, hand painted background with atmospheric depth and aerial perspective, volumetric light, shallow depth of field with the background softly out of focus, fine film grain, 16:9 frame:
```

**Traitement de lumière JOUR**, sur les plans d'extérieur et de foule. **Corrigé le 23 août** :

```
soft diffused key light, gentle contrast, clear readable midtones, luminous but restrained greens,
```

> La version d'épreuve portait `bright daylight, saturated blue sky with tall billowing cumulus clouds`. Résultat : les trois images D sont sorties en plein midi de ciel bleu, alors que le décor D1 prescrit une aube d'octobre brumeuse. **Le traitement de lumière a battu l'heure décrite par le décor.** La clause de ciel est retirée : l'heure appartient au décor, le traitement ne règle que la qualité de la lumière. C'est la même leçon que la RÈGLE 32, sous une autre forme : un bloc invariant ne doit pas décrire ce qu'une brique variable décrit déjà.

**Traitement de lumière TENSION**, sur les plans dramatiques, l'aube, la brume et le vide :

```
hard directional key light, a single hard edged cast shadow shape across each face, palette pulled to warm amber or to near black, strong contrast, glowing rim light along the silhouette,
```

Sur le pilote, les plans au sol 1a, 1b, 2, 3 et 4a sont en JOUR ; les plans en l'air 4b et 5 sont en TENSION, où la brume, le vide et le couteau appellent le contraste dur. Le registre s'écrit dans l'index du plan, il ne se décide pas au tirage.

Traitement d'époque D, à coller après le traitement de lumière :

```
era accurate historical setting, costumes in muted earth tones, period architecture and props,
```

Base négative D :

```
flat vector art, thick uniform black outline, corporate flat design, chibi proportions, super deformed, oversized anime eyes on adult characters, moe face, photorealism, photograph, 3D render, CGI, live action, extra characters.
```

> **Point de fond sur D.** Ce bloc **inverse** les bases négatives de A, B et C, qui interdisent toutes `gradient shading, soft shading, airbrush, painterly` et `anime`. Ce n'est pas une variante des trois styles existants, c'est le parti pris opposé : ombrage adouci voulu, décor peint voulu, profondeur de champ voulue. En conséquence, aucune négative de A, B ou C ne se recycle sur D.

## 4.2 Style E — 2D graphique angulaire

```
hand drawn 2D animation in a bold graphic poster style, strongly angular geometric character design built from sharp straight edged planes and decisive silhouettes, faces reduced to a few deliberate shapes with minimal interior detail, no outline on most colour areas and a thin dark accent line only where two shapes must be separated, flat colour fills with one hard edged shadow shape and no blending, dramatic high contrast lighting, restrained palette of three or four colours in the whole image, wide horizontal staging with large areas of empty space, background painted in flat gouache washes with visible dry brush texture, 16:9 frame:
```

Traitement d'époque E :

```
era accurate historical setting, restrained palette of dusty ochre, stone grey and deep ink blue, period architecture reduced to flat geometric masses,
```

Base négative E :

```
thick uniform outline around every shape, rounded soft character design, gradient shading, soft shading, airbrush, painterly rendering, cluttered background, busy small detail, many colours, photorealism, photograph, 3D render, CGI, live action, anime, manga, extra characters.
```

> **Point de fond sur E.** C'est le plus proche parent du style A : aplats, ombre d'un seul tenant, aucun dégradé. Il en diffère sur trois points mesurables, l'angularité des formes, l'absence de contour sur la plupart des aplats, et une palette bornée à trois ou quatre couleurs par image. Ces trois points sont exactement ce qu'il faudra contrôler à l'audit : si les images E sortent avec un contour noir épais partout et huit couleurs, ce n'est pas E, c'est A.

## 4.3 Style F — 3D stylisé mat

```
stylized 3D computer animation, characters carved from angular faceted planes with a strong squared jaw and sharp cheekbones, matte non reflective surfaces everywhere, visible woven cloth texture and hand painted texture on every material, skin rendered as matte painted surface with a slight dry brush grain and no specular sheen, cinematic three point lighting with soft shadows, moderate depth of field, physically staged sets with real volume and fine dust in the air, deliberately non photorealistic, the look of an animated puppet rather than a person, 16:9 frame:
```

Traitement d'époque F :

```
era accurate historical setting, muted earth toned costumes with visible fabric weave, period architecture built as real volumes with weathered surfaces,
```

Base négative F :

```
photorealism, photograph, live action, realistic human skin, subsurface scattering, glossy specular highlights, plastic sheen, wax figure, uncanny realistic face, video game screenshot, 2D drawing, flat cel shading, anime, manga, extra characters.
```

> **Point de fond sur F.** C'est le style qui s'écarte le plus de tout ce que le dépôt a construit. Il abandonne l'aplat, le contour et le 2D, donc l'argument du LoRA de style entraîné sur les 253 images validées ne vaut plus. Il porte aussi un risque propre, la **glissade vers le photoréalisme** : le modèle a vu bien plus de 3D photo que de 3D stylisé mat, et la négative seule ne suffira pas si les positifs `matte`, `woven cloth texture` et `puppet` ne tiennent pas. C'est l'objet du contrôle 3 de la section 7.

## 4.4 Style G — 3D cartoon à formes rondes

```
stylized 3D cartoon animation, feature animation look, appealing rounded character design built from soft bouncy volumes with no sharp angles anywhere, large expressive eyes, generous head on a compact body, smooth clean surfaces with a soft matte finish, gentle rim light and warm bounce light, rich saturated colour, shallow depth of field, cinematic lighting with soft shadows, polished and playful, absolutely not photorealistic, 16:9 frame:
```

Traitement d'époque G :

```
era accurate historical setting, costumes simplified into big readable shapes in muted earth tones, period architecture rounded and slightly caricatured,
```

Base négative G :

```
angular faceted character design, squared jaw, sharp cheekbones, hard edged planes, photorealism, photograph, live action, realistic human proportions, realistic skin pores, uncanny face, video game screenshot, 2D drawing, flat cel shading, anime, manga, extra characters.
```

> **Point de fond sur G.** C'est le contre pied exact de F, et les deux se lisent l'un contre l'autre : même technique, 3D stylisé, parti pris de forme opposé. Les quatre premières clauses de sa négative sont mot pour mot le positif de F. G est le seul des six styles où **la troupe se transpose presque sans redessin** : Sam, SamBis, Naya et Elio sont déjà construits en formes rondes et en grosse tête sur petit corps. C'est un avantage de coût considérable à l'étape 2.
>
> **Ce que G ne risque pas, contrairement à ce que ce document affirmait d'abord.** J'avais écrit que la rondeur ferait un registre trop enfantin pour un homme qui coupe une corde à mille mètres au dessus de Paris. C'est faux, et l'épreuve le montre : le P4b-1 en style G a un vrai vertige. La rondeur d'un volume ne détermine pas le registre d'un plan ; ce qui le détermine, ce sont **la lumière, le cadrage et la palette**. Un personnage rond en contre jour dur, cadré serré, en palette désaturée, porte le drame aussi bien qu'un personnage anguleux. L'inverse est vrai aussi : un style anguleux éclairé à plat et coloré vif ne fait pas sérieux pour autant.
>
> La conséquence pratique est que **G n'a pas de risque propre lié à sa forme**. Son vrai point de vigilance est ailleurs : la lumière chaude et l'ambiance douce prescrites par son bloc, `gentle rim light and warm bounce light, rich saturated colour, polished and playful`. Ce sont ces clauses là qui adouciraient les plans 4 et 5, pas les volumes ronds. Elles se remplacent, pour les plans de tension, par un traitement de lumière dur, sur le modèle des deux registres du style D.

## 4.5 Style H — 2D imprimé moderne, 12 à 20 ans

```
stylized 2D animation with a modern printed comic energy, confident brush inked linework of varying weight, painted colour with visible dry brush and canvas texture, halftone dot screens inside the shadows, a subtle chromatic offset along the edges as if the print were slightly misregistered, bold saturated palette with strong complementary rim lights in magenta and cyan against warm mid tones, dynamic diagonal staging with forced perspective, dramatic depth of field, graphic energy over realism, 16:9 frame:
```

Traitement d'époque H :

```
era accurate historical setting, period costume and architecture kept accurate but pushed graphic and high contrast, muted earth tones in the fabrics with the saturated colour carried entirely by the light,
```

Base négative H :

```
flat vector art, clean digital gradients, smooth airbrush, photorealism, photograph, 3D render, CGI, live action, chibi proportions, cute mascot design, muddy colours, low contrast, extra characters.
```

> **Point de fond sur H.** Le raisonnement derrière ce bloc : ce qui distingue l'animation qui parle aux 12 à 20 ans aujourd'hui, ce n'est ni le trait ni la technique, c'est **la matière et la lumière**. Texture d'impression visible, trames de demi teinte, léger décalage de couches, et surtout une lumière qui porte la couleur saturée pendant que les tissus restent sourds. C'est exactement compatible avec la contrainte d'époque du projet : les costumes restent justes et ternes, la couleur vient des sources.
>
> Son risque propre est le seul du lot qui touche à la **couleur réservée** : des lumières magenta et cyan sur des figurants au premier plan peuvent rejouer la RÈGLE 30, où le modèle prête aux figurants la palette des trois héros. À surveiller en priorité sur P02.

## 4.6 Style I — roman graphique européen, 30 à 40 ans

```
hand drawn 2D illustration in a European graphic novel manner, restrained clear line drawing with an even thin ink contour, colour laid in flat gouache with visible paper grain and slight brush irregularity, naturalistic adult proportions and understated faces without any cartoon exaggeration, muted sophisticated palette of ochre, slate, olive and faded brick, quiet even lighting with soft ambient shadow rather than dramatic contrast, calm horizontal composition with generous air, restrained and literary rather than spectacular, 16:9 frame:
```

Traitement d'époque I :

```
era accurate historical setting, carefully observed period costume and architecture, documentary accuracy in the detail,
```

Base négative I :

```
cartoon exaggeration, oversized eyes, chibi proportions, thick uneven outline, glossy digital rendering, airbrush, neon colours, oversaturation, dramatic rim light, photorealism, photograph, 3D render, CGI, live action, anime, manga, extra characters.
```

> **Point de fond sur I.** Le raisonnement : pour un adulte de 30 à 40 ans, la marque de sérieux d'une série historique n'est pas le spectacle, c'est la **retenue et la justesse documentaire**. Ligne claire, gouache, grain de papier, lumière égale, composition calme. C'est aussi le style qui sert le mieux le registre CADRE du projet, la table et les objets, et le seul qui rende crédible un ton de récit plutôt que de gag.
>
> Deux risques propres, opposés l'un à l'autre. D'abord la **platitude** : un style calme sur un épisode d'action peut tomber à plat aux plans 4 et 5. Ensuite la **troupe** : des proportions adultes naturalistes et des visages sans exagération sont incompatibles avec quatre personnages de dessin animé, donc I impose un redessin complet de la bible, au même titre que D et F.

## 4.7 Style J — cinéma réaliste

```
live action cinema look, photographed on 35mm film, naturalistic period drama cinematography, real actors in accurate historical costume, motivated practical lighting with soft overcast daylight and deep natural falloff, shallow depth of field with creamy bokeh, fine organic film grain, subtle halation on the highlights, desaturated filmic colour grade with rich blacks and warm skin tones, photorealistic, 16:9 frame:
```

Traitement d'époque J :

```
era accurate 1797 Directoire France, authentic period costume, real fabrics with wear and dirt, period architecture and props photographed on location,
```

Base négative J :

```
illustration, drawing, painting, cartoon, anime, manga, 3D render, CGI, video game, painterly, cel shading, ink outlines, plastic skin, waxy face, over sharpened, HDR, deformed hands, extra fingers, letterbox bars, black bars, extra characters.
```

**Clause de plein cadre, obligatoire sur tout prompt J.** À coller en fin de bloc de style :

```
the image fills the entire 16:9 frame edge to edge, no black bars,
```

> `letterbox bars, black bars` était déjà dans la négative, et `P02_StyleJ` est sorti avec deux bandes noires latérales quand même. Un cadre de cinéma **a** des bandes : c'est une structure, pas un élément, et une négative n'agit pas sur une structure. Corollaire de la RÈGLE 33.

**Traitement de lumière TENSION**, ajouté le 23 août, sur les plans 4b, 5 et 6 :

```
hard directional key light with deep shadow across two thirds of the frame, desaturated grade pulled to cold grey and near black, high contrast, tight framing, long lens compression,
```

> J n'avait qu'un seul traitement, contrairement à D. Sur un pilote qui finit par un homme qui coupe une corde au dessus de Paris, un seul registre de lumière ne suffit pas.

> **Point de fond sur J, et il est lourd.** J n'est pas un style d'animation, c'est l'abandon de l'animation. Ce qui tombe avec lui, dans l'ordre :
>
> * **La bible de la troupe.** Sam, SamBis, Naya et Elio ne sont plus des dessins mais des personnes. Les 40 assets par style, les turnarounds, les six expressions, la logique entière de la référence de production perdent leur objet. On ne fait pas un turnaround d'un comédien, on fait un casting.
> * **Le LoRA de style.** Il sert à tenir un aplat que le modèle vidéo veut ramollir. Sur du photoréalisme, il n'y a rien à tenir : c'est le point d'attraction naturel de Wan 2.2.
> * **Les 33 règles de `METHODE-generation-images.md`**, dont l'essentiel traite de défauts propres au dessin, moufles, contours, aplats, deux tons.
> * **Le registre CADRE**, la table et les objets, qui suppose un espace non naturaliste.
>
> Ce qui est gagné en échange n'est pas nul : c'est le seul des huit styles que la chaîne vidéo rend **sans aucun effort de conformation**, et il n'a besoin d'aucune fiche de personnage pour tenir un figurant.
>
> Deux risques propres à surveiller : les **mains**, défaut classique du photoréalisme génératif, et le **Paris moderne** qui remonte dans les plans en plongée, d'où les clauses `modern buildings, glass towers` dans sa négative de P4b-1.

## 4.8 Style K — 3D de long métrage, registre adulte

```
stylized 3D feature animation, high end computer animated film look, believable human proportions with only a light touch of caricature in the features, soft subsurface skin with fine texture and no plastic sheen, individually groomed hair, real cloth simulation with visible weave and wear, naturalistic cinematography with motivated light and long lens compression, restrained desaturated colour grade, shallow depth of field, subtle volumetric atmosphere, an adult dramatic register rather than a comic one, stylized and not photographic, 16:9 frame:
```

Traitement d'époque K :

```
era accurate 1797 Directoire France, authentic period costume in muted earth tones with real fabric weave and wear, period architecture and props,
```

Base négative K :

```
photograph, live action, real actors, broad cartoon caricature, chibi proportions, oversized head, rubbery squash and stretch, plastic sheen, waxy face, uncanny, saturated candy colours, 2D drawing, cel shading, anime, manga, letterbox bars, black bars, extra characters.
```

**Traitement de lumière TENSION**, ajouté le 23 août, sur les plans 4b, 5 et 6 :

```
hard directional key light with deep shadow across two thirds of every volume, desaturated grade pulled to cold grey and near black, high contrast, tight framing, no warm bounce light,
```

> Même raison qu'en J. Et c'est en K que ce traitement porte le plus : la démonstration du §8 bis de l'audit est que **la forme ne fait pas le registre, la lumière le fait**. K est précisément le style G rendu adulte par la lumière, la focale et l'étalonnage.

> **Point de fond sur K.** K est à G ce que le registre de tension est à la lumière douce : **même technique, registre adulte**. Le raisonnement suit directement la correction de la section 4.4, la forme ne fait pas le registre. Là où G caricature les volumes et chauffe la lumière, K garde des proportions crédibles, une peau à texture fine, un étalonnage sobre et une longue focale.
>
> K est **le point de croisement de tout ce qui a été appris** : il vise le même public que I et J, avec la technique de G, et sans l'abandon de l'animation qu'impose J. Sa négative contient explicitement `photograph, live action, real actors`, sans quoi il glisserait sur J ; et `broad cartoon caricature, oversized head`, sans quoi il retomberait sur G. **Le contrôle décisif de son audit est là** : s'il n'est distinguable ni de J ni de G, il n'existe pas.
>
> Avantage pratique par rapport à J : la troupe reste dessinable. Elle demande un redessin en proportions crédibles, comme D et I, mais elle reste une bible d'assets et non un casting.

---

# 5. Négatives conservées, telles quelles

Reprises sans modification de `S01E01-pilote-prompts-3-styles.md`, sections 4.1, 4.2 et 4.4.

* **Négative universelle**, sur toute image sans exception : `text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin`
* **Base personnages d'époque**, jamais optionnelle : `dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing`
* **Négative de foule**, sur les plans 1a, 1b, 2 et 4a **et seulement s'il n'y a aucun personnage nommé à visage dans le cadre** (RÈGLE 26) : `readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures`

## 5.1 La foule, tranché le 23 août

**En D, on revient à la clause des styles A, B et C.** La question était ouverte : sur un style à visages détaillés, `NO FACE VISIBLE ON ANY FIGURE` risquait de reproduire les ovales de peau vides qui ont tué le style C. L'épreuve dit non. Aucun visage vide sur les 24 images, ni en D où la clause avait été remplacée par des silhouettes floues, ni dans les cinq styles où elle avait été gardée telle quelle. Et le remplacement **n'a pas pris** : la foule de `P02_StyleD` est nette et de dos, pas floue. La clause d'origine est donc sûre, et on ne garde pas une variante qui ne sert à rien.

**En J et en K, elle ne suffit pas.** Les deux styles réalistes ont sorti une dizaine de figurants nets, alignés, visages lisibles, qui posent au lieu de regarder le ballon. Le flou d'arrière plan seul n'y a rien fait. La clause de foule se durcit **en positif**, sur ces deux styles uniquement :

```
the crowd behind them all seen from behind, turned toward the balloon, no figure facing the camera, thrown out of focus by the shallow depth of field
```

## 5.2 Les bannières, en positif sur J et K

RÈGLE 33. Sur tout plan qui montre une bannière, une enseigne ou un drapeau, en style réaliste :

```
plain undecorated banners with no emblem and no lettering, blank fabric only
```

La négative universelle a tenu sur six styles graphiques et a cédé du premier coup sur les deux réalistes. Ce n'est pas un défaut de la négative, c'est ce qu'est un fanion d'époque.

---

# 6. Le plan, étape par étape

## Étape 0 — écriture. 0 crédit

Ce document. Blocs, traitements, négatives, nommage, périmètre. Rien n'est généré tant qu'il n'est pas relu.

## Étape 1 — épreuve de style. 18 images, 38 crédits. **Faite le 23 août.** Point d'arrêt dur

Trois plans par style, choisis parce que ce sont **exactement les trois endroits où A, B et C se sont séparés** lors de l'audit du pilote :

| Plan | Ce qu'il met à l'épreuve | Pourquoi celui là |
|---|---|---|
| **P02** | deux personnages nommés à visage au premier plan, une foule derrière | c'est le plan qui a fait tomber le style C, visages effacés par la négative de foule. Il montre d'un coup comment un style traite un visage lisible et comment il traite une foule. |
| **P1a-3** | contre plongée sous le ballon, bannières, filet, cordages, aucun visage | lisibilité graphique pure, et piège du lettrage : la fiche demande des aplats, le style A les a donnés, le style B a sorti des motifs héraldiques, acceptés faute de mieux pour le pilote. |
| **P4b-1** | toits de Paris en plongée, rebord d'osier, aucun personnage | le décor seul, la profondeur, l'atmosphère. C'est là que D et F ont le plus à gagner et E le plus à perdre. |

Conditions d'exécution :

* Briques de plan **reprises telles quelles** de `prompts/S01E01-pilote-prompts-assembles.md`. Seuls changent le bloc de style, le traitement d'époque et la base négative. C'est ce qui rend la comparaison honnête.
* **Aucune référence réinjectée** (section 2.3).
* Pour D, chaque plan porte son registre : P02 et P1a-3 en JOUR, P4b-1 en TENSION. D montre donc ses deux traitements sans image supplémentaire. Les cinq autres styles n'ont qu'un traitement.
* En G, H et I, **la clause de foule reste celle des styles A, B et C**. La formulation en silhouettes hors mise au point est propre à D.
* `nano_banana_pro`, 16:9, 2K, une image par requête, 2 crédits.

Prompts et identifiants : `prompts/S01E01-epreuve-styles-DEF-prompts.md`. Rapatriement : `scripts/telecharger_epreuve_DEF.ps1`, à lancer depuis Windows, le CDN de résultat n'étant pas joignable depuis le conteneur.

Livrable : une planche de comparaison 3 plans par 8 styles, D à I contre les images A et B déjà validées aux mêmes cadrages. Guillaume regarde en pleine résolution contre la grille de la section 7.

## Étape 2 — épreuve de troupe. 4 images par style survivant, 8 crédits chacun. Point d'arrêt dur

Les quatre personnages récurrents, Sam, SamBis, Naya et Elio, en référence de production, seuls, de face, sur fond neutre.

**C'est la question de fond du test, et elle est plus déterminante que les décors.** Sam, SamBis, Naya et Elio sont des personnages de dessin animé simple, construits en grosse tête sur petit corps.

| Style | Ce qu'il fait de la troupe | Ce que coûte l'opération |
|---|---|---|
| **D** | proportions adultes réalistes : redessin complet, mais la troupe reste dessinée et reste une bible | 40 images, plus un arbitrage de design sur le turnaround |
| **K** | proportions crédibles en volume : redessin complet, la troupe reste une bible d'assets | 40 images, plus le même arbitrage |
| **J** | **la troupe cesse d'être une bible.** Quatre personnes, pas quatre dessins. On ne fait pas un turnaround d'un comédien | ce n'est plus une génération d'assets, c'est un casting, et il faut inventer comment le verrouiller |

Les trois retenus imposent tous les trois de **redessiner la troupe**, aucun ne la transpose. Ce n'est donc plus un critère de départage entre eux, sauf pour J, où le problème change de nature.

**La question à trancher à l'étape 2 est donc différente de celle prévue.** Elle n'est plus « la troupe survit elle », mais : **Sam, SamBis, Naya et Elio existent ils encore comme personnages une fois qu'ils ne sont plus des dessins simples ?** Quatre figures conçues pour la grosse tête et la couleur réservée, portées à un registre naturaliste, peuvent perdre exactement ce qui les rendait reconnaissables d'un épisode à l'autre. Les couleurs réservées elles mêmes, sable, sarcelle vif, orange vif, sont une convention de dessin animé : sur un comédien en costume ou sur un volume étalonné sobre, elles deviennent une veste, pas une signature.

Un style qui rend de belles images mais qui dissout la troupe est un style perdu, et il vaut mieux le savoir pour 8 crédits que pour 244.

Le bloc de style de l'épreuve est celui de la section 4, avec `on a plain flat light grey background` substitué à la clause de fond, exactement comme la fiche troupe le fait pour A, B et C. Les blocs identité des quatre personnages sont invariants et se recopient depuis `prompts/fiche-prompts-troupe-recurrente.md`.

## Étape 3 — mini bible de raccord. 3 images par style retenu, 6 crédits chacun

`D01`, `Foule` et `Garnerin` dans le style retenu. Ce sont les trois références que les dix huit plans du pilote réinjectent le plus souvent. Elles se regardent une par une avant d'en dériver quoi que ce soit : c'est le point d'arrêt qui a coûté 96 images la dernière fois.

## Étape 4 — pilote complet. 20 images clés par style retenu, 40 crédits chacun

Mêmes plans, mêmes briques, mêmes cadrages, même ordre de réinjection que A et B, y compris les clés de dialogue P02a et P02b bouches fermées (RÈGLE 31) et les cadrages corrigés du lot 8. Comparaison image contre image avec les pilotes existants.

## Étape 5 — clips. 16 par style retenu, environ 1 h 20 de GPU et 1 à 2 $ chacun

Wan 2.2 I2V A14B sur RunPod, gabarit de mouvement v2 avec ligne de présence par clip, dialogue découpé par locuteur, un seul personnage qui parle par clip. Rien de neuf dans la chaîne.

> **Remarque qui compte pour le choix.** `PIPELINE-video-et-voix.md` §5.1 pose que le défaut de Wan 2.2 est de **ramollir le trait et d'ajouter du volume, du grain et de la lumière rasante dès la deuxième seconde**, ce qui oblige à un LoRA de style pour tenir A, B ou C. Sur **D**, cette dérive est précisément la cible : le style demande déjà de l'ombrage adouci, de la profondeur de champ et du grain. **D pourrait donc tenir sans LoRA**, ce qu'aucun des styles existants ne peut prétendre. C'est un argument de coût et de délai, pas seulement de goût. **E** est dans la situation de A. **F** est un cas neuf, à mesurer.

## Étape 6 — montage et vérification par mesure

`analyse_montage.py`, une image par seconde plus transcription horodatée, puis un relecteur indépendant qui **reçoit le scénario exact** et dont chaque verdict se recontrôle sur la planche. Les deux règles issues du lot 8 s'appliquent sans exception.

---

# 7. Grille d'audit de l'épreuve

Les 13 contrôles de `METHODE-generation-images.md` §20 s'appliquent inchangés. S'y ajoutent cinq contrôles propres à ce test.

1. **Le style est il celui décrit, ou un style voisin déjà connu ?** E doit sortir avec trois ou quatre couleurs, des formes anguleuses et **pas de contour épais partout** ; s'il sort en aplats cernés de noir avec huit couleurs, c'est le style A et E n'existe pas. Même question pour I contre A : une ligne claire trop épaisse et trop colorée, c'est encore A.
2. **D, les deux registres se distinguent ils ?** Le P4b-1 en TENSION doit être lisiblement autre chose que le P02 en JOUR. Si les trois images D se ressemblent, le traitement de lumière ne prend pas et il faut le durcir.
3. **F et G, glissade vers le photoréalisme ?** En F : peau mate sans reflet spéculaire, trame du tissu visible, mâchoire facettée. En G : surfaces lisses et mates, aucun pore, aucun angle vif. Un seul visage à peau réaliste ou à reflet gras et l'image tombe.
4. **F contre G, les deux 3D se distinguent ils ?** C'est le seul couple du lot construit en opposition terme à terme, facettes anguleuses contre volumes ronds. Si les deux se ressemblent, l'un des deux est inutile et on économise un palier.
5. **H, les couleurs réservées.** Des lumières magenta et cyan sur des figurants au premier plan peuvent rejouer la RÈGLE 30. Contrôler qu'aucun figurant ne sort en sable, sarcelle vif ou orange vif, et que la couleur reste dans la lumière et non dans le tissu.
6. **I, la platitude.** Le P4b-1, le vide au dessus de Paris, est le plan où un style calme peut tomber à plat. S'il n'a aucune tension, I ne tiendra pas les plans 4 et 5.
7. **La foule.** Aucun visage lisible en E, F, G, H, I, comme en A et B. En D, silhouettes assombries hors mise au point.
8. **Lettrage.** Les bannières de P1a-3 sont le piège connu. Aplats ou motifs, jamais de lettres. Le style H y est le plus exposé, son idiome d'imprimé appelant naturellement du texte.

---

# 8. Budget

| Palier | Volume | Crédits |
|---|---|---|
| Étape 1, épreuve de style, 6 styles | 18 images | **38**, dépensés |
| Étape 2, épreuve de troupe, par style survivant | 4 images | **8** |
| Étape 3, mini bible, par style retenu | 3 images | **6** |
| Étape 4, pilote complet, par style retenu | 20 images | **40** |
| Étape 5, clips, par style retenu | 16 clips | 0 crédit, 1 à 2 $ de GPU |

L'étape 1 a coûté 38 crédits au lieu de 36 : un job resté bloqué en file d'attente, débité sans rien produire, a dû être resoumis.

* Si **trois** styles passent l'étape 2 et **deux** vont au bout : 38 + 24 + 92 = **154 crédits** et 2 à 4 $ de GPU.
* Si **quatre** passent l'étape 2 et **trois** vont au bout : 38 + 32 + 138 = **208 crédits** et 3 à 6 $ de GPU.

Solde Higgsfield après l'épreuve : **802 crédits**. Le test tient largement, et il reste de quoi produire l'épisode dans le style retenu, dont le plan de production chiffre les images clés à 506 crédits.

**La discipline qui protège ce budget** : ne jamais laisser plus de trois styles franchir l'étape 2. Six styles au pilote complet coûteraient 276 crédits et surtout six montages à comparer, ce qui est au delà de ce qu'un œil arbitre honnêtement en une passe. L'étape 1 est là pour éliminer, pas pour départager.

---

# 9. Ce qui reste à trancher

* **La troupe en D, F et I.** Si l'étape 2 confirme que Sam, SamBis, Naya et Elio ne se transposent pas, il faut décider s'ils sont **redessinés** pour ce style, ce qui refait les 40 assets de bible depuis le turnaround et rouvre un arbitrage de design, ou si le style est écarté pour cette raison seule.
* **La foule en D**, section 5.
* **Le LoRA de style.** Il n'a de sens que sur un style à aplats, donc sur E et sur I. Sur D, H, F et G, la dérive naturelle de Wan 2.2 va dans le sens du style, et l'étape 8 de la feuille de route du PIPELINE pourrait tomber, ce qui économise l'entraînement.
* **La cohérence entre le style et le public.** G vise 6 à 12 ans, H vise 12 à 20, I vise 30 à 40. Ces trois là ne se départagent pas au goût : ils se départagent en décidant d'abord **pour qui** la série est faite. Cette décision précède le choix du style et ne se déduit d'aucune image.
* **Le sort de A et B.** Ils restent en course et ne sont pas régénérés ; leurs 40 images clés et leurs montages servent de point de comparaison.
