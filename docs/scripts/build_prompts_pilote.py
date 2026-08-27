#!/usr/bin/env python3
"""Assemble les prompts d'image du pilote S01E01 (plans 1 à 6).

Six styles : A, B, C (verrouillés, source docs/S01E01-pilote-prompts-3-styles.md)
et D, J, K (retenus le 23 août, source docs/PLAN-styles-D-E-F.md §4).
Les blocs ci dessous sont la copie octet pour octet de ces deux fiches ; ils ne se
reformulent jamais. Seules les briques de plan (point 6) changent d'une image à l'autre.

Règle d'assemblage (point 1 de la fiche) :
  [STYLE scène] + [traitement de lumière du bloc] + [ÉPOQUE] + [brique, blocs identité substitués]
  + (si un personnage est réinjecté) "same characters as reference, same art style as reference"
  + " Avoid: " + [négatives de la brique (foule sur 1a, 1b, 2, 4a)] + [base style]
  + [base personnages d'époque] + [négative universelle]

Usage :
  python build_prompts_pilote.py <media_ids.json> <sortie.json> [<sortie.md>] [--styles StyleD,StyleJ]

<media_ids.json> : {"D01_StyleA.png": "<media_id>", ...} (5 entrées par style, phase A du runbook).
Sans --styles, les six styles sont assemblés, ce qui exige les 30 entrées de media_ids.
"""
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------- point 2 : blocs de style, version plan de scène
STYLE = {
    "StyleA": "2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:",
    "StyleB": "inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:",
    "StyleC": "hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:",
    # --- styles retenus le 23 août 2026, source PLAN-styles-D-E-F.md §4.1, §4.7, §4.8 ---
    "StyleD": "2D anime illustration, modern cinematic adventure anime style, clean thin dark brown ink linework with subtle weight variation, cel shaded characters with a soft airbrush gradient blending each shadow into its base tone, warm natural skin with a faint blush on the cheeks, adult realistic body proportions and grounded facial features, expressive eyes with a single specular highlight, hand painted background with atmospheric depth and aerial perspective, volumetric light, shallow depth of field with the background softly out of focus, fine film grain, 16:9 frame:",
    "StyleJ": "live action cinema look, photographed on 35mm film, naturalistic period drama cinematography, real actors in accurate historical costume, motivated practical lighting with deep natural falloff, shallow depth of field with creamy bokeh, fine organic film grain, subtle halation on the highlights, desaturated filmic colour grade with rich blacks and warm skin tones, photorealistic, the image fills the entire 16:9 frame edge to edge, no black bars, 16:9 frame:",
    # --- style P, ajouté le 25 août 2026 : bloc repris mot pour mot des trois épreuves validées (shortlist A/O/P) ---
    "StyleP": "modern anime television series look, clean black outlines of even weight, flat cel shading with exactly two or three tones per area and crisp hard shadow edges, appealing simple character shapes with clear expressive eyes and instantly readable silhouettes, bright clean saturated palette, digitally composited light: soft bloom around the highlights, smoothly graded sky, gentle light haze, background art painted more richly and in more detail than the characters, staged for limited animation with strong clear key poses, no surface texture of any kind, 16:9 frame:",
    "StyleK": "stylized 3D feature animation, high end computer animated film look, believable human proportions with only a light touch of caricature in the features, soft subsurface skin with fine texture and no plastic sheen, individually groomed hair, real cloth simulation with visible weave and wear, naturalistic cinematography with motivated light and long lens compression, restrained desaturated colour grade, shallow depth of field, subtle volumetric atmosphere, an adult dramatic register rather than a comic one, stylized and not photographic, 16:9 frame:",
}

# ---------------------------------------------------------------- traitements de lumière (23 août 2026)
# Un style peut porter deux registres de lumière. Le registre dépend du BLOC du plan, jamais du tirage.
# D : corrigé le 23 août, la clause de ciel `saturated blue sky with tall billowing cumulus clouds` est
# RETIRÉE du registre JOUR. Elle écrasait l'aube brumeuse décrite par la plaque D01 sur les trois images
# d'épreuve. L'heure appartient au décor, le traitement ne règle que la qualité de la lumière.
# J et K : registre TENSION ajouté le 23 août, ils n'en avaient aucun.
LUMIERE = {
    "StyleD": {
        "JOUR": "soft diffused key light, gentle contrast, clear readable midtones, luminous but restrained greens,",
        "TENSION": "hard directional key light, a single hard edged cast shadow shape across each face, palette pulled to warm amber or to near black, strong contrast, glowing rim light along the silhouette,",
    },
    "StyleJ": {
        "JOUR": "soft overcast daylight,",
        "TENSION": "hard directional key light with deep shadow across two thirds of the frame, desaturated grade pulled to cold grey and near black, high contrast, tight framing, long lens compression,",
    },
    "StyleK": {
        "JOUR": "soft overcast daylight,",
        "TENSION": "hard directional key light with deep shadow across two thirds of every volume, desaturated grade pulled to cold grey and near black, high contrast, tight framing, no warm bounce light,",
    },
}
# Blocs au sol en JOUR, blocs en l'air en TENSION (PLAN-styles-D-E-F.md §4.1).
REGISTRE_LUMIERE = {"1a": "JOUR", "1b": "JOUR", "2": "JOUR", "3": "JOUR", "4a": "JOUR", "4b": "TENSION", "5": "TENSION"}

