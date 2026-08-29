# Décisions du pilote S01E01 — ce qui est en vigueur

Consolidé le 29 août 2026 à partir du journal des arbitrages du 22 au 27 août. Première partie : les décisions **en vigueur**, datées, avec leur raison. Seconde partie : celles qu'elles ont **remplacées**, en une ligne chacune, pour qu'on ne les reprenne pas sans savoir pourquoi elles ont été écartées. Le suivi brut (heures de pod, graines, versions) reste dans le dossier de travail `Downloads\EpisodeModernise\pilote\journal.md` ; l'audit visuel est dans `AUDIT.md`.

---

## En vigueur

### 2026-08-29 — Le style de la série est **P, anime TV moderne**

Décision de Guillaume après six montages comparés (A, B, D, J, K, P). Tout ce qui est propre au style vit dans `styles/P-anime-tv-moderne/` ; les autres styles sont conservés dans la bibliothèque pour d'autres séries. Conséquences : la troupe récurrente (Sam, Elio, Naya), qui n'existe qu'en A, B et C, est **à refaire en P** ; les planches et clés P du pilote sont la base de l'épisode.

### 2026-08-29 — Le dépôt devient la bible de fabrication, en quatre dossiers

`ecriture/` (méthode d'écriture générique), `styles/` (bibliothèque réutilisable), `atelier/` (méthode d'images, stratégie vidéo, RunPod, scripts génériques, moteurs écartés), `iletaitunefois/` (la série et ses épisodes). Historique conservé par `git mv`. Les scripts d'assemblage sont génériques et lisent `styles/*/style.json` plus un module de briques par épisode.

### 2026-08-24 — Le moteur vidéo est **LTX-2.5, partout, voix libres**

Après E7 (plans muets : LTX-2.5 propre 12 fois sur 12 là où Wan 2.2 faisait surgir des personnages et où H3 hallucinait) et E8 (les trois modes de voix marchent sur 2.5), Guillaume tranche : voix **générées avec l'image**, parce que l'intonation suit l'action et que la voix est dans l'acoustique de la scène. Cadence 24 i/s, 1280 × 704, deux passes. Les modes gelé (nos pistes ElevenLabs) et référencé (ID-LoRA) restent validés en repli. Détail : `atelier/STRATEGIE-video.md`.

### 2026-08-24 — Un prompt de dialogue **cite les répliques exactes** entre guillemets

Décrire la scène sans citer le texte fait inventer un charabia (payé une heure de pod sur dix clips). La langue et le timbre s'écrivent avec (`says in French, grave voice: "…"`), et le prompt nomme qui écoute bouche fermée. Vérification par transcription horodatée, mais **la prononciation d'un nombre ou d'un nom propre se juge à l'oreille** : « Dix francs » lu « Dis Franck » par scribe_v1 est un artefact de transcription, pas un défaut de rendu (23 août).

### 2026-08-23 — Sur les plans de dialogue, la bouche bouge, et la synchro est faite par le moteur

Deux décisions successives de Guillaume : « pas de synchro labiale ne veut pas dire bouches immobiles » (22 août), puis « les plans de dialogue sont générés avec voix et bouche dans le même rendu » (23 août), ce qui retire la règle « pas de synchronisation labiale » de la bible. Le plan à deux est conservé (pas de champ-contrechamp obligatoire) et **les deux visages doivent être visibles sur la clé**.

### 2026-08-22 — Les images clés restent chez **Higgsfield, Nano Banana Pro**

Contrainte de continuité : tous les assets validés viennent de ce moteur avec les blocs de style verrouillés. Réglages : `nano_banana_pro`, 16:9, 2K, une image par requête, 2 crédits, négatives après `Avoid:`, sept références au plus dans l'ordre décor → personnages → accessoires. Aucun appel Higgsfield pendant une phase de plan.

### 2026-08-22 — En vidéo, **le bloc de style se réduit à la facture**

Le bloc complet décrit des personnages et le modèle en fabrique (style B : 12 clips sur 16 avec des têtes inventées, 0 sur 12 avec le bloc réduit). L'image clé porte le style ; le bloc vidéo (`clip` du `style.json`) ne parle que de trait, d'aplats, de palette, de cadence.

### 2026-08-22 — Le raccord se choisit selon que le cadrage change

Cadrage différent → **I2V depuis la clé validée** (le FLF2V morphe la caméra et la foule). Même cadrage → chaîne par dernière image rendue. Deux images identiques en FLF2V donnent un clip figé. Chaque clé validée est à l'écran à son temps ; aucune dérive ne s'accumule.

### 2026-08-22 — Musique et effets : **Eleven Music et Eleven SFX**, diffusion **YouTube et web uniquement**

