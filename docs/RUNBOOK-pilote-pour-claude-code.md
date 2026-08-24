# Runbook du pilote — à dérouler par Claude Code

**22 août 2026.** Document opératoire. Il s'adresse à un agent qui tourne **sur la machine de Guillaume**, avec un accès réseau complet et le fichier `.env` du dépôt. Il produit le pilote de l'épisode S01E01, plans 1 à 6, dans les trois styles.

> **Pourquoi ce document existe.** La session Cowork qui l'a écrit n'a **aucun accès réseau** vers RunPod, ElevenLabs, HuggingFace ni le stockage Higgsfield : testé, tout répond 000. Elle peut écrire des documents et piloter Higgsfield par MCP, rien de plus. Vous, vous avez le réseau. C'est la seule raison de la division du travail qui suit.

---

# 0. À lire avant de commencer

Dans cet ordre, sans sauter :

1. `docs/METHODE-generation-images.md` — les 35 règles et leurs corollaires. Non négociables.
2. `docs/S01E01-pilote-prompts-3-styles.md` — les prompts. C'est votre matériau.
3. `docs/PIPELINE-video-et-voix.md` — le pourquoi de la chaîne.
4. `docs/RUNPOD-COMFYUI-mode-d-emploi.md` — seulement à la phase E.

Les trois règles qui coûtent le plus cher quand on les oublie sont en tête du `README.md`. La deuxième est celle qui vous concerne le plus : **une référence se regarde avant d'en dériver quoi que ce soit.** Quatre vingt seize images ont déjà été produites sur des références fautives faute de l'avoir respectée.

---

# 1. Conventions

| | |
|---|---|
| **Dépôt** | `C:\Git\iletaitunefois` — **source et destination de l'information validée**. Rien n'y entre sans avoir été regardé. |
| **Répertoire de travail** | `C:\Users\kyoms\Downloads\EpisodeModernise` — tout le reste, y compris les sorties brutes. |
| **Clés** | `C:\Git\iletaitunefois\.env` : `ELEVEN_LABS`, `RUN_POD`, `RUN_POD_S3_ACCESS_KEY`, `RUN_POD_S3_SECRET_KEY`. Ne jamais les afficher, ne jamais les écrire ailleurs. |

Arborescence de travail à créer :

```
EpisodeModernise/pilote/
  images/Style{A,B,C}/
  clips/Style{A,B,C}/
  clips-runpod/
  index-pilote.csv
  journal.md
```

## L'index, tenu au fil de l'eau et non à la fin

`index-pilote.csv`, une ligne par génération, écrite **au moment du lancement** et non après :

```
horodatage,asset,style,type,modele,job_id,duree_s,graine,statut,fichier,note
```

C'est la leçon la plus chère des campagnes précédentes : **trois identifiants consignés dans un document n'existaient pas**, découverts seulement au moment de télécharger, et les planches correspondantes n'avaient jamais été générées. Une ligne écrite avant le lancement vaut mieux qu'un historique fouillé après.

## Nommage

* Images : `P<plan><bloc>-<clip>_Style<X>.png`, par exemple `P1a-3_StyleC.png`. Plans FIXE : `P02_StyleA.png`.
* Clips : même racine, extension `.mp4`.
* Références envoyées : nom d'origine inchangé.

---

# 2. Prérequis à vérifier avant la phase A

Arrêtez vous et demandez si l'un des trois manque.

1. **Accès Higgsfield.** Le `.env` ne contient **aucune clé Higgsfield**. Il vous faut soit le serveur MCP Higgsfield configuré dans Claude Code, soit une clé ajoutée au `.env`. Sans cela, les phases A, B et D sont impossibles.
2. **Solde de crédits.** Relever le solde avant de commencer et le noter dans `journal.md`. Il était de **1 032 crédits** le 22 août. Le pilote doit tenir dedans.
3. **Les 15 fichiers de référence existent** aux chemins du point 3.1.

---

# 3. Phase A — les 15 références dans Higgsfield

## 3.1 Les fichiers

