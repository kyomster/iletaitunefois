# Comparatif des styles — comment P a été choisi, et ce que valent les autres

Consolidé le 27 août 2026 à partir des audits d'épreuve (22 et 23 août), de la shortlist (25 août), des six montages de pilote et des retours de Guillaume. Les documents chronologiques d'origine sont dans l'historique git ; celui-ci ne garde que ce qui compte encore.

---

## 1. Le parcours, en quatre paliers

| Date | Palier | Ce qui a été jugé | Résultat |
|---|---|---|---|
| 8 → 22 août | **A, B, C** : bible complète (132 images de troupe), 46 décors et 12 personnages par style, pilote de 54 clés et 48 clips Wan 2.2 | l'exécution complète d'une chaîne | C retiré le 22 août ; A et B en course |
| 23 août | **D, E, F, G, H, I** puis **J, K** : épreuve à sec sur trois plans | l'identité d'un rendu | classement G, I, D, E, H, F ; puis K, G, J, I, D |
| 24 août | **A, B, D, J, K** : pilote complet en LTX-2.5 voix libres, cinq montages de 62,8 s | la tenue en mouvement | aucun ne s'impose |
| 25 → 27 août | **Db, L, M, N, O, P** : épreuve « modernité » puis shortlist **A, O, P** ; pilote P complet et corrigé | la modernité sans texture de support | **P retenu le 27 août** |

---

## 2. Ce que chaque palier a appris sur la manière de comparer

**Un pilote complet ne compare pas des styles, il compare des chaînes.** Les 48 clips A/B/C ont surtout appris à faire tenir Wan 2.2, puis à le remplacer. Le style était secondaire.

**Une épreuve à sec compare des identités, pas des images.** Sans référence réinjectée, les trois images d'épreuve ne raccordent pas avec un pilote ; elles disent seulement si le style existe et s'il tient sa charte. Deux règles de méthode en sont sorties (RÈGLES 32 et 33) et un préjugé est tombé : **la forme ne fait pas le registre** — un personnage rond en contre-jour dur porte le drame, un personnage anguleux éclairé à plat ne fait pas sérieux. Ce qui détermine le registre, ce sont la lumière, le cadrage et la palette.

**L'image fixe sélectionne des qualités qui ne survivent pas au mouvement.** H (trames), I (grain de papier), L (touche de pinceau) se définissent par une texture de support ; en animation, ce qui appartient au support grouille d'une image à l'autre. D'où le contrôle ajouté le 24 août — *ce style porte-t-il une texture qui grouillera en mouvement ?* — et les quatre styles conçus sans aucune texture : M, N, O, P.

**Le choix final se fait sur le montage.** Le défaut du ballon qui change de couleur, le visage noirci des figurants, l'aide qui décolle avec Garnerin : aucun ne se voit sur une image d'épreuve, tous se voient sur soixante secondes de film. C'est ce qui a fait écrire le §1 du guide de préparation — la chaîne physique et les rôles avant tout découpage.

---

## 3. Pourquoi P

La shortlist du 25 août mettait A, O et P côte à côte sur les trois plans d'épreuve. Trois faits ont décidé :

1. **P donne la lisibilité de A avec la profondeur de O.** A est irréprochable sur la grille et plat à l'écran — sur le plan 4b-1, qui doit donner le vertige, il ne le donne pas. O a la profondeur mais deux dérives (l'heure écrasée par la lumière, les couleurs réservées sur les fanions). P est le seul dont les trois images étaient utilisables en l'état.
2. **P est natif animation, conçu pour la production de masse en animation limitée** — exactement la contrainte de 79 plans et 300 rendus par épisode — et ne porte aucune texture de support.
3. **La troupe s'y transpose sans redessin.** Sam, Naya et Elio sont construits en grandes formes lisibles et couleurs franches, ce qui est la grammaire même de cet idiome. D, I, J et K imposaient un redessin complet des 40 assets de bible.

Ce que P a coûté à mettre au point, entre le 25 et le 27 août : la RÈGLE 37 (visages noircis sur un style à aplats), la RÈGLE 33 élargie (ornements dorés sur les bannières), la RÈGLE 15 durcie (fond neutre en ciel dégradé), et les planches d'objets de continuité (ballon, nacelle, parachute). Tout est dans `P-anime-tv-moderne/STYLE.md` et dans les RÈGLES 36 à 42 de la méthode.

---

## 4. Ce que valent les autres, si une autre série les appelle

* **K** est le premier choix pour une série au registre adulte et sobre qui reste de l'animation : distinguable de G et de J, troupe redessinable. Deux contraintes connues : la foule pose au lieu de regarder (à durcir en positif), et un plan sans personnage penche vers le jeu vidéo.
* **G** est le premier choix pour une série chaleureuse et familiale : la seule épreuve qui a rendu le décor juste du premier coup, et une troupe ronde s'y transpose sans effort. Lui donner un traitement TENSION avant les plans dramatiques.
* **J** est la meilleure image de toutes, et l'abandon de l'animation : casting au lieu de bible, aucun LoRA à entraîner, la moitié des règles sans objet. À réserver à un projet qui assume la prise de vue réelle générée.
* **I** sert un ton documentaire et le registre CADRE (la table, les objets) ; **E** une identité graphique forte au prix de l'expression ; **H** un public de 12 à 20 ans au prix d'un recalibrage de palette.
* **A** et **B** restent des chaînes complètes et validées, avec une troupe entière ; elles ont servi à apprendre les 42 règles. **C** est un résultat négatif documenté (RÈGLE 15).
* **Db, L, M, N, O** n'ont que leur épreuve ; O est le plus prometteur des cinq et n'a jamais été vu en mouvement.

---

## 5. Les trois plans d'épreuve, et pourquoi ceux-là

`P02` — un dialogue à deux au sol, foule derrière : teste les visages nommés, la foule sans visage, les couleurs réservées, les bouches fermées. `P1a-3` — une contre-plongée vers le sommet du ballon, bannières : teste le cadrage extrême (RÈGLE 32) et le lettrage (RÈGLE 33). `P4b-1` — une plongée sur les toits de Paris depuis la nacelle : teste la profondeur, le vertige et l'anachronisme urbain.

Pour une autre série, garder la même logique : un plan à deux visages, un cadrage extrême, un plan de profondeur. Trois images, six crédits, et l'on sait si le style existe.
