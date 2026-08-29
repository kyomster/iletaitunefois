# Style F — 3D stylisé facetté mat

**Famille** : 3D, marionnette. **Registre visé** : marionnette, matière. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août (3 images) — images non versionnées.

**Verdict** : Écarté : le plus faible des six. Son identité n'existe que là où il y a des personnages ; les plans sans figure sont des rendus 3D quelconques. Bandes noires incrustées sur deux images sur trois (RÈGLE 35), hangars en bois inventés dans Parc Monceau.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
stylized 3D computer animation, characters carved from angular faceted planes with a strong squared jaw and sharp cheekbones, matte non reflective surfaces everywhere, visible woven cloth texture and hand painted texture on every material, skin rendered as matte painted surface with a slight dry brush grain and no specular sheen, cinematic three point lighting with soft shadows, moderate depth of field, physically staged sets with real volume and fine dust in the air, deliberately non photorealistic, the look of an animated puppet rather than a person, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, muted earth toned costumes with visible fabric weave, period architecture built as real volumes with weathered surfaces,
```

### Base négative du style

```
photorealism, photograph, live action, realistic human skin, subsurface scattering, glossy specular highlights, plastic sheen, wax figure, uncanny realistic face, video game screenshot, 2D drawing, flat cel shading, anime, manga, extra characters.
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

* Risque propre : la glissade vers le photoréalisme, le modèle ayant vu bien plus de 3D photo que de 3D stylisé mat.

Contre-pied exact de G : même technique, parti pris de forme opposé.

---

## Exemples

Aucune image versionnée pour ce style : les trois images d'épreuve du 23 août 2026 n'ont pas été rapatriées dans le dépôt. Le bloc ci-dessus suffit à les refaire (2 crédits chacune).

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
