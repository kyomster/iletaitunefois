# Style B — Inkman

**Famille** : bonshommes bâton à tête ronde, décor peint. **Registre visé** : graphique, humour, adulte. **Variante de bloc identité** : `B` (voir `atelier/scripts/assembler_prompts.py`).

**État** : pilote complet (20 clés, 16 clips, montage v7) ; troupe complète.

**Verdict** : Resté en course jusqu'au montage v7. Le plus robuste des styles sur la foule (têtes vierges sans exception). Un relecteur extérieur a lu ses trois traitements de visage — foule vierge, parieurs en « rage comic », Garnerin rond — comme une incohérence ; c'est le parti pris de la fiche, mais c'est un signal. Écarté par le choix de P le 27 août 2026.

---

## Les blocs, mot pour mot

Ils se copient octet pour octet et ne se reformulent jamais (RÈGLE 13). Un style ne se réécrit pas de mémoire : il se relit sur la génération qui a été validée.

### Bloc de style, version plan de scène

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:
```

### Bloc de style, version personnage de la troupe (planches sur fond neutre)

```
inkman stick figure cartoon style, large round white head with bold black ink outline, simple dot eyes and expressive mouth, thin black stick limbs, flat graphic character design, hand drawn ink sketch feel with slightly wobbly brush lines, on a plain flat warm cream background:
```

### Bloc de style, version personnage d'époque

```
inkman stick figure cartoon style, large round white head with bold black ink outline, simple dot eyes and expressive mouth, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costume in muted earth tones, on a plain flat light neutral background:
```

### Traitement d'époque

```
era accurate historical setting, moody atmospheric period palette,
```

### Base négative du style

```
plain round ball hands, hollow circle hands, teardrop hands, pointed armless stumps, separate fingers, realistic hands, missing hand, missing arm, realistic human anatomy, detailed face, nose, photorealism, 3D render, anime, manga, extra inkman characters.
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
flat graphic 2D cartoon animation on a richly painted atmospheric background, textured light, muted earth tones, limited animation, 16:9 frame:
```

---

## Ce que ce style a appris

* RÈGLE 16 : la règle des moufles — toute main est une moufle noire arrondie avec un petit pouce, formulation positive obligatoire doublée de la négative complète. Le pouce n'a jamais tenu sur le pilote (réserve acceptée).
* RÈGLE 20 : une main qui touche un objet mange son bras.
* Le bloc de style vidéo DOIT être réduit à la facture : avec le bloc complet, Wan 2.2 fabriquait des têtes d'inkman partout (12 clips sur 16 inutilisables, 12 sur 12 propres avec le bloc réduit).
* Les bouches inkman se dessinent en trait, pas en point (P03 v4).

Bloc de style « en scène » distinct pour les plans avec décor : `inkman stick figure cartoon character in a richly illustrated scene, the character drawn flat and graphic with bold black ink, the background painted with atmospheric depth and dramatic lighting`.

---

## Exemples

Dans `exemples/` : `Alchimistes-propre_StyleB.png`, `Alchimistes-suie_StyleB.png`, `Charretier_StyleB.png`, `D01_StyleB.png`, `D02_StyleB.png`, `ELIO-gel_StyleB.png`, `Fermiers_StyleB.png`, `Foule_StyleB.png`, `Garnerin_StyleB.png`, `Huaibing_StyleB.png`, `INS-sacoche-givre_StyleB.png`, `INS-sacoche_StyleB.png`, `KITE-hibou_StyleB.png`, `Lenormand_StyleB.png`, `P02_StyleB.png`, `P1a-3_StyleB.png`, `P4b-1_StyleB.png`, `Parieurs_StyleB.png`, `Pilleurs_StyleB.png`, `Porteurs_StyleB.png`, `YuanHuangtou_StyleB.png`.

Les images `P02`, `P1a-3` et `P4b-1` sont les trois plans d'épreuve communs à tous les styles (un dialogue à deux au sol, une contre-plongée sur le ballon, une plongée sur Paris) ; `D01` et `D02` sont les plaques de décor, `Foule`, `Garnerin` et `Parieurs` les planches de personnages du pilote.

Dans `exemples/troupe/` : les turnarounds et les références de production de la troupe *Il était une fois* (Sam, Sam Bis, Naya, Elio) dans ce style — `Elio_StyleB_turnaround.png`, `Naya_StyleB_turnaround.png`, `REF_Elio_StyleB.png`, `REF_Naya_StyleB.png`, `REF_SamBis_StyleB.png`, `REF_Sam_StyleB.png`, `SamBis_StyleB_turnaround.png`, `Sam_StyleB_turnaround.png`.

---

## Comment réutiliser ce style pour une autre série

1. Copier `style.json` tel quel ; ne toucher ni au bloc de scène, ni à la négative, ni au traitement d'époque sans repasser une épreuve.
2. Générer d'abord les trois plans d'épreuve de la nouvelle série (un dialogue, un plan large, un plan de vertige ou d'action), à sec, sans référence.
3. Contrôler avec la grille de `atelier/METHODE-generation-images.md` §20, puis constituer les planches de référence de la série (RÈGLE 36).
4. Vérifier la variante de bloc identité : `AC` pour un style dessiné, `B` pour l'inkman, `JK` pour un rendu réaliste (matériau plutôt que teinte), `P` pour un style à aplats (têtes de dos, carnation nommée).
