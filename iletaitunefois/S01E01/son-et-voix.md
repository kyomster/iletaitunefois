# S01E01 — le son : voix, musique, effets

Ce qui est propre à l'épisode. La chaîne (LTX-2.5 voix libres, Eleven Music, Eleven SFX, montage, vérification) est dans `atelier/STRATEGIE-video.md` ; les décisions dans `pilote/DECISIONS.md`. Comptages du 29 août 2026 sur le scénario révisé (80 plans, 21 min 59).

---

## 1. Ce qu'il y a à dire

2 031 mots entre guillemets, tous attribués (comptage par blancs, celui de Studio) ; environ 11 200 caractères ; débit moyen 92.4 mots par minute, dans la fourchette 85 à 95 de la méthode.

| Locuteur | Répliques | Mots | Part | Plans |
|---|---|---|---|---|
| **SAM** | 62, dont **31 en voix off** | 1 577 | 77,6 % | 61 plans |
| **ELIO** | 18, dont **1 en voix off** | 209 | 10,3 % | 18 plans |
| **NAYA** | 11 | 103 | 5,1 % | 11 plans |
| LE BADAUD | 2 | 17 | 0,8 % | 51 |
| BADAUD 1 | 2 | 16 | 0,8 % | 2, 64 |
| LE GÉNÉRAL | 1 | 16 | 0,8 % | 67 |
| COMPÈRE 1 | 1 | 16 | 0,8 % | 68 |
| PAYSAN 2 | 1 | 14 | 0,7 % | 22 |
| PILLARD 1 | 1 | 13 | 0,6 % | 56 |
| BADAUD 2 | 2 | 11 | 0,5 % | 2, 64 |
| LA SENTINELLE | 1 | 11 | 0,5 % | 67 |
| PAYSAN 1 | 1 | 10 | 0,5 % | 22 |
| L'AIDE | 1 | 7 | 0,3 % | 3 |
| PILLARD 2 | 1 | 6 | 0,3 % | 56 |
| L'AUTRE | 1 | 3 | 0,1 % | 51 |
| GARNERIN | 1 | 2 | 0,1 % | 3 |
| **Total** | **107** | **2 031** | | **16 locuteurs** |

**33 plans font dialoguer deux locuteurs ou plus**, dont deux à trois voix : 64 et 67. Didascalies du texte verrouillé, à respecter : `(voix off)` et `(off)` pour Sam et Elio, `(en écrivant)` et `(lisant)` pour Naya, `(tendant la main)` et `(payant)` pour les badauds du plan 64.

---

## 2. Le casting — huit voix

Deux timbres d'appoint suffiraient à éviter les collisions dans un plan (aucun plan ne fait dialoguer plus de deux figures d'époque), mais sur 21 minutes les mêmes deux timbres joueraient treize figures dans sept scènes : le spectateur l'entend. Le coût d'un timbre de plus est nul (722 caractères pour les treize figures) ; **huit voix** est le point d'équilibre. Vérifié par script : dans aucun plan deux personnages ne partagent la même voix.

| Voix | Personnages | Répl. | Caractères | Plans |
|---|---|---|---|---|
| **V1 Sam** | Sam | 62, dont 31 en voix off | 8 820 | 61 plans |
| **V2 Elio** | Elio | 18 | 1 053 | 7, 11, 14, 15, 18, 24, 25, 27, 33, 34, 35, 52, 53, 58, 65, 70, 73, 78 |
| **V3 Naya** | Naya | 11 | 513 | 7, 10, 14, 20, 40, 43, 49, 54, 59, 76, 79 |
| **P1** rond, péremptoire | BADAUD 1 | 2 | 71 | 2, 64 |
| **P2** maigre, méfiant | BADAUD 2 | 2 | 54 | 2, 64 |
| **P3** grave, autoritaire | LE GÉNÉRAL · L'AUTRE · GARNERIN | 3 | 120 | 67, 51, 3 |
| **P4** jeune, clair | PAYSAN 2 · LA SENTINELLE · L'AIDE · PILLARD 2 | 4 | 209 | 22, 67, 3, 56 |
| **P5** rustique, rugueux | LE BADAUD · COMPÈRE 1 · PILLARD 1 · PAYSAN 1 | 5 | 268 | 51, 68, 56, 22 |

Deux contraintes commandent ce casting : **P1 et P2 sont verrouillés** (les badauds parient au plan 2 et se paient au plan 64, à seize minutes d'écart) ; **aucune paire ne se répète dans une même scène** (les sept scènes d'époque à deux voix sont les plans 2, 3, 22, 51, 56, 67, 68).

