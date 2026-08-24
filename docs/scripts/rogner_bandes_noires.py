#!/usr/bin/env python3
"""Détecte et retire les bandes noires incrustées sur une plaque, puis réétire en 16:9.

Né de l'audit des références du 23 août 2026. Sur les styles réalistes J et K, trois plaques
sur six sont sorties avec des bandes noires, **malgré** la négative `letterbox bars, black bars`
ET la clause positive `the image fills the entire 16:9 frame edge to edge`. Un cadre de cinéma
a des bandes : c'est une structure, pas un élément, et aucune formulation de prompt ne l'enlève.

Une plaque avec bandes réinjectée impose ses bandes à tous les plans qui la réinjectent
(RÈGLE 1). Le rognage doit donc se faire AVANT la première réinjection.

Usage :
  python rogner_bandes_noires.py <fichier.png> [<fichier.png> ...] [--seuil 18] [--essai]

--essai n'écrit rien, il se contente de mesurer. Sans lui, le fichier est réécrit en place
après une sauvegarde `<nom>.avant-rognage.png` à côté.
"""
import sys
from pathlib import Path

from PIL import Image


def bande(pixels, longueur, lire, seuil):
    """Nombre de lignes ou de colonnes consécutives sous le seuil, depuis le bord.

    Deux conditions, pas une. Une vraie bande incrustée est sombre ET UNIFORME. Un sujet très
    sombre au bord du cadre, une manche noire en contre jour par exemple, est sombre mais varié.
    Sans le test d'uniformité, `P5-1_StyleJ` était détectée avec 149 px de bande à gauche alors
    que c'était le manteau de Garnerin ; la rogner aurait supprimé du contenu (24 août 2026).
    """
    n = 0
    for i in range(longueur):
        vals = lire(i)
        if max(vals) > seuil:
            break
        moyenne = sum(vals) / len(vals)
        variance = sum((v - moyenne) ** 2 for v in vals) / len(vals)
        if variance > 1.0:            # sombre mais texturé : c'est du sujet, pas une bande
            break
        n += 1
    return n


def mesurer(im, seuil):
    g = im.convert("L")
    w, h = g.size
    px = g.load()
    ech_x = range(0, w, max(1, w // 64))
    ech_y = range(0, h, max(1, h // 64))
    haut = bande(px, h // 3, lambda y: [px[x, y] for x in ech_x], seuil)
    bas = bande(px, h // 3, lambda y: [px[x, h - 1 - y] for x in ech_x], seuil)
    gauche = bande(px, w // 3, lambda x: [px[x, y] for y in ech_y], seuil)
    droite = bande(px, w // 3, lambda x: [px[w - 1 - x, y] for y in ech_y], seuil)
    return haut, bas, gauche, droite


def traiter(chemin, seuil, essai):
    im = Image.open(chemin)
    w, h = im.size
    haut, bas, gauche, droite = mesurer(im, seuil)
    if not any((haut, bas, gauche, droite)):
        print(f"{chemin.name:24s} {w}x{h}  aucune bande")
        return False
    boite = (gauche, haut, w - droite, h - bas)
    nw, nh = boite[2] - boite[0], boite[3] - boite[1]
    print(f"{chemin.name:24s} {w}x{h}  bandes h={haut} b={bas} g={gauche} d={droite}  ->  {nw}x{nh}")
    if essai:
        return True
    sauvegarde = chemin.with_suffix(".avant-rognage.png")
    if not sauvegarde.exists():
        im.save(sauvegarde)
    util = im.crop(boite)
    # Ne JAMAIS réétirer la zone utile telle quelle : sur une image en bandes latérales, cela
    # écraserait l'image de 30 %. On prend le plus grand rectangle 16:9 centré dans la zone utile,
    # puis on remet à l'échelle. La géométrie est préservée, on perd seulement du champ.
    if nw / nh > 16 / 9:
        cw, ch = int(round(nh * 16 / 9)), nh
    else:
        cw, ch = nw, int(round(nw * 9 / 16))
    dx, dy = (nw - cw) // 2, (nh - ch) // 2
    util = util.crop((dx, dy, dx + cw, dy + ch))
    util.resize((w, h), Image.LANCZOS).save(chemin)
    perte = 100 - round(100 * cw * ch / (w * h))
    print(f"{'':24s} zone utile {nw}x{nh}, recadre 16:9 en {cw}x{ch}, remis a {w}x{h}, "
          f"{perte} % de champ perdu, original dans {sauvegarde.name}")
    return True


def main():
    seuil = 18
    essai = "--essai" in sys.argv
    args = []
    it = iter(sys.argv[1:])
    for a in it:
        if a == "--seuil":
            seuil = int(next(it))
        elif a != "--essai":
            args.append(a)
    if not args:
        print(__doc__)
        return
    touches = sum(traiter(Path(a), seuil, essai) for a in args)
    print(f"\n{touches} fichier(s) avec bandes sur {len(args)}.")


if __name__ == "__main__":
    main()
