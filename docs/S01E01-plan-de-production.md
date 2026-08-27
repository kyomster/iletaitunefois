# LES DÉCOUVREURS — S01E01 · « Nos ancêtres les Chinois » — version de production

> **Arbitrage du 22 août 2026, reporté dans ce document.** Sam n'a aucune lunette, nulle part : ni portées, ni sur le front, ni tenues, ni dans la sacoche. La réplique verrouillée du plan 8 devient « ...regardez ma sacoche : de la glace ! ». Le gag du givre est transféré à la sacoche, qui est le totem du personnage. Les descriptions visuelles des plans 8 et 76 et la liste des gags sont mises à jour en conséquence. Aucune autre modification de la zone verrouillée.

> **Révision des durées, 22 août 2026, arbitrée.** 22 plans n'avaient pas la place de dire leur texte à 150 mots par minute. Décision : allonger, jamais raccourcir. Nouvelle durée utile **1 296 s soit 21 min 36**, dans la fourchette de 20 à 22 min de la bible. 4 s reprises sur le plan 9 pour que l'objection d'Elio reste avant 3:00, où elle tombe à 2:58. Ratio ANIMÉ 36,7 %. Plans allongés : 6, 7, 8, 12, 13, 15, 18, 20, 25, 28, 31, 34, 37, 40, 48, 52, 58, 63, 64, 65, 66, 69. Plan raccourci : 9. Texte dit, faits, gags, ordre et numérotation inchangés.
>
> **Mouvements de caméra complétés, 22 août 2026.** Les 36 plans FIXE dont la colonne portait un tiret ont reçu leur mouvement de montage, sens précisé, conformément au point 5 bis de la bible. Aucun plan FIXE n'est plus sans mouvement.
>
> **Chaîne de rendu, 22 août 2026.** Le rendu vidéo passe hors de Higgsfield, sur ComfyUI hébergé chez RunPod. Les prompts de mouvement de la section 5 ci dessous sont écrits pour un moteur produisant des coupes internes et **sont périmés** : le gabarit de remplacement, un clip continu par coupe, est au point 6 de `PIPELINE-video-et-voix.md`. Les images clés restent sur Nano Banana Pro.




> Ce document est le **scénario v3 converti en plan de fabrication**, selon le protocole « Adaptation d'un scénario en plan de production ». La zone verrouillée est intacte : texte dit mot pour mot, chaîne mais/donc, faits, gags, durée totale (1 224 s soit 20 min 24), ordre et numérotation des plans. Les sections Parti pris, Corrections appliquées, Chaîne narrative, Minutage et Gags du scénario v3 restent valables à l'identique. Les deux formules de style sont rédigées au point 2 et se collent octet pour octet dans chaque prompt.

---

## 1. Diagnostic

