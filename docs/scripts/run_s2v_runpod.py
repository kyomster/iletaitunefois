#!/usr/bin/env python3
"""Wan 2.2 S2V (speech-to-video) sur ComfyUI/RunPod : image clé + réplique audio -> clip dont la bouche suit la voix.

Graphe (template officiel ComfyUI « video_wan2_2_14B_s2v », variante 4 étapes) :
  UNETLoader(wan2.2_s2v_14B_fp8_scaled) -> LoraLoaderModelOnly(lightx2v t2v 4 steps high noise) -> ModelSamplingSD3(shift 8)
  CLIPLoader(umt5 fp8) -> CLIPTextEncode x2 ; VAELoader(wan 2.1) ; AudioEncoderLoader(wav2vec2) -> AudioEncoderEncode(LoadAudio)
  WanSoundImageToVideo(positive, negative, vae, audio_encoder_output, ref_image, width, height, length) -> KSampler(4, cfg 1, uni_pc, simple)
  -> VAEDecode -> SaveImage (PNG) + CreateVideo(16 fps, audio) -> SaveVideo mp4
Un rendu par réplique (audio <= 4,8 s = 77 images). Essai du 22 août 2026, décidé par Guillaume : c'est du lipsync.

Usage :
  python run_s2v_runpod.py submit <url_comfy> <index_csv> <jobs_s2v.json>
  python run_s2v_runpod.py poll   <url_comfy> <index_csv>
  python run_s2v_runpod.py fetch  <url_comfy> <index_csv> <dossier_sortie>
jobs_s2v.json : [{"name","clip","style","image" (chemin 720p), "audio" (nom du fichier déjà dans input/ du pod),
                  "prompt","negative","length","seed","width","height","steps","cfg","lora" (true/false)}]
"""
import csv
import datetime
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_clips_runpod import http, upload_image, _set_job_id  # noqa: E402

S2V = {"unet": "wan2.2_s2v_14B_fp8_scaled.safetensors", "lora": "wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors",
       "clip": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "vae": "wan_2.1_vae.safetensors", "audio_enc": "wav2vec2_large_english_fp16.safetensors"}


def api_prompt_s2v(job, image_name):
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": S2V["unet"], "weight_dtype": "default"}},
        "7": {"class_type": "CLIPLoader", "inputs": {"clip_name": S2V["clip"], "type": "wan", "device": "default"}},
        "8": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": job["prompt"]}},
        "9": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": job["negative"]}},
        "10": {"class_type": "VAELoader", "inputs": {"vae_name": S2V["vae"]}},
        "11": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        "20": {"class_type": "AudioEncoderLoader", "inputs": {"audio_encoder_name": S2V["audio_enc"]}},
        "21": {"class_type": "LoadAudio", "inputs": {"audio": job["audio"]}},
        "22": {"class_type": "AudioEncoderEncode", "inputs": {"audio_encoder": ["20", 0], "audio": ["21", 0]}},
        "16": {"class_type": "VAEDecode", "inputs": {"samples": ["14", 0], "vae": ["10", 0]}},
        "17": {"class_type": "SaveImage", "inputs": {"images": ["16", 0], "filename_prefix": f"pilote/{job['style']}/{job['clip']}_{job['style']}/frame"}},
        "18": {"class_type": "CreateVideo", "inputs": {"images": ["16", 0], "fps": 16.0, "audio": ["21", 0]}},
        "19": {"class_type": "SaveVideo", "inputs": {"video": ["18", 0], "filename_prefix": f"pilote/{job['style']}/{job['clip']}_{job['style']}", "format": "mp4", "codec": "h264"}},
    }
    model = ["1", 0]
    if job.get("lora", True):
        g["3"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"model": model, "lora_name": S2V["lora"], "strength_model": 1.0}}
        model = ["3", 0]
    g["5"] = {"class_type": "ModelSamplingSD3", "inputs": {"model": model, "shift": 8.0}}
    g["12"] = {"class_type": "WanSoundImageToVideo", "inputs": {"positive": ["8", 0], "negative": ["9", 0], "vae": ["10", 0], "audio_encoder_output": ["22", 0],
                                                                "ref_image": ["11", 0], "width": job.get("width", 1280), "height": job.get("height", 720),
                                                                "length": job["length"], "batch_size": 1}}
    g["14"] = {"class_type": "KSampler", "inputs": {"model": ["5", 0], "seed": job["seed"], "steps": job.get("steps", 4), "cfg": job.get("cfg", 1.0),
                                                    "sampler_name": "uni_pc", "scheduler": "simple", "denoise": 1.0,
                                                    "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["12", 2]}}
    return g


def submit(base, index_csv, jobs_path):
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    for j in jobs:
        img = upload_image(base, j["image"])
        g = api_prompt_s2v(j, img)
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", "wan2.2-s2v-14b-fp8" + ("+lightx2v" if j.get("lora", True) else ""), "", str(round(j["length"] / 16, 2)), str(j["seed"]), "lance", "", f"s2v audio={j['audio']} length={j['length']} steps={j.get('steps', 4)} cfg={j.get('cfg', 1.0)}"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:500]); continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], pid)


if __name__ == "__main__":
    from run_clips_runpod import poll, fetch
    cmd = sys.argv[1]
    if cmd == "submit":
        submit(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4])
    elif cmd == "poll":
        poll(sys.argv[2].rstrip("/"), sys.argv[3])
    elif cmd == "fetch":
        fetch(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4])
