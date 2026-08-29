# Pilote S01E01, plans 1 à 6 — état, ce qu'il a coûté, ce qu'il reste

Consolidé le 29 août 2026 à partir de l'audit visuel lot par lot du 22 au 27 août (618 lignes, dans l'historique git de `docs/S01E01-pilote-audit.md`). Ce document garde **l'état du pilote en style P**, la chronologie condensée avec ce que chaque passe a appris, et les restes. Les règles qui en sont sorties sont dans `atelier/METHODE-generation-images.md` (RÈGLES 26 à 42) et `atelier/STRATEGIE-video.md` ; les verdicts sur les moteurs dans `atelier/moteurs-ecartes/VERDICTS.md`.

---

## 1. État au 29 août 2026 — style P, montage v7, 62,8 s

**Livré** : `Downloads\EpisodeModernise\pilote\montages\montage_StyleP_v7.mp4`, 18 clips LTX-2.5 à 24 i/s, voix libres sur P02 et P03, ambiances générées sur les muets. Les quatre répliques sont dites mot pour mot (transcription + oreille). Continuité vérifiée plan par plan à pleine résolution le 27 août : parc → ballon seul amarré → nacelle et parachute replié apportés et gréés → pari → Garnerin à la corde de largage, l'aide au sol, « Lâchez tout » aux amarres → décollage avec Garnerin visible → Paris → le couteau, la corde unique, la rupture, le parachute ouvert et la nacelle qui descend.

**Ce qui est versionné dans le dépôt** (`iletaitunefois/S01E01/`) :

| Quoi | Où | Nombre |
|---|---|---|
| Planches de référence P | `assets/references/` | 7 : D01, D02, Foule, Garnerin, Parieurs, Ballon, Nacelle |
| Images clés P, dernières versions | `assets/cles/` | 18 |
| Prompts de clés | `prompts/briques_pilote.py` (briques), `assembler_prompts.py --md` pour le texte assemblé | 20 briques (P02a/P02b en réserve) |
| Prompts de clips, tels que rendus | `prompts/clips-StyleP.json` | 18, avec graines et longueurs |
| Identifiants Higgsfield (media_id, job_id) | `pilote/identifiants.md` | — |
| Descriptions canoniques des objets | `prompts/assets-et-objets.md` §7 | 12 objets |
| Logique de la scène | `logique-ouverture-froide.md` | — |

**Restes assumés** :
* **1b-3** et **4b-2** gardent un cadrage élargi par la réinjection des planches (corollaire de la RÈGLE 36) : 4b-2 montre les jambes de Garnerin au lieu du gros plan sur la main gantée. Se corrige par une clause de cadrage durci, comme 4a-2 (2 clés, 2 clips).
* Huit descriptions d'objets de continuité sont marquées « à arbitrer » dans `assets-et-objets.md` §7 (plans 7 à 79).
* La troupe (Sam, Elio, Naya) n'existe pas en style P.
* La tenue d'une même voix sur 21 minutes n'est pas mesurée (voix libres tenues sur 60 s).
* Les mp4 ne sont pas dans le dépôt (décision du 22 août) ; ils sont dans le dossier de travail.

