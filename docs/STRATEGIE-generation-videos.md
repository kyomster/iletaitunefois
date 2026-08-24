# Stratégie de génération des vidéos — ce qui est retenu au 24 août 2026

Ce document fige ce que les essais E1 à E8 (22‑23 août 2026, `S01E01-pilote-audit.md`) ont établi. C'est la chaîne à appliquer
au pilote (montage v7) puis à l'épisode. Les décisions datées sont dans `DECISIONS-pilote.md` ; l'état de l'art détaillé dans
`ETAT-DE-L-ART-dialogue-video.md`.

## 1. Le moteur : LTX‑2.5 partout, voix libres

* **LTX‑2.5** (Lightricks, 22B distillé int8, dépôt HF *gated* → jeton `HUGGING_FACE` du `.env`) rend **tous** les plans :
  muets ET dialogues. Choisi contre Wan 2.2 (bouches non tenables, figurants surgis, LoRA qui fige — E7 : LTX propre sur les
  12 plans muets difficiles), contre InfiniteTalk (abandonné par Guillaume après E1/E1b), contre MiniMax H3 (très bon style et
  créativité mais hallucine sur les plans muets — tête géante, débris — et réécrit parfois les répliques ; reste le second choix
  pour un plan de dialogue qu'on veut plus « joué »).
* **Voix libres** : les voix des dialogues sont **générées par LTX‑2.5 avec l'image** (décision Guillaume du 24 août). Raisons :
  l'intonation suit l'action et la voix est **dans l'acoustique de la scène** (extérieur, foule, distance), là où une piste
  ElevenLabs sonne « studio » et devrait être retraitée au montage. Les mp3 ElevenLabs restent la **référence de timbre** des
  personnages ; la tenue d'une même voix sur tout un épisode se traitera par ID‑LoRA/`LTXVReferenceAudio` (une voix par rendu)
  ou par sélection de graines — à trancher à la production de l'épisode.
* Solutions de repli connues et validées : **IA2V « audio gelé »** (E8 : la piste ElevenLabs passe telle quelle et les lèvres
  suivent — `LTXVAudioVAEEncode → SetLatentNoiseMask(SolidMask 0) → LTXVConcatAVLatent` dans les deux passes, euler, CFG 1/1) si
  un jour il faut des voix verrouillées ; **H3** au format du skill officiel pour un plan qu'on veut plus vivant.

## 2. Le graphe LTX‑2.5 (API ComfyUI)

`docs/scripts/run_ltx25_runpod.py` (muets et dialogues voix libres) et `run_ltx_voix_runpod.py` (variantes IA2V gelé / ID‑LoRA).
Deux passes du template officiel : demi‑résolution 9 sigmas (`1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0`),
upsampler latent ×2, seconde passe 4 sigmas (`0.85, 0.7250, 0.4219, 0.0`), `LTXVDualCFGGuider` cfg vidéo 1 / audio 1,
euler_ancestral (muets) ou euler (audio gelé), VAE audio du modèle, `CreateVideo` 24 i/s. Clés d'image en **1280×704** (multiples
de 32), longueurs en **8n+1** images. Modèles : transformer int8 (21,5 Go), gemma4‑12b int8 (15,4 Go), 2 VAE, upsampler spatial
(dossier HF `latent_upscale_models/`). Bootstrap type : `docs/runpod/bootstrap_pod_essais_E8.sh`.

## 3. Les règles de prompt vidéo (apprises, mesurées)

1. **Prompt court** (25‑80 mots utiles) : style en une ligne, action concrète avec vitesse et direction, caméra explicite
   (« static camera » compte), consigne de présence (« nobody enters the frame », « no person anywhere »), ambiance sonore
   demandée en clair (« Ambient sound only: wind and distant murmur, no speech, no music » pour un plan muet).
