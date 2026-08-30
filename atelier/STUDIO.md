# Studio — travailler avec le socle qui détient la vérité

Depuis le 29 août 2026, la création est assistée par **Studio**, un serveur MCP qui détient la vérité des séries (programmes, saisons, épisodes, plans, répliques, faits, bible, apprentissages, styles, contrats de continuité, décisions, sessions de validation). Son contrat pour un agent est `C:\Users\kyoms\Desktop\EpisodeMerdenizeApp\docs\MCP-contrat-agent.md` ; ce document dit comment **nous** l'utilisons et ce qui reste dans le dépôt.

## Ce qui vit où

| Studio détient (la base fait foi) | Le dépôt garde (tant que les outils C n'existent pas) |
|---|---|
| programme « Il était une fois », saison 1 « Les Découvreurs », S01E01 | les planches de référence, les clés, les clips, les graphes ComfyUI, les scripts |
| le format effectif (durée, débit, registres, `voiceMode`, bloc vidéo) | les exemples de chaque style (`styles/*/exemples/`) — le `style.json` est importé |
| les 80 plans, 107 répliques, décors, locuteurs | les briques de prompts (`S01E01/prompts/briques_pilote.py`), les prompts rendus |
| les faits sourcés (audit du corpus) et leurs liens aux plans | le corpus `iletaitunefois/fiches_verifie/` lui-même |
| la bible, la méthode d'écriture, les 42 règles d'images, les verdicts moteurs | les documents longs (`METHODE-generation-images.md`, `STRATEGIE-video.md`, `GUIDE`) |
| les contrats de continuité (beats, promesses, questions, états) | l'audit et les décisions du pilote sous leur forme rédigée |
| les décisions, les sessions de validation | le dossier de travail (`Downloads\EpisodeModernise`) |

Une donnée qui est dans Studio se corrige **dans Studio** (par un outil, ou par une session si elle est verrouillée), puis le dépôt se remet en accord. Le dépôt n'est plus la source de ce que Studio modélise.

## Se connecter

* Claude Code : le serveur `studio` est enregistré en configuration utilisateur (`claude mcp list`) ; les outils s'appellent `mcp__studio__<nom>`.
* Scripts : `atelier/scripts/studio_client.py` (jeton `MCP_TOKEN` dans le `.env`, jamais affiché). `python studio_client.py ping` vérifie la connexion ; `call <outil> '<json>'` fait un appel.

## La boucle de travail

```
get_context(show, episode?)   ce qu'il faut savoir avant d'agir : bible, apprentissages (dont « à ne pas retenter »), styles, format
get_format(show, season?)     avant tout calcul de cadrage — jamais une valeur supposée
next(show)                    UNE action, avec son outil et ses arguments
[l'outil]
check(show, episode?)         ce que l'écriture a produit comme alertes
```

Rien n'est complété de mémoire : une donnée absente reste nulle et sort dans un rapport. Un refus porte un motif et ne se contourne pas ; on corrige la donnée ou on ouvre une session et on attend Guillaume. Une session que l'agent ouvre n'approuve rien tant qu'un humain ne l'a pas close.

## L'import du dépôt

`atelier/scripts/studio_import.py`, par étapes ordonnées : structure → format → styles → bible → apprentissages → decisions → locuteurs → lieux → plans → repliques → faits → contrats → prose. `--dry-run` écrit les appels prévus dans `iletaitunefois/S01E01/studio/dry-run/` ; les écritures réelles vont dans `journal.jsonl` (empreinte des arguments, `_commit`) et un appel déjà journalisé n'est pas rejoué ; `rapport.md` liste ce qui est resté nul et les alertes de `check`. Les parseurs sont dans `studio_sources.py` (`--verifier` recoupe scénario et tableau révisé). Les saisies humaines sont dans `studio/contrats.json`, `studio/lieux.json`, `studio/faits.json`.

## Correspondance dépôt → Studio

| Dépôt | Outil | Remarques |
|---|---|---|
| `styles/*/style.json` | `upsert_style` | `formulaEn` = bloc `scene`, `sceneBlockEn` = bloc `personnage`, `eraTreatment` = `epoque`, `negativeBase` = les trois négatives ; **verrouillé dès la création** |
| `serie/BIBLE-Les-Decouvreurs.md`, `ecriture/METHODE-ecriture.md` | `upsert_bible_entry` | jamais `enforceable` (refusé sans fonction serveur) |
| `atelier/METHODE-generation-images.md` (42 règles), `STRATEGIE-video.md` §4, `moteurs-ecartes/VERDICTS.md` | `upsert_learning` | `number` = numéro de règle, `doNotRetry` pour Wan 2.2 dialogues, S2V, InfiniteTalk, LTX-2.3 |
| `S01E01/pilote/DECISIONS.md` | `record_decision` | aucune lecture côté serveur : dédoublonnage par le journal |
| `S01E01/son-et-voix.md` §1 | `upsert_speaker` | voix off = même locuteur, `voiceOff` sur la réplique |
| `S01E01/plan-de-production.md` §3 + `studio/lieux.json` | `upsert_location` | années seulement saisies |
| `S01E01/plan-de-production.md` §4 + `scenario.md` | `upsert_plan` | `kind` ANIME sans accent ; blocs a/b/c dans `boardNote` (pas d'outil `AnimBlock`) |
| `scenario.md`, texte dit | `upsert_line` | à la ponctuation près ; `lock_line` exige une session SIGNATURE_VERROUILLAGE close |
| `fiches_verifie/_audit/…/S01E01….audit.md` | `upsert_fact`, `link_fact` | un fait par ligne de correction ; ❌ = un fait ECARTE + un fait VERIFIE |
| `studio/contrats.json` | beats, promesses, questions, échelles, états, emplois | saisis, jamais extraits |
| `serie/CHARTE-prose.md` | `upsert_prose_rule`, `upsert_voice_sample` | motifs de jugement avec `detector: null` |

## Pièges vérifiés dans le code du serveur

* Une clé inconnue d'un appel est ignorée en silence (Zod) : ne jamais compter sur un champ non listé par `tools/list`.
* `upsert_style`, `upsert_bible_entry`, `set_format`, `upsert_learning`, `upsert_state_*`, `upsert_fact`, `record_decision` **créent** à chaque appel (version +1 ou doublon) : lire avant d'écrire.
* Clés de format lues par les règles : `langue`, `scoreProseMax`, `dureeEpisodeSec` (0 = contrôle off), `dureeEpisodeToleranceSec`, `debitMotsParMinuteMin/Max`, `budgetMotsTolerance`, `registres`, `voiceMode`, `video{}`. Les autres sont conservées mais sans effet.
* `set_promesse_paiement` : `portee` vaut SERIE par défaut — passer `portee:"EPISODE", porteeEpisode`.
* `speech_check` signale, ne bloque pas ; « Dix francs » lu « Dis Franck » est un artefact de transcription connu.
* Codes `check` normaux pendant un import partiel : `CONT_QUESTION_OUVERTURE_SANS_REPONSE` (avant la réponse), `CONT_PROMESSE_NON_PAYEE` ; résiduel permanent : `CONT_PROMESSE_TEASER_ATTENTE_EPISODE`.

## Seconde vague (30 août 2026) — les outils de l'Amendement C sont livrés

115 outils. `atelier/scripts/studio_import_prod.py` a versé, dans cet ordre : **moteurs** (`upsert_engine` : Nano Banana Pro et LTX-2.5 deux passes RETENUS avec le graphe verbatim ; audio gelé, voix référencée, MiniMax H3 CANDIDATS ; Wan 2.2 I2V/FLF2V/S2V, InfiniteTalk, LTX-2.3, API fermées ÉCARTÉS avec leur motif) ; **personnages** (Sam, Naya, Elio à la portée SHOW avec fiche canon par famille de style — `_defaut`, `inkman`, `cel-2d`, `realiste`, `aplats` — et 21 personnages d'épisode, historiques liés à leur fait, crédités aux plans, locuteurs rattachés) ; **continuité visuelle** (21 éléments, planches Ballon et Nacelle rattachées ; couteau et parachute sans planche : `prepare_batch` refusera les plans 1 à 6 tant qu'elles n'existent pas) ; **assets** (7 planches, 20 clés, 18 clips en style P avec leur prompt tel qu'envoyé, leurs références réinjectées et, pour P02/P03, les répliques citées par leur adresse `S01E01/plan-2/ligne-0`) ; **attendus** des plans 1 à 6 ; **voix** (les deux voix ElevenLabs de référence) ; **musique et effets** ; **épreuve comparative** du pilote, avec une session CHOIX_STYLE à clore pour `close_trial`.

Toujours dans le dépôt : les fichiers eux-mêmes (planches, clés, clips, montages) tant qu'un lot n'a pas été préparé pour les archiver par `store_media_*` ; la saisie des attendus des plans 7 à 80 ; le casting des huit voix ; les planches du couteau et du parachute.

Manques constatés côté serveur : pas d'`unlink_fact` (un lien fait → plan erroné ne se retire pas), les réponses de `upsert_sfx_cue` et `upsert_character` ne rendent pas l'identifiant sous une clé stable (on relit les listes).
