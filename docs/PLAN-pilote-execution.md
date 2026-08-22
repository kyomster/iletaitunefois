# Plan d'exécution du pilote — plans 1 à 6, trois styles

**22 août 2026.** Vérification des moyens, puis marche à suivre. Rien n'est lancé.

**Conventions posées ce jour** : le dépôt `C:\Git\iletaitunefois` est la **source et la destination de l'information validée**. `C:\Users\kyoms\Downloads\EpisodeModernise` est le **répertoire de travail** : c'est là qu'atterrit tout ce qui n'est pas encore validé. Rien ne remonte au dépôt sans avoir été regardé.

---

# 1. Vérification des moyens

## Ce qui est en place

| Élément | État |
|---|---|
| `.env` dans le dépôt | 4 clés : `ELEVEN_LABS`, `RUN_POD`, `RUN_POD_S3_ACCESS_KEY`, `RUN_POD_S3_SECRET_KEY` |
| Higgsfield | connecté par MCP, **1 032 crédits**, plan Plus |
| Assets de référence | les 319 images sont sur le disque de travail et dans le dépôt |
| Prompts du pilote | `S01E01-pilote-prompts-3-styles.md`, 18 images et 16 clips par style |
| Scénario et plan de production | à jour, durées révisées, mouvements complétés, concordants au plan près |
| Répertoire de travail | 2,9 Go, dont **1,5 Go de `_A_SUPPRIMER_A_LA_MAIN`** à purger |
| Outils locaux | `python3`, `ffmpeg`, `git`, `jq`, `curl` présents |

## Ce qui bloque, mesuré et non supposé

J'ai testé la connectivité depuis les deux environnements, le conteneur cloud et le pont vers votre machine.

| Cible | Résultat |
|---|---|
| `rest.runpod.io` | **injoignable** |
| `api.elevenlabs.io` | **injoignable** |
| `huggingface.co` | **injoignable** |
| CDN Higgsfield `d8j0ntlcm91z4.cloudfront.net` | **injoignable** |
| `pypi.org`, `registry.npmjs.org`, `api.github.com` | joignables |
| Extension Chrome | **aucun navigateur connecté** |

Conséquences directes, sans détour :

1. **Je ne peux pas piloter RunPod.** Ni créer le pod, ni télécharger les modèles, ni poster un graphe. Les clés du `.env` ne me servent à rien depuis ici.
2. **Je ne peux pas appeler ElevenLabs.** La voix et la musique sont hors de ma portée directe.
3. **Je ne peux pas rapatrier ce que je génère chez Higgsfield.** C'est le même mur que celui déjà consigné dans `lecons-generation-images-higgsfield.md`.
4. **Je ne peux pas regarder les images que je génère.** Le contrôle visuel, qui est la RÈGLE 2 du dépôt, ne peut pas être fait par moi tant que les fichiers ne sont pas revenus sur votre disque.

## Ce que le blocage ne bloque pas

Le serveur Higgsfield passe par le transport MCP et non par mon réseau. **Je peux donc générer, images et clips, et suivre les jobs.** C'est l'essentiel du pilote.

## ⚠ Faille à corriger avant tout commit

**`.env` n'est pas dans `.gitignore`.** Le dépôt pointe sur `github.com/kyomster/iletaitunefois`. Au premier `git add .`, les quatre clés partent en clair dans l'historique public, où elles restent même après suppression du fichier. C'est le premier geste de la phase 0, avant toute autre chose.

## Un point non résolu : les identifiants des références

Réinjecter une référence validée demande soit son identifiant de job, soit un nouvel envoi du fichier. Or **seuls 129 identifiants complets sont consignés pour 319 images**, et ils couvrent les passes correctives, pas la campagne initiale. Sur les cinq références du pilote, seules quelques unes sont retrouvables.

La solution retenue n'est pas de fouiller l'historique, lent et fragile : **renvoyer les 15 fichiers une bonne fois**, par le widget d'envoi Higgsfield, et **consigner les 15 identifiants obtenus** dans l'index du pilote. Une fois fait, c'est fait pour tout l'épisode.

---

# 2. Qui fait quoi

| | Moi | Vous |
|---|---|---|
| Phase 0, mise en ordre | scripts et documents | valider, lancer le commit |
| Phase 1, références | consigner les 15 identifiants | choisir les 15 fichiers dans le widget |
| Phase 2, 54 images | assembler les prompts, lancer, suivre | — |
| Phase 3, rapatriement | ranger, renommer, indexer | télécharger depuis Higgsfield |
| Phase 4, contrôle visuel | relire les images une fois revenues | regarder, trancher |
| Phase 5, 48 clips | lancer, suivre | télécharger |
| Phase 6, contre épreuve locale | le mode d'emploi est écrit | monter le pod, rendre 16 clips |
| Phase 7, décision | comparer, chiffrer | **choisir le style et le moteur** |

---

# 3. Les phases

## Phase 0 — mise en ordre, avant toute génération

1. **Ajouter `.env` à `.gitignore`**, avec `*.env` et `.env.*`. Vérifier par `git check-ignore -v .env`.
2. **Premier vrai commit** du dépôt : `docs/`, `assets/`, `.gitattributes`, `.gitignore`. Décider si les 319 PNG entrent dans le dépôt ou restent hors suivi. Recommandation : **les faire entrer**, ils font l'essentiel de la valeur et le dépôt reste sous 500 Mo. Les pousser sur GitHub.
3. **Purger `_A_SUPPRIMER_A_LA_MAIN`**, 742 fichiers et 1,5 Go. Le pont ne sait pas effacer, il faut soit me donner la permission de suppression, soit le faire depuis l'explorateur.
4. **Créer l'arborescence de travail** :

