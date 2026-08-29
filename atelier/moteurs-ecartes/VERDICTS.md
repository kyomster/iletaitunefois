# Moteurs essayés puis écartés — ce qu'ils ont donné, pourquoi on ne les reprend pas, quand les rouvrir

Une semaine d'essais, 22 au 24 août 2026, une vingtaine de dollars de GPU et une centaine de crédits. Chaque dossier garde ses scripts, ses graphes et son bootstrap, exécutables tels quels sur un pod ; ce document garde les verdicts. Le détail chronologique et les sources sont dans `atelier/moteurs-ecartes/ETAT-DE-L-ART-dialogue-video.md`.

Le moteur retenu, LTX-2.5, est décrit dans `../STRATEGIE-video.md`.

---

## Wan 2.2 I2V A14B — `wan22/`

**Ce que c'est.** Le premier moteur du projet : deux experts fp8 (high noise, low noise), LoRA d'accélération LightX2V 4 étapes, 1280 × 720, 16 i/s, longueur 4n + 1, cfg 1, euler/simple, shift 5. Graphes `wan22_i2v_api.json` et `wan22_flf2v_api.json` ; il n'existe **pas** de poids FLF2V séparé, le nœud `WanFirstLastFrameToVideo` utilise les deux experts I2V. Client et soumission : `run_clips_runpod.py`.

**Ce qu'il a donné.** 48 clips du pilote en A, B, C ; ~65 s par clip sur A100 ; 3 $ le pilote.

**Pourquoi écarté (23 août).** Trois défauts structurels : (1) **l'auditeur ouvre la bouche** pendant la réplique de l'autre, quoi qu'on écrive — issue ouverte n° 77 du dépôt Wan 2.2, sans réponse ; le texte n'est pas le levier ; (2) **des personnages surgissent** dans les plans vides (visage géant, inkman fantôme, homme à chapeau sur la corde) ; (3) **le LoRA LightX2V tue le mouvement** (« live wallpaper ») ; le contournement à trois samplers (premier pas sans LoRA, cfg 2,0 et non 3,5 qui dérive les couleurs — `run_e2_trois_samplers.py`) gagne peu pour deux fois le temps.

**Ce qui reste vrai.** La ligne de présence par plan et les négatives de présence, nées ici, sont dans le gabarit LTX. La règle de raccord aussi : **le raccord se choisit selon que le cadrage change** (coupe nette → I2V depuis une clé neuve) **ou non** (continuité → chaîne par dernière image rendue, `chain_dialogue_runpod.py`) ; le FLF2V ne sert qu'avec deux clés distinctes dans le même cadrage, et deux images identiques en FLF2V donnent un clip figé.

**Quand le rouvrir.** Jamais pour un plan de dialogue. Pour un plan muet, seulement si LTX-2.5 échoue sur un cas précis, et alors avec les trois samplers.

---

## Wan 2.2 S2V — `wan22-s2v/`

**Ce que c'est.** Speech-to-video : image clé + mp3 d'une réplique → la bouche suit la voix. `wan2.2_s2v_14B_fp8_scaled` (16,4 Go), encodeur `wav2vec2_large_english_fp16`, nœud `WanSoundImageToVideo`, uni_pc/simple, shift 8. Une réplique ≤ 4,8 s = un rendu de 77 images. `run_s2v_runpod.py`, bootstrap dédié.

**Ce qu'il a donné.** La synchro est réelle, ~1 min par réplique sur RTX 5090, le style tient.

**Pourquoi écarté (22 août, lot 7).** **S2V anime le visage le plus visible, pas le locuteur** : aucune entrée de masque ni de choix du personnage. Sur un plan à deux, ou dès que le locuteur est de dos, c'est le mauvais visage qui parle. Comportement du modèle, confirmé par la documentation ComfyUI, pas un réglage.

**Quand le rouvrir.** Un plan à **un seul visage** (monologue, gros plan) dont la voix doit être exactement une piste fournie — et encore, le mode « audio gelé » de LTX-2.5 fait la même chose sur le moteur retenu.

---

## InfiniteTalk / MultiTalk (MeiGen, sur Wan 2.1) — `infinitetalk/`

