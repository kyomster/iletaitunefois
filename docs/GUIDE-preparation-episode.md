# Guide de préparation d'un épisode — pour que les défauts du pilote ne se reproduisent pas

Écrit le 27 août 2026, à la demande de Guillaume : « fais en sorte que tous ces soucis n'existent pas dans les épisodes suivants, consigne toutes les informations et guide ».

Ce guide rassemble, dans l'ordre où on s'en sert, ce que le pilote de S01E01 a coûté à apprendre. Chaque point renvoie à la règle qui le fonde dans `METHODE-generation-images.md` et porte la preuve qui l'a produit. **Il se déroule avant de générer la première image d'un épisode**, pas après.

Les six défauts du pilote, et ce qui les aurait tous évités :

| Défaut constaté | Ce qui manquait | Étape du guide |
|---|---|---|
| Le ballon change de couleur d'un plan à l'autre | une planche de référence pour l'objet | §2 |
| La nacelle change de forme, puis de proportions | une description canonique, puis son échelle | §3 |
| Les figurants ont le visage noirci | une formulation adaptée à la famille de style | §5 |
| Une femme pose un chapeau sur son bonnet | une garde des objets, puis une action non ambiguë | §5 et §6 |
| On ne sait pas quelle corde il coupe | un cadrage qui montre les deux termes de l'action | §4 |
| Le parachute est un paquet posé au sol | la chaîne physique de la scène, écrite avant les plans | §1 |

---

## §1. D'abord la chaîne physique et les rôles, avant tout découpage

**C'est l'étape qui manquait complètement, et c'est la plus rentable.** Avant d'écrire les descriptions visuelles d'une séquence d'action, on écrit deux choses :

**1.1 Ce qui tient à quoi.** Un schéma en trois lignes suffit. Pour l'ouverture de S01E01 : `BALLON — corde — PARACHUTE replié — suspentes — NACELLE`. Sans lui, le scénario a décrit le parachute comme un colis posé au plancher, si bien que couper la corde faisait tomber le héros avec un bagage. Le défaut n'était visible ni sur une image, ni sur un plan, **seulement sur la logique**.

Le test : **prendre l'action culminante de la séquence et vérifier qu'elle produit bien son effet**, en suivant la chaîne. « Il coupe la corde » → que se détache-t-il de quoi ? → que devient chaque morceau ?

**1.2 Qui fait quoi**, en tableau, avec une colonne « ce qu'il ne fait jamais ». Pour chaque personnage : où il est physiquement, ce qu'il fait, ce qui lui est interdit. C'est ce tableau qui a révélé que l'aide de Garnerin, écrit « au rebord », était rendu **dans** la nacelle — et qu'il décollait donc avec lui.

**1.3 Chaque ordre a un destinataire à l'image.** Une réplique impérative — « lâchez tout », « tirez », « ouvrez » — s'adresse à quelqu'un. Si personne dans le cadre ne peut y répondre, la réplique flotte. On met dans le plan **la main, la corde ou le dos** de celui à qui l'ordre s'adresse, et on montre sa réponse au plan suivant.

**1.4 Le protagoniste ne disparaît pas.** Un interdit du type « aucun personnage dans ce plan », posé pour empêcher des figurants de surgir, ne doit jamais faire sortir le héros du film. Sur le pilote, Garnerin donnait un ordre puis disparaissait vingt secondes. Vérifier, sur la frise, qu'il n'existe pas de trou de plus de dix secondes sans le personnage dont on suit l'action.

---

## §2. L'inventaire des éléments de continuité, et leurs planches

RÈGLE 36. Tout élément qui doit être **identique d'un plan à l'autre** se met en référence : une description recopiée ne tient pas la continuité, seule une image réinjectée la tient.

1. **Passe d'inventaire sur le tableau de plans.** Tout élément nommé dans deux plans ou plus, qui porte une identité visuelle propre — objet manipulé, véhicule, machine, animal, vêtement remarquable, enseigne.
2. **Arbitrage** : retenu si sa dérive se verrait au montage.
3. **Une planche par élément**, sur fond gris uni prescrit en positif (RÈGLE 15 + RÈGLE 37).
4. **Deux vues quand l'objet est vu des deux côtés** : la nacelle est filmée de l'extérieur **et** de l'intérieur, une planche extérieure seule n'aurait rien tenu.
5. **Inscription dans la bible de l'épisode**, avec la liste des plans.
6. **Réinjection** au rang accessoires, dans la limite de sept références par appel.