```
EpisodeModernise/
  pilote/
    references/                 les 15 fichiers à renvoyer
    images/Style{A,B,C}/        18 par style
    clips/Style{A,B,C}/         16 par style
    index-pilote.csv            asset, style, modèle, job id, prompt, graine, état
```

## Phase 1 — les 15 références dans Higgsfield

Les cinq briques, dans les trois styles :

| Brique | Fichier |
|---|---|
| D01, parc Monceau | `assets/S01E01/decors/Style{A,B,C}/D01_Style*.png` |
| D02, ciel de Paris | `assets/S01E01/decors/Style{A,B,C}/D02_Style*.png` |
| Foule | `assets/S01E01/personnages-episode/Style*/Foule_Style*.png` |
| Garnerin | `assets/S01E01/personnages-episode/Style*/Garnerin_Style*.png` |
| Parieurs | `assets/S01E01/personnages-episode/Style*/Parieurs_Style*.png` |

Envoi par le widget Higgsfield, qui laisse votre navigateur téléverser directement. Les 15 identifiants retournés vont dans `index-pilote.csv`. **C'est le seul moment du pilote où votre main est nécessaire avant que je puisse avancer.**

## Phase 2 — les 54 images clés

Assemblage selon le point 1 de `S01E01-pilote-prompts-3-styles.md`. Réglages `nano_banana_pro`, 16:9, 2K, une image par requête.

Ordre de lancement, par lots de douze au maximum, plafond dur :

1. **Trois images d'épreuve d'abord** : le plan 2 dans les trois styles. C'est le plan le plus exigeant du pilote, il porte deux personnages à fiche, la foule et le décor. S'il passe, le reste passe.
2. **Arrêt.** Vous les regardez. On corrige les blocs si besoin.
3. Puis les 51 restantes, par lots de douze, un style à la fois pour ne pas mélanger les contrôles.

Un job resté seul en `in_progress` alors que son lot est sorti est un job mort : trois minutes suffisent à trancher, on resoumet, voir la RÈGLE 19.

## Phase 3 — rapatriement

Téléchargement depuis Higgsfield vers `EpisodeModernise/pilote/images/Style*/`, renommage selon `P<plan><bloc>-<clip>_Style<X>.png`. Une fois les fichiers sur le disque, **je peux les lire et les regarder**, et le contrôle visuel devient possible des deux côtés.

Si vous connectez l'extension Chrome, ce téléchargement peut être automatisé depuis votre navigateur au lieu d'être fait à la main.

## Phase 4 — contrôle visuel

Les treize points de la grille de `METHODE-generation-images.md`, plus les huit contrôles propres au pilote, point 9 de la fiche de prompts. Les trois à ne pas rater : **aucun visage lisible dans la foule**, **Garnerin identique aux plans 3, 4a et 4b**, **moufles à pouce sur chaque main en style B**.

**Point d'arrêt dur.** Aucun clip n'est lancé avant que les 54 images soient validées. C'est la règle qui a coûté 96 images la dernière fois.

## Phase 5 — les 48 clips chez Higgsfield

Modèle retenu : **Wan 2.7**, pour deux raisons. Il accepte des durées à partir de 2 secondes, ce qu'aucun autre modèle de la liste ne fait, et nos clips vont de 2 à 4 secondes. Et c'est la même famille que le Wan 2.2 local, ce qui isole proprement la variable qu'on veut mesurer en phase 6 : ouvert contre fermé, et non un modèle contre un autre.

Il accepte `start_image` et `end_image`, ce qui couvre les raccords à l'intérieur d'un bloc. Résolution 720p. Audio désactivé partout : la voix vient d'ailleurs.

**Clip zéro obligatoire.** Le coût en crédits de Wan 2.7 n'est pas documenté. On génère **un seul clip**, on relève la transaction, on extrapole, et alors seulement on lance le lot. Sur 1 032 crédits, on ne lance pas 48 rendus à l'aveugle.

## Phase 6 — la contre épreuve locale, chez vous

Les 16 clips d'**un seul style**, celui qui sort gagnant de la phase 4, rendus sur ComfyUI et RunPod selon `RUNPOD-COMFYUI-mode-d-emploi.md`. C'est la seule façon de savoir si le LoRA de style maison tient sa promesse sur le trait.

## Phase 7 — décision

Deux choix, pris ensemble :

* **le style**, A, B ou C, sur les 54 images et les 48 clips ;
* **le moteur**, ComfyUI local ou API, sur la comparaison des 16 clips rendus deux fois.

Puis seulement : les prompts des plans 7 à 79 dans le style retenu, le LoRA de style, la production.

---

# 4. Budget du pilote

| Poste | Volume | Crédits |
|---|---|---|
| 3 images d'épreuve | 3 | 6 |
| 51 images restantes | 51 | 102 |
| Clip zéro | 1 | à mesurer |
| 47 clips restants | 47 | à extrapoler du clip zéro |
| Reprises, provision de 60 % | | à prévoir |

Ordre de grandeur attendu, si Wan 2.7 se situe entre Kling 3.0 et Seedance 2.0 : **entre 300 et 800 crédits pour les clips**. Avec les images, le pilote tient dans les 1 032 crédits, mais **pas confortablement dans le haut de la fourchette**. D'où le clip zéro.

Le rendu RunPod de la phase 6 est hors crédits : environ 1 h 20 de GPU, 1 à 2 $.

---

# 5. Ce qu'il me faut de vous pour démarrer

1. **Le feu vert sur la phase 0**, en particulier sur `.gitignore` et sur le commit.
2. **Les 15 références envoyées** par le widget Higgsfield.
3. Facultatif mais utile : **connecter l'extension Chrome**, ce qui automatiserait le rapatriement au lieu de 54 téléchargements à la main.

Le reste, je le fais.
