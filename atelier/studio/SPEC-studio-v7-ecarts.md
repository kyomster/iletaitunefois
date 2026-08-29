# SPEC Studio v7 — ce qui manque par rapport à notre process

Lecture de `SPEC-studio-v7.md`, `SPEC-studio-v7-amendement-A.md` et `SPEC-studio-v7-amendement-B.md` (25 août 2026), confrontée à la chaîne réellement pratiquée sur S01E01 : 36 règles de méthode d'images, six montages de pilote, quatre moteurs vidéo essayés, une stratégie vidéo figée, un journal de production.

Écrit le 26 août 2026.

**Verdict général.** La spécification est solide sur ce qu'elle a choisi de tenir : la vérité en base, l'écriture par MCP seul, la validation humaine par session, l'empreinte et la péremption, la zone verrouillée, le refus d'appeler un modèle. Les manques ne sont pas des oublis d'architecture, ce sont **des angles morts sur la moitié vidéo et image de la chaîne**. La spec modélise très bien un scénario, ses faits, sa prose et ses voix ; elle modélise beaucoup moins bien ce qui nous coûte réellement du temps et de l'argent : un graphe ComfyUI, un clip rendu, une transcription qui prouve qu'une réplique a été dite, un fichier dérivé, un pod allumé.

Quatorze écarts, classés. Les cinq premiers empêchent la base de détenir la vérité de notre chaîne telle qu'elle existe aujourd'hui ; les suivants sont des étapes de méthode que nous pratiquons et que rien dans la spec n'oblige à pratiquer.

---

# A. Ce qui empêche la base de détenir notre vérité

## A.1 Le moteur vidéo et son graphe ne sont pas modélisés

**Ce que fait notre chaîne.** Un clip n'est pas défini par son prompt mais par le couple prompt + graphe. LTX-2.5 tourne en deux passes, avec neuf sigmas écrits à la main, un rééchantillonneur latent ×2, un `LTXVDualCFGGuider` réglé à 1 et 1, en 1280×704, longueurs `8n+1`, 24 images par seconde. Changer un seul de ces réglages change le rendu autant que changer le prompt. Nous avons remplacé Wan 2.2 par LTX-2.5 en cours de pilote : mêmes images de départ, mêmes textes, résultat sans rapport.

**Ce que prévoit la spec.** `Job.provider`, `Job.model`, `Job.settings Json`. Le graphe n'existe pas ; `settings` est un sac sans version ni empreinte, et il n'entre pas dans `promptHash`.

**Ce qui manque.** Un modèle `Engine` (ou `Graph`) versionné, au même statut que `Style` : le fichier de graphe au format API, ses paramètres normatifs, sa version. Son numéro de version doit entrer dans l'empreinte et dans la péremption transitive, exactement comme `styleVersion`. Sans cela, deux clips rendus à trois semaines d'écart sont réputés comparables alors qu'ils ne le sont pas, et un changement de moteur ne périme rien.

**Le test d'acceptation à ajouter** : incrémenter la version d'un graphe périme les médias qui en dépendent, et la fiche technique d'un média affiche le graphe qui l'a produit.

## A.2 Le prompt vidéo cite les répliques — la dépendance texte → clip n'existe pas

**Ce que fait notre chaîne.** Un prompt de dialogue **cite la réplique exacte entre guillemets**, avec la langue et le timbre : `says in French, grave voice: "Lâchez tout."`. C'est la leçon la plus chère du pilote : décrire le dialogue sans le citer a produit cinq montages de charabia et coûté une heure de pod. Le prompt d'un clip contient donc, littéralement, le texte d'une `Line` verrouillée.

**Ce que prévoit la spec.** `Clip` porte `subjectEn` et `cameraEn`. Le prompt réellement envoyé n'est stocké nulle part pour la vidéo, alors qu'il l'est pour l'image (`Asset.promptPos`). La péremption est transitive « par `AssetRef` et par `MusicCue.referenceCueId` » — pas par `Line`.

