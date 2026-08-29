# Codex Novelcrafter — S01E01

**25 août 2026.** Ce fichier **ne s'importe pas**. Novelcrafter n'importe qu'un manuscrit ; le Codex se saisit à la main, une entrée à la fois. Chaque bloc ci dessous est prêt à coller : le **Nom** va dans le champ de nom, les **Alias** dans le champ d'alias, et le corps dans la description.

Tout vient de la bible de plateau de `../scenario.md`, section « Bible de plateau — la géographie permanente ». **Cette bible reste la source ; ce fichier en est une copie de commodité.** Si la bible change, ce fichier change avec elle.

**Pourquoi saisir le Codex.** Les alias déclenchent le suivi automatique : dès qu'une scène dit « Naya » ou « la sacoche », Novelcrafter attache l'entrée et la donne au modèle quand vous générez ou réécrivez. Sans Codex, chaque scène repart sans mémoire du plateau, et les erreurs de géographie reviennent.

**Ordre de saisie conseillé** : les trois lieux d'abord, puis les personnages, puis les objets, puis le savoir. Un lieu saisi avant les personnages permet de relier chaque personnage à son lieu par une relation.

---

# Lieux

## D3 — La pièce du cadre

**Type** : Location
**Alias** : la pièce, le cadre, la salle, la grande table, la table de bois miel

Décor du présent, 33 plans. Vue par son quatrième mur : caméra frontale, large, à hauteur de table, côté sud. **Personne ne s'assoit jamais dos à la caméra.** Gauche et droite s'entendent toujours à l'écran.

Géographie invariante :

* La grande table de bois miel occupe le centre, allongée dans le sens gauche droite. C'est sur elle que vivent les neuf objets.
* Sam est au côté nord de la table, face caméra, au centre. Debout à l'arrivée, assis ensuite. Sa sacoche est posée sur la table à sa gauche, donc à **droite de l'écran** : tout insert « objet rangé » va de la gauche vers la droite.
* Naya est assise à l'extrémité ouest, **gauche de l'écran**, de trois quarts droite, carnet devant elle, crayon en main droite.
* Elio est assis à l'extrémité est, **droite de l'écran**, de trois quarts gauche, tablette translucide devant lui ou levée en main droite.
* La porte est dans le mur ouest, **bord gauche du cadre**. Sam entre toujours par la gauche.
* La fenêtre est dans le mur est, **bord droit du cadre**. C'est par elle qu'on voit le cerf volant du soir au plan 79.
* Le grand écran mural occupe le fond **gauche**. Quand Sam pointe l'écran, il pointe vers la gauche.
* Les étagères d'objets de voyage occupent le fond **droit**. Théière et tasses vivent sur la table, côté Naya.

Registre : couleurs saturées, à l'inverse des récits d'époque.

## D1 — Le parc Monceau, octobre 1797

**Type** : Location
**Alias** : le parc, parc Monceau, l'allée, la pelouse, le ballon

Décor de l'épreuve publique. Plans 1 à 3, 4a, 60, 62, 63. Palette désaturée, aube brumeuse d'octobre.

* L'allée principale de gravier clair court du sud au nord ; la caméra générale est au **sud** et regarde vers le **nord**.
* Le ballon gonflé, rayures beige et bleu gris, se tient au centre d'une pelouse dans l'axe de l'allée, à une quarantaine de mètres, amarré à des piquets, cordes tendues. **Sa nacelle d'osier est posée dans l'herbe directement sous lui, attachée : il n'existe qu'une seule nacelle dans tout l'épisode.**
* Les fabriques néoclassiques et la colonnade ferment la perspective au nord ; bosquets d'arbres nus d'octobre à l'est et à l'ouest ; brume basse sur les pelouses.
* La foule, une douzaine de figurants Directoire, se tient sur l'allée entre la caméra et le ballon, **toujours dos à la caméra**, tournée vers le nord.
* Les deux badauds parieurs occupent le bord sud de la foule, au premier plan.

## D2 — La nacelle en vol

**Type** : Location
**Alias** : la nacelle, le panier, en vol, la corde de largage

Plans 3, 4b, 5, 60, 61. Rebord d'osier à hauteur de poitrine.

