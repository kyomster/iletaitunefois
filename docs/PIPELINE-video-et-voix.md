# Pipeline vidéo et voix — S01E01

**22 août 2026.** Ce document convertit le plan de production en chaîne de fabrication réelle : rendu vidéo hors de Higgsfield, voix par ElevenLabs. Il ne remplace pas `S01E01-plan-de-production.md`, il en refait le diagnostic technique et ajoute ce que ce dernier ne couvrait pas : le son, le montage, et le choix du fournisseur de rendu.

**Rien n'est lancé.** Tout ce qui suit est un plan à valider.

---

# 1. Ce que change le passage à ComfyUI

Le plan de production a été écrit pour un moteur qui **produit des coupes à l'intérieur d'un même rendu**. Ses prompts de mouvement disent :

```
PLAN 1 (0.0 à 2.5s) : la brume glisse sur les pelouses...
COUPE NETTE
PLAN 2 (2.5 à 5.0s) : plan moyen sur le ballon qui oscille...
```

Un modèle image vers vidéo classique ne fait pas cela. Il produit **un plan continu**, du premier au dernier frame. La coupe nette doit donc sortir du prompt et devenir une frontière entre deux rendus.

Conséquence : **chaque coupe interne devient un clip autonome, avec sa propre image de départ.** C'est plus de générations, mais c'est aussi une chaîne plus sûre, parce que chaque clip part d'une image validée à l'œil et ne peut pas dériver plus de deux ou trois secondes.

Une exception possible existe, traitée au point 4 : LTX 2.5 revendique la génération multi plans avec continuité à travers les coupes. Si cela tient sur le pilote, les prompts actuels redeviennent utilisables tels quels. À tester, pas à supposer.

---

# 2. Les chiffres recalculés

Comptés par script sur le tableau révisé après la révision des durées du 22 août 2026, 109 lignes, 79 plans.

| | Lignes | Durée | Part |
|---|---|---|---|
| ANIMÉ | 54 blocs | 476 s | 36,7 % |
| FIXE | 47 plans | 718 s | 55,4 % |
| POST | 8 plans | 102 s | 7,9 % |
| **Total** | | **1 296 s** | **21 min 36** |

Durées révisées le 22 août 2026 : 22 plans n'avaient pas la place de dire leur texte à 150 mots par minute, ils ont été allongés, aucun plan muet n'a été amputé. Les 36 plans FIXE sans mouvement de caméra ont reçu le leur. Le volume vidéo est inchangé, seul le temps de parole augmente.

Les 54 blocs ANIMÉ font tous de 6 à 10 s. Le volume ANIMÉ est resté à 476 s : le plan 8 a gagné 4 s, le plan 9 en a rendu 4.

## Nombre de clips selon la longueur de coupe

| Coupe visée | Clips | Images de départ |
|---|---|---|
| 2,0 s | 237 | 237 |
| **2,5 s** | **189** | **189** |
| 3,0 s | 155 | 155 |

**Retenu : 2,5 s.** C'est la valeur qui colle au découpage déjà écrit dans le pilote, où les cinq blocs contiennent 16 coupes, soit 3,2 coupes par bloc et une moyenne de 2,9 s. C'est aussi la longueur où un modèle image vers vidéo dérive le moins.

## Total des images clés, chaîne ComfyUI

| Poste | Nombre |
|---|---|
| Images de départ des clips | 189 |
| Plans FIXE | 47 |
| Vignettes supplémentaires des montages | 11 |
| Sources des plans POST | 6 |
| **Total par style** | **253** |

À comparer aux 118 du plan de production d'origine. Le poste image double, le poste vidéo passe de 54 rendus longs à 189 clips courts.

---

# 3. Le partage image et vidéo

**Les images clés restent chez Higgsfield, sur Nano Banana Pro.** Ce n'est pas une préférence, c'est une contrainte de continuité : les 319 assets validés ont été produits par ce moteur, avec les blocs de style verrouillés. Changer de moteur d'image casserait la cohérence avec la bible, les décors et les fiches personnages. Réglages inchangés : `nano_banana_pro`, 16:9, 2K, une image par requête, 2 crédits l'image, négatives en fin de prompt après `Avoid:`.

**Seul le rendu vidéo change de maison.** C'est le seul poste où Higgsfield n'apporte rien d'irremplaçable, et le seul où le coût explose à l'échelle de l'épisode.

---

# 4. Évaluation des fournisseurs de rendu vidéo

Base de comparaison : **476 s de vidéo à produire**, majorées d'un facteur de reprise de 1,6, soit **762 s facturées** pour l'épisode dans un seul style. Aucun modèle n'a besoin de générer du son : la voix vient d'ElevenLabs, la musique et les effets se posent au montage. Désactiver l'audio natif partout où c'est une option.

## 4.1 Les modèles à poids ouverts, chez soi sur RunPod

