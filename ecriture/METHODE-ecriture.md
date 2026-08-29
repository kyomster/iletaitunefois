# Méthode d'écriture — d'une fiche épisode à un scénario exécutable, puis à un plan de production

Partie générique de la bible d'écriture et de fabrication (v5.1), séparée le 29 août 2026 de ce qui est propre aux *Découvreurs* (`iletaitunefois/serie/BIBLE-Les-Decouvreurs.md`). Avec ce document, la bible d'une série, sa fiche personnages et une fiche épisode, un scénariste — humain ou IA — produit le scénario au bon format, puis le plan de production, sans instruction supplémentaire. Le prompt maître qui enchaîne les deux étapes est `PROMPT-MAITRE.md`.

---

## 0. Hiérarchie des sources — LA règle avant toutes les autres

1. **La fiche épisode dit QUOI raconter.** Pour *Il était une fois*, c'est le corpus `iletaitunefois/fiches_verifie/` — la fiche vérifiée **et son audit** (`_audit/`), qui seul porte les sources ; on écrit sur l'état de l'audit à sa dernière passe, pas sur la fiche d'un jour antérieur (S01E01 a dû être révisé pour trois corrections du 7 août). Son « Découpage séquentiel » est la **colonne vertébrale du scénario** : toutes ses séquences doivent être couvertes, dans le même ordre, aux seules exceptions qu'impose le dispositif de la série. Un épisode qui traite douze sujets donne un scénario qui traite douze sujets. **Ne jamais réduire un épisode inventaire à un seul de ses fils.**
2. **La bible de la série dit COMMENT le raconter** : structure, dispositif, registres, toujours/jamais.
3. **Les corrections de la fiche épisode sont la matière première des scènes de vérification.** Tout ce qui figure entre crochets *[l'épisode dit : ...]*, dans « Faits énoncés », « Réserves sur la source » et « Ce que l'on sait depuis » doit être traité : joué à l'écran ou explicitement noté hors périmètre en tête de scénario.
4. **En cas de conflit entre les fiches, ne jamais trancher en silence** : signaler le conflit et proposer l'arbitrage.
5. **Le pipeline complet tient en deux étapes** : Étape A, l'écriture — fiche épisode + bible + fiche personnages donnent le **scénario** (points 5 à 7). Étape B, la fabrication — le scénario donne le **plan de production** en six sections (point 11). Aucun autre document n'est requis.
6. **Ne jamais reproduire les dialogues de l'épisode d'origine** quand la série adapte un corpus existant. Seuls les courts motifs déjà cités dans la fiche épisode (refrains, devise, morale) peuvent être repris tels quels ; tout le reste est réécrit dans l'esprit.

Deux règles d'écriture valent pour toute série et se vérifient par script (point 7) :

* **Chaîne mais/donc** : chaque étape du récit est reliée à la précédente par « mais » ou « donc », jamais par « et puis ». La chaîne est **explicitée et numérotée en tête de scénario**, avec renvoi aux numéros de plans.
* **Zéro anachronisme de langage** dans les scènes d'époque : pas de mot, d'unité, d'objet ou de notion postérieurs à la scène jouée (exemple canonique : personne ne prononce « parachute » avant que Lenormand ne forge le mot en 1785).

---

## 5. Calibrage chiffré (mesuré sur le corpus — à respecter, pas à estimer)

| Paramètre | Valeur cible | Note |
|---|---|---|
| Durée utile hors générique | **20 à 22 min** (1 200 à 1 320 s) | Somme exacte des durées de plans, calculée |
| Nombre de plans | **70 à 95** | Durée moyenne 12 à 18 s ; plans muets jusqu'à 30 s |
| Débit de parole | **85 à 95 mots par minute** sur la durée totale | ~1 800 à 2 100 mots prononcés pour 20 min : une série de voix off et de silences, pas de bavardage |
| Séquences muettes ou en voix off seule | **8 à 12 min** | Écrites comme des scènes, pas comme des transitions ; découpables en capsules verticales de 60 à 90 s |
| Répartition | Cadre ~4 à 5 min, récit ~15 à 17 min | Le récit a ses décors, ses figurants et ses dialogues joués |
| Part de la voix off du conteur | De l'ordre des deux tiers des répliques | Fidèle au déséquilibre du corpus d'origine |

Les seuils propres à une série (objection avant 3:00, nombre de gels…) sont dans sa bible.

---

## 5 bis. Contraintes de fabrication — à respecter dès l'écriture

Le scénario doit sortir directement exécutable par la chaîne de génération. Ces règles s'appliquent au moment d'écrire le tableau de plans, pas après coup.

**Trois types de plans** :
* **FIXE** : une image clé générée ; peut porter un **mouvement de caméra de montage** (panoramique lent, zoom avant lent, zoom arrière lent, travelling latéral — préciser le sens) ; un plan de montage basculé en FIXE peut enchaîner plusieurs images fixes (une génération par vignette).
* **ANIMÉ** : un rendu vidéo. **Dix secondes maximum par bloc** : tout plan ANIMÉ plus long est découpé dès l'écriture en blocs a, b, c de 8 à 10 secondes, chacun avec sa propre description, chaque bloc démarrant sur la dernière image du précédent ; le texte dit reste attaché au plan entier et se cale au montage.
* **POST** : effet fabriqué au montage, jamais généré — désaturation, figement, surimpression, fondu, carton de titre ou de texte, raccord exact réutilisant un fichier déjà rendu. Chaque plan POST indique sa source (image ou clip à générer, ou fichier réutilisé) et le traitement à appliquer.

**Ratio économique** : **40 pour cent maximum de la durée totale en ANIMÉ**, mesuré au script. Réserver l'ANIMÉ aux plans dont le mouvement fait le sens : une lame qui tranche, une voilure qui s'ouvre, un vol, une chute, une course, une crue, un gag dont la chute est un mouvement, un plan muet porté par l'image. Écrire en FIXE avec mouvement de caméra : les réactions et contemplations sans déplacement, les inserts et détails d'objets, les montages de vignettes, les états et décors d'établissement.

**Registre par plan** : CADRE, ÉPOQUE ou MIXTE (gels, surimpressions, cartons). Le registre détermine laquelle des formules de style de la fiche personnages s'applique, octet pour octet.

**Écriture des descriptions visuelles** : chaque plan référence un décor nommé et des personnages nommés ; varier tailles et angles ; ne pas rouvrir chaque séquence sur le même plan large ; ne jamais mélanger deux registres dans un même plan (un insert du cadre au milieu d'une saynète d'époque se fabrique au montage et se signale) ; **mots bannis partout** : « enfant », « kid », « childlike », mentions d'âge (remplacer par la stature et les proportions) ; aucun nom de studio, de marque ou d'œuvre existante.

**La chaîne physique de chaque scène et qui fait quoi** s'écrivent avant le découpage (guide de préparation §1) : où est chacun, ce qui relie quoi à quoi, à qui s'adresse chaque ordre. Une action dont l'objet n'est pas nommé ne se dessine pas ; une scène dont la chaîne physique n'est pas écrite se contredit d'un plan à l'autre.

**Inventaire des éléments de continuité** : tout élément qui doit être **identique d'un plan à l'autre** — objet manipulé, véhicule, machine, animal, vêtement remarquable — se relève au moment d'écrire le tableau de plans, se liste dans le roster avec ses plans, **et reçoit une planche de référence** réinjectée sur chacun de ces plans, exactement comme un décor ou un personnage. Une description recopiée ne tient pas la continuité : seule une image réinjectée la tient (RÈGLE 36 de la méthode d'images). Un élément listé en continuité sans planche est un défaut de préparation, pas un détail de fabrication.

