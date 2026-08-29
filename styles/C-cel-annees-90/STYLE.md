# Style C — Cel animation années 90

**Famille** : cel deux tons, contour pinceau. **Registre visé** : aventure, série télé classique. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : pilote : 18 clés et 16 clips Wan 2.2 (22 août 2026) ; troupe complète.

**Verdict** : Retiré des choix le 22 août 2026 par Guillaume, au visionnage des premiers montages : il ne se distingue de A que sur les plans rapprochés. C'est aussi le style qui a le plus mal tenu sa charte sur la troupe : aucune planche n'appliquait les deux tons à bords durs, et la palette a éclaté en trois (Sam ambre, Sam Bis violet, Naya sarcelle).

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:
```

### Bloc de style, version personnage de la troupe (planches sur fond neutre)

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, warm saturated palette of amber ochre and burnt orange with deep teal blue shadows, crisp and graphic not painterly, on a plain flat light warm background:
```

### Bloc de style, version personnage d'époque

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period character with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costume, crisp and graphic not painterly, on a plain flat light warm background:
```

### Traitement d'époque

```
era accurate historical setting, palette shifted toward muted earth tones while keeping deep teal shadows,
```

### Base négative du style

```
gradient shading, soft shading, airbrush, painterly, rendered highlights, digital painting, muddy colors, cold blue palette, violet palette, purple palette, photorealism, photograph, 3D render, CGI, live action, anime, manga, flat vector art, extra characters.
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
hand drawn 2D cel animation, crisp ink outlines, flat two tone cel shading, amber and teal palette, limited animation, 16:9 frame:
```

---

## Ce que ce style a appris

* RÈGLE 15 : le style C ne tient pas sa palette sur un personnage en pied sur fond neutre ; il la tient sur un plan de scène dès qu'une plaque C est réinjectée.
* Pour Sam et Sam Bis, `appealing shape driven character design` devient `strongly angular shape driven character design`.
* `Sam_StyleC_turnaround` est la seule planche C qui tenait la palette : c'est la référence de charte.

Résultat négatif documenté, à ne pas repayer : voir RÈGLE 15.

---

## Exemples

Dans `exemples/` : `Alchimistes-propre_StyleC.png`, `Alchimistes-suie_StyleC.png`, `Charretier_StyleC.png`, `D01_StyleC.png`, `D02_StyleC.png`, `ELIO-gel_StyleC.png`, `Fermiers_StyleC.png`, `Foule_StyleC.png`, `Garnerin_StyleC.png`, `Huaibing_StyleC.png`, `INS-sacoche-givre_StyleC.png`, `INS-sacoche_StyleC.png`, `KITE-hibou_StyleC.png`, `Lenormand_StyleC.png`, `P02_StyleC.png`, `P1a-3_StyleC.png`, `P4b-1_StyleC.png`, `Parieurs_StyleC.png`, `Pilleurs_StyleC.png`, `Porteurs_StyleC.png`, `YuanHuangtou_StyleC.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

Dans `exemples/troupe/` : les turnarounds et les références de production de la troupe *Il était une fois* (Sam, Sam Bis, Naya, Elio) dans ce style — `Elio_StyleC_turnaround.png`, `Naya_StyleC_turnaround.png`, `REF_Elio_StyleC.png`, `REF_Naya_StyleC.png`, `REF_SamBis_StyleC.png`, `REF_Sam_StyleC.png`, `SamBis_StyleC_turnaround.png`, `Sam_StyleC_turnaround.png`.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
