#!/usr/bin/env python3
"""Rend les sous-clips de dialogue en chaîne : sous-clip 1 en I2V depuis l'image clé, puis chaque sous-clip suivant
part de la DERNIÈRE IMAGE RENDUE du précédent (continuité dans le même cadrage, sans saut). Les quatre chaînes
(P02 A, P02 B, P03 A, P03 B) avancent en parallèle, étage par étage.

Pourquoi (22 août 2026, 15 h 20) : le FLF2V avec départ = fin = image clé rend des sous-clips quasi figés
(mode d'emploi RunPod, piège n° 8) ; le découpage par locuteur reste, la méthode de raccord change.

Usage : python chain_dialogue_runpod.py <jobs_dialogue.json> <url_comfy> <index_csv> <dossier_sortie>
"""
import csv
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_clips_runpod import api_prompt, upload_image, http, _set_job_id  # noqa: E402


def main():
    jobs = json.load(open(sys.argv[1], encoding="utf-8"))
    base, index_csv, out_dir = sys.argv[2].rstrip("/"), sys.argv[3], Path(sys.argv[4])
    chains = {}
    for j in jobs:
        chains.setdefault((j["bloc"], j["style"]), []).append(j)
    for k in chains:
        chains[k].sort(key=lambda j: j["clip"])
    n_stages = max(len(v) for v in chains.values())
    prev_last = {}  # (bloc, style) -> nom du fichier image de départ du prochain sous-clip (dans input/ du pod)
    for stage in range(n_stages):
        submitted = {}
        for key, subs in chains.items():
            if stage >= len(subs):
                continue
            j = dict(subs[stage]); j["mode"] = "i2v"
            start_name = upload_image(base, j["start_image"]) if stage == 0 else prev_last[key]
            g = api_prompt(j, start_name)
            ts = datetime.datetime.now().isoformat(timespec="seconds")
            with open(index_csv, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([ts, j["clip"], j["style"], "clip", "wan2.2-i2v-a14b-fp8+lightx2v", "", str(j["duration_s"]), str(j["seed"]), "lance", "",
                                        f"i2v length={j['length']} runpod style={j.get('video_style')} gabarit={j.get('presence')} chaine=" + ("cle" if stage == 0 else "derniere image du precedent")])
            res = json.loads(http(f"{base}/prompt", "POST", json.dumps({"prompt": g, "client_id": "pilote"}).encode(), {"Content-Type": "application/json"}))
            pid = res["prompt_id"]
            _set_job_id(index_csv, j["clip"], j["style"], pid)
            submitted[key] = (j, pid)
            print(f"étage {stage + 1} : {j['name']} soumis {pid} (départ {start_name})")
        # attendre la fin de l'étage
        pending = dict(submitted)
        while pending:
            time.sleep(10)
            hist = json.loads(http(f"{base}/history", timeout=60))
            for key, (j, pid) in list(pending.items()):
                h = hist.get(pid)
                if not h or not h.get("status", {}).get("completed"):
                    continue
                outs = h["outputs"]
                pngs = sorted((o for k in outs for o in outs[k].get("images", []) if o.get("filename", "").endswith(".png")), key=lambda o: o["filename"])
                mp4 = next((o for k in outs for o in outs[k].get("video", []) + outs[k].get("images", []) if o.get("filename", "").endswith(".mp4")), None)
                last = pngs[-1]
                # la dernière image rendue devient l'image de départ du sous-clip suivant : on la copie dans input/ via /upload
                data = http(f"{base}/view?filename={urllib.request.quote(last['filename'])}&subfolder={urllib.request.quote(last.get('subfolder', ''))}&type=output", timeout=300)
                tmp = out_dir / "_chain" / f"{j['name']}_last.png"
                tmp.parent.mkdir(parents=True, exist_ok=True); tmp.write_bytes(data)
                prev_last[key] = upload_image(base, tmp)
                if mp4:
                    dest = out_dir / j["style"] / f"{j['clip']}_{j['style']}.mp4"
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(http(f"{base}/view?filename={urllib.request.quote(mp4['filename'])}&subfolder={urllib.request.quote(mp4.get('subfolder', ''))}&type=output", timeout=300))
                rows = list(csv.reader(open(index_csv, encoding="utf-8", newline="")))
                for r in rows[1:]:
                    if r[5] == pid:
                        r[8] = "rendu"; r[9] = f"clips-runpod/{j['style']}/{j['clip']}_{j['style']}"; r[10] += f" ; mp4={mp4['filename'] if mp4 else ''} ; derniere image={last['filename']}"
                csv.writer(open(index_csv, "w", newline="", encoding="utf-8")).writerows(rows)
                print(f"  rendu {j['name']} ; dernière image {last['filename']}")
                del pending[key]
    print("chaînes terminées")


if __name__ == "__main__":
    main()
