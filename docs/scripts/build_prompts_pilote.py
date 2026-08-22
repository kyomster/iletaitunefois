#!/usr/bin/env python3
"""Assemble les 54 prompts d'image du pilote S01E01 (plans 1 à 6, trois styles).

Source unique des blocs : docs/S01E01-pilote-prompts-3-styles.md. Les blocs ci dessous
en sont la copie octet pour octet ; ils ne se reformulent jamais. Seules les briques de
plan (point 6) changent d'une image à l'autre.

Règle d'assemblage (point 1 de la fiche) :
  [STYLE scène] + [ÉPOQUE] + [brique, blocs identité substitués]
  + (si un personnage est réinjecté) "same characters as reference, same art style as reference"
  + " Avoid: " + [négatives de la brique (foule sur 1a, 1b, 2, 4a)] + [base style]
  + [base personnages d'époque] + [négative universelle]

Usage :
  python build_prompts_pilote.py <media_ids.json> <sortie.json> [<sortie.md>]

<media_ids.json> : {"D01_StyleA.png": "<media_id>", ...} (15 entrées, phase A du runbook).
"""
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------- point 2 : blocs de style, version plan de scène
STYLE = {
    "StyleA": "2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:",
    "StyleB": "inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:",
    "StyleC": "hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:",
}

# ---------------------------------------------------------------- point 3 : traitement d'époque
EPOQUE = {
    "StyleA": "historical period setting in desaturated muted earth tones, dusty beige, stone grey, earth brown, softened contrast, era accurate architecture and props,",
    "StyleB": "era accurate historical setting, moody atmospheric period palette,",
    "StyleC": "era accurate historical setting, palette shifted toward muted earth tones while keeping deep teal shadows,",
}

# ---------------------------------------------------------------- point 4 : négatives
NEG_UNIVERSELLE = "text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin"
NEG_EPOQUE = "dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing"
NEG_STYLE = {
    "StyleA": "gradient shading, soft shading, airbrush, painterly, thin delicate linework, photorealism, photograph, realistic skin texture, 3D render, CGI, live action, anime style, manga, corporate flat vector art, extra characters.",
    "StyleB": "plain round ball hands, hollow circle hands, teardrop hands, pointed armless stumps, separate fingers, realistic hands, missing hand, missing arm, realistic human anatomy, detailed face, nose, photorealism, 3D render, anime, manga, extra inkman characters.",
    "StyleC": "gradient shading, soft shading, airbrush, painterly, rendered highlights, digital painting, muddy colors, cold blue palette, violet palette, purple palette, photorealism, photograph, 3D render, CGI, live action, anime, manga, flat vector art, extra characters.",
}
NEG_FOULE = "readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures"
BLOCS_FOULE = {"1a", "1b", "2", "4a"}  # point 4.4
# Correction du 22 août 2026 (audit lot 1, docs/S01E01-pilote-audit.md) : sur P02, la négative de foule
# effaçait les visages des deux badauds nommés en style C. Elle est retirée sur ce plan, le bloc positif
# [FOULE] suffit. P02_StyleA et P02_StyleB validés avaient été produits AVEC la négative (version 1).
PLANS_SANS_NEG_FOULE = {"P02"}

# ---------------------------------------------------------------- point 5 : blocs identité
IDENT = {
    "GARNERIN": {
        "AC": "Garnerin, a French aeronaut of the Directoire era, resolute determined face with a calm set jaw, dark tailcoat, hair tied back, pale scarf at the neck, period breeches and buckled shoes, upright decided posture",
        "B": "Garnerin, an inkman stick figure character, a few ink strokes of hair tied back on his round head, simple black dot eyes with no eyebrows, resolute small mouth, wearing a dark Directoire tailcoat drawn as a simple flat shape, a pale scarf knotted at the neck, simple period shoes on his stick legs, upright decided posture",
    },
    "PARIEURS": {
        "AC": "the round onlooker wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; the thin onlooker leaning on a cane, threadbare coat, suspicious squint",
        "B": "the round bellied onlooker inkman with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his belly, peremptory raised chin; the thin onlooker inkman leaning on a cane, threadbare coat, suspicious half closed dot eyes",
    },
    "FOULE": {
        "AC": "a dozen Directoire crowd silhouettes, MOST OF THEM SEEN FROM BEHIND and the rest in three quarter view from behind, varied scales, NO FACE VISIBLE ON ANY FIGURE, no facial features at all: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, simplified figures less detailed than main characters",
        "B": "a dozen Directoire inkman crowd silhouettes, MOST OF THEM SEEN FROM BEHIND, varied scales, plain round BLANK heads with absolutely no facial features, NO EYES, no dots, no mouths, men with tall hats and simple flat tailcoats, women with high waisted dresses and shawls, a few small inkman children, simplified figures even less detailed than the main characters",
    },
    "AIDE": {
        "AC": "an assistant in a rough jacket with rolled up sleeves, seen from behind at the edge of frame",
        "B": "an inkman assistant in a rough flat jacket, seen from behind at the edge of frame",
    },
}
SAME_AS_REF = "same characters as reference, same art style as reference"

