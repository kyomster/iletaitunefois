# Wan 2.2 I2V — graphes et scripts tels qu'exécutés le 22 août 2026

Écarté le 23 août 2026 ; verdict dans `../VERDICTS.md`.

* `wan22_i2v_api.json` — image de départ seule (`WanImageToVideo`).
* `wan22_flf2v_api.json` — image de départ et image de fin (`WanFirstLastFrameToVideo`). Il n'existe pas de poids FLF2V séparé pour Wan 2.2 : le nœud utilise les deux experts I2V.
* `clip-zero-DJK.json` — le clip zéro des styles D, J, K.
* `run_clips_runpod.py` — construit le graphe (`api_prompt`), soumet, interroge, rapatrie ; c'est ce fichier qui portait le client ComfyUI avant son extraction dans `../../scripts/comfy_client.py`.
* `run_e2_trois_samplers.py` — le contournement à trois samplers (premier pas sans LoRA, cfg 2,0).
* `chain_dialogue_runpod.py` — chaîne de sous-clips par dernière image rendue, pour un dialogue découpé par locuteur.
* `bootstrap_pod_wan22.sh` — modèles sur disque conteneur (le volume était plein à l'époque).

Modèles : `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`, `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` (Comfy-Org/Wan_2.2_ComfyUI_Repackaged), `umt5_xxl_fp8_e4m3fn_scaled.safetensors`, `wan_2.1_vae.safetensors` (le 14B utilise le VAE 2.1), LoRA LightX2V `Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1` high et low, un par expert.

Réglages : 1280 × 720, 16 i/s, `length` 4n + 1 (2 s → 33, 2,5 s → 41, 3 s → 49, 3,5 s → 57, 4 s → 65), 4 étapes (2 sur l'expert high noise avec bruit, 2 sur le low noise sans), cfg 1,0 (imposé par le LoRA distillé : au-dessus, l'image brûle), euler/simple, `ModelSamplingSD3` shift 5,0, graine fixe par clip. Deux `KSamplerAdvanced` chaînés, jamais un KSampler simple : le mélange d'experts perd tout son intérêt.

Pièges propres : un seul expert chargé ou le LoRA sur un seul expert → rendu mou ; le mauvais VAE (celui du 5B) → couleurs fausses ; `length` pair → refus.
