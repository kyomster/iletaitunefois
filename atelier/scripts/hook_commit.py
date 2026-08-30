#!/usr/bin/env python3
"""Hook Claude Code (PreToolUse sur Bash) : avant un `git commit`, les documents générés doivent être à jour
et doctor.py ne doit avoir aucun BLOQUANT. Lit l'appel d'outil sur stdin ; sort 2 pour bloquer, 0 sinon."""
import json
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SCRIPTS = RACINE / "atelier" / "scripts"

try:
    entree = json.load(sys.stdin)
except Exception:
    sys.exit(0)
cmd = (entree.get("tool_input") or {}).get("command", "")
if "git commit" not in cmd:
    sys.exit(0)
rendu = subprocess.run([sys.executable, str(SCRIPTS / "rendre.py"), "--check"], cwd=RACINE, capture_output=True, text=True, encoding="utf-8")
if rendu.returncode != 0:
    print("COMMIT REFUSÉ : les documents générés ne correspondent pas aux données. Lancer `python atelier/scripts/rendre.py`.\n" + rendu.stdout[-800:], file=sys.stderr)
    sys.exit(2)
doc = subprocess.run([sys.executable, str(SCRIPTS / "doctor.py")], cwd=RACINE, capture_output=True, text=True, encoding="utf-8")
if doc.returncode != 0:
    print("COMMIT REFUSÉ : doctor.py a un BLOQUANT.\n" + doc.stdout[-1500:], file=sys.stderr)
    sys.exit(2)
sys.exit(0)
