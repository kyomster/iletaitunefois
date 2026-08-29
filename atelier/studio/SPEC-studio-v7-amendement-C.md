# SPEC v7 — Amendement C

Destiné à Claude Code, à lire avec `SPEC-studio-v7.md`, `SPEC-studio-v7-amendement-A.md` et `SPEC-studio-v7-amendement-B.md`.
Rédigé le 26 août 2026.

**Périmètre.** Il ajoute deux modules que la v7 n'a pas : **la chaîne de rendu** — moteur, graphe, fichiers dérivés, transcription — et **la continuité visuelle**. Il complète les chapitres 6, 10, 11, 12, 13, 15, 16, 17, 19, 21, 23 et 24. **Tout le reste est inchangé.**

Motif : la v7 et ses deux amendements modélisent très bien un scénario, ses faits, sa prose et ses voix. Ils modélisent mal ce qui produit réellement les images et les clips. Cet amendement corrige ce déséquilibre à partir de ce que la chaîne fait sur S01E01, où quatre moteurs vidéo ont été essayés, six montages de pilote produits et trente six règles de méthode d'images écrites.

Source des constats : `docs/SPEC-studio-v7-ecarts-avec-notre-process.md`.

| Écart constaté | Traité en |
|---|---|
| A.1 graphe et moteur vidéo non modélisés | C.1 |
| A.2 prompt vidéo non stocké, dépendance réplique absente | C.2 |
| A.3 seule la prise séparée est prévue | C.3 |
| A.4 aucun contrôle texte attendu contre texte entendu | C.4 |
| A.5 fichiers dérivés non modélisés | C.5 |
| B.1 éléments de continuité sans planche | C.6 |
| B.2 pas d'attendus vérifiables par plan | C.7 |
| B.3 verdict machine indistinct du verdict humain | C.8 |
| B.4 l'épreuve comparative n'existe pas | C.9 |
| B.5 aucune trace d'exécution | C.10 |
| B.6 pas de rétention de stockage | C.11 |
| B.7 pas d'identifiant de média fournisseur | C.12 |
| B.8 fiche canon unique pour toutes les familles de style | C.13 |
| B.9 règles sans numéro ni preuve | C.14 |
| B.10 format sans bloc technique vidéo | C.15 |

---

# C.0 Alertes ajoutées

**ALERTE 17, le graphe est une source de vérité.** Un clip n'est pas défini par son prompt, mais par le couple prompt et graphe. Deux clips rendus avec le même texte sur deux graphes différents ne sont pas comparables. Tant que le graphe n'a ni version ni empreinte, la péremption ment.

**ALERTE 18, trois modes de voix, et le modèle n'en connaît qu'un.** La v7 suppose une prise audio par réplique, fabriquée à part. La chaîne en pratique trois modes, dont celui qui est retenu ne produit aucune prise. Un critère d'acceptation qui compte des prises échoue sur une chaîne saine.

**ALERTE 19, un clip peut être juste à l'image et faux au son.** Le seul contrôle qui l'attrape est une transcription comparée au texte attendu. **Mais la transcription se trompe**, en particulier sur les nombres : le contrôle est un signalement levable par l'oreille humaine, jamais un verdict automatique. Un contrôle audio qui bloque tout seul serait désactivé au bout d'une semaine.

**ALERTE 20, ce que l'humain juge est presque toujours un dérivé.** Un montage, une planche-contact, une image redimensionnée, une plaque rognée. Tant que le dérivé n'existe pas en base, un verdict désigne un fichier que personne n'a regardé.

**ALERTE 21, l'exécution a un coût opérationnel même sans budget.** Le suivi de budget reste écarté, ALERTE 1 tient. La trace d'exécution, elle, n'est pas financière : elle sert à savoir quel matériel a produit quoi, et surtout à savoir qu'une machine a été arrêtée. L'erreur la plus chère de ce projet à ce jour n'est pas un mauvais prompt, c'est une machine laissée allumée.

