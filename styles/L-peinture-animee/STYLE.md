# Style L — Peinture animée hybride

**Famille** : 3D finie à la peinture visible. **Registre visé** : 15 à 30 ans, « maintenant ». **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 25 août (3 images, à sec).

**Verdict** : Le langage dominant de l'animation des années 2020 — volumes mis en scène en trois dimensions puis finis à la peinture visible. Non retenu à la shortlist du 25 août : sa texture de support (touche de pinceau, grain de toile) est un marqueur d'image fixe qui grouille en mouvement.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
hybrid painted animation, three dimensional staged forms finished with visible hand painted brush texture on every surface, thick expressive paint strokes catching the light, bold graphic silhouettes, desaturated smoky base palette pierced by one or two saturated accent colours carried by the lighting only, hard rim light along the silhouettes, deep shadow, cinematic wide staging with strong depth, subtle canvas grain in the paint, painterly and deliberate, never a clean digital gradient, 16:9 frame:
```

### Traitement d'époque

```
era accurate 1797 Directoire France, period costume in muted earth tones with worn fabric, period architecture and props,
```

### Base négative du style

```
clean digital gradients, smooth airbrush, flat vector art, cel shading with uniform fills, photorealism, photograph, live action, video game screenshot, chibi proportions, cute mascot design, muddy colours, low contrast, anime, manga, extra characters.
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

Bloc récupéré le 27 août 2026 sur la génération Higgsfield `6ed44703…`.

---

## Exemples

Dans `exemples/` : `P02_StyleL.png`, `P1a-3_StyleL.png`, `P4b-1_StyleL.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
