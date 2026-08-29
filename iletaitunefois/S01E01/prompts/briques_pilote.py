#!/usr/bin/env python3
"""Briques de S01E01, plans 1 à 6 (le pilote) — tout ce qui est propre à cet épisode dans l'assemblage des prompts.

Ce module est chargé par `atelier/scripts/assembler_prompts.py`, `assembler_refs.py` et `assembler_clips.py`.
Les blocs de style, eux, viennent de `styles/*/style.json`. Rien ici ne se reformule : chaque brique porte,
en commentaire, la date et la raison de sa dernière modification (RÈGLE 41 : toute règle du script est aussi
écrite en clair dans `atelier/METHODE-generation-images.md`).

Chaîne physique de la scène et rôles : `../logique-ouverture-froide.md`. Descriptions canoniques des objets :
`assets-et-objets.md` §7.
"""

SERIE, EPISODE = "iletaitunefois", "S01E01"

# ---------------------------------------------------------------- blocs identité, par variante de style
# AC = styles dessinés, B = inkman, JK = rendus réalistes (matériau plutôt que teinte, RÈGLE 34), P = aplats (RÈGLE 37).
# Un style sans entrée propre retombe sur AC.
IDENT = {
    "GARNERIN": {
        "AC": "Garnerin, a French aeronaut of the Directoire era, resolute determined face with a calm set jaw, dark tailcoat, hair tied back, pale scarf at the neck, period breeches and buckled shoes, upright decided posture",
        "B": "Garnerin, an inkman stick figure character, a few ink strokes of hair tied back on his round head, simple black dot eyes with no eyebrows, resolute mouth drawn as one short flat ink line, closed, wearing a dark Directoire tailcoat drawn as a simple flat shape, a pale scarf knotted at the neck, simple period shoes on his stick legs, upright decided posture",
    },
    # 23 août 2026 : le manteau du maigre sortait en sarcelle désaturé (couleur réservée) → couleur nommée en positif (RÈGLE 30) ;
    # 24 août : sur le photoréalisme la teinte ne tient pas → matériau et usure (variante JK, corollaire RÈGLE 34).
    "PARIEURS": {
        "AC": "the round onlooker wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; the thin onlooker leaning on a cane, threadbare coat in muted brown and grey only, no blue and no green on any garment, suspicious squint",
        "B": "the round bellied onlooker inkman with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his belly, peremptory raised chin; the thin onlooker inkman leaning on a cane, threadbare coat, suspicious half closed dot eyes",
        "JK": "the round onlooker wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; the thin onlooker leaning on a cane, his coat made of undyed coarse brown wool, worn thin and patched at the elbows, the colour of raw sacking and dust, no dyed fabric on him, suspicious squint",
    },
    "PARIEURS_ROND": {
        "AC": "the round onlooker wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air",
        "B": "the round bellied onlooker inkman with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his belly, peremptory raised chin",
    },
    "PARIEURS_MAIGRE": {
        "AC": "the thin onlooker leaning on a cane, threadbare coat in muted brown and grey only, no blue and no green on any garment, suspicious squint",
        "B": "the thin onlooker inkman leaning on a cane, threadbare coat, suspicious half closed dot eyes",
        "JK": "the thin onlooker leaning on a cane, his coat made of undyed coarse brown wool, worn thin and patched at the elbows, the colour of raw sacking and dust, no dyed fabric on him, suspicious squint",
    },
    "FOULE": {
        "AC": "a dozen Directoire crowd silhouettes, MOST OF THEM SEEN FROM BEHIND and the rest in three quarter view from behind, varied scales, NO FACE VISIBLE ON ANY FIGURE, no facial features at all: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, simplified figures less detailed than main characters",
        "B": "a dozen Directoire inkman crowd silhouettes, MOST OF THEM SEEN FROM BEHIND, varied scales, plain round BLANK heads with absolutely no facial features, NO EYES, no dots, no mouths, men with tall hats and simple flat tailcoats, women with high waisted dresses and shawls, a few small inkman children, simplified figures even less detailed than the main characters",
        # 23 août 2026 : sur J et K la clause AC n'a pas tenu (figurants nets, de face) → durcie en positif.
        "JK": "a dozen Directoire crowd figures, ALL SEEN FROM BEHIND, turned toward the balloon, NO FIGURE FACING THE CAMERA, thrown out of focus by the shallow depth of field, no readable face on any background figure: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, much less detailed than the main characters",
        # 26 août 2026, RÈGLE 37 : sur un style à aplats « aucun trait » donne un visage noirci → on retire la zone, on nomme la carnation.
        "P": "a dozen Directoire crowd figures, EVERY SINGLE ONE SEEN STRICTLY FROM DIRECTLY BEHIND with the back of the head squarely toward the camera, no cheek, no jaw, no ear and no profile visible on any of them, so that no face exists anywhere in the image, turned toward the balloon; the small areas of skin that do show, a nape or a hand, are drawn in the SAME EVENLY LIT FLESH TONE as the main characters, never filled with black, never covered by shadow: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, simplified figures less detailed than the main characters",
    },
    "AIDE": {
        "AC": "an assistant in a rough jacket with rolled up sleeves, seen from behind at the edge of frame",
        "B": "an inkman assistant in a rough flat jacket, seen from behind at the edge of frame",
    },
    "AIDE_FACE": {
        "AC": "an assistant in a rough jacket with rolled up sleeves, his plain honest face fully visible, short hair, calm attentive expression",
        "B": "an inkman assistant in a rough flat jacket, his round white head fully visible with simple dot eyes and a closed mouth drawn as one short flat ink line",
    },
}
PERSONNAGES = {"Foule", "Garnerin", "Parieurs"}  # références qui déclenchent « same characters as reference »

