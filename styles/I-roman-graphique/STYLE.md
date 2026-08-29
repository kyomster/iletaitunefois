# Style I — Roman graphique européen

**Famille** : ligne claire, gouache, grain de papier. **Registre visé** : 30 à 40 ans, documentaire, retenu. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août (3 images) — images non versionnées.

**Verdict** : Second sur six, quatrième sur cinq après J et K. Meilleur Paris en 2D, tenue documentaire, sert le registre CADRE. Deux défauts : un cadre dessiné avec marge crème (à supprimer en positif, `the drawing bleeds to all four edges of the frame`) et une fidélité faible à la fiche des parieurs. Impose un redessin de la troupe en proportions naturalistes.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
hand drawn 2D illustration in a European graphic novel manner, restrained clear line drawing with an even thin ink contour, colour laid in flat gouache with visible paper grain and slight brush irregularity, naturalistic adult proportions and understated faces without any cartoon exaggeration, muted sophisticated palette of ochre, slate, olive and faded brick, quiet even lighting with soft ambient shadow rather than dramatic contrast, calm horizontal composition with generous air, restrained and literary rather than spectacular, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, carefully observed period costume and architecture, documentary accuracy in the detail,
```

### Base négative du style

```
cartoon exaggeration, oversized eyes, chibi proportions, thick uneven outline, glossy digital rendering, airbrush, neon colours, oversaturation, dramatic rim light, photorealism, photograph, 3D render, CGI, live action, anime, manga, extra characters.
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

* Porte un grain de papier : marqueur d'image fixe, voir H.

Si la série vise les 30 à 40 ans, I passe premier.

---

## Exemples

Aucune image versionnée pour ce style : les trois images d'épreuve du 23 août 2026 n'ont pas été rapatriées dans le dépôt. Le bloc ci-dessus suffit à les refaire (2 crédits chacune).

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
