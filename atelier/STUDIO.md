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

## Pas encore appelable (nos objets de l'Amendement C)

Médias et stockage, lots de production, chaîne de rendu (`Engine`, transcription, `speech_check`), continuité visuelle (`upsert_continuity_item`, `upsert_plan_expectation`), troupe en cascade, chaîne son. Jusqu'à leur arrivée, le dépôt reste la vérité pour les planches, les clés, les clips, les graphes et les voix ; `atelier/studio/SPEC-studio-v7-amendement-C.md` dit ce qu'on attend.