---

# C.1 Moteur et graphe de rendu

## C.1.1 Le modèle

```prisma
model Engine {
  id            String  @id @default(cuid())
  showId        String?                     // nul si partagé par tout le socle
  code          String                      // "ltx-2.5-i2v-2passes"
  label         String
  medium        String                      // IMAGE, VIDEO, AUDIO
  provider      String                      // "runpod-comfyui", "higgsfield", "elevenlabs"
  modelRef      String                      // le modèle de base et sa quantisation
  graph         Json?                       // le graphe au format API, verbatim
  graphSha256   String?                     // empreinte du graphe tel qu'exécuté
  params        Json                        // les paramètres normatifs, voir C.1.2
  version       Int     @default(1)         // entre dans le promptHash
  status        String                      // CANDIDAT, RETENU, ECARTE
  notes         String?
  sourceRef     String?
  locked        Boolean @default(true)
  @@unique([showId, code, version])
}
```

`Engine.status` porte l'histoire des arbitrages : un moteur écarté reste en base avec la raison de son écart, pour que personne ne le réessaie. Il se lit avec les `Learning` marqués `doNotRetry`, dont il est le pendant structuré.

## C.1.2 Les paramètres normatifs

`params` n'est pas un sac. Il contient les valeurs qui changent le rendu et qui doivent donc entrer dans l'empreinte :

```json
{
  "resolution": [1280, 704],
  "multipleDe": 32,
  "imagesParSeconde": 24,
  "longueurFormule": "8n+1",
  "passes": 2,
  "sigmas": [1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0],
  "sigmasSecondePasse": [0.85, 0.725, 0.4219, 0.0],
  "sampler": "euler_ancestral",
  "guider": "LTXVDualCFGGuider",
  "videoCfg": 1.0,
  "audioCfg": 1.0,
  "upscalerLatent": "x2"
}
```

Une clé inconnue est acceptée et conservée, comme pour `Format`. **Aucune de ces valeurs n'est en dur dans le code**, y compris la résolution et la cadence : elles se lisent sur le moteur retenu, jamais sur une constante.

## C.1.3 L'empreinte étendue

La formule du chapitre 11 devient :

```
promptHash = sha256(
    promptPos + promptNeg
  + refs triés par order, chacun avec son propre promptHash
  + styleCode + ":" + styleVersion
  + engineCode + ":" + engineVersion            <-- ajouté
  + lineIds cités + ":" + lockHash de chacune   <-- ajouté, voir C.2
  + hash des BibleEntry applicables où affectsPrompt = true
)
```

La péremption devient transitive **par `AssetRef`, par `MusicCue.referenceCueId`, par `Engine.version` et par `Line.lockHash`.**

## C.1.4 Outils MCP

```
list_engines(show?, medium?) / get_engine(code, version?)
upsert_engine(decisionId?) / set_engine_status(code, version, status, motif)
```

`upsert_engine` sur un moteur `RETENU` exige une `decisionId`, comme un style : changer de moteur est un arbitrage, pas une écriture ordinaire.

## C.1.5 Acceptation

- incrémenter la version d'un moteur périme les médias qui en dépendent, en cascade
- la fiche technique d'un média affiche le moteur, sa version et l'empreinte de son graphe
- un moteur `ECARTE` réutilisé dans un lot lève une alerte, avec la raison de son écart
- les paramètres normatifs ne se trouvent nulle part dans le code

---

# C.2 Le prompt vidéo est un asset, et il dépend du texte

## C.2.1 Ce qui change

`Clip` conserve `subjectEn` et `cameraEn`, qui sont des éléments de rédaction. Le prompt **réellement envoyé** devient un `Asset` de kind `CLIP_VIDEO`, avec son `promptPos`, son `promptNeg`, son empreinte et ses versions, exactement comme un prompt d'image. Un prompt qui n'est pas stocké tel qu'envoyé n'est pas auditable.

## C.2.2 La citation des répliques