**Règle du livrable complet** : quand un protocole aval liste des sections de sortie (diagnostic, formules, roster, tableau, prompts, alertes...), le document rendu les contient **toutes, rédigées**. Un renvoi vers une autre fiche ne vaut pas livrable ; toute section reportée est une décision explicite, consignée en ALERTES, jamais silencieuse.

**Compte des générations** : la chaîne est image vers vidéo. **Chaque bloc ANIMÉ consomme une image de départ** générée avec le même mécanisme de cohérence. Total d'images clés = plans FIXE + vignettes des montages + sources POST + une image de départ par bloc ANIMÉ.

**Plan d'ouverture** : le tout premier plan de l'épisode est toujours ANIMÉ. Jamais un mouvement de caméra sur image fixe en ouverture : il annoncerait un diaporama.

**Livraison par étapes** : tout livrable de prompts commence par la première séquence seulement (pilote de format), soumise à validation avant de produire le reste.

**Zone verrouillée pour l'étape de production** : le texte dit (mot pour mot, ponctuation comprise), la chaîne mais/donc, les faits vérifiés, les gags, la durée totale et le minutage, l'ordre et la numérotation des plans, les fiches personnages. Toute contrainte technique qui exigerait d'y toucher se signale en ALERTES et se laisse à l'arbitrage humain : le scénario gagne toujours.

