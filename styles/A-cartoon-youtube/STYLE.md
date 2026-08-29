# Style A — Cartoon YouTube

**Famille** : aplats, contour épais. **Registre visé** : tout public, lisible, plat. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : pilote complet (20 clés, 16 clips, montage v7 en LTX-2.5) ; troupe complète (turnarounds, références, poses, têtes).

**Verdict** : Troisième de la shortlist du 25 août 2026. Irréprochable sur la grille de contrôle et pauvre à l'écran : aucune profondeur atmosphérique, les plans larges se lisent comme un plateau de jeu, le vide de mille mètres du plan 4b-1 ne donne pas le vertige. Son avantage était l'avance de production, pas le rendu.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:
```

### Bloc de style, version personnage de la troupe (planches sur fond neutre)

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, bright saturated colors, flat cel shading with a single hard edged shadow tone, absolutely no photorealism, on a plain flat light grey background:
```

### Bloc de style, version personnage d'époque

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period character in desaturated muted earth tones, era accurate costume, absolutely no photorealism, on a plain flat light grey background:
```

### Traitement d'époque

```
historical period setting in desaturated muted earth tones, dusty beige, stone grey, earth brown, softened contrast, era accurate architecture and props,
```

### Base négative du style

```
gradient shading, soft shading, airbrush, painterly, thin delicate linework, photorealism, photograph, realistic skin texture, 3D render, CGI, live action, anime style, manga, corporate flat vector art, extra characters.
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
flat 2D cartoon animation, bold clean outlines, flat cel shading, muted earth tones, limited animation, 16:9 frame:
```

---

## Ce que ce style a appris

* RÈGLE 30 : sur ce style, les couleurs réservées reviennent sur les figurants en plan rapproché dès qu'elles ne sont pas nommées en positif (4a-2 : deux tirages sur deux en orange vif, sarcelle et sable).
* RÈGLE 28 : sur un très gros plan, le code de décor « D2 » a été écrit en toutes lettres dans l'image (5-2, 5-3) ; le code se développe toujours en clair.
* Le bloc de style vidéo se réduit à la facture (ligne `clip`) : le bloc complet, qui décrit des personnages, en fait apparaître dans les plans vides.

Le style d'origine du projet, sur lequel les 42 règles de la méthode ont été apprises. Le plus robuste des trois premiers styles.

---

## Exemples

Dans `exemples/` : `Alchimistes-propre_StyleA.png`, `Alchimistes-suie_StyleA.png`, `Charretier_StyleA.png`, `D01_StyleA.png`, `D02_StyleA.png`, `ELIO-gel_StyleA.png`, `Fermiers_StyleA.png`, `Foule_StyleA.png`, `Garnerin_StyleA.png`, `Huaibing_StyleA.png`, `INS-sacoche-givre_StyleA.png`, `INS-sacoche_StyleA.png`, `KITE-hibou_StyleA.png`, `Lenormand_StyleA.png`, `P02_StyleA.png`, `P1a-3_StyleA.png`, `P4b-1_StyleA.png`, `Parieurs_StyleA.png`, `Pilleurs_StyleA.png`, `Porteurs_StyleA.png`, `YuanHuangtou_StyleA.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

Dans `exemples/troupe/` : les turnarounds et les références de production de la troupe *Il était une fois* (Sam, Sam Bis, Naya, Elio) dans ce style — `Elio_StyleA_turnaround.png`, `Naya_StyleA_turnaround.png`, `REF_Elio_StyleA.png`, `REF_Naya_StyleA.png`, `REF_SamBis_StyleA.png`, `REF_Sam_StyleA.png`, `SamBis_StyleA_turnaround.png`, `Sam_StyleA_turnaround.png`.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