**Direction de jeu** : les 31 répliques en voix off de Sam et ses 31 répliques jouées sont **la même voix** ; ce qui change est le registre — posé et adressé au spectateur en voix off, vif et adressé à la table dans le cadre.

### Comment ce casting se réalise avec les voix libres

Depuis le 24 août, la voix d'un plan de dialogue est **générée par LTX-2.5 avec l'image** : le timbre se nomme dans le prompt (`grave voice`, `clear worried voice`), les répliques se citent mot pour mot. Le tableau ci-dessus reste le contrat : **un timbre nommé par voix**, réutilisé à l'identique dans tous les prompts de la même voix, et à vérifier à l'oreille sur chaque rendu. Les enregistrements ElevenLabs sont la **référence de timbre** — sur le pilote, grave « Guillaume – Narration and voiceover » (`ohItIVrXTBI80RrUECOD`) pour P1 et P3, claire « Curieux REM » (`jvSOBXJ1cP2sdvT5RgUP`) pour P2 et P4 ; non verrouillées tant que Guillaume ne les a pas entérinées.

**La voix off de Sam** (31 répliques, 5 001 caractères, l'essentiel de l'épisode) n'est pas dans un clip : elle se produit à part — ElevenLabs v3 sur la voix V1 verrouillée, une prise par réplique nommée par le numéro de plan (`S01E01_p008_SAM.wav`), texte à la ponctuation près — et se pose au montage sur les timecodes du minutage. C'est le point ouvert le plus lourd de l'épisode : la même voix doit être reconnue entre la voix off (ElevenLabs) et les répliques jouées dans le cadre (générées dans le clip, ou gelées depuis ElevenLabs par le mode IA2V validé en E8). À trancher sur la première séquence de cadre.

---

## 3. Musique

Sept plages **sans aucune parole**, 184 s (3 min 04), où la musique porte seule :

| Plans | Durée | Ce que la musique doit tenir |
|---|---|---|
| 1 | 18 s | ouverture froide, attente et tension au parc Monceau |
| 4 à 5 | 28 s | l'ascension puis la lame sur la corde |
| 39 | 32 s | la crue du fleuve Jaune et le renflouage |
| 45 à 46 | 44 s | le vol du prince, la plus longue plage |
| 57 | 14 s | la fuite des pillards |
| 62 à 63 | 38 s | la descente et le verdict de Garnerin |
| 80 | 10 s | le teaser final |

Le reste (70 plans, 1135 s) est porté par la voix off et demande un lit discret. Prévoir **un thème, sept pièces courtes et deux ou trois lits d'ambiance réutilisables**, pas 80 morceaux. Le thème se génère une fois puis sert de référence audio à toutes les variations. Prompt et référence de chaque morceau conservés dans l'index (dette de régénération si un diffuseur télévisé se présente).

---

## 4. Effets sonores

L'épisode se répartit en 42 plans ÉPOQUE (785 s), 31 plans CADRE (425 s) et 7 plans MIXTES (109 s). Trois familles, **une cinquantaine de générations** à quatre variantes chacune :

| Famille | Nombre | Nature |
|---|---|---|
| **Ambiances bouclées** | ~8 | le cadre intérieur, le parc au petit matin, le vent d'altitude, la campagne antique, le fleuve en crue, la ville Song la nuit, l'atelier et ses fours, la steppe |
| **Sons signature réutilisés** | ~6 | le gel d'Elio (5 plans, 78 s), la sacoche qui s'ouvre et se referme (10 plans, 155 s), la tablette d'Elio, le crayon de Naya, la porte du plan 8, le carton titre |
| **Effets ponctuels** | 25 à 35 | la corde tranchée, le ballon qui s'arrache, la crue, le cerf-volant, le pont de bambou, les fusées, les fours, la grange en feu |

Les ambiances générées par LTX-2.5 sur les plans muets (vent, murmure) se gardent ou se remplacent au montage ; les effets se posent après la voix et sous la musique. Ne pas appliquer le générateur aux clips en masse : ambiances, sons signature et grandes scènes seulement.

---

## 5. Mutualisations déjà décidées au montage

L'insert « main et sacoche » est **une seule image** réutilisée aux plans 23, 29, 34, 37, 64, 65, 68, 70, 73 et 74, avec l'objet changé. Le portrait de gel d'Elio est **une seule image** réutilisée aux plans 15, 25, 27, 34 et 53. Ne pas les redéfaire.
