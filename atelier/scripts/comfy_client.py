#!/usr/bin/env python3
"""Client HTTP minimal de ComfyUI sur un pod RunPod, partagé par tous les moteurs.

Extrait le 27 août 2026 de `run_clips_runpod.py` (Wan 2.2) pour que les scripts LTX-2.5 et les moteurs
écartés partagent le même code : envoi d'image, soumission d'un graphe au format API, suivi de l'index CSV,
interrogation de la file, rapatriement des mp4 par `/view`.

L'index CSV est celui de l'épisode (`index-pilote.csv`) : une ligne type=clip écrite AU LANCEMENT avec le
prompt_id et la graine — retrouver après coup ce qui a produit quoi est lent et fragile.
"""
import csv
import json
import mimetypes
import urllib.request
import uuid
from pathlib import Path


def http(url, method="GET", data=None, headers=None, timeout=120):
    h = {"User-Agent": "curl/8.0"}  # le proxy RunPod renvoie 403 à l'agent python par défaut
    h.update(headers or {})
    req = urllib.request.Request(url, method=method, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def upload_image(base, path):
    """Téléverse une image dans `input/` du pod et renvoie le nom sous lequel ComfyUI la connaît."""
    path = Path(path)
    boundary = uuid.uuid4().hex
    ctype = mimetypes.guess_type(str(path))[0] or "image/png"
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{path.name}\"\r\nContent-Type: {ctype}\r\n\r\n").encode() + path.read_bytes() + \
           (f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--{boundary}--\r\n").encode()
    res = json.loads(http(f"{base}/upload/image", "POST", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return res["name"]


def submit_graph(base, graph, client_id="atelier", front=False):
    """Poste un graphe au format API ; renvoie le prompt_id ou None (la réponse est alors affichée)."""
    res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": graph, "client_id": client_id, "front": front}).encode(),
                          {"Content-Type": "application/json"}))
    pid = res.get("prompt_id")
    if not pid:
        print("ERREUR", str(res)[:1500])
    return pid


def _set_job_id(index_csv, clip, style, pid):
    rows = list(csv.reader(open(index_csv, encoding="utf-8", newline="")))
    for r in rows[1:]:
        if r[1] == clip and r[2] == style and r[3] == "clip" and r[8] == "lance" and not r[5]:
            r[5] = pid; r[8] = "soumis"; break
    csv.writer(open(index_csv, "w", newline="", encoding="utf-8")).writerows(rows)


def poll(base, index_csv):
    """Met à jour l'index : les jobs soumis dont l'historique dit qu'ils sont rendus passent en `rendu`."""
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
    """Rapatrie par `/view` les mp4 des jobs `rendu`. Préférer `runpod_s3.py dl` quand les sorties sont sur le volume."""
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
