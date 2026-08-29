#!/usr/bin/env python3
"""Assemble les prompts de RÉFÉRENCE du pilote (décors, personnages, objets de continuité) pour un style donné.

Ce qui manquait au dépôt : les 20 briques de plans étaient versionnées (`build_prompts_pilote.py`), pas les
cinq planches réinjectées ensuite sur ces plans. Écrit le 25 août 2026 pour le style P, valable pour tous.

Sources : blocs de style, d'époque et négatives de `build_prompts_pilote.py` ; blocs identité de
`docs/prompts/fiche-prompts-personnages-episode-S01E01.md` (§C.1 Garnerin, §C.3 Parieurs, §C.11 Foule) ;
plaques de décor D1/D2 telles que décrites dans les briques du pilote.

Règles appliquées : planches sur fond neutre (RÈGLE 15), aucun visage lisible dans la foule (RÈGLE 26),
couleurs nommées en positif sur les personnages (RÈGLES 30 et 34), aucun texte nulle part.

Objets de continuité : ajoutés le 26 août 2026 (RÈGLE 36). Tout élément qui doit être identique d'un plan à
l'autre se met en référence ; une description recopiée ne tient pas la continuité. Le ballon du pilote en est la
preuve : décrit avec les mêmes mots sur les 18 plans, il est sorti rayé crème de près et rayé orangé de loin.

Usage : python build_refs_pilote.py <sortie.json> --styles=StyleP [--refs=D01,Ballon]
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_prompts_pilote import STYLE, EPOQUE, NEG_STYLE, NEG_EPOQUE, NEG_UNIVERSELLE, NEG_FOULE, GEN_PARAMS, variante_identite  # noqa: E402

FOND = "on a plain neutral flat background, no scenery, no props other than those listed"
# 26 août 2026 : en style P, le fond neutre est sorti en ciel dégradé sur la planche de foule (RÈGLE 15 non
# tenue). Le fond se prescrit alors en positif, comme toute zone qu'un référent veut remplir.
FOND_DUR = ("on ONE SINGLE FLAT UNIFORM GREY BACKGROUND filling the whole frame behind the figures, "
            "no sky, no gradient, no horizon, no ground line, no scenery, no props other than those listed")

# Décors : plaques sans aucun personnage. Le texte est celui des briques du pilote, développé.
DECORS = {
    "D01": ("Scene: the location only, empty of people: October dawn 1797, low mist lying over the lawns of Parc Monceau, "
            "pale gravel paths, dark groves of trees, a large inflated gas balloon swaying in the middle ground, mooring ropes "
            "trailing on the grass, a wicker basket set down beside it, stone follies and low buildings in the distance. "
            "Framing: wide establishing shot at eye level. Characters: none, absolutely no person anywhere in the frame. "
            "Props: balloon, netting, wicker basket, ropes."),
    "D02": ("Scene: the location only, empty of people, seen from high in the air: pale morning sky over Paris, grey slate rooftops "
            "and smoking chimneys far below, straight streets, the park visible as a bright green patch, light haze thickening "
            "toward the horizon. Framing: very wide high angle plate. Characters: none, absolutely no person anywhere in the frame. "
            "Props: rooftops, chimneys."),
}

# Personnages : blocs identité de la fiche, variante AC (styles dessinés) ou B (inkman).
IDENT = {
    "Foule": {
        # 26 août 2026, RÈGLE 37 : sur un style à aplats, demander l'absence de traits donne un visage noirci.
        "P": ("a dozen Directoire crowd figures, EVERY SINGLE ONE SEEN STRICTLY FROM DIRECTLY BEHIND with the back of the head "
              "squarely toward the camera, no cheek, no jaw, no ear and no profile visible on any of them, so that no face exists "
              "anywhere in the image, varied scales; the small areas of skin that do show, a nape or a hand, are drawn in the SAME "
              "EVENLY LIT FLESH TONE as the main characters, never filled with black, never covered by shadow: men in tailcoats and "
              "tall hats, women in high waisted dresses and shawls, a few children, one closed umbrella, simplified figures less "
              "detailed than main characters"),
        "AC": ("a dozen Directoire crowd silhouettes, MOST OF THEM SEEN FROM BEHIND and the rest in three quarter view from behind, "
               "varied scales, NO FACE VISIBLE ON ANY FIGURE, no facial features at all: men in tailcoats and tall hats, women in "
               "high waisted dresses and shawls, a few children, one closed umbrella, simplified figures less detailed than main characters"),
        "B": ("a dozen Directoire inkman crowd silhouettes, MOST OF THEM SEEN FROM BEHIND, varied scales, plain round BLANK heads with "
              "absolutely no facial features, NO EYES, no dots, no mouths, men with tall hats and simple flat tailcoats, women with high "
              "waisted dresses and shawls, a few small inkman children, one closed umbrella, simplified figures even less detailed than the main characters"),
    },
    "Garnerin": {
        "AC": ("Garnerin, a French aeronaut of the Directoire era, resolute determined face with a calm set jaw, dark tailcoat, hair tied back, "
               "pale scarf at the neck, period breeches and buckled shoes, upright decided posture, shown in four views at the same scale: "
               "front, three quarter, profile and back"),
        "B": ("Garnerin, an inkman stick figure character, a few ink strokes of hair tied back on his round head, simple black dot eyes with no "
              "eyebrows, resolute small mouth, wearing a dark Directoire tailcoat drawn as a simple flat shape, a pale scarf knotted at the neck, "
              "simple period shoes on his stick legs, upright decided posture, shown in four views at the same scale: front, three quarter, profile and back"),
    },
    "Parieurs": {
        "AC": ("the two Directoire onlookers standing side by side, full body, three quarter view, at the same scale: the round onlooker on the left "
               "wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; "
               "the thin onlooker on the right leaning on a cane, threadbare coat in muted brown and grey only, no blue and no green on any garment, "
               "suspicious squint"),
        "B": ("the two Directoire onlooker inkman characters standing side by side, full body, three quarter view, at the same scale: the round bellied "
              "onlooker on the left with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his "
              "belly, peremptory raised chin; the thin onlooker on the right leaning on a cane, threadbare coat in muted brown and grey only, "
              "suspicious half closed dot eyes"),
    },
}
# Objets de continuité : planche d'objet seul sur fond neutre, réinjectée au rang accessoires (RÈGLE 36).
OBJETS = {
    # Décrit d'après les clés déjà validées (P1a-3 au plus près), pas inventé : la planche doit ramener les plans
    # vers le ballon qui existe déjà à l'écran, pas en imposer un nouveau.
    # 26 août 2026 : deuxième objet de continuité. La nacelle changeait de forme d'un plan à l'autre — ronde à
    # rebord épais, rectangulaire à couvercle, rectangulaire à panneaux. Deux vues, parce que la moitié des plans
    # la montrent de l'intérieur : une planche extérieure seule ne tiendrait pas les plans depuis la nacelle.
    "Nacelle": ("Scene: the object alone, shown in TWO views side by side at the same scale on the same plain background, "
                "clearly separated: on the LEFT the basket seen from outside in three quarter view, on the RIGHT the same "
                "basket seen from above with its interior visible. It is a deep ROUND wicker gondola of 1797, natural honey "
                "coloured wicker woven in even horizontal bands, a THICK ROLLED RIM wrapped in rope running all the way "
                "around the top, four suspension ropes rising from the rim at the quarters and knotted to iron rings, two "
                "small sandbags hanging outside against the wall, a plain flat floor of woven wicker inside, nothing else "
                "in the basket, {fond}. Framing: the two views at the same scale, the whole object visible in each. "
                "Characters: none, absolutely no person and no hand anywhere in the frame."),
    "Ballon": ("Scene: the object alone: a large inflated hydrogen balloon of 1797, tall rounded envelope narrowing toward the "
               "bottom, made of alternating vertical silk gores in dusty rose and pale sage green, each gore ending in a pointed "
               "lancet arch at the widest part of the envelope, a diamond mesh rope net thrown over the upper half, a horizontal "
               "rope band circling the envelope at its widest point, the suspension ropes converging below to a wooden hoop, a "
               "round wicker basket hanging from the hoop, a mooring rope trailing from the basket, {fond}. Framing: the whole "
               "object seen from top to bottom, centred in frame, slight low angle. Characters: none, absolutely no person "
               "anywhere in the frame."),
}
CADRAGE = {"Foule": "Framing: full body group, all figures at the same scale.",
           "Garnerin": "Framing: character sheet, four full body views in a row at the same scale.",
           "Parieurs": "Framing: full body pair, both at the same scale."}


def assemble_ref(nom, style):
    variant = variante_identite(style)
    fond = FOND_DUR if variant == "P" else FOND
    if nom in DECORS:
        body = DECORS[nom]
        negs = [NEG_STYLE[style], NEG_EPOQUE, NEG_UNIVERSELLE]
    elif nom in OBJETS:
        body = OBJETS[nom].format(fond=fond)
        negs = [NEG_STYLE[style], NEG_EPOQUE, NEG_UNIVERSELLE]
    else:
        body = f"Scene: {IDENT[nom].get(variant, IDENT[nom]['AC'])}, {fond}. {CADRAGE[nom]}"
        negs = ([NEG_FOULE.get(variant, NEG_FOULE["defaut"])] if nom == "Foule" else []) + [NEG_STYLE[style], NEG_EPOQUE, NEG_UNIVERSELLE]
    positive = " ".join(x for x in (STYLE[style], EPOQUE[style], body) if x)
    # 26 août 2026 : les négatives se joignent par une virgule. Collées par une espace, la négative de foule
    # (qui ne finit pas par un point) se soudait à la négative de style : « silhouette head paper grain ».
    return {"name": f"{nom}_{style}", "reference": nom, "style": style,
            "params": {**GEN_PARAMS, "prompt": positive + " Avoid: " + ", ".join(n.rstrip(". ") for n in negs) + "."}}


DEFAUT = ("D01", "D02", "Foule", "Garnerin", "Parieurs", "Ballon")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    styles, refs = ["StyleP"], list(DEFAUT)
    for a in sys.argv[1:]:
        if a.startswith("--styles="):
            styles = a.split("=", 1)[1].split(",")
        if a.startswith("--refs="):
            refs = a.split("=", 1)[1].split(",")
    out = [assemble_ref(n, s) for s in styles for n in refs]
    Path(args[0]).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(out)} prompts de référence écrits dans {args[0]} ({', '.join(styles)})")


if __name__ == "__main__":
    main()