# ---------------------------------------------------------------- négatives propres à l'épisode
NEG_FOULE = {
    "defaut": "readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures",
    "P": ("readable faces, portraits, recognisable face on a crowd figure, front facing figure, three quarter face, "
          "profile face on a crowd figure, face filled with flat black, blacked out face, head painted as a solid dark shape, "
          "face hidden in solid shadow, silhouette head"),
    # sur P02 la négative de foule efface les visages des badauds nommés (22 août) ; en P on garde la seule partie anti-aplat.
    "P_plans_nommes": ("face filled with flat black, blacked out face, head painted as a solid dark shape, "
                       "face hidden in solid shadow, silhouette head"),
}
BLOCS_FOULE = {"1a", "1b", "2", "4a"}
PLANS_SANS_NEG_FOULE = {"P02", "P02a", "P02b"}
# 27 août 2026 : le nom « parachute » ramène le dôme ouvert (corollaire RÈGLE 42) ; l'état fermé a sa négative.
NEG_PARACHUTE_FERME = "open parachute, deployed parachute, parachute canopy, dome of silk, spread umbrella, inflated silk"
NEG_PLAN = {p: [NEG_PARACHUTE_FERME] for p in ("P1b-2", "P1b-3", "P02", "P03", "P4a-1", "P4a-3", "P4b-1", "P5-1", "P5-2")}

# ---------------------------------------------------------------- clauses ajoutées à certains plans
# (texte, plans, référence requise ou None). RÈGLE 29 : deux références qui montrent le même objet en donnent deux.
CLAUSES = [
    ("plain undecorated banners with no emblem and no lettering, blank fabric only", {"P1a-3"}, None),  # RÈGLE 33, tous styles
    ("ONE single gas balloon only, exactly the one shown in the balloon reference, identical envelope shape and identical stripe colours, no second balloon anywhere in the frame",
     {"P1a-1", "P1a-2", "P1a-3", "P1a-4", "P1b-1", "P1b-2", "P02", "P4a-1", "P4a-2", "P4a-3", "P5-1", "P5-2", "P5-3"}, "Ballon"),
    ("ONE single wicker basket only, exactly the one shown in the basket reference: round, deep, honey coloured wicker in even horizontal bands, thick rope wrapped rim, four suspension ropes at the quarters, sandbags outside, deep enough to reach a standing man's waist and wide enough for two men to stand in it side by side, barely wider than it is deep; no second basket, no crate, no rectangular hamper and no lid anywhere in the frame",
     {"P1b-2", "P1b-3", "P02", "P03", "P4a-1", "P4b-1", "P4b-2", "P5-1", "P5-2", "P5-3"}, "Nacelle"),
    # 27 août 2026 : le parachute est GRÉÉ entre le ballon et la nacelle, replié ; jamais un paquet au plancher (logique §1).
    ("the folded parachute hangs BETWEEN the balloon and the basket. It is STILL CLOSED: a long narrow vertical bundle of cream silk, no wider than a man's shoulders, tightly strapped at three points along its length and tapering to a point at the bottom, like a tightly furled umbrella stood on end. IT DOES NOT FORM A DOME AND IT IS NOT SPREAD: no canopy, no open parachute, no umbrella shape, no wide silk above the basket. Its lines run down to the rim of the basket and its crown is roped up to the balloon; the silk is never a bundle lying on the floor of the basket",
     {"P1b-2", "P1b-3", "P02", "P03", "P4a-1", "P4a-3", "P4b-1", "P5-1", "P5-2"}, None),
]

