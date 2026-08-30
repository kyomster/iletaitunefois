# CLAUDE.md — le standard de ce dépôt

Ce dépôt est la bible de fabrication d'une série animée générée par IA (*Il était une fois — Les Découvreurs*, saison 1, style P). Tout est local, dans git : pas de serveur, pas de MCP de vérité. Ce fichier dit comment on y travaille ; il s'applique à toute session, humaine ou agent.

## 1. Où est la vérité

1. **La couche de données** : `iletaitunefois/S01E01/donnees/*.json` (plans, répliques, décors, faits, personnages, continuité, assets, contrats, attendus, décisions, état) et `atelier/regles/regles.json`. Chaque objet a une **adresse** (`S01E01/plan-2`, `S01E01/plan-2/ligne-0`, `fait/1.16`, `perso/garnerin`, `asset/clip-P02`, `continuite/ballon`, `regle/36`, `decision/…`), un **statut** et une **empreinte**. Les styles sont dans `styles/*/style.json`.
2. **Les documents générés** — `scenario.md`, `plan-de-production.md`, `son-et-voix.md` — sortent de `python atelier/scripts/rendre.py`. **On ne les édite jamais à la main.** Une correction passe par le JSON, puis `rendre.py`, puis `doctor.py`, puis un commit.
3. **Les documents rédigés** (méthode, stratégie, guide, bible, audit, décisions) restent du markdown écrit à la main : ils expliquent, ils ne détiennent pas.
4. **Ma mémoire persistante** (`~/.claude/projects/…/memory/`) ne garde que les façons de travailler et les préférences de Guillaume, jamais un fait de la série.

Hiérarchie en cas de doute : données > documents générés > documents rédigés > mémoire. Ce qui n'est pas dans les données n'est pas établi : une donnée absente reste nulle et se signale, elle ne se complète pas de mémoire.

## 2. Les statuts, et qui les pose

| Statut | Sens | Qui |
|---|---|---|
| `propose` | écrit par l'agent, pas encore validé | l'agent |
| `valide` | Guillaume a dit oui, `valide_par` et `valide_le` renseignés | l'agent, **sur le mot de Guillaume** |
| `verrouille` | zone verrouillée (texte dit, style retenu, moteur retenu) : ne change que sur décision datée dans `decisions.json` | idem |
| `ecarte` | on ne reprend pas, le motif est écrit | idem |

Modifier un objet `valide` ou `verrouille` sans décision fait échouer `doctor.py` (`VERROU_ROMPU`, `PLAN_VALIDE_MODIFIE`). La marche : consigner la décision (date, qui, pourquoi), modifier, re-valider avec `donnees.valider`, régénérer, committer.

## 3. La boucle d'une session

```
SessionStart   → python atelier/scripts/contexte.py   (hook automatique : état, doctor, prochaine action, « à ne pas retenter »)
avant d'agir   → lire l'adresse concernée dans le JSON, pas le markdown
écrire         → JSON → rendre.py → doctor.py
commit         → un commit par changement cohérent ; le hook refuse si les documents ne sont pas régénérés ou si doctor a un BLOQUANT
fin de session → mettre à jour donnees/etat.json (où on en est, ce qui est ouvert, la prochaine étape)
```

`contexte.py --next` rend **une** action ; quand il dit « rien », il n'y a rien à faire — on n'invente pas de tâche. Un refus de `doctor.py` se corrige dans la donnée, jamais en contournant le contrôle.

## 4. Les règles de fabrication qui ne se discutent pas

* Un bloc de style, une brique, une garde **se copient, ne se reformulent pas** ; un prompt corrigé se réécrit en entier (RÈGLE 13).
* **La référence impose sa mise en page** ; une planche se regarde avant d'en dériver quoi que ce soit ; un élément de continuité a **une planche réinjectée**, pas une description (RÈGLES 1, 14, 36).
* Un prompt de dialogue **cite la réplique à l'octet** entre guillemets, avec langue et timbre ; l'asset garde l'empreinte de ce qu'il cite, et se périme quand ça change.
* Le texte dit est zone verrouillée ; les durées et l'ordre des plans aussi. Le scénario gagne sur la technique.
* Les 42 règles d'images (`atelier/METHODE-generation-images.md`, `atelier/regles/regles.json`) et les moteurs écartés (`ne_pas_retenter`) s'appliquent avant toute génération.
* Pas d'appel Higgsfield pendant une phase de plan ; tout pod RunPod est éteint en fin de session et `runpod.py list` est vide ; les sorties passent par S3 et sont supprimées du volume après rapatriement.

## 5. Secrets et périmètre

`.env` à la racine (`ELEVEN_LABS`, `RUN_POD`, `RUN_POD_S3_*`, `HUGGING_FACE`) : jamais affiché, jamais commité, jamais dans un JSON. Le dossier de travail `C:\Users\kyoms\Downloads\EpisodeModernise` garde le brut et les mp4 ; le dépôt garde ce qui est validé. Les fichiers lourds (clips, montages) ne sont pas dans git : les assets pointent vers eux.

## 6. Repères

* Écrire un épisode : `ecriture/METHODE-ecriture.md` ; la série : `iletaitunefois/serie/BIBLE-Les-Decouvreurs.md` ; le corpus source : `iletaitunefois/fiches_verifie/` (la fiche **et son audit**, à la dernière passe).
* Préparer une séquence : `atelier/GUIDE-preparation-episode.md` ; images : `atelier/METHODE-generation-images.md` ; vidéo et son : `atelier/STRATEGIE-video.md` ; rendu : `atelier/RUNPOD.md`.
* Scripts : `atelier/scripts/` — `donnees.py` (la couche), `rendre.py`, `doctor.py`, `contexte.py`, `assembler_*.py` (prompts), `run_ltx25_runpod.py`, `runpod.py`, `runpod_s3.py`, `analyse_montage.py`.
