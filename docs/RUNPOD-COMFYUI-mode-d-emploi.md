# RunPod et ComfyUI — mode d'emploi

**22 août 2026.** De rien à 48 clips rendus. Rédigé pour être suivi ligne à ligne le jour du lancement, sans avoir à rechercher quoi que ce soit.

Ce document ne traite que le **rendu vidéo**. Les images clés restent sur Nano Banana Pro chez Higgsfield, voir `PIPELINE-video-et-voix.md` point 3.

---

# 1. Ce qu'on monte

Un ComfyUI sur GPU loué, qui prend une image clé et produit un clip de 2 à 4 secondes, avec **Wan 2.2 I2V A14B** à poids ouverts. Deux graphes seulement :

* **I2V** : une image de départ, un clip. C'est le cas général, il couvre le premier clip de chaque bloc et tous les clips qui suivent une coupe nette.
* **FLF2V** : une image de départ et une image de fin, un clip entre les deux. C'est le cas des raccords à l'intérieur d'un bloc, quand la dernière image du clip précédent doit être la première du suivant.

Deux phases distinctes, à ne pas mélanger :

| Phase | Mode | Pourquoi |
|---|---|---|
| Mise au point du graphe et essais de style | **Pod persistant** | On garde l'interface ouverte, on itère, on regarde |
| Production des lots | **Serverless** ou pod à la demande | On paie à la seconde de calcul, pas au temps passé à réfléchir |

---

# 2. Le GPU

| Usage | GPU | VRAM | Prix indicatif |
|---|---|---|---|
| **Retenu pour la production** | L40S ou RTX 6000 Ada | 48 Go | 0,79 à 0,99 $/h |
| Repli économique | RTX 5090 | 32 Go | environ 0,69 $/h |
| Brouillons de cadrage | RTX 4090 | 24 Go | 0,34 à 0,74 $/h |
| Inutile ici | H100, H200, B200 | | de 2,89 à 6,79 $/h, aucun gain sur un modèle de 14B en FP8 |

Le palier de 48 Go est le bon : il fait tourner le 14B en 720p **sans quantification agressive**. En dessous il faut du GGUF, et ce qu'on perd en premier est la netteté du trait, c'est à dire exactement ce que cette série ne peut pas se permettre de perdre.

Les tarifs varient entre Community Cloud et Secure Cloud et changent souvent. **Vérifier la grille du jour avant de réserver**, et regarder les instances interruptibles, moins chères de 50 à 80 %, parfaitement adaptées à un rendu par lots qu'on peut relancer.

---

# 3. Monter le pod

1. Créer un **volume réseau de 100 Go** dans la région où le GPU visé est disponible. Le volume est ce qui survit à la destruction du pod : les modèles s'y installent une fois pour toutes. Environ 7 $ par mois.
2. Déployer un pod avec un **template ComfyUI officiel**, en attachant le volume réseau sur `/workspace`.
3. Ouvrir l'interface ComfyUI, mettre à jour ComfyUI et le ComfyUI Manager avant toute chose.
4. Vérifier que le pod voit bien le volume : les modèles téléchargés doivent atterrir sous `/workspace/ComfyUI/models/`, pas sur le disque du conteneur, qui disparaît avec le pod.

**Le piège numéro un** : télécharger 60 Go de modèles sur le disque du conteneur, arrêter le pod le soir, et tout retélécharger le lendemain. Vérifier le point de montage avant de lancer le moindre téléchargement.

---

# 4. Les modèles à installer

Ne pas construire le graphe à la main. **Partir du template officiel Wan 2.2 livré avec ComfyUI**, qui déclare exactement les fichiers attendus et leur emplacement. Le menu des templates propose les entrées Wan 2.2 image vers vidéo et Wan 2.2 première et dernière image.

Ce qu'il faut, sur le volume réseau :

