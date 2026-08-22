#!/usr/bin/env python3
"""Recale les répliques sur le mouvement réel du locuteur dans les sous-clips de dialogue.

Pour chaque sous-clip « parlant », on mesure image par image l'énergie de mouvement dans la moitié de l'écran
où se trouve le locuteur, on repère le début et la fin du mouvement (seuil à 30 % du maximum), puis :
  * le sous-clip est ré-échantillonné (setpts) pour que la durée du mouvement = durée de la réplique + 0,3 s
    (facteur borné entre 0,6 et 1,8) ;
  * la réplique est posée au début du mouvement mesuré.
Ce n'est pas une synchronisation labiale (la bouche n'articule pas les phonèmes) : c'est un recalage de début
et de durée. Une vraie synchro demande un modèle piloté par l'audio (Wan 2.2 S2V), voir DECISIONS.

Usage : python align_dialogue_audio.py <dossier_clips> <dossier_audio> <style> <sortie_dossier_aligned>
Écrit <sortie>/<style>/<sous-clip>.mp4 (retimés) et <sortie>/offsets_<style>.json {sous-clip: décalage audio en s}.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# (sous-clip, fichier audio, moitié d'écran du locuteur)
PARLANTS = [("P02-2", "S01E01_P02_BADAUD1.mp3", "left"), ("P02-3", "S01E01_P02_BADAUD2.mp3", "right"),
            ("P03-2", "S01E01_P03_AIDE.mp3", None), ("P03-3", "S01E01_P03_GARNERIN.mp3", None)]
# P03 : l'aide et Garnerin ne sont pas du même côté selon le style
P03_COTE = {"StyleA": {"P03-2": "left", "P03-3": "right"}, "StyleB": {"P03-2": "right", "P03-3": "left"}}


def duree(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip())


def frames(p, tmp):
    tmp.mkdir(parents=True, exist_ok=True)
    for f in tmp.glob("f_*.png"):
        f.unlink()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-vf", "scale=320:180", str(tmp / "f_%04d.png")], check=True)
    return [np.asarray(Image.open(f).convert("L"), dtype=np.float32) for f in sorted(tmp.glob("f_*.png"))]


def main():
    clips, audio, style, out = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
    (out / style).mkdir(parents=True, exist_ok=True)
    offsets, rapport = {}, []
    for sub, wav, cote in PARLANTS:
        cote = cote or P03_COTE[style][sub]
        src = clips / style / f"{sub}_{style}.mp4"
        fr = frames(src, out / "_tmp")
        n = len(fr)
        half = slice(0, 160) if cote == "left" else slice(160, 320)
        energy = np.array([np.abs(fr[i][:, half] - fr[i - 1][:, half]).mean() for i in range(1, n)])
        thr = 0.3 * energy.max()
        idx = np.where(energy > thr)[0]
        debut, fin = (idx[0] + 1) / 16.0, (idx[-1] + 2) / 16.0
        span = max(fin - debut, 0.5)
        cible = duree(audio / wav) + 0.3
        facteur = min(max(cible / span, 0.6), 1.8)
        dst = out / style / f"{sub}_{style}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"setpts={facteur}*PTS,fps=16", "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-an", str(dst)], check=True)
        offsets[sub] = round(debut * facteur, 3)
        rapport.append(f"{sub}_{style} : mouvement {debut:.2f}->{fin:.2f} s (côté {cote}), réplique {cible - 0.3:.2f} s, facteur {facteur:.2f}, audio à +{offsets[sub]:.2f} s")
    json.dump(offsets, open(out / f"offsets_{style}.json", "w"), indent=1)
    print("\n".join(rapport))


if __name__ == "__main__":
    main()
