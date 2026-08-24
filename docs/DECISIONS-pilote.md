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

## 2026-08-22, 15 h 05 — Le style C est retiré des choix ; les plans de dialogue se découpent par locuteur

Décisions de Guillaume au visionnage des montages parlants :
* **Style C retiré** : le pilote se joue désormais entre A et B. Les clips et images C restent dans le dossier de travail et le dépôt comme archive.
* Un plan de dialogue rendu en **un clip de 5 s bouclé** donne des « scènes en double » et des **bouches qui parlent toutes les deux pendant tout le plan**, décalées des répliques. Nouvelle règle : **un plan de dialogue se découpe en clips par locuteur** — attente (bouches fermées) → le locuteur 1 parle seul → le locuteur 2 répond seul → silence —, chaque clip part de l'image clé **et y revient** (FLF2V avec départ = fin = image clé : le raccord est invisible, c'est ici que le FLF2V sert), et la réplique est posée au début du clip de son locuteur. Le prompt nomme qui parle et dit que l'autre garde la bouche fermée.
* Rappel de périmètre : pas de bruitages ni de musique dans le pilote (Eleven SFX / Eleven Music viennent ensuite) ; les plans 4 et 5 sont muets par le scénario.

## 2026-08-22, 15 h 20 — Raccord des sous-clips de dialogue : par dernière image rendue, pas par image clé

