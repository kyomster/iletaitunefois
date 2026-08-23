#!/usr/bin/env python3
"""Pilotage minimal de RunPod pour le pilote S01E01 (API REST v1 + GraphQL pour les ports).

La clé est lue dans C:/Git/iletaitunefois/.env (RUN_POD) et n'est jamais affichée.

Usage :
  python runpod_pilote.py create <nom> <cle_publique_ssh_fichier> [jupyter_password]
  python runpod_pilote.py status <podId>
  python runpod_pilote.py ports  <podId>          # ip:port SSH public, URL proxy ComfyUI
  python runpod_pilote.py stop   <podId>
  python runpod_pilote.py terminate <podId>
  python runpod_pilote.py list

Choix posés le 22 août 2026 (DECISIONS-pilote.md) : volume réseau existant `atelier-modeles` (o6g76dr9cj, EU-RO-1),
image runpod/pytorch:1.1.0-cu1281-torch280-ubuntu2204, GPU par ordre de préférence A100 80 Go PCIe, RTX PRO 6000
Blackwell Server, RTX 5090 (ni L40S ni RTX 6000 Ada en stock en EU-RO-1 ce jour).
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

ENV = Path(r"C:/Git/iletaitunefois/.env")
REST = "https://rest.runpod.io/v1"
GQL = "https://api.runpod.io/graphql"
VOLUME_ID = "o6g76dr9cj"
IMAGE = "runpod/pytorch:1.1.0-cu1281-torch280-ubuntu2204"
GPUS = ["NVIDIA A100 80GB PCIe", "NVIDIA RTX PRO 6000 Blackwell Server Edition", "NVIDIA GeForce RTX 5090"]


def key():
    for line in ENV.read_text(encoding="utf-8").splitlines():
        if line.startswith("RUN_POD="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("RUN_POD absent du .env")


def call(method, path, body=None):
    req = urllib.request.Request(REST + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            txt = r.read().decode()
            return r.status, (json.loads(txt) if txt else None)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def gql(query):
    req = urllib.request.Request(GQL, method="POST", data=json.dumps({"query": query}).encode(),
                                 headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json",
                                          "User-Agent": "curl/8.0"})  # l'endpoint GraphQL refuse l'UA python (403)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def create(name, pubkey_file, jupyter_password="pilote"):
    body = {
        "name": name, "imageName": IMAGE, "cloudType": "SECURE", "computeType": "GPU",
        "gpuTypeIds": GPUS, "gpuTypePriority": "custom", "gpuCount": 1,
        "dataCenterIds": ["EU-RO-1"], "dataCenterPriority": "custom",
        "networkVolumeId": VOLUME_ID, "volumeMountPath": "/workspace",
        "containerDiskInGb": int(os.environ.get("DISK_GB", "60")), "ports": ["22/tcp", "8188/http", "8888/http"],
        "env": {"PUBLIC_KEY": Path(pubkey_file).read_text().strip(), "JUPYTER_PASSWORD": jupyter_password},
        "supportPublicIp": True, "interruptible": False,
    }
    status, res = call("POST", "/pods", body)
    print(status); print(json.dumps(res, indent=1) if not isinstance(res, str) else res)


def status(pod_id):
    s, res = call("GET", f"/pods/{pod_id}")
    print(s); print(json.dumps(res, indent=1) if not isinstance(res, str) else res)


def ports(pod_id):
    d = gql('{ pod(input:{podId:"%s"}) { id desiredStatus machine { gpuDisplayName } runtime { uptimeInSeconds ports { ip isIpPublic privatePort publicPort type } } } }' % pod_id)
    pod = d.get("data", {}).get("pod")
    print(json.dumps(pod, indent=1))
    if pod and pod.get("runtime"):
        for p in pod["runtime"]["ports"] or []:
            if p["privatePort"] == 22 and p["isIpPublic"]:
                print(f"SSH: ssh -p {p['publicPort']} root@{p['ip']}")
    print(f"ComfyUI proxy: https://{pod_id}-8188.proxy.runpod.net/")


def main():
    cmd = sys.argv[1]
    if cmd == "create":
        create(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "pilote")
    elif cmd == "status":
        status(sys.argv[2])
    elif cmd == "ports":
        ports(sys.argv[2])
    elif cmd == "stop":
        print(call("POST", f"/pods/{sys.argv[2]}/stop"))
    elif cmd == "terminate":
        print(call("DELETE", f"/pods/{sys.argv[2]}"))
    elif cmd == "list":
        s, res = call("GET", "/pods"); print(s, json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