Trois pièges, tous payés :

* **Une planche ne se pose que sur les plans où l'objet doit être VISIBLE.** Sur un plan dont la brique dit « hors champ », la référence le fait entrer dans le cadre.
* **Ajouter une référence déplace le cadrage** : le modèle recompose pour loger le nouvel objet. Le nombre et l'échelle se reprennent alors en positif.
* **Deux références qui montrent le même objet en donnent deux dans l'image** (RÈGLE 29). Si la plaque de décor porte déjà un ballon, la clause `ONE single … only, exactly the one shown in the reference` est obligatoire.

---

## §3. La description canonique d'un asset

RÈGLE 38, complétée par la RÈGLE 42. **Un nom commun n'est pas une description, et une description sans le nom n'est pas un objet.**

Un asset se décrit en **sept points**, dans le dépôt, avant la première génération :

1. **son nom exact**, écrit tel quel — « parachute », « semoir à trois rangs », « collier d'épaule » ;
2. **la forme d'ensemble** et sa proportion ;
3. **la structure** : comment les parties s'assemblent ;
4. **la matière et son état** ;
5. **les couleurs nommées en positif** (RÈGLE 30) ;
6. **l'échelle par rapport au corps humain** — « profonde jusqu'à la taille d'un homme, deux hommes peuvent s'y tenir côte à côte » : sans elle la forme tient mais les proportions dérivent ;
7. **ce que l'objet n'a pas**, dès qu'une variante plausible existe.

**Ne jamais retirer le nom pour contrôler l'état.** Le parachute avait été réécrit en `folded bundle of undyed cream coloured raw silk` pour nommer les couleurs en positif : le modèle a dessiné du linge plié, parce que plus rien ne lui disait ce que c'était. **Le nom porte la fonction et la structure, l'adjectif porte l'état** : on écrit `the folded parachute, closed and bound like a furled umbrella`, jamais une périphrase qui cache le nom.

Toutes les descriptions de S01E01 sont dans `prompts/S01E01-assets-prompts-v3.4.md` §7, chacune avec un statut : **validé**, **à générer**, **à arbitrer**.

---

## §4. Le cadrage

RÈGLE 39. Le cadrage porte le sens, ce n'est pas une question de goût.

* **Un plan d'action montre ce que l'action relie.** Au moins un plan du bloc tient dans le même cadre les deux termes de la relation. Trois très gros plans successifs sur une corde ne disent pas ce qu'elle retient.
* **La variété des cadrages est une contrainte.** Le plan de production nomme une taille de plan par plan : elle se respecte. Trois plans de suite cadrés en dos de foule aplatissent une séquence.
* **Le cadrage se vérifie sur le montage, pas sur l'image.** Un cadrage juste isolément peut être faux dans la suite. C'est ce que la planche-contact à une image par seconde sert à voir.
* **Un décor qui doit se lire comme « au sol » garde le sol dans le cadre.** Une nacelle cadrée sur fond de ciel semble déjà voler.

---

## §5. Écrire une action que le modèle ne peut pas lire de travers

* **Quand deux actions différentes produisent la même image, aucune formulation ne les sépare : on change l'action.** Une main sur un chapeau, c'est *tenir son chapeau* et *poser un chapeau*. Remplacé par une main en visière au-dessus des yeux — même sens, image univoque. Devant un défaut d'action qui résiste à deux reformulations, arrêter de reformuler.
* **Un prompt de mouvement décrit un déplacement, jamais une possession** (RÈGLE 40). « Tenir », « prendre », « mettre », « sortir », « donner » appliqués à un objet déjà présent en fabriquent un second exemplaire. On écrit `raising both hands to the brim of the hat he is already wearing`.
* **L'image clé est un état de repos** (RÈGLE 31), le mouvement est dans le prompt vidéo.
* **Sur un style à aplats, ne jamais demander l'absence de traits** (RÈGLE 37) : deux ou trois tons par zone, « aucun visage » se résout par le ton le plus sombre. On supprime la **zone** — têtes strictement de dos — et on nomme la carnation en positif.