**Coût du pilote, tous styles et essais confondus** : Higgsfield ≈ 480 crédits (1 032 → ≈ 552 ; à relever), RunPod ≈ 35 $ sur une vingtaine de pods, ElevenLabs quelques centaines de caractères et une dizaine de transcriptions. Le pilote en style P seul : 160 crédits (5 planches + 2 planches d'objets + 18 clés + 49 reprises de clés) et ≈ 6 $ de GPU.

---

## 2. Chronologie condensée, et ce que chaque passe a appris

### 22 août — 54 images clés en A, B, C ; 48 clips Wan 2.2

* **P02 en C sans visages** : une négative de foule agit sur toute l'image ; jamais sur un plan où un personnage nommé montre son visage → RÈGLE 26. 
* **1a-2 dérive** (couleurs réservées en A, visages en B) : seul plan de foule sans la référence Foule → RÈGLE 27, toujours réinjecter la fiche dès qu'un figurant est nommé.
* **5-2 corde déjà tranchée** dans deux styles sur trois : la brique se lisait comme un résultat → l'état prescrit en positif (`still in ONE piece, the blade halfway through`), RÈGLE 7.
* **Un code de décor seul (`D2`) sur un très gros plan devient un lettrage** → description en clair accolée, RÈGLE 28.
* **Deux nacelles** (la plaque D01 en porte une, la brique en apporte une) → RÈGLE 29 : deux références qui montrent le même objet en donnent deux ; clause anti-doublon.
* **Faux positif `nsfw`** sur un paysage vide : resoumettre à l'identique, non débité.
* 54 / 54 validées par Guillaume à 11 h 40 ; 142 crédits.
* **Clips** : le FLF2V morphe les cadrages → I2V par clé ; le gabarit doit dire ce qu'il y a à l'image (ligne de présence par plan) ; le bloc de style vidéo ne décrit pas les personnages ; une graine identique reproduit le même défaut. Wan 2.2 tient le trait sans LoRA sur 2 à 4 s. 48 clips, ~2 h 10 d'A100 ≈ 3 $.
* **Dialogues** (lots 4 à 8) : clip bouclé → scènes en double ; sous-clips par locuteur → l'auditeur ouvre quand même la bouche ; S2V anime le mauvais visage ; clés bouches fermées, cadrages variés, couleurs nommées en positif (RÈGLES 30 et 31) règlent tout ce qui se règle à l'image, pas la réplique. Un bug de montage (variante `_aligned` ramassée d'office) trouvé par transcription horodatée : **un montage se vérifie par mesure**, et le relecteur reçoit le scénario exact.

### 23 août — Essais E1 à E8 : le moteur

* E1/E1b InfiniteTalk : l'auditeur se tait, sur nos voix ; hallucination d'une voiture ; abandonné par Guillaume au rendu. P03 réécrit **autour de l'action** (main sur la corde de largage) : la clé doit porter la réplique.
* E2 trois samplers Wan 2.2 : cfg 2,0 garde les couleurs, gain faible.
* E3/E3b LTX-2.3 puis 2.5 (jeton Hugging Face) : propre, ~1 min par clip, audio d'ambiance généré ; insère une coupe vers 5-6 s sur un dialogue.
* E4 MiniMax H3 : très bon en français **au format du skill officiel**, hallucine sur les muets.
* E6 modèles fermés Higgsfield : tous tiennent le style, aucun ne prend nos voix.
* **E7** : six plans muets difficiles × A/B × trois moteurs → LTX-2.5 propre 12 fois sur 12. **E8** : voix gelée, voix référencée et voix libre marchent sur LTX-2.5 ; Guillaume choisit les voix libres (intonation, acoustique de scène).

### 24 août — Montage v7 en cinq styles (A, B, D, J, K), tout en LTX-2.5

90 clés vérifiées contre le script ; **le bras qui manie le couteau doit venir de l'intérieur de la nacelle** (5-1, 5-2 réécrits). Première salve de dialogues en charabia : **citer les répliques entre guillemets**. Cinq montages de 62,8 s, quatre répliques mot pour mot.

### 25-27 août — Le pilote en style P, six passes

| Passe | Retour de Guillaume | Cause | Réponse | Coût |
|---|---|---|---|---|
| 25-26 août, création | « le pilote en style P » | ni bloc versionné, ni planches | bloc relu sur les générations d'essai (jamais réécrit de mémoire) ; `assembler_refs.py` créé parce que les planches n'étaient pas versionnées ; 18 clés, 1 reprise (4a-1 enveloppe molle) ; dialogues cités dès le premier rendu, zéro re-rendu | 46 cr, 1 h A100 |
| 26 août | « le visage des personnages est tout noir en fond » | « aucun trait de visage » sur un style à deux ou trois tons donne le ton le plus sombre ; défaut sur la planche Foule, multiplié par sept réinjections | RÈGLE 37 : têtes strictement de dos, carnation nommée ; variante d'identité `P` ; fond gris uni durci | 16 cr, 7 clips |
| 26 août | « fais la planche du ballon » | l'aspect changeait sur 4a-3 (pas 4b, vérifié) | planche Ballon décrite d'après les clés validées, réinjectée sur les onze plans où il est visible, clause anti second ballon ; deux effets de bord → corollaires RÈGLE 36 (1b-3 : le ballon entre dans le champ ; 4a-2 : le cadrage s'élargit) | 28 cr, 11 clips |
| 26 août | second chapeau sur un bonnet ; nacelle changeante ; « quelle corde ? » | `hats held on with both hands` fabrique un chapeau ; un nom commun n'est pas une description ; trois très gros plans sans les deux bouts de la corde | RÈGLES 40 (garde des objets dans le gabarit), 38 (description canonique en sept points, planche Nacelle à deux vues), 39 (le cadre tient les deux termes de la relation) ; RÈGLE 41 | 28 cr, 14 clips |
| 27 août | « il y a des incohérences de scénario, réfléchis à la logique complète » ; « ça sert à rien de décrire le parachute sans écrire le mot » | le parachute était un paquet au plancher, l'aide à bord, l'ordre sans destinataire ; le mot avait été retiré en appliquant la RÈGLE 30 | chaîne physique écrite (`logique-ouverture-froide.md`), scénario corrigé, aide au sol, amarres tenues, Garnerin visible ; RÈGLE 42 ; main en visière (corollaire RÈGLE 40) ; P5-3 en triptyque repris par cadrage prescrit ; `GUIDE-preparation-episode.md` | 24 cr, 11 clips |
| 27 août, vérification | « vérifie la vidéo » | contrôle à deux images par plan à pleine résolution | nacelle accrochée avant d'être apportée (briques contradictoires → bloc 1a = ballon seul) ; parachute ouvert sur P02/4a-3 (le nom ramène la forme courante → état prescrit par la forme + `NEG_PARACHUTE_FERME`) ; ciel bleu / ballon rouge sur les plans lointains (couleurs nommées dans la scène) ; un prompt qui se contredisait (RÈGLE 13 : on remplace la phrase, on ne l'empile pas) | 18 cr, 8 clips |

Deux enseignements d'outil au passage : l'API S3 de RunPod refuse `HeadObject` (lire `get_object`) et supprime dossier par dossier (profondeur décroissante) ; une RTX PRO 6000 rend un clip en 28 s contre ~1 min sur A100.

---

## 3. Ce que le pilote a établi pour l'épisode

* **Le process** : chaîne physique et rôles → inventaire de continuité → descriptions canoniques → planches → clés regardées → clips → montage vérifié par mesure. C'est `atelier/GUIDE-preparation-episode.md`, avec sa liste de contrôle.
* **Le coût unitaire** en style P : 2 crédits la clé, ~30 s à 1 min de GPU le clip, une reprise sur trois clés en moyenne sur les premières passes, quasi nulle une fois les règles appliquées d'avance (le pilote P initial : une reprise sur dix-huit).
* **Ce qui ne se voit qu'au montage** : la continuité d'un objet, l'échelle d'une nacelle, la lisibilité d'une corde. D'où la vérification plan par plan avant de montrer.