2. **Négative anti‑anachronisme systématique** : `car, cars, vehicle, carriage, modern object, anachronism, extra people, new
   characters, camera cut, scene change` (la voiture de P03 A sous Wan 2.1 et les coupes LTX l'ont payée).
3. **Piège connu : LTX‑2.5 insère une coupe vers 5‑6 s** sur un plan de dialogue (multishot natif, 4 rendus sur 5 sur P02).
   Parades : une seule phrase d'action continue (pas de « puis… puis… » séquencés), négative `camera cut, scene change`,
   ou couper le plan en deux rendus. À vérifier à l'image sur chaque plan parlé.
4. **L'image clé décrit un état de repos** (RÈGLE 31) : bouches fermées sur les clés de dialogue, l'action est dans le prompt vidéo.
5. **L'action de la clé porte la réplique** (corollaire METHODE) : relire la réplique et demander « que fait‑il en le disant ? »
   avant de figer la clé (leçon P03 v4 : main sur la corde de largage, pas la soie tendue comme une couverture).
6. **Un prompt de dialogue CITE les répliques exactes entre guillemets** (langue + timbre : `says in French, grave voice: "…"`).
   Décrire la scène sans citer le texte fait inventer un charabia (payé sur les 10 premiers dialogues v7).
7. Les nombres et noms propres se jugent **à l'oreille**, pas à la transcription (scribe_v1 déforme « Dix francs »).

## 4. La vérification (non optionnelle)

Chaque montage passe par `docs/scripts/analyse_montage.py` (1 image/s + piste audio + transcription horodatée + ligne de temps)
puis une relecture indépendante (agent, **avec le scénario exact** — les erreurs de consigne fabriquent de faux défauts) ;
tout verdict d'agent se recontrôle sur les planches avant d'être rapporté. Avant de rendre les clips d'un style : contrôle des
18 clés contre le scénario (présence des personnages, intention, position cohérente avec l'action et l'environnement).

## 5. Ce que les autres moteurs ont donné (pour mémoire, chiffres du 23 août)

| Moteur | Verdict | Coût P02 8 s |
|---|---|---|
| LTX‑2.5 | **retenu** — propre, ~1 min/clip A100, audio d'ambiance natif | ~0,05 $ |
| MiniMax H3 (skill officiel, fr) | très bon dialogue, hallucine sur les muets | ~0,25 $ |
| InfiniteTalk (Wan 2.1) | abandonné (rendu jugé insuffisant) | ~0,5 $ |
| Wan 2.2 I2V | remplacé (bouches, figurants, LoRA qui fige) | ~0,03 $ |
| Veo 3.1 Lite / Wan 2.7 / Seedance Mini / Kling 3.0 (Higgsfield) | bons, voix générées propres (Wan 2.7 et Seedance : texte exact) ; pas de voix à nous | 12‑20 crédits |

## 6. Chaîne type d'une session de rendu

1. Pod RunPod SECURE (A100 80 Go de préférence ; `GPUS=` et `DISK_GB=200` sur `runpod_pilote.py create`), bootstrap LTX‑2.5 avec
   `HF_TOKEN`, ~40 min de téléchargements.
2. Clés 1280×704 + `jobs.json` (prompt court + négative), soumission `run_ltx25_runpod.py`, CSV renseigné **au lancement**.
3. Fetch, planches 1 i/s, `analyse_montage.py`, relecture, reprises ciblées (graine +1, prompt corrigé).
4. Montage (`montage_pilote.py`, 24 i/s), **pod terminé** dès le rapatriement, `list` vide vérifié, coûts au journal.

## 7. Amélioration à mettre en place (proposée par Guillaume, 24 août 2026) : le S3 RunPod

Chaque session recommence ~40 min de téléchargements de modèles sur le disque conteneur du pod. Les volumes réseau RunPod
exposent une **API compatible S3** (`s3api-<datacenter>.runpod.io`, clés `RUN_POD_S3_ACCESS_KEY`/`RUN_POD_S3_SECRET_KEY` du
`.env`) : on peut **téléverser les modèles sur le volume sans GPU allumé** (aws cli / boto3 depuis la machine locale, ou un
pod CPU), puis monter le volume sur `/workspace` et pointer `extra_model_paths.yaml` de ComfyUI dessus — bootstrap réduit à
l'installation de ComfyUI. Même chose dans l'autre sens : écrire les sorties sur le volume et les **rapatrier par S3 sans GPU**.
À faire avant la prochaine session de rendu : (1) agrandir ou recréer le volume (l'actuel `atelier-modeles`, EU-RO-1, est plein
à 77 %) ; (2) y déposer LTX‑2.5 (~55 Go) par S3 ; (3) adapter le bootstrap pour lier `/workspace/models` au lieu de télécharger.
Limite connue : l'API S3 RunPod n'existe que dans certains datacenters (EU-RO-1 en fait partie) et le débit d'upload depuis la
machine locale devient le facteur limitant pour les gros fichiers.