| Quoi | Où | Note |
|---|---|---|
| Wan 2.2 I2V A14B, expert **high noise**, FP8 | `models/diffusion_models/` | le modèle est un mélange d'experts, il y a **deux fichiers**, pas un |
| Wan 2.2 I2V A14B, expert **low noise**, FP8 | `models/diffusion_models/` | |
| Wan 2.2 14B FLF2V | `models/diffusion_models/` | pour le graphe des raccords |
| Encodeur de texte UMT5 XXL, FP8 | `models/text_encoders/` | |
| VAE Wan | `models/vae/` | le 14B utilise le VAE de la génération 2.1, le 5B a le sien, ne pas les confondre |
| LoRA d'accélération LightX2V pour Wan 2.2 | `models/loras/` | **deux fichiers là aussi**, un par expert |
| LoRA de style maison | `models/loras/` | à entraîner, voir le point 9 |

Les fichiers packagés pour ComfyUI sont regroupés dans le dépôt Hugging Face de l'organisation Comfy, sous une arborescence `split_files` qui reprend exactement celle des dossiers ci dessus. Les LoRA d'accélération sont publiés par LightX2V. Compter **50 à 70 Go** au total, et une bonne heure de téléchargement la première fois.

---

# 5. Le graphe I2V, cas général

L'ordre logique, tel que le template le pose :

1. **Load Image** — l'image clé, sortie Nano Banana Pro en 2752 x 1536, redimensionnée en **1280 x 720**.
2. **Load CLIP** — UMT5 XXL, type `wan`.
3. **CLIP Text Encode**, deux nœuds : le positif reçoit le prompt de mouvement assemblé, le négatif reçoit la négative de mouvement.
4. **Load Diffusion Model**, deux nœuds : expert high noise et expert low noise.
5. **LoraLoaderModelOnly**, deux fois : le LoRA LightX2V correspondant sur chaque expert, puis le LoRA de style sur chacun également.
6. **WanImageToVideo** — reçoit l'image, le VAE, les deux conditionnements, et les dimensions. C'est ici qu'on fixe **`length`**, le nombre d'images.
7. **KSampler (Advanced)** en deux passes chaînées : la première sur l'expert high noise pour les premières étapes, la seconde sur l'expert low noise pour les dernières. **Ne pas remplacer par un KSampler simple** : le mélange d'experts perd tout son intérêt et le mouvement s'écrase.
8. **VAE Decode**, puis **Save WEBM** ou une sortie en séquence PNG.

## Longueur des clips

Cadence native **16 images par seconde**. La table de correspondance à utiliser :

| Durée voulue | `length` |
|---|---|
| 2,0 s | 33 |
| 2,5 s | 41 |
| 3,0 s | 49 |
| 3,5 s | 57 |
| 4,0 s | 65 |

Toujours un nombre impair de la forme 4n+1, c'est ce qu'attend le modèle. Le maximum raisonnable est 81, soit 5 secondes ; au delà la cohérence se dégrade nettement et ce n'est de toute façon pas notre découpage.

## Réglages retenus

```
résolution      1280 x 720
length          selon la table ci dessus
steps           4 au total, 2 sur l'expert high noise puis 2 sur le low noise
cfg             1.0
sampler         euler
scheduler       simple
shift           5.0
seed            fixe et consigné par clip
```

Le CFG à 1 n'est pas une erreur : c'est ce qu'impose le LoRA d'accélération distillé. Avec un CFG plus élevé et 4 étapes, l'image brûle.

**Sans le LoRA d'accélération**, il faudrait 20 étapes et un CFG autour de 3,5, pour un temps de rendu multiplié par cinq. À ne faire que si le pilote montre que les 4 étapes coûtent trop en qualité de trait.

---

# 6. Le graphe FLF2V, pour les raccords

Identique au précédent, à trois différences :

* le modèle chargé est la variante FLF2V ;
* le nœud d'entrée prend **deux images**, première et dernière ;
* la dernière image vient du clip précédent, extraite par un nœud d'extraction de dernière image, ou rechargée depuis le fichier.

**Quand l'utiliser.** À l'intérieur d'un bloc, entre deux clips qui se raccordent. Le tableau du pilote donne les cas : les clips 2, 3 et 4 de 1a, les clips 2 et 3 de 1b, et ainsi de suite. **Ne pas l'utiliser après une coupe nette** entre deux blocs : là on veut une rupture, pas une interpolation.

