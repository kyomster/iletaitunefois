# Style Db — Anime affûté (D sans grain ni aérographe)

**Famille** : anime, ombre à bord dur. **Registre visé** : adulte, contrasté. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 25 août (3 images, à sec, sans référence).

**Verdict** : Même dessin, même troupe, même identité que D ; seule la finition change — retiré le grain, l'aérographe, la brume et le pastel ; ajouté l'ombre à bord dur, les noirs riches, une seule couleur d'accent portée par la lumière. Question posée : ce qui date D est-il le dessin ou seulement son rendu ? Non retenu à la shortlist du 25 août (A, O, P).

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
2D anime illustration, contemporary cinematic anime style, crisp thin dark ink linework with confident weight variation, cel shaded characters with ONE hard edged shadow shape and one bright highlight, no airbrush softness anywhere, clean skin with strong colour separation, adult realistic body proportions and grounded facial features, sharp expressive eyes with a crisp specular highlight, graphic painted background with crisp edges and clearly separated planes, strong directional light, deep contrast with rich blacks, one saturated accent colour carried by the lighting only, shallow depth of field, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, costumes in muted earth tones, period architecture and props,
```

### Base négative du style

```
soft airbrush gradient, blended shading, film grain, hazy atmosphere, washed out pastel palette, muted low contrast, watercolour wash, flat vector art, thick uniform black outline, chibi proportions, oversized anime eyes on adult characters, moe face, photorealism, photograph, 3D render, CGI, live action, extra characters.
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

Bloc récupéré le 27 août 2026 sur la génération Higgsfield `c6cac08c…` : il n'avait jamais été versionné en texte.

---

## Exemples

Dans `exemples/` : `P02_StyleDb.png`, `P1a-3_StyleDb.png`, `P4b-1_StyleDb.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
