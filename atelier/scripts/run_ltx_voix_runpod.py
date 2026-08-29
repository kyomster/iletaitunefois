#!/usr/bin/env python3
"""Essai E8 (23 août 2026) : voix cohérentes avec LTX — deux voies, sur LTX-2.5 (et repli LTX-2.3 pour l'ID-LoRA).

  mode "ia2v"    : image + NOTRE audio (mix ElevenLabs pré-aligné) → vidéo ; l'audio est encodé par le VAE audio et GELÉ
                   (SetLatentNoiseMask avec un SolidMask à 0 : le sampler ne le réécrit pas) puis injecté dans les deux passes
                   via LTXVConcatAVLatent ; euler, CFG vidéo 1 / audio 1. C'est le template officiel « LTX-2.3 Image Audio to Video »
                   transposé sur 2.5 (recette confirmée par la discussion HF Lightricks/LTX-2.5 n° 44).
  mode "idlora"  : LTX-2.5 + ID-LoRA talkvid (entraîné sur 2.3) + LTXVReferenceAudio (référence ~5 s) : la voix est générée au
                   timbre de la référence ; le LoRA et la référence ne s'appliquent qu'à la première passe (comme le template ID LoRA).
  mode "idlora23": même chose sur le checkpoint LTX-2.3 dev fp8 (repli si 2.5 refuse le LoRA).

jobs : [{"name","clip","style","mode","image","audio" (ia2v : mix ; idlora : référence),"prompt","negative","seed","length","width","height","fps"}]
Usage : python run_ltx_voix_runpod.py submit <url_comfy> <index_csv> <jobs.json> [noms]
"""
import csv
import datetime
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "moteurs-ecartes" / "ltx23"))
from comfy_client import http, upload_image, _set_job_id  # noqa: E402
from run_ltx25_runpod import api_prompt_ltx25  # noqa: E402
from run_ltx23_runpod import api_prompt_ltx, CKPT  # noqa: E402

IDLORA = "ltx-2.3-id-lora-talkvid-3k.safetensors"


def graph_ia2v(j, image_name, audio_name):
    g = api_prompt_ltx25(j, image_name)
    n, fps = j["length"], j.get("fps", 24)
    g["aud"] = {"class_type": "LoadAudio", "inputs": {"audio": audio_name}}
    g["trim"] = {"class_type": "TrimAudioDuration", "inputs": {"audio": ["aud", 0], "start_index": 0.0, "duration": round(n / fps, 4)}}
    g["aenc"] = {"class_type": "LTXVAudioVAEEncode", "inputs": {"audio": ["trim", 0], "audio_vae": ["avae", 0]}}
    g["amask"] = {"class_type": "SolidMask", "inputs": {"value": 0.0, "width": j.get("width", 1280), "height": j.get("height", 704)}}
    g["afrozen"] = {"class_type": "SetLatentNoiseMask", "inputs": {"samples": ["aenc", 0], "mask": ["amask", 0]}}
    g["cat1"]["inputs"]["audio_latent"] = ["afrozen", 0]
    g["cat2"]["inputs"]["audio_latent"] = ["afrozen", 0]
    g["ks"]["inputs"]["sampler_name"] = "euler"
    del g["alat"]
    return g


def graph_idlora(j, image_name, audio_name, base="25"):
    if base == "25":
        g = api_prompt_ltx25(j, image_name)
        model0 = ["unet", 0]
    else:
        g = api_prompt_ltx(j, image_name)
        model0 = ["lora", 0]  # checkpoint + LoRA distillée 0,5
    g["aud"] = {"class_type": "LoadAudio", "inputs": {"audio": audio_name}}
    g["idlora"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"model": model0, "lora_name": IDLORA, "strength_model": j.get("idlora_strength", 1.0)}}
    g["refa"] = {"class_type": "LTXVReferenceAudio", "inputs": {"model": ["idlora", 0], "positive": ["cond", 0], "negative": ["cond", 1], "reference_audio": ["aud", 0],
                                                               "audio_vae": ["avae", 0], "identity_guidance_scale": j.get("identity_guidance", 2.0), "start_percent": 0.0, "end_percent": 1.0}}
    # première passe : modèle + conditionnement de référence ; seconde passe : modèle de base
    g["g1"]["inputs"]["model"] = ["refa", 0]; g["g1"]["inputs"]["positive"] = ["refa", 1]; g["g1"]["inputs"]["negative"] = ["refa", 2]
    return g


def submit(base, index_csv, jobs_path, which=None):
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    if which:
        jobs = [j for j in jobs if j["name"] in set(which.split(","))]
    for j in jobs:
        img = upload_image(base, j["image"])
        aud = upload_image(base, j["audio"])
        if j["mode"] == "ia2v":
            g = graph_ia2v(j, img, aud)
        elif j["mode"] == "idlora":
            g = graph_idlora(j, img, aud, "25")
        else:
            g = graph_idlora(j, img, aud, "23")
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", "ltx-2.5" if j["mode"] != "idlora23" else "ltx-2.3", "", str(round(j["length"] / j.get("fps", 24), 2)), str(j["seed"]), "lance", "",
                                    f"E8 {j['mode']} : audio={Path(j['audio']).name} length={j['length']}"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote", "front": os.environ.get("COMFY_FRONT") == "1"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:1500]); continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], pid)


if __name__ == "__main__":
    if sys.argv[1] == "submit":
        submit(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else None)