# ---------------------------------------------------------------- point 6 : briques d'image (identiques dans les trois styles)
# (nom de fichier sans style, bloc, brique)
BRIQUES = [
    ("P1a-1", "1a", "Scene: dawn mist drifting low over the lawns of Parc Monceau, a large inflated gas balloon swaying in the middle ground, a Directoire crowd gathered at its foot. Framing: very wide establishing shot, slight high angle. Decor: D1. Characters: [FOULE]. Props: balloon, wicker basket, ropes trailing on the grass."),
    ("P1a-2", "1a", "Scene: the inflated balloon swaying in the wind, mooring ropes pulling taut. Framing: medium shot on the balloon. Decor: D1. Characters: a few crowd figures at the lower edge, seen from behind. Props: balloon, taut ropes, stakes."),
    ("P1a-3", "1a", "Scene: banners snapping at the top of the balloon. Framing: low angle from the ground toward the crown of the balloon. Decor: D1, sky and treetops only. Characters: none. Props: balloon crown, netting, banners."),
    ("P1a-4", "1a", "Scene: the whole crowd turning their heads in one movement toward the wicker basket. Framing: very wide shot, slight high angle. Decor: D1. Characters: [FOULE]. Props: balloon, basket, ropes."),
    ("P1b-1", "1b", "Scene: the crowd parting into two lines, hats lifted. Framing: wide shot at eye level, down the axis of the lane. Decor: D1. Characters: [FOULE]. Props: hats, canes."),
    # Briques 1b-2, 1b-3 et P03 amendées le 22 août 2026 (décision Guillaume, audit : la plaque D01 impose un ballon
# avec sa nacelle, d'où deux nacelles à l'image). Version 1 : sans la clause « balloon hanging above / no other basket ».
    ("P1b-2", "1b", "Scene: the wicker basket carried forward by assistants, ropes trailing, toward the balloon hanging above with no basket under it yet. Framing: lateral medium shot. Decor: D1. Characters: two assistants in rough jackets, crowd behind them seen from behind. Props: ONE wicker basket, ropes."),
    ("P1b-3", "1b", "Scene: the basket being lashed under the balloon, hands knotting the ropes, the balloon is directly above this basket and out of frame. Framing: close shot on the knots. Decor: D1, blurred behind, no other balloon or basket in the background. Characters: hands and forearms only. Props: ropes, wicker rim, iron ring."),
    ("P02", "2", "Scene: two Directoire onlookers in the foreground leaning toward each other to make a bet, the basket and the crowd behind them. Framing: medium close shot at chest height, slightly low angle. Decor: D1. Characters: [PARIEURS], [FOULE] far behind. Props: cane, cockaded hats."),
    ("P03", "3", "Scene: inside the basket, Garnerin checking a large folded bundle of silk, his assistant speaking to him from the rim, the balloon is directly above this basket and out of frame. Framing: medium shot over the assistant's shoulder, the assistant in the foreground. Decor: D1 seen past the rim of the basket, no other balloon or basket in the background. Characters: [GARNERIN], [AIDE]. Props: folded silk bundle, ropes, a knife tucked at the side of the basket."),
    ("P4a-1", "4a", "Scene: the balloon tearing away from the ground, the released ropes falling back. Framing: very wide shot at crowd level, the backs of onlookers in the foreground. Decor: D1. Characters: [FOULE] from behind. Props: balloon, basket, falling ropes."),
    ("P4a-2", "4a", "Scene: the crowd rocking backwards to follow the balloon with their eyes, hats held on with both hands. Framing: medium shot on the crowd from behind and slightly to the side. Decor: D1. Characters: [FOULE]. Props: hats, shawls."),
    ("P4a-3", "4a", "Scene: the balloon rising and shrinking above the trees. Framing: wide low angle shot. Decor: D1, treetops and sky. Characters: none. Props: balloon, basket, trailing rope."),
    ("P4b-1", "4b", "Scene: seen from the basket, the rooftops of Paris sliding slowly below, chimney smoke streaming. Framing: very wide high angle shot, the rim of the basket in the foreground. Decor: D2. Characters: none. Props: wicker rim, rope, folded silk bundle."),
    ("P4b-2", "4b", "Scene: the wicker rim vibrating in the wind, a gloved hand tightening on it. Framing: close shot on the hand and the rim. Decor: D2, blurred sky behind. Characters: [GARNERIN], gloved hand only. Props: wicker rim, glove, rope."),
    ("P4b-3", "4b", "Scene: the whole city under the haze, the crowd reduced to a dark patch in the middle of the park. Framing: very wide high angle shot. Decor: D2. Characters: none. Props: none."),
    ("P5-1", "5", "Scene: a hand taking hold of the knife tucked at the side of the basket. Framing: very close shot. Decor: D2, out of focus behind. Characters: [GARNERIN], hand only. Props: knife, wicker side, taut rope."),
    # Briques 5-2 et 5-3 : « Decor: D2 » explicité le 22 août 2026 (en style A, sur ces très gros plans, le code D2 seul
# donnait un mur ou un panneau « D2 » ; B et C avaient le ciel). Brique 5-2 amendée le 22 août 2026 (audit : corde déjà tranchée en A et C, RÈGLE 7/13). Version 1 :
# "Scene: the blade sawing the taut rope, fibres springing free one by one. [...] Props: knife, rope, loose fibres."
    ("P5-2", "5", "Scene: the blade sawing the taut rope, the rope is still in ONE piece and taut, only a few outer fibres cut and springing free one by one, the blade halfway through. Framing: very close shot at a raking angle along the rope. Decor: D2, the sky and the rooftops of Paris far below, out of focus behind. Characters: hand only. Props: knife, one unbroken rope, loose fibres."),
    ("P5-3", "5", "Scene: the rope giving way at once, the strands whipping the air. Framing: very close frontal shot on the break. Decor: D2, the sky and the rooftops of Paris far below, out of focus behind. Characters: none. Props: severed rope, whipping strands."),
]