* La corde de largage monte du centre de la nacelle vers le ballon, hors cadre en haut.
* **Garnerin à gauche**, debout, main droite sur la corde au dessus de sa tête dans les plans d'attente. **L'aide à droite**, penché vers lui. Après le plan 3, l'aide n'est plus à bord.
* Le couteau est glissé dans le tressage du **flanc gauche** de la nacelle, côté Garnerin.
* Le paquet de soie plié est au plancher, entre les deux hommes, puis aux pieds de Garnerin.
* En vol, Paris est en bas et au fond ; le parc est la tache verte.

---

# Personnages

## Sam

**Type** : Character
**Alias** : Sam, le conteur, le voyageur

Le conteur de la série, savant du jour au sens large. Place fixe : côté nord de la table, face caméra, au centre.

Physique et costume, invariants sur les 79 plans : **sans barbe**, **aucune lunette nulle part** (ni portée, ni sur le front, ni tenue, ni dans la sacoche), chapeau à large bord, veste sable, sacoche patinée, **pansement du jour sur la main droite**.

Méthode : il s'autocorrige sur les dates, il perd le fil (« Où j'en étais, déjà ? »), et il tient un tic de vérification hérité du conteur d'origine : « Belle histoire. Rien ne le prouve : c'est une légende. Mais quelle légende ! »

Sa sacoche est son totem. Elle est posée sur la table à sa gauche, donc à droite de l'écran.

## Naya

**Type** : Character
**Alias** : Naya

Assise à l'extrémité ouest de la table, **gauche de l'écran**, de trois quarts droite. Boucles volumineuses, sweat **bleu sarcelle**, carnet devant elle, crayon en main droite.

Fonction dramatique : elle pose la question du jour et elle note. Sa page revient au plan 75.

## Elio

**Type** : Character
**Alias** : Elio

Assis à l'extrémité est de la table, **droite de l'écran**, de trois quarts gauche. Casquette **orange vif**, bandes contrastées, tablette translucide posée devant lui ou levée en main droite.

Fonction dramatique : le vérificateur. Il impose la règle du jeu au plan 15, et il **gèle** les embellissements du canon : la cervoise, le cheval étranglé, l'étrier et la chevalerie, les « cinq siècles » du pont, l'ambassadeur « en Chine », le miracle de l'imprimerie.

**Le gel d'Elio, dispositif visuel fixe** : Elio passe au premier plan **droit**, en couleurs saturées, tablette levée main droite ; tout le reste du cadre fige en gris désaturé. Le sujet gelé occupe le fond gauche et le centre.

## André Jacques Garnerin

**Type** : Character
**Alias** : Garnerin, le citoyen Garnerin

Parc Monceau, octobre 1797. Saute d'un ballon à hydrogène sous une voilure de soie. Place fixe dans la nacelle : **à gauche**, debout, main droite gantée sur la corde de largage.

Il tranche la corde au plan 5 ; le verdict est différé jusqu'au plan 62. Parle en « citoyen » et compte en francs.

## L'aide de Garnerin

**Type** : Character
**Alias** : l'aide

Plan 3 uniquement à bord. **À droite** dans la nacelle, penché vers Garnerin, main ouverte qui supplie. Après le plan 3, il n'est plus à bord.

## Le badaud rond

**Type** : Character
**Alias** : badaud rond, BADAUD 1, le rond

Bord sud de la foule, **à gauche** au premier plan. Chapeau haut à cocarde tricolore, gilet tendu sur le ventre. Il parie que Garnerin va se tuer. Mêmes place et costume aux plans 2 et 63.

## Le badaud maigre

**Type** : Character
**Alias** : badaud maigre, BADAUD 2, le maigre

Bord sud de la foule, **à droite** au premier plan. Canne en main droite, **manteau de laine écrue brune, non teinte, usée et rapiécée**, couleur de toile à sac et de poussière. Il parie dix francs que Garnerin ne coupe pas la corde. Mêmes place et costume aux plans 2 et 63.

**Note de fabrication** : la matière est prescrite, jamais la teinte. Nommer une couleur laisse revenir le sarcelle réservé de Naya.

---

# Objets

## La sacoche de Sam

**Type** : Item
**Alias** : la sacoche, sa sacoche

Le totem du personnage, patinée. Posée sur la table à la gauche de Sam, donc à **droite de l'écran**. Renversée au plan 9 : neuf objets en tombent, une seule origine annoncée.