---

## §6. Les gardes qui doivent vivre dans le gabarit, pas dans la vigilance

RÈGLE 41 : une règle qui ne dépend que de l'attention sera oubliée. Ces clauses sont collées par les scripts sur **tous** les prompts concernés :

| Garde | Ce qu'elle empêche | Où |
|---|---|---|
| `Nobody new enters the frame` | un figurant qui surgit dans un plan vide | `build_clips_pilote.py`, ligne de présence |
| `Every object visible is already present in the first frame` | un second chapeau, un objet qui se matérialise | `build_clips_pilote.py`, `CLAUSE_OBJETS` |
| `ONE single … only, exactly the one shown in the reference` | un deuxième ballon, une deuxième nacelle | `build_prompts_pilote.py`, clauses d'objet |
| citation exacte des répliques entre guillemets | un dialogue en charabia inventé | prompts vidéo, `STRATEGIE-generation-videos.md` §6 |
| négative anti aplat noir sur les styles à aplats | des visages de foule remplis de noir | `NEG_FOULE` variante P |

**Toute règle posée dans un script est aussi écrite en clair dans le dépôt**, avec le numéro de règle cité en commentaire (RÈGLE 41), et le tableau de correspondance est tenu à jour dans `METHODE-generation-images.md`.

---

## §7. La liste de contrôle, avant de lancer un lot

À dérouler dans l'ordre. Chaque case non cochée est un défaut qui apparaîtra à l'écran.

**Avant la première image**

- [ ] la chaîne physique de chaque séquence d'action est écrite, et l'action culminante a été testée dessus
- [ ] le tableau « qui fait quoi », avec la colonne « ce qu'il ne fait jamais »
- [ ] chaque réplique impérative a un destinataire visible dans le plan
- [ ] aucun trou de plus de dix secondes sans le protagoniste
- [ ] l'inventaire des éléments de continuité est fait, arbitré, et chaque élément retenu a sa description canonique en sept points
- [ ] chaque description porte le **nom** de l'objet, son **échelle** et ce qu'il **n'a pas**
- [ ] les planches de référence sont générées, contrôlées, et la liste des plans où chacune se réinjecte est écrite

**Avant chaque lot de clés**

- [ ] les références réinjectées le sont uniquement sur les plans où l'élément est visible
- [ ] les clauses `ONE single … only` sont présentes partout où deux références montrent le même objet
- [ ] les tailles de plan du plan de production sont respectées, et deux plans voisins ne sont pas cadrés pareil
- [ ] la variante de bloc identité correspond à la famille de style

**Avant chaque lot de clips**

- [ ] chaque sujet décrit un déplacement, pas une possession
- [ ] aucune action ne peut se lire de deux façons
- [ ] les répliques sont citées mot pour mot entre guillemets
- [ ] les gardes de gabarit sont bien collées (personnes, objets)

**Après le montage, avant de livrer**

- [ ] planche-contact à une image par seconde relue en entier
- [ ] transcription comparée au texte attendu, écarts levés à l'oreille
- [ ] continuité de chaque élément de référence vérifiée d'un bout à l'autre
- [ ] la chaîne physique se lit à l'écran : un spectateur qui n'a pas lu le scénario comprend ce qui tient à quoi

---

## §8. Où vivent les règles

`METHODE-generation-images.md` porte les 42 règles numérotées et leurs corollaires, chacune avec sa preuve. `STRATEGIE-generation-videos.md` porte la chaîne vidéo et les règles de prompt de mouvement. `BIBLE-modernisation-v5.1.md` porte ce qui contraint l'écriture dès le scénario. `S01E01-logique-ouverture-froide.md` est le modèle de ce que §1 demande pour une séquence d'action. Ce guide est la porte d'entrée : il ne remplace aucun des quatre, il dit dans quel ordre s'en servir.