Un prompt de dialogue **cite la réplique exacte entre guillemets**, avec la langue et le timbre. C'est une règle de bible exécutable, pas une convention :

```
key: "prompt-video-cite-les-repliques"
enforceable: true, affectsPrompt: true, severity: "BLOQUANT"
```

La fonction associée vérifie que le prompt d'un clip rattaché à un plan porteur de répliques contient chacune de ces répliques, au caractère près, entre guillemets. Un prompt de dialogue qui décrit la parole sans la citer est refusé à l'écriture.

Cette règle a un coût connu et mesuré : sans elle, les moteurs inventent une bande son plausible et incompréhensible.

## C.2.3 Le lien texte vers clip

```prisma
model AssetLineRef {
  assetId  String
  lineId   String
  lockHash String        // le hash de la réplique au moment de l'assemblage
  @@id([assetId, lineId])
}
```

Le `lockHash` mémorisé permet la péremption exacte : **modifier une réplique périme tous les clips dont le prompt la citait**, et le message de péremption nomme la réplique et le plan. Sans ce lien, corriger un texte laisserait en place un clip qui dit l'ancienne version, sans aucun signal.

## C.2.4 Acceptation

- un prompt de clip est stocké tel qu'envoyé et s'affiche intégralement dans la fiche technique
- un prompt de dialogue sans citation exacte est refusé, avec la réplique manquante nommée
- modifier une `Line` périme les clips qui la citent, et eux seuls
- le message de péremption nomme le plan et la réplique

---

# C.3 Les trois modes de voix

## C.3.1 Le mode déclaré

Nouvelle clé de format, portée programme ou saison :

```json
{ "voiceMode": "INTEGREE" }
```

| Mode | Ce qui se passe | Ce qui s'audite |
|---|---|---|
| `EXTERNE` | prise fabriquée chez un fournisseur de voix, posée au montage | la prise, puis le montage |
| `INTEGREE` | la voix naît dans le clip, avec l'acoustique de la scène | **le clip, par transcription** |
| `GELEE` | la prise existante est imposée au clip, les lèvres suivent | le clip, et la prise doit s'y retrouver intacte |

## C.3.2 Ce que chaque mode implique

En `INTEGREE`, **il n'existe aucun `VOICE_TAKE`**. Une `Line` n'attend pas de prise, elle attend un clip qui la dit. Les comptages de prises, les critères d'acceptation portant sur un nombre de prises et l'onglet Son doivent en tenir compte plutôt que de supposer l'existence des fichiers.

En `GELEE`, la prise existe, elle est rattachée à la `Line` comme dans la v7, **et un contrôle supplémentaire s'applique** : la piste du clip doit être identique à la prise. C'est vérifiable, et c'est le mode qui garantit l'identité vocale.

En `EXTERNE`, le modèle de la v7 s'applique inchangé.

## C.3.3 Ce qui reste vrai dans tous les modes

Les réglages de voix restent zone verrouillée. Deux voix pour un même locuteur restent une alerte bloquante. `lipSyncAutorise` cesse d'être un booléen de format et devient une propriété du moteur retenu : c'est le graphe qui sait si les lèvres suivent, pas une préférence déclarée.

## C.3.4 Acceptation

- en `INTEGREE`, l'absence de `VOICE_TAKE` n'est jamais une alerte
- en `GELEE`, un clip dont la piste diffère de la prise lève une alerte bloquante
- changer le `voiceMode` d'une saison périme les contrôles audio, pas les images
- un rapport d'import ne réclame jamais des prises que le mode ne produit pas

---

# C.4 Transcription et conformité de la parole

## C.4.1 Le modèle

