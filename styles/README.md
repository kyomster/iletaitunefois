# Bibliothèque de styles

Un dossier par style essayé sur *Il était une fois*, autonome, réutilisable pour une autre série. Dix-sept styles, dont **un retenu** : `P-anime-tv-moderne`.

Chaque dossier contient :

| Fichier | Ce que c'est |
|---|---|
| `STYLE.md` | la fiche lisible : blocs mot pour mot, verdict, ce que le style a appris, comment le réutiliser |
| `style.json` | les mêmes blocs, lisibles par `atelier/scripts/assembler_prompts.py` — c'est ce fichier que les scripts chargent |
| `exemples/` | les planches de référence et les images d'épreuve produites dans ce style ; `exemples/troupe/` pour A, B et C, les turnarounds et références de la troupe |

Les styles E, F, G, H et I n'ont que leur fiche : leurs images d'épreuve n'ont jamais été rapatriées dans le dépôt. Leurs blocs suffisent à les refaire.

## Ce qu'est un style ici

Un style est **une technique de production décrite par ses procédés** — nature du trait, construction des formes, mode d'ombrage, palette, lumière, matière — et jamais par une marque, un titre ou un nom d'auteur. Une technique n'appartient à personne ; un design appartient à quelqu'un. C'est aussi une contrainte de génération : le modèle refuse ou renvoie des designs protégés, et une image dérivée d'un design protégé n'est pas exploitable.

Un style se compose de cinq blocs qui **se copient octet pour octet** :

1. le **bloc de scène**, en tête de tout prompt de plan ;
2. le **traitement d'époque**, juste après, quand le plan est en registre d'époque ;
3. la **base négative du style**, après `Avoid:`, suivie de la base personnages d'époque et de la négative universelle ;
4. pour certains styles, des **traitements de lumière** par registre (JOUR, TENSION), choisis par le bloc du plan, jamais au tirage ;
5. le **bloc vidéo**, réduit à la facture, pour les prompts de mouvement.

Et d'une **variante de bloc identité**, qui dit comment les personnages se décrivent dans ce style : `AC` (dessiné), `B` (inkman), `JK` (réaliste : matériau plutôt que teinte), `P` (aplats : têtes de dos, carnation nommée). Voir `atelier/METHODE-generation-images.md`, RÈGLES 34 et 37.

## Comment essayer un nouveau style

Le protocole qui a servi dix-sept fois, avec un point d'arrêt dur à chaque palier :

1. **Écrire le bloc** par ses procédés, à partir d'une intention (public, registre, technique). 0 crédit.
2. **Épreuve de style** : les trois mêmes plans que tous les autres styles — un dialogue à deux au sol (`P02`), une contre-plongée (`P1a-3`), une plongée sur la ville (`P4b-1`) — générés **à sec, sans aucune référence** : réinjecter une plaque d'un autre style ramènerait cet autre style (RÈGLE 1). 6 crédits. Grille de contrôle : `atelier/METHODE-generation-images.md` §20, plus la question **ce style porte-t-il une texture de support qui grouillera en mouvement ?**
3. **Épreuve de troupe** si le style survit : les récurrents de la série dans ce style, 4 images. C'est là qu'on sait si la troupe se transpose ou impose un redessin.
4. **Planches de référence** de la série (décors, personnages, objets de continuité), puis **pilote de format** — la première séquence, en clés et en clips — et son montage. Le cadrage, la continuité et le mouvement ne se jugent que là.
5. **Comparaison** en montage, jamais sur image fixe : voir `COMPARATIF.md`.

Une leçon payée trois fois : **les qualités d'une image fixe ne survivent pas toutes au mouvement**. Grain de papier, trame, touche de pinceau sont des marqueurs de support qui dansent à 24 images par seconde. Les styles M, N, O et P ont été conçus après ce constat, sans aucune texture de support.

## Les dix-sept styles en une ligne

| Style | Dossier | Famille | Sort |
|---|---|---|---|
| A | `A-cartoon-youtube` | aplats, contour épais | pilote complet ; troisième de la shortlist finale |
| B | `B-inkman` | bonshommes bâton, décor peint | pilote complet ; écarté par le choix de P |
| C | `C-cel-annees-90` | cel deux tons | retiré le 22 août : indiscernable de A sur les plans larges |
| D | `D-anime-aventure` | anime, ombrage adouci | pilote complet ; cinquième sur cinq |
| Db | `Db-anime-affute` | D à ombre dure | épreuve seule |
| E | `E-2d-graphique-angulaire` | aplats anguleux sans contour | réserve, sous condition d'expression |
| F | `F-3d-facette-mat` | 3D marionnette | écarté |
| G | `G-3d-cartoon-rond` | 3D rond | premier de la première épreuve |
| H | `H-2d-imprime-moderne` | trames, impression | réserve, palette à calibrer |
| I | `I-roman-graphique` | ligne claire, gouache | second de la première épreuve |
| J | `J-cinema-realiste` | photoréaliste | pilote complet ; abandonne l'animation |
| K | `K-3d-long-metrage` | 3D adulte | pilote complet ; premier du classement révisé |
| L | `L-peinture-animee` | 3D finie à la peinture | épreuve seule |
| M | `M-2d-lumiere-numerique` | aplats, contre-jour coloré | épreuve seule |
| N | `N-2d-eclaire-en-volume` | 2D à lumière volumétrique | épreuve seule |
| O | `O-3d-toon-dur` | 3D cel shading dur | second de la shortlist finale |
| **P** | **`P-anime-tv-moderne`** | **aplats à trois tons, compositing de lumière** | **retenu le 27 août 2026** |