| Modèle | Poids | VRAM | Licence | Notes |
|---|---|---|---|---|
| **Wan 2.2 I2V A14B** | ouverts | 25 Go en FP8 pour 480p, 40 Go pour 720p | Apache 2.0 | La référence. Variante **FLF2V** native dans ComfyUI, qui prend une première et une dernière image. LoRA d'accélération LightX2V qui descend à 4 étapes. |
| Wan 2.2 TI2V 5B | ouverts | 8 à 12 Go | Apache 2.0 | Tourne partout, qualité en dessous. Utile comme brouillon de cadrage. |
| **LTX 2.5** | ouverts | 32 Go en FP8, 80 Go conseillés | licence LTX, gratuite sous 10 M$ de revenus | Intégration ComfyUI de première main, **séquences multi plans avec continuité à travers les coupes**, conditionnement IC LoRA par profondeur, pose, contours. |
| HunyuanVideo 1.5 | ouverts | 80 Go et plus | licence Tencent, restrictions commerciales | Écarté, licence et VRAM. |
| CogVideoX 1.5 | ouverts | 40 Go et plus | Apache 2.0 | Écarté, qualité en retrait sur les plans complexes. |

**Wan 2.5, 2.6 et 2.7 ne sont pas à poids ouverts.** Wan 2.5 n'a jamais été publié, Wan 2.6 est sorti en API commerciale en décembre 2025, Wan 2.7 de même. Localement, Wan 2.2 est le dernier maillon ouvert de la famille.

Trois raisons de préférer le local pour cette série précisément :

1. **Le style est le sujet.** Un aplat cel à contour noir constant est exactement ce que les modèles fermés « embellissent » : ils ajoutent du volume, du grain, de la lumière rasante. En local on verrouille avec un LoRA de style entraîné sur les 319 images déjà validées. Aucune API ne permet cela.
2. **La cadence limitée à 10 images par seconde** est une consigne de la série. En local, on rend à 16 im/s et on décime au montage, ou on le fait dans le graphe. En API, on subit la cadence du fournisseur.
3. **Le coût marginal d'une reprise est du temps GPU, pas de l'argent par seconde.** Sur un épisode où l'on va refaire beaucoup de plans, c'est structurant.

### Configuration RunPod visée

| Poste | Choix | Prix indicatif |
|---|---|---|
| GPU | **L40S 48 Go** ou RTX 6000 Ada 48 Go | 0,79 à 0,99 $/h |
| Repli économique | RTX 5090 32 Go | 0,69 $/h |
| Brouillons | RTX 4090 24 Go | 0,34 à 0,74 $/h |
| Volume réseau | 100 Go pour modèles et sorties | environ 7 $/mois |
| Mode | **Pod persistant** pour la mise au point, **serverless** ensuite via `runpod-workers/worker-comfyui` | serverless L40S environ 1,75 $/h |

Le 48 Go est le bon palier : il fait tourner le 14B en 720p sans quantifier. En dessous, on quantifie et on perd un peu de tenue de trait, ce qui est précisément ce qu'on ne veut pas perdre ici.

**Temps de rendu attendu**, avec le LoRA LightX2V à 4 étapes et CFG 1 : de l'ordre d'une minute pour 56 images en 480p sur une 4090. En 720p sur L40S, compter deux à trois minutes par clip de 2,5 s. Pour 189 clips majorés à 300 rendus, cela fait **12 à 15 heures de GPU**, soit **12 à 15 $**. Avec la mise au point du graphe, les essais et le stockage, **compter 40 à 80 $ pour l'épisode entier dans un style**.

## 4.2 Les API, même travail facturé à la seconde

| Fournisseur | Modèle | Prix | Coût des 762 s | Première et dernière image | Remarque |
|---|---|---|---|---|---|
| **fal.ai** | Wan 2.5 | 0,05 $/s | **38 $** | oui | Le moins cher des accès directs. |
| **Alibaba Model Studio** | Wan 2.6 | 0,0708 $/s | **54 $** | oui | Accès direct au constructeur. |
| **Alibaba Model Studio** | Wan 2.7 720p | 0,086 $/s | **66 $** | oui, plus clonage de voix | Le plus récent de la famille. 0,144 $/s en 1080p. |
| **Higgsfield** | Kling 3.0 | environ 7 crédits pour 5 s en 720p, soit 0,068 $/s | **52 $**, environ 1 070 crédits | oui | Déjà connecté, déjà payé en partie. |
| **Higgsfield** | Seedance 2.0 | environ 22 crédits pour 5 s en 720p, soit 0,216 $/s | **165 $** | oui | Excellent en cohérence d'identité, cher. |
| **Higgsfield** | Veo 3.1 | environ 29 crédits pour 4 s, soit 0,355 $/s | **270 $** | oui sur la variante Lite | Hors sujet : trop photoréaliste, trop cher. |
| **BytePlus ModelArk** | Seedance 2.0 et 2.5 | packs de jetons, 4,30 $ le million, déduction variable selon 480p, 720p, 1080p | non normalisable en l'état | oui | Tarification opaque tant qu'on n'a pas mesuré la consommation réelle. Aucun intérêt à passer en direct tant que fal et Higgsfield revendent les mêmes modèles à un prix lisible. |
| **ElevenLabs Image and Video** | Wan 2.5 et 2.6, Seedance 1 Pro, 1.5 Pro, 2.0, Kling 2.5 à 3.0, Veo 3.1, Sora 2, LTX, Runway | prix affiché avant génération, non documenté par modèle | à mesurer | oui sur Seedance, Kling et Wan, non sur Sora | **Point de vigilance : Seedance et Kling y sont annoncés indisponibles depuis les États Unis.** Vérifier la disponibilité depuis Dubaï avant d'en dépendre. |

