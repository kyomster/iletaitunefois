#!/usr/bin/env python3
"""Essai E2 (23 août 2026) : Wan 2.2 I2V avec TROIS samplers au lieu de deux, contre les plans figés du LoRA LightX2V.

Bonne pratique communautaire (discussions « bad motion » du dépôt lightx2v/Wan2.2-Lightning) : le premier pas du
modèle haut-bruit se fait SANS LoRA à cfg 3,5 (c'est lui qui décide du mouvement), puis le haut-bruit avec LoRA
(force 0,8), puis le bas-bruit avec LoRA (force 1, cfg 1). Ici : 8 pas au total, 0→1 sans LoRA, 1→4 haut+LoRA, 4→8 bas+LoRA.

Usage : python run_e2_trois_samplers.py submit <jobs.json> <url_comfy> <index_csv> <noms séparés par des virgules>
        (poll / fetch : ceux de run_clips_runpod.py ; le clip sort sous <clip>-3s_<style>.mp4)
"""
import csv
import os
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_clips_runpod import MODELS, http, upload_image, _set_job_id  # noqa: E402


def api_prompt_3s(job, start_name, steps=8, cut1=1, cut2=4, cfg0=3.5, lora_high=0.8):
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": MODELS["high"], "weight_dtype": "default"}},
        "2": {"class_type": "UNETLoader", "inputs": {"unet_name": MODELS["low"], "weight_dtype": "default"}},
        "3": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1", 0], "lora_name": MODELS["lora_high"], "strength_model": lora_high}},
        "4": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["2", 0], "lora_name": MODELS["lora_low"], "strength_model": 1.0}},
        "5": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["3", 0], "shift": 5.0}},
        "5b": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 5.0}},
        "6": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["4", 0], "shift": 5.0}},
        "7": {"class_type": "CLIPLoader", "inputs": {"clip_name": MODELS["clip"], "type": "wan", "device": "default"}},
        "8": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": job["prompt"]}},
        "9": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": job["negative"]}},
        "10": {"class_type": "VAELoader", "inputs": {"vae_name": MODELS["vae"]}},
        "11": {"class_type": "LoadImage", "inputs": {"image": start_name}},
        "12": {"class_type": "WanImageToVideo", "inputs": {"positive": ["8", 0], "negative": ["9", 0], "vae": ["10", 0], "width": 1280, "height": 720,
                                                           "length": job["length"], "batch_size": 1, "start_image": ["11", 0]}},
        "13": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["5b", 0], "add_noise": "enable", "noise_seed": job["seed"], "steps": steps, "cfg": cfg0,
                                                            "sampler_name": "euler", "scheduler": "simple", "start_at_step": 0, "end_at_step": cut1,
                                                            "return_with_leftover_noise": "enable", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["12", 2]}},
        "14": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["5", 0], "add_noise": "disable", "noise_seed": job["seed"], "steps": steps, "cfg": 1.0,
                                                            "sampler_name": "euler", "scheduler": "simple", "start_at_step": cut1, "end_at_step": cut2,
                                                            "return_with_leftover_noise": "enable", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["13", 0]}},
        "15": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["6", 0], "add_noise": "disable", "noise_seed": job["seed"], "steps": steps, "cfg": 1.0,
                                                            "sampler_name": "euler", "scheduler": "simple", "start_at_step": cut2, "end_at_step": steps,
                                                            "return_with_leftover_noise": "disable", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["14", 0]}},
        "16": {"class_type": "VAEDecode", "inputs": {"samples": ["15", 0], "vae": ["10", 0]}},
        "18": {"class_type": "CreateVideo", "inputs": {"images": ["16", 0], "fps": 16.0}},
        "19": {"class_type": "SaveVideo", "inputs": {"video": ["18", 0], "filename_prefix": f"pilote/{job['style']}/{job['clip']}-3s_{job['style']}", "format": "mp4", "codec": "h264"}},
    }
    return g


def submit(jobs_path, base, index_csv, which):
    jobs = [j for j in json.load(open(jobs_path, encoding="utf-8")) if j["name"] in set(which.split(","))]
    for j in jobs:
        img = upload_image(base, j["start_image"])
        cfg0 = float(os.environ.get("E2_CFG0", "3.5")); suffix = os.environ.get("E2_SUFFIX", "-3s")
        g = api_prompt_3s(j, img, cfg0=cfg0)
        g["19"]["inputs"]["filename_prefix"] = f"pilote/{j['style']}/{j['clip']}{suffix}_{j['style']}"
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        clip = j["clip"] + suffix
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, clip, j["style"], "clip", "wan2.2-i2v-a14b-fp8+lightx2v", "", str(j["duration_s"]), str(j["seed"]), "lance", "",
                                    f"E2 trois samplers : 8 pas, 0-1 sans LoRA cfg {cfg0}, 1-4 haut LoRA 0.8, 4-8 bas LoRA 1 ; length={j['length']}"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:800]); continue
        _set_job_id(index_csv, clip, j["style"], pid)
        print(j["name"], "->", clip, pid)


if __name__ == "__main__":
    if sys.argv[1] == "submit":
        submit(sys.argv[2], sys.argv[3].rstrip("/"), sys.argv[4], sys.argv[5])
