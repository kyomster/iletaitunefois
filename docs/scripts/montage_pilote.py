#!/usr/bin/env python3
"""Montage de comparaison du pilote : les 16 clips d'un style bout à bout, plans FIXE tenus, 1280x720 16 im/s.

Ordre du scénario : 1a-1..4, 1b-1..3, P02 (10 s, fixe), P03 (12 s, fixe), 4a-1..3, 4b-1..3, 5-1..3.
Les mouvements de caméra des plans FIXE (travelling, zoom) se font au montage final, pas ici : on juge la continuité.

Usage : python montage_pilote.py <dossier_clips> <dossier_images_2752> <style> <sortie.mp4>
  <dossier_clips>/<style>/P1a-1_<style>.mp4 ...   <dossier_images_2752>/<style>/P02_<style>.png ...
"""
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


def main():
    clips, images, style, out = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
    tmp = Path(tempfile.mkdtemp(prefix="montage_"))
    parts = []
    for name, hold in ORDRE:
        if hold is None:
            src = clips / style / f"{name}_{style}.mp4"
            dst = tmp / f"{name}.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", "scale=1280:720,fps=16,format=yuv420p",
                            "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-an", str(dst)], check=True)
        else:
            src = images / style / f"{name}_{style}.png"
            dst = tmp / f"{name}.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(hold), "-i", str(src),
                            "-vf", "scale=1280:720,fps=16,format=yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-an", str(dst)], check=True)
        parts.append(dst)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out)], check=True)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.strip()
    print(f"{out} : {float(dur):.1f} s")


if __name__ == "__main__":
    main()