**Ce qui manque.** Deux choses. D'abord le prompt vidéo assemblé doit être un `Asset` de plein droit, avec son `promptPos`, son `promptNeg` et son empreinte, comme le prompt d'image. Ensuite **une modification de `Line.text` doit périmer tous les clips dont le prompt la cite** : il faut un lien `LineRef` entrant dans le `promptHash`. Aujourd'hui, corriger une réplique laisserait en place un clip qui dit l'ancienne, et rien ne le signalerait.

## A.3 La spec ne prévoit pas la voix générée dans le clip

**Ce que fait notre chaîne.** La méthode retenue le 24 août, et validée depuis sur six montages, est **la voix libre générée avec l'image** par LTX-2.5 : pas de prise séparée, la voix naît dans le clip, avec l'acoustique de la scène, et les lèvres suivent. C'est précisément ce qui a fait écarter nos prises ElevenLabs, jugées « studio avec de l'écho ». Deux autres modes restent techniquement validés : l'audio gelé IA2V, qui impose notre piste ElevenLabs telle quelle, et la voix référencée par ID-LoRA, une voix par rendu.

**Ce que prévoit la spec.** `lipSyncAutorise: false` dans le format ; « une prise par réplique, jamais un fichier fleuve » ; un `Asset` de kind `VOICE_TAKE` rattaché à une `Line` ; les 106 prises de S01E01 comme critère d'acceptation du lot 5. Le modèle suppose que le son est fabriqué à part et posé au montage.

**Ce qui manque.** Un `voiceMode` déclaré par programme ou par saison — `EXTERNE`, `INTEGREE`, `GELEE` — parce que les contrôles diffèrent radicalement selon le mode : en `INTEGREE` il n'y a pas de prise à auditer, il y a un clip à transcrire ; en `GELEE` la prise existe et doit être retrouvée intacte dans le clip. En l'état, l'import de S01E01 produirait 106 prises attendues qui n'existent pas, et le lot 5 échouerait sur un critère devenu faux. Le manque est bien du côté de la spec : notre méthode est arrêtée, c'est le modèle de données qui décrit encore la chaîne ElevenLabs d'avant le pilote.

## A.4 La conformité d'une réplique se vérifie par transcription, et ce contrôle n'existe pas

**Ce que fait notre chaîne.** Chaque montage passe par `analyse_montage.py` : une image par seconde, l'audio extrait, une transcription horodatée, une frise des plans. C'est la transcription — et elle seule — qui a révélé que les cinq montages v7 parlaient un charabia inventé. Un clip peut être parfait à l'image et dire n'importe quoi.

**Ce que prévoit la spec.** `Verdict` avec `rating` et `defects Json`, audité par un humain en session. Rien qui rattache un texte reconnu à un texte attendu.

**Ce qui manque.** Un `Transcript` rattaché à un `MediaFile` (moteur, langue, segments horodatés) et un contrôle déterministe **texte attendu contre texte entendu**, rendu comme une alerte bloquante en cas d'écart. Avec une réserve à écrire noir sur blanc, car nous l'avons payée : **la transcription se trompe sur les nombres** — « Dix francs » est ressorti « Dis Franck » sur trois styles alors que le clip était juste. Le contrôle doit donc être un signalement que l'oreille humaine peut lever, jamais un verdict automatique. C'est un `Learning` à importer tel quel.

## A.5 Les fichiers dérivés n'ont pas de modèle

**Ce que fait notre chaîne.** Ce que l'humain regarde n'est presque jamais le fichier sorti du fournisseur : c'est un montage concaténé à 24 images par seconde, une planche-contact d'une image par seconde, une image redimensionnée en 1280×704 pour servir de départ, une plaque rognée de ses bandes noires. La RÈGLE 35 dit même que certains défauts **ne se corrigent qu'en aval, jamais dans le prompt**, par un script — donc le fichier utile est le dérivé, pas l'original.

