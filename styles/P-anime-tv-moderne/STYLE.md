# Style P — Anime TV moderne

**Famille** : aplats à deux ou trois tons, contour constant, compositing de lumière. **Registre visé** : série animée télé, animation limitée, tout public. **Variante de bloc identité** : `P` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 25 août, pilote complet (18 clés, 18 clips LTX-2.5 voix libres, montage v7 corrigé jusqu'au 27 août) ; troupe à générer.

**Verdict** : **Retenu le 27 août 2026 par Guillaume pour *Il était une fois*.** Premier de la shortlist du 25 août : la lisibilité de A avec la profondeur de O, et le seul dont les trois images d'épreuve étaient utilisables en l'état. Natif animation, aucune texture de support, conçu pour la production de masse en animation limitée. La troupe s'y transpose sans redessin : Sam, Naya et Elio sont faits de grandes formes lisibles et de couleurs franches, ce qui est la grammaire même de cet idiome.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
modern anime television series look, clean black outlines of even weight, flat cel shading with exactly two or three tones per area and crisp hard shadow edges, appealing simple character shapes with clear expressive eyes and instantly readable silhouettes, bright clean saturated palette, digitally composited light: soft bloom around the highlights, smoothly graded sky, gentle light haze, background art painted more richly and in more detail than the characters, staged for limited animation with strong clear key poses, no surface texture of any kind, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, costumes in muted earth tones, period architecture and props,
```

### Base négative du style

```
paper grain, canvas texture, halftone dots, visible brush strokes, print texture, film grain, painterly rendering, gradient shading on the characters, soft airbrush, photorealism, photograph, 3D render, CGI, live action, chibi proportions, oversized anime eyes on adult characters, moe face, extra characters.
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
modern anime television series look, clean black outlines, flat cel shading with hard shadow edges, bright clean palette, soft bloom, richly painted background, muted earth tones.
```

---

## Ce que ce style a appris

* RÈGLE 37 : sur un style à aplats, demander « aucun trait de visage » se résout par le ton le plus sombre — les figurants sortent avec le visage noirci. On supprime la ZONE (têtes strictement de dos) au lieu des traits, on nomme la carnation en positif, la négative ne vise que le remplissage. Variante d'identité P.
* RÈGLE 33 élargie : les bannières sortent avec des ornements dorés même sur ce style non réaliste ; la clause de bannières nues s'applique à tous les styles.
* RÈGLE 15 durcie : le fond neutre d'une planche sort en ciel dégradé ; le fond gris uni se prescrit en positif (`ONE SINGLE FLAT UNIFORM GREY BACKGROUND`).
* Sur un plan où l'objet est lointain et petit, la référence ne suffit pas à tenir la couleur : on la nomme dans la scène elle-même (1a-2, 1b-1).
* Le nom « parachute » ramène sa forme la plus courante, le dôme ouvert : l'état replié se prescrit par la FORME et une négative dédiée (corollaire RÈGLE 42).

Une technique n'appartient à personne, un design appartient à quelqu'un : aucune marque, aucun titre de série, aucun nom d'auteur dans le bloc. Le bloc a été relu tel quel sur les trois générations d'épreuve validées, jamais réécrit de mémoire.

---

## Exemples

Dans `exemples/` : `Ballon_StyleP.png`, `D01_StyleP.png`, `Foule_StyleP.png`, `P02_StyleP.png`, `P1a-3_StyleP.png`, `P4b-1_StyleP.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