**Sur les plans de dialogue**, depuis le pilote : la voix et la bouche sont générées **dans le même rendu** que l'image (moteur omni-modal, `atelier/STRATEGIE-video.md`). Le scénario écrit donc chaque réplique pour être **citée mot pour mot dans le prompt vidéo** ; une réplique qui ne tient pas en huit à dix secondes de clip se coupe dès l'écriture.

---

## 6. Format de sortie obligatoire du scénario

Un fichier Markdown contenant, dans cet ordre :

1. **Titre et paramètres** (durée calculée, format).
2. **Parti pris** : gabarit choisi et pourquoi, liants retenus, tout conflit de sources signalé.
3. **Corrections du canon appliquées** : liste des corrections de la fiche épisode et où chacune est jouée ; celles laissées hors périmètre, avec raison.
4. **Chaîne narrative** numérotée en mais/donc avec renvois aux plans.
5. **Légende** FIXE/ANIMÉ et rappel des identifiants personnages.
6. **Le tableau de plans**, un seul tableau, une ligne par plan (et par bloc pour les plans ANIMÉ découpés), huit colonnes exactement : **N° | Bloc | Durée (s) | Registre | Type | Description visuelle (une phrase) | Mouvement caméra | Texte dit** (locuteur en capitales, « — (muet, musique) » pour les plans muets, texte porté par le plan entier et non par ses blocs). Type = FIXE, ANIMÉ ou POST ; Registre = CADRE, ÉPOQUE ou MIXTE ; la colonne Bloc reste vide hors découpage ; la colonne Mouvement caméra porte le mouvement de montage des plans FIXE concernés et la source des plans POST.
7. **Minutage récapitulatif** par séquence (plans, timecodes calculés, chapitre du découpage source correspondant), total exact, et **liste des gags**.

---

## 7. Vérifications obligatoires avant livraison (par script, jamais à l'estime)

* Somme exacte des durées et recalcul des timecodes du récapitulatif.
* Décompte des mots prononcés et débit en mots/min, comparé à la cible 85 à 95.
* Part du muet et de la voix off seule (cible 8 à 12 min).
* Zéro « et puis » entre les étapes ; chaîne mais/donc complète.
* Les seuils de la bible de la série (objection avant 3:00…).
* Liste de contrôle : chaque séquence du découpage source est couverte ; chaque correction entre crochets est traitée ou déclarée hors périmètre.
* Aucun dialogue repris verbatim de l'épisode d'origine (hors motifs autorisés).
* Ratio ANIMÉ inférieur ou égal à 40 pour cent de la durée totale.
* Aucun bloc ANIMÉ au delà de 10 secondes ; la somme des blocs égale la durée du plan.
* Chaque plan POST indique sa source et son traitement ; chaque plan FIXE basculé porte son mouvement de caméra.
* Mots bannis absents des descriptions ; aucun nom de marque, de studio ou d'œuvre.
* Toutes les sections exigées par le protocole aval sont présentes et rédigées dans le livrable (aucun renvoi).
* Le compte d'images inclut une image de départ par bloc ANIMÉ.
* Le premier plan de l'épisode est ANIMÉ.

---

## 11. Du scénario au plan de production