**Ce que prévoit la spec.** `MediaFile` en ajout seul, un objet S3 jamais écrasé, et des dérivés produits « à la volée, cache disque » pour les vignettes, les formes d'onde et les posters. Les dérivés sont traités comme de l'affichage, pas comme des livrables.

**Ce qui manque.** Un `DerivedFile` : fichier source, outil et paramètres qui l'ont produit, empreinte, rôle (`MONTAGE`, `PLANCHE_CONTACT`, `IMAGE_DE_DEPART`, `ROGNAGE`). Sans lui, un verdict d'audit désigne l'original alors que l'humain a jugé le dérivé, et le montage — notre unique instrument de jugement d'une séquence — n'existe pas en base. Le chapitre 22 range le montage hors périmètre : c'est défendable pour le montage final, ce ne l'est pas pour le montage de contrôle.

---

# B. Étapes de méthode que nous pratiquons et que la spec n'impose pas

## B.1 L'inventaire des éléments de continuité et leurs planches

Écart constaté aujourd'hui même, sur le pilote en style P : le ballon est sorti rayé crème sur les plans proches et rayé orangé sur les plans lointains, alors que les dix huit prompts le décrivaient avec les mêmes mots. Une description recopiée ne tient pas la continuité ; seule une image réinjectée la tient. C'est la RÈGLE 36, ajoutée à la méthode le 26 août.

La spec a tout ce qu'il faut pour le porter — `AssetRef` avec son ordre, `AssetUsage`, `refsMaxParPrompt: 7` — mais **rien qui l'exige**. Il manque une alerte calculée, peu coûteuse : *un élément déclaré de continuité, ou nommé dans deux plans ou plus, sans asset de référence commun réinjecté sur ces plans*. Et il manque la contrepartie côté écriture : le roster doit livrer, pour chaque objet de continuité, sa planche et la liste de ses plans, pas seulement son nom.

## B.2 Le contrôle de l'image contre le script

Guillaume l'a formulé pour le montage v7 : vérifier « la présence des personnages, les intentions, que le visuel correspond à l'action, que la position des personnages correspond au script et à l'environnement — pour couper la corde, il faut être dans la nacelle ». C'est ce contrôle qui a fait reprendre douze images.

La spec donne `Plan.synopsis`, de la prose. Un auditeur humain devant douze images en quatre minutes ne relit pas de la prose. Il manque une liste d'**attendus** par plan, courte et vérifiable — qui est présent, vu comment, placé où, tenant quoi — affichée à côté de l'image dans la session `AUDIT_IMAGES`. Sans elle, l'audit se fait de mémoire, et la mémoire laisse passer un bras qui coupe une corde depuis le mauvais côté d'une nacelle.

## B.3 Le verdict machine et le verdict humain ne sont pas la même chose

Nous faisons auditer les planches-contact par un agent avant de les montrer à Guillaume. C'est utile et c'est faillible : plusieurs verdicts d'agent se sont révélés faux au recontrôle. `Verdict.auditedBy` est une simple chaîne, donc rien n'empêche un verdict machine de compter comme une approbation, ce qui viderait l'ALERTE 5 de son sens. Il faut un `auditKind` — `MACHINE` ou `HUMAIN` — avec la règle : **un verdict machine ne clôt jamais une session et ne fait jamais avancer un `stage`.**

## B.4 L'épreuve comparative — c'est exactement ce qu'est un pilote

Notre pilote est un sous-ensemble de plans, les six premiers, rendu en six styles, avec un montage par style, pour trancher trois questions : le style, le moteur, la méthode de dialogue. La spec a la session `CHOIX_STYLE`, qui soumet « des plans, plusieurs styles, leurs images ». Deux manques : rien ne modélise l'épreuve elle-même (le sous-ensemble, les styles en lice, les artefacts produits, la question posée), et surtout **la session soumet des images fixes**. Or le défaut du ballon est invisible sur une image et évident sur un montage. Une session de choix de style doit pouvoir porter des vidéos.

## B.5 La trace d'exécution GPU

