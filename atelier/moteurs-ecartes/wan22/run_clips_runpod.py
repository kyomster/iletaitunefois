#!/usr/bin/env python3
"""Soumet les jobs vidéo du pilote à un ComfyUI (pod RunPod) par son API HTTP, et rapatrie les résultats.

Graphes (atelier/moteurs-ecartes/VERDICTS.md, Wan 2.2, valeurs du workflow de référence lightx2v) :
  UNETLoader(high) -> LoraLoaderModelOnly(LightX2V high) -> ModelSamplingSD3(shift 5) -> KSamplerAdvanced(steps 4, 0->2, add_noise)
  UNETLoader(low)  -> LoraLoaderModelOnly(LightX2V low)  -> ModelSamplingSD3(shift 5) -> KSamplerAdvanced(steps 4, 2->4, no noise)
  CLIPLoader(umt5 fp8, wan) -> CLIPTextEncode x2 ; VAELoader(wan 2.1)
  WanImageToVideo (i2v) ou WanFirstLastFrameToVideo (flf2v) 1280x720, length 4n+1
  VAEDecode -> SaveImage (séquence PNG, master) + CreateVideo(16 fps) -> SaveVideo mp4 (aperçu)

Usage :
  python run_clips_runpod.py submit <jobs.json> <url_comfy> <index_csv> [noms séparés par des virgules | all]
  python run_clips_runpod.py poll   <url_comfy> <index_csv>
  python run_clips_runpod.py fetch  <url_comfy> <index_csv> <dossier_sortie>   # aperçus mp4 ; les PNG se rapatrient par scp

L'index CSV est celui du pilote (index-pilote.csv) : une ligne type=clip écrite AU LANCEMENT avec le prompt_id et la graine.
"""
import csv
import datetime
import json
import mimetypes
import sys
import time
import urllib.request
import uuid
from pathlib import Path

MODELS = {
    "high": "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors",
    "low": "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors",
    "lora_high": "wan2.2_i2v_lightx2v_4steps_high_noise.safetensors",
    "lora_low": "wan2.2_i2v_lightx2v_4steps_low_noise.safetensors",
    "clip": "umt5_xxl_fp8_e4m3fn_scaled.safetensors",
    "vae": "wan_2.1_vae.safetensors",
}


def api_prompt(job, start_name, end_name=None):
    """Construit le graphe au format API de ComfyUI pour un job de jobs.json."""
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": MODELS["high"], "weight_dtype": "default"}},
        "2": {"class_type": "UNETLoader", "inputs": {"unet_name": MODELS["low"], "weight_dtype": "default"}},
        "3": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1", 0], "lora_name": MODELS["lora_high"], "strength_model": 1.0}},
        "4": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["2", 0], "lora_name": MODELS["lora_low"], "strength_model": 1.0}},
        "5": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["3", 0], "shift": 5.0}},
        "6": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["4", 0], "shift": 5.0}},
        "7": {"class_type": "CLIPLoader", "inputs": {"clip_name": MODELS["clip"], "type": "wan", "device": "default"}},
        "8": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": job["prompt"]}},
        "9": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": job["negative"]}},
        "10": {"class_type": "VAELoader", "inputs": {"vae_name": MODELS["vae"]}},
        "11": {"class_type": "LoadImage", "inputs": {"image": start_name}},
        "14": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["5", 0], "add_noise": "enable", "noise_seed": job["seed"], "steps": 4, "cfg": 1.0,
                                                            "sampler_name": "euler", "scheduler": "simple", "start_at_step": 0, "end_at_step": 2,
                                                            "return_with_leftover_noise": "enable", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["12", 2]}},
        "15": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["6", 0], "add_noise": "disable", "noise_seed": job["seed"], "steps": 4, "cfg": 1.0,
                                                            "sampler_name": "euler", "scheduler": "simple", "start_at_step": 2, "end_at_step": 4,
                                                            "return_with_leftover_noise": "disable", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["14", 0]}},
        "16": {"class_type": "VAEDecode", "inputs": {"samples": ["15", 0], "vae": ["10", 0]}},
        "17": {"class_type": "SaveImage", "inputs": {"images": ["16", 0], "filename_prefix": f"pilote/{job['style']}/{job['clip']}_{job['style']}/frame"}},
        "18": {"class_type": "CreateVideo", "inputs": {"images": ["16", 0], "fps": 16.0}},
        "19": {"class_type": "SaveVideo", "inputs": {"video": ["18", 0], "filename_prefix": f"pilote/{job['style']}/{job['clip']}_{job['style']}", "format": "mp4", "codec": "h264"}},
    }
    base = {"positive": ["8", 0], "negative": ["9", 0], "vae": ["10", 0], "width": 1280, "height": 720, "length": job["length"], "batch_size": 1, "start_image": ["11", 0]}
    if job["mode"] == "flf2v":
        g["13"] = {"class_type": "LoadImage", "inputs": {"image": end_name}}
        g["12"] = {"class_type": "WanFirstLastFrameToVideo", "inputs": {**base, "end_image": ["13", 0]}}
    else:
        g["12"] = {"class_type": "WanImageToVideo", "inputs": base}
    return g


