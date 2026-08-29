# Style H — 2D imprimé moderne

**Famille** : trames, texture d'impression, lumière colorée. **Registre visé** : 12 à 20 ans. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août (3 images) — images non versionnées.

**Verdict** : Cinquième sur six. Identité forte et vraiment moderne, compatible avec la contrainte d'époque (tissus sourds, couleur dans la lumière), mais non calibrée : palette qui dérive en violet et orange saturés, liseré chromatique trop appuyé. Deux réglages avant toute suite : décalage ramené à `a barely visible chromatic offset`, saturation limitée aux sources lumineuses.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
stylized 2D animation with a modern printed comic energy, confident brush inked linework of varying weight, painted colour with visible dry brush and canvas texture, halftone dot screens inside the shadows, a subtle chromatic offset along the edges as if the print were slightly misregistered, bold saturated palette with strong complementary rim lights in magenta and cyan against warm mid tones, dynamic diagonal staging with forced perspective, dramatic depth of field, graphic energy over realism, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, period costume and architecture kept accurate but pushed graphic and high contrast, muted earth tones in the fabrics with the saturated colour carried entirely by the light,
```

### Base négative du style

```
flat vector art, clean digital gradients, smooth airbrush, photorealism, photograph, 3D render, CGI, live action, chibi proportions, cute mascot design, muddy colours, low contrast, extra characters.
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

* Porte une texture de support (trame, grain de toile) : c'est un marqueur d'image fixe, qui grouille en mouvement. C'est ce constat qui a fait concevoir M, N et O.

Si la série vise les 12 à 20 ans, H remonte dans le classement ; cette décision ne se lit sur aucune image.

---

## Exemples

Aucune image versionnée pour ce style : les trois images d'épreuve du 23 août 2026 n'ont pas été rapatriées dans le dépôt. Le bloc ci-dessus suffit à les refaire (2 crédits chacune).

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