L'ALERTE 1 écarte le suivi de budget : décision prise, elle se respecte. Mais elle écarte au passage quelque chose qui n'est pas financier et dont nous apprenons à chaque session : quel pod, quel GPU, combien de temps, quels modèles étaient déjà sur le volume, quelle version de bootstrap, **et le pod a-t-il été éteint**. Notre erreur la plus coûteuse dans ce projet n'est pas un mauvais prompt, c'est un pod laissé allumé.

Proposition minimale, sans réintroduire de budget : un contexte d'exécution sur `Job` — identifiant de pod, type de GPU, durée, drapeau d'arrêt — et une alerte d'attention tant qu'un pod déclaré n'est pas déclaré arrêté.

## B.6 La rétention du stockage

La spec connaît un bucket, privé, où rien n'est jamais écrasé. Notre pratique en connaît deux, et Guillaume en a fait une bonne pratique permanente le 24 août : le **volume de calcul**, où les sorties sont écrites puis supprimées après rapatriement, et où seul le réutilisable reste — modèles, images clés, références, workflows ; et l'**archive**, permanente. Confondre les deux, c'est soit payer un volume qui gonfle, soit perdre les modèles à chaque session. Il manque un champ de rétention par `kind`, et la distinction des deux espaces.

## B.7 L'identifiant de média chez le fournisseur

`Job.providerJobId` existe. Ce qui n'existe pas, c'est l'identifiant du **média téléversé et réutilisable** — chez Higgsfield, les `media_id` de nos cinq planches de référence, valables pour tout l'épisode. Nous les consignons parce que les renvoyer coûte du temps et fait dériver les références. Un `Asset.providerMediaId`, par fournisseur, suffit.

## B.8 La variante d'identité par famille de style

`Character.canonSheet` est unique. Or nos blocs d'identité **changent selon la famille de style** : en style inkman, Garnerin est un bonhomme bâton à tête ronde et yeux en points ; dans les styles dessinés, c'est un aéronaute au visage résolu. Le script de références choisit la variante en fonction du style. La spec doit permettre un `canonSheet` indexé par famille, sinon la fiche canon devient fausse dès le deuxième style.

## B.9 Le corpus de règles perd son identité

`Learning` porte un titre, un corps, une catégorie et `doNotRetry`. Nos règles sont **numérotées, citées par leur numéro entre documents et jusque dans les commentaires des scripts**, et chacune porte sa preuve : quel style, combien de tirages, ce que disait la négative qui n'a pas marché. Une règle sans sa preuve se refait litige au bout de deux mois. Il manque deux champs : un numéro stable et une `evidence`. Le lot 1 prévoit d'importer « les 24 règles de méthode » : elles sont 36 aujourd'hui, avec leurs corollaires, et le compte est à refaire à l'import plutôt qu'à figer dans un critère d'acceptation.

## B.10 Le format n'a pas de bloc technique vidéo

Les clés du chapitre 6 décrivent l'image (`resolutionImage: "2k"`, `ratio: "16:9"`) et donnent `imagesParSeconde: 16` et `decimationImagesParSeconde: 10`. Le moteur retenu impose 24 images par seconde, 1280×704, des longueurs en `8n+1` et deux passes. Importer les valeurs actuelles produirait un format faux dès le premier lot vidéo. Il faut un bloc vidéo explicite, lu par les règles au lieu d'être supposé.

---

# C. Dans l'autre sens : ce que la spec impose et que nous ne faisons pas encore

À porter au crédit du document, ce sont de vrais manques de notre côté.

* **Le registre de faits sourcés.** Nous n'avons rien de structuré. Sur une série éducative, c'est le seul défaut qui abîme autre chose que le calendrier, et la spec a raison de le dire.
* **Les contrats de continuité de l'amendement B.** Notre plan 79 est un teaser et rien ne garantit qu'il soit honoré au début de S01E02. La progression de conviction d'Elio est exactement un état durable qui ne doit pas reculer.
* **Le budget de mots de B.3.3.** Il est cohérent avec notre minutage calibré et il protège une zone verrouillée. À adopter tel quel.
* **Le score de prose.** Nous n'en avons aucun, et l'ordre d'application de B.3.1 — couper l'inflation de sens avant de polir les adjectifs — est une discipline que nous n'appliquons pas.
* **La péremption transitive.** Nous la faisons de tête, mal.

