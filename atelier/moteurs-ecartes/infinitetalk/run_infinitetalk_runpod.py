#!/usr/bin/env python3
"""Essai E1 (23 août 2026) : plan de dialogue à deux rendu en UN clip par InfiniteTalk multi-locuteurs
(MeiGen, sur Wan 2.1 I2V 14B 720p) — chaque piste audio est liée à un masque de visage, mode « para » avec des
pistes pré-alignées (silence là où l'autre parle), donc l'auditeur n'est pas piloté par la voix de l'autre.

Graphe = l'exemple de Kijai `wanvideo_2_1_14B_I2V_InfiniteTalk_example_03.json` (ComfyUI-WanVideoWrapper) réécrit
au format API, + masques (LoadImageMask x2 -> MaskBatchMulti -> ref_target_masks) + CreateVideo/SaveVideo natifs
(pas de VHS). Signatures vérifiées sur /object_info du pod.

jobs_e1.json : [{"name","clip","style","image" (720p),"masks":[png,png],"audios":[wav,wav],"audio_mix":wav,
                 "num_frames" (4n+1 à 25 i/s),"prompt","negative","seed","steps","shift","scheduler","width","height"}]
Usage : python run_infinitetalk_runpod.py submit <url_comfy> <index_csv> <jobs_e1.json> [noms]
        poll / fetch : run_clips_runpod.py
"""
import csv
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from comfy_client import http, upload_image, _set_job_id  # noqa: E402

M = {"wan": "Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors", "infinitetalk": "Wan2_1-InfiniteTalk-Multi_fp16.safetensors",
     "t5": "umt5-xxl-enc-fp8_e4m3fn.safetensors", "vae": "Wan2_1_VAE_bf16.safetensors", "clip_vision": "clip_vision_h.safetensors",
     "lora": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "wav2vec": "TencentGameMate/chinese-wav2vec2-base"}