| Indicateur | Avant | Après |
|---|---|---|
| Durée totale | 1 224 s | **1 296 s soit 21 min 36** — révision des durées du 22 août, voir la note en tête |
| Part ANIMÉ | 714 s soit 58,3 % | **476 s soit 36,7 %** (cible : 40 % maximum) |
| Plans basculés ANIMÉ vers FIXE (avec mouvement de caméra) | — | **11** : plans 12, 16, 19, 26, 35, 36, 44, 46, 47, 65, 68 (le plan 1, d'abord basculé, est repassé en ANIMÉ : voir ALERTES) |
| Plans reclassés POST | — | **8** : plans 6, 15, 25, 27, 34, 52, 60, 74 (dont 2 venus d'ANIMÉ : 60 et 74) |
| Plans ANIMÉ découpés | — | **21 plans en 51 blocs**, tous de 10 s ou moins |
| Générations vidéo | ~37 rendus dont certains de 20 à 32 s (hors capacité des modèles) | **54 blocs de 6 à 10 s**, réexplosés en **189 clips de 2,5 s** par la chaîne ComfyUI, voir `PIPELINE-video-et-voix.md` |
| Générations image | — | **~118 images clés** : 47 plans FIXE, 11 vignettes supplémentaires des montages basculés, ~6 images sources des plans POST, et **54 images de départ, une par bloc ANIMÉ** (la chaîne est image vers vidéo : chaque rendu vidéo part d'une image clé générée avec le même mécanisme de cohérence) |
| Estimation de coût | vidéo dominante et irréaliste (blocs trop longs) | 54 rendus vidéo de 6 à 10 s et ~118 images clés ; la vidéo reste le poste dominant, réduite d'environ un tiers ; plus aucun appel au delà de 10 s |

---

## 2. Les deux formules de style

À coller **octet pour octet** en tête de chaque prompt d'image et de mouvement. La formule ÉPOQUE est la formule CADRE augmentée du traitement de désaturation. Les plans MIXTES utilisent la formule ÉPOQUE pour le fond et la formule CADRE pour le personnage incrusté.

**Formule CADRE** :

> Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9.

**Formule ÉPOQUE** :

> Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

---

## 3. Roster d'assets

### Personnages récurrents (vues nécessaires, déduites des plans)

| Personnage | Vues à générer | Plans |
|---|---|---|
| Sam | Face, trois quarts, profil, en pied ; assis à la table ; bras écartés (manifeste) ; carnet en main ; expressions : enthousiasme, contrition, gravité ; sacoche givrée (plan 8) ; pansement main droite | 8 à 15, 18, 20, 23, 24, 28, 31, 33, 37, 40, 43, 48, 51, 53, 57, 58, 64, 69, 72, 73, 76, 77, 78 |
| Naya | Face, trois quarts ; penchée en travers de la table ; carnet et crayon ; expressions : émerveillement, concentration, tristesse (carnet fermé) | 7, 10, 14, 20, 40, 43, 48, 53, 58, 75, 78 |
| Elio | Face, trois quarts ; bras croisés ; tablette levée ; tablette posée à plat ; **portrait « gel » en couleurs vives, généré une fois et mutualisé** (plans 15, 25, 27, 34, 52) ; sourire honnête final | 7, 11, 14, 15, 18, 24, 25, 27, 33, 34, 51, 52, 57, 64, 69, 72, 77, 78 |

### Personnages d'époque (fiche à partir de trois plans ; en deçà, génération à la volée)

| Personnage | Plans | Occurrences | Statut | Phrase figée (à copier dans les prompts) |
|---|---|---|---|---|
| Garnerin | 3, 4, 62 (+ réemploi du clip 5 au plan 60) | 3 | **Fiche** | Garnerin, aéronaute au visage résolu, redingote sombre du Directoire, cheveux noués, foulard clair au cou |
| Yuan Huangtou | 44, 45, 47 | 3 | **Fiche** | Yuan Huangtou, prince déchu, maigre et digne, longue tunique usée, cheveux dénoués |
| Badauds parieurs (paire) | 2, 63 | 2 | À la volée, **même référence conservée** (continuité ouverture et fermeture) | badaud rond au chapeau haut à cocarde ; badaud maigre à la canne, habit râpé |
| Paysans du semoir (paire) | 21, 22 | 2 | Même référence sur la scène | paysan couvert de graines, chapeau de paille ; paysan au semoir, tablier de toile |
| Pillards (paire) | 55, 56 | 2 | Même référence sur la scène | pillard trapu aux parasols ; pillard maigre aux sacs |
| Porteurs du pont | 49, 50 | 2 | Même référence sur la scène | porteurs chargés de hottes, sandales de corde |
| L'aide de Garnerin | 3 | 1 | À la volée | aide en veste rude, manches retroussées |
| Empereur Gao Yang | 44 | 1 | À la volée | — |
| Moine Huaibing | 39 (quatre blocs) | 1 | Référence conservée le temps du plan | moine en robe simple, crâne rasé, gestes calmes |
| Cavaliers antiques | 30 | 1 | À la volée | — |
| Cavaliers avars | 32 | 1 | À la volée | — |
| Passants de Ye | 46 | 1 | À la volée | — |
| Badauds du pont (paire) | 50 | 1 | À la volée | — |
| Shun | 54 | 1 | À la volée | — |
| Lenormand | 59 | 1 | Référence conservée entre 59a et 59b | jeune savant ébouriffé, habit clair du XVIIIᵉ |
| Sentinelle et général | 66 | 1 | À la volée | — |
| Compères faux monnayeurs (paire) | 67 | 1 | À la volée | — |
| Alchimistes (paire) | 70 | 1 | Référence conservée entre 70a et 70b | — |
| Charretier han | 29 | 1 | Référence conservée entre 29a et 29b | — |
| Figuration : foule du parc Monceau | 1, 2, 4, 62, 63 | 5 | **Référence de foule réutilisable** (silhouettes du Directoire, sans visage identifiable) | — |

### Décors (plans rattachés ; les suites de plus de deux plans consécutifs sont signalées)

| Décor | Plans | Signalement |
|---|---|---|
| D1 · Parc Monceau au sol, aube | 1, 2, 3, 62, 63 | **1 à 3 consécutifs** |
| D2 · Ciel de Paris (ballon, voilure) | 4, 5, 61 (+ réemploi au 60) | — |
| D3 · Le cadre (intérieur, grande table) | 7 à 15, 18, 20, 23, 24, 28, 31, 33, 37, 40, 43, 48, 51, 53, 57, 58, 64, 69, 72, 73, 75 à 79 | **7 à 15 et 75 à 79 consécutifs** |
| D4 · Ateliers et table de jeu des Tang | 12 | — |
| D5 · Nature (trois vignettes) | 16 | — |
| D6 · Campement préhistorique nocturne | 17 | — |
| D7 · Dégel et planisphère stylisé | 19 | — |
| D8 · Champs des Royaumes combattants | 21, 22 | **consécutifs (quatre lignes avec blocs)** |
| D9 · Brasserie antique (source du gel 25) | 25 | — |
| D10 · Route antique (attelage) | 26, 27 | — |
| D11 · Route han (charretier) | 29 | — |
| D12 · Cour équestre antique | 30 | — |
| D13 · Steppe | 32 | — |
| D14 · Vignettes techniques (boussole, cardan, écluse, gouvernail) | 35 | — |
| D15 · Puits du Sichuan | 36 | — |
| D16 · Marché et verger d'agrumes | 38 | — |
| D17 · Fleuve Jaune en crue | 39 | **quatre blocs consécutifs** |
| D18 · Colline venteuse | 41 | — |
| D19 · Remparts de Taicheng | 42 | — |
| D20 · Ye : tour du Phénix d'or et ville | 44, 45, 46, 47 | **consécutifs** |
| D21 · Gorge du Sichuan (pont de bambou) | 49, 50 | — |
| D22 · Chevalier en armure (source du gel 34) | 34 | — |
| D23 · Pont de chaînes de fer (source du gel 52) | 52 | — |
| D24 · Grenier en flammes | 54 | — |
| D25 · Tour des Song et ruelle | 55, 56 | — |
| D26 · Montpellier (arbre, potager, tour de l'observatoire) | 59 | — |
| D27 · Rempart aux armures | 66 | — |
| D28 · Ruelle aux billets | 67 | — |
| D29 · Vignettes de l'écrit (argile, hiéroglyphes, atelier du papier) | 65 | — |
| D30 · Rouleau imprimé et atelier de Bi Sheng | 68 | — |
| D31 · Fourneaux d'alchimie | 70 | — |
| D32 · Ciel de fête, champ de bataille | 71 | — |
| D33 · Parc actuel ensoleillé (source du POST 74) | 74 | — |

### Accessoires (objets manipulés, montrés en insert ou porteurs de continuité)

| Accessoire | Continuité |
|---|---|
| La sacoche de Sam | Tout l'épisode : elle se vide au plan 9 et se remplit jusqu'au plan 73 |
| Les neuf objets : pétard, carte à jouer, boussole, cerf volant de poche, carré de soie, allumette, billet ancien, petit soc, fer d'attelage | Continuité majeure : la table se vide objet par objet (plans 9, 23, 29, 34, 37, 63, 64, 67, 69, 72, 73) |
| Insert mutualisé « main et sacoche » | Une seule image, objet interchangeable, réutilisée à chaque retour d'objet |
| Tablette d'Elio ; carnet de Naya ; carnet de terrain de Sam | Permanents |
| Ballon, nacelle, couteau, parachute replié puis voilure ouverte | Plans 1 à 6, 60 à 63 — descriptions canoniques en `prompts/S01E01-assets-prompts-v3.4.md` §7 ; le parachute est **gréé entre le ballon et la nacelle**, jamais posé au plancher |
| Hibou de papier | Plans 44, 45, 47 : même objet, continuité stricte |
| Parasols et sacs des pillards | 55, 56 |
| Semoir à trois rangs et soc de fonte | 21, 22 |
| Collier d'épaule | 28, 29 |
| Nids de fourmis et tiges de bambou | 38 |
| Barges, cordes, bœufs de fonte | 39 |
| Livre de La Loubère | 57, 58 |
| Cuirasse de papier ; liasse de billets ; caractères de terre cuite et rouleau du Sutra | 66 ; 67 ; 68 |
| Flacon de verre (teaser) | 78 |

---

## 4. Tableau de plans révisé

Type : FIXE, ANIMÉ ou POST. Registre : CADRE, ÉPOQUE ou MIXTE (le registre choisit la formule de style). La colonne Mouvement caméra porte les mouvements de montage des plans FIXE et la source des plans POST. Le texte dit reste attaché au plan entier (première ligne du plan) et se cale au montage. Chaque bloc après le premier démarre sur la dernière image du bloc précédent.

| N° | Bloc | Durée (s) | Registre | Type | Description visuelle | Mouvement caméra | Texte dit |
|---|---|---|---|---|---|---|---|
| 1 | a | 9 | ÉPOQUE | ANIMÉ | Aube d'octobre : brume sur les pelouses du parc Monceau, le ballon gonflé oscille dans le vent au milieu d'une foule en habits du Directoire, année 1797. | — | — (muet, musique) |
| 1 | b | 9 | ÉPOQUE | ANIMÉ | La foule s'écarte et tourne les têtes vers la nacelle qu'on amène sous le ballon, cordages tendus. | — | — |
| 2 |  | 10 | ÉPOQUE | FIXE | Deux badauds au premier plan, cocardes et chapeaux, la nacelle en fond. | Travelling latéral lent vers la droite, des badauds vers la nacelle | BADAUD 1 : « Il va se tuer, je vous dis. » BADAUD 2 : « Dix francs qu'il ne coupe pas la corde. » |
| 3 |  | 12 | ÉPOQUE | FIXE | Dans la nacelle, Garnerin, la main sur la corde de largage, regarde le ballon mâchoire serrée ; son aide, **au sol à l'extérieur**, le supplie ; le parachute replié **suspendu entre le ballon et la nacelle** (correction du 27 août 2026). | Zoom avant lent sur la main de Garnerin serrant la corde | L'AIDE : « Citoyen Garnerin, renoncez, il est encore temps. » GARNERIN : « Lâchez tout. » |
| 4 | a | 10 | ÉPOQUE | ANIMÉ | Le ballon quitte le sol, la foule bascule en arrière pour le suivre des yeux. | — | — (muet) |
| 4 | b | 10 | ÉPOQUE | ANIMÉ | Vu d'en haut, les toits de Paris rapetissent, la foule devient une tache sombre ; le vent siffle. | — | — |
| 5 |  | 8 | ÉPOQUE | ANIMÉ | Très gros plan : la lame tranche la corde qui retient la nacelle au ballon. | — | — (muet) |
| 6 |  | 13 | MIXTE | POST | L'image se fige en pleine chute ; carton titre « LES DÉCOUVREURS — Nos ancêtres les Chinois ». | Source : dernière image du plan 5 ; traitement : figement, incrustation du carton titre | SAM (voix off) : « Octobre 1797 : tout Paris est venu voir un homme tomber du ciel. Mais pour savoir s'il se relèvera, il faut d'abord faire un très long détour... par la Chine. » |
| 7 |  | 13 | CADRE | FIXE | Intérieur du cadre en couleurs saturées : Naya griffonne, Elio pianote, deux tasses fument sur la grande table. | Panoramique lent vers la droite, de Naya à Elio | NAYA : « Il n'est jamais en retard. J'espère qu'il ne lui est rien arrivé. » ELIO : « Lui ? Il est solide comme un roc. Je parie qu'il arrive avec une histoire impossible. » |
| 8 | a | 9 | CADRE | ANIMÉ | La porte s'ouvre en coup de vent : Sam entre, transi, sacoche givrée à l'épaule, et secoue sa veste sable. | — | SAM : « Quelle circulation ! Quel froid ! Quelle... enfin, regardez ma sacoche : de la glace ! Et cette éraflure, cadeau du verglas. Un thé bien chaud, quelqu'un ? Merci. Où j'en étais, déjà ? Ah oui : nulle part, je viens d'arriver. » |
| 8 | b | 9 | CADRE | ANIMÉ | Il s'avance vers la table en gesticulant, pansement visible sur la main droite, et se laisse tomber sur sa chaise. | — | — |
| 9 | a | 6 | CADRE | ANIMÉ | Sam retourne sa sacoche couverte d'étiquettes : les premiers objets déferlent sur la table. | — | SAM : « Le butin du jour. » |
| 9 | b | 6 | CADRE | ANIMÉ | La cascade continue — pétard, carte à jouer, boussole, cerf volant de poche, carré de soie, allumette, billet ancien, petit soc, fer d'attelage ; la boussole roule jusqu'au bord, une main la rattrape. | — | — |
| 10 |  | 10 | CADRE | FIXE | Naya penchée sur le fouillis, yeux écarquillés, crayon suspendu. | Panoramique lent vers le bas, du visage de Naya vers le fouillis d'objets | NAYA : « C'est quoi, tout ça ? » SAM : « Neuf objets... et une seule origine. » |
| 11 |  | 12 | CADRE | FIXE | Contrechamp sur Elio, moue de défi sous la casquette orange. | Zoom avant lent sur Elio | ELIO : « Moi, je préfère qu'on parle des cowboys. Et pan pan ! » SAM : « Pan pan ? Parfait : le fusil, la poudre, le canon — chinois, chinois, chinois. » |
| 12 |  | 15 | ÉPOQUE | FIXE | Bref montage : fours de potiers, vases de porcelaine translucide, joueurs de cartes sous les Tang. | 2 images (fours et porcelaine ; joueurs de cartes) ; zoom avant lent sur chacune | SAM (voix off) : « La porcelaine de ton saloon ? Maîtrisée huit à dix siècles avant l'Europe — Meissen n'en percera le secret qu'en 1708. Et les cartes à jouer du poker : cinq siècles avant tout le monde. » |
| 13 |  | 17 | CADRE | FIXE | Sam écarte les bras devant la table couverte d'objets, ton de manifeste. | Zoom arrière lent, de la table couverte d'objets à Sam bras écartés | SAM : « Tout ce qui nous entoure semble évident. Mais il a fallu des milliers d'années d'efforts et d'ingéniosité pour en arriver là. Donc cette série racontera les découvreurs et leurs découvertes. Barbant ? C'est le plus passionnant de tous les romans. » |
| 14 |  | 12 | CADRE | FIXE | Naya lève son crayon : la question du jour ; Elio croise les bras. | Panoramique lent vers la droite, de Naya à Elio | NAYA : « Alors qui a trouvé quoi en premier ? » ELIO : « Et surtout : des preuves. Objet par objet. C'est même pas vrai, la moitié de ce qu'on raconte. » |
| 15 |  | 15 | MIXTE | POST | Elio lève sa tablette, la table passe en gris figé : plan signature du gel, puis retour couleurs. | Source : image FIXE de la table du cadre ; traitement : désaturation du fond, Elio conservé en couleurs, retour couleurs en fin de plan | ELIO : « La règle : chaque objet vérifié retourne dans la sacoche. S'il en reste un sur la table à la fin, tu as perdu. » SAM : « Tenu. Donc commençons par le commencement. Le tout premier inventeur. » |
| 16 |  | 22 | ÉPOQUE | FIXE | Montage nature — un oiseau tisserand noue son nid, un singe casse une noix avec une pierre, une loutre sur le dos ouvre un coquillage. | 3 images (oiseau ; singe ; loutre) ; zoom avant lent sur chacune | SAM (voix off) : « Les premiers inventeurs n'étaient sans doute pas des hommes. Les oiseaux bâtissent, les singes cassent, les loutres martèlent. Le hasard aide souvent ; le génie, c'est de le remarquer. » |
| 17 | a | 10 | ÉPOQUE | ANIMÉ | Silhouettes préhistoriques : un éclat de silex jaillit sous le percuteur. | — | SAM (voix off) : « Donc viennent le premier outil, la première arme, le premier feu. Trois inventions qui n'ont pas d'inventeur connu... et qui portent toutes les autres. » |
| 17 | b | 10 | ÉPOQUE | ANIMÉ | Une flamme prend dans la nuit, des visages s'éclairent lentement. | — | — |
| 18 |  | 17 | CADRE | FIXE | Elio consulte sa tablette posée à plat, sans figer, presque poli. | Zoom avant lent sur la tablette posée à plat | ELIO : « Détail : les plus vieux outils taillés ont 3,3 millions d'années. Avant même le genre humain. » SAM : « Donc les premiers tailleurs de pierre n'étaient pas encore des hommes. Belle leçon de modestie pour ouvrir une série sur le génie. » |
| 19 |  | 24 | ÉPOQUE | FIXE | Grand montage : les glaciers reculent, des pousses percent, sept vignettes s'allument sur un planisphère stylisé — blé, riz, millets, maïs, tubercules. | 2 images (glaciers et pousses ; planisphère aux vignettes) ; zoom arrière lent sur le planisphère | SAM (voix off) : « Puis le climat se réchauffe, il y a environ douze mille ans. Donc, un peu partout, on cesse de courir après la nourriture : on la fait pousser. Pas une découverte : sept ou huit, indépendantes — dont deux en Chine, le riz au sud, les millets au nord. » |
| 20 |  | 15 | CADRE | FIXE | Naya fronce les sourcils, carnet ouvert. | Zoom avant lent sur Naya | NAYA : « On m'avait dit : c'est parce que le gibier manquait. » SAM : « Vieille chanson. Le vrai moteur, c'est le climat. Et retiens ceci : la Chine n'a pas reçu l'agriculture — elle en est un berceau. » |
| 21 | a | 8 | ÉPOQUE | ANIMÉ | Champs des Royaumes combattants : le premier paysan sème à la volée dans le vent, nuage de graines. | — | SAM (voix off) : « Donc les Chinois la perfectionnent : culture en ligne, sarclage, soc de charrue en fonte, et bientôt le semoir à rangs multiples. » |
| 21 | b | 8 | ÉPOQUE | ANIMÉ | L'autre paysan pousse un semoir de bois à trois rangs derrière un soc de fonte ; sillons impeccables. | — | — |
| 21 | c | 8 | ÉPOQUE | ANIMÉ | Plan large des deux parcelles côte à côte ; le premier s'arrête, bouche ouverte. | — | — |
| 22 |  | 12 | ÉPOQUE | FIXE | Les deux paysans face à face, l'un couvert de graines, l'autre appuyé sur son semoir. | Travelling latéral lent vers la gauche, du paysan couvert de graines au semoir | PAYSAN 1 : « Trois rangs d'un coup ? Et droits, en plus ! » PAYSAN 2 : « Droits comme la parole du juge. À toi les oiseaux, à moi la récolte. » |
| 23 |  | 12 | CADRE | FIXE | Insert — le petit soc quitte la table et rejoint la sacoche. | Zoom avant lent sur la sacoche ouverte | SAM : « L'Europe attendra le semoir de Jethro Tull... en 1701. Deux mille ans, vous vous rendez compte ? Premier objet vérifié, premier objet rangé. » |
| 24 |  | 10 | CADRE | FIXE | Sam s'emballe, l'index levé, une chope imaginaire à la main ; Elio lève déjà sa tablette. | Panoramique lent vers la droite, de Sam à Elio | SAM : « Et la cervoise des Gaulois ? On brassait en Chine bien avant ! » ELIO : « Gel. » |
| 25 |  | 16 | MIXTE | POST | GEL : Elio en couleurs vives devant une brasserie antique figée en gris. | Source : image ÉPOQUE « brasserie antique » à générer ; traitement : désaturation totale, incrustation d'Elio en couleurs (portrait FIXE dédié, réutilisable pour tous les gels) | ELIO : « Vérifié : on brassait en Chine très tôt, c'est vrai. Mais la bière est née avant en Mésopotamie et en Égypte. » SAM : « ...Donc la cervoise sort de la liste. Personne n'est parfait — pas même mes Chinois. » |
| 26 |  | 18 | ÉPOQUE | FIXE | Un attelage antique tire une charrette, jougs et sangles bien visibles sur le poitrail. | Travelling latéral lent le long de l'attelage, du poitrail vers la charge | SAM (voix off) : « L'agriculture mène à l'attelage. Et là, une histoire célèbre : le harnais antique, à ce qu'on racontait partout, étranglait le cheval... » |
| 27 |  | 12 | MIXTE | POST | GEL : Elio fige l'attelage en gris, tablette levée. | Source : image du plan 26 ; traitement : désaturation totale, incrustation d'Elio en couleurs | ELIO : « On racontait faux. L'expérience l'a réfuté en 1977 : l'attelage antique tirait sur le poitrail et les épaules. Le cheval respirait très bien. » |
| 28 |  | 18 | CADRE | FIXE | Sam s'incline, puis pointe l'écran où apparaît un collier d'épaule rembourré. | Travelling latéral lent vers la droite, de Sam vers l'écran mural | SAM : « Donc je corrige : pas de cheval étranglé. Mais le collier d'épaule chinois reste une vraie avancée : la charge augmente — sans le fameux "dix fois plus" des vieux livres —, et l'Europe l'adopte trois à cinq siècles plus tard. » |
| 29 | a | 10 | ÉPOQUE | ANIMÉ | Le charretier han passe le collier d'épaule à son cheval. | — | SAM (voix off) : « Donc voilà le cheval promu bête de trait... avec le panache en plus. Deuxième objet rangé. » |
| 29 | b | 10 | ÉPOQUE | ANIMÉ | Le cheval se rengorge comme un général, la lourde charrette s'ébranle sans effort. | — | — |
| 30 | a | 10 | ÉPOQUE | ANIMÉ | Un cavalier antique prend son élan, saute vers sa monture... et glisse de l'autre côté (gag). | — | SAM (voix off) : « Atteler ne suffit pas : il faut monter. Ni les Égyptiens, ni les Grecs, ni les Romains ne connaissaient l'étrier. Monter à cheval était un sport de voltige... ou de domestiques. » |
| 30 | b | 10 | ÉPOQUE | ANIMÉ | Un second cavalier se fait hisser par deux serviteurs, dignité en berne. | — | — |
| 31 |  | 15 | CADRE | FIXE | Sam feuillette son carnet de terrain, honnête. | Zoom avant lent sur le carnet de terrain | SAM : « Et les Chinois ? Longtemps, on leur a prêté des étriers de métal du temps des Grecs. Mon carnet dit : premier étrier attesté en 302, première paire en 415. Tardif... mais décisif. » |
| 32 | a | 8 | ÉPOQUE | ANIMÉ | La steppe au galop : cavaliers avars en ligne, étriers luisants. | — | SAM (voix off) : « Donc, en 567, les Avars le portent jusqu'en Europe : les plus vieux étriers du continent sortent de leurs tombes. » |
| 32 | b | 8 | ÉPOQUE | ANIMÉ | La poussière dorée monte, la horde file. | — | — |
| 32 | c | 6 | ÉPOQUE | ANIMÉ | L'horizon de l'Europe se dessine au loin. | — | — |
| 33 |  | 12 | CADRE | FIXE | Sam se lève à moitié, bras déployé, ton de grande fresque ; Elio lève sa tablette. | Zoom arrière lent, de Sam au cercle du cadre | SAM : « Et voilà comment l'étrier chinois fit naître la chevalerie d'Occident ! » ELIO : « Gel. » |
| 34 |  | 15 | MIXTE | POST | GEL : un chevalier en armure figé en gris derrière Elio. | Source : image ÉPOQUE « chevalier en armure » à générer ; traitement : désaturation, incrustation d'Elio en couleurs | ELIO : « Trop simple : les historiens ont conclu que ce rôle était très surestimé. » SAM : « Exact. L'étrier aide le cavalier ; il ne fabrique pas une société. Donc je range mon envolée... et l'étrier dans la sacoche. » |
| 35 |  | 22 | ÉPOQUE | FIXE | Montage : aiguille de boussole qui pivote, cardan, écluse, gouvernail d'étambot sous une jonque. | 4 images (boussole ; cardan ; écluse ; gouvernail) ; zoom avant lent sur chacune | SAM (voix off) : « Donc la liste continue : la boussole — décrite en 1088, un siècle d'avance seulement, celle là —, le cardan, les écluses, le gouvernail... » ELIO (off) : « Et la vapeur ? » SAM (off) : « Déjà sortie de la liste. Bien essayé. » |
| 36 |  | 14 | ÉPOQUE | FIXE | Le Sichuan : hautes tours de bambou, câbles qui plongent dans des puits ; une flamme de gaz brûle près d'un bassin de saumure. | Panoramique vertical lent, du sommet des tours de bambou vers le puits | SAM (voix off) : « Ajoutez le forage profond, au Sichuan, dès le IIᵉ siècle avant notre ère : des tours de bambou pour puiser la saumure... et déjà le pétrole. » |
| 37 |  | 12 | CADRE | FIXE | Insert — l'allumette quitte la table pour la sacoche. | Zoom avant lent sur la sacoche ouverte | SAM : « L'allumette ? En 577, des dames de cour assiégées enduisent des bâtonnets de soufre. La moderne attendra 1827 : douze siècles et demi d'écart. Objet rangé. » |
| 38 | a | 9 | ÉPOQUE | ANIMÉ | Au marché du sud, des paysans achètent des nids de fourmis. | — | SAM (voix off) : « En 304, seize siècles avant l'Occident, un lettré décrit la lutte biologique : des fourmis achetées au marché pour garder les vergers, des ponts de bambou pour leurs rondes. L'Europe y viendra en 1888... avec une coccinelle. » |
| 38 | b | 9 | ÉPOQUE | ANIMÉ | Ils tendent des tiges de bambou d'arbre en arbre dans le verger d'agrumes. | — | — |
| 38 | c | 8 | ÉPOQUE | ANIMÉ | Colonnes de fourmis en patrouille sur les tiges ; une chenille happée. | — | — |
| 39 | a | 8 | ÉPOQUE | ANIMÉ | Le fleuve Jaune en crue : les bœufs de fonte disparaissent sous l'eau boueuse. | — | — (muet, musique) |
| 39 | b | 8 | ÉPOQUE | ANIMÉ | Le moine Huaibing fait charger deux barges de terre ; les cordes se tendent vers le fond. | — | — |
| 39 | c | 8 | ÉPOQUE | ANIMÉ | On vide la terre des barges, pelletée après pelletée. | — | — |
| 39 | d | 8 | ÉPOQUE | ANIMÉ | Les barges remontent et arrachent les bœufs du fond, cris de joie sur la rive. | — | — |
| 40 |  | 13 | CADRE | FIXE | Naya, soufflée, redessine le principe dans son carnet. | Zoom avant lent sur la page du carnet de Naya | NAYA : « Donc il soulève des bœufs de fer... en vidant de la terre ? » SAM : « Par la seule flottaison, vers 1060. Mille ans plus tard, on ne renfloue toujours pas autrement. » |
| 41 | a | 10 | ÉPOQUE | ANIMÉ | Colline venteuse, Vᵉ siècle avant notre ère : des artisans assemblent le grand oiseau de bois et de soie. | — | SAM (voix off) : « Mais tout ne se joue pas au sol. Dès le Vᵉ siècle avant notre ère, les Chinois font tenir des ailes dans le vent : le cerf volant. » |
| 41 | b | 10 | ÉPOQUE | ANIMÉ | L'oiseau monte au bout de son fil et tient dans le vent. | — | — |
| 42 | a | 10 | ÉPOQUE | ANIMÉ | Remparts assiégés : des cerfs volants s'élèvent, emportant des rouleaux. | — | SAM (voix off) : « On racontait la scène mille ans trop tôt ; la chronique la date de 549 de notre ère, au siège de Taicheng. Donc je la remets à sa place : des assiégés confient au vent leurs appels au secours. » |
| 42 | b | 10 | ÉPOQUE | ANIMÉ | Des flèches montent des lignes ennemies ; les cerfs volants filent vers l'horizon. | — | — |
| 43 |  | 12 | CADRE | FIXE | Naya, doigt levé, la question qui fait basculer le chapitre. | Zoom arrière lent, de Naya au cercle du cadre | NAYA : « Si le vent porte un message... il peut porter quelqu'un ? » SAM : « Quelqu'un l'a prouvé. Mais pas de son plein gré. » |
| 44 |  | 22 | ÉPOQUE | FIXE | Ye, 559 : la tour du Phénix d'or dressée sur la ville ; l'empereur Gao Yang au sommet ; un prisonnier maigre et digne attaché à un immense hibou de papier. | Zoom avant lent sur les mains liées aux montants du hibou | SAM (voix off) : « En 559, l'empereur Gao Yang "libère" ses prisonniers du haut d'une tour, à sa manière. Ce jour, le prisonnier s'appelle Yuan Huangtou, fils d'un empereur déchu. » |
| 45 | a | 10 | ÉPOQUE | ANIMÉ | Le hibou décroche de la tour, pique vers le sol, la cour hurle. | — | — (muet, musique seule) |
| 45 | b | 10 | ÉPOQUE | ANIMÉ | Le vent le prend, il frôle les remparts. | — | — |
| 45 | c | 10 | ÉPOQUE | ANIMÉ | Il plane sur la ville minuscule et se pose rudement sur une longue voie. | — | — |
| 46 |  | 14 | ÉPOQUE | FIXE | Vu du sol : des passants lèvent la tête, bouche ouverte, vers la silhouette qui plane dans le ciel pâle. | Panoramique lent le long des visages levés | — (muet) |
| 47 |  | 14 | ÉPOQUE | FIXE | Des gardes le relèvent ; une porte de cachot se referme ; le hibou de papier reste accroché à un arbre. | 2 images (les gardes l'encadrent ; la porte close et le hibou dans l'arbre) ; zoom avant lent sur chacune | SAM (voix off) : « Il plane près de 2,5 kilomètres et se pose vivant : le premier homme volant de l'humanité. Mais son vol ne le libère pas — il meurt en captivité peu après. » |
| 48 |  | 14 | CADRE | FIXE | Silence ; Naya a refermé son carnet. | Zoom avant lent sur Naya et son carnet refermé | NAYA : « Donc le premier vol humain... est une exécution. » SAM : « La chronique le raconte ainsi, et les historiens la citent. Gardez cette histoire en tête : elle pèsera dans la morale du jour. » |
| 49 | a | 8 | ÉPOQUE | ANIMÉ | Gorge du Sichuan : le pont de câbles de bambou tendu en travers du vide. | — | SAM (voix off) : « Franchir le vide, maintenant. Le pont suspendu vient bien de Chine : les câbles de bambou du Sichuan, décrits dès le Iᵉʳ siècle de notre ère. » |
| 49 | b | 8 | ÉPOQUE | ANIMÉ | Des porteurs chargés s'y engagent. | — | — |
| 49 | c | 6 | ÉPOQUE | ANIMÉ | Le tablier ondule sous leurs pas, le vide dessous. | — | — |
| 50 |  | 14 | ÉPOQUE | FIXE | Deux badauds au bord de la gorge ; le porteur traverse tranquillement derrière eux. | Travelling latéral lent vers la droite, des badauds au porteur qui traverse | LE BADAUD : « Ça ne tiendra jamais. Ça ne tiendra jamais, je te dis. » L'AUTRE : « Il est passé. » LE BADAUD : « ...C'est bien ce que je disais. » |
| 51 |  | 12 | CADRE | FIXE | Sam, grandiose ; Elio lève sa tablette. | Panoramique lent vers la droite, de Sam à Elio | SAM : « Deux mille ans avant l'Occident ! Et il lui faudra cinq siècles de plus pour l'égaler ! » ELIO : « Gel. » |
| 52 |  | 17 | MIXTE | POST | GEL : un pont de chaînes de fer figé en gris derrière Elio. | Source : image ÉPOQUE « pont de chaînes de fer » à générer ; traitement : désaturation, incrustation d'Elio en couleurs | ELIO : « Faux : premier pont de fer occidental en 1801, le pont de Menai en 1826. 25 ans, pas 500. » SAM : « Donc l'Occident rattrape parfois très vite. C'est aussi ça, l'histoire des techniques : des avances, des dégradés... et des sprints. » |
| 53 |  | 12 | CADRE | FIXE | Naya fixe le pont à l'écran, une main crispée sur son carnet. | Zoom avant lent sur l'écran mural où s'affiche le pont | NAYA : « Et si la corde casse ? » SAM : « Alors il faut apprendre à tomber sans mourir. Donc : notre morceau de soie. » |
| 54 | a | 8 | ÉPOQUE | ANIMÉ | Chine légendaire : le grenier en flammes dans la nuit, le jeune homme cerné au sommet. | — | SAM (voix off) : « La plus vieille histoire vient du Shiji : le souverain légendaire Shun échappe à un grenier en feu, accroché à deux chapeaux de paille. Ça s'est passé ainsi ? Rien ne le prouve : c'est une légende. Mais quelle légende ! » |
| 54 | b | 8 | ÉPOQUE | ANIMÉ | Il saute, freiné par les deux grands chapeaux coniques. | — | — |
| 54 | c | 6 | ÉPOQUE | ANIMÉ | Il roule dans la poussière et se relève dans les étincelles. | — | — |
| 55 |  | 12 | ÉPOQUE | FIXE | Chine des Song, nuit : deux pillards sur le toit d'une tour, sacs de butin et grands parasols. | Panoramique lent vers le bas, du toit de la tour à la ruelle | PILLARD 1 : « C'est moi qui saute avec le butin : je suis le plus léger. » PILLARD 2 : « Alors moi, je fais quoi ? » |
| 56 | a | 7 | ÉPOQUE | ANIMÉ | Le premier pillard saute avec parasols et sacs. | — | — (muet, gag) |
| 56 | b | 7 | ÉPOQUE | ANIMÉ | Atterrissage en douceur dans une charrette de paille ; l'autre gesticule tout en haut. | — | — |
| 57 |  | 12 | CADRE | FIXE | Sam, très sûr de lui, brandit un vieux volume ; Elio lève sa tablette. | Zoom avant lent sur le volume brandi | SAM : « Ensuite, un ambassadeur de France voit tout cela en Chine, et son récit file droit vers l'Europe. » ELIO : « Gel. Montre la page de titre. » |
| 58 |  | 18 | CADRE | FIXE | Insert : la page gravée du livre de Simon de La Loubère, planche d'acrobates sous de grands parasols. | Panoramique lent vers le bas sur la planche gravée | NAYA (lisant) : « "Du royaume de Siam"... Siam ? Ce n'est pas la Chine ! » SAM : « Exact, je corrige : l'envoyé s'appelle La Loubère, et ses acrobates sautent à Ayutthaya. Donc l'idée a voyagé en Asie, mais la page qui traverse l'Europe vient du Siam. » |
| 59 | a | 10 | ÉPOQUE | ANIMÉ | Montpellier : Lenormand saute d'un arbre avec deux parasols et atterrit dans un potager. | — | SAM (voix off) : « Donc, en France, le jeune Lenormand essaie : d'abord d'un arbre, puis, en 1783, de la tour de l'observatoire — premier saut public attesté. En 1785, il forge le mot : parachute. » |
| 59 | b | 10 | ÉPOQUE | ANIMÉ | Devant une foule, il descend lentement de la tour de l'observatoire sous un grand cadre de toile ; une plume trace un mot neuf. | — | — |
| 60 |  | 14 | ÉPOQUE | POST | Raccord exact avec le plan 5 : la lame tranche la corde, la nacelle décroche, la foule pousse un seul cri. | Source : réutilisation du clip du plan 5, remonté tel quel ; aucun nouveau rendu (le cri de la foule est au mixage son) | SAM (voix off) : « Mais son cadre rigide ne s'emporte pas sous un ballon. Donc nous revoilà en 1797, à la verticale du parc Monceau — sous un ballon à hydrogène, pas une montgolfière : vérifié. » |
| 61 |  | 10 | ÉPOQUE | ANIMÉ | Vue depuis l'intérieur de la voilure : la soie jaillit du paquet et s'épanouit en corolle blanche, les cordages chantent. | — | — (muet) |
| 62 | a | 10 | ÉPOQUE | ANIMÉ | La descente balance violemment de gauche à droite, la foule retient son souffle. | — | — (muet, musique) |
| 62 | b | 9 | ÉPOQUE | ANIMÉ | Atterrissage brutal dans une allée, roulade, la voilure le recouvre. | — | — |
| 62 | c | 9 | ÉPOQUE | ANIMÉ | Il en émerge en boitant, bras levés, la foule explose. | — | — |
| 63 |  | 16 | ÉPOQUE | FIXE | Les deux badauds de l'ouverture ; l'un paie, l'autre encaisse. | Zoom avant lent sur les mains qui échangent les pièces | BADAUD 2 (tendant la main) : « Mes dix francs. » BADAUD 1 (payant) : « Il a coupé... et il marche. Enfin, il boite. » SAM (voix off) : « Une entorse pour tout dommage. Donc le verdict est rendu : on peut tomber du ciel et se relever. Deux objets rangés d'un coup. » |
| 64 |  | 19 | CADRE | FIXE | Sur la table, il ne reste que la carte, le billet, la boussole et le pétard ; Elio les compte du doigt. | Travelling latéral lent vers la droite, le long des quatre derniers objets | ELIO : « Quatre objets. » SAM : « Donc accélérons — la boussole est déjà vérifiée, elle rentre. Et presque tout le reste tient dans une feuille : la voilure de Garnerin est en soie, la soie coûte un champ... le support du pauvre, lui, va conquérir le monde. » |
| 65 |  | 21 | ÉPOQUE | FIXE | Montage : tablette d'argile d'Uruk, hiéroglyphes peints, puis un atelier han où l'on presse la pâte à papier et lève des feuilles claires. | 3 images (argile ; hiéroglyphes ; atelier du papier) ; zoom avant lent sur chacune | SAM (voix off) : « L'écriture naît sur l'argile d'Uruk il y a cinq mille quatre cents ans, presque en même temps que les hiéroglyphes. Mais le papier est chinois : deux siècles avant notre ère — et en 105, un intendant nommé Cai Lun le perfectionne et le fait adopter par la cour. » |
| 66 |  | 18 | ÉPOQUE | FIXE | Saynète sur un rempart : un général adverse palpe la cuirasse de feuilles pliées d'une sentinelle ravie. | Travelling latéral lent vers la gauche, le long du chemin de ronde | LA SENTINELLE : « Trois flèches arrêtées, général, et mes épaules ne pèsent plus rien. » LE GÉNÉRAL : « Légère... et cent hommes armés pour le prix de dix. J'échange vos cuirasses contre les miennes. » SAM (voix off) : « L'armure de papier vaut surtout par son prix : le métal reste le métal. » |
| 67 |  | 14 | ÉPOQUE | FIXE | Saynète dans une ruelle : deux compères, une liasse de billets entre eux ; une patrouille passe au fond ; ils enterrent la liasse. | Zoom avant lent sur la liasse que l'on enterre | COMPÈRE 1 : « Du simple papier ! On peut en faire autant qu'on veut. Riches, on va être riches. » SAM (voix off) : « Le vrai billet naît au Sichuan vers 1023. Mais la contrefaçon, elle, est punie de mort. » |
| 68 |  | 22 | ÉPOQUE | FIXE | Un rouleau imprimé se déroule — le Sutra du diamant — puis l'atelier de Bi Sheng : des milliers de petits caractères de terre cuite alignés dans des casiers, une plaque composée à la cire. | 2 images ; travelling latéral lent le long du rouleau, puis zoom avant lent sur les casiers | SAM (voix off) : « Donc le papier appelle l'imprimerie : en 868, le plus ancien livre imprimé complet qui nous soit parvenu ; vers 1045, Bi Sheng grave des caractères mobiles en terre cuite — des milliers, là où notre alphabet en demande 26. » |
| 69 |  | 23 | CADRE | FIXE | Elio, tablette posée, sourcil levé ; Sam répond carnet en main. | Panoramique lent vers la gauche, d'Elio à Sam | ELIO : « Et ensuite, l'imprimerie apparaît en Europe... comme par miracle ? » SAM : « Aucun miracle documenté : les historiens parlent d'inventions convergentes. Et entre les deux, un maillon coréen : le Jikji, imprimé en 1377, soixante ans avant Gutenberg — dont la presse est un système à part. La carte à jouer, elle, rentre au bercail. » |
| 70 | a | 10 | ÉPOQUE | ANIMÉ | Fourneaux d'alchimistes : cornues, fumées, gestes précautionneux. | — | SAM (voix off) : « Mais tout n'est pas rose dans la sacoche. En cherchant un élixir de longue vie, les alchimistes trouvent la poudre : de quoi raccourcir celle des hommes. » |
| 70 | b | 10 | ÉPOQUE | ANIMÉ | La détonation fait trembler les jarres ; deux savants couverts de suie. | — | — |
| 71 | a | 10 | ÉPOQUE | ANIMÉ | Fusées de fête dans un ciel de nouvel an. | Fondu entre 71a et 71b réalisé au montage | SAM (voix off) : « Les fusées naissent pour la fête. Donc, fatalement, quelqu'un les tourne vers la guerre : lances de feu, canons, fusils. Encore quelques siècles, et tout cela atteindra l'Occident. » |
| 71 | b | 10 | ÉPOQUE | ANIMÉ | Flèches de feu, canons et fusils sur un champ de bataille. | — | — |
| 72 |  | 12 | CADRE | FIXE | Le pétard, dernier objet sur la table ; Sam le regarde sans le prendre. | Zoom avant lent sur le pétard, dernier objet de la table | ELIO : « Il en reste un. » SAM : « Je sais. Ce dernier, je le range sans fierté. » |
| 73 |  | 12 | CADRE | FIXE | Sam range lentement le pétard, referme la sacoche à demi. | Zoom avant lent sur la sacoche qui se referme | SAM : « Le même peuple a inventé le semoir et le canon, le billet et la poudre. Donc l'invention ne choisit pas : c'est nous qui choisissons. » |
| 74 |  | 18 | MIXTE | POST | Surimpression : la silhouette du prince volant sous son hibou de papier... et un petit cerf volant de fête, aujourd'hui, dans un parc ensoleillé. | Sources : 2 images FIXE à générer (le prince sous son hibou, registre ÉPOQUE ; le cerf volant dans un parc actuel, registre CADRE) ; traitement : surimpression croisée au montage | SAM (voix off) : « Le premier vol humain fut une exécution ; le même cerf volant fait rire nos parcs. Tout le chemin des inventions tient entre ces deux images. » |
| 75 |  | 12 | CADRE | FIXE | Insert sur le carnet de Naya : la page s'écrit sous son crayon. | Zoom avant lent sur la page du carnet qui s'écrit | NAYA (en écrivant) : « Regarder, voir, ça ne suffit pas. Il faut observer, comparer, déduire. C'est ça, la science. » |
| 76 |  | 12 | CADRE | FIXE | Sam, doux, chapeau repoussé en arrière, sans aucun triomphe. | Zoom avant très lent sur Sam | SAM : « Les inventions peuvent et doivent signifier progrès, et non pas agression. S'il le veut, l'homme saura être utile, bienfaisant, et parfois même génial. » |
| 77 |  | 12 | CADRE | FIXE | Elio contemple la table vide, tablette baissée, petit sourire honnête. | Zoom arrière lent, d'Elio à la table vide | ELIO : « La table est vide. Tu as gagné... grâce aux corrections. » SAM : « Donc nous avons gagné ensemble. Vérifier, ce n'est pas perdre : c'est ça, découvrir. » |
| 78 |  | 14 | CADRE | FIXE | Sam sort de sa sacoche un petit flacon de verre au liquide clair ; Naya et Elio se penchent d'un même mouvement. | Zoom avant lent sur le flacon de verre | NAYA : « Et ça ? » SAM : « Un flacon qui a sauvé des millions de mères... mais ça, c'est pour la prochaine fois. » |
| 79 |  | 10 | CADRE | ANIMÉ | La sacoche fermée sur la table ; par la fenêtre du cadre, un cerf volant monte dans le soir. | Fondu final réalisé au montage | — (muet, fin) |

---

## 5. Prompts — plans 1 à 6 (pilote de format)

Les prompts des plans 7 à 79 seront produits après validation de ce format. Registre des six plans : ÉPOQUE (formule ÉPOQUE collée intégralement). Références d'image par appel : sept maximum, dans l'ordre décor, personnages, accessoires.

### Plan 1a — image de départ

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : à l'aube, brume sur les pelouses du parc Monceau, un grand ballon gonflé oscille au milieu d'une foule en habits du Directoire.
Cadrage : très grand ensemble, légère plongée.
Décor : D1 · Parc Monceau au sol, aube.
Personnages : figuration, foule du parc Monceau (silhouettes du Directoire, sans visage identifiable).
Accessoires : ballon, nacelle, cordages.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 1a — mouvement (9 s)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

PLAN 1 (0.0 à 2.5s) : la brume glisse sur les pelouses, la foule ondule doucement au pied du ballon.
COUPE NETTE
PLAN 2 (2.5 à 5.0s) : plan moyen sur le ballon qui oscille dans le vent, cordages qui se tendent.
COUPE NETTE
PLAN 3 (5.0 à 7.0s) : vue du sol vers le sommet du ballon, les bannières claquent.
COUPE NETTE
PLAN 4 (7.0 à 9.0s) : grand ensemble, la foule tourne les têtes d'un même mouvement vers la nacelle.

Cadence d'animation limitée, autour de 10 images par seconde.
Les personnages gesticulent et réagissent, ils ne parlent pas.
Mouvement dès la première image, aucun démarrage figé.
NÉGATIF : rendu photoréaliste, texture de peau, dégradés lisses, mouvement de caméra fluide et continu.
```

### Plan 1b — image de départ (continuité : dernière image du bloc 1a)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : la foule s'écarte en deux haies ; on amène la nacelle d'osier sous le ballon, cordages tendus.
Cadrage : ensemble, hauteur d'homme, dans l'axe de la haie.
Décor : D1 · Parc Monceau au sol, aube.
Personnages : figuration, foule du parc Monceau.
Accessoires : nacelle, cordages, ballon en fond.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 1b — mouvement (9 s)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

PLAN 1 (0.0 à 3.0s) : la foule s'écarte en deux haies, chapeaux qui se lèvent.
COUPE NETTE
PLAN 2 (3.0 à 6.0s) : plan moyen latéral, la nacelle avance portée par des aides, cordages traînants.
COUPE NETTE
PLAN 3 (6.0 à 9.0s) : plan rapproché sur la nacelle qu'on arrime sous le ballon, mains qui nouent.

Cadence d'animation limitée, autour de 10 images par seconde.
Les personnages gesticulent et réagissent, ils ne parlent pas.
Mouvement dès la première image, aucun démarrage figé.
NÉGATIF : rendu photoréaliste, texture de peau, dégradés lisses, mouvement de caméra fluide et continu.
```

### Plan 2 — image clé (FIXE)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : deux badauds au premier plan se penchent l'un vers l'autre pour parier, la nacelle et la foule en fond.
Cadrage : plan rapproché taille, vue légèrement basse.
Décor : D1 · Parc Monceau au sol, aube.
Personnages : badaud rond au chapeau haut à cocarde ; badaud maigre à la canne, habit râpé.
Accessoires : canne, chapeaux à cocarde.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 3 — image clé (FIXE)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : dans la nacelle, Garnerin, la main sur la corde de largage, regarde le ballon mâchoire serrée ; son aide, au rebord, le supplie ; le paquet de soie plié à leurs pieds. (Réécrit le 23 août 2026 : l'action doit porter la réplique « Lâchez tout » ; la soie tenue à la main se lisait comme une couverture.)
Cadrage : plan moyen à deux, de côté, Garnerin à gauche et l'aide à droite, les deux visages visibles (un locuteur par clip exige les deux visages).
Décor : D1 · Parc Monceau au sol, aube.
Personnages : Garnerin, aéronaute au visage résolu, redingote sombre du Directoire, cheveux noués, foulard clair au cou ; aide en veste rude, manches retroussées.
Accessoires : corde de largage tendue, paquet de soie plié au sol, cordages, couteau glissé au flanc de la nacelle.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 4a — image de départ

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : le ballon quitte le sol avec sa nacelle, la foule bascule en arrière pour le suivre des yeux.
Cadrage : grand ensemble au ras de la foule, dos des badauds au premier plan.
Décor : D1 · Parc Monceau au sol, aube.
Personnages : figuration, foule du parc Monceau ; Garnerin, aéronaute au visage résolu, redingote sombre du Directoire, cheveux noués, foulard clair au cou, minuscule dans la nacelle.
Accessoires : ballon, nacelle, cordages largués.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 4a — mouvement (10 s)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

PLAN 1 (0.0 à 3.0s) : le ballon s'arrache du sol, les cordages largués retombent.
COUPE NETTE
PLAN 2 (3.0 à 6.0s) : plan rapproché sur la foule qui bascule en arrière, chapeaux tenus à deux mains.
COUPE NETTE
PLAN 3 (6.0 à 10.0s) : ensemble en vue basse, le ballon monte et rapetisse au dessus des arbres.

Cadence d'animation limitée, autour de 10 images par seconde.
Les personnages gesticulent et réagissent, ils ne parlent pas.
Mouvement dès la première image, aucun démarrage figé.
NÉGATIF : rendu photoréaliste, texture de peau, dégradés lisses, mouvement de caméra fluide et continu.
```

### Plan 4b — image de départ (continuité : dernière image du bloc 4a)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : vus depuis la nacelle, les toits de Paris rapetissent, la foule du parc devient une tache sombre.
Cadrage : très grand ensemble en plongée, bord de nacelle au premier plan.
Décor : D2 · Ciel de Paris.
Personnages : la main gantée de Garnerin sur le bord d'osier.
Accessoires : bord de nacelle, cordage, paquet de soie.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 4b — mouvement (10 s)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

PLAN 1 (0.0 à 3.5s) : les toits glissent lentement sous la nacelle, fumées de cheminées qui filent.
COUPE NETTE
PLAN 2 (3.5 à 7.0s) : plan rapproché sur le bord d'osier qui vibre au vent, la main gantée se crispe.
COUPE NETTE
PLAN 3 (7.0 à 10.0s) : très grand ensemble, la ville entière sous la brume, la tache sombre de la foule au centre du parc.

Cadence d'animation limitée, autour de 10 images par seconde.
Les personnages gesticulent et réagissent, ils ne parlent pas.
Mouvement dès la première image, aucun démarrage figé.
NÉGATIF : rendu photoréaliste, texture de peau, dégradés lisses, mouvement de caméra fluide et continu.
```

### Plan 5 — image de départ

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

Scène : très gros plan sur une lame posée contre la corde tendue qui retient la nacelle au ballon.
Cadrage : très gros plan, angle rasant sur la corde.
Décor : D2 · Ciel de Paris.
Personnages : la main de Garnerin serrée sur le manche du couteau.
Accessoires : couteau, corde tendue, cordages du ballon.

Les personnages gesticulent et réagissent, ils ne parlent pas.
```

### Plan 5 — mouvement (8 s)

```
Trait de contour net, sombre, d'épaisseur constante, fermé sur chaque forme ; aplats francs, sans texture ni grain ; palette saturée et chaude : bois miel, ocre doré, rouge brique, vert olive, crème, lumière ambrée ; trois teintes réservées aux personnages : sable, bleu sarcelle, orange vif ; fonds simplifiés en volumes géométriques, moins détaillés que les personnages ; une seule valeur d'ombre posée en aplat, sans dégradé ; poses dynamiques et gestes amples, jamais figés ; aucun rendu photographique ni volumétrique ; dessin animé 2D, format 16:9. L'ensemble est désaturé : tons terreux — brun terre, gris pierre, beige poussière —, contrastes adoucis, lumière grise, costumes et décors exacts.

PLAN 1 (0.0 à 2.5s) : la main saisit le couteau glissé au flanc de la nacelle.
COUPE NETTE
PLAN 2 (2.5 à 5.5s) : angle rasant, la lame scie la corde, des fibres sautent une à une.
COUPE NETTE
PLAN 3 (5.5 à 8.0s) : très gros plan frontal, la corde cède d'un coup, les brins fouettent l'air.

Cadence d'animation limitée, autour de 10 images par seconde.
Les personnages gesticulent et réagissent, ils ne parlent pas.
Mouvement dès la première image, aucun démarrage figé.
NÉGATIF : rendu photoréaliste, texture de peau, dégradés lisses, mouvement de caméra fluide et continu.
```

### Plan 6 — POST (aucune génération)

```
Source : dernière image du bloc du plan 5.
Traitement : figement de l'image ; incrustation du carton titre « LES DÉCOUVREURS — Nos ancêtres les Chinois » en typographie de la série ; la voix off du plan se cale au montage.
```

---

## 6. Alertes

* **Arbitrage du plan 8 rendu le 22 août 2026** : la réplique devient « ...regardez ma sacoche : de la glace ! ». Les plans 8a et 8b sont débloqués.
* **Durées révisées et mouvements de caméra complétés le 22 août 2026**, voir les notes en tête de document.
* **Section 5 périmée** : gabarit de mouvement remplacé, voir `PIPELINE-video-et-voix.md`.

* **Plan 1 repassé en ANIMÉ** (blocs 1a et 1b de 9 s) : première image de la série, un panoramique sur image fixe y annoncerait un diaporama. **Compensation : le plan 47 est basculé en FIXE** (2 images, zoom avant lent) — ses blocs de 7 s étaient déjà sous la fourchette, et le plan décrit un état final, la captivité, plus qu'une action ; la fermeture de la porte se lit très bien en deux images. Ratio final : 476 s soit 38,9 pour cent.
* **Plan 26 : arbitrage à valider sur le pilote.** Un attelage censé tirer, figé avec un simple travelling, risque de se voir. Laissé en FIXE ; à tester en priorité, et à repasser en ANIMÉ (2 blocs de 9 s) si le rendu trahit l'immobilité.
* Plans 8 et 56 (14 s) : découpés en blocs de 7 s, sous la fourchette de 8 à 10 s, pour ne pas toucher aux durées verrouillées. Même raison pour les blocs de 6 s (32c, 49c, 54c).
* Plan 9 : la description d'origine énumérait les neuf objets ; la liste complète est portée par le bloc 9b pour garder chaque bloc générable. Aucun objet retiré.
* Plans 23, 29, 34, 37, 63, 64, 67, 69 (retours d'objets) : les retours d'objets dans la sacoche sont des inserts du registre CADRE. Générer **une seule image FIXE d'insert « main et sacoche »** avec objet interchangeable, réutilisée à chaque occurrence ; pour les plans d'époque concernés (29, 63), l'insert s'ajoute au montage, il ne se génère pas dans la scène.
* Plan 63 : mélange registre ÉPOQUE (badauds) et insert CADRE — voir point précédent ; le plan lui même reste ÉPOQUE.
* Plans 12, 16, 19, 35, 65, 68 basculés en FIXE : ce sont des montages, donc plusieurs images fixes enchaînées (une génération par vignette), comptées dans le diagnostic.
* Plan 25 : le portrait d'Elio en couleurs pour l'incrustation des gels se génère une fois et se réutilise pour les plans 15, 25, 27, 34 et 52.
* Plan 74 : la description d'origine employait un mot banni des prompts ; reformulée en « petit cerf volant de fête ». Le texte dit est inchangé.
* Plan 79 : le fondu final est au montage ; le plan reste un rendu ANIMÉ de 10 s.
* Ratio ANIMÉ final : 38,6 pour cent, sous la cible de 40 ; aucune réplique, date, durée ou numérotation modifiée.
