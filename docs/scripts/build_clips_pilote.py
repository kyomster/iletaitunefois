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
    # --- styles retenus le 23 août 2026, copie de PLAN-styles-D-E-F.md §4.1, §4.7, §4.8 ---
    "StyleD": "2D anime illustration, modern cinematic adventure anime style, clean thin dark brown ink linework with subtle weight variation, cel shaded characters with a soft airbrush gradient blending each shadow into its base tone, warm natural skin with a faint blush on the cheeks, adult realistic body proportions and grounded facial features, expressive eyes with a single specular highlight, hand painted background with atmospheric depth and aerial perspective, volumetric light, shallow depth of field with the background softly out of focus, fine film grain, 16:9 frame:",
    "StyleJ": "live action cinema look, photographed on 35mm film, naturalistic period drama cinematography, real actors in accurate historical costume, motivated practical lighting with deep natural falloff, shallow depth of field with creamy bokeh, fine organic film grain, subtle halation on the highlights, desaturated filmic colour grade with rich blacks and warm skin tones, photorealistic, the image fills the entire 16:9 frame edge to edge, no black bars, 16:9 frame:",
    "StyleK": "stylized 3D feature animation, high end computer animated film look, believable human proportions with only a light touch of caricature in the features, soft subsurface skin with fine texture and no plastic sheen, individually groomed hair, real cloth simulation with visible weave and wear, naturalistic cinematography with motivated light and long lens compression, restrained desaturated colour grade, shallow depth of field, subtle volumetric atmosphere, an adult dramatic register rather than a comic one, stylized and not photographic, 16:9 frame:",
}

# Essai du 22 août 2026 (lot 3) : bloc de style VIDÉO réduit à la facture, sans description des personnages, pour
# empêcher le modèle vidéo de fabriquer des têtes (style B surtout). Option --video-style=reduced. Écart à la fiche
# (bloc non copié octet pour octet), signalé dans DECISIONS ; l'image clé porte déjà le style.
STYLE_REDUCED = {
    "StyleA": "flat 2D cartoon animation, bold clean outlines, flat cel shading, muted earth tones, limited animation, 16:9 frame:",
    "StyleB": "flat graphic 2D cartoon animation on a richly painted atmospheric background, textured light, muted earth tones, limited animation, 16:9 frame:",
    "StyleC": "hand drawn 2D cel animation, crisp ink outlines, flat two tone cel shading, amber and teal palette, limited animation, 16:9 frame:",
    # 23 août 2026 : blocs réduits écrits pour D, J et K, mais NON VÉRIFIÉS.
    # Le style B avait exigé le bloc réduit parce que le bloc complet faisait fabriquer des têtes d'inkman
    # partout par Wan 2.2 (12 clips sur 16 inutilisables, corrigé à 12 sur 12 avec le bloc réduit).
    # On ne sait pas si D, J et K souffrent du même défaut. À trancher sur UN clip d'essai par style,
    # pas sur les seize. Voir ETAT-DE-PREPARATION-styles-D-J-K.md §3.3.
    "StyleD": "2D anime animation, thin dark brown linework, soft cel shading, hand painted background, shallow depth of field, film grain, limited animation, 16:9 frame:",
    "StyleJ": "live action 35mm period film, naturalistic cinematography, shallow depth of field, film grain, no black bars, 16:9 frame:",
    "StyleK": "stylized 3D feature animation, restrained desaturated grade, long lens, shallow depth of field, 16:9 frame:",
}

# Styles qui exigent le bloc réduit en vidéo. B est le seul VÉRIFIÉ (lot 3, 22 août).
STYLES_BLOC_REDUIT_OBLIGATOIRE = {"StyleB"}

# Styles pour lesquels le pilote est produit. A, B, C conservés pour reproduire l'historique ;
# D, J, K retenus le 23 août. Surchargeable par --styles=StyleD,StyleJ,StyleK.
STYLES_DEFAUT = ("StyleA", "StyleB", "StyleC")

NEG_MOUVEMENT = "photorealistic rendering, skin texture, smooth gradients, cut, scene change, camera shake, morphing, text, watermark, lip sync, mouth articulation, extra characters appearing, new object appearing, second hat, a hat above another hat, duplicated prop, object materialising"
# Ajout du 22 août 2026 (premier lot : personnages et visages surgis dans des plans vides, 4 clips sur 19) :
NEG_PRESENCE = "new character entering the frame, person appearing, face appearing, giant face, ghost figure, figure emerging from the mist, hands appearing, head appearing, crowd figures turning to face the camera, dot eyes on crowd figures, faces in the crowd"
# 26 août 2026, retour de Guillaume sur le pilote P : « une femme met un chapeau alors qu'elle a déjà quelque chose
# sur la tête ». Le gabarit gardait les PERSONNES (« Nobody new enters the frame ») mais rien ne gardait les OBJETS.
# Le sujet disait « hats held on with both hands » : nommer un objet déjà présent comme complément d'un verbe de
# possession fait apparaître un SECOND exemplaire, que le modèle pose sur celui de l'image. RÈGLE 40.
CLAUSE_OBJETS = ("Every object visible is already present in the first frame: no new object appears, nothing is taken out, "
                 "put on, handed over or produced, and no object is duplicated.")
