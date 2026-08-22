#!/usr/bin/env python3
"""Prépare les 48 jobs vidéo du pilote S01E01 (16 clips x 3 styles) pour ComfyUI / RunPod.

Sources, copiées octet pour octet :
  * blocs de style « plan de scène » : docs/S01E01-pilote-prompts-3-styles.md point 2 ;
  * briques de mouvement (durée, sujet, caméra) : même fiche, point 7 ;
  * gabarit de prompt de mouvement : docs/PIPELINE-video-et-voix.md point 6 ;
  * négatives de mouvement : fiche point 4.5 ;
  * table length (16 im/s, 4n+1) : docs/RUNPOD-COMFYUI-mode-d-emploi.md point 5.

Raccords. Première lecture (22 août 2026, 12 h) : à l'intérieur d'un bloc, clip k = clé k en départ, clé k+1 en fin
(FLF2V). Résultat constaté sur le style A : les clés successives d'un bloc ont des CADRAGES différents (très large,
moyen, contre-plongée), le FLF2V morphe donc la caméra d'un cadrage à l'autre au lieu d'une coupe nette.
Application de PIPELINE-video-et-voix.md §5.2 : une coupe nette = I2V avec image de départ neuve ; FLF2V seulement
pour un raccord de continuité dans le même cadrage. Sur le pilote, toutes les coupes internes changent de cadrage :
MODE par défaut = "i2v" partout. L'option --chain reconstruit la chaîne FLF2V par images clés.

Usage :
  python build_clips_pilote.py <dossier_images_720p> <sortie_jobs.json> [<sortie.md>] [--chain] [--seed-offset=N]

<dossier_images_720p> contient Style{A,B,C}/P<plan>-<clip>_Style<X>.png en 1280x720.
Les graines sont fixées de façon déterministe (stable d'un appel à l'autre) et consignées.
"""
import json
import sys
import zlib
from pathlib import Path

STYLE = {
    "StyleA": "2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:",
    "StyleB": "inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:",
    "StyleC": "hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:",
}

# Essai du 22 août 2026 (lot 3) : bloc de style VIDÉO réduit à la facture, sans description des personnages, pour
# empêcher le modèle vidéo de fabriquer des têtes (style B surtout). Option --video-style=reduced. Écart à la fiche
# (bloc non copié octet pour octet), signalé dans DECISIONS ; l'image clé porte déjà le style.
STYLE_REDUCED = {
    "StyleA": "flat 2D cartoon animation, bold clean outlines, flat cel shading, muted earth tones, limited animation, 16:9 frame:",
    "StyleB": "flat graphic 2D cartoon animation on a richly painted atmospheric background, textured light, muted earth tones, limited animation, 16:9 frame:",
    "StyleC": "hand drawn 2D cel animation, crisp ink outlines, flat two tone cel shading, amber and teal palette, limited animation, 16:9 frame:",
}

NEG_MOUVEMENT = "photorealistic rendering, skin texture, smooth gradients, cut, scene change, camera shake, morphing, text, watermark, lip sync, mouth articulation, extra characters appearing"
# Ajout du 22 août 2026 (premier lot : personnages et visages surgis dans des plans vides, 4 clips sur 19) :
NEG_PRESENCE = "new character entering the frame, person appearing, face appearing, giant face, ghost figure, figure emerging from the mist, hands appearing, head appearing, crowd figures turning to face the camera, dot eyes on crowd figures, faces in the crowd"

# Présence à l'image (22 août 2026, après le premier lot) : "none" = aucun personnage, "hands" = mains seules,
# "crowd" ou "character" = des personnages. Elle choisit la ligne du gabarit sur les personnages, voir motion_prompt.
# La ligne générique « Characters gesture and react, they do not speak » collée sur tous les clips invitait des
# personnages dans les plans vides (4b-1, 4b-3, 5-3, 1a-1 B).
PRESENCE = {"P1a-1": "crowd", "P1a-2": "crowd", "P1a-3": "none", "P1a-4": "crowd", "P1b-1": "crowd", "P1b-2": "character",
            "P1b-3": "hands", "P4a-1": "crowd", "P4a-2": "crowd", "P4a-3": "none", "P4b-1": "none", "P4b-2": "hands",
            "P4b-3": "none", "P5-1": "hands", "P5-2": "hands", "P5-3": "none"}
PRESENCE_LINE = {
    "none": "There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.",
    "hands": "Only the hands and arms already in the first frame move; no face, no head and no other person appears.",
    "crowd": "The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.",
    "character": "Characters gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.",
}

# (clip, bloc, durée s, subject, camera) — fiche point 7, dans l'ordre
CLIPS = [
    ("P1a-1", "1a", 2.5, "the mist drifts slowly across the lawns, the crowd sways gently at the foot of the balloon", "static"),
    ("P1a-2", "1a", 2.5, "the balloon sways in the wind, the mooring ropes pull taut and slacken", "static"),
    ("P1a-3", "1a", 2.0, "the banners snap in the wind at the crown of the balloon", "static"),
    ("P1a-4", "1a", 2.0, "the crowd turns their heads in one movement toward the basket", "static"),
    ("P1b-1", "1b", 3.0, "the crowd parts into two lines, hats are lifted", "static"),
    ("P1b-2", "1b", 3.0, "the basket is carried forward, ropes trailing on the grass", "slow lateral tracking to the right, following the basket"),
    ("P1b-3", "1b", 3.0, "hands knot the ropes around the wicker rim", "static"),
    ("P4a-1", "4a", 3.0, "the balloon tears away from the ground, the released ropes fall back", "static"),
    ("P4a-2", "4a", 3.0, "the crowd rocks backwards, hats held on with both hands", "static"),
    ("P4a-3", "4a", 4.0, "the balloon rises and shrinks above the trees", "very slow tilt upward, following the balloon"),
    ("P4b-1", "4b", 3.5, "the rooftops slide slowly below, chimney smoke streams sideways", "static"),
    ("P4b-2", "4b", 3.5, "the wicker rim vibrates, the gloved hand tightens on it", "static"),
    ("P4b-3", "4b", 3.0, "the haze drifts over the city, the dark patch of the crowd stays still", "very slow zoom out"),
    ("P5-1", "5", 2.5, "the hand takes hold of the knife", "static"),
    ("P5-2", "5", 3.0, "the blade saws the rope, fibres spring free one by one", "static"),
    ("P5-3", "5", 2.5, "the rope gives way at once, the strands whip the air", "static"),
]

