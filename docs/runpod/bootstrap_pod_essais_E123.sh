#!/bin/bash
# Bootstrap du pod pour les essais E1 (InfiniteTalk multi-locuteurs, Wan 2.1), E2 (Wan 2.2 I2V trois samplers)
# et E3 (LTX-2.5 I2V) — 23 août 2026. Disque conteneur >= 200 Go (DISK_GB=250 à la création).
# ComfyUI dernière version (LTX-2.5 est natif), WanVideoWrapper + KJNodes (InfiniteTalk), modèles sur disque conteneur.
set -e
cd /root
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git /root/ComfyUI
cd /root/ComfyUI && pip install -q -r requirements.txt
cd /root/ComfyUI/custom_nodes
git clone --depth 1 https://github.com/kijai/ComfyUI-WanVideoWrapper.git
git clone --depth 1 https://github.com/kijai/ComfyUI-KJNodes.git
pip install -q -r ComfyUI-WanVideoWrapper/requirements.txt
pip install -q -r ComfyUI-KJNodes/requirements.txt
M=/root/ComfyUI/models
mkdir -p $M/diffusion_models $M/text_encoders $M/vae $M/loras $M/clip_vision /root/input /root/output
K=https://huggingface.co/Kijai/WanVideo_comfy/resolve/main
B=https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files
L=https://huggingface.co/lightx2v/Wan2.2-Lightning/resolve/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1
X=https://huggingface.co/Lightricks/LTX-2.5/resolve/main
dl() { curl -sL --retry 3 -o "$1" "$2" || echo "ECHEC $1"; }
# E1 — Wan 2.1 I2V 14B 720p + InfiniteTalk multi (Kijai)
dl $M/diffusion_models/Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors $K/Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors &
dl $M/diffusion_models/Wan2_1-InfiniteTalk-Multi_fp16.safetensors $K/InfiniteTalk/Wan2_1-InfiniteTalk-Multi_fp16.safetensors &
dl $M/text_encoders/umt5-xxl-enc-fp8_e4m3fn.safetensors $K/umt5-xxl-enc-fp8_e4m3fn.safetensors &
dl $M/vae/Wan2_1_VAE_bf16.safetensors $K/Wan2_1_VAE_bf16.safetensors &
dl $M/clip_vision/clip_vision_h.safetensors https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors &
dl $M/loras/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors $K/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors &
# E2 — Wan 2.2 I2V (graphe natif habituel)
dl $M/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors $B/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors &
dl $M/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors $B/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors &
dl $M/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors $B/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors &
dl $M/vae/wan_2.1_vae.safetensors $B/vae/wan_2.1_vae.safetensors &
dl $M/loras/wan2.2_i2v_lightx2v_4steps_high_noise.safetensors $L/high_noise_model.safetensors &
dl $M/loras/wan2.2_i2v_lightx2v_4steps_low_noise.safetensors $L/low_noise_model.safetensors &
# E3 — LTX-2.5 (natif ComfyUI)
dl $M/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors $X/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors &
dl $M/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors $X/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors &
dl $M/vae/ltx-2.5-video-vae-bf16.safetensors $X/vae/ltx-2.5-video-vae-bf16.safetensors &
dl $M/vae/ltx-2.5-audio-vae-bf16.safetensors $X/vae/ltx-2.5-audio-vae-bf16.safetensors &
wait
ls -la $M/diffusion_models $M/text_encoders $M/vae $M/loras $M/clip_vision
cd /root/ComfyUI
nohup python main.py --listen 0.0.0.0 --port 8188 --output-directory /root/output --input-directory /root/input > /root/comfy.log 2>&1 &
sleep 30
tail -5 /root/comfy.log
echo BOOTSTRAP_DONE
