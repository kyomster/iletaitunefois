#!/usr/bin/env python3
"""Volume réseau RunPod par son API S3 — SANS allumer de GPU (bonne pratique posée par Guillaume le 24 août 2026).

Le volume sert de dépôt permanent : modèles, images clés, références, workflows. Les sorties de génération y sont
écrites par le pod, rapatriées ici, puis SUPPRIMÉES du volume ; tout ce qui est réutilisable y reste.

Endpoint : https://s3api-<datacenter>.runpod.io (EU-RO-1 → s3api-eu-ro-1.runpod.io), bucket = id du volume.
Clés : RUN_POD_S3_ACCESS_KEY / RUN_POD_S3_SECRET_KEY du `.env` (jamais affichées).

Usage :
  python runpod_s3.py ls [prefixe]              liste le contenu (taille totale par dossier de premier niveau)
  python runpod_s3.py up <local> <cle>          téléverse un fichier
  python runpod_s3.py dl <cle> <local>          télécharge un fichier
  python runpod_s3.py rm <cle>                  supprime un objet
  python runpod_s3.py rmdir <prefixe>           supprime tous les objets sous un préfixe (sorties rapatriées)
Options : --volume=<id> (défaut o6g76dr9cj), --dc=<eu-ro-1>
"""
import os
import sys
from pathlib import Path

import boto3
from botocore.config import Config

ENV = Path(__file__).resolve().parents[2] / ".env"


def client(dc="eu-ro-1"):
    vals = {}
    for line in ENV.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            vals[k.strip()] = v.strip().strip('"')
    return boto3.client("s3", endpoint_url=f"https://s3api-{dc}.runpod.io",
                        aws_access_key_id=vals["RUN_POD_S3_ACCESS_KEY"],
                        aws_secret_access_key=vals["RUN_POD_S3_SECRET_KEY"],
                        region_name=dc, config=Config(signature_version="s3v4", retries={"max_attempts": 5}))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = {a.split("=", 1)[0].lstrip("-"): a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--") and "=" in a}
    vol, dc = opts.get("volume", "o6g76dr9cj"), opts.get("dc", "eu-ro-1")
    s3, cmd = client(dc), args[0]
    if cmd == "ls":
        prefix = args[1] if len(args) > 1 else ""
        total, par_dossier, n = 0, {}, 0
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=vol, Prefix=prefix):
            for o in page.get("Contents", []):
                total += o["Size"]; n += 1
                par_dossier[o["Key"].split("/")[0]] = par_dossier.get(o["Key"].split("/")[0], 0) + o["Size"]
                if n <= 40:
                    print(f"{o['Size']:>13,}  {o['Key']}")
        if n > 40:
            print(f"... et {n - 40} autres objets")
        print("---")
        for d, s in sorted(par_dossier.items(), key=lambda x: -x[1]):
            print(f"{s / 2**30:8.1f} Gio  {d}/")
        print(f"{total / 2**30:8.1f} Gio  TOTAL ({n} objets)")
    elif cmd == "up":
        s3.upload_file(args[1], vol, args[2])
        print("téléversé", args[2], os.path.getsize(args[1]))
    elif cmd == "dl":
        Path(args[2]).parent.mkdir(parents=True, exist_ok=True)
        s3.download_file(vol, args[1], args[2])
        print("téléchargé", args[2], os.path.getsize(args[2]))
    elif cmd == "rm":
        s3.delete_object(Bucket=vol, Key=args[1]); print("supprimé", args[1])
    elif cmd == "rmdir":
        n = 0
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=vol, Prefix=args[1]):
            for o in page.get("Contents", []):
                s3.delete_object(Bucket=vol, Key=o["Key"]); n += 1  # delete_objects renvoie 307 sur l'API S3 RunPod : suppression une par une
        print("supprimés", n, "objets sous", args[1])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