NEG_OBJETS = "new object appearing, second hat, a hat above another hat, duplicated prop, object materialising, object handed over"

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
    # 22 août 2026, demande de Guillaume : pas de synchro labiale ne veut pas dire bouches immobiles.
    "talking": "The characters talk to each other with simple cartoon mouth movements, mouths opening and closing, not synchronized to any audio; they gesture lightly and stay in place. Nobody new enters the frame, no figure appears in the foreground.",
    # 22 août 2026, 17 h 30 (Guillaume) : un seul locuteur par clip, qui parle du premier au dernier frame ; le clip dure la réplique.
    "talking_solo": "Only ONE character speaks in this clip, continuously from the very first frame to the very last frame, his mouth opening and closing the whole time in simple cartoon mouth movements; the other character keeps his mouth firmly closed and only listens. Both stay in place. Nobody new enters the frame.",
}
# Sur un clip « talking », les négatives « lip sync, mouth articulation » sont retirées.
NEG_TALKING_RETIRE = ("lip sync", "mouth articulation")

# Dialogue découpé par locuteur (décision Guillaume, 22 août 15 h : un clip bouclé donne des scènes en double et deux
# bouches qui parlent). Chaque sous-clip part de l'image clé et Y REVIENT (FLF2V départ = fin = image clé) : le raccord
# est invisible. (sous-clip, durée s, présence, subject). Les durées somment à celle du plan : P02 10 s, P03 12 s.
DIALOGUE = {
    # v3 du 22 août, 17 h 30 : durée des sous-clips parlants = durée de la réplique + 0,4 s ; le locuteur parle tout le clip.
    "P02": [
        ("P02-1", 2.0, "character", "the two onlookers stand and watch the balloon behind them in silence, both mouths closed, slight breathing, the round one adjusts his hat"),
        ("P02-2", 1.5, "talking_solo", "the round onlooker with the top hat speaks, his mouth opening and closing from the first frame to the last, he points toward the basket; the thin onlooker with the cane listens with his mouth firmly closed"),
        ("P02-3", 2.25, "talking_solo", "the thin onlooker with the cane speaks, his mouth opening and closing from the first frame to the last as he leans in; the round onlooker listens with his mouth firmly closed"),
        ("P02-4", 4.25, "character", "both onlookers turn their eyes toward the basket in silence, mouths closed, the thin one taps his cane on the ground"),
    ],
    "P03": [
        ("P03-1", 2.0, "character", "Garnerin grips the release rope and looks up at the balloon in silence, the assistant leans on the rim, both mouths closed"),
        ("P03-2", 3.75, "talking_solo", "the assistant on the right speaks, pleading, his mouth and hands moving from the first frame to the last; Garnerin keeps his hand on the rope and his eyes up, mouth firmly closed"),
        ("P03-3", 1.25, "talking_solo", "Garnerin gives a short curt order, his mouth opening and closing from the first frame to the last, eyes still on the balloon; the assistant is silent and still"),
        ("P03-4", 5.0, "character", "Garnerin pulls the release rope in silence and the assistant steps back a little, both mouths closed"),
    ],
}

# Clips de dialogue du pilote (plans FIXE du scénario rendus en clips parlants bouclables, + un ANIMÉ où les
# personnages échangent), essai du 22 août 2026 : (clip, bloc, durée s, subject, camera)
TALK_CLIPS = [
    ("P02", "2", 5.0, "the two onlookers lean toward each other and argue about a bet, one of them points toward the basket behind them", "static"),
    ("P03", "3", 5.0, "the assistant pleads with Garnerin from the rim of the basket, Garnerin answers curtly with his hand on the release rope and his eyes on the balloon", "static"),
    ("P1b-2", "1b", 3.0, "the basket is carried forward, ropes trailing on the grass, the two assistants exchange a few words as they walk", "slow lateral tracking to the right, following the basket"),
]

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
    # 26 août 2026 : « hats held on with both hands » faisait naître un second chapeau dans les mains. On décrit
    # le déplacement de ce qui est déjà là, en désignant le chapeau comme DÉJÀ PORTÉ (RÈGLE 40).
    ("P4a-2", "4a", 3.0, "the onlookers lean backwards to follow the balloon, each of them raising both hands to the brim of the hat he is already wearing and pressing it down onto his head; the hats never leave the heads", "static"),
    ("P4a-3", "4a", 4.0, "the balloon rises and shrinks above the trees", "very slow tilt upward, following the balloon"),
    ("P4b-1", "4b", 3.5, "the rooftops slide slowly below, chimney smoke streams sideways", "static"),
    ("P4b-2", "4b", 3.5, "the wicker rim vibrates, the gloved hand tightens on it", "static"),
    ("P4b-3", "4b", 3.0, "the haze drifts over the city, the dark patch of the crowd stays still", "very slow zoom out"),
    ("P5-1", "5", 2.5, "the hand takes hold of the knife", "static"),
    ("P5-2", "5", 3.0, "the blade saws the rope, fibres spring free one by one", "static"),
    ("P5-3", "5", 2.5, "the rope gives way at once, the strands whip the air", "static"),
]

