#!/usr/bin/env python3
"""Essai E3 (23 août 2026) : LTX-2.3 image-to-video (Lightricks, poids ouverts, natif ComfyUI) sur deux plans sans dialogue,
pour comparer mouvement et tenue du style à Wan 2.2. (LTX-2.5 était prévu : dépôt Hugging Face gated, fichiers vides.)

Graphe = template officiel `video_ltx2_3_i2v.json` (Comfy-Org/workflow_templates) réécrit au format API :
checkpoint dev fp8 + LoRA distillée 0,5, encodeur texte gemma-3-12B fp4, deux passes (demi-résolution, 8 sigmas manuels,
puis upsampler latent x2 et 3 sigmas), audio généré par le modèle (VAE audio du checkpoint), CreateVideo 25 i/s.
Le négatif du template contenait « cartoon, childish » : retiré (notre style EST du cartoon).
L'image d'entrée est pré-redimensionnée en 1280x704 (multiples de 32) ; ResizeImageMaskNode (combo dynamique) est évité.

jobs_e3.json : [{"name","clip","style","image","prompt","negative","seed","length" (8n+1),"width","height","fps"}]
Usage : python run_ltx23_runpod.py submit <url_comfy> <index_csv> <jobs_e3.json> [noms]
"""
import csv
import datetime
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_clips_runpod import http, upload_image, _set_job_id  # noqa: E402

CKPT = "ltx-2.3-22b-dev-fp8.safetensors"
LORA = "ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors"
TE = "gemma_3_12B_it_fp4_mixed.safetensors"
UP = "ltx-2.3-spatial-upscaler-x2-1.1.safetensors"
SIG1 = "1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0"
SIG2 = "0.85, 0.7250, 0.4219, 0.0"


def api_prompt_ltx(j, image_name):
    w, h, fps, n = j.get("width", 1280), j.get("height", 704), j.get("fps", 25), j["length"]
    g = {
        "ckpt": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}},
        "lora": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["ckpt", 0], "lora_name": LORA, "strength_model": 0.5}},
        "te": {"class_type": "LTXAVTextEncoderLoader", "inputs": {"text_encoder": TE, "ckpt_name": CKPT, "device": "default"}},
        "avae": {"class_type": "LTXVAudioVAELoader", "inputs": {"ckpt_name": CKPT}},
        "up": {"class_type": "LatentUpscaleModelLoader", "inputs": {"model_name": UP}},
        "pos": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["te", 0], "text": j["prompt"]}},
        "neg": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["te", 0], "text": j["negative"]}},
        "cond": {"class_type": "LTXVConditioning", "inputs": {"positive": ["pos", 0], "negative": ["neg", 0], "frame_rate": float(fps)}},
        "img": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        "big": {"class_type": "ResizeImagesByLongerEdge", "inputs": {"images": ["img", 0], "longer_edge": 1536}},
        "pre": {"class_type": "LTXVPreprocess", "inputs": {"image": ["big", 0], "img_compression": 18}},
        "lat": {"class_type": "EmptyLTXVLatentVideo", "inputs": {"width": w // 2, "height": h // 2, "length": n, "batch_size": 1}},
        "i2v1": {"class_type": "LTXVImgToVideoInplace", "inputs": {"vae": ["ckpt", 2], "image": ["pre", 0], "latent": ["lat", 0], "strength": 0.7, "bypass": False}},
        "alat": {"class_type": "LTXVEmptyLatentAudio", "inputs": {"frames_number": n, "frame_rate": float(fps), "batch_size": 1, "audio_vae": ["avae", 0]}},
        "cat1": {"class_type": "LTXVConcatAVLatent", "inputs": {"video_latent": ["i2v1", 0], "audio_latent": ["alat", 0]}},
        "n1": {"class_type": "RandomNoise", "inputs": {"noise_seed": j["seed"]}},
        "ks": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "sg1": {"class_type": "ManualSigmas", "inputs": {"sigmas": SIG1}},
        "g1": {"class_type": "CFGGuider", "inputs": {"model": ["lora", 0], "positive": ["cond", 0], "negative": ["cond", 1], "cfg": 1.0}},
        "s1": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["n1", 0], "guider": ["g1", 0], "sampler": ["ks", 0], "sigmas": ["sg1", 0], "latent_image": ["cat1", 0]}},
        "sep1": {"class_type": "LTXVSeparateAVLatent", "inputs": {"av_latent": ["s1", 0]}},
        "ups": {"class_type": "LTXVLatentUpsampler", "inputs": {"samples": ["sep1", 0], "upscale_model": ["up", 0], "vae": ["ckpt", 2]}},
        "i2v2": {"class_type": "LTXVImgToVideoInplace", "inputs": {"vae": ["ckpt", 2], "image": ["pre", 0], "latent": ["ups", 0], "strength": 1.0, "bypass": False}},
        "cat2": {"class_type": "LTXVConcatAVLatent", "inputs": {"video_latent": ["i2v2", 0], "audio_latent": ["sep1", 1]}},
        "crop": {"class_type": "LTXVCropGuides", "inputs": {"positive": ["cond", 0], "negative": ["cond", 1], "latent": ["sep1", 0]}},
        "n2": {"class_type": "RandomNoise", "inputs": {"noise_seed": 42}},
        "sg2": {"class_type": "ManualSigmas", "inputs": {"sigmas": SIG2}},
        "g2": {"class_type": "CFGGuider", "inputs": {"model": ["lora", 0], "positive": ["crop", 0], "negative": ["crop", 1], "cfg": 1.0}},
        "s2": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["n2", 0], "guider": ["g2", 0], "sampler": ["ks", 0], "sigmas": ["sg2", 0], "latent_image": ["cat2", 0]}},
        "sep2": {"class_type": "LTXVSeparateAVLatent", "inputs": {"av_latent": ["s2", 0]}},
        "dec": {"class_type": "VAEDecodeTiled", "inputs": {"samples": ["sep2", 0], "vae": ["ckpt", 2], "tile_size": 768, "overlap": 64, "temporal_size": 4096, "temporal_overlap": 4}},
        "adec": {"class_type": "LTXVAudioVAEDecode", "inputs": {"samples": ["sep2", 1], "audio_vae": ["avae", 0]}},
        "vid": {"class_type": "CreateVideo", "inputs": {"images": ["dec", 0], "fps": float(fps), "audio": ["adec", 0]}},
        "save": {"class_type": "SaveVideo", "inputs": {"video": ["vid", 0], "filename_prefix": f"pilote/{j['style']}/{j['clip']}_{j['style']}", "format": "mp4", "codec": "h264"}},
    }
    return g


def submit(base, index_csv, jobs_path, which=None):
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    if which:
        jobs = [j for j in jobs if j["name"] in set(which.split(","))]
    for j in jobs:
        img = upload_image(base, j["image"])
        g = api_prompt_ltx(j, img)
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", "ltx-2.3-22b-dev-fp8+lora-distill", "", str(round(j["length"] / j.get("fps", 25), 2)), str(j["seed"]), "lance", "",
                                    f"E3 LTX-2.3 i2v deux passes : length={j['length']} {j.get('width', 1280)}x{j.get('height', 704)} {j.get('fps', 25)} i/s"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote", "front": os.environ.get("COMFY_FRONT") == "1"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:1500]); continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], pid)


if __name__ == "__main__":
    if sys.argv[1] == "submit":
        submit(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else None)
