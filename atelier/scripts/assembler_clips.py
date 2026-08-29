#!/usr/bin/env python3
"""Assemble les prompts de MOUVEMENT d'un épisode pour LTX-2.5 (`run_ltx25_runpod.py`), pour un style de la bibliothèque.

Gabarit LTX-2.5, tel que validé sur le pilote (STRATEGIE-video.md §4) :
  [style.clip, réduit à la facture] Single continuous shot, no cut. <sujet>. Camera: <caméra>. <ligne de présence>
  <garde des objets> Ambient sound only: <ambiance>.
Un plan de dialogue remplace le sujet par le texte de DIALOGUES, qui CITE les répliques exactes entre guillemets.
La ligne de présence est celle du plan (PRESENCE) quand le module en donne une, sinon la ligne générique.

Les gardes sont collées par le code, pas par la vigilance (RÈGLE 41) : la ligne de présence par plan (22 août) et
la garde des objets (RÈGLE 40, 26 août). Le module de briques fournit CLIPS, PRESENCE, DIALOGUES.

Usage :
  python assembler_clips.py <briques.py> <dossier_cles_1280x704> <sortie.json> [--styles=StyleP] [--seed-base=9700] [--clips=P02,P03]

<dossier_cles> contient <clip>_<style>.png (par exemple iletaitunefois/S01E01/assets/cles/), à redimensionner en 1280x704
(multiples de 32) avant soumission — run_ltx25_runpod.py s'en charge si la clé est plus grande.
Longueur en images = 8n+1 la plus proche de durée × 24.
"""
import json
import sys
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bibliotheque import charger_briques, charger_styles, options  # noqa: E402

FPS, W, H = 24, 1280, 704
PRESENCE_LINE = {
    "none": "There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.",
    "hands": "Only the hands and arms already in the first frame move; no face, no head and no other person appears.",
    "crowd": "The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer. Nobody new enters the frame, no figure appears in the foreground.",
    "character": "Nobody new enters the frame, no figure appears in the foreground.",
}
PRESENCE_GENERIQUE = "Nobody new enters the frame."  # ce qu'ont reçu les 16 clips muets du pilote P, propres 16 fois sur 16
CLAUSE_OBJETS = ("Every object visible is already present in the first frame: no new object appears, nothing is taken out, "
                 "put on, handed over or produced, and no object is duplicated.")
AMBIANCE_MUET = "Ambient sound only: wind and distant murmur, no speech, no music."
NEGATIVE = ("blurry, low quality, jpeg artifacts, text, watermark, subtitles, extra people, new characters, deformed hands, "
            "car, vehicle, carriage, modern object, anachronism, camera cut, scene change, "
            "new object appearing, second hat, a hat above another hat, duplicated prop, object materialising, object handed over")


def longueur(duree_s):
    n = round(duree_s * FPS)
    return max(9, 8 * round((n - 1) / 8) + 1)


def seed_for(name):
    return zlib.crc32(name.encode("utf-8")) % (2**31 - 1)


def prompt_muet(style, sujet, camera, presence):
    ligne = PRESENCE_LINE[presence] if presence else PRESENCE_GENERIQUE
    return f"{style['clip']} Single continuous shot, no cut. {sujet.rstrip('.')}. Camera: {camera}. {ligne} {CLAUSE_OBJETS} {AMBIANCE_MUET}"


def prompt_dialogue(style, texte):
    return f"{style['clip']} {texte} {CLAUSE_OBJETS}"


def main():
    args, opts, styles = options(sys.argv[1:])
    B = charger_briques(args[0])
    cles = Path(args[1])
    bib = charger_styles()
    only = set(opts["clips"].split(",")) if isinstance(opts.get("clips"), str) else None
    base = int(opts["seed-base"]) if isinstance(opts.get("seed-base"), str) else None
    jobs = []
    for code in styles:
        style = bib[code]
        assert style.get("clip"), f"{code} n'a pas de bloc de style vidéo (clé `clip` de style.json)"
        entries = [(c, b, d, "muet", (s, cam)) for c, b, d, s, cam in B.CLIPS]
        entries += [(c, b, d, "dialogue", t) for c, (b, d, t) in getattr(B, "DIALOGUES", {}).items()]
        ordre = getattr(B, "ORDRE_MONTAGE", [e[0] for e in entries])
        entries.sort(key=lambda e: ordre.index(e[0]) if e[0] in ordre else 999)
        for i, (clip, bloc, duree, genre, payload) in enumerate(entries):
            if only and clip not in only:
                continue
            prompt = prompt_dialogue(style, payload) if genre == "dialogue" else prompt_muet(style, payload[0], payload[1], getattr(B, "PRESENCE", {}).get(clip))
            jobs.append({
                "name": f"{clip}-{style['lettre']}", "clip": clip, "bloc": bloc, "style": code,
                "image": str(cles / f"{clip}_{code}.png"), "prompt": prompt, "negative": NEGATIVE,
                "seed": (base + i) if base is not None else seed_for(f"{clip}_{code}"),
                "length": longueur(duree), "width": W, "height": H, "fps": FPS,
            })
    manquantes = [j["image"] for j in jobs if not Path(j["image"]).exists()]
    if manquantes:
        print("CLÉS MANQUANTES :", *manquantes, sep="\n  ")
    Path(args[2]).write_text(json.dumps(jobs, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(jobs)} clips écrits dans {args[2]} ({', '.join(styles)})")


if __name__ == "__main__":
    main()