# ---------------------------------------------------------------- références par plan (runbook §4.1, ordre décor puis personnages)
REFS = {
    "P1a-1": ["D01", "Foule"], "P1a-2": ["D01", "Foule"], "P1a-3": ["D01"], "P1a-4": ["D01", "Foule"],  # 1a-2 : Foule ajoutée le 22 août 2026 (audit : dérive des figurants sans référence en A et B)
    "P1b-1": ["D01", "Foule"], "P1b-2": ["D01", "Foule"], "P1b-3": ["D01"],
    "P02": ["D01", "Parieurs", "Foule"],
    "P03": ["D01", "Garnerin"],
    "P4a-1": ["D01", "Foule", "Garnerin"], "P4a-2": ["D01", "Foule", "Garnerin"], "P4a-3": ["D01"],
    "P4b-1": ["D02"], "P4b-2": ["D02", "Garnerin"], "P4b-3": ["D02"],
    "P5-1": ["D02", "Garnerin"], "P5-2": ["D02"], "P5-3": ["D02"],
}
PERSONNAGES = {"Foule", "Garnerin", "Parieurs"}

GEN_PARAMS = {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1, "use_unlim": False}


def assemble(name, bloc, brique, style, media_ids):
    variant = "B" if style == "StyleB" else "AC"
    body = brique
    for key, blocs in IDENT.items():
        body = body.replace(f"[{key}]", blocs[variant])
    assert "[" not in body, f"substitution incomplète sur {name}"
    refs = REFS[name]
    positive = f"{STYLE[style]} {EPOQUE[style]} {body}"
    if any(r in PERSONNAGES for r in refs):
        positive += f" {SAME_AS_REF}"
    negs = []
    if bloc in BLOCS_FOULE and name not in PLANS_SANS_NEG_FOULE:
        negs.append(NEG_FOULE)
    negs += [NEG_STYLE[style], NEG_EPOQUE, NEG_UNIVERSELLE]
    prompt = f"{positive} Avoid: " + ", ".join(negs)
    medias = [{"role": "image_references", "value": media_ids[f"{r}_{style}.png"]} for r in refs]
    return {
        "name": f"{name}_{style}", "plan": name, "bloc": bloc, "style": style,
        "references": [f"{r}_{style}.png" for r in refs],
        "params": {**GEN_PARAMS, "prompt": prompt, "medias": medias},
    }


def main():
    media_ids = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = []
    for style in ("StyleA", "StyleB", "StyleC"):
        for name, bloc, brique in BRIQUES:
            out.append(assemble(name, bloc, brique, style, media_ids))
    assert len(out) == 54
    Path(sys.argv[2]).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    if len(sys.argv) > 3:
        md = ["# S01E01 — les 54 prompts du pilote, tels que soumis", "",
              "Générés par `docs/scripts/build_prompts_pilote.py` à partir des blocs de `S01E01-pilote-prompts-3-styles.md`. Réglages : `nano_banana_pro`, 16:9, 2k, count 1. Références dans l'ordre indiqué, rôle `image_references`.", ""]
        for e in out:
            md += [f"## {e['name']}", "", f"Références : {', '.join(e['references'])}", "", "```", e["params"]["prompt"], "```", ""]
        Path(sys.argv[3]).write_text("\n".join(md), encoding="utf-8", newline="\n")
    print(f"{len(out)} prompts écrits dans {sys.argv[2]}")


if __name__ == "__main__":
    main()
