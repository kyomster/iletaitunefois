set -e
cd /root
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git /root/ComfyUI
cd /root/ComfyUI && pip install -q -r requirements.txt
mkdir -p /root/wan22/diffusion_models /root/wan22/text_encoders /root/wan22/vae /root/wan22/loras /root/input /root/output
cd /root/wan22
B=https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files
L=https://huggingface.co/lightx2v/Wan2.2-Lightning/resolve/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1
curl -sL -o diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors $B/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors &
curl -sL -o diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors $B/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors &
curl -sL -o text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors $B/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors &
curl -sL -o vae/wan_2.1_vae.safetensors $B/vae/wan_2.1_vae.safetensors &
curl -sL -o loras/wan2.2_i2v_lightx2v_4steps_high_noise.safetensors $L/high_noise_model.safetensors &
curl -sL -o loras/wan2.2_i2v_lightx2v_4steps_low_noise.safetensors $L/low_noise_model.safetensors &
curl -sL -o diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors $B/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors &
mkdir -p audio_encoders && curl -sL -o audio_encoders/wav2vec2_large_english_fp16.safetensors $B/audio_encoders/wav2vec2_large_english_fp16.safetensors &
wait
cd /root/ComfyUI
mkdir -p /root/ComfyUI/models/audio_encoders; for d in diffusion_models text_encoders vae loras audio_encoders; do for f in /root/wan22/$d/*; do ln -sf "$f" "models/$d/$(basename $f)"; done; done
nohup python main.py --listen 0.0.0.0 --port 8188 --output-directory /root/output --input-directory /root/input > /root/comfy.log 2>&1 &
sleep 20
echo BOOTSTRAP_DONE