Vous avez vu juste : ElevenLabs héberge bien Wan et Seedance depuis le lancement de son offre Image and Video. L'intérêt réel est de n'avoir **qu'un seul fournisseur et une seule facture** pour la voix et l'image animée, avec en prime le lipsync maison. L'inconvénient est qu'on paie un intermédiaire de plus sur des modèles accessibles moins cher ailleurs, et que la grille par modèle n'est pas publiée.

## 4.3 Recommandation

**Chaîne principale : ComfyUI sur RunPod, Wan 2.2 I2V A14B en FP8, LoRA LightX2V à 4 étapes, LoRA de style maison, variante FLF2V pour les raccords.** C'est la seule option qui verrouille le style, et c'est aussi la moins chère à l'échelle de l'épisode, d'un facteur trois à cinq contre les API.

> **Tranché le 22 août 2026, voir `DECISIONS-pilote.md`** : sur le pilote, RunPod rend **les 48 clips des trois styles en premier** ; la contre épreuve API (Wan 2.7 plutôt que Kling 3.0, seul modèle qui descend à 2 s) n'est lancée que si le rendu RunPod ne convient pas.

**Contre épreuve sur le pilote, et seulement sur le pilote** : passer les 16 clips de la première séquence par **Higgsfield Kling 3.0** avec image de départ et image de fin. C'est déjà connecté, cela coûte environ 300 crédits sur les 1 032 disponibles, et cela donne une base de comparaison honnête. Si le rendu Kling tient le style aussi bien que Wan 2.2 avec LoRA, l'argument du local s'effondre et on gagne un temps considérable.

**Deuxième contre épreuve, si le temps le permet** : LTX 2.5 en multi plans, pour voir si un bloc entier de 9 s avec ses trois coupes internes peut sortir d'un seul rendu. C'est le seul scénario où les prompts de mouvement déjà écrits restent valables sans réécriture.

**Écartés** : Veo et Sora, trop chers et trop photoréalistes pour du cel 2D. BytePlus en direct, tant que la tarification par jetons n'est pas mesurée et que les mêmes modèles sont revendus ailleurs à un prix lisible.

---

# 5. Le graphe ComfyUI

## 5.1 Modèles et fichiers à mettre sur le volume réseau

* `Wan2.2-I2V-A14B` en FP8, plus la variante `Wan2.2-14B-FLF2V`
* LoRA d'accélération `LightX2V` pour Wan 2.2
* LoRA de style maison, à entraîner, voir 5.3
* VAE et encodeur de texte de Wan 2.2
* Optionnel : `Wan2.2-TI2V-5B` pour les brouillons de cadrage sur GPU bon marché

## 5.2 Le graphe, dans l'ordre

1. **Chargement de l'image de départ**, sortie Nano Banana Pro en 2752 x 1536, redimensionnée en 1280 x 720.
2. **Premier clip d'un bloc** : I2V simple, image de départ seule.
3. **Clips suivants du même bloc** : FLF2V, avec la dernière image du clip précédent en première image. Quand la coupe est nette et non un raccord de continuité, revenir à l'I2V simple avec une image de départ neuve, générée pour ce cadrage.
4. **Échantillonnage** : 4 étapes, CFG 1, avec le LoRA LightX2V.
5. **Longueur** : 40 images à 16 im/s pour un clip de 2,5 s. Ajuster au cas par cas selon la durée exacte de la coupe.
6. **Décimation à 10 im/s** en fin de graphe, ou au montage. À décider sur le pilote : la décimation dans le graphe fige le choix, au montage elle reste réversible. **Recommandé : au montage.**
7. **Sortie** : ProRes ou PNG en séquence, jamais du H.264 à ce stade. Le H.264 est pour la livraison, pas pour le master.

## 5.3 Le LoRA de style, la pièce qui fait la différence

