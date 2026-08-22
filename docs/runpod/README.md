# Graphes ComfyUI du pilote (format API), tels qu'exécutés le 22 août 2026

* `wan22_i2v_api.json` — image de départ seule (WanImageToVideo). Exemple : P5-3_StyleA.
* `wan22_flf2v_api.json` — image de départ et image de fin (WanFirstLastFrameToVideo). Exemple : P1a-1 → P1a-2, style A.

Les deux sont générés par `docs/scripts/run_clips_runpod.py::api_prompt` à partir de `jobs.json` (`docs/scripts/build_clips_pilote.py`). Le texte des prompts et les graines de chaque clip sont dans `docs/prompts/S01E01-pilote-clips-prompts.md`.

Modèles (noms de fichiers tels que dans `models/`) : `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`, `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` (Comfy-Org/Wan_2.2_ComfyUI_Repackaged), `umt5_xxl_fp8_e4m3fn_scaled.safetensors`, `wan_2.1_vae.safetensors`, LoRA LightX2V `lightx2v/Wan2.2-Lightning/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1/{high,low}_noise_model.safetensors` renommés `wan2.2_i2v_lightx2v_4steps_{high,low}_noise.safetensors`.

Réglages : 1280 × 720, 16 im/s, `length` 4n+1 (2 s → 33, 2,5 s → 41, 3 s → 49, 3,5 s → 57, 4 s → 65), 4 étapes (2 sur l'expert high noise avec bruit, 2 sur le low noise sans), cfg 1.0, euler / simple, ModelSamplingSD3 shift 5.0, LoRA force 1.0, graine fixe par clip. Sortie : séquence PNG (master) + mp4 h264 (aperçu).

**Il n'existe pas de poids FLF2V séparé pour Wan 2.2** : le nœud WanFirstLastFrameToVideo utilise les deux experts I2V. Le mode d'emploi §4 qui liste « Wan 2.2 14B FLF2V » comme fichier distinct est à corriger.