---

# D. Trois réserves sur la spec elle-même

**Un commit par appel MCP en écriture** (ALERTE 2). Sur notre volumétrie — plusieurs centaines d'images clés, quatre-vingt-dix clips pour un seul montage comparatif, des reprises — cela produit des milliers de commits dont aucun ne raconte quoi que ce soit. Un commit par lot et un par clôture de session garderaient la traçabilité sans noyer l'historique.

**Le montage hors périmètre.** Défendable pour le montage final, intenable pour le montage de contrôle : c'est notre seul instrument de jugement d'une séquence, et la moitié de nos défauts ne se voient que là.

**Les critères d'acceptation chiffrés.** « Les 319 images sont en base », « les 106 prises se rattachent à leur réplique », « les 24 règles de méthode » : ces nombres datent d'avant le pilote. Ils sont faux aujourd'hui — six styles rendus, méthode de voix changée, 36 règles. Un critère d'acceptation qui porte un nombre périmé fait échouer un lot pour de mauvaises raisons. Mieux vaut écrire « le compte de l'import est vérifié contre l'index des assets », et laisser le rapport d'import donner le nombre.

---

# Récapitulatif

| # | Écart | Gravité | Correction proposée |
|---|---|---|---|
| A.1 | Graphe et moteur vidéo non modélisés | bloquant | modèle `Engine` versionné, entrant dans l'empreinte et la péremption |
| A.2 | Prompt vidéo non stocké, dépendance `Line` → clip absente | bloquant | prompt vidéo en `Asset`, `LineRef` dans le `promptHash` |
| A.3 | La spec ne prévoit que la prise séparée, pas la voix générée dans le clip | bloquant | `voiceMode` : `EXTERNE`, `INTEGREE`, `GELEE` |
| A.4 | Aucun contrôle texte attendu / texte entendu | bloquant | `Transcript` + alerte d'écart, levable à l'oreille |
| A.5 | Fichiers dérivés non modélisés | bloquant | `DerivedFile` avec source, outil, paramètres, rôle |
| B.1 | Éléments de continuité sans planche | important | alerte calculée + roster livrant la planche |
| B.2 | Pas d'attendus vérifiables par plan | important | `PlanExpectation`, affichée dans l'audit |
| B.3 | Verdict machine indistinct du verdict humain | important | `auditKind`, sans effet sur les sessions |
| B.4 | L'épreuve comparative n'existe pas | important | modèle d'épreuve ; `CHOIX_STYLE` portant des vidéos |
| B.5 | Aucune trace d'exécution GPU | important | contexte d'exécution sur `Job`, alerte si pod non arrêté |
| B.6 | Pas de rétention de stockage | moyen | rétention par `kind`, calcul et archive distingués |
| B.7 | Pas d'identifiant de média fournisseur | moyen | `Asset.providerMediaId` |
| B.8 | Fiche canon unique pour toutes les familles de style | moyen | `canonSheet` indexée par famille |
| B.9 | Règles sans numéro ni preuve | moyen | `number` et `evidence` sur `Learning` |
| B.10 | Format sans bloc technique vidéo | moyen | bloc vidéo lu par les règles |

**Le fil commun des cinq écarts bloquants** : la spec traite l'image et la vidéo comme des fichiers produits par un fournisseur, alors que dans notre chaîne ce sont des fichiers produits par **un graphe que nous réglons**, contrôlés par **des dérivés que nous fabriquons**, et validés par **une transcription qui prouve qu'une réplique a été dite**. Aucun de ces trois objets n'existe dans le modèle. Ce sont eux qui manquent, plus qu'aucun outil MCP.