Cinq briques, trois styles, sous `C:\Git\iletaitunefois\assets\` :

| Brique | Chemin |
|---|---|
| D01, parc Monceau | `S01E01/decors/Style{A,B,C}/D01_Style*.png` |
| D02, ciel de Paris | `S01E01/decors/Style{A,B,C}/D02_Style*.png` |
| Foule | `S01E01/personnages-episode/Style*/Foule_Style*.png` |
| Garnerin | `S01E01/personnages-episode/Style*/Garnerin_Style*.png` |
| Parieurs | `S01E01/personnages-episode/Style*/Parieurs_Style*.png` |

## 3.2 La marche à suivre

Pourquoi renvoyer les fichiers plutôt que réutiliser les identifiants d'origine : **seuls 129 identifiants complets sont consignés pour 319 images**, et ils couvrent les passes correctives, pas la campagne initiale. Fouiller l'historique est lent et fragile. Un renvoi, une fois, règle la question pour tout l'épisode.

1. Copier les 15 fichiers dans `pilote/references/`.
2. Pour chacun : demander une URL d'envoi présignée à Higgsfield, y déposer les octets en PUT avec le bon `Content-Type`, puis **confirmer le média**. Un envoi non confirmé n'existe pas.
3. **Consigner les 15 `media_id`** dans `index-pilote.csv`, type `reference`.
4. Contrôle : les 15 identifiants sont là, aucun doublon, aucun vide.

**Point d'arrêt.** Sans les 15 identifiants, la phase B ne peut pas commencer.

---

# 4. Phase B — les 54 images clés

Réglages, sans exception : `nano_banana_pro`, `aspect_ratio: 16:9`, `resolution: 2k`, `use_unlim: false`, `count: 1`. **2 crédits l'image**, réinjection de référence comprise, elle ne majore rien.

Attention au piège qui a fait trébucher deux agents : on **soumet** `nano_banana_pro`. Le serveur répond `nano_banana_2`, qui est le nom du moteur, c'est normal et c'est le bon. **Soumettre `nano_banana_2` route vers un moteur allégé au même prix.** Vérifier ce qu'on envoie, pas ce qu'on reçoit.

## 4.1 Assemblage des prompts

Selon le point 1 de `S01E01-pilote-prompts-3-styles.md`, et **rien d'autre** :

```
[bloc de style, plan de scène, point 2]  +  [traitement d'époque, point 3]  +  [brique du plan, point 6]
+  Avoid: [négatives de la brique] + [base du style, 4.3] + [base personnages d'époque, 4.2] + [négative universelle, 4.1]
```

**Les blocs se copient octet pour octet. Ils ne se reformulent jamais.** C'est la règle qui a tenu sur 319 images ; les seules dérives constatées viennent des endroits où on s'en est écarté.

Ajouter `same characters as reference, same art style as reference` sur tout plan qui réinjecte un personnage.

Références par appel : **sept au maximum, dans l'ordre décor, personnages, accessoires**. Le décor toujours en premier, parce que la référence impose sa mise en page.

Table des références par plan, point 5 de la fiche de prompts :

| Plans | Réinjecter |
|---|---|
| 1a-1, 1a-4, 1b-1 | D01, Foule |
| 1a-2, 1a-3, 1b-3 | D01 |
| 1b-2 | D01, Foule |
| P02 | D01, Parieurs, Foule |
| P03 | D01, Garnerin |
| 4a-1, 4a-2 | D01, Foule, Garnerin |
| 4a-3 | D01 |
| 4b-1, 4b-3 | D02 |
| 4b-2, 5-1 | D02, Garnerin |
| 5-2, 5-3 | D02 |

## 4.2 Ordre de lancement

**Étape 1, trois images d'épreuve : le plan 2 dans les trois styles.** C'est le plan le plus exigeant du pilote : deux personnages à fiche, la foule et le décor dans la même image. S'il passe, le reste passe.

**Arrêt. Rapatrier ces trois images, les regarder, les faire valider par Guillaume.** Ne pas enchaîner.

**Étape 2, les 51 restantes**, par **lots de douze au maximum**, c'est un plafond dur, et **un style à la fois** pour ne pas mélanger les contrôles.

## 4.3 Suivi des jobs

Un lot peut renvoyer « Out of credits » à tort quand la file est chargée, sans rapport avec le solde : resoumettre par lots de quatre.

**Un job resté seul en `in_progress` alors que tout son lot est sorti n'est pas une file chargée, c'est un job mort.** Trois minutes suffisent à trancher. Resoumettre : la file est vide, cela aboutit en quelques secondes. Ne jamais attendre plus longtemps.

Faux positif `nsfw` possible sur les portraits rapprochés : le lever en retirant les descripteurs morphologiques du visage.

---

# 5. Phase C — rapatriement et audit

1. Télécharger les 54 images vers `pilote/images/Style*/`, renommées selon la convention.
2. Vérifier que chaque fichier fait bien 2752 x 1536.
3. Mettre `statut` et `fichier` à jour dans l'index.

## L'audit, treize points plus huit

Les treize points de la grille de `METHODE-generation-images.md`, dont le treizième, le balayage libre, qui est celui qui trouve ce que les douze autres ne cherchent pas. C'est ainsi qu'un visage dessiné sur le dos d'une main a survécu à trois campagnes.

Plus les huit contrôles du point 9 de la fiche de prompts. Les trois à ne pas rater :

* **Aucun visage lisible dans la foule**, sur les quatre plans de foule, dans les trois styles. Défaut déjà passé trois fois.
* **Garnerin est le même homme** aux plans 3, 4a-1, 4a-2, 4b-2 et 5-1. Les mettre côte à côte.
* **Style B : moufle noire arrondie à petit pouce sur chaque main visible**, y compris les mains qui nouent du clip 1b-3 et la main gantée du 4b-2.

**Point d'arrêt dur. Aucun clip n'est lancé avant validation des 54 images par Guillaume.** C'est la règle dont le non respect a coûté 96 images.

---

# 6. Phase D — les 48 clips

> **Écart décidé le 22 août 2026, voir `DECISIONS-pilote.md`.** Les 48 clips sont rendus **d'abord sur RunPod / ComfyUI** (la phase E ci dessous devient la phase principale, sur les trois styles). Ce qui suit dans cette section n'est exécuté **qu'en repli**, sur un seul style, si le rendu RunPod ne convient pas à Guillaume. Raison : Higgsfield coûterait 300 à 1 000 crédits sur les 1 032 nécessaires aux images, contre 10 à 15 $ de GPU.

**Modèle : Wan 2.7**, en 720p, **audio désactivé**. Choisi parce qu'il descend à 2 secondes, ce qu'aucun autre modèle disponible ne fait, et parce qu'il appartient à la même famille que le Wan 2.2 local, ce qui isole proprement la variable mesurée en phase E.

## 6.1 Le clip zéro, obligatoire

Le coût en crédits de Wan 2.7 n'est pas documenté. **Générer un seul clip**, le 5-3 du style A, qui est court et sans personnage. Relever la consommation dans les transactions. Extrapoler sur 48 clips plus 60 % de reprises. **Si la projection dépasse le solde, s'arrêter et le dire à Guillaume** plutôt que de lancer et de tomber à court au milieu.

## 6.2 Le lot

Durées exactes et briques de mouvement : point 7 de la fiche de prompts. Assemblage :

```
[bloc de style, plan de scène]  +  [brique de mouvement]  +  NEGATIVE: [négatives de mouvement, point 4.5]
```

Images de départ et de fin :

* **Premier clip d'un bloc** : image de départ seule.
* **Clips suivants du même bloc** : image de départ **et** image de fin, pour tenir le raccord. Les blocs concernés sont 1a, 1b, 4a, 4b et 5.
* **Jamais de raccord entre deux blocs** : là on veut une coupe nette.

Consigner la graine de chaque clip. Un clip validé qu'on ne peut pas reproduire est un clip perdu.

## 6.3 Rapatriement

Vers `pilote/clips/Style*/`. Puis un montage de comparaison par style, les 16 clips bout à bout, pour juger sur la continuité et non sur des clips isolés.

---

# 7. Phase E — la contre épreuve locale

> **Écart du 22 août 2026** : cette phase passe **avant** l'API et couvre **les 48 clips des trois styles**, pas seulement 16. Le paragraphe d'origine est conservé ci dessous pour mémoire.

Seulement **après** que Guillaume ait désigné un style favori. Les **16 clips de ce seul style**, rendus sur ComfyUI et RunPod, en suivant `RUNPOD-COMFYUI-mode-d-emploi.md` de bout en bout. Sortie dans `pilote/clips-runpod/`.

But : savoir si le modèle ouvert avec LoRA de style tient le trait mieux que l'API. C'est la seule question à laquelle la phase D ne répond pas.

Les dix pièges connus sont à la fin du mode d'emploi. Le premier et le deuxième coûtent une journée chacun : les modèles sur le disque du conteneur au lieu du volume réseau, et un seul expert chargé sur les deux.

---

# 8. Phase F — remontée au dépôt

Uniquement ce qui est validé, et uniquement après validation explicite.

1. `assets/S01E01/pilote/images/Style*/` — les images retenues.
2. `assets/S01E01/pilote/clips/Style*/` — les clips retenus.
3. `docs/S01E01-pilote-job-ids.md` — l'index nettoyé, au format des fiches `PASSE-*`.
4. Mettre à jour `docs/S01E01-index-assets-et-fichiers.md`.
5. Commit et push.

Le brouillon, les rebuts et les variantes restent dans le répertoire de travail. Le dépôt ne contient que du validé.

---

# 9. Règles absolues

1. **Ne jamais reformuler un bloc verrouillé.** Copier, coller, compléter.
2. **Ne jamais dériver d'une référence non regardée.**
3. **Ne jamais toucher au texte dit, aux durées, à l'ordre ou à la numérotation des plans.** Zone verrouillée. Un conflit se signale, il ne se tranche pas.
4. **Consigner l'identifiant au moment du lancement**, jamais après.
5. **Chiffrer avant de lancer une phase**, et dire ce qu'il restera pour les reprises.
6. **S'arrêter aux deux points d'arrêt** : après les trois images d'épreuve, et après l'audit des 54.
7. **Ne jamais afficher le contenu du `.env`.**
8. En cas de contradiction entre deux documents : le scénario gagne sur une contrainte technique, la fiche troupe gagne sur les identités, la méthode gagne sur la fabrication. Toute ambiguïté se signale, elle ne se tranche pas en silence.

---

# 10. Ce que le pilote doit permettre de trancher

Deux décisions, et elles appartiennent à Guillaume :

* **le style**, A, B ou C ;
* **le moteur**, ComfyUI local ou API.

Livrer, pour l'aider : les 54 images rangées par style, les trois montages de 16 clips, la comparaison des 16 clips rendus deux fois, et le relevé exact des crédits et du temps GPU consommés.