# ---------------------------------------------------------------- point 3 : traitement d'époque
EPOQUE = {
    "StyleA": "historical period setting in desaturated muted earth tones, dusty beige, stone grey, earth brown, softened contrast, era accurate architecture and props,",
    "StyleB": "era accurate historical setting, moody atmospheric period palette,",
    "StyleC": "era accurate historical setting, palette shifted toward muted earth tones while keeping deep teal shadows,",
    "StyleD": "era accurate historical setting, costumes in muted earth tones, period architecture and props,",
    "StyleJ": "era accurate 1797 Directoire France, authentic period costume, real fabrics with wear and dirt, period architecture and props photographed on location,",
    "StyleP": "era accurate historical setting, costumes in muted earth tones, period architecture and props,",
    "StyleK": "era accurate 1797 Directoire France, authentic period costume in muted earth tones with real fabric weave and wear, period architecture and props,",
}

# ---------------------------------------------------------------- styles réalistes : deux règles propres (RÈGLE 33)
STYLES_REALISTES = {"StyleJ", "StyleK"}
# Sur un style réaliste, un objet dont la fonction historique est de porter un signe en porte un malgré
# la négative universelle. Les bannières de P1a-3 sont sorties brodées de lettres en J comme en K.
CLAUSE_BANNIERES = "plain undecorated banners with no emblem and no lettering, blank fabric only"
PLANS_A_BANNIERES = {"P1a-3"}
# 26 août 2026, RÈGLE 36 : le ballon est un élément de continuité, il se réinjecte au lieu d'être décrit.
# La plaque D01 en porte déjà un (RÈGLE 29) : sans cette clause, deux références qui montrent un ballon
# donnent deux ballons dans l'image, comme la nacelle l'avait fait le 24 août sur 1b-2.
CLAUSE_BALLON = ("ONE single gas balloon only, exactly the one shown in the balloon reference, identical envelope shape "
                 "and identical stripe colours, no second balloon anywhere in the frame")
PLANS_A_BALLON = {"P1a-1", "P1a-2", "P1a-3", "P1a-4", "P1b-1", "P1b-2", "P02", "P4a-1", "P4a-2", "P4a-3", "P5-1", "P5-2", "P5-3"}
# 26 août 2026, RÈGLE 36 sur le deuxième objet de continuité : la nacelle changeait de forme d'un plan à l'autre
# (ronde à rebord épais, rectangulaire à couvercle, rectangulaire à panneaux). Planche à deux vues, extérieure et
# intérieure, parce que la moitié des plans la montrent de l'intérieur.
CLAUSE_NACELLE = ("ONE single wicker basket only, exactly the one shown in the basket reference: round, deep, honey coloured "
                  "wicker in even horizontal bands, thick rope wrapped rim, four suspension ropes at the quarters, sandbags "
                  "outside, deep enough to reach a standing man's waist and wide enough for two men to stand in it side by side, barely wider than it is deep; no second basket, no crate, no rectangular hamper and no lid anywhere in the frame")
PLANS_A_NACELLE = {"P1a-1", "P1a-2", "P1a-4", "P1b-2", "P1b-3", "P02", "P03", "P4a-1", "P4b-1", "P4b-2", "P5-1", "P5-2", "P5-3"}

# 27 août 2026 : le parachute était écrit comme un paquet posé au plancher de la nacelle. Trancher la corde
# ferait alors tomber Garnerin avec un bagage, et le plan 6 perd son sens. Il est gréé ENTRE le ballon et la
# nacelle, replié comme un parapluie fermé — fait historique. Voir docs/S01E01-logique-ouverture-froide.md §1.
CLAUSE_PARACHUTE = ("the folded parachute hangs BETWEEN the balloon and the basket, closed and bound like a furled umbrella, "
                    "its lines running down to the rim of the basket and its crown roped up to the balloon; the silk is never "
                    "a bundle lying on the floor of the basket")
PLANS_A_PARACHUTE = {"P1b-2", "P1b-3", "P02", "P03", "P4a-1", "P4a-3", "P4b-1", "P5-1", "P5-2", "P5-3"}

