#!/bin/bash
# Bootstrap du pod E8 (23 août 2026) : LTX-2.5 (jeton HF) + LTX-2.3 (miroirs ouverts) + ID-LoRA talkvid, pour
# les essais « voix cohérentes » (IA2V audio gelé, LTXVReferenceAudio). Disque conteneur 200 Go. HF_TOKEN dans l'env.
set -e
cd /root
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git /root/ComfyUI
cd /root/ComfyUI && pip install -q -r requirements.txt
M=/root/ComfyUI/models
mkdir -p $M/diffusion_models $M/text_encoders $M/vae $M/loras $M/latent_upscale_models $M/checkpoints /root/input /root/output
X=https://huggingface.co/Lightricks/LTX-2.5/resolve/main
dl() { curl -sL --retry 3 -o "$1" "$2" || echo "ECHEC $1"; }
dlg() { curl -sL --retry 3 -H "Authorization: Bearer $HF_TOKEN" -o "$1" "$2" || echo "ECHEC $1"; }
# LTX-2.5
dlg $M/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors $X/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors &
dlg $M/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors $X/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors &
dlg $M/vae/ltx-2.5-video-vae-bf16.safetensors $X/vae/ltx-2.5-video-vae-bf16.safetensors &
dlg $M/vae/ltx-2.5-audio-vae-bf16.safetensors $X/vae/ltx-2.5-audio-vae-bf16.safetensors &
dlg $M/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors $X/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors &
# LTX-2.3 (repli ID-LoRA) + ID-LoRA
dl $M/checkpoints/ltx-2.3-22b-dev-fp8.safetensors https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors &
dl $M/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors &
dl $M/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors &
dl $M/latent_upscale_models/ltx-2.3-spatial-upscaler-x2-1.1.safetensors https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors &
dl $M/loras/ltx-2.3-id-lora-talkvid-3k.safetensors https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-id-lora-talkvid-3k.safetensors &
wait
ls -la $M/diffusion_models $M/checkpoints $M/text_encoders $M/vae $M/loras $M/latent_upscale_models | awk '{print $5, $9}'
cd /root/ComfyUI
nohup python main.py --listen 0.0.0.0 --port 8188 --output-directory /root/output --input-directory /root/input > /root/comfy.log 2>&1 &
sleep 30
tail -3 /root/comfy.log
echo BOOTSTRAP_DONE