Motif juridique (données d'entraînement licenciées). Si un diffuseur télévisé se manifeste, passer en Enterprise et **régénérer toute la musique** ; d'où l'obligation de conserver le prompt et la référence audio de chaque morceau. Un thème généré une fois sert de référence à toutes les variations. Rien de tout cela n'est produit sur le pilote, muet par le scénario hors P02 et P03.

### 2026-08-26 — Les éléments de continuité passent en **référence**, et leur inventaire est une étape du process

Guillaume : « les éléments qui doivent être identiques sur les différents plans doivent être en mode référence et dans la bible de l'épisode ». RÈGLE 36 et corollaires, inventaire exigé dès l'écriture (méthode §5 bis), planches d'objets fabriquées comme les décors (`assembler_refs.py`). Une planche ne se réinjecte que sur les plans où l'objet est visible ; elle déplace le cadrage, qu'on reprend en positif.

### 2026-08-26 — Un asset se décrit en entier et **par son nom** ; le cadrage montre ce que l'action relie

Trois retours (second chapeau, nacelle changeante, corde illisible) → RÈGLES 38, 39, 40, puis 41 (toute règle de script est écrite en clair) et 42 (nommer l'objet, prescrire l'état par la forme ; `NEG_PARACHUTE_FERME`). Douze objets de continuité de S01E01 ont leur description canonique dans `../prompts/assets-et-objets.md` §7 ; huit restent marqués « à arbitrer ».

### 2026-08-27 — La logique de l'ouverture froide : **parachute gréé entre le ballon et la nacelle**

Le scénario faisait tomber Garnerin avec un « paquet de soie » ; la chaîne réelle est ballon → corde → parachute replié → suspentes → nacelle. Corrigé dans le scénario, le plan de production, les briques et la fiche d'assets, sans toucher au texte dit ni aux durées. **Correction factuelle appliquée, à entériner par Guillaume.** Qui fait quoi : Garnerin dans la nacelle et visible au décollage, l'aide au sol, les amarres tenues comme destinataire de « Lâchez tout ». Les badauds mettent la main en visière, jamais au chapeau. Analyse : `../logique-ouverture-froide.md`.

### 2026-08-26 — Bonne pratique permanente RunPod : **tout passe par le volume et S3**

Modèles résidents sur `atelier-modeles` (EU-RO-1, 37 Go LTX-2.5, volume ramené à 100 Go après purge des 68 Gio de restes de LoRA le 28 août) ; le pod démarre sans rien télécharger ; sorties écrites sur le volume, rapatriées par `runpod_s3.py`, **puis supprimées** ; références et modèles conservés. Quand EU-RO-1 n'a pas de GPU, on attend (boucle de relance) plutôt que de déménager. Tout pod est terminé en fin de session, `runpod.py list` vide.

### 2026-08-22 — Règles de travail

Aucun appel Higgsfield en phase de plan ; toute information durable s'écrit dans le dépôt au moment où elle est acquise (désormais dans les quatre dossiers) ; le dossier de travail ne garde que le brut et le suivi ; un outil de montage ne choisit jamais une variante tout seul, chaque source est explicite ; un montage se vérifie par mesure (images datées + transcription + relecteur qui reçoit le scénario exact), et tout verdict d'agent se recontrôle sur la planche.

### Voix de référence, non verrouillées

Les quatre répliques du pilote ont été enregistrées avec ElevenLabs v3 sur deux voix du compte — grave « Guillaume – Narration and voiceover » (`ohItIVrXTBI80RrUECOD`), claire « Curieux REM » (`jvSOBXJ1cP2sdvT5RgUP`). Elles servent de **référence de timbre** ; le casting de l'épisode (huit voix) est dans `../son-et-voix.md` et reste à entériner.

---

## Remplacées

| Date | Décision | Remplacée par | Pourquoi |
|---|---|---|---|
| 22 août | RunPod d'abord avec **Wan 2.2 I2V**, API Higgsfield Wan 2.7 en repli | LTX-2.5 partout (24 août) | Wan 2.2 : auditeur qui ouvre la bouche, personnages surgis, LoRA qui fige ; Wan 2.7 ne prend qu'une référence audio |
| 22 août | Chaîne **FLF2V** clé k → clé k+1 dans un bloc | I2V par clé quand le cadrage change | le FLF2V morphe la caméra et la foule entre deux cadrages |
| 22 août | Plan de dialogue en **clip de 5 s bouclé** | un clip par plan, répliques citées | scènes en double, deux bouches qui parlent tout le plan |
| 22 août | Sous-clips **par locuteur** chaînés + recalage audio heuristique (`align_dialogue_audio.py`) | génération jointe voix + image | Wan 2.2 ne tient pas une bouche fermée sur commande textuelle |
| 22 août | **Wan 2.2 S2V** pour la synchro | écarté | anime le visage le plus visible, pas le locuteur |
| 23 août | **InfiniteTalk** (nos voix, masques) pour les dialogues | abandonné par Guillaume | rendu insuffisant, hallucinations de fond (voiture), 22 min par plan |
| 23 août | **MiniMax H3** comme moteur principal | second choix pour un dialogue plus « joué » | hallucine sur les plans muets |
| 23 août | Voix **ElevenLabs gelées** (IA2V) dans LTX-2.5 | voix libres | voix plates, acoustique « studio avec écho » ; le mode reste validé en repli |
| 22 août | **Compositing au montage** de l'auditeur | inutile | résolu par le moteur |
| 22 août | Style **C retiré** ; puis choix entre A, B, D, J, K, P | **P** (29 août) | — |
| 22 août | LoRA de style à entraîner sur le style retenu | non lancé | LTX-2.5 tient le trait des styles sans LoRA sur 2 à 4 s ; à réévaluer sur un épisode entier (entraîneur officiel Lightricks) |
| 26 août | Volume 100 → 200 Go pour loger LTX-2.5 | 100 Go | restes de LoRA purgés le 28 août (68,4 Gio, sauvegarde locale) |