# ---------------------------------------------------------------- durcissements de cadrage (24 août 2026)
# Deux plans ont raté leur cadrage à l'audit du pilote, et dans les deux cas le modèle a rendu un plan
# PLUS LARGE que demandé : P5-1 en J a donné un plan moyen de Garnerin portant un panier au lieu du très
# gros plan sur la main, P1a-3 en K a donné le ballon au sol au lieu de la contre plongée sur la couronne.
# `Framing: very close shot` et `low angle` ne suffisent pas seuls : on décrit ce que le cadre CONTIENT.
CADRAGE_DURCI = {
    # 26 août 2026 : le « edge to edge » contredisait le nouveau cadrage de 5-1, qui doit suivre la corde jusqu'au
    # ballon (RÈGLE 39). On garde ce que la clause servait vraiment à interdire : un visage, une tête, un corps.
    "P5-1": "No face, no head, no shoulders and no full body anywhere in the frame: only the hand, the forearm, the woven side of the basket, the rope and the sky.",
    "P1a-3": "The camera is tilted steeply upward from directly below; the crown of the balloon fills the upper half of the frame and the ground is not visible at all.",
    # 26 août 2026 : avec la planche Ballon réinjectée, le plan est passé du gros plan sur trois badauds à un
    # plan large de foule, qui répétait le cadrage de 1a-4 et de 1b-1. Le nombre et l'échelle se prescrivent.
    "P4a-2": "EXACTLY THREE onlookers are visible and no one else, seen from close behind at shoulder height, their heads and shoulders filling the lower half of the frame; no fourth figure anywhere, no wide crowd.",
}

# ---------------------------------------------------------------- point 4 : négatives
NEG_UNIVERSELLE = "text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin"
NEG_EPOQUE = "dominant sand colored outfit, dominant teal outfit, dominant vivid orange outfit, saturated orange clothing, saturated teal clothing"
NEG_STYLE = {
    "StyleA": "gradient shading, soft shading, airbrush, painterly, thin delicate linework, photorealism, photograph, realistic skin texture, 3D render, CGI, live action, anime style, manga, corporate flat vector art, extra characters.",
    "StyleB": "plain round ball hands, hollow circle hands, teardrop hands, pointed armless stumps, separate fingers, realistic hands, missing hand, missing arm, realistic human anatomy, detailed face, nose, photorealism, 3D render, anime, manga, extra inkman characters.",
    "StyleC": "gradient shading, soft shading, airbrush, painterly, rendered highlights, digital painting, muddy colors, cold blue palette, violet palette, purple palette, photorealism, photograph, 3D render, CGI, live action, anime, manga, flat vector art, extra characters.",
    "StyleD": "flat vector art, thick uniform black outline, corporate flat design, chibi proportions, super deformed, oversized anime eyes on adult characters, moe face, photorealism, photograph, 3D render, CGI, live action, extra characters.",
    "StyleJ": "illustration, drawing, painting, cartoon, anime, manga, 3D render, CGI, video game, painterly, cel shading, ink outlines, plastic skin, waxy face, over sharpened, HDR, deformed hands, extra fingers, modern buildings, glass towers, letterbox bars, black bars, extra characters.",
    "StyleP": "paper grain, canvas texture, halftone dots, visible brush strokes, print texture, film grain, painterly rendering, gradient shading on the characters, soft airbrush, photorealism, photograph, 3D render, CGI, live action, chibi proportions, oversized anime eyes on adult characters, moe face, extra characters.",
    "StyleK": "photograph, live action, real actors, broad cartoon caricature, chibi proportions, oversized head, rubbery squash and stretch, plastic sheen, waxy face, uncanny, saturated candy colours, 2D drawing, cel shading, anime, manga, modern buildings, glass towers, letterbox bars, black bars, extra characters.",
}
# 26 août 2026, retour de Guillaume sur le pilote P : « le visage des personnages est tout noir quand ils sont
# en fond ». Vérifié sur la planche Foule_StyleP et sur onze clés : partout où un figurant laisse voir un bout
# de joue, le style P remplit la zone d'un APLAT NOIR. Les styles A et D, mêmes mots, rendent une joue normale.
# Mécanisme : demander « aucun trait de visage » à un style dont le référent est l'aplat à deux ou trois tons
# revient à demander le ton le plus sombre. RÈGLE 37. On retire la ZONE (têtes strictement de dos) au lieu de
# retirer les traits, et on nomme la carnation en positif.
NEG_FOULE = {
    "defaut": "readable faces, portraits, facial features, eyes, dot eyes on crowd figures, front facing figures",
    "P": ("readable faces, portraits, recognisable face on a crowd figure, front facing figure, three quarter face, "
          "profile face on a crowd figure, face filled with flat black, blacked out face, head painted as a solid dark shape, "
          "face hidden in solid shadow, silhouette head"),
    # P02 est le plan où la négative de foule efface les visages des deux badauds nommés (correction du 22 août).
    # En style P, on garde quand même la partie anti-aplat noir : elle ne vise pas les visages lisibles, seulement
    # le remplissage. Sans elle, P02 est justement le plan où le défaut se voyait le plus.
    "P_plans_nommes": ("face filled with flat black, blacked out face, head painted as a solid dark shape, "
                       "face hidden in solid shadow, silhouette head"),
}
BLOCS_FOULE = {"1a", "1b", "2", "4a"}  # point 4.4
# Correction du 22 août 2026 (audit lot 1, docs/S01E01-pilote-audit.md) : sur P02, la négative de foule
# effaçait les visages des deux badauds nommés en style C. Elle est retirée sur ce plan, le bloc positif
# [FOULE] suffit. P02_StyleA et P02_StyleB validés avaient été produits AVEC la négative (version 1).
PLANS_SANS_NEG_FOULE = {"P02", "P02a", "P02b"}

