#!/bin/bash
# Bootstrap du pod E7 (23 août 2026) : LTX-2.5 (jeton HF dans HF_TOKEN) + MiniMax H3 I2V, rien d'autre. Disque conteneur 200 Go.
set -e
cd /root
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git /root/ComfyUI
cd /root/ComfyUI && pip install -q -r requirements.txt
M=/root/ComfyUI/models
mkdir -p $M/diffusion_models $M/text_encoders $M/vae $M/loras $M/latent_upscale_models /root/input /root/output
H=https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main
X=https://huggingface.co/Lightricks/LTX-2.5/resolve/main
dl() { curl -sL --retry 3 -o "$1" "$2" || echo "ECHEC $1"; }
dlg() { curl -sL --retry 3 -H "Authorization: Bearer $HF_TOKEN" -o "$1" "$2" || echo "ECHEC $1"; }
dl $M/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors $H/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors &
dl $M/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors $H/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors &
dl $M/vae/minimax_h3_video_vae_fp16.safetensors $H/vae/minimax_h3_video_vae_fp16.safetensors &
dl $M/vae/minimax_h3_audio_vae_fp32.safetensors $H/vae/minimax_h3_audio_vae_fp32.safetensors &
dl $M/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/main/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors &
dlg $M/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors $X/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors &
dlg $M/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors $X/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors &
dlg $M/vae/ltx-2.5-video-vae-bf16.safetensors $X/vae/ltx-2.5-video-vae-bf16.safetensors &
dlg $M/vae/ltx-2.5-audio-vae-bf16.safetensors $X/vae/ltx-2.5-audio-vae-bf16.safetensors &
dlg $M/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors $X/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors &
wait
ls -la $M/diffusion_models $M/text_encoders $M/vae $M/latent_upscale_models | awk '{print $5, $9}'
cd /root/ComfyUI
nohup python main.py --listen 0.0.0.0 --port 8188 --output-directory /root/output --input-directory /root/input > /root/comfy.log 2>&1 &
sleep 30
tail -3 /root/comfy.log
echo BOOTSTRAP_DONE