def http(url, method="GET", data=None, headers=None, timeout=120):
    h = {"User-Agent": "curl/8.0"}  # le proxy RunPod renvoie 403 à l'agent python par défaut
    h.update(headers or {})
    req = urllib.request.Request(url, method=method, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def upload_image(base, path):
    path = Path(path)
    boundary = uuid.uuid4().hex
    ctype = mimetypes.guess_type(str(path))[0] or "image/png"
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{path.name}\"\r\nContent-Type: {ctype}\r\n\r\n").encode() + path.read_bytes() + \
           (f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--{boundary}--\r\n").encode()
    res = json.loads(http(f"{base}/upload/image", "POST", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return res["name"]


def submit(jobs_path, base, index_csv, which):
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    if which != "all":
        wanted = set(which.split(","))
        jobs = [j for j in jobs if j["name"] in wanted]
    uploaded = {}
    for j in jobs:
        for key in ("start_image", "end_image"):
            p = j.get(key)
            if p and p not in uploaded:
                uploaded[p] = upload_image(base, p)
    rows = []
    for j in jobs:
        g = api_prompt(j, uploaded[j["start_image"]], uploaded.get(j.get("end_image")) if j.get("end_image") else None)
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        # ligne d'index AVANT le lancement
        row = [ts, j["clip"], j["style"], "clip", "wan2.2-i2v-a14b-fp8+lightx2v", "", str(j["duration_s"]), str(j["seed"]), "lance", "", f"{j['mode']} length={j['length']} runpod style={j.get('video_style', 'fiche')} gabarit={j.get('presence', 'v1')}"]
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(row)
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], res)
            continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], j["mode"], pid)
        rows.append((j["name"], pid))
    return rows


def _set_job_id(index_csv, clip, style, pid):
    rows = list(csv.reader(open(index_csv, encoding="utf-8", newline="")))
    for r in rows[1:]:
        if r[1] == clip and r[2] == style and r[3] == "clip" and r[8] == "lance" and not r[5]:
            r[5] = pid; r[8] = "soumis"; break
    csv.writer(open(index_csv, "w", newline="", encoding="utf-8")).writerows(rows)


def poll(base, index_csv):
    hist = json.loads(http(f"{base}/history", timeout=60))
    rows = list(csv.reader(open(index_csv, encoding="utf-8", newline="")))
    done = 0
    for r in rows[1:]:
        if r[3] == "clip" and r[8] == "soumis" and r[5] in hist:
            h = hist[r[5]]
            st = h.get("status", {})
            if st.get("completed"):
                outs = h.get("outputs", {})
                mp4 = next((o["filename"] for k in outs for o in outs[k].get("images", []) + outs[k].get("video", []) + outs[k].get("gifs", []) if str(o.get("filename", "")).endswith(".mp4")), "")
                r[8] = "rendu"; r[9] = f"clips-runpod/{r[2]}/{r[1]}_{r[2]}"; r[10] += f" ; mp4={mp4}"
                done += 1
            elif st.get("status_str") == "error":
                r[8] = "erreur"; r[10] += " ; " + str(st.get("messages", ""))[:200]
    csv.writer(open(index_csv, "w", newline="", encoding="utf-8")).writerows(rows)
    q = json.loads(http(f"{base}/queue", timeout=60))
    print(f"rendus maintenant: {done} ; en cours: {len(q.get('queue_running', []))} ; en attente: {len(q.get('queue_pending', []))}")


def fetch(base, index_csv, out_dir):
    hist = json.loads(http(f"{base}/history", timeout=60))
    rows = list(csv.reader(open(index_csv, encoding="utf-8", newline="")))
    for r in rows[1:]:
        if r[3] == "clip" and r[8] == "rendu" and r[5] in hist:
            outs = hist[r[5]].get("outputs", {})
            for k in outs:
                for o in outs[k].get("video", []) + outs[k].get("images", []) + outs[k].get("gifs", []):
                    fn = o.get("filename", "")
                    if fn.endswith(".mp4"):
                        sub = o.get("subfolder", "")
                        data = http(f"{base}/view?filename={urllib.request.quote(fn)}&subfolder={urllib.request.quote(sub)}&type=output", timeout=300)
                        dest = Path(out_dir) / r[2] / f"{r[1]}_{r[2]}.mp4"
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(data)
                        print(dest, len(data))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "submit":
        submit(sys.argv[2], sys.argv[3].rstrip("/"), sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "all")
    elif cmd == "poll":
        poll(sys.argv[2].rstrip("/"), sys.argv[3])
    elif cmd == "fetch":
        fetch(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4])