# ---------------------------------------------------------------- point 5 : blocs identité
IDENT = {
    "GARNERIN": {
        "AC": "Garnerin, a French aeronaut of the Directoire era, resolute determined face with a calm set jaw, dark tailcoat, hair tied back, pale scarf at the neck, period breeches and buckled shoes, upright decided posture",
        "B": "Garnerin, an inkman stick figure character, a few ink strokes of hair tied back on his round head, simple black dot eyes with no eyebrows, resolute mouth drawn as one short flat ink line, closed, wearing a dark Directoire tailcoat drawn as a simple flat shape, a pale scarf knotted at the neck, simple period shoes on his stick legs, upright decided posture",
    },
    # 23 août 2026, audit des références : le manteau du maigre est sorti en SARCELLE DÉSATURÉ en styles
    # J et K, vert olive en D. Deux styles sur trois (RÈGLE 7) : la cause est dans le prompt, qui ne
    # nommait aucune couleur. Les négatives `dominant teal outfit, saturated teal clothing` ne l'ont pas
    # arrêté parce que le sarcelle sorti est désaturé : il passe sous la négative tout en étant la couleur
    # dominante du personnage. Couleur nommée en positif, application de la RÈGLE 30 à un personnage nommé.
    "PARIEURS": {
        "AC": "the round onlooker wearing a tall cylindrical top hat with a tricolour cockade pinned on it, waistcoat tight over his belly, peremptory self assured air; the thin onlooker leaning on a cane, threadbare coat in muted brown and grey only, no blue and no green on any garment, suspicious squint",
        "B": "the round bellied onlooker inkman with a tall cylindrical top hat with a cockade on his round head, waistcoat drawn as a flat shape stretched over his belly, peremptory raised chin; the thin onlooker inkman leaning on a cane, threadbare coat, suspicious half closed dot eyes",
        # 24 août 2026, audit du pilote J : la couleur nommée en positif n'a pas tenu sur le style
        # photoréaliste, le manteau du maigre est ressorti bleu sarcelle sur P02 et brun sur P02b,
        # soit une rupture de raccord entre deux plans qui se suivent. Sur un rendu réaliste, une
        # veste d'ouvrier bleu passé est historiquement plausible : le référent la ramène malgré la
        # consigne. Corollaire de la RÈGLE 34 : on décrit le MATÉRIAU et l'usure, pas la teinte.
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
        # 23 août 2026 : sur J et K, la clause AC n'a pas tenu. Une dizaine de figurants nets, alignés,
        # visages lisibles, qui posent au lieu de regarder le ballon. Le flou d'arrière plan seul n'y a rien fait.
        # Durcie en positif, PLAN-styles-D-E-F.md §5.1. Le style D, lui, garde la clause AC : l'épreuve a
        # montré qu'elle est sûre même sur un style à visages détaillés.
        "JK": "a dozen Directoire crowd figures, ALL SEEN FROM BEHIND, turned toward the balloon, NO FIGURE FACING THE CAMERA, thrown out of focus by the shallow depth of field, no readable face on any background figure: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, much less detailed than the main characters",
        # 26 août 2026, RÈGLE 37 : sur un style à aplats, « aucun trait de visage » se résout par le ton le plus
        # sombre, donc par un visage noirci. On supprime la zone au lieu des traits, et on nomme la carnation.
        "P": "a dozen Directoire crowd figures, EVERY SINGLE ONE SEEN STRICTLY FROM DIRECTLY BEHIND with the back of the head squarely toward the camera, no cheek, no jaw, no ear and no profile visible on any of them, so that no face exists anywhere in the image, turned toward the balloon; the small areas of skin that do show, a nape or a hand, are drawn in the SAME EVENLY LIT FLESH TONE as the main characters, never filled with black, never covered by shadow: men in tailcoats and tall hats, women in high waisted dresses and shawls, a few children, simplified figures less detailed than the main characters",
    },
    "AIDE": {
        "AC": "an assistant in a rough jacket with rolled up sleeves, seen from behind at the edge of frame",
        "B": "an inkman assistant in a rough flat jacket, seen from behind at the edge of frame",
    },
    # variante du 23 août 2026 (P03 v3) : l'aide de face, pour que les deux visages d'un plan de dialogue soient visibles
    "AIDE_FACE": {
        "AC": "an assistant in a rough jacket with rolled up sleeves, his plain honest face fully visible, short hair, calm attentive expression",
        "B": "an inkman assistant in a rough flat jacket, his round white head fully visible with simple dot eyes and a closed mouth drawn as one short flat ink line",
    },
}
SAME_AS_REF = "same characters as reference, same art style as reference"

