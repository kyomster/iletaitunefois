# Style K — 3D de long métrage, registre adulte

**Famille** : 3D stylisée, proportions crédibles. **Registre visé** : adulte, sobre. **Variante de bloc identité** : `JK` (voir `atelier/scripts/assembler_prompts.py`).

**État** : épreuve du 23 août, pilote complet (20 clés, 16 clips, montage v7).

**Verdict** : Premier sur cinq au classement révisé du 23 août : registre adulte sans quitter l'animation, distinguable de G et de J, troupe redessinable en bible. Réserve : sans personnage dans le cadre, penche vers le rendu de jeu vidéo haut de gamme. Écarté par le choix de P le 27 août 2026.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
stylized 3D feature animation, high end computer animated film look, believable human proportions with only a light touch of caricature in the features, soft subsurface skin with fine texture and no plastic sheen, individually groomed hair, real cloth simulation with visible weave and wear, naturalistic cinematography with motivated light and long lens compression, restrained desaturated colour grade, shallow depth of field, subtle volumetric atmosphere, an adult dramatic register rather than a comic one, stylized and not photographic, 16:9 frame:
```

### Traitement d'époque

```
era accurate 1797 Directoire France, authentic period costume in muted earth tones with real fabric weave and wear, period architecture and props,
```

### Traitements de lumière

Le registre dépend du BLOC du plan, jamais du tirage : plans au sol en JOUR, plans en l'air ou de tension en TENSION. L'heure appartient au décor ; le traitement ne règle que la qualité de la lumière.

**JOUR**

```
soft overcast daylight,
```

**TENSION**

```
hard directional key light with deep shadow across two thirds of every volume, desaturated grade pulled to cold grey and near black, high contrast, tight framing, no warm bounce light,
```

### Base négative du style

```
photograph, live action, real actors, broad cartoon caricature, chibi proportions, oversized head, rubbery squash and stretch, plastic sheen, waxy face, uncanny, saturated candy colours, 2D drawing, cel shading, anime, manga, modern buildings, glass towers, letterbox bars, black bars, extra characters.
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
stylized 3D feature animation, restrained desaturated grade, long lens, shallow depth of field, 16:9 frame:
```

---

## Ce que ce style a appris

* Corollaire de la RÈGLE 2 : « une douzaine de figurants en pied sur fond neutre » est une demande de grille déguisée ; K compose en deux rangées, deux fois sur deux. Nombre explicite et petit, ligne au sol prescrite, et surtout la zone vide prescrite en positif.
* RÈGLES 33, 34 et 35 s'appliquent comme sur J (foule durcie, matériau plutôt que teinte, bannières nues).

Contrôle décisif de son audit : s'il n'est distinguable ni de J ni de G, il n'existe pas. Il l'était.

---

## Exemples

Dans `exemples/` : `D01_StyleK.avant-rognage.png`, `D01_StyleK.png`, `D02_StyleK.png`, `Foule_StyleK.png`, `Garnerin_StyleK.png`, `P02_StyleK.png`, `P1a-3_StyleK.png`, `P4b-1_StyleK.png`, `Parieurs_StyleK.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
