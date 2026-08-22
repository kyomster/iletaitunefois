# Décisions du pilote S01E01 — journal des arbitrages

Une ligne par décision, datée, avec sa raison. Ce document capitalise ce qui a été tranché pendant le pilote ; le suivi brut reste dans le dossier de travail (`EpisodeModernise/pilote/journal.md`).

---

## 2026-08-22 — La vidéo se rend d'abord sur RunPod, l'API Higgsfield n'est qu'un repli

**Décision de Guillaume.** L'ordre des phases D et E du `RUNBOOK-pilote-pour-claude-code.md` est inversé :

* **Phase D** : les **48 clips** (16 par style, les trois styles) sont rendus sur **ComfyUI / RunPod**, Wan 2.2 I2V A14B, selon `RUNPOD-COMFYUI-mode-d-emploi.md`.
* **Phase E** : l'API Higgsfield (Wan 2.7) n'est lancée **que si le rendu RunPod ne convient pas**, sur un seul style, après `get_cost` et un clip zéro.

**Pourquoi.** Vérification du coût à partir des chiffres déjà consignés dans le dépôt, sans appel à Higgsfield :

| Moteur | Base de calcul | 48 clips, 138 s, ×1,6 de reprises = 221 s |
|---|---|---|
| RunPod L40S, Wan 2.2 I2V | `RUNPOD-COMFYUI-mode-d-emploi.md` §2, `PIPELINE-video-et-voix.md` §9.1 : ~1 h 20 de GPU par 16 clips, 0,79 à 0,99 $/h | ~4 h GPU soit 4 à 8 $, plus 1 à 2 h de mise au point et 7 $/mois de volume → **10 à 15 $ en argent, 0 crédit** |
| Higgsfield Wan 2.7 | prix non documenté ; fourchette `PLAN-pilote-execution.md` §4 : entre Kling 3.0 (7 crédits / 5 s ≈ 0,068 $/s) et Seedance 2.0 (22 crédits / 5 s ≈ 0,216 $/s) | **300 à 1 000 crédits, soit 15 à 48 $ d'équivalent crédits** |