# ---------------------------------------------------------------- point 6 : briques d'image (identiques dans les trois styles)
# (nom de fichier sans style, bloc, brique)
BRIQUES = [
    # 24 août 2026, essai de réinjection en style D : DEUX nacelles d'osier, une accrochée sous le ballon
    # et une seconde posée sur l'herbe. RÈGLE 29, la plaque D01 porte déjà sa nacelle et la brique en
    # nommait une dans les props : le modèle a produit les deux lectures. Corrigé comme 1b-2 l'avait été,
    # en nommant l'état voulu au lieu de le taire.
    ("P1a-1", "1a", "Scene: dawn mist drifting low over the lawns of Parc Monceau, a large inflated gas balloon swaying in the middle ground, a Directoire crowd gathered at its foot. Framing: very wide establishing shot, slight high angle. Decor: D1. Characters: [FOULE]. Props: ONE single wicker basket only, resting on the grass directly under the balloon and tied to it, no second basket and no crate anywhere in the frame, ropes trailing on the grass."),
    ("P1a-2", "1a", "Scene: the inflated balloon swaying in the wind, mooring ropes pulling taut. Framing: medium shot on the balloon. Decor: D1. Characters: a few crowd figures at the lower edge, seen from behind. Props: balloon, taut ropes, stakes."),
    ("P1a-3", "1a", "Scene: banners snapping at the top of the balloon. Framing: low angle from the ground toward the crown of the balloon. Decor: D1, sky and treetops only. Characters: none. Props: balloon crown, netting, banners."),
    # Briques 1a-4, 4a-1, 4a-2, 4b-3 et P02/P03 amendées le 22 août 2026, 19 h (audit Sonnet + Guillaume) : cadrages répétés
    # (trois très larges identiques), saut d'altitude du ballon, bouches déjà ouvertes sur les images clés de dialogue.
    ("P1a-4", "1a", "Scene: the whole crowd turning their heads in one movement toward the wicker basket. Framing: medium shot at head height on the backs of a few onlookers, hats and bonnets filling the lower half, the basket and the balloon ropes beyond them. Decor: D1. Characters: [FOULE]. Props: basket, ropes, hats."),
    ("P1b-1", "1b", "Scene: the crowd parting into two lines, hats lifted. Framing: wide shot at eye level, down the axis of the lane. Decor: D1. Characters: [FOULE]. Props: hats, canes."),
    # Briques 1b-2, 1b-3 et P03 amendées le 22 août 2026 (décision Guillaume, audit : la plaque D01 impose un ballon
# avec sa nacelle, d'où deux nacelles à l'image). Version 1 : sans la clause « balloon hanging above / no other basket ».
    ("P1b-2", "1b", "Scene: the wicker basket carried forward by assistants, ropes trailing, toward the balloon hanging above with no basket under it yet. Framing: lateral medium shot. Decor: D1. Characters: two assistants in rough jackets, crowd behind them seen from behind. Props: ONE wicker basket, ropes."),
    ("P1b-3", "1b", "Scene: the basket being lashed under the balloon, hands knotting the ropes, the balloon is directly above this basket and out of frame. Framing: close shot on the knots. Decor: D1, blurred behind, no other balloon or basket in the background. Characters: hands and forearms only. Props: ropes, wicker rim, iron ring."),
    ("P02", "2", "Scene: two Directoire onlookers in the foreground leaning toward each other to make a bet, both with their mouths firmly closed in a neutral pause, hands down, the basket and the crowd behind them. Framing: medium close shot at chest height, slightly low angle. Decor: D1. Characters: [PARIEURS], [FOULE] far behind. Props: cane, cockaded hats."),
    # Champ-contrechamp de P02, 22 août 2026 (décision Guillaume) : la synchro labiale S2V n'anime correctement que si le seul
    # visage visible est celui qui parle. Deux images clés supplémentaires, une par badaud, même décor, mêmes références.
    ("P02a", "2", "Scene: close shot on the round onlooker alone as he speaks, his hand down, his mouth clearly visible, the top hat with the tricolour cockade, the thin onlooker out of frame, the crowd and the basket far behind. Framing: close shot at shoulder height, slightly low angle. Decor: D1. Characters: [PARIEURS_ROND]. Props: cockaded hat."),
    ("P02b", "2", "Scene: close shot on the thin onlooker alone as he answers, leaning on his cane, his mouth clearly visible, the round onlooker out of frame, the crowd and the basket far behind. Framing: close shot at shoulder height, slightly low angle. Decor: D1. Characters: [PARIEURS_MAIGRE]. Props: cane."),
    # P03 v4 (23 août 2026, Guillaume) : l'action porte la réplique — Garnerin la main sur la corde de largage, l'aide qui supplie, la soie au sol ; la v3 (les deux de profil, la soie tendue) se lisait comme une couverture offerte
    ("P03", "3", "Scene: inside the basket, Garnerin standing at the release rope, one gloved hand gripping the taut rope above his head, looking up toward the balloon with his jaw set, his assistant STANDING ON THE GRASS OUTSIDE THE BASKET on the other side, both hands on the outer rim, leaning in and pleading with one open hand, the basket wall between them, BOTH FACES FULLY VISIBLE to the camera in three quarter view, both with their mouths firmly closed, the balloon is directly above this basket and out of frame. Framing: medium two shot from the side at chest height, Garnerin on the left inside the basket, the assistant on the right outside it standing on the ground, the lawn and the mist clearly visible behind them so the basket is plainly still on the ground, two taut mooring ropes entering the bottom of the frame and held by crew hands at the very edge of the image. Decor: D1 seen past the rim of the basket, no other balloon or basket in the background. Characters: [GARNERIN], [AIDE_FACE]. Props: taut release rope, mooring ropes held by crew hands, a knife tucked at the side of the basket."),
    ("P4a-1", "4a", "Scene: the balloon tearing away from the ground, the released mooring ropes falling back to the grass, GARNERIN VISIBLE IN THE BASKET, head and shoulders above the rim, one hand on the rim, looking up. Framing: low angle from the ground, the balloon, the folded parachute and the basket filling the frame as they lift off, no onlooker in the frame. Decor: D1, treetops and sky. Characters: [GARNERIN], head and shoulders only, inside the basket. Props: balloon, folded parachute, basket, falling mooring ropes."),
    # Brique 4a-2 amendée le 22 août 2026 (continuité : le ballon ne doit pas « redécoller » deux fois entre 4a-1 et 4a-2).
    # 4a-2 : couleurs des habits nommées en positif le 23 août 2026 (deux tirages sur deux sortaient orange vif, sarcelle et sable : RÈGLE 4)
    ("P4a-2", "4a", "Scene: three onlookers rocking backwards to follow the balloon with their eyes, each shading their eyes with ONE FLAT HAND held above the eyebrows like a visor, palm down, no hand touching any hat, their coats in muted brown, grey and dark green only, no bright color on any garment, the balloon just above the treetops, still large, rising away. Framing: close shot on the backs and shoulders of three onlookers, low angle. Decor: D1. Characters: [FOULE]. Props: hats, shawls."),
    ("P4a-3", "4a", "Scene: the balloon rising and shrinking above the trees, the whole rig visible in one piece: the balloon on top, the folded parachute hanging below it, the basket hanging below the parachute. Framing: wide low angle shot. Decor: D1, treetops and sky. Characters: none. Props: balloon, folded parachute, basket, trailing rope."),
    ("P4b-1", "4b", "Scene: seen from the basket, the rooftops of Paris sliding slowly below, chimney smoke streaming. Framing: very wide high angle shot, the rim of the basket in the foreground. Decor: D2. Characters: none. Props: wicker rim, the parachute lines rising from the rim and leaving the top of the frame."),
    ("P4b-2", "4b", "Scene: the wicker rim vibrating in the wind, a gloved hand tightening on it. Framing: close shot on the hand and the rim. Decor: D2, blurred sky behind. Characters: [GARNERIN], gloved hand only. Props: wicker rim, glove, rope."),
    ("P4b-3", "4b", "Scene: the whole city under the haze, much higher and farther than before, the park a small green rectangle with the crowd reduced to a dark patch in its middle. Framing: very wide high angle shot from far above, no basket and no rim in the frame. Decor: D2, the rooftops of Paris under the haze. Characters: none, no person anywhere. Props: none."),  # D2 explicité (RÈGLE 28) : la v1 du 22 août 19 h portait un « D2 » en bas à droite
    # 24 août 2026, audit du pilote D : P5-1 est sortie avec « D2 » ECRIT EN GROSSES LETTRES sur un
    # second ballon au fond. C'est la RÈGLE 28 mot pour mot, le code de décor devenu texte sur un très
    # gros plan. Le défaut a une histoire : la correction du 22 août 2026 avait développé D2 en clair
    # sur 5-2 et 5-3, et avait OUBLIÉ 5-1. En styles A, B et C ce plan est sorti correct par chance,
    # personne ne l'a vu. Développement ajouté, plus la clause anti second ballon de 1b-3 et 5-2.
        # P5-1 v2 (24 août 2026, Guillaume) : le bras vient de l'INTÉRIEUR de la nacelle — sur les clés précédentes il se lisait comme venant de l'extérieur, impossible
    ("P5-1", "5", "Scene: seen from INSIDE the basket: Garnerin's arm in his dark sleeve comes from inside the basket and his hand takes hold of the knife sheathed against the inner wicker wall, the woven rim of the basket in the foreground, the parachute lines rising from the rim to the closed folded parachute just above, and above it the single taut rope that ties the parachute crown to the balloon. Framing: close shot from inside the basket, tilted up so the eye follows the lines to the folded parachute and to the rope above it, the underside of the balloon showing at the very top of the frame. Decor: D2, the sky and the rooftops of Paris far below, out of focus beyond the rim, no other balloon and no other basket anywhere in the frame. Characters: [GARNERIN], one hand and forearm only, clearly reaching from inside the basket. Props: knife, inner wicker wall, taut rope."),
    # Briques 5-2 et 5-3 : « Decor: D2 » explicité le 22 août 2026 (en style A, sur ces très gros plans, le code D2 seul
# donnait un mur ou un panneau « D2 » ; B et C avaient le ciel). Brique 5-2 amendée le 22 août 2026 (audit : corde déjà tranchée en A et C, RÈGLE 7/13). Version 1 :
# "Scene: the blade sawing the taut rope, fibres springing free one by one. [...] Props: knife, rope, loose fibres."
        # P5-2 v3 (24 août 2026, Guillaume) : idem — la coupe se fait depuis l'intérieur, le rebord dans le cadre
    ("P5-2", "5", "Scene: Garnerin's arm reaching up from INSIDE the basket, over the woven rim visible at the bottom of the frame, the blade sawing the single taut rope that ties the crown of the folded parachute to the balloon, the rope still in ONE piece and taut, only a few outer fibres cut and springing free one by one, the blade halfway through. Framing: medium close shot from inside the basket at a low angle, the woven rim running across the bottom of the frame, the closed folded parachute hanging just above the basket and, above it, the single taut rope reaching the balloon, all three clearly visible in the same frame, so that what the blade is cutting is the ONE rope holding the parachute, and the basket under it, to that balloon. Decor: D2, the sky and the rooftops of Paris far below, out of focus behind. Characters: ONE hand only, Garnerin's hand in his dark sleeve reaching from inside the basket, no second hand, the taut rope is fixed to the rim of the basket. Props: knife, one unbroken rope, loose fibres, woven rim."),  # 5-2 : une seule main (22 août, deux manches différentes lues comme deux personnes)
    ("P5-3", "5", "Scene: the rope giving way at once, the strands whipping the air, the cut end still attached to the crown of the parachute dropping away with it at the bottom of the frame while the other cut end springs upward with the balloon, which leaps away and shrinks at the top of the frame, and the parachute BEGINS TO OPEN above the falling basket, its folded silk swelling into a dome. Framing: close frontal shot on the break, wide enough to hold both the basket rim at the bottom and the balloon rising away at the top. Decor: D2, the sky and the rooftops of Paris far below, out of focus behind. Characters: none. Props: severed rope, whipping strands, basket rim, balloon rising away."),
]

