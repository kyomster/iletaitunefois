#!/bin/bash
# Bootstrap du pod pour la 2e série d'essais (23 août 2026) : InfiniteTalk (P03 v4, B audio_scale), LTX-2.5 (jeton HF requis),
# MiniMax H3 (test anglais). Pas de Wan 2.2 cette fois. Disque conteneur 250 Go. HF_TOKEN doit être dans l'environnement.
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
mkdir -p $M/diffusion_models $M/text_encoders $M/vae $M/loras $M/clip_vision $M/latent_upscale_models /root/input /root/output
K=https://huggingface.co/Kijai/WanVideo_comfy/resolve/main
H=https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main
X=https://huggingface.co/Lightricks/LTX-2.5/resolve/main
dl() { curl -sL --retry 3 -o "$1" "$2" || echo "ECHEC $1"; }
dlg() { curl -sL --retry 3 -H "Authorization: Bearer $HF_TOKEN" -o "$1" "$2" || echo "ECHEC $1"; }
# InfiniteTalk
dl $M/diffusion_models/Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors $K/Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors &
dl $M/diffusion_models/Wan2_1-InfiniteTalk-Multi_fp16.safetensors $K/InfiniteTalk/Wan2_1-InfiniteTalk-Multi_fp16.safetensors &
dl $M/text_encoders/umt5-xxl-enc-fp8_e4m3fn.safetensors $K/umt5-xxl-enc-fp8_e4m3fn.safetensors &
dl $M/vae/Wan2_1_VAE_bf16.safetensors $K/Wan2_1_VAE_bf16.safetensors &
dl $M/clip_vision/clip_vision_h.safetensors https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors &
dl $M/loras/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors $K/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors &
# MiniMax H3 (I2V seulement)
dl $M/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors $H/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors &
dl $M/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors $H/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors &
dl $M/vae/minimax_h3_video_vae_fp16.safetensors $H/vae/minimax_h3_video_vae_fp16.safetensors &
dl $M/vae/minimax_h3_audio_vae_fp32.safetensors $H/vae/minimax_h3_audio_vae_fp32.safetensors &
dl $M/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/main/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors &
# LTX-2.5 (gated : jeton)
dlg $M/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors $X/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors &
dlg $M/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors $X/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors &
dlg $M/vae/ltx-2.5-video-vae-bf16.safetensors $X/vae/ltx-2.5-video-vae-bf16.safetensors &
dlg $M/vae/ltx-2.5-audio-vae-bf16.safetensors $X/vae/ltx-2.5-audio-vae-bf16.safetensors &
dlg $M/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors $X/upscalers/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors &
wait
ls -la $M/diffusion_models $M/text_encoders $M/vae $M/latent_upscale_models | awk '{print $5, $9}'
cd /root/ComfyUI
nohup python main.py --listen 0.0.0.0 --port 8188 --output-directory /root/output --input-directory /root/input > /root/comfy.log 2>&1 &
sleep 30
tail -3 /root/comfy.log
echo BOOTSTRAP_DONE