Le dépôt contient 253 images validées et homogènes par style. C'est un jeu d'entraînement propre, déjà audité, déjà nettoyé de son lettrage parasite. Entraîner un LoRA de style par style retenu, sur les décors et les personnages de ce style, permet de tenir le contour noir constant et l'aplat sans dégradé sur toute la longueur d'un clip, là où le modèle de base a tendance à ramollir le trait dès la deuxième seconde.

À faire **après** le choix du style, sur un seul style, jamais sur les trois.

---

# 6. Nouveau gabarit de prompt de mouvement

> **Appris sur le pilote, 22 août 2026 (voir `S01E01-pilote-audit.md`, clips, et `DECISIONS-pilote.md`).** Trois amendements au gabarit ci dessous : (1) la ligne « Characters gesture and react, they do not speak » ne se colle que sur les clips qui ont des personnages ; sur un plan vide on écrit « There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame », sur des mains seules « Only the hands and arms already in the first frame move; no face, no head and no other person appears », sur une foule de dos « The crowd keeps its back to the camera… » ; (2) négatives de présence ajoutées : `new character entering the frame, person appearing, face appearing, giant face, ghost figure, figure emerging from the mist, hands appearing, head appearing, crowd figures turning to face the camera, dot eyes on crowd figures, faces in the crowd` ; (3) **le bloc de style ne se copie pas tel quel en vidéo** : réduit à la facture (trait, aplats, palette, cadence), sans description des personnages, sinon le modèle en fabrique (style B : 12 clips sur 16 avec des têtes inventées, 0 sur 12 avec le bloc réduit). Le gabarit exécutable est `docs/scripts/build_clips_pilote.py`.

L'ancien gabarit décrivait plusieurs plans séparés par des coupes. Le nouveau décrit **un seul geste continu**. Il remplace intégralement la section 5 du plan de production pour les blocs ANIMÉ.

```
[BLOC DE STYLE ANGLAIS du style retenu, collé octet pour octet]

Single continuous shot, no cut, no scene change.
Subject : <ce qui bouge, une seule action>
Camera : <fixe, ou un seul mouvement lent et nommé>
Duration : <2 à 3> seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Characters gesture and react, they do not speak.
Motion starts on the first frame, no frozen start.

Avoid: photorealistic rendering, skin texture, smooth gradients, cut, scene change, camera shake, text, watermark, lip sync, mouth articulation
```

Trois règles de rédaction :

* **Une action par clip.** Si la description en contient deux, c'est qu'il faut deux clips.
* **Aucune coupe dans le prompt.** Le mot `cut` ne figure qu'en négative.
* **La caméra ou le sujet, rarement les deux.** Un panoramique sur un sujet qui bouge est le meilleur moyen d'obtenir de la bouillie en 2,5 s.

---

# 7. La chaîne voix, ElevenLabs

## 7.1 Ce qu'il y a à dire

Extrait par script des 79 plans du scénario :

Comptage définitif du 22 août 2026, contrôlé : 1 957 mots attribués sur 1 957 mots entre guillemets, aucun orphelin.

| Locuteur | Répliques | Mots | Part | Plans |
|---|---|---|---|---|
| **SAM** | 61, dont **30 en voix off** | 1 513 | 77,3 % | 60 plans |
| **ELIO** | 18 | 199 | 10,2 % | 18 plans |
| **NAYA** | 11 | 103 | 5,3 % | 11 plans |
| LE BADAUD | 2 | 17 | 0,9 % | 50 |
| BADAUD 1 | 2 | 16 | 0,8 % | 2, 63 |
| LE GÉNÉRAL | 1 | 16 | 0,8 % | 66 |
| COMPÈRE 1 | 1 | 16 | 0,8 % | 67 |
| PAYSAN 2 | 1 | 14 | 0,7 % | 22 |
| PILLARD 1 | 1 | 13 | 0,7 % | 55 |
| BADAUD 2 | 2 | 11 | 0,6 % | 2, 63 |
| LA SENTINELLE | 1 | 11 | 0,6 % | 66 |
| PAYSAN 1 | 1 | 10 | 0,5 % | 22 |
| L'AIDE | 1 | 7 | 0,4 % | 3 |
| PILLARD 2 | 1 | 6 | 0,3 % | 55 |
| L'AUTRE | 1 | 3 | 0,2 % | 50 |
| GARNERIN | 1 | 2 | 0,1 % | 3 |
| **Total** | **106** | **1 957** | | **16 locuteurs** |

Environ 12 100 caractères. Débit moyen de 96 mots par minute sur 21 min 36, **juste au dessus de la fourchette de 85 à 95 de la bible**, ce qui est acceptable. Sam porte plus des trois quarts du texte, fidèle au déséquilibre du corpus d'origine.

**33 plans font dialoguer deux locuteurs ou plus**, dont trois à trois voix : les plans 63, 66 et 67. À prendre en compte au montage, ces plans demandent des prises séparées recollées.