# ---------------------------------------------------------------- références par plan (runbook §4.1, ordre décor puis personnages)
REFS = {
    "P1a-1": ["D01", "Foule", "Ballon", "Nacelle"], "P1a-2": ["D01", "Foule", "Ballon", "Nacelle"], "P1a-3": ["D01", "Ballon"], "P1a-4": ["D01", "Foule", "Ballon", "Nacelle"],  # 1a-2 : Foule ajoutée le 22 août 2026 (audit : dérive des figurants sans référence en A et B)
    "P1b-1": ["D01", "Foule", "Ballon"], "P1b-2": ["D01", "Foule", "Ballon", "Nacelle"], "P1b-3": ["D01", "Nacelle"],  # 1b-3 : pas de planche Ballon, la brique le veut hors champ et la référence le faisait entrer (RÈGLE 1)
    "P02": ["D01", "Parieurs", "Foule", "Ballon", "Nacelle"], "P02a": ["D01", "Parieurs"], "P02b": ["D01", "Parieurs"],
    "P03": ["D01", "Garnerin", "Nacelle"],
    "P4a-1": ["D01", "Ballon", "Nacelle"], "P4a-2": ["D01", "Foule", "Garnerin", "Ballon"], "P4a-3": ["D01", "Ballon"],  # 4a-1 : D01 seul depuis le 22 août 19 h (plus de personnage dans la brique)
    "P4b-1": ["D02", "Nacelle"], "P4b-2": ["D02", "Garnerin", "Nacelle"], "P4b-3": ["D02"],  # 4b-3 : la brique exclut la nacelle du champ
    "P5-1": ["D02", "Garnerin", "Nacelle", "Ballon"], "P5-2": ["D02", "Nacelle", "Ballon"], "P5-3": ["D02", "Nacelle", "Ballon"],
}
PERSONNAGES = {"Foule", "Garnerin", "Parieurs"}

