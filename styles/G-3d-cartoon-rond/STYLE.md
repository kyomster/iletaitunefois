# Style G — 3D cartoon à formes rondes

**Famille** : 3D, long métrage familial. **Registre visé** : chaleureux, familial. **Variante de bloc identité** : `AC` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août (3 images) — images non versionnées.

**Verdict** : Premier sur six à la première épreuve, second après l'arrivée de K. Seul style à rendre l'aube d'octobre, la brume et les rotondes de Parc Monceau dès la première image ; `P02_StyleG` était l'image la plus aboutie des dix-huit. Troupe transposable sans redessin. Point de vigilance : les clauses de lumière douce de son bloc adouciraient les plans de tension, d'où le traitement TENSION.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
stylized 3D cartoon animation, feature animation look, appealing rounded character design built from soft bouncy volumes with no sharp angles anywhere, large expressive eyes, generous head on a compact body, smooth clean surfaces with a soft matte finish, gentle rim light and warm bounce light, rich saturated colour, shallow depth of field, cinematic lighting with soft shadows, polished and playful, absolutely not photorealistic, 16:9 frame:
```

### Traitement d'époque

```
era accurate historical setting, costumes simplified into big readable shapes in muted earth tones, period architecture rounded and slightly caricatured,
```

### Traitements de lumière

Le registre dépend du BLOC du plan, jamais du tirage : plans au sol en JOUR, plans en l'air ou de tension en TENSION. L'heure appartient au décor ; le traitement ne règle que la qualité de la lumière.

**TENSION**

```
hard directional key light, deep shadow on two thirds of every volume, desaturated palette pulled to cold grey and near black, high contrast, tight framing, no warm bounce light
```

### Base négative du style

```
angular faceted character design, squared jaw, sharp cheekbones, hard edged planes, photorealism, photograph, live action, realistic human proportions, realistic skin pores, uncanny face, video game screenshot, 2D drawing, flat cel shading, anime, manga, extra characters.
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

* Un préjugé corrigé par l'épreuve : la forme ne fait pas le registre. Un personnage rond en contre-jour dur, cadré serré, en palette désaturée, porte le drame. Ce qui détermine le registre, ce sont la lumière, le cadrage et la palette.

G et K sont le même moteur à deux registres : K est G rendu adulte par la lumière, la focale et l'étalonnage.

---

## Exemples

Aucune image versionnée pour ce style : les trois images d'épreuve du 23 août 2026 n'ont pas été rapatriées dans le dépôt. Le bloc ci-dessus suffit à les refaire (2 crédits chacune).

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
