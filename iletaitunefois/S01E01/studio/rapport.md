# Rapport d'import Studio — 2026-08-29

Dépôt `b490f92` ; dry-run : False ; plans : tous ; étapes : structure, format, styles, bible, apprentissages, decisions, locuteurs, lieux, plans, repliques, faits, contrats, prose

## doctor

```
{
 "cible": {
  "show": "il-etait-une-fois",
  "episode": "S01E01"
 },
 "defaillances": [
  {
   "code": "CONT_PROMESSE_TEASER_ATTENTE_EPISODE",
   "famille": "CONTINUITE",
   "severite": "ATTENTION",
   "rang": 7,
   "adresse": {
    "show": "il-etait-une-fois",
    "episode": "S01E01",
    "plan": 79,
    "cle": "teaser-flacon"
   },
   "message": "il-etait-une-fois · S01E01 plan 79 · « teaser-flacon » : l'épisode suivant n'existe pas encore. Le paiement sera exigé dès sa création.",
   "reparation": {
    "verbe": "créer",
    "cible": "l'épisode suivant",
    "outil": "create_episode"
   },
   "empreinte": "32b740cdc3f2faa0"
  }
 ],
 "prochainesEtapes": [],
 "resume": {
  "bloquant": 0,
  "erreur": 0,
  "attention": 1,
  "parFamille": {
   "CONTINUITE": 1
  }
 },
 "controlesExecutes": [
  "continuite",
  "faits",
  "voix",
  "comptages",
  "prose:preseance",
  "prose:licences",
  "sessions",
  "acces",
  "executions",
  "opportunites"
 ],
 "relecturesHumaines": []
}
```

## Notes