Attention à un effet connu : quand la première et la dernière image sont trop proches, le modèle produit un mouvement mou, parfois un aller retour. Si cela arrive, repasser le clip en I2V simple et laisser le modèle inventer la fin.

---

# 7. La cadence limitée à 10 images par seconde

La série demande une animation limitée, pas une interpolation fluide. Deux façons de l'obtenir :

* **Dans le graphe**, par un nœud de sélection d'images qui ne garde qu'une image sur 1,6. Figé, irréversible.
* **Au montage**, en appliquant la décimation sur la piste. Réversible, comparable, annulable.

**Retenu : au montage.** On rend en 16 im/s, on garde le master, et on décide de l'aspect final en voyant le montage. Le surcoût est nul.

---

# 8. Produire par lots

Une fois le graphe au point, l'exporter depuis ComfyUI par **Workflow puis Export (API)**. On obtient un JSON où chaque nœud est adressable par son numéro.

La boucle de production est alors simple : pour chaque clip du pilote, charger le JSON, y remplacer le chemin de l'image de départ, le prompt positif, la valeur de `length` et la graine, puis poster le tout sur l'endpoint.

* En **pod persistant**, poster sur l'API locale de ComfyUI, sur le port du pod.
* En **serverless**, déployer le worker ComfyUI officiel de RunPod, qui accepte exactement ce JSON dans le champ `input.workflow`, avec les images en base64 dans `input.images`. Attention aux limites de taille de requête, de l'ordre de 10 Mo en asynchrone : passer les images par le volume réseau plutôt qu'en base64 dès que le lot grossit.

Consigner au fil de l'eau, dans un index stable, **le nom du clip, la graine, le modèle et l'heure**. C'est la RÈGLE apprise à la dure sur les 235 images : retrouver après coup ce qui a produit quoi est lent et fragile.

---

# 9. Le LoRA de style

C'est la pièce qui justifie tout le montage. Le dépôt contient, pour le style retenu, environ 84 images validées, homogènes, déjà auditées et nettoyées de leur lettrage parasite : les décors, les personnages d'époque et la troupe. C'est un jeu d'entraînement propre, ce qui est rare.

Entraîner un LoRA de style sur ce jeu permet de tenir le contour noir d'épaisseur constante et l'aplat sans dégradé sur toute la longueur d'un clip, là où le modèle de base ramollit le trait dès la deuxième seconde.

* **Après** le choix du style, jamais sur les trois.
* Sur un GPU de 48 Go, quelques heures.
* Le LoRA se charge sur **les deux experts**, high noise et low noise.
* Le tester d'abord sur trois clips déjà rendus sans lui, et comparer côte à côte. Si le gain n'est pas visible à l'œil, ne pas l'imposer à toute la production.

---

# 10. Rapatriement et nommage

Nommage des clips, aligné sur celui des images du pilote :

```
P<plan><bloc>-<clip>_Style<X>.mp4      exemple : P1a-3_StyleC.mp4
```

Sortie en séquence PNG ou en ProRes pour le master, **jamais en H.264 à ce stade**. Le H.264 est un format de livraison, pas un format de travail : réencoder un clip déjà compressé au montage ajoute des artefacts sur les aplats, qui sont précisément ce que ce style met en avant.

Rapatrier depuis le volume réseau vers `assets/S01E01/clips/Style<X>/`.

---

# 11. Pièges connus, à lire avant de commencer

1. **Les modèles sur le disque du conteneur** au lieu du volume réseau. Tout est à retélécharger au prochain pod.
2. **Un seul expert chargé** au lieu des deux. Le rendu sort, il est simplement mou et sans mouvement franc. Symptôme : tous les clips se ressemblent et rien ne bouge vraiment.
3. **Le LoRA d'accélération sur un seul expert.** Même symptôme, en pire.
4. **Un CFG supérieur à 1 avec 4 étapes.** L'image brûle, les contours bavent.
5. **Le mauvais VAE.** Celui du 5B sur le 14B donne une sortie colorée n'importe comment.
6. **`length` pair.** Le modèle attend un nombre de la forme 4n+1.
7. **Une image de départ en 2752 x 1536** envoyée telle quelle. Redimensionner en 1280 x 720 en amont, sinon le modèle recadre tout seul et on perd le cadrage voulu.
8. **Le FLF2V sur deux images trop proches.** Mouvement mou ou aller retour.
9. **Oublier de consigner la graine.** Un clip validé qu'on ne peut pas reproduire est un clip perdu.
10. **Le pod laissé allumé la nuit.** Un L40S oublié un week end coûte plus cher que tout le pilote.