```prisma
model Transcript {
  id           String  @id @default(cuid())
  mediaFileId  String
  engineCode   String                      // le moteur de reconnaissance et sa version
  lang         String
  text         String                      // le texte reconnu, intégral
  segments     Json                        // [{start, end, text}]
  createdAt    DateTime @default(now())
}

model SpeechCheck {
  id           String  @id @default(cuid())
  transcriptId String
  lineId       String
  expected     String                      // le texte attendu, verrouillé
  heard        String                      // l'extrait reconnu correspondant
  distance     Float                       // distance normalisée, 0 = identique
  verdict      String                      // CONFORME, ECART, LEVE_A_L_OREILLE
  liftedBy     String?                     // qui a levé l'écart, et donc humain
  liftedNote   String?
}
```

## C.4.2 Le contrôle

Déterministe : même média, même moteur de reconnaissance, même verdict. Un écart au delà d'un seuil lu dans le format produit une **alerte d'attention**, jamais un blocage automatique, et cette alerte se lève explicitement par un humain avec une note.

Nouvelle clé de format :

```json
{ "toleranceTranscription": 0.15 }
```

**La raison de ce choix est écrite dans ALERTE 19 et elle est mesurée** : sur trois montages, une réplique parfaitement prononcée a été transcrite de travers parce qu'elle contenait un nombre. Un contrôle qui bloque sur ce genre d'erreur se fait désactiver, et on perd le contrôle entier — y compris le jour où le moteur invente vraiment une bande son.

## C.4.3 Outils MCP

```
ingest_transcript(mediaId, engineCode, lang, text, segments)
speech_check(mediaId | planNumbers)
lift_speech_check(checkId, note)        exige une session ouverte
```

## C.4.4 Acceptation

- un clip dont la piste ne dit pas la réplique attendue lève une alerte d'attention nommant le plan
- l'alerte se lève par un humain, avec une note conservée, jamais par l'agent seul
- deux exécutions du contrôle sur le même média rendent le même verdict
- un `SpeechCheck` levé reste visible dans l'historique du média

---

# C.5 Les fichiers dérivés

## C.5.1 Le modèle

```prisma
model DerivedFile {
  id             String  @id @default(cuid())
  sourceIds      Json                       // un ou plusieurs mediaFileId, ordonnés
  role           String                     // MONTAGE, PLANCHE_CONTACT, IMAGE_DE_DEPART,
                                            // ROGNAGE, REDIMENSION, EXTRAIT, POSTER
  tool           String                     // "ffmpeg", "sharp", nom du script
  toolVersion    String?
  params         Json                       // les arguments exacts, rejouables
  bucket         String; objectKey String @unique
  mime String; bytes Int; sha256 String
  width Int?; height Int?; durationSec Float?
  createdAt      DateTime @default(now())
}
```

`sourceIds` est une liste ordonnée parce qu'un montage a plusieurs sources et que leur ordre est l'information principale.

## C.5.2 Ce que ça débloque

Un `Verdict` peut désormais porter sur un `DerivedFile`, ce qui correspond à la réalité : un montage se juge sur le montage, pas sur les dix huit clips pris un par un. Le champ `mediaFileId` du `Verdict` devient `targetId` avec un `targetKind` valant `MEDIA` ou `DERIVE`.

Cela règle aussi le cas des défauts structurels : la méthode d'images établit que certains défauts ne se corrigent **jamais dans le prompt** mais en aval, par un script. Le fichier utile est alors le dérivé, et c'est lui qui doit être réinjecté comme référence, pas l'original.

## C.5.3 Le montage de contrôle rentre dans le périmètre

Le chapitre 22 range le montage hors périmètre. **Cette exclusion est maintenue pour le montage final et levée pour le montage de contrôle** : concaténer des clips dans l'ordre des plans pour juger une séquence est un acte de vérification, pas de post-production. Le socle ne monte pas, mais il **détient** le montage de contrôle, son ordre, ses sources et son verdict.

## C.5.4 Acceptation

- un montage de contrôle existe en base avec ses sources ordonnées et se rejoue à l'identique depuis ses paramètres
- un verdict peut porter sur un dérivé, et la fiche technique remonte jusqu'aux originaux
- une plaque rognée est réinjectable comme référence, l'originale reste consultable

