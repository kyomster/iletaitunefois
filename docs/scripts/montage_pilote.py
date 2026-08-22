#!/usr/bin/env python3
"""Montage de comparaison du pilote : les 16 clips d'un style bout à bout, plans FIXE tenus, 1280x720 16 im/s.

Ordre du scénario : 1a-1..4, 1b-1..3, P02 (10 s), P03 (12 s), 4a-1..3, 4b-1..3, 5-1..3.
Les mouvements de caméra des plans FIXE (travelling, zoom) se font au montage final, pas ici : on juge la continuité.

Depuis le 22 août 2026 (demande de Guillaume : pas de synchro labiale ne veut pas dire bouches immobiles) :
  * si un clip « parlant » P02-talk / P03-talk existe pour le style, il remplace l'image fixe, bouclé sur la durée du plan ;
  * si un dossier audio est donné, les répliques ElevenLabs sont posées sur P02 et P03, identiques pour les trois styles :
    BADAUD1 à +1,0 s, BADAUD2 0,6 s après la fin de BADAUD1 ; AIDE à +1,0 s, GARNERIN 0,8 s après la fin de AIDE.

Usage : python montage_pilote.py <dossier_clips> <dossier_images_2752> <style> <sortie.mp4> [<dossier_audio>]
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ORDRE = [("P1a-1", None), ("P1a-2", None), ("P1a-3", None), ("P1a-4", None),
         ("P1b-1", None), ("P1b-2", None), ("P1b-3", None),
         ("P02", 10.0), ("P03", 12.0),
         ("P4a-1", None), ("P4a-2", None), ("P4a-3", None),
         ("P4b-1", None), ("P4b-2", None), ("P4b-3", None),
         ("P5-1", None), ("P5-2", None), ("P5-3", None)]
ENC = ["-vf", "scale=1280:720,fps=16,format=yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-an"]
REPLIQUES = {"P02": [("S01E01_P02_BADAUD1.mp3", 1.0, None), ("S01E01_P02_BADAUD2.mp3", 0.6, "S01E01_P02_BADAUD1.mp3")],
             "P03": [("S01E01_P03_AIDE.mp3", 1.0, None), ("S01E01_P03_GARNERIN.mp3", 0.8, "S01E01_P03_AIDE.mp3")]}


def duree(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip())


def main():
    clips, images, style, out = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
    audio = Path(sys.argv[5]) if len(sys.argv) > 5 else None
    tmp = Path(tempfile.mkdtemp(prefix="montage_"))
    parts, t, starts = [], 0.0, {}
    for name, hold in ORDRE:
        dst = tmp / f"{name}.mp4"
        talk = clips / style / f"{name}-talk_{style}.mp4"
        # sous-clips recalés sur le mouvement (align_dialogue_audio.py) s'ils existent, sinon les bruts
        aligned = clips / "_aligned"
        offsets = json.load(open(aligned / f"offsets_{style}.json")) if (aligned / f"offsets_{style}.json").exists() else {}
        subs = [(aligned / style / f"{name}-{k}_{style}.mp4") if (aligned / style / f"{name}-{k}_{style}.mp4").exists() else clips / style / f"{name}-{k}_{style}.mp4" for k in (1, 2, 3, 4)]
        # S2V (bouche pilotée par la voix, 22 août 2026) : si P02-2s2v / P02-3s2v existent, ils remplacent les sous-clips
        # des locuteurs et la réplique démarre avec eux (décalage 0)
        for k in (2, 3):
            s2v = clips / style / f"{name}-{k}s2v_{style}.mp4"
            if s2v.exists():
                subs[k - 1] = s2v
                offsets[f"{name}-{k}"] = 0.0
        if hold is None:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(clips / style / f"{name}_{style}.mp4"), *ENC, str(dst)], check=True)
        elif all(s.exists() for s in subs):  # dialogue découpé par locuteur : quatre sous-clips enchaînés
            sub_lst = tmp / f"{name}_subs.txt"
            encoded = []
            for k, s in enumerate(subs, 1):
                e = tmp / f"{name}-{k}.mp4"
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(s), *ENC, str(e)], check=True)
                encoded.append(e)
            sub_lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in encoded), encoding="utf-8")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(sub_lst), "-c", "copy", str(dst)], check=True)
            # réplique du locuteur 1 au début du mouvement mesuré dans le sous-clip 2 (offsets), sinon 0,3 s après son début ; idem locuteur 2 / sous-clip 3
            starts[f"{name}/2"] = duree(encoded[0]) + offsets.get(f"{name}-2", 0.3)
            starts[f"{name}/3"] = duree(encoded[0]) + duree(encoded[1]) + offsets.get(f"{name}-3", 0.3)
        elif talk.exists():  # clip parlant bouclé sur la durée du plan
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", str(talk), "-t", str(hold), *ENC, str(dst)], check=True)
        else:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(hold), "-i", str(images / style / f"{name}_{style}.png"), *ENC, str(dst)], check=True)
        starts[name] = t
        t += duree(dst)
        parts.append(dst)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
    silent = tmp / "silent.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(silent)], check=True)
    out.parent.mkdir(parents=True, exist_ok=True)
    if audio and all((audio / f).exists() for plan in REPLIQUES for f, _, _ in REPLIQUES[plan]):
        ins, filt, labels = ["-i", str(silent)], [], []
        i = 1
        for plan, reps in REPLIQUES.items():
            cursor = starts[plan]
            for n_rep, (f, gap, after) in enumerate(reps, 2):
                if f"{plan}/{n_rep}" in starts:      # sous-clips par locuteur : réplique au début du sous-clip du locuteur
                    cursor = starts[plan] + starts[f"{plan}/{n_rep}"]
                else:
                    cursor += gap
                ms = int(cursor * 1000)
                ins += ["-i", str(audio / f)]
                filt.append(f"[{i}]adelay={ms}|{ms}[a{i}]"); labels.append(f"[a{i}]")
                cursor += duree(audio / f)
                i += 1
        filt.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0,apad[a]")  # apad : l'audio dure autant que la vidéo
        subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(filt), "-map", "0:v", "-map", "[a]",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", str(out)], check=True)
    else:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(silent), "-c", "copy", str(out)], check=True)
    print(f"{out} : {duree(out):.1f} s ; P02 à {starts['P02']:.1f} s, P03 à {starts['P03']:.1f} s")


if __name__ == "__main__":
    main()
