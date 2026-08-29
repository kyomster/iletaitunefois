# Style O — 3D à ombrage toon dur

**Famille** : 3D, cel shading deux tons, contour net. **Registre visé** : long métrage moderne. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 25 août (3 images, à sec).

**Verdict** : Second de la shortlist du 25 août, derrière P. Le plus cinématographique des trois : volumes sculptés à ombrage dur, profondeur réelle, `P4b-1` excellent. Deux dérives corrigibles : l'heure écrasée par la lumière (crépuscule bleu au lieu de l'aube) et deux fanions sortis en sarcelle et orange vif (couleurs réservées, RÈGLE 34). Sa modernité tient à la cadence, que seule la vidéo montre — jamais rendu en clip.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
3D animated feature look with hard toon shading, sculpted volumes rendered with crisp two step cel shading and a clean dark contour line, appealing stylised character design with believable proportions, deliberate graphic silhouettes, strong key light and a coloured bounce, deep saturated shadow, clean matte surfaces with no photographic texture, staged like a modern animated feature with clear depth, 16:9 frame:
```

### Traitement d'époque

```
era accurate 1797 Directoire France, period costume in muted earth tones with visible fabric weave, period architecture and props,
```

### Base négative du style

```
paper grain, canvas texture, halftone dots, visible brush strokes, print texture, film grain, soft airbrush gradient, photorealism, photograph, live action, realistic skin pores, video game screenshot, chibi proportions, extra characters.
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

* Traitement de lumière à amputer de sa clause d'heure, comme D le 23 août.

Bloc récupéré le 27 août 2026 sur la génération Higgsfield `e388b372…`.

---

## Exemples

Dans `exemples/` : `P02_StyleO.png`, `P1a-3_StyleO.png`, `P4b-1_StyleO.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