Higgsfield est donc **2 à 5 fois plus cher** en équivalent crédits, et surtout consommerait **30 à 100 % des 1 032 crédits** disponibles, alors que ces crédits sont indispensables aux images : Nano Banana Pro y est irremplaçable pour la continuité avec les 319 assets validés (108 crédits pour le pilote, 506 pour l'épisode). Le temps GPU RunPod, lui, ne mord pas sur ce budget.

**Limite connue de la comparaison.** Le LoRA de style n'est entraîné qu'après le choix du style ; le rendu RunPod du pilote est donc du Wan 2.2 de base. Si le trait ne tient pas sur le pilote, la cause peut être l'absence de LoRA et non le moteur.

**Ce qui reste à mesurer, seulement si la phase E se déclenche.** Le coût réel de Wan 2.7 par seconde chez Higgsfield (`get_cost:true`, 0 crédit, puis un clip zéro), et si l'audio natif peut être coupé.

## 2026-08-22 — Faits du catalogue Higgsfield relevés en phase de plan

Relevés par `models_explore`, sans aucune génération. À ne pas re‑mesurer.

* `nano_banana_pro` : rôles `image_references`, résolutions `1k`/`2k`/`4k`, 16:9 disponible. Inchangé par rapport à `METHODE-generation-images.md` §19.
* `wan2_7` : durée **2 à 15 s** par pas entiers, résolution `720p`/`1080p`, rôles `start_image`, `end_image`, `audio_references`. **Aucun paramètre d'audio** (ni `sound` ni `generate_audio`) exposé dans le catalogue : la consigne « audio désactivé » du runbook §6 ne sera peut‑être pas applicable sur ce modèle.
* Solde au 22 août : **1 032,44 crédits**, plan Plus. Trois médias seulement étaient déjà envoyés chez Higgsfield, aucun n'est une de nos références : le renvoi des 15 fichiers (phase A) est nécessaire.

## 2026-08-22 — Règles de travail données par Guillaume

* **Aucun appel Higgsfield pendant une phase de planification**, même un préflight de coût. Les coûts se vérifient d'abord sur les chiffres du dépôt.
* **Toute information à capitaliser va dans `docs/`**, au moment où elle est acquise. Le dossier de travail ne garde que le brut et le suivi.

## 2026-08-22 — Corrections de fiche décidées pendant la phase B/C (validées par Guillaume)

* **P02** : négative de foule §4.4 retirée (RÈGLE 26). P02_StyleA et B validés avec la v1 du prompt, P02_StyleC avec la v2.
* **1a‑2** : référence Foule ajoutée à la table §4.1 (RÈGLE 27).
* **5‑2** : brique précisée, `the rope is still in ONE piece and taut, only a few outer fibres cut and springing free one by one, the blade halfway through` (RÈGLE 7 : deux styles sur trois montraient une corde déjà tranchée).
* **5‑2 et 5‑3** : `Decor: D2` explicité en `the sky and the rooftops of Paris far below` (RÈGLE 28).
* **1b‑2, 1b‑3, P03** : clause « ballon au‑dessus, pas d'autre nacelle » (RÈGLE 29), à la demande de Guillaume après explication de la double nacelle.
* **Bannières 1a‑3** à écussons : acceptées pour le pilote.

Les prompts canoniques sont ceux de `docs/scripts/build_prompts_pilote.py` et de `prompts/S01E01-pilote-prompts-assembles.md` ; les versions antérieures sont commentées dans le script.

## 2026-08-22 — Contradiction à trancher dans la fiche personnages d'épisode

Le bloc identité de Garnerin dit `dark tailcoat` ; la fiche de référence validée `Garnerin_StyleC` le montre en **habit vert olive**. Sur le pilote, les trois images C qui montrent son habit suivent la fiche (olive). La fiche gagne sur les identités (hiérarchie du PROMPT‑MAÎTRE) ; le bloc de `prompts/fiche-prompts-personnages-episode-S01E01.md` est à mettre en accord pour le style C.

## 2026-08-22 — Les 54 images validées par Guillaume ; raccords par images clés

Point d'arrêt dur levé à 11 h 45 : les 54 images du pilote sont validées, la phase D (RunPod) peut commencer.

**Raccord à l'intérieur d'un bloc, tranché par Guillaume** : clip k = image clé k en départ, image clé k+1 en fin (FLF2V) ; le dernier clip du bloc part seul (I2V). Chaque image clé validée est à l'écran exactement à son temps, les coupes internes raccordent, aucune dérive ne s'accumule. L'autre lecture (départ = dernière frame rendue du clip précédent) est écartée. Cela précise `PIPELINE-video-et-voix.md` §5.2 et `RUNPOD-COMFYUI-mode-d-emploi.md` §6, qui étaient ambigus.

## 2026-08-22, 12 h 15 — Les clips internes d'un bloc se rendent en I2V, pas en FLF2V

La « chaîne par images clés » (départ = clé k, fin = clé k+1) a été essayée sur les sept premiers clips du style A. Résultat : comme les clés successives d'un bloc ont des **cadrages différents** (très large → moyen → contre‑plongée), le FLF2V **morphe la caméra et la foule** d'un cadrage à l'autre au lieu d'une coupe nette (bandes dans `pilote/_thumbs/clips/`, clips dans `pilote/clips-runpod/_flf2v/`). C'est le cas que `PIPELINE-video-et-voix.md` §5.2 réserve à l'I2V : « quand la coupe est nette et non un raccord de continuité, revenir à l'I2V simple avec une image de départ neuve ». Sur le pilote, toutes les coupes internes changent de cadrage : **les 48 clips sont rendus en I2V**, chacun depuis son image clé validée. Le FLF2V reste l'outil d'un raccord de continuité dans le même cadrage, ce qui n'arrive pas dans les plans 1 à 6. Décision prise par Claude Code pendant le rendu pour ne pas laisser tourner le GPU sur des clips inutilisables, signalée à Guillaume ; l'option `--chain` de `build_clips_pilote.py` permet de revenir en arrière.

## 2026-08-22, 12 h 40 — Le gabarit de mouvement dit ce qu'il y a à l'image, clip par clip

Premier lot I2V (19 clips rendus) : dans **quatre plans sans personnage ou presque**, le modèle en a fait apparaître — deux hommes qui surgissent dans la nacelle (4b‑1 A), un visage géant et une foule de têtes qui sortent de la brume (4b‑3 A), un inkman fantôme au premier plan (1a‑1 B), une tête d'inkman puis un homme à chapeau qui agrippent la corde (5‑3 B et C). Deux causes se cumulent : le bloc de style décrit des personnages (« exaggerated expressive face », « large round white heads… »), et la ligne du gabarit `PIPELINE` §6 « *Characters gesture and react, they do not speak* » est collée sur tous les clips, vides compris.

Correction appliquée (RÈGLE 4 et RÈGLE 25 : prescrire le vide en positif, nommer le défaut en négatif) : une **ligne de présence par clip** dans `build_clips_pilote.py` — `none` : « There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame » ; `hands` : « Only the hands and arms already in the first frame move; no face, no head and no other person appears » ; `crowd` / `character` : la ligne d'origine plus « Nobody new enters the frame, no figure appears in the foreground » — et des **négatives de présence** (`new character entering the frame, person appearing, face appearing, giant face, ghost figure, figure emerging from the mist, hands appearing, head appearing`). Les 13 clips A validables du lot v1 sont conservés ; 4b‑1, 4b‑2, 4b‑3 A et tous les B et C sont rendus avec le gabarit v2. Les v1 restent dans `pilote/clips-runpod/_v1/` pour comparaison. Le gabarit du `PIPELINE` §6 est à mettre à jour en conséquence après validation.

## 2026-08-22, 13 h 15 — Bloc de style vidéo réduit pour le style B (essai v3, concluant)

Avec le bloc de style B de la fiche, Wan 2.2 fabrique des têtes d'inkman partout (12 clips sur 16 inutilisables, voir audit lots 1 et 2). Essai sur les 12 clips fautifs avec un bloc réduit à la facture, sans aucune description de personnage, et une graine décalée de 1 : **12 sur 12 exploitables**. Décision de Claude Code pendant le rendu, signalée : les clips B retenus portent ce bloc réduit (`video_style=reduced` dans l'index). À entériner par Guillaume : pour la vidéo, le bloc de style de la fiche n'est pas copié tel quel ; il est réduit à la facture et l'image clé porte le style. Le `PIPELINE` §6 est amendé d'une note. A et C gardent le bloc de la fiche (sauf 4b‑3 A, rendu avec le bloc réduit).

