# S01E01 — index des assets et des fichiers

9 août 2026. **319 images actives**, toutes générées, rapatriées et regardées une par une.

Les chemins de ce document sont ceux du dépôt : les images sous `assets/`, les documents sous `docs/`.

---

# 1. Arborescence

```
assets/
  bible/
    turnarounds/     12   4 personnages x 3 styles, reference de DESIGN
    references/      12   4 personnages x 3 styles, reference de PRODUCTION
    poses/           24   2 poses x 4 personnages x 3 styles
    tetes/           72   6 expressions x 4 personnages x 3 styles
    expressions/     12   planches assemblees en local a partir des 72 tetes
  S01E01/
    decors/StyleA/            46
    decors/StyleB/            46
    decors/StyleC/            46
    personnages-episode/StyleA/  12
    personnages-episode/StyleB/  12
    personnages-episode/StyleC/  12
    assets-partages/          13

docs/
  S01E01-scenario.md
  S01E01-plan-de-production.md
  PIPELINE-video-et-voix.md
  S01E01-pilote-prompts-3-styles.md
  RUNPOD-COMFYUI-mode-d-emploi.md
  METHODE-generation-images.md
  S01E01-index-assets-et-fichiers.md
  PROMPT-MAITRE-chaine-production.md
  BIBLE-modernisation-v5.1.md
  prompts/
    fiche-prompts-troupe-recurrente.md
    fiche-prompts-personnages-episode-S01E01.md
    fiches-prompts-personnages-v3.md
    S01E01-assets-prompts-v3.4.md
```

**Convention de nommage, valable partout : `<Asset>_<Style>.png`**, avec `Style` valant `StyleA`, `StyleB` ou `StyleC`. Les anciens suffixes `_ref`, `_v2` à `_v5` ont tous été résorbés : le fichier au nom canonique est toujours la version validée la plus récente.

---

# 2. La bible, troupe récurrente

Quatre personnages : **Sam**, **SamBis**, **Naya**, **Elio**. Trois styles chacun.

| Dossier | Motif de nom | Rôle |
|---|---|---|
| `assets/bible/turnarounds` | `Sam_StyleA_turnaround.png` | quatre vues, référence de design, ne sert pas en production |
| `assets/bible/references` | `REF_Sam_StyleA.png` | personnage seul de face, **c'est elle qu'on réinjecte** |
| `assets/bible/poses` | `Sam_StyleA_portrait-cadre.png`, `Sam_StyleA_pleinpied-aventure.png` | les deux poses de travail |
| `assets/bible/tetes` | `TETE_Sam_StyleA_3-surprise.png` | une tête par expression, réutilisable seule |
| `assets/bible/expressions` | `EXPR_Sam_StyleA.png` | planche 3 x 2 assemblée en local |

Les six expressions, dans l'ordre des cases : **1 neutre, 2 joie, 3 surprise, 4 sceptique, 5 inquiétude, 6 rire.** Ligne du haut 1 2 3, ligne du bas 4 5 6.

Les douze planches n'ont **pas d'identifiant de job**, elles sont produites par programme à partir des six têtes correspondantes. Pour en refaire une, réassembler, voir la RÈGLE 24 de la méthode.

Distinction à ne pas confondre : le **turnaround** est la vérité du design, la **référence** est l'image de travail. On réinjecte toujours la référence, jamais le turnaround, sans quoi le modèle recopie la disposition à quatre vues.

---

# 3. Personnages d'époque, 12 par style

Même liste dans les trois styles, ce qui permet de comparer un même personnage d'un style à l'autre.

`Alchimistes-propre` · `Alchimistes-suie` · `Charretier` · `Fermiers` · `Foule` · `Garnerin` · `Huaibing` · `Lenormand` · `Parieurs` · `Pilleurs` · `Porteurs` · `YuanHuangtou`

Les paires **propre et suie** doivent être le même plan à la suie près. Elles se produisent en générant la version propre, puis en réinjectant celle ci pour la version suie, voir la RÈGLE 22.

---

# 4. Assets partagés, 13 fichiers

`ELIO-gel_Style{A,B,C}` · `INS-sacoche_Style{A,B,C}` · `INS-sacoche-givre_Style{A,B,C}` · `KITE-hibou_Style{A,B,C}` · `PLATE-laloubere` (indépendante des styles)

`PLATE-laloubere` est la seule image du projet où le lettrage est **voulu** : la négative anti texte doit y être levée.