Gag du plan 8 : elle est givrée à l'arrivée.

## Le jeu de la sacoche

**Type** : Lore
**Alias** : la règle du jeu, le jeu, les neuf objets

Règle posée par Elio au plan 15 : **chaque objet vérifié retourne dans la sacoche ; s'il en reste un à la fin, Sam a perdu.** La table qui se vide rythme tout l'épisode.

À chaque plan du cadre, la table doit montrer **exactement** les objets non encore rangés :

* petit soc de charrue, rangé au plan 23
* fer d'attelage miniature, rangé au plan 29
* allumette, rangée au plan 37
* carré de soie, rangé au plan 63
* cerf volant de poche, rangé au plan 63
* boussole, rangée au plan 64
* billet ancien, rangé au plan 67
* carte à jouer, rangée au plan 69
* pétard, rangé au plan 73

**Point ouvert, à arbitrer.** Au plan 34, la réplique verrouillée de Sam dit « je range... l'étrier dans la sacoche », mais l'étrier n'est pas l'un des neuf objets et le fer d'attelage est déjà rangé au plan 29. Le compte du plan 64, « Quatre objets », n'est juste que si le plan 34 ne range **rien** physiquement. Traitement retenu en attendant : au plan 34, aucun objet ne quitte la table, la phrase est rhétorique.

## Le couteau de la nacelle

**Type** : Item
**Alias** : le couteau, la lame

Glissé dans le tressage du **flanc gauche** de la nacelle, côté Garnerin. Tranche la corde de largage aux plans 5 et 60.

## Le paquet de soie

**Type** : Item
**Alias** : la soie, le paquet de soie, la voilure

Plié au plancher de la nacelle, entre les deux hommes au plan 3, puis aux pieds de Garnerin. S'ouvre en corolle au plan 61.

**Note de fabrication** : soie écrue crème, matière nommée, jamais une teinte libre.

---

# Savoir

## Les couleurs réservées

**Type** : Lore
**Alias** : couleurs réservées, sable, sarcelle, orange vif

Trois couleurs appartiennent à la troupe du présent et n'apparaissent sur **aucun** personnage d'époque ni **aucun** décor d'époque : le **sable** de la veste de Sam, le **sarcelle vif** du sweat de Naya, l'**orange vif** de la casquette d'Elio.

Les récits d'époque sont désaturés, le cadre est saturé, les enfants du cercle sont en couleurs vives sur fond désaturé.

## Les interdits permanents

**Type** : Lore
**Alias** : interdits, interdits permanents

Vrais sur les 79 plans :

* Sam n'a **aucune lunette nulle part** et **pas de barbe**.
* Le pansement est sur la main **droite** de Sam.
* Les couleurs réservées ne débordent jamais sur l'époque.
* Toute image clé de dialogue se génère **bouches fermées** ; seules les clés de champ contrechamp destinées à la synchro labiale montrent la bouche du locuteur ouverte.
* **Aucun texte dans l'image, jamais**, sauf le carton titre du plan 6 et la page de titre du plan 58, tous deux posés au montage.
* Il n'existe qu'**une seule nacelle** dans tout l'épisode.
* Aucun anachronisme de langage : paysans, badauds, pillards et soldats parlent une langue neutre et datée ; les scènes de 1797 disent « citoyen » et comptent en francs ; **personne ne prononce le mot parachute avant que Lenormand ne le forge à l'écran**.

## La chaîne narrative

**Type** : Lore
**Alias** : chaîne narrative, mais donc

Chaque étape est reliée à la suivante par « mais » ou par « donc », jamais par « et puis ». C'est le test de tenue du récit : une étape qui ne se relie que par « et puis » est une étape à couper.

Trois fils tiennent l'inventaire : l'épreuve publique en boucle, ouverte au plan 1 et refermée au plan 62 ; le jeu de la sacoche, qui vide la table ; la vérification comme dispositif, par les gels d'Elio et les autocorrections de Sam.

## Le tic de méthode

**Type** : Lore
**Alias** : belle histoire, c'est une légende

Formule de Sam, héritée du conteur d'origine, employée chaque fois qu'une source est belle mais non prouvée : « Belle histoire. Rien ne le prouve : c'est une légende. Mais quelle légende ! »

Elle sert notamment sur la légende de Shun, au plan 54.