---

# C.6 Continuité visuelle

## C.6.1 Le principe

Une description recopiée ne tient pas la continuité ; seule une image réinjectée la tient. Preuve mesurée : un ballon décrit avec les mêmes mots sur dix huit plans est sorti rayé crème sur les plans proches et rayé orangé sur les plans lointains. Le défaut est invisible sur une image isolée et évident sur un montage.

## C.6.2 Le modèle

```prisma
model ContinuityItem {
  id         String  @id @default(cuid())
  showId     String; episodeId String?      // nul si l'élément traverse la série
  key        String                         // "ballon", "hibou-de-papier"
  label      String
  kind       String                         // OBJET, VEHICULE, MACHINE, ANIMAL,
                                            // VETEMENT, ENSEIGNE, LIEU
  planNumbers Json                          // les plans où il doit être identique
  refAssetId String?                        // la planche de référence, par style
  note       String?
  @@unique([showId, episodeId, key])
}
```

## C.6.3 Les contrôles

- **un `ContinuityItem` sans `refAssetId` dans un style actif est une alerte bloquante à la préparation** d'un lot touchant ses plans — pas au moment de l'écriture, pour ne pas bloquer la rédaction
- un plan listé dans `planNumbers` dont le prompt ne réinjecte pas la planche est une alerte d'attention
- un élément nommé dans deux plans ou plus et absent du registre est une alerte d'attention, heuristique, levable

Le dernier point est l'équivalent visuel de la détection des faits non sourcés, avec la même prudence : heuristique, jamais bloquant.

## C.6.4 Ce que le roster doit livrer

Le point 3 du livrable de la partie II de la bible réclamait « les accessoires avec les objets de continuité ». **Il réclame désormais, pour chacun, sa planche et la liste des plans où elle se réinjecte.** La liste de noms sans images était précisément le défaut : elle existait sur S01E01 et n'a produit aucune référence.

## C.6.5 Acceptation

- préparer un lot sur un plan dont un élément de continuité n'a pas de planche échoue, en nommant l'élément
- ajouter la planche débloque le lot sans autre intervention
- un élément cité dans deux plans et absent du registre apparaît en alerte d'attention

---

# C.7 Les attendus d'un plan

## C.7.1 Le modèle

```prisma
model PlanExpectation {
  id       String @id @default(cuid())
  planId   String
  order    Int
  kind     String        // PRESENCE, POSITION, ACTION, INTENTION, CADRAGE, ACCESSOIRE
  text     String        // "le bras qui coupe part de l'intérieur de la nacelle"
  critical Boolean @default(false)
}
```

Court, vérifiable à l'œil, une ligne par attendu. Ce n'est pas une reformulation du synopsis : le synopsis raconte, l'attendu se coche.

## C.7.2 Usage

Les attendus s'affichent **à côté de l'image** dans une session `AUDIT_IMAGES`, et à côté du clip dans un audit vidéo. Un attendu `critical` non satisfait impose un verdict `REPRENDRE` : l'auditeur ne peut pas valider en le laissant décoché.

Justification par l'expérience : le contrôle « la position des personnages correspond au script et à l'environnement » a fait reprendre douze images sur le pilote. Devant douze images en quatre minutes, personne ne relit un synopsis en prose.

## C.7.3 Acceptation

- les attendus s'affichent avec le média jugé et se cochent au clavier
- un attendu critique non satisfait interdit le verdict `BON`
- un plan sans attendu n'est jamais bloqué, mais apparaît dans le rapport de préparation

---

# C.8 Verdict machine et verdict humain

```prisma
// Verdict reçoit :
auditKind String @default("HUMAIN")     // MACHINE, HUMAIN
```

**Un verdict `MACHINE` ne clôt jamais une session, ne fait jamais avancer un `stage`, et ne satisfait jamais une condition d'acceptation.** Il sert à trier, à préparer le travail de l'humain et à signaler ce qui mérite un regard.