# ---------------------------------------------------------------- cadrages durcis (RÈGLES 28, 32, 39) : on décrit ce que le cadre CONTIENT
CADRAGE_DURCI = {
    "P5-1": "No face, no head, no shoulders and no full body anywhere in the frame: only the hand, the forearm, the woven side of the basket, the rope and the sky.",
    "P1a-3": "The camera is tilted steeply upward from directly below; the crown of the balloon fills the upper half of the frame and the ground is not visible at all.",
    "P4a-2": "EXACTLY THREE onlookers are visible and no one else, seen from close behind at shoulder height, their heads and shoulders filling the lower half of the frame; no fourth figure anywhere, no wide crowd.",
}

# ---------------------------------------------------------------- registre de lumière par bloc (pour les styles qui en ont)
REGISTRE_LUMIERE = {"1a": "JOUR", "1b": "JOUR", "2": "JOUR", "3": "JOUR", "4a": "JOUR", "4b": "TENSION", "5": "TENSION"}

# ---------------------------------------------------------------- briques de plan : (nom, bloc, brique)
BRIQUES = [
    # bloc 1a : le ballon SEUL, amarré — la nacelle et le parachute n'arrivent qu'au 1b-2 (27 août, vérification plan par plan)
    ("P1a-1", "1a", "Scene: dawn mist drifting low over the lawns of Parc Monceau, a large inflated gas balloon swaying in the middle ground, a Directoire crowd gathered at its foot. Framing: very wide establishing shot, slight high angle. Decor: D1. Characters: [FOULE]. Props: mooring ropes trailing on the grass and pegged down. THE BALLOON HANGS ALONE: there is NO basket and NO parachute under it yet, nothing hangs below the hoop, they are brought in later; no basket and no crate anywhere in the frame."),
    ("P1a-2", "1a", "Scene: the inflated balloon swaying in the wind at dawn, its envelope made of alternating vertical gores in DUSTY ROSE and PALE SAGE GREEN under a diamond rope net, mooring ropes pulling taut, NOTHING HANGING UNDER IT YET. Framing: medium shot on the balloon. Decor: D1, October dawn, low mist over the lawns, pale peach and grey sky, soft hazy light, no blue sky, no midday sun. Characters: a few crowd figures at the lower edge, seen from behind. Props: balloon, taut mooring ropes, stakes. The balloon hangs alone: no basket and no parachute under the hoop."),
    ("P1a-3", "1a", "Scene: banners snapping at the top of the balloon. Framing: low angle from the ground toward the crown of the balloon. Decor: D1, sky and treetops only. Characters: none. Props: balloon crown, netting, banners."),
    ("P1a-4", "1a", "Scene: the whole crowd turning their heads in one movement toward the balloon. Framing: medium shot at head height on the backs of a few onlookers, hats and bonnets filling the lower half, the balloon and its mooring ropes beyond them, nothing hanging under the balloon yet. Decor: D1. Characters: [FOULE]. Props: mooring ropes, hats. The balloon hangs alone: no basket and no parachute under the hoop."),
    ("P1b-1", "1b", "Scene: the crowd stepping aside to open a clear lane down the middle of the frame, the people on each side turning to look down that lane, hands at their sides. Framing: wide shot at eye level, down the axis of the lane. Decor: D1, October dawn, low mist, at the end of the lane the balloon, its envelope made of alternating vertical gores in DUSTY ROSE and PALE SAGE GREEN under a diamond rope net, with nothing hanging under it yet. Characters: [FOULE]. Props: hats worn on the heads, canes. No hand touches a hat. The balloon hangs alone: no basket and no parachute under the hoop."),
    ("P1b-2", "1b", "Scene: two assistants carrying the wicker basket forward toward the balloon hanging above with nothing under it yet, a third assistant walking beside them carrying THE FOLDED PARACHUTE, a long bound bundle of cream silk closed like a furled umbrella, ropes trailing behind them. Framing: lateral medium shot. Decor: D1. Characters: three assistants in rough jackets, crowd behind them seen from behind. Props: ONE wicker basket, ONE folded parachute, ropes."),
    ("P1b-3", "1b", "Scene: the rig being tied together, hands knotting the parachute lines to the iron rings of the basket rim, THE FOLDED PARACHUTE hanging just above the rim as a long bound bundle of cream silk closed like a furled umbrella, its crown roped up toward the balloon which is out of frame above. Framing: close shot on the knotting hands, the rim across the bottom, the lower end of the folded parachute filling the upper part of the frame. Decor: D1, blurred behind, no other balloon or basket in the background. Characters: hands and forearms only. Props: parachute lines, folded parachute, wicker rim, iron rings."),
    ("P02", "2", "Scene: two Directoire onlookers in the foreground leaning toward each other to make a bet, both with their mouths firmly closed in a neutral pause, hands down, behind them the whole rig at rest, MUCH LARGER THAN THE MEN: the balloon towering over the lawn, THE FOLDED PARACHUTE hanging under it as a long narrow closed bundle, and the basket under the parachute resting on the grass, with the crowd around it. Framing: medium close shot at chest height, slightly low angle. Decor: D1. Characters: [PARIEURS], [FOULE] far behind. Props: cane, cockaded hats."),
    ("P02a", "2", "Scene: close shot on the round onlooker alone as he speaks, his hand down, his mouth clearly visible, the top hat with the tricolour cockade, the thin onlooker out of frame, the crowd and the basket far behind. Framing: close shot at shoulder height, slightly low angle. Decor: D1. Characters: [PARIEURS_ROND]. Props: cockaded hat."),
    ("P02b", "2", "Scene: close shot on the thin onlooker alone as he answers, leaning on his cane, his mouth clearly visible, the round onlooker out of frame, the crowd and the basket far behind. Framing: close shot at shoulder height, slightly low angle. Decor: D1. Characters: [PARIEURS_MAIGRE]. Props: cane."),
    # P03 : l'action porte la réplique (main sur la corde de largage) ; l'aide DEHORS, au sol ; amarres tenues = destinataire de « Lâchez tout »
    ("P03", "3", "Scene: inside the basket, Garnerin standing at the release rope, one gloved hand gripping the taut rope above his head, looking up toward the balloon with his jaw set, his assistant STANDING ON THE GRASS OUTSIDE THE BASKET on the other side, both hands on the outer rim, leaning in and pleading with one open hand, the basket wall between them, BOTH FACES FULLY VISIBLE to the camera in three quarter view, both with their mouths firmly closed, the balloon is directly above this basket and out of frame. Framing: medium two shot from the side at chest height, Garnerin on the left inside the basket, the assistant on the right outside it standing on the ground, the lawn and the mist clearly visible behind them so the basket is plainly still on the ground, two taut mooring ropes entering the bottom of the frame and held by crew hands at the very edge of the image. Decor: D1 seen past the rim of the basket, no other balloon or basket in the background. Characters: [GARNERIN], [AIDE_FACE]. Props: taut release rope, THE FOLDED PARACHUTE hanging above the basket as a bound bundle of cream silk closed like a furled umbrella, its lines coming down to the rim, mooring ropes held by crew hands, a knife tucked at the side of the basket."),
    ("P4a-1", "4a", "Scene: the balloon tearing away from the ground, the released mooring ropes falling back to the grass, GARNERIN VISIBLE IN THE BASKET, head and shoulders above the rim, one hand on the rim, looking up. Framing: low angle from the ground, the balloon, the folded parachute and the basket filling the frame as they lift off, no onlooker in the frame. Decor: D1, treetops and sky. Characters: [GARNERIN], head and shoulders only, inside the basket. Props: balloon, folded parachute, basket, falling mooring ropes."),
    # 4a-2 : main en visière et non au chapeau (corollaire RÈGLE 40 : quand deux actions donnent la même image, on change l'action)
    ("P4a-2", "4a", "Scene: three onlookers rocking backwards to follow the balloon with their eyes, each shading their eyes with ONE FLAT HAND held above the eyebrows like a visor, palm down, no hand touching any hat, their coats in muted brown, grey and dark green only, no bright color on any garment, the balloon just above the treetops, still large, rising away. Framing: close shot on the backs and shoulders of three onlookers, low angle. Decor: D1. Characters: [FOULE]. Props: hats, shawls."),
    ("P4a-3", "4a", "Scene: the balloon rising and shrinking above the trees, the whole rig visible in one piece: the balloon on top, the folded parachute hanging below it as a long narrow closed bundle, the basket hanging below the parachute. Framing: wide low angle shot. Decor: D1, treetops and sky. Characters: none. Props: balloon, folded parachute, basket, trailing rope."),
    ("P4b-1", "4b", "Scene: seen from the basket, the rooftops of Paris sliding slowly below, chimney smoke streaming. Framing: very wide high angle shot, the rim of the basket in the foreground. Decor: D2. Characters: none. Props: wicker rim, the parachute lines rising from the rim and leaving the top of the frame."),
    ("P4b-2", "4b", "Scene: the wicker rim vibrating in the wind, a gloved hand tightening on it. Framing: close shot on the hand and the rim. Decor: D2, blurred sky behind. Characters: [GARNERIN], gloved hand only. Props: wicker rim, glove, rope."),
    ("P4b-3", "4b", "Scene: the whole city under the haze, much higher and farther than before, the park a small green rectangle with the crowd reduced to a dark patch in its middle. Framing: very wide high angle shot from far above, no basket and no rim in the frame. Decor: D2, the rooftops of Paris under the haze. Characters: none, no person anywhere. Props: none."),
    # bloc 5 : RÈGLE 39, au moins un plan tient dans le même cadre les deux termes de la relation (nacelle, parachute, corde, ballon)
    ("P5-1", "5", "Scene: seen from INSIDE the basket: Garnerin's arm in his dark sleeve comes from inside the basket and his hand takes hold of the knife sheathed against the inner wicker wall, the woven rim of the basket in the foreground, the parachute lines rising from the rim to the closed folded parachute just above, and above it the single taut rope that ties the parachute crown to the balloon. Framing: close shot from inside the basket, tilted up so the eye follows the lines to the folded parachute and to the rope above it, the underside of the balloon showing at the very top of the frame. Decor: D2, the sky and the rooftops of Paris far below, out of focus beyond the rim, no other balloon and no other basket anywhere in the frame. Characters: [GARNERIN], one hand and forearm only, clearly reaching from inside the basket. Props: knife, inner wicker wall, taut rope."),
    ("P5-2", "5", "Scene: Garnerin's arm reaching up from INSIDE the basket, over the woven rim visible at the bottom of the frame, the blade sawing the single taut rope that ties the crown of the folded parachute to the balloon, the rope still in ONE piece and taut, only a few outer fibres cut and springing free one by one, the blade halfway through. Framing: medium close shot from inside the basket at a low angle, the woven rim running across the bottom of the frame, the closed folded parachute hanging just above the basket and, above it, the single taut rope reaching the balloon, all three clearly visible in the same frame, so that what the blade is cutting is the ONE rope holding the parachute, and the basket under it, to that balloon. Decor: D2, the sky and the rooftops of Paris far below, out of focus behind. Characters: ONE hand only, Garnerin's hand in his dark sleeve reaching from inside the basket, no second hand, the taut rope is fixed to the rim of the basket. Props: knife, one unbroken rope, the folded parachute, loose fibres, woven rim."),
    ("P5-3", "5", "Scene: the rope has given way, the cut strands whipping the air, the balloon leaping away and shrinking at the top of the frame while below it the parachute has opened into a wide dome of cream silk and the wicker basket hangs under the dome on its lines, falling. Framing: ONE SINGLE WIDE IMAGE THAT FILLS THE ENTIRE 16:9 FRAME EDGE TO EDGE, no vertical bands, no panels, no split screen, no blurred borders: a single continuous sky across the whole width, the balloon high at the top, the open parachute and the basket in the middle, the rooftops of Paris far below across the bottom. Decor: D2, the rooftops of Paris far below, out of focus behind. Characters: none. Props: severed rope, whipping strands, the open parachute dome, the wicker basket hanging under it, balloon rising away."),
]