**Ce que c'est.** Un module audio greffé sur Wan 2.1 I2V 14B, qui **lie chaque piste audio à un masque de visage** (L-RoPE, mode séquentiel `add`) : c'est l'architecture qui répond à « un locuteur parle, l'autre se tait ». Nœuds Kijai (`ComfyUI-WanVideoWrapper`), `run_infinitetalk_runpod.py`, bootstrap E123.

**Ce qu'il a donné.** Sur P02 et P03 en A et B : le locuteur parle sur **notre** voix, l'auditeur garde la bouche fermée, en un seul rendu par plan. ~22 min d'A100 par plan de 8 s.

**Pourquoi abandonné (23 août, Guillaume).** Rendu jugé insuffisant après deux séries : bouches inkman faiblement alignées, une voiture moderne hallucinée dans un fond de rue (Wan 2.1), qualité globale en retrait. Deux pièges consignés : **l'ordre des pistes audio doit suivre l'ordre des masques**, pas la position à l'image ; l'audio se charge par le widget, pas par un chemin de fichier.

**Quand le rouvrir.** Si un jour il faut deux voix verrouillées à l'identique dans un même plan et que le mode gelé de LTX ne tient pas. Peu probable.

---

## MiniMax H3 — `minimax-h3/`

**Ce que c'est.** Modèle omni-modal à poids ouverts, natif ComfyUI, I2V et R2V (référence → vidéo), 1344 × 768, 24 i/s, LoRA turbo. Génère voix et image ensemble. `run_minimax_h3_runpod.py`, bootstrap E7.

**Ce qu'il a donné.** Le style tient en I2V comme en R2V ; les dialogues en français sont **très bons** dès que le prompt suit le format du skill officiel (`<d>[French] …</d>`, locuteurs `(S1)`/`(S2)` décrits par timbre ; R2V en six sections `<Subject n>`, `<Picture n>`, `<Audio n>`) — sans ce format, des mots qui n'existent pas. Mouvement de caméra plus riche que LTX. Ne recopie pas une référence audio, il la resynthétise.

**Pourquoi écarté comme moteur principal (23 août, E7).** **Il hallucine sur les plans muets** : tête géante sur 4a-1 B, débris sur 5-2 A, là où LTX-2.5 est propre douze fois sur douze. Et il réécrit parfois une réplique.

**Quand le rouvrir.** C'est le **second choix pour un plan de dialogue qu'on veut plus « joué »** que ce que LTX donne. Guillaume l'a jugé « plus créatif, parfois trop ». Toujours au format du skill.

---

## LTX-2.3 — `ltx23/`

Prédécesseur de 2.5, poids ouverts sans jeton, testé quand 2.5 était encore *gated* pour nous. Deux clips propres à ~1 min ; a fait tomber ComfyUI une fois au chargement (file perdue → resoumettre, moteur inconnu en fin de file). Remplacé par 2.5 dès le jeton obtenu. Ses templates IA2V et ID-LoRA ont servi de modèle aux modes de voix de 2.5.

---

## Modèles fermés par API Higgsfield — pas de dossier

Veo 3.1 Lite (12 crédits), Wan 2.7 (12), Kling 3.0 (16), Seedance 2.0 Mini (20), sur P02 A 8 s : tous tiennent le style et alternent les bouches ; Wan 2.7 et Seedance disent le texte exact, Veo presque, Kling déforme. **Aucun n'a pu prendre nos voix** (Wan 2.7 : une seule référence audio ; Seedance : échec avec nos mp3 ; Veo et Kling : pas de référence). Une option « voix générées » propre et rapide si l'on renonce au contrôle des voix — et un coût par plan dix fois supérieur à LTX sur un pod.

---

## Ce qui ne s'est pas fait

* **HunyuanVideo-Avatar** (multi-personnage par masque latent) : 96 Go recommandés, nœud ComfyUI immature.
* **AnyTalker** (multi-personnes de gauche à droite) : code de recherche, pas de ComfyUI.
* **Retouche locale de bouche** (LatentSync, MuseTalk, Wav2Lip) : entraînés sur visages réels, comportement sur du cartoon inconnu.
* **Compositing au montage** (moitié d'image de l'auditeur prise dans le sous-clip de silence) : gratuit et déterministe, proposé au lot 8, rendu inutile par LTX.
