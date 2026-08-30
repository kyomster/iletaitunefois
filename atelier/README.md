# Atelier — comment on fabrique les images et la vidéo

Tout ce qui est **indépendant de la série et du style** : la méthode d'images, la stratégie vidéo, le mode d'emploi RunPod, les scripts, et les moteurs essayés puis écartés. Une nouvelle série y puise sans rien réécrire ; ce qu'elle apporte de nouveau s'y consigne au moment où c'est acquis.

```
atelier/
  GUIDE-preparation-episode.md   la porte d'entrée : ce qu'on prépare AVANT de générer la première image, et la liste de contrôle
  METHODE-generation-images.md   les 42 règles d'images et leurs corollaires, toutes payées au moins une fois
  STRATEGIE-video.md             le moteur (LTX-2.5, voix libres), le graphe, les règles de prompt vidéo, le son, le montage, la vérification
  RUNPOD.md                      volume réseau et S3, pod, bootstrap, lots, pièges
  scripts/                       les outils, génériques : ils lisent styles/*/style.json et un module de briques de série
  runpod/                        les bootstraps de pod (LTX-2.5 sur volume ; avec ID-LoRA pour le mode référencé)
  moteurs-ecartes/               Wan 2.2, S2V, InfiniteTalk, MiniMax H3, LTX-2.3 : scripts exécutables + VERDICTS.md
```

## Le parcours d'un épisode, en six pas

1. **Préparer** (`GUIDE-preparation-episode.md`) : la chaîne physique de chaque scène et qui fait quoi, l'inventaire des éléments de continuité, la description canonique de chaque asset, les cadrages, puis la liste de contrôle.
2. **Écrire les briques** de l'épisode dans un module Python de la série (modèle : `iletaitunefois/S01E01/prompts/briques_pilote.py`) : plans, références par plan, blocs identité par variante de style, clauses, cadrages durcis, clips.
3. **Générer les planches de référence** dans le style choisi : `scripts/assembler_refs.py <briques.py> refs.json --styles=StyleP`, puis Higgsfield (Nano Banana Pro), puis **les regarder** avant d'en dériver quoi que ce soit (RÈGLE 2). Les envoyer comme médias et noter les `media_id`.
4. **Générer les images clés** : `scripts/assembler_prompts.py <briques.py> media_ids.json cles.json --styles=StyleP --md=cles.md`, Higgsfield, audit par planche-contact contre le script.
5. **Rendre les clips** : `scripts/assembler_clips.py <briques.py> <dossier_cles> clips.json --styles=StyleP`, pod RunPod avec le volume (`RUNPOD.md`), `scripts/run_ltx25_runpod.py submit …`, rapatriement par `scripts/runpod_s3.py dl`, sorties supprimées du volume, **pod terminé**.
6. **Monter et vérifier** : concaténation à 24 i/s, puis `scripts/analyse_montage.py` (une image par seconde + transcription horodatée) et une vérification plan par plan à pleine résolution. Ce n'est pas optionnel avant de montrer un montage.

## Les scripts

| Script | Rôle |
|---|---|
| `bibliotheque.py` | charge `styles/*/style.json` et un module de briques ; options `--styles=`, `--plans=`, `--clips=` |
| `assembler_refs.py` | prompts des planches de référence (décors, personnages, objets de continuité) |
| `assembler_prompts.py` | prompts des images clés : style + lumière + époque + brique + clauses + `Avoid:` ; sortie JSON pour `generate_image_batch` et MD lisible |
| `assembler_clips.py` | prompts de mouvement LTX-2.5 : gabarit, ligne de présence, garde des objets, répliques citées, longueur 8n+1 |
| `comfy_client.py` | client HTTP ComfyUI partagé : envoi d'image, soumission, index CSV, suivi, `/view` |
| `run_ltx25_runpod.py` | graphe LTX-2.5 deux passes au format API ; `submit`, `poll`, `fetch` |
| `run_ltx_voix_runpod.py` | les modes de voix gelée (IA2V) et référencée (ID-LoRA), validés en repli |
| `runpod.py` | pods : `list`, `create`, `terminate` (REST + GraphQL, clé `RUN_POD` du `.env`, jamais affichée) |
| `runpod_s3.py` | volume réseau par S3 : `ls`, `up`, `dl`, `rm`, `rmdir` (contournements des bizarreries de l'API dans `RUNPOD.md`) |
| `analyse_montage.py` | vérification d'un montage : images datées, audio, transcription horodatée, ligne de temps |
| `rogner_bandes_noires.py` | rogne les bandes noires d'un rendu avant réutilisation |
| `comfy_ui_to_api.py` | convertisseur graphe UI → API (les templates à sous-graphes se réécrivent à la main) |

Les assembleurs ne reformulent jamais un bloc (RÈGLE 13) et collent les gardes par le code, pas par la vigilance (RÈGLE 41). Le tableau de correspondance script ↔ règle est au §6 du guide.

## Ce qu'il faut avoir sous la main

* un `.env` à la racine du dépôt : `RUN_POD`, `RUN_POD_S3_ACCESS_KEY`, `RUN_POD_S3_SECRET_KEY`, `ELEVEN_LABS`, `HUGGING_FACE` — jamais affiché, jamais commité ;
* le MCP Higgsfield connecté (images), un compte RunPod avec le volume `atelier-modeles` (EU-RO-1, 100 Go, 37 Go de modèles LTX-2.5 résidents) ;
* ffmpeg, python 3, boto3.
