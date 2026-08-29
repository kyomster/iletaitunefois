# Style D — Anime d'aventure moderne

**Famille** : anime cinématographique, ombrage adouci. **Registre visé** : adulte, cinématographique. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août (3 images), pilote complet (20 clés, 16 clips, montage v7).

**Verdict** : Troisième sur six à la première épreuve, cinquième sur cinq après l'arrivée de J et K. Deux registres de lumière prouvés distincts ; mais le traitement JOUR d'origine (`bright daylight, saturated blue sky with tall billowing cumulus clouds`) écrasait l'aube brumeuse du décor — corrigé le 23 août en amputant la clause de ciel : l'heure appartient au décor, le traitement ne règle que la qualité de la lumière. Impose un redessin complet de la troupe.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
2D anime illustration, modern cinematic adventure anime style, clean thin dark brown ink linework with subtle weight variation, cel shaded characters with a soft airbrush gradient blending each shadow into its base tone, warm natural skin with a faint blush on the cheeks, adult realistic body proportions and grounded facial features, expressive eyes with a single specular highlight, hand painted background with atmospheric depth and aerial perspective, volumetric light, shallow depth of field with the background softly out of focus, fine film grain, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, costumes in muted earth tones, period architecture and props,
```

### Traitements de lumière

Le registre dépend du BLOC du plan, jamais du tirage : plans au sol en JOUR, plans en l'air ou de tension en TENSION. L'heure appartient au décor ; le traitement ne règle que la qualité de la lumière.

**JOUR**

```
soft diffused key light, gentle contrast, clear readable midtones, luminous but restrained greens,
```

**TENSION**

```
hard directional key light, a single hard edged cast shadow shape across each face, palette pulled to warm amber or to near black, strong contrast, glowing rim light along the silhouette,
```

### Base négative du style

```
flat vector art, thick uniform black outline, corporate flat design, chibi proportions, super deformed, oversized anime eyes on adult characters, moe face, photorealism, photograph, 3D render, CGI, live action, extra characters.
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
2D anime animation, thin dark brown linework, soft cel shading, hand painted background, shallow depth of field, film grain, limited animation, 16:9 frame:
```

---

## Ce que ce style a appris

* Ce bloc INVERSE les négatives de A, B et C : ombrage adouci voulu, décor peint voulu, profondeur de champ voulue. Aucune négative des trois premiers styles ne se recycle sur D.
* Le registre de lumière (JOUR ou TENSION) dépend du BLOC du plan, jamais du tirage : plans au sol en JOUR, plans en l'air en TENSION.
* RÈGLE 28 confirmée sur le pilote D : « D2 » écrit en grosses lettres sur un second ballon (5-1).
* Clause de foule des styles A/B/C sûre sur D : la variante « silhouettes floues » n'a rien changé.

Dérivé affûté : Db.

---

## Exemples

Dans `exemples/` : `D01_StyleD.png`, `D02_StyleD.png`, `Foule_StyleD.png`, `Garnerin_StyleD.png`, `P02_StyleD.png`, `P1a-3_StyleD.png`, `P4b-1_StyleD.png`, `Parieurs_StyleD.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
