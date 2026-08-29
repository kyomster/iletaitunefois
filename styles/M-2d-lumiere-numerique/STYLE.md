# Style M — 2D de série moderne à lumière numérique

**Famille** : aplats, contre-jour coloré. **Registre visé** : streaming moderne. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 25 août (3 images, à sec).

**Verdict** : Conçu avec N et O comme style natif animation, sans aucune texture de support : dessin plat et graphique, mais contre-jour coloré, ombres teintées, halos — la texture est la couleur. Non retenu à la shortlist du 25 août.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
2D animated series look, modern streaming animation, flat graphic character drawing with clean confident linework and simple decorative shapes, flat colour fills with ONE crisp shadow shape, but lit digitally: coloured rim light along the silhouettes, tinted shadows, soft glow around light sources, decorative flat background shapes in layered planes, confident limited palette, everything drawn and coloured cleanly with no surface texture of any kind, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, costumes in muted earth tones, period architecture and props,
```

### Base négative du style

```
paper grain, canvas texture, halftone dots, visible brush strokes, print texture, film grain, painterly rendering, photorealism, photograph, 3D render, CGI, live action, chibi proportions, oversized anime eyes on adult characters, thick uniform black outline, extra characters.
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

* Rien de propre à ce style : les règles générales de `atelier/METHODE-generation-images.md` s'appliquent.

Bloc récupéré le 27 août 2026 sur la génération Higgsfield `6d62a7af…`.

---

## Exemples

Dans `exemples/` : `P02_StyleM.png`, `P1a-3_StyleM.png`, `P4b-1_StyleM.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
