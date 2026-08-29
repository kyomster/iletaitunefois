#!/bin/bash
# Bootstrap LTX-2.5 AVEC le volume réseau monté sur /workspace (bonne pratique S3, 25 août 2026).
#
# Les modèles vivent sur le volume, pas sur le disque conteneur : le premier pod les y dépose (une fois),
# les suivants ne téléchargent plus rien et démarrent en deux minutes. Les sorties sont écrites sur
# /workspace/out, rapatriées par S3 puis supprimées du volume ; tout le réutilisable y reste.
# HF_TOKEN doit être dans l'environnement (dépôt LTX-2.5 gated).
set -e
M=/workspace/models
mkdir -p $M/diffusion_models $M/text_encoders $M/vae $M/latent_upscale_models /workspace/out /workspace/in
X=https://huggingface.co/Lightricks/LTX-2.5/resolve/main
need() { [ ! -s "$1" ] || [ "$(stat -c%s "$1")" -lt 1000000 ]; }
dlg() { if need "$1"; then echo "-> $1"; curl -sL --retry 3 -H "Authorization: Bearer $HF_TOKEN" -o "$1" "$2" || echo "ECHEC $1"; else echo "deja la : $1"; fi; }
dlg $M/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors $X/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors &
dlg $M/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors $X/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors &
dlg $M/vae/ltx-2.5-video-vae-bf16.safetensors $X/vae/ltx-2.5-video-vae-bf16.safetensors &
dlg $M/vae/ltx-2.5-audio-vae-bf16.safetensors $X/vae/ltx-2.5-audio-vae-bf16.safetensors &
dlg $M/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors $X/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors &
cd /root
[ -d /root/ComfyUI ] || git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git /root/ComfyUI
cd /root/ComfyUI && pip install -q -r requirements.txt
wait
# ComfyUI lit les modèles sur le volume
cat > /root/ComfyUI/extra_model_paths.yaml <<'YAML'
runpod_volume:
  base_path: /workspace/models/
  diffusion_models: diffusion_models
  text_encoders: text_encoders
  vae: vae
  latent_upscale_models: latent_upscale_models
  loras: loras
YAML
ls -la $M/diffusion_models $M/text_encoders $M/vae $M/latent_upscale_models | awk '{print $5, $9}'
nohup python main.py --listen 0.0.0.0 --port 8188 --output-directory /workspace/out --input-directory /workspace/in > /root/comfy.log 2>&1 &
sleep 30
tail -3 /root/comfy.log
echo BOOTSTRAP_DONE
