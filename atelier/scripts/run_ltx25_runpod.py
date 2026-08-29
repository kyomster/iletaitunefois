#!/usr/bin/env python3
"""Essai E3b (23 août 2026) : LTX-2.5 image-to-video (Lightricks, poids ouverts mais dépôt gated : jeton Hugging Face de Guillaume).

Graphe = template officiel `video_ltx2_5_i2v.json` (Comfy-Org/workflow_templates, sous-graphe « Image to Video (LTX-2.5) »)
réécrit au format API : transformer distillé int8 + encodeur gemma4-12b int8, VAE vidéo + VAE audio, deux passes
(demi-résolution 9 sigmas, upsampler latent x2, 4 sigmas), guider LTXVDualCFGGuider (cfg vidéo 1, audio 1), euler_ancestral,
LTX génère aussi l'audio (dialogue si le prompt le dit). Image pré-redimensionnée en multiples de 32 (1280x704).

jobs : [{"name","clip","style","image","prompt","negative","seed","length" (8n+1),"width","height","fps"}]
Usage : python run_ltx25_runpod.py submit <url_comfy> <index_csv> <jobs.json> [noms]
"""
import csv
import datetime
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_clips_runpod import http, upload_image, _set_job_id  # noqa: E402

UNET = "ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors"
TE = "gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors"
VVAE = "ltx-2.5-video-vae-bf16.safetensors"
AVAE = "ltx-2.5-audio-vae-bf16.safetensors"
UP = "ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors"
SIG1 = "1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0"
SIG2 = "0.85, 0.7250, 0.4219, 0.0"


def api_prompt_ltx25(j, image_name):
    w, h, fps, n = j.get("width", 1280), j.get("height", 704), j.get("fps", 24), j["length"]
    g = {
        "unet": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET, "weight_dtype": "default"}},
        "te": {"class_type": "CLIPLoader", "inputs": {"clip_name": TE, "type": "ltxv", "device": "default"}},
        "vvae": {"class_type": "VAELoader", "inputs": {"vae_name": VVAE}},
        "avae": {"class_type": "VAELoader", "inputs": {"vae_name": AVAE}},
        "up": {"class_type": "LatentUpscaleModelLoader", "inputs": {"model_name": UP}},
        "pos": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["te", 0], "text": j["prompt"]}},
        "neg": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["te", 0], "text": j["negative"]}},
        "cond": {"class_type": "LTXVConditioning", "inputs": {"positive": ["pos", 0], "negative": ["neg", 0], "frame_rate": float(fps)}},
        "img": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        "big": {"class_type": "ResizeImagesByLongerEdge", "inputs": {"images": ["img", 0], "longer_edge": 1536}},
        "pre": {"class_type": "LTXVPreprocess", "inputs": {"image": ["big", 0], "img_compression": 18}},
        "lat": {"class_type": "EmptyLTXVLatentVideo", "inputs": {"width": w // 2, "height": h // 2, "length": n, "batch_size": 1}},
        "i2v1": {"class_type": "LTXVImgToVideoInplace", "inputs": {"vae": ["vvae", 0], "image": ["pre", 0], "latent": ["lat", 0], "strength": 0.7, "bypass": False}},
        "alat": {"class_type": "LTXVEmptyLatentAudio", "inputs": {"frames_number": n, "frame_rate": float(fps), "batch_size": 1, "audio_vae": ["avae", 0]}},
        "cat1": {"class_type": "LTXVConcatAVLatent", "inputs": {"video_latent": ["i2v1", 0], "audio_latent": ["alat", 0]}},
        "n1": {"class_type": "RandomNoise", "inputs": {"noise_seed": j["seed"]}},
        "ks": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler_ancestral"}},
        "sg1": {"class_type": "ManualSigmas", "inputs": {"sigmas": SIG1}},
        "g1": {"class_type": "LTXVDualCFGGuider", "inputs": {"model": ["unet", 0], "positive": ["cond", 0], "negative": ["cond", 1], "video_cfg": 1.0, "audio_cfg": 1.0}},
        "s1": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["n1", 0], "guider": ["g1", 0], "sampler": ["ks", 0], "sigmas": ["sg1", 0], "latent_image": ["cat1", 0]}},
        "sep1": {"class_type": "LTXVSeparateAVLatent", "inputs": {"av_latent": ["s1", 0]}},
        "ups": {"class_type": "LTXVLatentUpsampler", "inputs": {"samples": ["sep1", 0], "upscale_model": ["up", 0], "vae": ["vvae", 0]}},
        "i2v2": {"class_type": "LTXVImgToVideoInplace", "inputs": {"vae": ["vvae", 0], "image": ["pre", 0], "latent": ["ups", 0], "strength": 1.0, "bypass": False}},
        "cat2": {"class_type": "LTXVConcatAVLatent", "inputs": {"video_latent": ["i2v2", 0], "audio_latent": ["sep1", 1]}},
        "n2": {"class_type": "RandomNoise", "inputs": {"noise_seed": 42}},
        "sg2": {"class_type": "ManualSigmas", "inputs": {"sigmas": SIG2}},
        "g2": {"class_type": "LTXVDualCFGGuider", "inputs": {"model": ["unet", 0], "positive": ["cond", 0], "negative": ["cond", 1], "video_cfg": 1.0, "audio_cfg": 1.0}},
        "s2": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["n2", 0], "guider": ["g2", 0], "sampler": ["ks", 0], "sigmas": ["sg2", 0], "latent_image": ["cat2", 0]}},
        "sep2": {"class_type": "LTXVSeparateAVLatent", "inputs": {"av_latent": ["s2", 0]}},
        "dec": {"class_type": "VAEDecodeTiled", "inputs": {"samples": ["sep2", 0], "vae": ["vvae", 0], "tile_size": 512, "overlap": 64, "temporal_size": 64, "temporal_overlap": 16}},
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
        g = api_prompt_ltx25(j, img)
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", "ltx-2.5-22b-distilled-int8", "", str(round(j["length"] / j.get("fps", 24), 2)), str(j["seed"]), "lance", "",
                                    f"E3b LTX-2.5 i2v deux passes : length={j['length']} {j.get('width', 1280)}x{j.get('height', 704)} {j.get('fps', 24)} i/s"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote", "front": os.environ.get("COMFY_FRONT") == "1"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:1500]); continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], pid)


if __name__ == "__main__":
    if sys.argv[1] == "submit":
        submit(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else None)
