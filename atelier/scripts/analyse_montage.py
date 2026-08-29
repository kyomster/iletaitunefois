#!/usr/bin/env python3
"""Prépare la vérification indépendante d'un montage : une image par seconde + transcription horodatée de la piste audio.

Demandé par Guillaume le 22 août 2026 (« Extrait une image par seconde de la vidéo avec l'audio pour vérifier.
Analyse les images extraites avec Sonnet ») : on ne juge pas un montage à l'œil sur le lecteur, on le réduit à
une planche d'images datées et à une ligne de temps des mots, et un agent indépendant relit le tout.

  * <sortie>/f_NNN.jpg : image à t = NNN-1 s (640x360)
  * <sortie>/audio.mp3 : piste audio du montage
  * <sortie>/transcript.json : réponse brute ElevenLabs STT (scribe_v1, fr, horodatage des mots)
  * <sortie>/timeline_audio.txt : « debut- fin  mot » par ligne, puis la liste des images avec les mots entendus pendant chaque seconde

La clé ElevenLabs est lue dans le .env (ELEVEN_LABS), jamais affichée.
Usage : python analyse_montage.py <montage.mp4> <dossier_sortie> [<chemin .env>]
"""
import json
import os
import subprocess
import sys
import uuid
import urllib.request
from pathlib import Path


def cle_eleven(env_path):
    for line in Path(env_path).read_text(encoding="utf-8").splitlines():
        if line.startswith("ELEVEN_LABS="):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("ELEVEN_LABS absente du .env")


def stt(mp3, key):
    boundary = uuid.uuid4().hex
    body = b""
    for k, v in (("model_id", "scribe_v1"), ("language_code", "fra"), ("timestamps_granularity", "word")):
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"audio.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n".encode()
    body += Path(mp3).read_bytes() + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request("https://api.elevenlabs.io/v1/speech-to-text", data=body,
                                 headers={"xi-api-key": key, "Content-Type": f"multipart/form-data; boundary={boundary}"})
    return json.loads(urllib.request.urlopen(req, timeout=300).read())


def main():
    video, out = Path(sys.argv[1]), Path(sys.argv[2])
    env = sys.argv[3] if len(sys.argv) > 3 else str(Path(__file__).resolve().parents[2] / ".env")
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("f_*.jpg"):
        f.unlink()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf", "fps=1,scale=640:360", "-q:v", "3", str(out / "f_%03d.jpg")], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vn", "-c:a", "libmp3lame", "-b:a", "128k", str(out / "audio.mp3")], check=True)
    tr = stt(out / "audio.mp3", cle_eleven(env))
    json.dump(tr, open(out / "transcript.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    words = [w for w in tr.get("words", []) if w.get("type") == "word"]
    lines = [f"{w['start']:6.2f}-{w['end']:6.2f}  {w['text']}" for w in words]
    n = len(list(out.glob("f_*.jpg")))
    lines.append("")
    lines.append("image -> seconde couverte -> mots entendus")
    for i in range(1, n + 1):
        t0, t1 = i - 1, i
        heard = " ".join(w["text"] for w in words if w["end"] > t0 and w["start"] < t1)
        lines.append(f"f_{i:03d}.jpg  {t0:3d}-{t1:3d} s  {heard}")
    (out / "timeline_audio.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"{n} images, {len(words)} mots -> {out}")


if __name__ == "__main__":
    main()
