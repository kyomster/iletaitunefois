#!/usr/bin/env python3
"""Essai E4 (23 août 2026, demandé par Guillaume) : MiniMax H3 (poids ouverts, natif ComfyUI >= 0.30) en I2V et en R2V.

H3 est omni-modal : il génère la vidéo ET l'audio (voix comprises) en une passe, 24 i/s, 1344x768 natif.
  * I2V  : `MiniMaxH3ImageToVideo` (first_frame = image clé, le prompt décrit l'action et les répliques)
  * R2V  : `MiniMaxH3ReferenceToVideo` (ref_images = image clé, ref_audios = nos répliques ElevenLabs, le prompt cite
           <Picture 1> / <Audio 1> / <Audio 2> comme dans le template officiel)
Graphes = templates `video_minimax_h3_i2v.json` / `video_minimax_h3_r2v.json` (Comfy-Org/workflow_templates) au format API.
Longueur en images : max(5, round(s*24)) arrondi au 17k+5 supérieur (grille temporelle de H3).

jobs_e4.json : [{"name","clip","style","mode":"i2v"|"r2v","image","audios":[...] (r2v),"prompt","seed","seconds","turbo":true}]
Usage : python run_minimax_h3_runpod.py submit <url_comfy> <index_csv> <jobs_e4.json> [noms]
"""
import csv
import datetime
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from comfy_client import http, upload_image, _set_job_id  # noqa: E402

M = {"i2v": "minimax_h3_fl2va_pruned_int8_convrot.safetensors", "r2v": "minimax_h3_ref2va_pruned_int8_convrot.safetensors",
     "clip": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "vae": "minimax_h3_video_vae_fp16.safetensors", "avae": "minimax_h3_audio_vae_fp32.safetensors",
     "lora_i2v": "minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors", "lora_r2v": "minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors"}


def h3_length(seconds):
    n = max(5, round(seconds * 24))
    return n + (5 - (n % 17)) % 17


def api_prompt_h3(j, image_name, audio_names):
    mode = j["mode"]
    turbo = j.get("turbo", True)
    steps = (8 if mode == "i2v" else 4) if turbo else 20
    n = h3_length(j["seconds"])
    w, h = j.get("width", 1344), j.get("height", 768)
    g = {
        "unet": {"class_type": "UNETLoader", "inputs": {"unet_name": M[mode], "weight_dtype": "default"}},
        "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": M["clip"], "type": "minimax", "device": "default"}},
        "vae": {"class_type": "VAELoader", "inputs": {"vae_name": M["vae"]}},
        "avae": {"class_type": "VAELoader", "inputs": {"vae_name": M["avae"]}},
        "img": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        "noise": {"class_type": "RandomNoise", "inputs": {"noise_seed": j["seed"]}},
        "ks": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "res_multistep"}},
        "dec": {"class_type": "VAEDecode", "inputs": {"samples": ["samp", 0], "vae": ["vae", 0]}},
        "adec": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["samp", 0], "vae": ["avae", 0]}},
        "vid": {"class_type": "CreateVideo", "inputs": {"images": ["dec", 0], "fps": 24.0, "audio": ["adec", 0]}},
        "save": {"class_type": "SaveVideo", "inputs": {"video": ["vid", 0], "filename_prefix": f"pilote/{j['style']}/{j['clip']}_{j['style']}", "format": "mp4", "codec": "h264"}},
    }
    model = ["unet", 0]
    if turbo:
        g["lora"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"model": model, "lora_name": M["lora_" + mode], "strength_model": 1.0}}
        model = ["lora", 0]
    if mode == "i2v":
        g["cond"] = {"class_type": "MiniMaxH3ImageToVideo", "inputs": {"clip": ["clip", 0], "vae": ["vae", 0], "prompt": j["prompt"], "width": w, "height": h, "length": n, "first_frame": ["img", 0]}}
    else:
        inputs = {"clip": ["clip", 0], "vae": ["vae", 0], "audio_vae": ["avae", 0], "prompt": j["prompt"], "width": w, "height": h, "length": n,
                  "ref_image_size": j.get("ref_image_size", "match"), "ref_images.ref_image_0": ["img", 0]}
        for k, a in enumerate(audio_names):
            g[f"aud{k}"] = {"class_type": "LoadAudio", "inputs": {"audio": a}}
            inputs[f"ref_audios.ref_audio_{k}"] = [f"aud{k}", 0]
        g["cond"] = {"class_type": "MiniMaxH3ReferenceToVideo", "inputs": inputs}
    g["guider"] = {"class_type": "BasicGuider", "inputs": {"model": model, "conditioning": ["cond", 0]}}
    g["sched"] = {"class_type": "BasicScheduler", "inputs": {"model": model, "scheduler": "simple", "steps": steps, "denoise": 1.0}}
    g["samp"] = {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["noise", 0], "guider": ["guider", 0], "sampler": ["ks", 0], "sigmas": ["sched", 0], "latent_image": ["cond", 1]}}
    return g, n, steps


def submit(base, index_csv, jobs_path, which=None):
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    if which:
        jobs = [j for j in jobs if j["name"] in set(which.split(","))]
    for j in jobs:
        img = upload_image(base, j["image"])
        audios = [upload_image(base, a) for a in j.get("audios", [])]
        g, n, steps = api_prompt_h3(j, img, audios)
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", f"minimax-h3-{j['mode']}-int8" + ("+turbo" if j.get("turbo", True) else ""), "", str(round(n / 24, 2)), str(j["seed"]), "lance", "",
                                    f"E4 minimax h3 {j['mode']} : length={n} steps={steps} 1344x768 24 i/s audios={len(audios)}"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote", "front": os.environ.get("COMFY_FRONT") == "1"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:2000]); continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], pid, "length", n, "steps", steps)


if __name__ == "__main__":
    if sys.argv[1] == "submit":
        submit(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else None)