---

# 4 bis. Pilote, plans 1 à 6 (22 août 2026)

`assets/S01E01/pilote/images/Style{A,B,C}/` — **18 images clés par style, 54 au total**, validées par Guillaume le 22 août 2026. Nommage `P<plan><bloc>-<clip>_Style<X>.png` (`P1a-3_StyleC.png`), plans FIXE `P02_StyleA.png`, `P03_StyleA.png`. 2752 × 1536, Nano Banana Pro, prompts dans `docs/prompts/S01E01-pilote-prompts-assembles.md`, identifiants dans `docs/S01E01-pilote-job-ids.md`.

Les **48 clips** (16 par style, Wan 2.2 I2V sur RunPod) ne sont pas dans le dépôt : mp4 et séquences PNG master restent dans `EpisodeModernise/pilote/clips-runpod/`, montages dans `pilote/montages/`. Leurs prompts, graines et `prompt_id` sont dans `docs/prompts/S01E01-pilote-clips-prompts.md` et `docs/S01E01-pilote-job-ids.md` ; les graphes ComfyUI dans `docs/runpod/`.

# 5. Décors, 46 par style

`D01` à `D33`, avec des variantes numérotées `v1` à `v4` et des insertions `i1`, `i2` sur certains plans, ce qui porte le total à 46 plaques par style. Nommage `D14v4_StyleB.png`.

Règles qui les gouvernent : plein cadre 16:9 sans bande ni panneau, aucune présence humaine sauf exception documentée, une valeur moyenne lisible au sol pour permettre l'incrustation d'un personnage, et aucune couleur réservée en dominante.

Les descriptions de scène des 33 décors, indépendantes du style, sont dans `docs/prompts/S01E01-assets-prompts-v3.4.md`, section 4.

---

# 6. Couleurs réservées

Elles appartiennent à la troupe et ne doivent jamais dominer un décor, un personnage d'époque ou un accessoire :

* **sable** : Sam
* **sarcelle vif** : Naya
* **orange vif** : Elio

---

# 7. Où trouver quoi

* **Comment générer sans refaire les erreurs** : `docs/METHODE-generation-images.md`, 35 règles, dont deux résultats négatifs à ne pas repayer, le style C sur personnage en pied et le pouce des moufles.
* **Ce qu'il faut tourner** : `docs/S01E01-scenario.md` pour les 79 plans et le minutage, `docs/S01E01-plan-de-production.md` pour le tableau révisé à huit colonnes, le roster d'assets et les prompts du pilote.
* **Comment lancer le pilote** : `docs/S01E01-pilote-prompts-3-styles.md` pour les prompts, `docs/RUNPOD-COMFYUI-mode-d-emploi.md` pour la machine.
* **Comment fabriquer la vidéo et le son** : `docs/PIPELINE-video-et-voix.md`, qui refait le diagnostic pour une chaîne ComfyUI sur RunPod et cadre la voix ElevenLabs.
* **Comment écrire un épisode** : `docs/PROMPT-MAITRE-chaine-production.md`, qui s'appuie sur `docs/BIBLE-modernisation-v5.1.md`.
* **Les prompts eux mêmes** : `docs/prompts/`. La fiche troupe donne les blocs identité et les chartes de style, la fiche personnages d'épisode donne les onze figures d'époque de S01E01, la fiche v3.4 donne les 33 décors et les assets partagés.

**Ce qui n'est pas dans ce dépôt** : les identifiants de jobs Higgsfield, les audits visuels et le suivi de production. Ils restent dans le projet claude.ai et dans le dossier de travail `EpisodeModernise`. Ils servent à retracer l'historique, pas à reproduire le résultat.

---

# 8. Ce qui reste ouvert

* ~~Alerte du plan 8~~ **tranchée le 22 août 2026** : la réplique devient « ...regardez ma sacoche : de la glace ! ». Le gag du givre passe à la sacoche. Report fait dans le scénario et dans le plan de production, plans 8 et 76 et liste des gags compris. Les plans 8a et 8b sont débloqués.
* **Les prompts s'arrêtent au plan 6**, et c'est voulu : le pilote de format se produit d'abord dans les trois styles, le style est choisi, puis les plans 7 à 79 sont rédigés dans ce seul style.
* Le style C ne se distingue du style A que sur les plans rapprochés. Décision prise de le garder tel quel sur les plans larges, documentée en RÈGLE 15.