Rôle : directeur technique de production. **On convertit, on ne réécrit pas** : la zone verrouillée du point 5 bis s'applique intégralement. Règle de dernier recours : en cas de conflit entre le scénario et une contrainte technique, **le scénario gagne** ; le conflit se signale en ALERTES et l'humain tranche.

### Le livrable — six sections, dans cet ordre, toutes rédigées

1. **Diagnostic.** Ratio ANIMÉ avant et après correction ; plans basculés ; plans découpés et blocs résultants ; plans reclassés POST ; nombre de générations vidéo (**une par bloc ANIMÉ**) et d'images clés (**plans FIXE + vignettes des montages basculés + sources POST + une image de départ par bloc ANIMÉ**) ; estimation de coût.
2. **Les formules de style**, recopiées **dans le livrable même**, octet pour octet — un renvoi ne vaut pas livrable. Depuis la bibliothèque de styles, c'est le `style.json` du style retenu.
3. **Le roster d'assets** : quatre listes sans doublon, déduites des descriptions visuelles. Personnages récurrents avec les vues nécessaires ; personnages d'époque avec le nombre de plans où chacun apparaît (**fiche à partir de trois plans** ; en deçà, génération à la volée — mais toute paire ou tout personnage à continuité garde sa référence le temps de ses plans) ; décors avec la liste des plans rattachés (**signaler plus de deux plans consécutifs sur le même décor**) ; accessoires avec les objets de continuité, **chacun assorti de sa description canonique complète, de sa planche de référence et de la liste des plans où il se réinjecte** — un nom commun n'est pas une description : nom, forme, structure, matière, couleurs nommées en positif, échelle par rapport au corps humain, et ce que l'objet n'a pas (RÈGLES 38 et 42). Chaque personnage à fiche reçoit sa **phrase figée**, copiée telle quelle dans les prompts.
4. **Le tableau révisé** à huit colonnes (point 6), après application des quatre corrections : rééquilibrage sous 40 pour cent selon les critères du point 5 bis ; découpage de tout ANIMÉ en blocs de 10 s maximum avec description propre et continuité ; reclassement POST avec source et traitement ; mouvement de caméra sur chaque FIXE basculé.
5. **Les prompts** — livrés par étapes : **la première séquence seule d'abord** (pilote de format), le reste après validation humaine. Un prompt d'image par plan et par bloc ; un prompt de mouvement par bloc ANIMÉ. Les gabarits exécutables sont ceux de l'atelier : `assembler_prompts.py` (image clé : Scene / Framing / Decor / Characters / Props, blocs identité substitués, clauses, `Avoid:`) et `assembler_clips.py` (mouvement : une seule action continue, caméra nommée, présence, garde des objets, répliques citées). Contraintes sur tous les prompts : sept références d'image maximum par appel, dans l'ordre décor, personnages, accessoires ; varier taille et angle à chaque coupe interne ; le plan par dessus l'épaule exige un personnage nommé visible au premier plan et reste interdit sur un plan d'objet ou de décor vide ; ne pas rouvrir chaque séquence sur le même plan large ; mots bannis et interdiction des noms de studio, marque ou œuvre.
6. **Alertes.** Tout ce qui a été repéré et volontairement laissé en l'état parce que le corriger toucherait la zone verrouillée — un point par ligne, avec numéro de plan et raison. Y consigner aussi toute section reportée, tout arbitrage à valider sur le pilote, et toute mutualisation d'assets décidée (portraits de gel, inserts réutilisables).

### Vérifications avant de rendre le plan de production

En plus de celles du point 7 : texte dit intact à la ponctuation près ; durée totale et minutage inchangés ; chaque bloc ANIMÉ de 10 s ou moins et somme des blocs égale à la durée du plan ; ratio ANIMÉ sous 40 pour cent ; premier plan ANIMÉ ; chaque FIXE basculé avec son mouvement ; chaque POST avec sa source ; chaque plan référençant un décor et des personnages du roster ; formules identiques octet pour octet dans tous les prompts d'un même registre ; aucun mot banni, aucune marque ; **les six sections présentes et rédigées**. Si une case ne peut pas être cochée : corriger d'abord, ne pas rendre.

Ensuite, avant la première image : `atelier/GUIDE-preparation-episode.md`.