C'est l'application directe de l'ALERTE 5 de la v7 : une session non ouverte n'est pas une approbation, et un audit automatique n'est pas une session. La raison est empirique : plusieurs verdicts d'agent se sont révélés faux au recontrôle sur planche-contact.

Acceptation : un média n'ayant que des verdicts `MACHINE` reste dans la file des médias non audités.

---

# C.9 L'épreuve comparative

## C.9.1 Le modèle

```prisma
model Trial {
  id         String @id @default(cuid())
  showId     String; episodeId String?
  label      String                        // "pilote 70 secondes"
  question   String                        // ce qu'il s'agit de trancher
  planNumbers Json                         // le sous-ensemble de plans
  arms       Json                          // les branches comparées : styles, moteurs, modes
  artifacts  Json                          // les derivedFileId produits, par branche
  status     String                        // EN_COURS, TRANCHEE, ABANDONNEE
  decisionId String?
}
```

Un pilote est exactement cela : un sous-ensemble de plans, rendu en plusieurs branches, pour trancher une question. Rien dans la v7 ne le nomme, alors que c'est l'objet le plus coûteux de la production.

## C.9.2 La session de choix porte des vidéos

`CHOIX_STYLE` soumet aujourd'hui « des plans, plusieurs styles, leurs images ». **Elle doit pouvoir soumettre des montages**, et par défaut les soumettre quand la branche en a produit. Le défaut du ballon était invisible sur une image et évident sur un montage : soumettre des images fixes revient à demander un arbitrage sur ce qui ne montre pas le problème.

Les branches ne portent pas que des styles : un moteur, un mode de voix, un réglage de graphe se tranchent de la même façon. La session gagne un `kind` `CHOIX_TECHNIQUE`, de mécanique identique, écrivant `Engine.status` et `format.voiceMode` au lieu de `format.stylesActifs`.

## C.9.3 Acceptation

- une épreuve retient ses branches, ses artefacts et sa question, et se clôt par une décision
- une session de choix affiche les montages quand ils existent, les images sinon
- trancher une épreuve technique écrit le statut du moteur retenu et écarte les autres avec leur motif

---

# C.10 Contexte d'exécution

L'ALERTE 1 tient : ni crédits, ni coûts, ni licences. Ce qui suit est opérationnel.

```prisma
model Execution {
  id          String @id @default(cuid())
  batchId     String?
  provider    String
  hostRef     String?                     // identifiant de machine ou de pod
  hardware    String?                     // "A100 80 Go"
  startedAt   DateTime; endedAt DateTime?
  stopped     Boolean @default(false)     // la machine a été arrêtée
  bootstrapRef String?                    // le script d'amorçage et sa version
  note        String?
}
```

`Job` reçoit `executionId String?`.

Contrôles : une `Execution` ouverte depuis plus de quelques heures sans `stopped` lève une alerte d'attention, et `next` la fait remonter. Une machine non arrêtée est la défaillance la plus fréquente et la plus évitable de cette chaîne.

Acceptation : `doctor` signale toute exécution non arrêtée ; la fiche technique d'un média nomme la machine et le script d'amorçage qui l'ont produit.

---

# C.11 Deux espaces de stockage, et une rétention

La v7 connaît un bucket où rien n'est jamais écrasé. La pratique en connaît deux, et les confondre coûte soit de la place, soit une heure de téléchargement à chaque session.

| Espace | Contenu | Règle |
|---|---|---|
| **Calcul** | volume monté par la machine de rendu | les sorties y sont écrites, rapatriées, **puis supprimées** ; tout ce qui est réutilisable y reste : modèles, images de départ, références, graphes |
| **Archive** | bucket permanent du socle | rien n'est jamais écrasé ni supprimé |

```prisma
// MediaFile et DerivedFile reçoivent :
space     String @default("ARCHIVE")     // ARCHIVE, CALCUL
retention String @default("PERMANENTE")  // PERMANENTE, APRES_RAPATRIEMENT
```