- check après `structure` : rien
- format : `ratioAnimeMax`, `blocAnimeMaxSec`, `image`, `refsMaxParPrompt` sont conservés par Studio mais lus par aucune règle (à rapporter à l'auteur du serveur).
- check après `format` : rien
- styles : `formulaEn` = bloc `scene` du style.json, `sceneBlockEn` = bloc `personnage` ; verrouillés dès la création par Studio.
- check après `styles` : rien
- bible : aucune entrée `enforceable` (le serveur refuse une règle exécutable sans fonction) ; `decoupage.bloc.dureeMax` non exécutable car la règle serveur teste la durée du plan, pas des blocs.
- check après `bible` : rien
- check après `apprentissages` : rien
- décisions : `record_decision` n'a aucune lecture côté serveur ; le dédoublonnage repose sur journal.jsonl seulement.
- check après `decisions` : rien
- check après `locuteurs` : rien
- lieu D3 : époque non chiffrée (texte libre : « Pièce du cadre, couleurs saturées, fin de journée. »)
- lieu D4 : époque non chiffrée (texte libre : « Récit d'époque désaturé, Chine des Tang. Deux vignettes (décor D4). »)
- lieu D5 : époque non chiffrée (texte libre : « Récit, montage nature en trois vignettes, pleine lumière. »)
- lieu D6 : époque non chiffrée (texte libre : « Récit, préhistoire, nuit et pénombre, silhouettes. »)
- lieu D7 : époque non chiffrée (texte libre : « Récit, grand montage. »)
- lieu D8 : époque non chiffrée (texte libre : « Récit, champs des Royaumes combattants, vent, lumière franche. »)
- lieu D9 : époque non chiffrée (texte libre : « Gel : brasserie antique figée. »)
- lieu D10 : époque non chiffrée (texte libre : « Récit, route antique, jour. »)
- lieu D11 : époque non chiffrée (texte libre : « Récit, cour de ferme han, jour. »)
- lieu D12 : époque non chiffrée (texte libre : « Récit, cour antique, jour. Gag en deux temps. »)
- lieu D13 : époque non chiffrée (texte libre : « Récit, steppe, lumière dorée, poussière. »)
- lieu D14 : époque non chiffrée (texte libre : « Récit, montage en quatre vignettes techniques, fonds sobres. »)
- lieu D15 : époque non chiffrée (texte libre : « Récit, Sichuan, IIᵉ siècle avant notre ère, jour voilé. ») — plan 36, LIEU · Sichuan, IIe siècle avant notre ère — à saisir : -200 / -101, SIECLE
- lieu D16 : époque non chiffrée (texte libre : « Récit, vergers d'agrumes du sud, 304, jour clair. ») — plan 38, LIEU · vergers, 304 — à saisir : 304 / 304, ANNEE
- lieu D17 : époque non chiffrée (texte libre : « Récit muet, fleuve Jaune en crue, vers 1060, ciel chargé. Le plus long ANIMÉ de l'épisode : 32 s, séquence en cinq temps. ») — plan 39, LIEU · fleuve Jaune, vers 1060 — à saisir : 1060 / 1069, DECENNIE
- lieu D18 : époque non chiffrée (texte libre : « Récit, colline venteuse, Vᵉ siècle avant notre ère, jour venté. ») — plan 41, LIEU · colline, Ve siècle avant notre ère — à saisir : -500 / -401, SIECLE
- lieu D19 : époque non chiffrée (texte libre : « Récit, remparts de Taicheng assiégés, 549, jour gris de siège. ») — plan 42, LIEU · Taicheng, 549 — à saisir : 549 / 549, ANNEE
- lieu D20 : époque non chiffrée (texte libre : « Récit, Ye, 559, jour blafard. ») — plan 44, LIEU · Ye, 559 — à saisir : 559 / 559, ANNEE
- lieu D21 : époque non chiffrée (texte libre : « Récit, gorge du Sichuan, Iᵉʳ siècle, jour, brume de fond de gorge. ») — plan 50, LIEU · gorge du Sichuan, Ier siècle — à saisir : 1 / 100, SIECLE
- lieu D22 : époque non chiffrée (texte libre : « Gel. »)
- lieu D23 : époque non chiffrée (texte libre : « Gel. »)
- lieu D24 : époque non chiffrée (texte libre : « Récit, Chine légendaire, NUIT, un grenier en flammes. »)
- lieu D25 : époque non chiffrée (texte libre : « Récit, Chine des Song, NUIT, toit d'une tour. »)
- lieu D26 : époque non chiffrée (texte libre : « Récit, Montpellier, 1783, jour. Deux temps plus une chute d'image. ») — plan 60, LIEU · Montpellier, 1783 — à saisir : 1783 / 1783, ANNEE
- lieu D27 : époque non chiffrée (texte libre : « Récit, chemin de ronde d'un rempart, jour. »)
- lieu D28 : époque non chiffrée (texte libre : « Récit, ruelle des Song, tombée du jour. »)
- lieu D29 : époque non chiffrée (texte libre : « Récit, montage en trois vignettes. »)
- lieu D30 : époque non chiffrée (texte libre : « Récit, deux temps. »)
- lieu D31 : époque non chiffrée (texte libre : « Récit, cave d'alchimistes, nuit, lueurs de fourneaux. »)
- lieu D32 : époque non chiffrée (texte libre : « Récit, un ciel de nouvel an qui devient champ de bataille. »)
- lieu D33 : époque non chiffrée (texte libre : « Surimpression, hors registre : le pont entre époque et présent. »)
- check après `lieux` : rien
- check après `plans` : rien
- check après `repliques` : rien
- fait 1.1 : exclu — Remarque de cadrage sur l'inventaire de Needham/Temple, pas un fait ponctuel : reste en note de l'audit.
- fait 1.25 : renvoi (sans source), non importé
- fait 1.26 : renvoi (3), non importé
- fait 1.27 : renvoi (5), non importé
- fait 1.28 : renvoi (7), non importé
- fait 1.29 : renvoi (8), non importé
- fait 1.30 : renvoi (9), non importé
- fait 1.31 : renvoi (13), non importé
- fait 1.32 : renvoi (14), non importé
- fait 1.33 : renvoi (15), non importé
- fait 1.34 : renvoi (16), non importé
- fait 1.35 : renvoi (17), non importé
- fait 1.36 : renvoi (18), non importé
- fait 1.37 : renvoi (20), non importé
- fait 1.38 : renvoi (21), non importé
- fait 1.39 : renvoi (22 et 23), non importé
- fait 1.40 : renvoi (sans source), non importé
- fait 1.41 : renvoi (sans source), non importé
- fait 1.42 : renvoi (sans source), non importé
- fait 1.43 : renvoi (sans source), non importé
- fait 1.45 : renvoi (sans source), non importé
- fait 1.46 : renvoi (sans source), non importé
- fait 1.47 : renvoi (sans source), non importé
- fait 1.48 : exclu — Date « 27 janvier 1894 » issue d'un blog de brevets, source proscrite ; remplacée par la correction 2.55 (27 juin 1894).
- fait 1.49 : renvoi (sans source), non importé
- fait 1.50 : renvoi (sans source), non importé
- fait 1.51 : renvoi (sans source), non importé
- fait 2.54 : renvoi (sans source), non importé
- check après `faits` : rien
- contrats : Au plan 34, la réplique verrouillée de Sam dit « je range... l'étrier dans la sacoche » alors que l'étrier n'est pas l'un des neuf objets et que le fer d'attelage est déjà rangé au 29. Traitement retenu en attendant l'arbitrage : rien ne quitte la table au plan 34. À porter en session ARBITRAGE.
- contrats : l'échelle CONVICTION d'Elio est une proposition non validée, non envoyée (contrats.json → propositions)
- check après `contrats` : rien
- prose : échantillons de voix pris dans la prose validée de S01E01 (hypothèse : le serveur attend « votre propre écriture » ; à remplacer par des textes de Guillaume s'il en a)
- check après `prose` : rien