# ---------------------------------------------------------------- références par plan (décor, personnages, accessoires — sept au plus)
# RÈGLE 36 et corollaires : une planche d'objet ne se pose que sur les plans où l'objet est VISIBLE.
REFS = {
    "P1a-1": ["D01", "Foule", "Ballon"], "P1a-2": ["D01", "Foule", "Ballon"], "P1a-3": ["D01", "Ballon"], "P1a-4": ["D01", "Foule", "Ballon"],
    "P1b-1": ["D01", "Foule", "Ballon"], "P1b-2": ["D01", "Foule", "Ballon", "Nacelle"], "P1b-3": ["D01", "Nacelle"],
    "P02": ["D01", "Parieurs", "Foule", "Ballon", "Nacelle"], "P02a": ["D01", "Parieurs"], "P02b": ["D01", "Parieurs"],
    "P03": ["D01", "Garnerin", "Nacelle"],
    "P4a-1": ["D01", "Ballon", "Nacelle"], "P4a-2": ["D01", "Foule", "Garnerin", "Ballon"], "P4a-3": ["D01", "Ballon"],
    "P4b-1": ["D02", "Nacelle"], "P4b-2": ["D02", "Garnerin", "Nacelle"], "P4b-3": ["D02"],
    "P5-1": ["D02", "Garnerin", "Nacelle", "Ballon"], "P5-2": ["D02", "Nacelle", "Ballon"], "P5-3": ["D02", "Nacelle", "Ballon"],
}