Didascalies présentes dans le texte verrouillé, à respecter à la prise : `(voix off)` et `(off)` pour Sam et Elio, `(en écrivant)` et `(lisant)` pour Naya, `(tendant la main)` et `(payant)` pour les badauds du plan 63.

## 7.1 bis Casting — huit voix, et pourquoi pas cinq

Une première version de ce document disait « cinq voix, dont deux d'appoint ». C'était sous calibré. Deux voix d'appoint suffisent à éviter les collisions **à l'intérieur d'un plan**, puisque aucun plan ne fait dialoguer plus de deux figures d'époque. Mais à l'échelle de l'épisode, les mêmes deux timbres joueraient les treize figures, dans sept scènes différentes, sur 21 minutes. Le spectateur l'entend.

Le coût marginal d'une voix supplémentaire est nul : les treize figures représentent **722 caractères en tout**, le prix est dans le texte, pas dans le nombre de timbres. Le seul coût réel est l'audition et le verrouillage des identifiants. **Huit voix est le bon point d'équilibre.**

| Voix | Personnages | Répl. | Caractères | Plans |
|---|---|---|---|---|
| **V1 Sam** | Sam | 61, dont 30 en voix off | 8 474 | 60 plans |
| **V2 Elio** | Elio | 18 | 1 053 | 7, 11, 14, 15, 18, 24, 25, 27, 33, 34, 35, 51, 52, 57, 64, 69, 72, 77 |
| **V3 Naya** | Naya | 11 | 513 | 7, 10, 14, 20, 40, 43, 48, 53, 58, 75, 78 |
| **P1** rond, péremptoire | BADAUD 1 | 2 | 71 | 2, 63 |
| **P2** maigre, méfiant | BADAUD 2 | 2 | 54 | 2, 63 |
| **P3** grave, autoritaire | LE GÉNÉRAL · L'AUTRE · GARNERIN | 3 | 120 | 66, 50, 3 |
| **P4** jeune, clair | PAYSAN 2 · LA SENTINELLE · L'AIDE · PILLARD 2 | 4 | 209 | 22, 66, 3, 55 |
| **P5** rustique, rugueux | LE BADAUD · COMPÈRE 1 · PILLARD 1 · PAYSAN 1 | 5 | 268 | 50, 67, 55, 22 |

**Vérifié par script : aucun conflit.** Dans aucun des 79 plans deux personnages ne partagent la même voix. Total 10 762 caractères.

### Les deux contraintes qui commandent ce casting

1. **P1 et P2 sont verrouillés.** Les deux badauds parient au plan 2 et se payent au plan 63, à seize minutes d'écart. Ce sont les mêmes personnages, ils doivent avoir la même voix, et ces deux timbres ne servent à personne d'autre.
2. **Aucune paire ne se répète dans une même scène.** Les sept scènes d'époque à deux voix sont les plans 2, 3, 22, 50, 55, 66 et 67. Le tableau les répartit sur P1 à P5 sans collision.

### Direction de jeu

**Les 30 répliques en voix off de Sam et ses 31 répliques jouées sont la même voix**, pas deux. C'est le même personnage qui raconte et qui parle dans le cadre. Ce qui change est le registre : posé et adressé au spectateur en voix off, vif et adressé à la table dans le cadre. À obtenir par les réglages de stabilité et par la ponctuation du texte verrouillé, jamais en changeant d'identifiant de voix.

Les didascalies du texte verrouillé sont des indications de jeu et se respectent : `(voix off)` et `(off)`, `(en écrivant)`, `(lisant)`, `(tendant la main)`, `(payant)`.

## 7.2 Modèle

**Eleven v3** pour tout : 70 langues dont le français, conçu pour la narration longue et le dialogue de personnage, limite de 5 000 caractères par requête. Nos 12 100 caractères passent en quelques appels, un par personnage et par séquence.

Eleven Multilingual v2 reste le repli si v3 se révèle instable d'une prise à l'autre : il est moins expressif mais plus régulier sur de longues séries, ce qui compte quand on doit raccorder 31 répliques de Sam enregistrées séparément.

Aucun besoin des modèles Flash : il n'y a pas de contrainte de latence, on n'est pas en temps réel.

## 7.3 Règles de production de la voix