## Appris le 22 août 2026, sur le pilote

11. **Le volume réseau était déjà plein aux trois quarts** (`atelier-modeles`, 100 Go : un ancien ComfyUI Qwen et ai‑toolkit, 77 Go). Les 38 Go de Wan 2.2 n'y tenaient pas. Pour le pilote, ComfyUI et les modèles ont été mis sur le **disque conteneur** (60 Go) : rapide (2 à 3 min de téléchargement à 5 Gb/s) mais perdu à l'arrêt du pod. Avant la production : soit libérer le volume, soit l'agrandir (`POST /networkvolumes/{id}/update`), soit créer un second volume. Toujours faire `df -h /workspace` et `du -sh /workspace/*` avant de télécharger.
12. **Ni L40S ni RTX 6000 Ada en stock en EU-RO-1** (le centre du volume) ce jour. A100 80 Go PCIe secure à 1,39 $/h a fait l'affaire : ~70 s par clip de 2,5 s en 720p à 4 étapes, modèles compris au premier clip. Interroger `gpuTypes { lowestPrice(input:{dataCenterId}) { stockStatus } }` en GraphQL avant de choisir.
13. **Il n'y a pas de poids FLF2V séparé pour Wan 2.2** : `WanFirstLastFrameToVideo` utilise les deux experts I2V. La ligne « Wan 2.2 14B FLF2V » du §4 est caduque ; le graphe FLF2V ne change que le nœud d'entrée (`docs/runpod/wan22_flf2v_api.json`).
14. **L'API GraphQL et le proxy HTTP des pods renvoient 403 à l'agent utilisateur Python par défaut.** Mettre `User-Agent: curl/8.0` (fait dans `docs/scripts/runpod_pilote.py` et `run_clips_runpod.py`). L'API REST v1, elle, accepte urllib tel quel.
15. **Pour piloter le pod sans interface** : passer `PUBLIC_KEY` (clé ssh publique) et `JUPYTER_PASSWORD` en variables d'environnement à la création, exposer `22/tcp` et `8188/http`, récupérer l'ip:port SSH par GraphQL (`pod { runtime { ports } }`). ComfyUI se lance avec `--listen 0.0.0.0 --port 8188` et se pilote par `https://<podId>-8188.proxy.runpod.net/` : `/upload/image`, `/prompt`, `/history`, `/view`. Tout est dans `run_clips_runpod.py`.
16. **Un plan sans personnage peut s'en voir attribuer un.** Sur P5‑3 (la corde seule), les styles B et C ont fait apparaître une tête d'inkman, puis un homme à chapeau, qui agrippent la corde, malgré `extra characters appearing` en négative. Le bloc de style décrit des personnages ; sur un gros plan vide, le modèle en fournit un. Prescrire le vide en positif dans la brique de mouvement (`nobody in the shot, no hands, the rope and the sky only`), comme la RÈGLE 25 pour la peau.
17. **Coût réel du pilote** : pod A100 80 Go PCIe secure, 2 h 13 (création 11 h 47, fin 14 h 00 UTC), **3,08 $** pour 96 rendus (48 clips en trois lots, dont deux relances de méthode) + téléchargement des modèles et mise au point. ~65 s par clip de 2,5 à 3 s, ~90 s pour 4 s. La prévision du §9.1 du PIPELINE (4 à 8 $ sur L40S) était large.
18. **Terminer le pod, pas seulement l'arrêter** (`DELETE /pods/{id}`) : le disque conteneur disparaît de toute façon, le volume réseau survit, et plus rien n'est facturé. Fait à 14 h 00 UTC, vérifié par `GET /pods` vide.
