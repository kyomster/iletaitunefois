# État de l'art — plans de dialogue en vidéo générée : ce que Wan 2.2 sait faire, ce qu'il ne sait pas, et quoi tester à la place

Recherche du 23 août 2026, demandée par Guillaume après le lot 8 du pilote (« les images avec dialogue c'est toujours pas ça »). Sources en bas de page. Tout ce qui est affirmé ici vient soit des sources, soit de nos propres mesures (audits lots 5 à 8) ; les deux sont distingués.

## 1. Le diagnostic, confirmé par l'extérieur

Notre problème : sur un plan à deux, pendant que l'un parle, **l'autre ouvre la bouche**, quoi qu'on écrive dans le prompt (« the other keeps his mouth firmly closed », négatives, images clés bouches fermées — lot 8).

* C'est un **défaut connu et non résolu de Wan 2.2 I2V** : l'issue officielle n° 77 du dépôt Wan‑Video/Wan2.2 (août 2025) décrit exactement ça — « unwanted mouth movements, where the character appears to be talking, even when the prompts explicitly instruct "no talking" or "mouth closed" » — et n'a reçu aucune réponse ni contournement.
* Les guides de prompt Wan 2.2 (VEED, wan27.org, instasd) disent tous la même chose : structure Sujet → Action → Caméra → Scène, **25 à 80 mots** (au‑delà, le prompt est « partiellement ignoré »), verbes concrets avec vitesse et direction, caméra explicite même pour « static shot », n'animer que ce qui est visible. **Aucun ne propose de moyen de tenir une bouche fermée**. Le texte n'est pas le bon levier pour ça — c'est notre RÈGLE 1 (on ne contrôle pas par la négative) transposée à la vidéo.
* **Wan 2.2 S2V** (ce qu'on a testé au lot 6/7) : la doc ComfyUI le confirme, les entrées sont image + audio + texte (+ une vidéo de pose optionnelle), **pas de masque ni de choix du personnage animé** ; il anime le visage le plus visible. Creepybits (comparatif pratique MultiTalk / InfiniteTalk / Wan‑S2V) juge Wan‑S2V « not recommended in current state ». Notre mesure du lot 7 (S2V anime le mauvais visage) est donc un comportement du modèle, pas une erreur de réglage.

Conclusion : **on a atteint la limite du couple Wan 2.2 I2V + prompt** pour les plans de dialogue à deux. Ce n'est pas une question de brique.

## 2. Ce qui existe pour faire exactement ce qu'on veut : une voix → un personnage, l'autre se tait

### 2.1 MultiTalk / InfiniteTalk (MeiGen‑AI, NeurIPS 2025) — candidat n° 1

* **Ce que c'est** : un module audio greffé sur **Wan 2.1 I2V 14B** (pas 2.2), entraîné pour la **génération de vidéos de conversation à plusieurs personnes**. Chaque piste audio est **liée à une région de l'image** (boîte englobante dans le code d'origine, **masque par visage** dans ComfyUI) par un mécanisme de position (« L‑RoPE », un intervalle de fréquences par locuteur : locuteur 1 = [0‑4], locuteur 2 = [20‑24], fond = 12). C'est précisément l'architecture qui manque à Wan 2.2 S2V : **la bouche de l'auditeur n'est pas pilotée par la voix de l'autre**.
* **Modes** : `para` (les deux parlent en même temps) ou **`add` (séquentiel : l'un puis l'autre)** — notre cas. Le README revendique la **généralisation aux personnages de dessin animé** et au chant. 480p et 720p, jusqu'à 15 s (MultiTalk) ; **InfiniteTalk** est la version « longue durée » (fenêtres de 81 images avec recouvrement, meilleure tenue d'identité, ~1 min de rendu par seconde de vidéo sans LoRA ; « rock‑solid » sur la synchro selon Creepybits).
* **Dans ComfyUI** : nœuds de Kijai (`ComfyUI‑WanVideoWrapper`) : `MultiTalkWav2VecEmbeds` (jusqu'à 4 pistes audio, `ref_target_masks` = un masque par visage, **masques qui ne se touchent jamais**, `multi_audio_type` add/para, `audio_scale` à baisser si les mouvements exagèrent) → `WanVideoImageToVideoMultiTalk` (fenêtre 81 images, `motion_frame` 25, `colormatch` contre la dérive de couleur) → sampler. Exemples livrés : `wanvideo_2_1_14B_I2V_InfiniteTalk_example_03.json` ; variante multi‑locuteurs documentée par RunComfy (« draw one mask per face in the mask editor »). Poids : `Wan2.1‑I2V‑14B‑480P` (ou 720P), `chinese‑wav2vec2‑base`, `InfiniteTalk/multi/infinitetalk.safetensors` ; accélération **lightx2v 4 pas** ou **FusioniX 8 pas** (`text_guide 1.0`, `audio_guide 2.0`).
* **RunPod** : un modèle de pod/serverless existe (`wlsdml1114/Infinitetalk_Runpod_hub`, workflows `I2V_multi.json`, `V2V_multi.json`) ; sinon notre pod ComfyUI habituel + le wrapper de Kijai.
* **Limites** : base **Wan 2.1** — MultiTalk sur Wan 2.2 ne marche pas (issue wrapper n° 1326 sans solution : « little effect on the 2.2 high noise model ») ; MultiTalk court peut donner un effet « ventriloque » (yeux/joues raides), InfiniteTalk corrige ; dérive de couleur au‑delà d'une minute (sans objet pour nous) ; l'audio doit être **chargé par le widget audio** (chemin de fichier = son étouffé et synchro médiocre, piège rapporté par Creepybits). Le rendu 2.1 ne sera pas identique au 2.2 : à comparer sur la même clé.

### 2.2 HunyuanVideo‑Avatar (Tencent) — candidat n° 2

Modèle MM‑DiT audio‑driven « emotion‑controllable, **multi‑character dialogue** », le multi‑personnage se fait par **masquage dans l'espace latent** (un masque par visage, un audio par visage). Mais : 24 Go « très lent », **96 Go recommandés**, et le nœud ComfyUI communautaire est jeune (29 étoiles, pas de release). À garder pour plus tard.

### 2.3 AnyTalker (HKUST, nov. 2025, Apache 2.0) — candidat n° 3

Multi‑personnes, audio lié aux personnes **de gauche à droite** (détection de visages InsightFace, seuil réglable pour « abstract‑style images »), base **Wan2.1‑Fun 1.3B** (le 14B demande 80 Go), 832×480, pas de ComfyUI. Code de recherche : possible sur un pod, mais tout à la main.

### 2.4 LTX‑2.3 / LTX‑2.5 (Lightricks, poids ouverts) — autre moteur, pas une réponse au dialogue à deux

* LTX‑2 (19B, janvier 2026), **LTX‑2.3** (mars 2026) et **LTX‑2.5** (22B, **11 août 2026**) génèrent **vidéo + audio dans la même passe** ; natifs dans ComfyUI (T2V, I2V, FLF2V, multi‑plans, upscalers) ; RunPod publie un guide (RTX 4090 pour fp8/distillé, L40S/A100 pour bf16 ; LTX‑2.5 : int8 ~66 Go de fichiers, **32‑48 Go de VRAM** = RTX 5090 / L40S, 80‑96 Go pour le bf16). Très rapide (distillé 8 pas).
* Il existe un workflow **LTX‑2.3 « image + audio → vidéo »** (IA2V) où l'audio fourni pilote la bouche — mais il est conçu pour **un portrait + une voix** ; rien de documenté pour choisir qui parle dans un plan à deux.
* Intérêt pour nous : **moteur alternatif pour les plans sans dialogue** (mouvement, cohérence, vitesse) et pour un plan de dialogue **à un seul visage**. Le style 2D n'est pas documenté ; à juger sur un essai.

### 2.5 Retouches locales de bouche (LatentSync 1.6, MuseTalk, Wav2Lip)

Ces outils ne génèrent pas la vidéo : ils **remplacent la région de la bouche** dans une vidéo existante à partir d'un audio. On pourrait les appliquer à nos sous‑clips I2V sur **le visage du locuteur seulement** (et figer l'autre). Entraînés sur des visages réels ; comportement sur des visages cartoon A/B inconnu, donc pari. LatentSync demande ≥ A10/RTX 4090.

### 2.6 Rien à installer : compositing au montage (proposition du lot 8)

Sur un plan fixe où les deux personnages ne se chevauchent pas (P02, P03), on prend la moitié d'image de l'auditeur dans le sous‑clip de silence (bouche fermée garantie) et la moitié du locuteur dans son sous‑clip. Gratuit, déterministe, déjà faisable avec ce qu'on a. Ne règle pas « le locuteur de dos » ni la qualité de l'articulation.

## 3. Deux bonnes pratiques Wan 2.2 qu'on n'applique pas encore (plans hors dialogue)

1. **Le LoRA LightX2V 4 pas tue le mouvement.** La doc ComfyUI S2V l'écrit (« significant dynamic and quality loss »), et la discussion « bad motion » du dépôt Wan2.2‑Lightning le détaille (« almost like a live wallpaper »). Nos plans « figés » (4b‑1/2/3, 4a‑2, 5‑1/5‑2 relevés par Sonnet) en sont très probablement la conséquence. Contournement communautaire : **trois samplers** — 1er pas haut‑bruit **sans LoRA à cfg 3.5**, puis pas haut‑bruit avec LoRA (force 0,6‑0,8), puis bas‑bruit avec LoRA (force 1, cfg 1), ~8 pas au total. Coût : environ ×2 en temps de rendu. À tester sur deux plans fixes avant de généraliser.
2. **Prompt vidéo de 25 à 80 mots.** Nos prompts vidéo (bloc de style + gabarit + ligne de présence + négatives) dépassent largement ; on a déjà constaté que le style B marche mieux avec le bloc de style réduit. Il faut un gabarit court : action concrète (vitesse, direction), caméra explicite, et le style en deux mots, le reste étant porté par l'image clé.

## 4. Ce que je propose de tester (à valider par Guillaume)

| Essai | Quoi | Où | Coût estimé |
|---|---|---|---|
| **E1 — InfiniteTalk multi‑locuteurs** | P02 et P03 en A et B : image clé 720p + deux masques (un par visage) + deux pistes (BADAUD1 puis BADAUD2 ; AIDE puis GARNERIN) en mode `add`, 81 images, lightx2v 4 pas puis sans LoRA si raide | pod RunPod A100 ou RTX 5090, ComfyUI + WanVideoWrapper, poids Wan 2.1 I2V 14B 720p fp8 + InfiniteTalk multi + wav2vec2 (~35 Go à télécharger) | 1 h 30 à 2 h de pod ≈ 2‑3 $ ; 0 crédit Higgsfield |
| **E2 — trois samplers** | 4b‑2 et 5‑2 A re‑rendus avec le 1er pas sans LoRA | même pod, graphe I2V actuel modifié | 10 min |
| **E3 — LTX‑2.5 I2V** (optionnel) | 2 plans sans dialogue (1a‑2, 4a‑3) en A, pour comparer mouvement/style à Wan 2.2 | même pod, modèles LTX‑2.5 int8 (~66 Go, volume à libérer) | 30 min + téléchargement |

Prérequis pour E1 : **P03 recadré** pour que les deux visages soient visibles (A : l'aide est de dos ; B : Garnerin est de dos) — 2 images Higgsfield (4 crédits) ; sinon on teste E1 sur P02 seul. Ce que E1 doit prouver : l'auditeur garde la bouche fermée, la bouche du locuteur suit la voix, le style A/B tient sur Wan 2.1. Si c'est concluant, la méthode de dialogue de l'épisode devient « un rendu MultiTalk par plan de dialogue » et la bible passe de « pas de synchro labiale » à « synchro par MultiTalk » ; sinon, compositing (§ 2.6) pour le pilote.

## Sources

* Wan 2.2, bouche qui bouge malgré le prompt : https://github.com/Wan-Video/Wan2.2/issues/77
* Guides de prompt Wan 2.2 : https://www.veed.io/learn/wan-2-2-prompting-guide · https://wan27.org/blog/wan-2-2-prompt-guide · https://www.instasd.com/post/wan2-2-whats-new-and-how-to-write-killer-prompts
* Wan 2.2 S2V, doc ComfyUI (entrées, 77 images, LoRA « significant dynamic and quality loss ») : https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v · https://blog.comfy.org/p/wan22-s2v-in-comfyui-audio-driven
* LightX2V « bad motion », trois samplers : https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/5 · https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/20
* MultiTalk (papier, code, multi‑personnes, cartoon, réglages LoRA) : https://github.com/MeiGen-AI/MultiTalk · https://arxiv.org/abs/2505.22647 · InfiniteTalk : https://github.com/MeiGen-AI/InfiniteTalk
* Nœuds ComfyUI (MultiTalkWav2VecEmbeds, ref_target_masks, add/para, L‑RoPE) : https://deepwiki.com/kijai/ComfyUI-WanVideoWrapper/8.1-multitalk-system · https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows · multi‑locuteurs : https://www.runcomfy.com/comfyui-workflows/comfyui-multitalk-workflow-multi-speaker-lip-synced-video-generator · https://infinitetalk.org/infinitetalk-multi-person
* MultiTalk sur Wan 2.2 (ne marche pas) : https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1326 · https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1492
* Comparatif pratique MultiTalk / InfiniteTalk / Wan‑S2V : https://zanno.se/lets-talk-multitalk-infinitetalk-wan-s2v/
* InfiniteTalk sur RunPod : https://github.com/wlsdml1114/Infinitetalk_Runpod_hub
* HunyuanVideo‑Avatar : https://hunyuanvideo-avatar.github.io/ · https://github.com/Yuan-ManX/ComfyUI-HunyuanVideo-Avatar
* AnyTalker : https://github.com/HKUST-C4G/AnyTalker · https://arxiv.org/abs/2511.23475
* LTX‑2 / 2.3 / 2.5 : https://blog.comfy.org/p/ltx-2-open-source-audio-video-ai · https://comfy.org/workflows/video_ltx2_3_ia2v-adca306765ce/ · https://docs.comfy.org/tutorials/video/ltx/ltx-2-5 · https://www.runpod.io/articles/guides/comfyui-ltx-2-runpod · https://www.runpod.io/blog/ltx-2-5-the-open-weights-world-model-built-for-speed-and-how-to-run-it-on-runpod · https://comfyui-wiki.com/en/news/2026-08-11-ltx-2-5-open-weights-release
* Comparatifs de moteurs ouverts 2026 : https://ltxworkflow.com/blog/ltx-2-3-vs-hunyuanvideo-vs-wan2-2-comparison-2026 · https://www.aimagicx.com/blog/open-source-ai-video-models-comparison-2026
* Lipsync local (LatentSync, MuseTalk) : https://instavar.com/research/ai-video/open-source-lip-sync-models · https://lipsync.com/blog/open-source-lip-sync