Outil : `purge_space(space, prefix)`, qui refuse de supprimer un objet dont la copie d'archive n'est pas vérifiée par empreinte. **Aucune suppression n'est possible sans copie vérifiée.**

Acceptation : rapatrier un lot puis purger l'espace de calcul ne perd rien ; une purge sans copie vérifiée échoue en nommant les objets à risque.

---

# C.12 Identifiant de média chez le fournisseur

```prisma
// Asset reçoit :
providerMediaIds Json?     // { "higgsfield": "ecfa74c5-...", ... }
```

Une planche de référence téléversée chez un fournisseur y reçoit un identifiant réutilisable pour tout l'épisode, voire toute la série. Ne pas le conserver oblige à renvoyer les fichiers, ce qui coûte du temps et fait dériver les références.

Acceptation : réutiliser une référence déjà téléversée ne produit aucun nouveau téléversement.

---

# C.13 Fiche canon par famille de style

`Character.canonSheet` devient indexée par famille de style :

```json
{
  "_defaut": "...",
  "inkman": "un bonhomme bâton, tête ronde, yeux en points, ...",
  "cel-2d": "un aéronaute au visage résolu, mâchoire calme, ..."
}
```

Résolution : famille exacte, puis `_defaut`. La cascade personnage de la v7 — univers, programme, saison, épisode — est inchangée et s'applique avant cette résolution.

Sans cela, la fiche canon devient fausse dès le deuxième style, puisqu'un personnage n'a pas la même définition graphique selon la famille.

Acceptation : le même personnage rendu dans deux familles produit deux blocs d'identité différents et cohérents, sans saisie en double du reste de la fiche.

---

# C.14 Les règles gardent leur numéro et leur preuve

```prisma
// Learning reçoit :
number   Int?      // le numéro stable, cité entre documents et dans les scripts
evidence String?   // ce qui a été observé : combien de tirages, quels styles,
                   // ce que disait la négative qui n'a pas marché
```

Une règle est citée par son numéro dans les autres documents et jusque dans les commentaires des scripts ; le numéro est donc une donnée, pas un habillage. Et une règle sans sa preuve se refait litige au bout de deux mois : `evidence` n'est pas de la documentation, c'est ce qui empêche de la rediscuter.

Le chapitre 21 prévoit d'importer « les 24 règles de méthode ». Le compte a changé et changera encore. **Le critère d'acceptation ne porte pas un nombre**, il porte sur le fait que l'import est vérifié contre le document source et que le rapport donne le compte.

---

# C.15 Bloc technique vidéo dans le format

Le chapitre 6 décrit l'image et donne une cadence qui n'est pas celle du moteur retenu. Ajout :

```json
{
  "video": {
    "engineCode": "ltx-2.5-i2v-2passes",
    "imagesParSeconde": 24,
    "resolution": [1280, 704],
    "longueurFormule": "8n+1",
    "dureeClipMaxSec": 10
  },
  "analyse": {
    "imagesParSecondeAnalyse": 1
  }
}
```

`imagesParSeconde` et `decimationImagesParSeconde`, à la racine, décrivent l'image et l'analyse, pas le rendu vidéo : les laisser servir aux deux produirait un format faux dès le premier lot de clips. Les valeurs du bloc vidéo se lisent en priorité sur le moteur retenu ; le format ne fait que le désigner et fixer ce qui lui est propre.

---

# C.16 Récapitulatif des outils MCP ajoutés

```
list_engines / get_engine / upsert_engine / set_engine_status
upsert_continuity_item / list_continuity_items / link_continuity_ref
upsert_plan_expectation / list_plan_expectations
ingest_transcript / speech_check / lift_speech_check
register_derived(sourceIds, role, tool, params, ...) / get_derived
upsert_trial / close_trial(decisionId)
open_execution / close_execution(stopped)
purge_space(space, prefix)
```