# ---------------------------------------------------------------- planches de référence (assembler_refs.py)
FOND = "on a plain neutral flat background, no scenery, no props other than those listed"
FOND_DUR = ("on ONE SINGLE FLAT UNIFORM GREY BACKGROUND filling the whole frame behind the figures, "
            "no sky, no gradient, no horizon, no ground line, no scenery, no props other than those listed")  # RÈGLE 15 durcie (P)
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
IDENT_REFS = {
    "Foule": {
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
        "AC": IDENT["GARNERIN"]["AC"] + ", shown in four views at the same scale: front, three quarter, profile and back",
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
CADRAGE_REFS = {"Foule": "Framing: full body group, all figures at the same scale.",
                "Garnerin": "Framing: character sheet, four full body views in a row at the same scale.",
                "Parieurs": "Framing: full body pair, both at the same scale."}
# Objets de continuité (RÈGLE 36, descriptions canoniques RÈGLES 38 et 42 dans assets-et-objets.md §7).
OBJETS = {
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
REFS_DEFAUT = ("D01", "D02", "Foule", "Garnerin", "Parieurs", "Ballon", "Nacelle")

# ---------------------------------------------------------------- clips (assembler_clips.py) : (clip, bloc, durée s, sujet, caméra)
# Sujets nettoyés le 27 août 2026 (une seule action, RÈGLE 13). Les prompts EXACTEMENT rendus pour le montage v7, avec leurs
# graines, sont dans `clips-StyleP.json` : c'est la pièce d'archive, ceci est le point de départ de la prochaine génération.
CLIPS = [
    ("P1a-1", "1a", 2.375, "The mist drifts slowly across the lawns, the crowd sways gently at the foot of the balloon", "static"),
    ("P1a-2", "1a", 2.375, "The balloon sways in the wind, the mooring ropes pull taut and slacken", "static"),
    ("P1a-3", "1a", 2.0, "The banners snap in the wind at the crown of the balloon", "static"),
    ("P1a-4", "1a", 2.0, "The crowd turns their heads in one movement toward the balloon", "static"),
    ("P1b-1", "1b", 3.0, "The two lines of people step further apart and the lane between them opens wider, everyone keeping their hands down at their sides and their hats on their heads; no arm is raised and no hand goes near a hat", "static"),
    ("P1b-2", "1b", 3.0, "The basket and the folded parachute are carried forward, ropes trailing on the grass", "slow lateral tracking to the right, following the basket"),
    ("P1b-3", "1b", 3.0, "Hands knot the parachute lines to the rings of the wicker rim", "static"),
    ("P4a-1", "4a", 3.0, "The rig rises steadily: balloon, folded parachute and basket together, Garnerin motionless in the basket, the mooring ropes falling back onto the grass", "static"),
    ("P4a-2", "4a", 3.0, "The three onlookers lean backwards to follow the balloon with their eyes, each keeping one flat hand held above the eyebrows like a visor, palm down; no hand ever touches a hat", "static"),
    ("P4a-3", "4a", 4.0, "The balloon rises and shrinks above the trees, the whole rig in one piece", "very slow tilt upward, following the balloon"),
    ("P4b-1", "4b", 3.375, "The rooftops slide slowly below, chimney smoke streams sideways", "static"),
    ("P4b-2", "4b", 3.375, "The wicker rim vibrates, the gloved hand tightens on it", "static"),
    ("P4b-3", "4b", 3.0, "The haze drifts over the city, the dark patch of the crowd stays still", "very slow zoom out"),
    ("P5-1", "5", 2.375, "The hand takes hold of the knife", "static"),
    ("P5-2", "5", 3.0, "The blade saws the rope, fibres spring free one by one", "static"),
    ("P5-3", "5", 2.375, "The cut cords whip, the balloon climbs away and shrinks, the open parachute sways gently and the basket swings under it", "static"),
]
PRESENCE = {"P1a-1": "crowd", "P1a-2": "crowd", "P1a-3": "none", "P1a-4": "crowd", "P1b-1": "crowd", "P1b-2": "character",
            "P1b-3": "hands", "P4a-1": "character", "P4a-2": "crowd", "P4a-3": "none", "P4b-1": "none", "P4b-2": "hands",
            "P4b-3": "none", "P5-1": "hands", "P5-2": "hands", "P5-3": "none"}
# Plans de dialogue, voix libres : le sujet cite les répliques EXACTES entre guillemets, avec langue et timbre (STRATEGIE §4.6).
DIALOGUES = {
    "P02": ("2", 8.0, "historical Paris park 1797, a crowd watching a hot air balloon. Two onlookers in the foreground talk, static camera, single continuous shot, no cut. First both watch in silence. Then the stout man on the left with the cockade on his hat says in French, grave voice: \"Il va se tuer, je vous dis.\" while the thin man on the right listens with his mouth closed. Then the thin man on the right answers in French, clear voice: \"Dix francs qu'il ne coupe pas la corde.\" while the stout man listens with his mouth closed. Then both look back up at the balloon, silent. Ambient: distant crowd murmur, light wind, no music."),
    "P03": ("3", 9.0, "inside a wicker balloon basket above a park. Static camera, single continuous shot, no cut. Garnerin on the left grips the release rope and looks up. The assistant on the right pleads in French, clear worried voice: \"Citoyen Garnerin, renoncez, il est encore temps.\" while Garnerin keeps his mouth closed. Then Garnerin answers in French, grave firm voice: \"Lâchez tout.\" while the assistant falls silent. Ambient: wind and distant crowd far below, no music."),
}
ORDRE_MONTAGE = ["P1a-1", "P1a-2", "P1a-3", "P1a-4", "P1b-1", "P1b-2", "P1b-3", "P02", "P03", "P4a-1", "P4a-2", "P4a-3",
                 "P4b-1", "P4b-2", "P4b-3", "P5-1", "P5-2", "P5-3"]