Le FLF2V avec départ = fin = image clé rend des sous-clips **quasi figés** (piège n° 8 du mode d'emploi RunPod : deux images identiques, mouvement mou). Abandonné après 6 rendus (`clips-runpod/_fige/`). Méthode retenue pour un plan de dialogue découpé par locuteur : sous-clip 1 en I2V depuis l'image clé validée, puis **chaque sous-clip suivant part de la dernière image rendue du précédent** (`docs/scripts/chain_dialogue_runpod.py`, quatre chaînes en parallèle, étage par étage). C'est la « chaîne par dernière image rendue » écartée le matin pour les clips à cadrage différent ; elle est juste ici parce que le cadrage ne change pas. Ajout à la règle : **le raccord se choisit selon que le cadrage change (I2V, coupe nette) ou non (chaîne par dernière image)** ; le FLF2V ne sert qu'avec deux images clés distinctes dans le même cadrage.

## 2026-08-22, 15 h 55 — Alignement des voix : recalage sur le mouvement mesuré, la vraie synchro demande S2V

Guillaume : « l'audio est clairement pas aligné au bon moment ». Cause : la bouche bouge quand le modèle vidéo le décide à l'intérieur du sous-clip, et plus longtemps que la réplique. Réponse immédiate, locale et gratuite (`docs/scripts/align_dialogue_audio.py`) : mesure du mouvement dans la moitié d'écran du locuteur, **sous-clip ré-échantillonné** pour que la durée du mouvement colle à celle de la réplique (+0,3 s, facteur borné 0,6 à 1,8) et **réplique posée au début du mouvement mesuré**. C'est un recalage de début et de durée, pas une synchronisation labiale. Montages `montage_Style{A,B}_parlant_v3.mp4`.

La seule façon d'obtenir une bouche **synchronisée** est un modèle piloté par l'audio : **Wan 2.2 S2V** (speech‑to‑video, `wan2.2_s2v_14B_fp8_scaled.safetensors`, 16 Go, nœud ComfyUI `WanSoundImageToVideo` avec l'encodeur wav2vec2) à partir de l'image clé et du mp3 de la réplique. C'est du lipsync, ce que `PIPELINE` §7.3 et la bible excluaient par choix de style et de coût ; la décision de le tester appartient à Guillaume.

## 2026-08-22, 15 h 55 — Deux défauts de continuité à corriger à l'image, pas au clip

* **4a‑1 / 4a‑2** : les deux images clés montrent le ballon au même niveau ; au montage il « redécolle » deux fois. La brique 4a‑2 doit dire l'état d'avancement : `the balloon already well above the treetops, rising away`. Même famille que 1a‑1 / 1a‑4 et 4b‑1 / 4b‑3 (cadrages voisins, voulus par le découpage).
* **5‑2 A** : deux manches différentes (beige et grise) sur les deux mains → lues comme deux personnes qui coupent. Brique : `Characters: ONE hand only, Garnerin's, in his dark sleeve`.
À reprendre quand Guillaume le décide : 2 images × 2 styles (8 crédits) puis 4 clips (~15 min de pod).

## 2026-08-22, 17 h 05 — S2V testé et concluant : la synchro se fait par Wan 2.2 S2V, un rendu par réplique

Décision de Guillaume de tester Wan 2.2 S2V malgré l'exclusion du lipsync par la bible. Résultat (audit lot 6) : sur les 8 rendus, la bouche du locuteur suit la voix, l'autre personnage reste silencieux, le style et le décor de l'image clé tiennent, ~1 min par réplique sur une RTX 5090. Méthode de dialogue retenue pour le pilote : **attente (I2V) → réplique 1 (S2V) → réplique 2 (S2V) → silence (I2V)**, chaque S2V rendu depuis l'image clé avec le mp3 de sa réplique, la voix posée à 0 s du sous-clip. Le recalage heuristique (`align_dialogue_audio.py`) devient inutile quand S2V est disponible. À entériner par Guillaume pour l'épisode, avec la mise à jour de la bible (« pas de synchronisation labiale » → « synchronisation par S2V sur les plans de dialogue »). Images 4a‑2 et 5‑2 reprises en A et B (briques amendées dans `build_prompts_pilote.py`).

## 2026-08-22, 18 h 30 — Dialogue : un clip par réplique, un seul personnage qui parle par clip ; S2V anime le mauvais visage

Diagnostic mesuré (audit lot 7) : l'audio était bien placé, mais **S2V fait parler le visage le plus visible**, pas le locuteur, dès qu'il y a deux personnages ou que le locuteur est de dos. Règle de Guillaume : **sur un plan à deux, chaque réplique est un clip où un seul personnage parle, qui parle du premier au dernier frame, et dont la durée est celle de la réplique** ; la voix démarre avec le clip ; pas besoin de contrechamp, et S2V devient superflu. Livré en deux variantes à comparer : v5 (I2V, un locuteur par clip, `build_clips_pilote.py --dialogue`, présence `talking_solo`) et v5b (S2V sur champ‑contrechamp, images P02a/P02b). Le S2V garde un intérêt si un plan ne montre qu'un seul visage (monologue, gros plan).

## 2026-08-22, 18 h 50 — Bug de montage trouvé par la mesure : sous-clips recalés périmés ramassés implicitement

La transcription horodatée du montage v5 A plaçait les répliques 0,5 à 1 s trop tard par rapport aux sous-clips v3. Cause : `montage_pilote.py` prenait d'office les sous-clips de `clips-runpod/_aligned/` (version v2 ré-échantillonnée par `align_dialogue_audio.py`) quand ils existaient, à la place des v3. Corrigé : le recalage ne s'applique que si `MONTAGE_ALIGNED=1` ; `_aligned/` renommé `_aligned_v2_obsolete/`. Montages v5 et v5b refaits : répliques à 20,86 / 22,48 / 31,16 / 34,72 s, soit 0,3 s après le début de chaque sous-clip de locuteur, comme prévu. Leçon : **un outil de montage ne doit jamais choisir une variante tout seul ; chaque source est explicite.** Analyse indépendante (agent Sonnet) des 69 images du v5 A en cours.

## 2026-08-23, 00 h 30 — Lot 8 vérifié par Sonnet : ce que l'image clé règle, ce qu'elle ne règle pas

Lot 8 (décidé par Guillaume « tout en un lot ») : clés P02/P03 **bouches fermées** (RÈGLE 31), cadrages 1a‑4 / 4a‑1 / 4a‑2 / 4b‑3 refaits pour ne plus se répéter, 4a‑2 à mi‑hauteur, 4b‑3 sans géants ni lettrage, 4a‑2 A couleurs nommées en positif (RÈGLE 30), 16 sous‑clips de dialogue rechaînés, montages v6 A/B, puis **vérification par `analyse_montage.py` (1 image/s + transcription horodatée) et deux agents Sonnet indépendants** (audit lot 8).

Acquis : attente et silence bouches fermées, audio à sa place, cadrages distincts, continuité d'altitude, plus de lettrage ni de géants. Non réglé : **l'auditeur ouvre la bouche pendant la réplique de l'autre** (les deux styles, P02 et P03), et sur P03 un des deux locuteurs est de dos (A : l'aide, B : Garnerin). Conclusion posée : **la consigne textuelle « l'autre garde la bouche fermée » n'est pas tenue par Wan 2.2 I2V dès qu'un visage est animé dans le cadre** ; l'image clé ne contrôle que l'état de repos. Trois issues soumises à Guillaume : compositing au montage (moitié d'image de l'auditeur prise dans le sous‑clip de silence ; recommandé pour le pilote), S2V en champ‑contrechamp (seule méthode qui anime la bonne bouche), ou accepter. Quoi qu'il soit choisi, les clés de dialogue doivent montrer **les deux visages** (P03 à recadrer).

Deux règles de méthode sortent du lot : (1) **on vérifie un montage par mesure** (images datées + transcription + relecteur indépendant qui ne connaît pas les noms de fichiers), pas à l'œil sur le lecteur — c'est ce qui a trouvé le bug de montage du 22 août et les bouches ouvertes ; (2) **le relecteur doit recevoir le scénario exact** : mon énoncé disait « P5 : le parachute s'ouvre » et « P1b : Garnerin dans la nacelle », d'où deux faux défauts (« climax absent », « P1b‑1 sans nacelle ») écartés à la main. Le relecteur A s'est aussi trompé sur f_023‑027 (« de dos ») : tout verdict d'agent se recontrôle sur la planche avant d'être rapporté.

Pour le choix du style : un relecteur extérieur lit les trois traitements de visage du style B (foule vierge, parieurs « rage comic », Garnerin rond) comme une incohérence ; c'est le parti pris de la fiche, mais c'est un signal. État : aucun pod actif ; Higgsfield 842,44 ; questions ouvertes inchangées (style A ou B, voix, S2V vs I2V vs compositing pour le dialogue).

## 2026-08-23, 01 h 30 — Recherche demandée par Guillaume : Wan 2.2 a une limite connue sur les bouches, MultiTalk/InfiniteTalk est le candidat

Guillaume : « les images avec dialogue c'est toujours pas ça », chercher les bonnes pratiques Wan 2.2 et un autre modèle testable sur RunPod. Résultat dans `docs/ETAT-DE-L-ART-dialogue-video.md` : (1) la bouche qui bouge malgré « mouth closed » est une **issue ouverte et sans réponse du dépôt Wan 2.2** (n° 77) — le texte n'est pas le levier ; (2) **Wan 2.2 S2V** n'a ni masque ni choix du locuteur (doc ComfyUI), ce qui explique le lot 7 ; (3) **MultiTalk / InfiniteTalk** (MeiGen, sur Wan 2.1 I2V 14B) lie chaque piste audio à un masque de visage, mode séquentiel `add`, cartoon revendiqué, nœuds Kijai dans ComfyUI, modèle de pod RunPod existant — c'est l'architecture qui répond à « un locuteur par clip, l'autre se tait » ; (4) LTX‑2.5 (22B, poids ouverts 11 août 2026, vidéo+audio en une passe, natif ComfyUI, RunPod) est un moteur alternatif crédible pour les plans sans dialogue, pas une réponse au plan à deux ; (5) deux bonnes pratiques Wan 2.2 à adopter : trois samplers (1er pas sans LoRA LightX2V) contre les plans figés, prompt vidéo de 25‑80 mots. Essais proposés E1 (InfiniteTalk sur P02/P03 A/B, ~2‑3 $), E2 (trois samplers), E3 (LTX‑2.5 sur deux plans) — en attente de Guillaume.

## 2026-08-23, nuit — Essais E1 à E4 : InfiniteTalk fait taire l'auditeur ; H3 tient le style mais pas le texte

Guillaume : « faisons les 3 tests », puis « ajoute un 4ᵉ test avec MiniMax H3 en I2V et R2V ». Détail dans l'audit (section « Essais E1 à E4 »). Ce qui est acquis : (1) **InfiniteTalk multi‑locuteurs** (Wan 2.1 + masques + pistes pré‑alignées) rend P02 A et B avec **le locuteur qui parle sur notre voix et l'auditeur bouche fermée**, en un seul rendu par plan — c'est la réponse technique à la règle « un locuteur par clip » que Wan 2.2 I2V n'obéissait pas ; **P03 A et B (clés v3, deux visages)** : premier rendu faux par ma faute (piste AIDE liée au masque de Garnerin : l'ordre des pistes doit suivre l'ordre des masques, pas la position à l'image) → refait avec les masques inversés ; résultat : l'aide (à droite) parle 2‑5 s bouche ouverte, Garnerin bouche fermée, puis Garnerin dit « Lâchez tout » 6‑7 s, l'aide bouche fermée, en A comme en B. **Défaut : sur P03 A une voiture moderne traverse le fond à partir de 4 s** (hallucination Wan 2.1 sur un fond de rue ; à bannir par la négative « car, vehicle, modern object ») ; P03 B : Garnerin porte une perruque blanche sur la clé v3 (dérive de la clé, pas du clip) ; (2) **trois samplers** : le premier pas sans LoRA à cfg 3,5 décale les couleurs, cfg 2,0 les garde ; gain de mouvement modeste ; (3) **LTX‑2.5 est gated** sur Hugging Face ; LTX‑2.3 a fait tomber ComfyUI au premier essai ; relancé en dernier dans la file, les deux clips (1a‑2 : 81 images, 4a‑3 : 105 images, 1280×704, 25 i/s) sont sortis en ~1 min chacun sans incident ; le style A tient, le ballon bouge (1a‑2 se soulève un peu trop, 4a‑3 monte et s'éloigne), LTX ajoute une piste sonore d'ambiance ; à comparer côte à côte dans `E3_ltx23_vs_wan22.mp4` ; (4) **MiniMax H3** tient le style A en I2V et R2V et génère des voix françaises, mais **réécrit les répliques** (phrase inventée en I2V, paraphrase en R2V) : bon moteur d'ambiance, pas un moteur de dialogue écrit. Leçons de méthode : un template ComfyUI à sous‑graphe se réécrit à la main au format API à partir de son dump ; les entrées « autogrow » s'écrivent `groupe.entree_N` ; après un crash de ComfyUI la file et l'historique sont perdus (resoumettre, retrouver les mp4 par `/view`) ; mettre les moteurs inconnus **en fin de file**. Décision attendue de Guillaume : quel moteur pour les dialogues (InfiniteTalk recommandé), garder ou non le premier pas sans LoRA (cfg 2,0), et s'il veut pousser H3 ou LTX.

## 2026-08-23, matin — Retours de Guillaume sur les essais E1 à E4

* E1 InfiniteTalk : la voiture de P03 A est vue ; **en style B les bouches ne sont pas vraiment alignées sur l'audio** (têtes inkman : bouche dessinée par le modèle, mouvement faible ou décalé) ; question de fond : **pourquoi Garnerin tient-il une « couverture » en disant « Lâchez tout »** — c'est le ballot de soie du parachute de la brique P03, mais à l'écran il se lit comme une couverture et l'action (vérifier la toile, la tendre à l'aide) ne porte pas la réplique (ordre de larguer). La brique P03 est à réécrire autour de l'action : Garnerin main sur la corde de largage / regard vers le haut, l'aide au rebord qui le supplie, la soie pliée seulement visible au fond.
* E2 : Guillaume confirme le verdict trois samplers (cfg 2,0, pas 3,5).
* E3 : « gated » = dépôt Hugging Face à accès restreint (compte HF + acceptation de la licence Lightricks + jeton de lecture) ; sans jeton les fichiers téléchargés sont des pages d'erreur de 126 octets. Un jeton HF dans le `.env` (HF_TOKEN) suffirait pour tester LTX‑2.5.
* E4 MiniMax H3 : **l'audio des dialogues a des parasites (mots qui n'existent pas)**, avec les voix générées comme avec nos mp3 en référence ; 4a‑3 et 1a‑2 ont un son propre **mais en anglais**. Hypothèse : H3 parle mal le français (données surtout anglais/chinois) et ne recopie pas une référence audio, il la resynthétise ; à vérifier par un P02 I2V avec les répliques en anglais (10 min de pod) avant d'écarter H3 pour les dialogues. Pour les plans muets, son audio se remplace par le nôtre au montage.

## 2026-08-23, après-midi — Deuxième série : P03 v4, InfiniteTalk propre, H3 bien prompté, modèles fermés

Acquis (détail dans l'audit, « Deuxième série ») : (1) **P03 réécrit autour de l'action** (corde de largage) dans le scénario, le plan de production, les briques et METHODE — la clé doit porter la réplique ; (2) **les bouches inkman se dessinent en trait** ; (3) InfiniteTalk sur P03 v4 A/B : locuteur/auditeur corrects, plus de voiture avec la négative anti‑anachronisme ; masques serrés sur les têtes + audio_scale 2 : les bouches inkman s'ouvrent nettement sur la réplique de chacun (le rond à 2‑3 s, le maigre à 4‑5 s) et restent fermées sinon ; c'est plus lisible que la v1 (masques tête+torse, audio_scale 1) — à confirmer à l'oreille sur E1b ; (4) **H3** : la langue et surtout la **syntaxe du skill officiel** (`<d>[French] …</d>`, (S1)/(S2)) suppriment les parasites ; reste une déformation sur « Dix francs » ; (5) **LTX‑2.5** : 1a‑2 et 4a‑3 propres (le ballon monte, la foule frémit, audio d'ambiance généré) ; P02 parlé : voix françaises générées, « Il va se tuer, je vous dis » exact puis « Dis Frank qu'il ne coupe pas la corde » (même déformation de « Dix francs » que H3), et **LTX ajoute une coupe** vers 6 s (contre‑plongée derrière les badauds) malgré « single continuous shot » ; ~1 min par clip sur A100, aucun crash cette fois ; (6) **modèles fermés** (Veo 3.1 Lite, Wan 2.7, Kling 3.0, Seedance 2.0 Mini, 12‑20 crédits le plan) : tous tiennent le style A et alternent les bouches ; Wan 2.7 et Seedance disent le texte exact, Veo presque, Kling déforme ; **aucun n'a pu prendre nos voix ElevenLabs** (Wan 2.7 : 1 seule référence ; Seedance : échec avec nos mp3 ; Veo/Kling : pas de référence audio). Conclusion provisoire pour l'épisode : **InfiniteTalk reste le seul procédé où la voix est la nôtre** ; les modèles fermés sont une option « voix générées » propre et rapide (Veo/Wan 2.7/Seedance) si on accepte de perdre le contrôle des voix. À trancher par Guillaume.

## 2026-08-23, fin d'après-midi — Verdict de Guillaume sur la deuxième série : InfiniteTalk abandonné, H3 et LTX‑2.5 retenus

Guillaume, après visionnage : **E4c (MiniMax H3 en français, prompt au format du skill officiel, en I2V comme en R2V avec nos voix en référence de timbre) est très bien** ; **E3b (LTX‑2.5 I2V avec l'audio généré par LTX) est très bien** ; **InfiniteTalk v4 n'est toujours pas bon : abandonné** ; les modèles fermés (Veo 3.1 Lite, Wan 2.7, Kling 3.0, Seedance Mini) sont bien aussi ; E4b (H3 anglais) est bien, avec en plus un mouvement de caméra. Conséquences : (1) la règle « pas de synchronisation labiale » de la bible tombe — les plans de dialogue seront générés **avec voix et bouche dans le même rendu** par un modèle omni‑modal (H3 en local, LTX‑2.5 en local, ou un modèle fermé), et **les voix ne sont plus nos mp3 ElevenLabs mais des voix générées (timbre référencé au mieux)** ; (2) `run_infinitetalk_runpod.py`, les masques et les pistes pré‑alignées restent dans le dépôt comme trace, sans suite ; (3) prochain chantier : choisir entre H3 et LTX‑2.5 (ou les deux selon les plans), régler « Dix francs » (épeler, ou écrire la réplique autrement), et refaire P02/P03 A/B pour un montage v7. Les prompts H3 s'écrivent désormais **toujours** au format du skill `h3-prompt-writing` (`integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music`, `<d>[French] …</d>`, locuteurs (S1)/(S2) décrits par timbre ; R2V en six sections avec `<Subject n>`, `<Picture n>`, `<Audio n>`).

## 2026-08-23, soir — Correction : « Dix francs » est bien prononcé (H3 E4c, LTX‑2.5 E3b) ; c'est la transcription qui se trompe

Guillaume, à l'oreille : « Dix francs » est correctement dit dans E4c et E3b. Les « Dis Franck / Dis‑toi » venaient de la **transcription ElevenLabs scribe_v1**, pas des modèles. Leçon : la transcription horodatée sert à **placer** les mots dans le temps et à repérer les phrases inventées ou manquantes, **pas à juger la prononciation d'un nombre ou d'un nom propre** ; pour ça, l'oreille humaine tranche. Le défaut « Dix francs » est clos ; aucune reformulation de réplique n'est nécessaire.

## 2026-08-23, soir — E7 : LTX‑2.5 remplace Wan 2.2 sur les plans muets (proposition) ; H3 hallucine sur les muets

Guillaume : « est‑il encore nécessaire de garder Wan 2.2 ? peut‑on tout basculer sur H3 ou LTX‑2.5 ? » → E7, 6 plans muets difficiles × A/B × {Wan 2.2, LTX‑2.5, H3}. Résultat (audit E7) : **LTX‑2.5 est propre sur les 12 clips** là où Wan 2.2 faisait surgir des personnages et où **H3 invente** (tête géante sur 4a‑1 B, débris sur 5‑2 A). Proposition : **tout le pilote sans Wan 2.2** — LTX‑2.5 pour les plans muets, H3 ou LTX‑2.5 pour les dialogues ; cadence 24 i/s ; audio d'ambiance généré par LTX conservé ou remplacé au montage ; le LoRA de style, s'il se fait, s'entraîne avec l'entraîneur officiel Lightricks. En attente du verdict de Guillaume sur la vidéo E7.

## 2026-08-23, soir — Voix cohérentes avec LTX‑2.5 : deux voies identifiées, E8 proposé

Guillaume : « LTX‑2.5 hallucine moins, H3 est plus créatif (parfois trop) ; comment avoir des voix cohérentes avec LTX‑2.5, peut‑être via LTXVSetAudioRefTokens ? ». Recherche (ETAT § 7) : (a) **IA2V « audio gelé »** — notre audio ElevenLabs encodé et gelé (`LTXVAudioVAEEncode` → `LTXVSetAudioRefTokens.frozen_audio` ou `SetLatentNoiseMask` à 0 → `LTXVConcatAVLatent` dans les deux passes, euler, CFG 1/1, pas de guidance de modalité) : les lèvres suivent **notre** voix — officiel sur 2.3, recette communautaire sur 2.5 en attendant le pipeline de doublage annoncé par Lightricks ; (b) **`LTXVReferenceAudio` + ID‑LoRA** (natif ComfyUI, poids 2.3 talkvid/celebvhq) : voix générée au timbre d'une référence de 5 s, stable entre clips. `LTXVSetAudioRefTokens` sert aujourd'hui surtout à geler l'audio ; son conditionnement « référence » ne marche pas encore sur 2.5. Proposition E8 : P02 A/B en IA2V gelé + P02 A en ID‑LoRA, contre le P02 d'E3b.

## 2026-08-23, soir — E8 : avec LTX‑2.5, nos voix ElevenLabs peuvent être gardées (IA2V audio gelé)

Résultat (audit E8) : l'**IA2V « audio gelé »** sur LTX‑2.5 (VAE audio → `SetLatentNoiseMask` à 0 → les deux passes, euler, CFG 1/1) rend P02 A/B et P03 A avec **la piste ElevenLabs telle quelle** et les lèvres qui suivent — voix verrouillées sans masques ni InfiniteTalk. `LTXVReferenceAudio` + ID‑LoRA marche aussi sur 2.5 (une voix générée par rendu, au timbre d'une référence). **`LTXVSetAudioRefTokens` n'est pas dans le cœur de ComfyUI** (paquet Lightricks) ; la voie native suffit. Défaut à régler avant le montage v7 : **LTX‑2.5 insère une coupe vers 5‑6 s sur P02** (4 rendus sur 5) — prompt sans enchaînement « then… then… », négative, ou plans de dialogue coupés en deux rendus. Décision attendue : après E8, le pilote peut se faire **entièrement en LTX‑2.5 avec les voix ElevenLabs gelées** (ou H3 pour les dialogues si Guillaume préfère sa créativité).

## 2026-08-23, soir — Retour E8 de Guillaume : l'intonation compte ; nos voix ElevenLabs sont plates

Guillaume : « la référence voix claire (ID‑LoRA) n'est pas en français ; les voix libres de LTX‑2.5 sont pas mal parce qu'il y a de l'intonation ; nos voix ElevenLabs n'ont pas trop d'intonation ». Conséquences : (1) l'ID‑LoRA peut dériver de langue (le rendu « claire » a parlé autre chose que français) — à forcer par la langue dans [SPEECH] et à vérifier à chaque rendu ; (2) le critère n'est pas seulement « voix verrouillée » mais **jeu** : les répliques ElevenLabs de juin (eleven_v3, réglages par défaut) sont trop neutres. Essai immédiat sans pod : les 4 répliques regénérées en **eleven_v3 mode créatif (stabilité 0) avec balises d'intention** (`[worried, muttering]`, `[scoffs, confident]`, `[pleading, urgent]`, `[calm, firm, commanding]`) — `pilote/essais/E8/audio/expressif/` — envoyées à Guillaume pour comparaison à l'oreille. Deux voies restent ouvertes selon son verdict : **voix ElevenLabs expressives + IA2V gelé** (identité garantie, jeu à doser par les balises) ou **voix libres LTX‑2.5 / H3** (jeu naturel, identité à tenir par ID‑LoRA ou timbre référencé, langue à surveiller).

## 2026-08-23, soir — Retour sur les voix ElevenLabs « expressives » : intonations pas justes, rendu « studio » avec écho

Guillaume : « je ne suis pas sûr que les intonations soient les bonnes, les voix font très studio avec de l'écho ». Le mode créatif v3 (stabilité 0 + balises) ajoute du jeu mais aussi une acoustique de studio/réverbération étrangère à un parc plein de monde. Variante « naturel » (stabilité 0,5, sans balise, sans speaker boost) générée dans `essais/E8/audio/naturel/` pour comparaison. Observation de fond à retenir : **les voix générées dans la vidéo (LTX‑2.5 « voix libres », H3) sont placées dans l'acoustique de la scène** — extérieur, foule, distance — alors qu'une voix ElevenLabs est un enregistrement de studio qu'il faudrait ensuite « mettre dans la pièce » au montage (réverbération, filtrage). C'est un argument réel en faveur des voix libres, à peser contre la tenue de l'identité vocale. Décision de Guillaume attendue : voix libres (LTX‑2.5/H3, identité par ID‑LoRA ou timbre référencé, langue à surveiller) ou ElevenLabs (réglage à trouver + traitement de scène au montage).

## 2026-08-24 — Montage v7 livré en cinq styles ; règle : citer les répliques dans le prompt

v7 rendu entièrement en **LTX‑2.5, voix libres** (styles A, B, D, J, K — D/J/K repris du travail d'une autre session, P5 corrigé partout : **le bras vient de l'intérieur de la nacelle**, briques + fiche mises à jour). Leçon : décrire le dialogue sans le citer fait inventer un charabia — **les répliques exactes se citent entre guillemets dans le prompt vidéo** (règle ajoutée à la stratégie). Les cinq montages disent les quatre répliques mot pour mot (transcription + oreille). En attente : verdict de Guillaume sur les cinq styles.