Tous obéissent à la règle intangible du 16.7 : le serveur ne contourne jamais une règle métier, n'écrit jamais ce qu'une session aurait dû autoriser, et n'appelle jamais de modèle. `ingest_transcript` reçoit une transcription produite ailleurs ; il n'en produit aucune.

---

# C.17 Compléments au chapitre 21, import

- les moteurs essayés entrent tous, y compris les écartés, avec leur statut et le motif de l'écart
- le moteur retenu entre en version 1 avec son graphe et ses paramètres normatifs
- le `voiceMode` de la saison entre à sa valeur réelle, et **aucune prise n'est réclamée si le mode n'en produit pas**
- les montages du pilote entrent comme `DerivedFile` de rôle `MONTAGE`, avec leurs sources ordonnées
- le pilote entre comme `Trial`, avec ses branches, ses artefacts et sa question
- les éléments de continuité de l'épisode entrent en `ContinuityItem`, **avec la mention explicite de ceux qui n'ont pas encore de planche** — le rapport d'import les liste comme dette de préparation, il ne les invente pas
- les règles de méthode entrent avec leur numéro et leur preuve, le compte étant donné par le rapport
- les verdicts d'audit produits par un agent entrent en `auditKind: MACHINE`

**Rien n'est complété de mémoire.** Un moteur dont le graphe n'a pas été conservé entre sans graphe, avec `graphSha256` nul, et le rapport le signale.

---

# C.18 Compléments au chapitre 23, lots et acceptation

**Lot 1** reçoit `Engine`, `DerivedFile`, `Execution`, les deux espaces de stockage et `auditKind`. Ce sont les fondations : sans elles, tout média importé entre déjà incomplet.

- un média affiche le moteur, sa version, la machine et le script d'amorçage qui l'ont produit
- un dérivé se rejoue à l'identique depuis ses paramètres
- une purge sans copie vérifiée échoue
- un verdict machine ne fait pas sortir un média de la file d'audit

**Lot 2** reçoit `AssetLineRef` et la règle de citation des répliques.

- un prompt de dialogue sans citation exacte est refusé
- modifier une réplique périme les clips qui la citent, et eux seuls

**Lot 4** reçoit `ContinuityItem`, `PlanExpectation`, `Trial` et `CHOIX_TECHNIQUE`.

- préparer un lot sur un plan dont un élément de continuité n'a pas de planche échoue
- un attendu critique non satisfait interdit le verdict `BON`
- une session de choix affiche les montages quand ils existent

**Lot 5** reçoit `voiceMode`, `Transcript` et `SpeechCheck`, et **ses critères chiffrés sont réécrits** : ils portaient sur un nombre de prises que le mode retenu ne produit pas.

- en mode intégré, un clip dont la piste ne dit pas la réplique attendue lève une alerte d'attention
- l'écart se lève par un humain, avec sa note
- en mode gelé, une piste qui diffère de la prise lève une alerte bloquante

---

# C.19 Compléments au chapitre 24

**Traiter le graphe comme un réglage.** Un graphe sans version est un style sans formule : tout ce qu'on croit comparer ne l'est pas.

**Bloquer automatiquement sur une transcription.** Un contrôle audio qui bloque sur une erreur de reconnaissance se fait désactiver, et on perd le seul contrôle capable d'attraper une bande son inventée.

**Auditer l'original quand l'humain a jugé le dérivé.** Le verdict pointe alors un fichier que personne n'a regardé.

**Lister un élément de continuité sans en faire une image.** C'est exactement le défaut qui a produit deux ballons différents dans le même montage : la liste existait, la place dans l'ordre des références existait, l'image n'existait pas.

**Compter des prises dans un mode qui n'en produit pas.** Un critère d'acceptation qui porte un nombre périmé fait échouer un lot sain, et on finit par ignorer les critères.

**Laisser une machine allumée.** Ce n'est pas du budget, c'est de la discipline opérationnelle, et c'est la défaillance la plus fréquente de cette chaîne.
