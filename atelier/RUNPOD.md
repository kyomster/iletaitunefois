# RunPod, le volume S3 et ComfyUI — mode d'emploi

Consolidé le 27 août 2026. Tout ce qu'il faut pour rendre des clips sur un GPU loué, sans rien retélécharger, et sans laisser tourner une machine. Ce qui est propre à Wan 2.2 est dans `moteurs-ecartes/wan22/`.

---

## 1. Le principe : le volume est permanent, le pod est jetable

Un **volume réseau** (`atelier-modeles`, id `o6g76dr9cj`, EU-RO-1, 100 Go) porte les modèles une fois pour toutes. Un **pod** GPU se crée pour une session, monte le volume sur `/workspace`, rend, et se **termine** — pas seulement s'arrêter : `DELETE /pods/{id}`, disque conteneur perdu, volume conservé, plus rien de facturé.

Le volume expose une **API compatible S3** (`https://s3api-eu-ro-1.runpod.io`, bucket = **l'id du volume**, pas son nom ; clés `RUN_POD_S3_ACCESS_KEY` / `RUN_POD_S3_SECRET_KEY` du `.env`). C'est la bonne pratique permanente posée par Guillaume le 24 août :

* **les modèles se déposent sur le volume sans GPU allumé** — `scripts/runpod_s3.py up` ; le pod les trouve par `extra_model_paths.yaml` ;
* **les sorties s'écrivent sur le volume** (`--output-directory /workspace/out`), se rapatrient par S3, puis **se suppriment du volume** ;
* **on garde sur le volume tout ce qui est réutilisable** : modèles, encodeurs, VAE, upsampler, LoRA, clés 1280×704, références, workflows ;
* avant chaque session : `runpod_s3.py ls` pour vérifier le contenu, compléter ce qui manque.

Résultat mesuré : pod prêt en ~2 minutes au lieu de ~45, 1,6 $ pour 18 clips au lieu de 4 $.

---

## 2. L'outil S3 et ses pièges

`python scripts/runpod_s3.py ls [préfixe] | up <local> <clé> | dl <clé> <local> | rm <clé> | rmdir <préfixe>` — boto3, `signature_version="s3v4"`.

Quatre comportements propres à l'API S3 de RunPod, tous payés :

* **`HeadObject` répond 403** → `download_file` de boto3 échoue ; `dl` lit `get_object` directement.
* **`DeleteObjects` (suppression par lot) répond 307** → suppression objet par objet.
* **L'API est adossée à un vrai système de fichiers** : `DeleteObject` sur un dossier non vide répond « directory not empty » ; `rmdir` supprime par profondeur décroissante. Les liens symboliques (`lib64`) ne se suppriment que depuis un pod.
* **Redimensionner un volume passe par REST** : `PATCH https://rest.runpod.io/v1/networkvolumes/{id}` avec `{"size": N}` ; la mutation GraphQL `updateNetworkVolume` renvoie 400.

L'API S3 n'existe que dans certains datacenters (EU-RO-1 en fait partie) ; le débit d'upload depuis la machine locale est le facteur limitant sur les gros fichiers.

---

## 3. Le pod

`python scripts/runpod.py create <nom> <clé_ssh.pub> | status <id> | ports <id> | stop <id> | terminate <id> | list`. Clé `RUN_POD` du `.env`, jamais affichée.

* **GPU** : `GPUS=` liste ordonnée. Mesuré sur LTX-2.5 : **RTX PRO 6000 Blackwell 96 Go** ~30 s par clip, **A100 80 Go** ~1 min, **A100 SXM** équivalent ; **RTX 5090 32 Go** trop petite pour LTX-2.5 + un second moteur. Les L40S et RTX 6000 Ada ne sont jamais en stock en EU-RO-1.
* **Capacité** : EU-RO-1 n'a parfois **aucune instance** pendant un quart d'heure. Le volume y est ; on réessaie toutes les trois minutes plutôt que de déménager (`DCS=` existe, mais coûte 45 min de retéléchargement).
* **Disque conteneur** : `DISK_GB=60` suffit quand les modèles sont sur le volume.
* **Réseau** : `PUBLIC_KEY` et `JUPYTER_PASSWORD` en variables d'environnement, ports `22/tcp`, `8188/http` ; ip:port SSH par GraphQL (`pod { runtime { ports } }`) ; ComfyUI se pilote par `https://<podId>-8188.proxy.runpod.net/` (`/upload/image`, `/prompt`, `/history`, `/queue`, `/view`).
* **L'API GraphQL et le proxy des pods renvoient 403 à l'agent utilisateur Python** : `User-Agent: curl/8.0` partout. L'API REST v1 accepte urllib tel quel.

---

## 4. Le bootstrap

`runpod/bootstrap_pod_ltx25_volume.sh` : clone ComfyUI, `pip install`, écrit `extra_model_paths.yaml` vers `/workspace/models`, ne télécharge que ce qui manque (`need()` vérifie la taille — un dépôt Hugging Face *gated* sans jeton renvoie des pages d'erreur de 126 octets), lance ComfyUI avec `--listen 0.0.0.0 --port 8188 --output-directory /workspace/out --input-directory /workspace/in`, affiche `BOOTSTRAP_DONE`.

`runpod/bootstrap_pod_ltx25_idlora.sh` ajoute LTX-2.3 et l'ID-LoRA talkvid pour le mode de voix référencé.

Modèles LTX-2.5 sur le volume, dans `models/` :

```
diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors   21,5 Go
text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors           15,4 Go
vae/ltx-2.5-video-vae-bf16.safetensors                                                1,5 Go
vae/ltx-2.5-audio-vae-bf16.safetensors                                                0,4 Go
latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors        0,9 Go
```

---

## 5. Produire par lots

Un graphe ComfyUI s'exporte en **format API** (Workflow → Export (API)) ou se réécrit à la main depuis un template : `scripts/comfy_ui_to_api.py` convertit un workflow d'interface. Un template à sous-graphe se réécrit à la main à partir de son dump ; les entrées « autogrow » s'écrivent `groupe.entree_N`.

La boucle : pour chaque clip, charger le graphe, y mettre l'image de départ, le prompt, la longueur et la graine, poster sur `/prompt`. **La ligne d'index s'écrit avant le lancement** — nom du clip, graine, modèle, heure ; retrouver après coup ce qui a produit quoi est lent et fragile.

Après un crash de ComfyUI, la file et l'historique sont perdus : resoumettre, retrouver les mp4 par `/view`. Mettre un moteur inconnu **en fin de file**.

---

## 6. Pièges, dans l'ordre où ils coûtent

1. **Le pod laissé allumé.** C'est la défaillance la plus chère de ce projet. `terminate`, puis `list` vide vérifié, à chaque session, sans exception.
2. **Les modèles sur le disque conteneur** au lieu du volume : tout à retélécharger au pod suivant. `df -h /workspace` et `du -sh /workspace/*` avant tout téléchargement.
3. **Les sorties laissées sur le volume** : il gonfle, on paie. `rmdir out/` après rapatriement.
4. **Une image de départ en 2752 × 1536** envoyée telle quelle : redimensionner en 1280 × 704 en amont, sinon le modèle recadre.
5. **Une longueur qui n'est pas en 8n + 1** (LTX) ou 4n + 1 (Wan).
6. **Oublier la graine** : un clip validé qu'on ne peut pas reproduire est un clip perdu.
7. **Le volume plein de restes d'une autre session** : 67 Gio d'entraînements LoRA y dormaient. Inventaire S3 avant d'agrandir.
