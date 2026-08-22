# Il était une fois — *Les Découvreurs*

Dépôt de production de la série animée. Il contient les images validées de l'épisode S01E01 et les documents qui permettent de les reproduire.

```
assets/
  bible/                   la troupe récurrente, 132 images
    turnarounds/    12     quatre vues, référence de DESIGN
    references/     12     personnage seul de face, référence de PRODUCTION
    poses/          24     portrait cadre et plein pied aventure
    tetes/          72     six expressions par personnage et par style
    expressions/    12     planches 3 x 2 assemblées en local
  S01E01/                  l'épisode, 187 images
    decors/StyleA|B|C/     46 plaques par style
    personnages-episode/StyleA|B|C/   12 fiches par style
    assets-partages/ 13    inserts, props et gravure

  S01E01/pilote/images/Style*/  54   les images clés du pilote, plans 1 à 6, validées le 22 août 2026

docs/
  DECISIONS-pilote.md                 les arbitrages du pilote, datés, avec leurs raisons
  S01E01-pilote-audit.md              l'audit des 54 images et des 48 clips, lot par lot
  ETAT-DE-L-ART-dialogue-video.md     recherche du 23 août 2026 : limites de Wan 2.2 sur les dialogues, MultiTalk/InfiniteTalk, LTX-2.5, essais proposés
  S01E01-pilote-job-ids.md            media_id des références, job_id des images, prompt_id des clips
  scripts/                            build_prompts_pilote.py, build_clips_pilote.py, run_clips_runpod.py, runpod_pilote.py, montage_pilote.py, chain_dialogue_runpod.py, run_s2v_runpod.py, align_dialogue_audio.py (obsolète), analyse_montage.py
  runpod/                             les graphes ComfyUI (format API) I2V et FLF2V tels qu'exécutés
  S01E01-scenario.md                  les 79 plans, le minutage, les 14 gags
  S01E01-plan-de-production.md        diagnostic, roster, tableau révisé, prompts du pilote
  PIPELINE-video-et-voix.md           rendu ComfyUI sur RunPod, voix ElevenLabs, montage, budget
  S01E01-pilote-prompts-3-styles.md   les 18 images et 16 clips du pilote, dans les trois styles
  RUNPOD-COMFYUI-mode-d-emploi.md     du pod vide aux 48 clips rendus
  RUNBOOK-pilote-pour-claude-code.md  le pilote, à dérouler pas à pas par un agent
  PLAN-pilote-execution.md            la répartition du travail et le budget
  METHODE-generation-images.md        les 24 règles. À lire avant toute génération.
  S01E01-index-assets-et-fichiers.md  ce que contient chaque dossier, et le nommage
  PROMPT-MAITRE-chaine-production.md  d'une fiche épisode à la chaîne complète
  BIBLE-modernisation-v5.1.md         la méthode d'écriture et de fabrication
  prompts/                            les prompts eux mêmes, sans lesquels on ne régénère rien
```

## Par où commencer

* **Pour savoir ce qu'on tourne** : `docs/S01E01-scenario.md`, puis `docs/S01E01-plan-de-production.md`.
* **Pour comprendre ce qu'on a** : `docs/S01E01-index-assets-et-fichiers.md`.
* **Pour écrire un nouvel épisode** : `docs/PROMPT-MAITRE-chaine-production.md`, qui s'appuie sur `docs/BIBLE-modernisation-v5.1.md`.
* **Pour fabriquer les images** : `docs/METHODE-generation-images.md` d'abord, les fiches de `docs/prompts/` ensuite.
* **Pour fabriquer la vidéo et le son** : `docs/PIPELINE-video-et-voix.md`.
* **Pour lancer le pilote** : `docs/RUNBOOK-pilote-pour-claude-code.md`, à dérouler tel quel.

## Où vivent les choses

Le dépôt est la **source et la destination de l'information validée**. `C:\Users\kyoms\Downloads\EpisodeModernise` est le **répertoire de travail** : tout ce qui n'a pas encore été regardé y reste.

## Les trois règles qui coûtent le plus cher quand on les oublie

1. **La référence impose sa mise en page.** Le modèle ne copie pas seulement le personnage, il copie la disposition de l'image qu'on lui réinjecte. Aucune négative ne corrige ça.
2. **Une référence se regarde avant d'en dériver quoi que ce soit.** C'est un point d'arrêt, pas une recommandation. Quatre vingt seize images ont été produites sur des références fautives faute de l'avoir respecté.
3. **Les négatives agissent sur la présence d'un élément, jamais sur une structure, un nombre ou une mise en page.** Un défaut de structure se corrige en changeant la méthode de production, pas en allongeant la liste `Avoid:`.

## Nommage

`<Asset>_<Style>.png` partout, `Style` valant `StyleA`, `StyleB` ou `StyleC`. Le fichier au nom canonique est toujours la version validée la plus récente. Aucun suffixe de version ne subsiste dans le dépôt.

## Les trois styles

* **A** — cartoon YouTube, contours noirs épais, aplats cel.
* **B** — inkman, tête ronde blanche, deux yeux points, moufles noires pleines.
* **C** — cel années 1990, palette ambre ocre orange brûlé, ombres sarcelle.

Les couleurs réservées de la troupe ne dominent jamais un décor ni un personnage d'époque : **sable** pour Sam, **sarcelle vif** pour Naya, **orange vif** pour Elio.
