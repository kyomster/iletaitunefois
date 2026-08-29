# Style E — 2D graphique angulaire

**Famille** : aplats sans contour, formes anguleuses. **Registre visé** : affiche, graphique. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août (3 images) — images non versionnées dans le dépôt.

**Verdict** : Quatrième sur six. Identité graphique la plus forte du lot, palette tenue à quatre couleurs, foule exemplaire. Mais les visages réduits à une ligne fermée et une entaille ne porteront pas l'expression sur 79 plans et quatorze gags. Gardé en réserve sous condition d'une épreuve d'expression (les six têtes de la bible).

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
hand drawn 2D animation in a bold graphic poster style, strongly angular geometric character design built from sharp straight edged planes and decisive silhouettes, faces reduced to a few deliberate shapes with minimal interior detail, no outline on most colour areas and a thin dark accent line only where two shapes must be separated, flat colour fills with one hard edged shadow shape and no blending, dramatic high contrast lighting, restrained palette of three or four colours in the whole image, wide horizontal staging with large areas of empty space, background painted in flat gouache washes with visible dry brush texture, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, restrained palette of dusty ochre, stone grey and deep ink blue, period architecture reduced to flat geometric masses,
```

### Base négative du style

```
thick uniform outline around every shape, rounded soft character design, gradient shading, soft shading, airbrush, painterly rendering, cluttered background, busy small detail, many colours, photorealism, photograph, 3D render, CGI, live action, anime, manga, extra characters.
```

À laquelle s'ajoutent toujours la base personnages d'époque et la négative universelle :

```
dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing
```
```
text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin
```

### Bloc de style vidéo

Jamais rendu en clip : à écrire, réduit à la facture, le jour où le style passe en vidéo.

---

## Ce que ce style a appris

* Contrôle décisif à l'audit : si les images sortent avec un contour noir épais partout et huit couleurs, ce n'est pas E, c'est A.

Le plus proche parent de A : aplats, ombre d'un seul tenant, aucun dégradé ; en diffère par l'angularité, l'absence de contour et la palette bornée.

---

## Exemples

Aucune image versionnée pour ce style : les trois images d'épreuve du 23 août 2026 n'ont pas été rapatriées dans le dépôt. Le bloc ci-dessus suffit à les refaire (2 crédits chacune).

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
