# Il était une fois — *Les Découvreurs*

Le programme est **« Il était une fois », version 2026** ; sa **saison 1 est *Les Découvreurs*** (26 épisodes du corpus d'origine), en style **P, anime TV moderne** (choix du 29 août 2026). Depuis le 29 août, la vérité de la série (plans, répliques, faits, bible, contrats, décisions) est détenue par **Studio**, le serveur MCP (`atelier/STUDIO.md`) ; ce dossier garde ce que Studio ne modélise pas encore et le corpus source.

```
iletaitunefois/
  fiches_verifie/                 LE CORPUS : 208 fiches d'épisode des six séries d'origine, vérifiées et sourcées (audits dans _audit/)
  serie/
    BIBLE-Les-Decouvreurs.md      comment la série raconte : gabarits, dispositif de vérification, cast, toujours/jamais
    CHARTE-prose.md               la charte du roman en prose
    troupe-recurrente.md          Sam, Naya, Elio : fiches, marqueurs, couleurs réservées
    troupe-prompts-styles-ABC.md  les prompts de la troupe en A, B, C — à refaire en P
  S01E01/                         le pilote : Garnerin, le parachute, le pari
    scenario.md                   les 80 plans, le minutage, les 14 gags — zone verrouillée
    plan-de-production.md         diagnostic, roster, tableau révisé, prompts de la première séquence
    logique-ouverture-froide.md   la chaîne physique de la scène d'ouverture et qui fait quoi
    son-et-voix.md                casting des voix, plages musicales, effets, mutualisations
    prompts/
      briques_pilote.py           les briques des plans 1 à 6 : plans, références, identités, clauses, clips
      clips-StyleP.json           les 18 prompts de clips exactement rendus, avec graines
      assets-et-objets.md         décors, assets partagés et §7 descriptions canoniques des objets de continuité
      personnages-episode.md      les personnages d'époque et leurs blocs identité
    assets/
      references/                 les 7 planches P réinjectées (D01, D02, Foule, Garnerin, Parieurs, Ballon, Nacelle)
      cles/                       les 18 images clés P, dernières versions
      partages/                   assets partagés (plaque La Loubère)
    pilote/
      AUDIT.md                    état du pilote, ce que chaque passe a appris, ce qui reste
      DECISIONS.md                les décisions en vigueur et celles qu'elles ont remplacées
      identifiants.md             media_id et job_id Higgsfield
    novelcrafter/                 le roman en prose, le manuscrit technique, le codex
    studio/                       import Studio : contrats.json, lieux.json, faits.json (saisies), journal.jsonl, rapport.md
```

## Où en est S01E01

* **Pilote (plans 1 à 6)** : livré en style P, 62,8 s, vérifié plan par plan. Restes : cadrage de 1b-3 et 4b-2, huit objets à arbitrer, voix sur la longueur. Voir `S01E01/pilote/AUDIT.md`.
* **Scénario révisé le 29 août 2026** d'après l'audit du corpus (cognac, système décimal, Baden-Powell et Lilienthal au plan 48) : **80 plans, 21 min 59**, 107 répliques, 92 mots/min ; 54 blocs ANIMÉ (476 s, 36,1 %), 48 FIXE, 8 POST. La prose Novelcrafter n'a pas encore son chapitre 48.
* **Studio** : S01E01 importé (structure, format, 17 styles, bible, 61 apprentissages, 27 décisions, 16 locuteurs, 34 décors, 80 plans, 107 répliques, 40 faits sourcés reliés à leurs plans, contrats de continuité, règles de prose). Plans 7 à 80 à préparer avec `atelier/GUIDE-preparation-episode.md` et la boucle `next()` de Studio.
* **Troupe** : Sam, Elio et Naya à générer en style P avant la première séquence de cadre (plan 7).

## Comment on continue

1. `atelier/GUIDE-preparation-episode.md` pour la séquence suivante : chaîne physique, inventaire de continuité, descriptions canoniques, cadrages.
2. Les briques de la séquence dans un module à côté de `briques_pilote.py`.
3. Planches → clés → clips → montage vérifié, avec les scripts de `atelier/scripts/`.
4. Tout ce qui est appris s'écrit ici (série) ou dans `atelier/` (générique) au moment où c'est acquis.

Le dossier de travail (brut, suivi, mp4) est `C:\Users\kyoms\Downloads\EpisodeModernise\pilote\`.