LENGTH = {1.25: 21, 1.5: 25, 2.0: 33, 2.25: 37, 2.5: 41, 3.0: 49, 3.5: 57, 3.75: 61, 4.0: 65, 4.25: 69, 4.5: 73, 5.0: 81}  # 16 im/s, 4n+1

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
        f"{CLAUSE_OBJETS}\n"
        "Motion starts on the first frame, no frozen start."
    )


def seed_for(name):
    return zlib.crc32(name.encode("utf-8")) % (2**31 - 1)


def main():
    chain = "--chain" in sys.argv
    seed_offset = 0
    reduced = "--video-style=reduced" in sys.argv
    talking = "--talking" in sys.argv
    dialogue = "--dialogue" in sys.argv
    styles = STYLES_DEFAUT
    for a in sys.argv[1:]:
        if a.startswith("--seed-offset="):
            seed_offset = int(a.split("=", 1)[1])  # reprise : autre tirage, meme graine de base + decalage
        if a.startswith("--styles="):
            styles = tuple(a.split("=", 1)[1].split(","))
    for st in styles:
        assert st in STYLE, f"style inconnu : {st}"
    args = [a for a in sys.argv[1:] if a not in ("--chain", "--video-style=reduced", "--talking", "--dialogue") and not a.startswith("--seed-offset=") and not a.startswith("--styles=")]
    sys.argv = [sys.argv[0]] + args
    img_dir = Path(sys.argv[1])
    jobs = []
    if dialogue:
        # sous-clips par locuteur, FLF2V départ = fin = image clé, styles A et B (C retiré le 22 août)
        neg_talk = ", ".join(x for x in (NEG_MOUVEMENT + ", " + NEG_PRESENCE).split(", ") if x not in NEG_TALKING_RETIRE)
        neg_idle = NEG_MOUVEMENT + ", " + NEG_PRESENCE
        for style in [st for st in styles if st in ("StyleA", "StyleB")]:
            red = reduced or style in STYLES_BLOC_REDUIT_OBLIGATOIRE
            for plan, subs in DIALOGUE.items():
                key = str(img_dir / style / f"{plan}_{style}.png")
                for sub, dur, pres, subject in subs:
                    jobs.append({
                        "name": f"{sub}_{style}", "clip": sub, "bloc": plan, "style": style, "mode": "flf2v",
                        "duration_s": dur, "length": LENGTH[dur], "start_image": key, "end_image": key,
                        "seed": seed_for(f"{sub}_{style}_dlg") + seed_offset, "presence": pres,
                        "prompt": motion_prompt(style, dur, subject, "static", pres, red),
                        "video_style": "reduced" if red else "fiche",
                        "negative": neg_talk if pres == "talking" else neg_idle, "settings": SETTINGS,
                        "output": f"clips-runpod/{style}/{sub}_{style}",
                    })
        Path(sys.argv[2]).write_text(json.dumps(jobs, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{len(jobs)} sous-clips de dialogue écrits dans {sys.argv[2]}")
        return
    if talking:
        # clips de dialogue : présence "talking", négatives sans lip sync / mouth articulation,
        # bloc de style réduit pour B (décision du 22 août, lot 3), bloc de la fiche pour A et C
        neg = ", ".join(x for x in (NEG_MOUVEMENT + ", " + NEG_PRESENCE).split(", ") if x not in NEG_TALKING_RETIRE)
        for style in styles:
            red = reduced or style in STYLES_BLOC_REDUIT_OBLIGATOIRE
            for clip, bloc, dur, subject, camera in TALK_CLIPS:
                jobs.append({
                    "name": f"{clip}_{style}", "clip": clip, "bloc": bloc, "style": style, "mode": "i2v",
                    "duration_s": dur, "length": LENGTH[dur],
                    "start_image": str(img_dir / style / f"{clip}_{style}.png"), "end_image": None,
                    "seed": seed_for(f"{clip}_{style}_talk") + seed_offset, "presence": "talking",
                    "prompt": motion_prompt(style, dur, subject, camera, "talking", red),
                    "video_style": "reduced" if red else "fiche", "negative": neg, "settings": SETTINGS,
                    "output": f"clips-runpod/{style}/{clip}_{style}_talk",
                })
        Path(sys.argv[2]).write_text(json.dumps(jobs, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{len(jobs)} jobs parlants écrits dans {sys.argv[2]}")
        return
    for style in styles:
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
    assert len(jobs) == len(CLIPS) * len(styles), f"{len(jobs)} clips pour {len(styles)} styles"
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