def api_prompt_e1(j, image_name, mask_names, audio_names, mix_name):
    w, h = j.get("width", 1280), j.get("height", 720)
    g = {
        "vae": {"class_type": "WanVideoVAELoader", "inputs": {"model_name": M["vae"], "precision": "bf16"}},
        "cv": {"class_type": "CLIPVisionLoader", "inputs": {"clip_name": M["clip_vision"]}},
        "lora": {"class_type": "WanVideoLoraSelect", "inputs": {"lora": M["lora"], "strength": j.get("lora_strength", 1.0), "low_mem_load": False, "merge_loras": True}},
        "mt": {"class_type": "MultiTalkModelLoader", "inputs": {"model": M["infinitetalk"]}},
        "model": {"class_type": "WanVideoModelLoader", "inputs": {"model": M["wan"], "base_precision": "fp16", "quantization": "fp8_e4m3fn", "load_device": "offload_device",
                                                                  "attention_mode": "sdpa", "lora": ["lora", 0], "multitalk_model": ["mt", 0]}},
        "txt": {"class_type": "WanVideoTextEncodeCached", "inputs": {"model_name": M["t5"], "precision": "bf16", "positive_prompt": j["prompt"], "negative_prompt": j["negative"],
                                                                     "quantization": "fp8_e4m3fn", "use_disk_cache": False, "device": "gpu"}},
        "img": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        "cve": {"class_type": "WanVideoClipVisionEncode", "inputs": {"clip_vision": ["cv", 0], "image_1": ["img", 0], "strength_1": 1.0, "strength_2": 1.0, "crop": "center",
                                                                     "combine_embeds": "average", "force_offload": True, "tiles": 0, "ratio": 0.5}},
        "w2v": {"class_type": "DownloadAndLoadWav2VecModel", "inputs": {"model": M["wav2vec"], "base_precision": "fp16", "load_device": "main_device"}},
        "a1": {"class_type": "LoadAudio", "inputs": {"audio": audio_names[0]}},
        "a2": {"class_type": "LoadAudio", "inputs": {"audio": audio_names[1]}},
        "m1": {"class_type": "LoadImageMask", "inputs": {"image": mask_names[0], "channel": "red"}},
        "m2": {"class_type": "LoadImageMask", "inputs": {"image": mask_names[1], "channel": "red"}},
        "mb": {"class_type": "MaskBatchMulti", "inputs": {"inputcount": 2, "mask_1": ["m1", 0], "mask_2": ["m2", 0]}},
        "emb": {"class_type": "MultiTalkWav2VecEmbeds", "inputs": {"wav2vec_model": ["w2v", 0], "audio_1": ["a1", 0], "audio_2": ["a2", 0], "normalize_loudness": True,
                                                                   "num_frames": j["num_frames"], "fps": 25.0, "audio_scale": j.get("audio_scale", 1.0), "audio_cfg_scale": 1.0,
                                                                   "multi_audio_type": "para", "ref_target_masks": ["mb", 0]}},
        "i2v": {"class_type": "WanVideoImageToVideoMultiTalk", "inputs": {"vae": ["vae", 0], "width": w, "height": h, "frame_window_size": 81, "motion_frame": 9,
                                                                          "force_offload": False, "colormatch": "disabled", "start_image": ["img", 0], "tiled_vae": False,
                                                                          "clip_embeds": ["cve", 0], "mode": "infinitetalk", "output_path": ""}},
        "samp": {"class_type": "WanVideoSampler", "inputs": {"model": ["model", 0], "image_embeds": ["i2v", 0], "steps": j.get("steps", 6), "cfg": 1.0, "shift": j.get("shift", 11.0),
                                                             "seed": j["seed"], "force_offload": True, "scheduler": j.get("scheduler", "dpm++_sde"), "riflex_freq_index": 0,
                                                             "text_embeds": ["txt", 0], "multitalk_embeds": ["emb", 0], "rope_function": "comfy"}},
        "pass": {"class_type": "WanVideoPassImagesFromSamples", "inputs": {"samples": ["samp", 0]}},
        "amix": {"class_type": "LoadAudio", "inputs": {"audio": mix_name}},
        "vid": {"class_type": "CreateVideo", "inputs": {"images": ["pass", 0], "fps": 25.0, "audio": ["amix", 0]}},
        "save": {"class_type": "SaveVideo", "inputs": {"video": ["vid", 0], "filename_prefix": f"pilote/{j['style']}/{j['clip']}_{j['style']}", "format": "mp4", "codec": "h264"}},
    }
    return g


def submit(base, index_csv, jobs_path, which=None):
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    if which:
        jobs = [j for j in jobs if j["name"] in set(which.split(","))]
    for j in jobs:
        img = upload_image(base, j["image"])
        masks = [upload_image(base, m) for m in j["masks"]]
        audios = [upload_image(base, a) for a in j["audios"]]   # /upload/image accepte n'importe quel fichier dans input/
        mix = upload_image(base, j["audio_mix"])
        g = api_prompt_e1(j, img, masks, audios, mix)
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        with open(index_csv, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", "wan2.1-i2v-14b-720p-fp8+infinitetalk-multi+lightx2v", "", str(round(j["num_frames"] / 25, 2)), str(j["seed"]), "lance", "",
                                    f"E1 infinitetalk multi : 2 masques, 2 pistes para, frames={j['num_frames']} steps={j.get('steps', 6)} shift={j.get('shift', 11)} audio_scale={j.get('audio_scale', 1.0)}"])
        res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote"}).encode(), {"Content-Type": "application/json"}))
        pid = res.get("prompt_id")
        if not pid:
            print("ERREUR", j["name"], str(res)[:1500]); continue
        _set_job_id(index_csv, j["clip"], j["style"], pid)
        print(j["name"], pid)


if __name__ == "__main__":
    if sys.argv[1] == "submit":
        submit(sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else None)