GEN_PARAMS = {"model": "nano_banana_pro", "aspect_ratio": "16:9", "resolution": "2k", "count": 1, "use_unlim": False}


STYLES_APLATS = {"StyleP"}  # styles à aplats : deux ou trois tons par zone, ombres à bord dur (RÈGLE 37)


def variante_identite(style):
    """Quel jeu de blocs identité s'applique. Un style sans entrée propre retombe sur AC."""
    if style == "StyleB":
        return "B"
    if style in STYLES_REALISTES:
        return "JK"
    if style in STYLES_APLATS:
        return "P"
    return "AC"


def assemble(name, bloc, brique, style, media_ids):
    variant = variante_identite(style)
    body = brique
    for key, blocs in IDENT.items():
        body = body.replace(f"[{key}]", blocs.get(variant, blocs["AC"]))
    assert "[" not in body, f"substitution incomplète sur {name}"
    if name in PLANS_A_BANNIERES:
        body += f" {CLAUSE_BANNIERES}."  # RÈGLE 33, élargie à tous les styles le 25 août 2026 (ornements dorés en P)
    if name in PLANS_A_BALLON and "Ballon" in REFS[name]:
        body += f" {CLAUSE_BALLON}."  # RÈGLE 36 + RÈGLE 29
    if name in PLANS_A_NACELLE and "Nacelle" in REFS[name]:
        body += f" {CLAUSE_NACELLE}."  # RÈGLE 36 + RÈGLE 29
    if name in PLANS_A_PARACHUTE:
        body += f" {CLAUSE_PARACHUTE}."  # logique de la scène, §1
    if name in CADRAGE_DURCI:
        body += f" {CADRAGE_DURCI[name]}"
    refs = REFS[name]
    lumiere = LUMIERE.get(style, {}).get(REGISTRE_LUMIERE[bloc], "")
    positive = " ".join(x for x in (STYLE[style], lumiere, EPOQUE[style], body) if x)
    if any(r in PERSONNAGES for r in refs):
        positive += f" {SAME_AS_REF}"
    negs = []
    if bloc in BLOCS_FOULE:
        if name not in PLANS_SANS_NEG_FOULE:
            negs.append(NEG_FOULE.get(variant, NEG_FOULE["defaut"]))
        elif variant == "P":
            negs.append(NEG_FOULE["P_plans_nommes"])
    negs += [NEG_STYLE[style], NEG_EPOQUE, NEG_UNIVERSELLE]
    prompt = f"{positive} Avoid: " + ", ".join(negs)
    medias = [{"role": "image_references", "value": media_ids[f"{r}_{style}.png"]} for r in refs]
    return {
        "name": f"{name}_{style}", "plan": name, "bloc": bloc, "style": style,
        "registre_lumiere": REGISTRE_LUMIERE[bloc] if style in LUMIERE else None,
        "references": [f"{r}_{style}.png" for r in refs],
        "params": {**GEN_PARAMS, "prompt": prompt, "medias": medias},
    }


