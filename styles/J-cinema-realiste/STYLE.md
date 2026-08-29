# Style J — Cinéma réaliste 35 mm

**Famille** : photoréaliste, prise de vue réelle. **Registre visé** : film d'époque. **Variante de bloc identité** : `JK` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août, pilote complet (20 clés, 16 clips, montage v7).

**Verdict** : La meilleure image des 24 de l'épreuve (`P4b-1_StyleJ`) et la meilleure fidélité aux fiches. Mais J n'est pas un style d'animation, c'est l'abandon de l'animation : la bible de la troupe, le LoRA de style, l'essentiel des règles de la méthode et le registre CADRE tombent avec lui. Troisième sur cinq.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
live action cinema look, photographed on 35mm film, naturalistic period drama cinematography, real actors in accurate historical costume, motivated practical lighting with deep natural falloff, shallow depth of field with creamy bokeh, fine organic film grain, subtle halation on the highlights, desaturated filmic colour grade with rich blacks and warm skin tones, photorealistic, the image fills the entire 16:9 frame edge to edge, no black bars, 16:9 frame:
```

### Traitement d'époque

```
era accurate 1797 Directoire France, authentic period costume, real fabrics with wear and dirt, period architecture and props photographed on location,
```

### Traitements de lumière

Le registre dépend du BLOC du plan, jamais du tirage : plans au sol en JOUR, plans en l'air ou de tension en TENSION. L'heure appartient au décor ; le traitement ne règle que la qualité de la lumière.

**JOUR**

```
soft overcast daylight,
```

**TENSION**

```
hard directional key light with deep shadow across two thirds of the frame, desaturated grade pulled to cold grey and near black, high contrast, tight framing, long lens compression,
```

### Base négative du style

```
illustration, drawing, painting, cartoon, anime, manga, 3D render, CGI, video game, painterly, cel shading, ink outlines, plastic skin, waxy face, over sharpened, HDR, deformed hands, extra fingers, modern buildings, glass towers, letterbox bars, black bars, extra characters.
```

À laquelle s'ajoutent toujours la base personnages d'époque et la négative universelle :

```
dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing
```
```
text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin
```

### Bloc de style vidéo (prompt de mouvement)

Réduit à la facture, sans description de personnage : le bloc complet en fait apparaître dans les plans vides.

```
live action 35mm period film, naturalistic cinematography, shallow depth of field, film grain, no black bars, 16:9 frame:
```

---

## Ce que ce style a appris

* RÈGLE 33 : sur un rendu réaliste, un objet fait pour porter un signe en porte un malgré la négative universelle (bannières brodées) ; les bannières nues se prescrivent en positif.
* RÈGLE 34, corollaire : la couleur nommée en positif ne tient pas sur le photoréalisme (manteau du maigre bleu sarcelle sur P02, brun sur P02b) ; on décrit le MATÉRIAU et l'usure, jamais la teinte — variante d'identité JK.
* RÈGLE 35 : les bandes noires de cinéma sont une structure, pas un élément ; ni négative ni positif ne les enlèvent, on rogne en aval (`rogner_bandes_noires.py`).
* Corollaire de la RÈGLE 35 : un aérien photoréaliste de Paris ramène le Paris d'aujourd'hui (voitures, passage piéton) ; on interdit le SOL lui-même en positif.
* La foule doit être durcie en positif (`ALL SEEN FROM BEHIND, NO FIGURE FACING THE CAMERA`) : le flou d'arrière-plan seul n'y fait rien.

Seul style que la chaîne vidéo rend sans aucun effort de conformation. Mains : le risque annoncé ne s'est pas réalisé.

---

## Exemples

Dans `exemples/` : `D01_StyleJ.avant-rognage.png`, `D01_StyleJ.png`, `D02_StyleJ.avant-rognage.png`, `D02_StyleJ.png`, `Foule_StyleJ.png`, `Garnerin_StyleJ.png`, `P02_StyleJ.png`, `P1a-3_StyleJ.png`, `P4b-1_StyleJ.png`, `Parieurs_StyleJ.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