LENGTH = {2.0: 33, 2.5: 41, 3.0: 49, 3.5: 57, 4.0: 65}  # 16 im/s, 4n+1

SETTINGS = {"width": 1280, "height": 720, "fps": 16, "steps": 4, "steps_high": 2, "steps_low": 2,
            "cfg": 1.0, "sampler": "euler", "scheduler": "simple", "shift": 5.0,
            "model": "Wan2.2-I2V-A14B fp8 (high+low) + LightX2V 4 steps ; FLF2V : Wan2.2-14B-FLF2V"}


def motion_prompt(style, duration, subject, camera, presence="character", reduced=False):
    return (
        f"{(STYLE_REDUCED if reduced else STYLE)[style]}\n\n"
        "Single continuous shot, no cut, no scene change.\n"
        f"Subject : {subject}\n"
        f"Camera : {camera}\n"
        f"Duration : {duration:g} seconds at 16 frames per second.\n"
        "Limited animation cadence, holds on twos, not fluid interpolation.\n"
        f"{PRESENCE_LINE[presence]}\n"
        "Motion starts on the first frame, no frozen start."
    )


def seed_for(name):
    return zlib.crc32(name.encode("utf-8")) % (2**31 - 1)


def main():
    chain = "--chain" in sys.argv
    seed_offset = 0
    reduced = "--video-style=reduced" in sys.argv
    for a in sys.argv[1:]:
        if a.startswith("--seed-offset="):
            seed_offset = int(a.split("=", 1)[1])  # reprise : autre tirage, meme graine de base + decalage
    args = [a for a in sys.argv[1:] if a not in ("--chain", "--video-style=reduced") and not a.startswith("--seed-offset=")]
    sys.argv = [sys.argv[0]] + args
    img_dir = Path(sys.argv[1])
    jobs = []
    for style in ("StyleA", "StyleB", "StyleC"):
        for i, (clip, bloc, dur, subject, camera) in enumerate(CLIPS):
            nxt = CLIPS[i + 1] if i + 1 < len(CLIPS) else None
            chain_here = chain and nxt is not None and nxt[1] == bloc  # même bloc → raccord FLF2V (option)
            start = img_dir / style / f"{clip}_{style}.png"
            end = (img_dir / style / f"{nxt[0]}_{style}.png") if chain_here else None
            jobs.append({
                "name": f"{clip}_{style}", "clip": clip, "bloc": bloc, "style": style,
                "mode": "flf2v" if chain_here else "i2v",
                "duration_s": dur, "length": LENGTH[dur],
                "start_image": str(start), "end_image": str(end) if end else None,
                "seed": seed_for(f"{clip}_{style}") + seed_offset,
                "presence": PRESENCE[clip],
                "prompt": motion_prompt(style, dur, subject, camera, PRESENCE[clip], reduced),
                "video_style": "reduced" if reduced else "fiche",
                "negative": NEG_MOUVEMENT + ", " + NEG_PRESENCE,
                "settings": SETTINGS,
                "output": f"clips-runpod/{style}/{clip}_{style}",
            })
    assert len(jobs) == 48
    missing = [j["start_image"] for j in jobs if not Path(j["start_image"]).exists()]
    missing += [j["end_image"] for j in jobs if j["end_image"] and not Path(j["end_image"]).exists()]
    if missing:
        print("IMAGES MANQUANTES :", *missing, sep="\n  ")
    Path(sys.argv[2]).write_text(json.dumps(jobs, indent=1, ensure_ascii=False), encoding="utf-8")
    if len(sys.argv) > 3:
        md = ["# S01E01 — les 48 jobs vidéo du pilote, tels que soumis à ComfyUI", "",
              "Générés par `docs/scripts/build_clips_pilote.py`. Réglages : " + SETTINGS["model"] + ", 1280x720, 16 im/s, 4 étapes (2+2), cfg 1, euler/simple, shift 5. Négative commune : `" + NEG_MOUVEMENT + "`.", "",
              "| Clip | Style | Mode | s | length | Image de fin | Graine |", "|---|---|---|---|---|---|---|"]
        for j in jobs:
            md.append(f"| {j['clip']} | {j['style']} | {j['mode']} | {j['duration_s']:g} | {j['length']} | {Path(j['end_image']).name if j['end_image'] else '—'} | {j['seed']} |")
        md += ["", "## Prompts de mouvement", ""]
        for j in jobs:
            md += [f"### {j['name']}", "", "```", j["prompt"], "```", ""]
        Path(sys.argv[3]).write_text("\n".join(md), encoding="utf-8", newline="\n")
    print(f"{len(jobs)} jobs écrits dans {sys.argv[2]} ; flf2v={sum(j['mode']=='flf2v' for j in jobs)}, i2v={sum(j['mode']=='i2v' for j in jobs)}")


if __name__ == "__main__":
    main()