TOUS_LES_STYLES = ("StyleA", "StyleB", "StyleC", "StyleD", "StyleJ", "StyleK")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    styles = TOUS_LES_STYLES
    for a in sys.argv[1:]:
        if a.startswith("--styles"):
            styles = tuple(a.split("=", 1)[1].split(",")) if "=" in a else styles
    for s in styles:
        assert s in STYLE, f"style inconnu : {s}"
    media_ids = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    out = []
    for style in styles:
        for name, bloc, brique in BRIQUES:
            out.append(assemble(name, bloc, brique, style, media_ids))
    assert len(out) == 20 * len(styles), f"{len(out)} prompts pour {len(styles)} styles"
    Path(args[1]).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    if len(args) > 2:
        md = [f"# S01E01 — les {len(out)} prompts du pilote, tels que soumis", "",
              "Générés par `docs/scripts/build_prompts_pilote.py`. Blocs A, B, C repris de `S01E01-pilote-prompts-3-styles.md` ; blocs D, J, K repris de `PLAN-styles-D-E-F.md` §4. Réglages : `nano_banana_pro`, 16:9, 2k, count 1. Références dans l'ordre indiqué, rôle `image_references`.", ""]
        for e in out:
            entete = f"Références : {', '.join(e['references'])}"
            if e["registre_lumiere"]:
                entete += f" · registre de lumière : **{e['registre_lumiere']}**"
            md += [f"## {e['name']}", "", entete, "", "```", e["params"]["prompt"], "```", ""]
        Path(args[2]).write_text("\n".join(md), encoding="utf-8", newline="\n")
    print(f"{len(out)} prompts écrits dans {args[1]} ({len(styles)} styles : {', '.join(styles)})")


if __name__ == "__main__":
    main()
