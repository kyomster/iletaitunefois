#!/bin/bash
# Bootstrap du pod v7 (24 août 2026) : LTX-2.5 seul (jeton HF dans HF_TOKEN). Disque conteneur 150 Go.
set -e
cd /root
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git /root/ComfyUI
cd /root/ComfyUI && pip install -q -r requirements.txt
M=/root/ComfyUI/models
mkdir -p $M/diffusion_models $M/text_encoders $M/vae $M/latent_upscale_models /root/input /root/output
X=https://huggingface.co/Lightricks/LTX-2.5/resolve/main
dlg() { curl -sL --retry 3 -H "Authorization: Bearer $HF_TOKEN" -o "$1" "$2" || echo "ECHEC $1"; }
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
