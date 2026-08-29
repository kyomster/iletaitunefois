# Style N — Dessin 2D éclairé en volume

**Famille** : 2D plat, passe de lumière volumétrique. **Registre visé** : long métrage. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 25 août (3 images, à sec).

**Verdict** : Le pont entre A et D jamais testé avant : personnages dessinés à plat, puis passe de lumière volumétrique par-dessus. Non retenu à la shortlist du 25 août.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
hand drawn 2D characters lit in three dimensions, feature animation technique: flat drawn characters with clean ink lines and flat colour, over which a full volumetric lighting pass is applied — soft cast shadows wrapping the forms, warm bounce light, specular sheen on cloth and leather, believable falloff into darkness, painted background with real depth and aerial perspective, the drawing stays a drawing while the light behaves like cinema light, smooth clean surfaces, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, costumes in muted earth tones, period architecture and props,
```

### Base négative du style

```
paper grain, canvas texture, halftone dots, visible brush strokes, print texture, film grain, flat unlit look, photorealism, photograph, live action, video game screenshot, chibi proportions, thick uniform black outline, extra characters.
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

Bloc récupéré le 27 août 2026 sur la génération Higgsfield `06fac737…`.

---

## Exemples

Dans `exemples/` : `P02_StyleN.png`, `P1a-3_StyleN.png`, `P4b-1_StyleN.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