* **Une prise par réplique, nommée par le numéro de plan** : `S01E01_p008_SAM.wav`. 106 prises au total. Le montage se cale sur le tableau de plans, pas sur un fichier fleuve.
* **Pas de synchronisation labiale.** La bible l'interdit sur les plans ANIMÉ, et les plans FIXE sont des images fixes avec mouvement de montage. C'est une économie considérable et cela retire tout besoin de modèle de lipsync dans le graphe. **Précision du 22 août 2026 (Guillaume) : pas de synchro ne veut pas dire bouches immobiles.** Sur un plan de dialogue, les personnages parlent en animation limitée (bouches qui s'ouvrent et se ferment, non synchronisées) ; les plans FIXE de dialogue peuvent être rendus en clip court bouclé (testé sur P02 et P03, voir `S01E01-pilote-audit.md` lot 4 et `DECISIONS-pilote.md`).
* **Verrouiller les huit identifiants de voix** dès le pilote, comme on a verrouillé les blocs de style, et les consigner dans l'index au même titre que les graines de clips. Une voix regénérée avec d'autres réglages ne raccorde pas.
* **Le pilote ne demande que trois voix** : P1 et P2 pour les badauds du plan 2, P3 et P4 pour Garnerin et son aide au plan 3, et V1 pour la voix off du plan 6. Soit cinq des huit, et c'est l'occasion de les auditionner sur du texte réel avant d'engager le reste.
* **Le texte dit est zone verrouillée**, ponctuation comprise. Aucune reformulation à la lecture, y compris pour améliorer le débit.

## 7.4 Musique et effets — Eleven Music

**Décision du 22 août 2026 : génération IA, chez ElevenLabs, sur la même plateforme que la voix.**

Le motif est juridique avant d'être artistique. Eleven Music est le seul générateur dont **les données d'entraînement ont été licenciées dès le départ**, par des accords signés avec Merlin et Kobalt. Suno et Udio ont transigé avec les majors fin 2025, mais leurs clauses d'indemnisation restent ambiguës et le risque de réclamation Content ID sur une chaîne monétisée n'est pas nul. Pour une série qui vise la diffusion, la sécurité de la licence prime sur les quelques points de qualité musicale que Suno conserve.

Avantages pratiques : **une seule plateforme, un seul pool de crédits et une seule facture** pour la voix, la musique et les effets sonores. Le paramètre `force_instrumental` garantit des pistes sans voix, ce qui est ce qu'il nous faut partout. Les morceaux vont de 10 secondes à 10 minutes. Les sorties portent un filigrane SynthID.

### Périmètre de diffusion, tranché le 22 août 2026

**YouTube et web uniquement.** Une offre ElevenLabs en libre service suffit donc, à partir de Starter : elles autorisent tout usage commercial en ligne et hors ligne, monétisation comprise.

**Ce qu'elles excluent, et qui reste hors périmètre : le cinéma, la télévision, la radio et les jeux de studio.** Si un diffuseur se manifeste un jour, il faudra passer à **Eleven Music Enterprise**, qui lève toutes les exclusions, et **régénérer toute la musique de la série** sous cette licence. La voix, les images et les clips ne sont pas concernés, seule la musique l'est. C'est une dette connue et bornée, pas un risque diffus.

Corollaire à tenir dès maintenant : **conserver le prompt et la référence audio de chaque morceau**, dans le même index que les graines de clips. Une régénération sous Enterprise doit pouvoir repartir des mêmes intentions, sinon la série change de son.

Deux autres limites à connaître : **la revente et la constitution d'une bibliothèque sous licence sont interdites** en libre service, et **rien dans la documentation ne mentionne l'export en pistes séparées**. Sans stems, on ne peut pas remixer un morceau au montage, seulement l'utiliser tel quel ou en régénérer un. À vérifier au moment de la mise en œuvre.

### Identité sonore de la série

Le thème se génère **une fois**, puis sert de **référence audio** pour toutes les variations d'épisode, avec le mécanisme d'Audio Reference et de Music Finetunes. C'est la même logique que les blocs de style verrouillés pour l'image : une source, des dérivés, jamais deux définitions concurrentes.

### Ce que l'épisode demande

Sept plages **sans aucune parole**, 184 s au total soit 3 min 04, où la musique porte seule :

| Plans | Durée | Ce que la musique doit tenir |
|---|---|---|
| 1 | 18 s | ouverture froide, attente et tension au parc Monceau |
| 4 à 5 | 28 s | l'ascension puis la lame sur la corde |
| 39 | 32 s | la crue du fleuve Jaune et le renflouage |
| 45 à 46 | 44 s | le vol du prince, la plus longue plage de l'épisode |
| 56 | 14 s | la fuite des pillards |
| 61 à 62 | 38 s | la descente et le verdict de Garnerin |
| 79 | 10 s | le teaser final |

Le reste, 69 plans et 1 112 s, est porté par la voix off et demande un lit musical discret, pas un thème. Prévoir donc **un thème, sept pièces courtes et deux ou trois lits d'ambiance réutilisables**, plutôt que 79 morceaux.

## 7.5 Effets sonores — Eleven SFX, et pourquoi ça vaut le coup

Étudié le 22 août 2026. **Verdict : oui, et pour cette série plus que pour une autre.**

### Ce que l'outil sait faire

SFX v2 produit des clips de **0,5 à 30 secondes en 48 kHz**, avec un **drapeau de bouclage sans couture**, un réglage `prompt_influence` de 0 à 1, une sortie MP3 ou PCM, et **quatre variantes par requête** pour choisir. Les offres payantes accordent la licence commerciale complète, sans attribution ni redevance par piste, et sans l'exclusion cinéma et télévision qui pèse sur Eleven Music : le palier Pro couvre explicitement le film, la diffusion, le jeu et la publicité.

### Les quatre raisons pour cette série

1. **Le bouclage change l'économie du poste.** Un lit d'ambiance de 8 secondes bouclé couvre la plage de 44 secondes du plan 45. Huit ambiances bouclées couvrent les 21 minutes de l'épisode. On ne génère pas 79 pistes, on en génère une poignée.
2. **La série a besoin de sons qui n'existent dans aucune bibliothèque.** Le gel d'Elio, sa signature sonore, revient sur **cinq plans, 75 secondes**. L'insert « main et sacoche » revient sur **dix plans, 155 secondes**. Ce sont des sons de marque, pas des bruitages génériques : ils se conçoivent une fois et se réutilisent, exactement comme leurs images.
3. **Même plateforme, même facture, mêmes droits** que la voix et la musique. Un seul contrat à comprendre au lieu de trois.
4. **Le monde inkman du style B n'a pas de son naturel.** Si ce style est retenu, aucune bibliothèque ne propose le bruitage d'un personnage bâton. Il faut l'inventer, et un générateur descriptif est le bon outil pour cela.

### Les trois limites à respecter

1. **Ce n'est pas un bruiteur.** L'outil de vidéo vers son manque les détails de foley qu'un humain ajouterait. **Ne pas l'appliquer aux 189 clips en masse.** Il sert aux ambiances, aux sons signature et aux grandes scènes, pas au pas à pas.
2. **Quatre variantes par requête veulent dire quatre écoutes.** C'est une tâche d'audition humaine, exactement comme l'audit visuel des images. La prévoir dans le planning.
3. **Le coût par génération n'est pas documenté publiquement.** Même discipline que pour les clips : **une génération d'essai, on lit la consommation, on extrapole.**

### Le devis en volume

L'épisode se répartit en **41 plans ÉPOQUE (766 s)**, **31 plans CADRE (424 s)** et **7 plans MIXTES (106 s)**. D'où trois familles :

| Famille | Nombre | Nature |
|---|---|---|
| **Ambiances bouclées** | environ 8 | le cadre intérieur, le parc au petit matin, le vent d'altitude, la campagne antique, le fleuve en crue, la ville Song la nuit, l'atelier et ses fours, la steppe |
| **Sons signature réutilisés** | environ 6 | le gel d'Elio, la sacoche qui s'ouvre et se referme, la tablette d'Elio, le crayon de Naya, la porte du plan 8, le carton titre |
| **Effets ponctuels** | 25 à 35 | la corde tranchée, le ballon qui s'arrache, la crue, le cerf volant, le pont de bambou, les fusées, les fours, la grange en feu |

**Une cinquantaine de générations pour l'épisode entier**, à quatre variantes chacune. C'est un poste léger, très loin du volume vidéo.

Les effets se posent au montage, après la voix et sous la musique.


---

# 8. Montage

Chaîne conseillée, la plus simple possible :

1. Assemblage sur la timeline dans l'ordre du tableau révisé, plan par plan, bloc par bloc.
2. **Plans FIXE** : import de l'image clé, application du mouvement de caméra de montage, sens précisé, sur la durée exacte de la colonne Durée.
3. **Plans ANIMÉ** : les clips du bloc bout à bout, sans transition, les coupes sont nettes par construction.
4. **Plans POST** : traitement appliqué à la source indiquée, gels d'Elio, inserts sacoche réutilisés.
5. **Décimation à 10 im/s** sur les seuls plans ANIMÉ, pour l'aspect animation limitée.
6. Voix posée sur les timecodes du minutage récapitulatif.
7. Musique et ambiances en dernier.

L'insert « main et sacoche » est **une seule image** réutilisée aux plans 23, 29, 34, 37, 63, 64, 67, 69, 72 et 73, avec l'objet changé. Le portrait de gel d'Elio est **une seule image** réutilisée aux plans 15, 25, 27, 34 et 52. Ces mutualisations sont déjà décidées dans le plan de production, il ne faut pas les redéfaire.

---

# 9. Budget

## 9.1 Le pilote, plans 1 à 6, trois styles

Contenu par style : blocs 1a, 1b, 4a, 4b et 5, soit 46 s d'ANIMÉ et 16 coupes, plus les plans FIXE 2 et 3. Le plan 6 est un POST sans génération.

| Poste | Par style | Trois styles |
|---|---|---|
| Images clés Nano Banana Pro | 18 | **54 images, 108 crédits Higgsfield** |
| Clips vidéo | 16 | **48 clips, 138 s** |
| Rendu sur RunPod L40S | environ 1 h 20 | **environ 4 h, soit 4 à 8 $** |
| Contre épreuve Kling 3.0 sur un seul style | | environ **110 crédits** |
| Voix : rien | | le pilote est muet, plans 1 à 5 sans parole sauf 2 et 3 |

Solde Higgsfield actuel : **1 032 crédits**. Le pilote y tient très largement.

## 9.2 L'épisode entier, un seul style

| Poste | Volume | Coût |
|---|---|---|
| Images clés Nano Banana Pro | 253 images | **506 crédits**, environ 25 $ |
| Rendu vidéo sur RunPod | 189 clips, 300 rendus avec reprises | **40 à 80 $** |
| Même rendu en API, pour comparaison | 762 s facturées | 38 $ chez fal, 52 $ chez Higgsfield en Kling 3.0, 54 à 66 $ chez Alibaba, 165 $ en Seedance 2.0 |
| Voix ElevenLabs | 6 800 caractères, 5 voix | négligeable devant le reste, tient dans une offre payante d'entrée de gamme, à confirmer sur votre plan |
| Musique et effets | non chiffré | à décider |

**Ordre de grandeur : entre 70 et 120 $ pour l'épisode complet dans un style**, hors musique et hors temps de travail. Ce n'est pas le coût qui décidera, c'est la tenue du style.

---

# 10. Ordre d'exécution

1. **Trancher le style ?** Non. C'est le pilote qui tranche. On produit les trois.
2. Rédiger les prompts d'image et de mouvement du pilote **dans les trois styles**, avec les blocs de style anglais de la fiche v3.4, et le nouveau gabarit de mouvement du point 6.
3. Générer les **54 images clés** du pilote sur Nano Banana Pro, par réinjection des plaques D1 et D2 et des fiches Garnerin, Foule et Parieurs déjà validées.
4. **Les regarder une par une** avant d'en dériver le moindre clip. C'est la règle la plus chère du dépôt quand on l'oublie.
5. Monter le pod RunPod, installer le graphe, générer les **48 clips**.
6. Contre épreuve Kling 3.0 sur les 16 clips d'un seul style.
7. **Choisir le style et le moteur.**
8. Entraîner le LoRA de style sur le style retenu.
9. Rédiger les prompts des plans 7 à 79 dans ce seul style.
10. Produire, monter, sonoriser.

---

# 11. Défauts à corriger avant de lancer

* ~~36 plans FIXE sans mouvement de caméra~~ **corrigé le 22 août 2026** : les 36 ont reçu leur mouvement de montage avec le sens précisé. Aucun plan FIXE n'est plus à un tiret.
* ~~22 plans trop courts pour leur texte~~ **corrigé le 22 août 2026** : allongés, l'épisode passe à 21 min 36, dans la fourchette de la bible.
* **La section 5 du plan de production est à réécrire** avec le gabarit du point 6, et ses prompts sont encore en formule française alors que la fiche v3.4 les remplace par les blocs de style anglais.
* ~~La musique n'a pas de source décidée~~ **tranché le 22 août 2026** : Eleven Music en offre libre service, diffusion YouTube et web uniquement. Voir le point 7.4, y compris la dette de régénération si un diffuseur télévisé se manifeste un jour.

---

# 12. Sources

Modèles ouverts et ComfyUI : [panorama LTX des modèles ouverts 2026](https://ltx.io/blog/open-source-video-generation-models-guide) · [guide Wan 2.2 ComfyUI, Thunder Compute, août 2026](https://www.thundercompute.com/blog/wan-2-2-comfyui-ai-video-model) · [workflows Wan 2.2 dont FLF2V, ComfyUI Wiki](https://comfyui-wiki.com/en/tutorial/advanced/video/wan2.2/wan2-2) · [LoRA LightX2V 4 étapes](https://www.nextdiffusion.ai/tutorials/fast-image-to-video-comfyui-wan2-2-lightx2v-lora)

RunPod : [grille tarifaire officielle](https://www.runpod.io/pricing) · [relevé GPUPerHour](https://gpuperhour.com/providers/runpod) · [worker ComfyUI serverless](https://github.com/runpod-workers/worker-comfyui)

API : [tarifs Wan 2.5, 2.6 et 2.7](https://evolink.ai/blog/wan-api-pricing-guide) · [tarifs fal.ai](https://fal.ai/pricing) · [Seedance 2.0 et BytePlus ModelArk](https://kingy.ai/news/byteplus-review-seedance-2-0-turns-byteplus-into-a-serious-ai-video-platform/) · [crédits Higgsfield](https://www.scopeful.org/blog/higgsfield-pricing-2026)

ElevenLabs : [modèles de synthèse vocale](https://elevenlabs.io/docs/overview/models) · [Image and Video, liste des modèles](https://elevenlabs.io/docs/eleven-creative/playground/image-video) · [annonce Image and Video](https://elevenlabs.io/blog/introducing-elevenlabs-image-and-video)