## 2026-08-22, 14 h 05 — Phase F : remontée au dépôt sans les clips

Décision de Guillaume : commit et push des documents, des assets validés et des 54 images du pilote, **sans les mp4** (ni les séquences PNG), qui restent dans `EpisodeModernise/pilote/clips-runpod/` et `pilote/montages/`. Commit `43dfecc` sur `main`. La question du moteur (RunPod suffit‑il ?) et le choix du style restent ouverts ; Guillaume regarde les montages. Remarque consignée : le pilote est muet et sans synchronisation labiale par construction (PIPELINE §7.3 et §9.1), les plans FIXE reçoivent leur mouvement de caméra au montage final.

## 2026-08-22, 14 h 15 — Pas de synchro labiale ne veut pas dire bouches immobiles ; voix du pilote

Décision de Guillaume après le visionnage des montages : sur les plans de dialogue, **les bouches bougent** (animation limitée, non synchronisée), même si la série renonce au lipsync. Conséquences :
* `PIPELINE` §6 : la ligne « they do not speak » ne vaut que pour les clips sans dialogue ; sur un plan de dialogue, ligne `talking` et négatives sans `lip sync` / `mouth articulation` (gabarit exécutable `build_clips_pilote.py --talking`).
* `PIPELINE` §7.3 (« pas de synchronisation labiale ») reste vrai pour la synchro ; il est complété : un plan FIXE de dialogue peut devenir un **clip court bouclé** où les personnages parlent (P02 et P03 rendus en 5 s, bouclés sur 10 et 12 s). Si cette règle est retenue pour l'épisode, le ratio ANIMÉ du scénario (36,7 %) augmente, à recalculer.
* **Audio** : une seule piste voix pour les trois styles. Les quatre répliques du pilote sont générées avec ElevenLabs v3 : voix **grave** « Guillaume – Narration and voiceover » (`ohItIVrXTBI80RrUECOD`) pour BADAUD 1 et GARNERIN, voix **claire** « Curieux REM » (`jvSOBXJ1cP2sdvT5RgUP`) pour BADAUD 2 et L'AIDE. Ce sont des voix déjà présentes sur le compte ; elles ne sont pas verrouillées pour la série tant que Guillaume ne les a pas entérinées (PIPELINE §7.3 : verrouiller les identifiants de voix dès le pilote). Solde ElevenLabs : 6 778 / 10 000 caractères consommés sur la période, +120.
* Second pod A100 `8vem2qbtwzbw4y`, 14 h 17 → 14 h 55 UTC, ~0,9 $, 9 clips ; archive PNG `clips-runpod/_png/talk_output.tar`.
