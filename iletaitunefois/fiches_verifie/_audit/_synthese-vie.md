# Synthèse de campagne — série `vie`

> **Série** : *Il était une fois… la Vie* (1987) · **Date de campagne** : 2026-08-05
> **Périmètre** : `/data/origo/fiches/vie` (26 fiches) → `/data/origo/fiches_verifie/vie`
> **Audits** : `_audit/vie/` (26 fichiers, 2 484 lignes) · **Couverture** : 26 fiches sur 26 (100 %)
> **Reconstruction** : les données de réécriture du run producteur ne sont plus disponibles pour les dix-huit premières fiches. La volumétrie ci-dessous est reconstruite à partir des 26 fichiers d'audit — bilans et tableaux de corrections — et de mesures programmatiques sur les fiches source et vérifiées. Elle décrit donc ce que les audits déclarent, non ce qu'un journal d'exécution aurait enregistré. Les huit dernières fiches (S01E19 à S01E26) ont été réécrites manuellement, sans workflow, à partir des audits déjà produits.

---

## 1. Volumétrie

### 1.1 Vue d'ensemble

| | |
|---|---|
| Fiches de la série | 26 |
| Fiches présentes dans `fiches_verifie/vie` | 26 (100 %) |
| Section `## Ce que l'on sait depuis` présente | 26 / 26 |
| Faits contrôlés (série, d'après les 26 audits) | 846 |
| ✅ Confirmés | 441 (52,1 %) |
| ⚠️ Imprécis | 215 (25,4 %) |
| ❌ Erronés | 83 (9,8 %) |
| 🕰️ Dépassés depuis la diffusion | 51 (6,0 %) |
| ❓ Non tranchés | 56 (6,6 %) |
| Lignes de correction consignées dans les audits | 335 |
| Recherches web déclarées | 700 |
| Lignes avant → après | 5 143 → 5 770 (+12,2 %) |
| Mots avant → après | 144 978 → 221 914 (+53,1 %) |
| Fiches conformes au contrôle structurel | 26 sur 26 |

Aucune fiche n'a été raccourcie. Aucune URL n'apparaît dans les 26 fiches produites, aucun tableau de statuts, aucune section hors `## Ce que l'on sait depuis`, aucun marqueur de remplissage — vérification programmatique sur les 26 fiches. Les cinq sections préservées (`Personnages`, `Découpage séquentiel`, `Gags`, `Répliques marquantes`, `Réserves sur la source`) sont identiques à l'octet près à leurs originales sur les 26 fiches.

**La série la plus solide du corpus traité à ce jour.** 47,9 % des faits contrôlés portent un statut autre que ✅ dans `terre`, 43,7 % dans `decouvreurs` — mais seulement **37,9 %** ici. La biologie de 1987 vieillit mieux que le climat de 2008 ou l'histoire des sciences de 1994, pour une raison simple : la série décrit des mécanismes stables et les décrit correctement. Ce qui a bougé, ce sont presque toujours les **chiffres** et les **cadres théoriques**, rarement les mécanismes eux-mêmes.

Deux exceptions notables à ce satisfecit — voir § 3.1 et § 3.2 : la série traîne d'un bout à l'autre deux erreurs systématiques, le « cerveau à trois étages » et la carte HLA universelle, qui ne sont pas des accidents de fiche mais des motifs de scénario.

### 1.2 Détail par fiche

Les colonnes de statut reprennent le bilan de chaque audit. « Corr. » compte les lignes du tableau *Corrections appliquées* de l'audit — un même énoncé faux y occupe une ligne par section où il apparaît.

| Fiche | Faits | ✅ | ⚠️ | ❌ | 🕰️ | ❓ | Corr. | Rech. | Lignes |
|---|---|---|---|---|---|---|---|---|---|
| S01E01 La naissance de la vie et la cellule | 40 | 15 | 15 | 3 | 5 | 2 | 23 | 30 | 190 → 211 |
| S01E02 La fécondation et la formation du fœtus | 29 | 20 | 2 | 3 | 2 | 2 | 7 | 26 | 186 → 211 |
| S01E03 Les globules blancs et la défense | 36 | 16 | 11 | 5 | 3 | 1 | 19 | 31 | 196 → 219 |
| S01E04 La moelle osseuse et la leucémie | 35 | 12 | 14 | 5 | 3 | 1 | 20 | 31 | 196 → 219 |
| S01E05 Le sang, la circulation, la grippe | 26 | 14 | 5 | 4 | 2 | 1 | 11 | 21 | 180 → 206 |
| S01E06 Les plaquettes et la coagulation | 22 | 12 | 7 | 0 | 1 | 2 | 8 | 27 | 181 → 203 |
| S01E07 Le cœur et la circulation | 44 | 26 | 9 | 5 | 2 | 2 | 16 | 14 | 200 → 227 |
| S01E08 La respiration et l'invasion microbienne | 25 | 10 | 5 | 5 | 2 | 3 | 12 | 30 | 189 → 210 |
| S01E09 Le cerveau | 38 | 12 | 9 | 7 | 3 | 7 | 19 | 33 | 203 → 227 |
| S01E10 Les neurones et le système nerveux | 26 | 11 | 7 | 3 | 2 | 3 | 10 | 22 | 185 → 208 |
| S01E11 L'œil, la vision et les larmes | 38 | 20 | 9 | 3 | 2 | 4 | 14 | 13 | 193 → 213 |
| S01E12 L'oreille, l'audition et l'équilibre | 27 | 20 | 4 | 1 | 1 | 1 | 6 | 20 | 193 → 218 |
| S01E13 La peau | 46 | 21 | 15 | 5 | 2 | 3 | 17 | 36 | 208 → 231 |
| S01E14 La bouche, les dents et la carie | 25 | 16 | 6 | 1 | 1 | 1 | 8 | 22 | 194 → 217 |
| S01E15 La digestion et l'intestin | 30 | 14 | 8 | 3 | 4 | 1 | 15 | 34 | 214 → 234 |
| S01E16 Le foie et l'hépatite | 37 | 23 | 6 | 4 | 1 | 3 | 10 | 16 | 199 → 220 |
| S01E17 Les reins | 28 | 15 | 8 | 2 | 1 | 2 | 11 | 34 | 198 → 224 |
| S01E18 Le système lymphatique et la rate | 33 | 18 | 10 | 1 | 2 | 2 | 12 | 29 | 207 → 226 |
| S01E19 Le squelette, les os et les fractures | 32 | 15 | 9 | 4 | 2 | 2 | 15 | 18 | 198 → 226 |
| S01E20 Les muscles, l'effort, la sédentarité | 30 | 10 | 11 | 5 | 2 | 2 | 18 | 33 | 209 → 233 |
| S01E21 La pollution et la réparation de l'ADN | 34 | 25 | 3 | 2 | 1 | 3 | 6 | 33 | 206 → 229 |
| S01E22 Le tétanos et la vaccination | 32 | 20 | 8 | 2 | 1 | 1 | 10 | 14 | 201 → 226 |
| S01E23 Les hormones et les glandes endocrines | 34 | 21 | 7 | 2 | 2 | 2 | 11 | 22 | 207 → 231 |
| S01E24 Chaîne alimentaire, vitamines, équilibre | 34 | 16 | 11 | 4 | 2 | 1 | 16 | 25 | 209 → 240 |
| S01E25 Le sommeil, les rêves, le vieillissement | 34 | 23 | 7 | 1 | 1 | 2 | 9 | 19 | 198 → 227 |
| S01E26 La vieillesse, la transmission, l'espace | 31 | 16 | 9 | 3 | 1 | 2 | 12 | 67 | 203 → 234 |
| **Total** | **846** | **441** | **215** | **83** | **51** | **56** | **335** | **700** | **5 143 → 5 770** |

**Réserves de comptage.**

- Le décompte des recherches n'est pas homogène. Le quota `WebSearch` de session (200 appels) a été épuisé à partir de `S01E21` : les audits suivants ont procédé par récupération directe (`WebFetch`) de sources primaires — PubMed, NCBI Bookshelf, NASA, ANSES, OMS, INSEE — et déclarent ces récupérations dans le même compteur. `S01E26` déclare 67 recherches, record de la série, dont une part importante d'échecs (reCAPTCHA, HTTP 403, pages indisponibles) explicitement listés.
- `S01E07` et `S01E11` déclarent peu de recherches (14 et 13) pour beaucoup de faits (44 et 38) : les faits d'anatomie stable n'en demandaient pas.
- Les épisodes les plus solides sont `S01E06` (les plaquettes : **zéro fait erroné** sur 22 contrôlés), `S01E12` (l'oreille : un seul) et `S01E21` (la réparation de l'ADN : 25 confirmés sur 34). Les plus fragiles sont `S01E09` (le cerveau : 7 erronés, 7 non tranchés — moins d'un tiers de faits confirmés) et `S01E04`/`S01E20` (5 erronés chacun).

---

## 2. Les erreurs les plus lourdes, par gravité

### Niveau A — le mécanisme est faux, pas seulement le chiffre

Ce sont les corrections qui interdisent tout réemploi de la séquence telle quelle : le raisonnement de l'épisode s'effondre avec le fait.

| Fiche | Énoncé de l'épisode | État 2026 |
|---|---|---|
| S01E22 | « Le nerf ne transmet plus, rien ne répond. La ligne doit être coupée. » | La tétanospasmine ne coupe pas la ligne : elle clive la synaptobrévine des interneurones **inhibiteurs**. Elle supprime le frein, et les motoneurones déchargent sans retenue. Le tétanos est une paralysie **spastique** — exactement l'inverse de ce que l'épisode montre pendant vingt-cinq minutes. |
| S01E08 | « La vraie respiration se fait au cœur de la cellule, où l'oxygène est transformé en gaz carbonique » | L'oxygène n'est pas transformé en gaz carbonique : accepteur final d'électrons de la chaîne respiratoire, il se combine à des protons pour former de l'**eau**. Le CO₂ vient du cycle de Krebs, en amont. |
| S01E05 | « Les plaquettes empêchent la circulation de se bloquer » | Elles font exactement l'inverse : bloquer est leur métier. Adhésion à la brèche, activation, agrégation en clou plaquettaire. L'épisode inverse la fonction du personnage. |
| S01E20 | « Les plaquettes fluidifient la circulation quand les graisses circulent mal » | Même inversion, cinq épisodes plus loin. Les acides gras circulent fixés à l'albumine ; les plaquettes n'ont aucun rôle dans le transport des lipides. |
| S01E08 | « Une fois dans le sang, les envahisseurs échappent presque entièrement à la police du corps » | Le sang est au contraire l'un des compartiments les mieux surveillés de l'organisme : le complément y attaque directement les surfaces étrangères, et les neutrophiles y représentent 50 à 60 % des leucocytes. |
| S01E24 | « Dans la feuille, l'énergie lumineuse permet d'assembler oxygène et carbone » | La photosynthèse combine du **dioxyde de carbone et de l'eau**. L'eau est le donneur d'électrons, l'oxygène libéré en provient, et il est expulsé comme déchet — il n'entre pas dans le sucre. |
| S01E24 | « Le foie a besoin de lipides et d'acides gras pour fabriquer du cholestérol » | La synthèse part de l'acétyl-CoA par la voie du mévalonate, dont l'HMG-CoA réductase est l'étape limitante — celle des statines. Aucun apport lipidique n'est requis. |
| S01E16 | « Les virus substituent leur propre ADN pour changer les commandes du ribosome » | Le virus de l'hépatite A n'a pas d'ADN : c'est un virus à ARN simple brin positif, dont le génome sert directement d'ARN messager. |
| S01E04 | « Une erreur de programmation retourne les globules blancs contre le corps » | La leucémie ne retourne pas les défenseurs contre l'organisme : elle fait proliférer un clone bloqué dans sa maturation. Les cellules leucémiques n'attaquent rien — elles sont immatures et non fonctionnelles, d'où les infections. |
| S01E10 | « Le message emprunte l'arc réflexe et va au centre de commande sans passer par le cerveau » | L'arc de la toux ne contourne pas l'encéphale : les afférences vagales remontent au bulbe rachidien, où le groupe respiratoire ventral caudal intègre la commande avant de la redescendre. |
| S01E12 | « Les ions de sodium servent de messagers pour la transmission ; la cellule doit être polarisée pour les admettre » | Le courant de mécanotransduction des cellules ciliées est porté par le **potassium** : l'endolymphe est riche en K⁺, et son entrée dépolarise la cellule. Le calcium prend ensuite le relais. |
| S01E11 | « Le cerveau gauche voit à droite et le cerveau droit à gauche » | Le croisement porte sur le **champ visuel**, non sur l'œil : seules les fibres des hémirétines nasales décussent au chiasma, environ 53 % chez l'humain. Chaque œil envoie des fibres aux deux hémisphères. |
| S01E15 | « La pepsine est une enzyme spécialisée dans les protéines et n'agit pas sur le lait » | Les caséines du lait *sont* des protéines : la pepsine agit précisément sur elles, et c'est son action qui coagule le lait. L'épisode se contredit dans la même phrase. |
| S01E26 | « La force de gravité a sûrement cessé d'agir » | À 400 km d'altitude, la pesanteur terrestre vaut encore 88,8 % de sa valeur au sol. L'apesanteur est une chute libre partagée — d'où le terme de microgravité. |
| S01E13 | « C'est nous [les mélanocytes] qui fabriquons également les vitamines D » | Les kératinocytes sont les seules cellules à posséder la voie complète de la vitamine D. La mélanine, elle, **inhibe** sa synthèse UVB. |

### Niveau B — ordres de grandeur faux, par un facteur de 10 à 10³²

C'est la faiblesse dominante de la série : sur les dix chiffres spectaculaires qu'elle avance, dix sont faux, et neuf le sont par excès. La seule sous-estimation — les globules blancs produits chaque jour — est aussi le seul de ces chiffres qui ne servait pas à impressionner.

| Fiche | Énoncé | État 2026 | Facteur |
|---|---|---|---|
| S01E09 | « dix milliards de milliards de milliards de milliards de milliards de connexions » | 10¹⁴ à 5 × 10¹⁴ synapses. L'énoncé vaut 10⁴⁶ — davantage que le nombre d'atomes d'un corps humain | ×10³² |
| S01E05 | « sept cent mille globules blancs » par millimètre cube | 4 000 à 11 000. Le chiffre de l'épisode correspond au **rapport** globules rouges / globules blancs, non à un effectif | ×100 |
| S01E05 | « sept cent mille mètres carrés » de surface vasculaire | « Plus de mille mètres carrés » chez Jaffe, trois à sept mille pour les estimations les plus généreuses | ×100 à 700 |
| S01E03 | « un million de milliards de globules blancs » | 1,8 × 10¹² cellules immunitaires, pour environ 1,2 kg | ×500 |
| S01E03 | « quinze milliards [de globules blancs] par jour » | Environ cent milliards, presque tous des polynucléaires neutrophiles | ÷7 (sous-estimation) |
| S01E03 | « des bactéries bénéfiques, par millions » | 3,9 × 10¹³ bactéries — autant que de cellules humaines | ×10⁷ |
| S01E01 | « cinquante millions [de cellules] à chaque seconde » | Environ 3,8 millions par seconde — et le chiffre était déjà incompatible avec les « cinq cents milliards par jour » de la même phrase, qui n'en donnent que 5,8 millions | ×13, et incohérent |
| S01E26 | « À chaque seconde, des milliards de cellules » | Même erreur, en clôture de série : 0,33 × 10¹² cellules par jour, soit 3,8 millions par seconde | ×250 |
| S01E01, S01E02 | « soixante mille milliards de cellules » dans un corps humain | 36 000 milliards chez l'homme adulte, 28 000 chez la femme, 17 000 chez un enfant de dix ans | ×2 |
| S01E09 | « cent milliards de neurones » | 86,1 ± 8,1 milliards — et autant de cellules non neuronales, le rapport glie/neurones étant de 1 pour 1 et non de 10 pour 1 | proche, mais le rapport est faux ×10 |

### Niveau C — deux erreurs systématiques, répétées d'un bout à l'autre de la série

Voir § 3.1 et § 3.2 : ce ne sont pas des accidents de fiche, ce sont des motifs de scénario. Le « cerveau à trois étages » traverse quatre épisodes, la « carte HLA universelle » cinq.

### Niveau D — attributions et éponymes erronés

| Fiche | Énoncé | Ce qu'il en est |
|---|---|---|
| S01E07 | « Vésale parle le premier de la circulation en 1543, est condamné au bûcher, sauvé par Philippe II » | Vésale ne décrit pas la circulation ; la condamnation commuée en pèlerinage est une légende colportée par Hubert Languet en 1565 et rejetée par les biographes. Vésale meurt du typhus le 15 octobre 1564 à Zante. |
| S01E07 | « Michel Servet périt sur le bûcher, faute de protection royale » | Brûlé le 27 octobre 1553 au plateau de Champel, à Genève, sur sentence du Petit Conseil calviniste — non par l'Inquisition. Le motif est l'hérésie antitrinitaire. |
| S01E07 | « Cinquante ans après Harvey, Guy Patin enseigne encore que le sang ne circule pas » | Patin est doyen de 1650 à 1652, soit vingt-deux ans après le *De motu cordis*, et meurt en 1672. « Cinquante ans après Harvey » est chronologiquement impossible. |
| S01E13 | « Voilà trois siècles que Malpighi a su nous trouver » (les globules rouges) | Jan Swammerdam les décrit le premier en 1658, Leeuwenhoek précisément en 1674. Malpighi a découvert les capillaires, pas les hématies. |
| S01E11 | « Les lysosomes sont des enzymes nettoyeurs qui opèrent à la surface de l'œil » | Confusion de mots, fausse dès 1987 : le lysosome est un organite intracellulaire. L'agent décrit est le **lysozyme**, identifié par Fleming en 1922. |
| S01E13 | « Ruffini, récepteur de la chaleur ; Krause, le frigorifié » | Ruffini est un mécanorécepteur à adaptation lente de type II, qui détecte l'étirement cutané. La fonction thermique de Krause est aujourd'hui abandonnée. La chaleur est perçue par des terminaisons libres. |
| S01E13 | « Les corpuscules de Golgi, récepteurs des pressions légères » | Aucun mécanorécepteur cutané ne porte ce nom. La peau glabre en compte quatre encapsulés : Merkel, Meissner, Pacini, Ruffini. |
| S01E02 | « Les protéines fabriquées comprennent le collagène et l'ovalbumine » | L'ovalbumine est la protéine majoritaire du blanc d'œuf de poule, synthétisée par l'oviducte. Aucune cellule humaine n'en fabrique. |
| S01E19 | « Seuls trois des grands os de la jambe touchent le sol » | Aucun os de la jambe ne touche le sol : l'appui passe par le pied, dont les contacts forment un trépied — calcanéum, têtes des premier et cinquième métatarsiens. |
| S01E20 | « Contraction du vaste externe et du triceps » au bras droit | Le vaste externe — aujourd'hui vaste latéral — est le chef le plus volumineux du quadriceps fémoral : il est à la cuisse et étend le genou. |

---

## 3. Motifs récurrents dans la série

### 3.1 Le cerveau à trois étages — quatre épisodes, un mythe

C'est l'erreur la plus structurante du corpus `vie`. Le modèle « triunique » de Paul MacLean — un cerveau reptilien surmonté d'un cerveau paléomammalien lui-même surmonté d'un néocortex — irrigue :

- **S01E01**, qui le pose en exposé (« l'archicortex vient des reptiles, le paléocortex des mammifères ») et date le néocortex de « cinq cent mille ans » ;
- **S01E09**, qui en fait la structure entière de l'épisode, avec trois dates fausses (200 millions d'années pour l'archicortex, 100 millions pour le paléocortex, 100 000 ans pour le néocortex) et une morale (« le plus ancien de ses trois étages veut toujours dominer ») ;
- **S01E24**, qui le transforme en personnage — le « cerveau primitif » qui ordonne de se saisir de toute nourriture, insulté par le cerveau moderne (« ce fossile », « cet olibrius ») ;
- **S01E10**, qui en hérite l'idée d'une hiérarchie d'ancienneté entre centres nerveux.

La neuroanatomie comparée l'a démonté : les ganglions de la base existent chez tous les vertébrés actuels et non chez les seuls reptiles ; l'archicortex désigne en réalité l'hippocampe et le gyrus denté, propres aux mammifères ; le paléocortex est le cortex olfactif ; le néocortex à six couches était déjà présent chez les premiers mammifères, il y a quelque 200 millions d'années. Trois publications le qualifient explicitement de mythe (2020, 2020, 2022).

**Conséquence pour un scénariste** : le personnage est excellent et l'anatomie est fausse. Il faut l'assumer comme une fable, non comme une donnée. La fiche vérifiée le signale à chacune de ses quatre apparitions.

### 3.2 La carte HLA universelle — cinq épisodes, un contresens immunologique

Le motif du contrôle d'identité — un globule rouge présente sa carte HLA à un poste de garde — est l'un des plus beaux de la série et l'un des plus faux. Il apparaît dans **S01E03**, **S01E04**, **S01E17**, **S01E18** et par ricochet dans **S01E22**.

Deux erreurs à chaque fois. D'abord la distribution : les molécules HLA de classe I ne sont portées que par les cellules **nucléées**. Les globules rouges matures, personnages centraux de la série, ont expulsé leur noyau et n'en portent pas — c'est précisément ce qui permet la transfusion sans typage tissulaire, leur compatibilité relevant des systèmes ABO et Rhésus. Ensuite l'unicité : le système HLA est le plus polymorphe du génome humain, mais il n'est pas unique au monde — les vrais jumeaux l'ont identique, et deux personnes sans lien de parenté peuvent l'être aussi, ce qui rend possible la greffe entre donneur non apparenté.

`S01E04` pousse le contresens jusqu'à sa conséquence dramatique : un contrôleur démasque une cellule leucémique parce que « vous n'êtes pas de la même espèce que celle de notre corps ». Or les cellules leucémiques descendent des propres cellules du malade et portent exactement son HLA. C'est bien pourquoi son système immunitaire ne les élimine pas.

### 3.3 Les enzymes de restriction, outil bactérien devenu ouvrier du corps humain

Trois épisodes — **S01E04**, **S01E21**, **S01E25** — font appel à des « enzymes de restriction » pour réparer l'ADN ou l'ARN d'une cellule humaine. Elles n'existent que chez les bactéries et les archées, où elles découpent l'ADN des virus envahisseurs. Le génie génétique en a fait ses ciseaux à partir des années 1970, ce qui explique probablement leur présence dans la vulgarisation de l'époque. La réparation de l'ADN humain mobilise des glycosylases, des endonucléases AP, des polymérases et des ligases — plus MRE11, PARP1 et RAD51 pour les cassures double brin.

`S01E25` ajoute une seconde couche d'erreur en faisant réparer un « message ARN » par un procédé — couper, réapparier les bases, recoller — qui est celui de l'ADN.

### 3.4 Le microbiote, absent de 1987, omniprésent en 2026

C'est le plus grand angle mort de la série, et il traverse au moins six épisodes. `S01E03` parle de bactéries bénéfiques « par millions » là où il y en a 3,9 × 10¹³ ; `S01E15` leur fait digérer la cellulose (ce qu'elles ne font que marginalement chez l'humain) et fabriquer des vitamines « qu'on ne trouve pas dans les aliments » (ce qui est inexact) ; `S01E19` définit les bactéries comme des parasites ; `S01E24` et `S01E26` ignorent complètement la colonisation intestinale du nouveau-né par les bifidobactéries, nourries sélectivement par les oligosaccharides du lait maternel ; `S01E11` postule une surface oculaire stérile, alors qu'un microbiote résident y a été établi par séquençage.

La partition binaire entre bactéries amies et ennemies, que la série reprend partout, n'a plus cours : les bactéries se répartissent sur un continuum allant du mutualisme à la pathogénicité opportuniste. `S01E26` en donne l'exemple canonique en rangeant *Escherichia coli* parmi les amis sans réserve — alors que les souches entérohémorragiques provoquent colites hémorragiques et syndrome hémolytique et urémique.

### 3.5 Le renouvellement cellulaire, chiffré cinq fois et faux cinq fois

`S01E01` (deux fois), `S01E03`, `S01E15` et `S01E26` avancent chacun un chiffre de renouvellement ou d'effectif cellulaire. Aucun n'est exact. La série fonctionne à l'hyperbole numérique — c'est un procédé narratif assumé, la stupeur devant le très grand nombre —, mais le résultat est qu'aucun de ses chiffres spectaculaires n'est réutilisable tel quel. Les valeurs de référence de 2026, issues des travaux de Sender et Milo : 36 000 milliards de cellules chez l'homme adulte, 0,33 × 10¹² renouvelées par jour, 80 grammes de matière, dont près de 90 % de cellules sanguines et d'épithélium intestinal.

### 3.6 Ce que la série a eu raison de dire avant tout le monde

Le tableau serait injuste sans son revers. Plusieurs intuitions de 1987 ont été confirmées et outillées depuis :

- **Le cerveau qui trie pendant le sommeil** (`S01E25`) : les séquences de décharge des ensembles hippocampiques enregistrées à l'apprentissage sont bien rejouées pendant le sommeil, et l'on sait aujourd'hui rejouer un souvenir à la demande par réactivation ciblée.
- **Les défenseurs qui manquent d'énergie pour se dédoubler** (`S01E23`) : l'immunométabolisme a fait de cette réplique un champ constitué — le lymphocyte activé bascule vers une glycolyse aérobie intense pour financer son expansion clonale.
- **Le délai de l'ordre de satiété** (`S01E24`) : l'intuition d'un message lent était juste, et la raison en a été trouvée en 1994 et 1999 — ce sont des hormones, leptine et ghréline, non des influx nerveux.
- **Le corps réglé pour la rareté et débordé par l'abondance** (`S01E24`) : 2,5 milliards d'adultes en surpoids en 2022, l'obésité adulte ayant plus que doublé depuis 1990.
- **La difficulté à se rendormir avec l'âge** (`S01E25`) : le sommeil lent profond décline dès la quarantaine.
- **Le monde visuel flou du nouveau-né** (`S01E26`) : sensibilité au contraste très basse à la naissance, acuité proche de celle de l'adulte avant un an.

---

## 4. Ce que la biologie a ajouté depuis 1987

Ce que la série ne dit pas n'est pas faux : c'est ce qui n'existait pas encore. Les sections `Ce que l'on sait depuis` des 26 fiches convergent vers une douzaine d'apports majeurs.

| Domaine | Ce qui est arrivé après la diffusion |
|---|---|
| Vieillissement | Passage de l'usure et de l'« erreur catastrophique » d'Orgel (1963, sans soutien empirique) aux **douze repères du vieillissement** (2013, révisés en 2023) : des processus actifs, distincts, en partie modifiables |
| Sénescence | Phénotype sécrétoire des cellules sénescentes, sénolytiques, essais cliniques humains en cours |
| Âge biologique | **Horloges épigénétiques** fondées sur la méthylation de l'ADN (2011-2013), puis deuxième génération et horloges nucléosomiques (2024-2025) |
| Rajeunissement | Reprogrammation partielle par les facteurs de Yamanaka : des cellules humaines âgées redeviennent presque indiscernables de jeunes |
| Neurogenèse adulte | Le gyrus denté produit des neurones toute la vie — progéniteurs en prolifération directement identifiés en 2025 |
| Sommeil | **Système glymphatique** (2013, révisé 2025), rejeu hippocampique, orexine (1998) et ses antagonistes devenus somnifères, Nobel 2017 du rythme circadien |
| Faim et satiété | **Leptine** (1994), **ghréline** (1999), GLP-1 — et les agonistes du récepteur GLP-1 comme traitement de l'obésité |
| Endocrinologie | Le corps entier s'est révélé endocrine : cœur (1981), tissu adipeux (1994), estomac (1999), os, muscle en action (2012) |
| Microbiote | De 10¹³ à 10¹⁴ bactéries, 300 à 1 000 espèces, acides gras à chaîne courte, axe intestin-cerveau, dysbiose et obésité |
| Immunologie | **Immunoédition** (élimination, équilibre, échappement) en remplacement du « filtrage », tolérance périphérique en complément de la tolérance thymique |
| Hématologie | Chromosome Philadelphie et imatinib ; survie à cinq ans de la leucémie aiguë lymphoblastique de l'enfant au-delà de 90 % |
| Génomique | Séquençage du génome humain, transposons à 45 % du génome, Human Cell Atlas (des milliers de types cellulaires contre deux cents en 1987) |
| Transmission | ADN mitochondrial exclusivement maternel, microchimérisme maternel, marques épigénétiques |
| Astronomie | Plus de 6 000 exoplanètes confirmées depuis 51 Pegasi b (1995) — aucune n'était connue à la diffusion |

---

## 5. Non tranchés — 56 énoncés laissés intacts

Le référentiel impose de ne corriger que ce qu'une source confirme : « corriger à tort est pire que ne pas corriger ». Cinquante-six énoncés sont donc restés inchangés dans les fiches, avec dans chaque audit la mention de ce qui manquerait pour trancher. Trois familles se dégagent.

- **Les superlatifs non quantifiables.** « C'est bien les plus puissantes parmi les hormones » (`S01E23`) : il n'existe pas d'échelle permettant de comparer des hormones aux cibles, aux affinités et aux échelles de temps différentes. Trancher supposerait un critère explicite que ni l'épisode ni la littérature ne posent.
- **Les facteurs multiplicatifs sans étude.** « Mon corps mettra dix fois plus de temps que le vôtre à réparer cette coupure » (`S01E26`) : le ralentissement de la cicatrisation avec l'âge est bien documenté qualitativement, mais aucune source ne fournit de facteur, et une revue de 2024 signale au contraire que l'hypothèse d'une cicatrisation massivement déficiente chez le sujet âgé a été remise en cause.
- **Les métaphores sans référent identifiable.** « C'est complètement encrassé, ce tuyau. Avec le temps, tout s'engraisse » (`S01E25`) : selon qu'elle vise l'athérosclérose, l'accumulation de lipofuscine ou l'agrégation protéique, l'image est juste, approximative ou hors sujet. Faute de référent dans la source, elle ne peut être ni confirmée ni corrigée.

`S01E09` (le cerveau) concentre à lui seul 7 non tranchés sur 38 faits — la proportion la plus forte de la série, et le signe que les questions de conscience, de mémoire et de personnalité restent les moins tranchables du corpus.

---

## 6. Contrôle structurel

Les 26 fiches ont été contrôlées programmatiquement sur les critères du référentiel :

| Critère | Résultat |
|---|---|
| Les 11 sections `##` présentes dans l'ordre canonique | 26 / 26 |
| `## Ce que l'on sait depuis` en dernière position, ≥ 4 puces | 26 / 26 |
| Sections préservées identiques à l'octet (5 sections) | 26 / 26 |
| En-tête de vérification complet (fiche source, date, audit, avertissement) | 26 / 26 |
| Aucune URL, aucun marqueur de remplissage, aucun statut ✅/❌/🕰️/❓ | 26 / 26 |
| Audit présent et non trivial | 26 / 26 |
| Fiche jamais plus courte que sa source | 26 / 26 |

**Exceptions §3.1 tracées.** Le référentiel autorise à corriger une puce de `Procédés narratifs & ton` lorsqu'elle énonce en propre un fait sur le monde, à condition que l'audit la nomme. Trois occurrences dans la série, toutes tracées :

- `S01E17`, puce « Le problème posé avant la solution » — la « chance sur quatre » y était présentée comme la probabilité d'être nettoyé, alors qu'il s'agit de celle d'atteindre le rein ;
- `S01E24`, puce « Le scorbut comme démonstration » — « l'organisme ne sait pas fabriquer cette vitamine », énoncé sans restriction d'espèce ;
- `S01E24`, puce « Le conflit des deux cerveaux, rejoué » — attribuait l'ordre alimentaire à l'archicortex.

Hors ces trois puces, `Procédés narratifs & ton` est intégralement préservée sur les 26 fiches.

**Intégrité de la source.** Contrôle md5 sur les 223 fichiers de `/data/origo/fiches/` après la campagne : **223 / 223 conformes à la ligne de base**. Aucune écriture dans le répertoire source.

---

## 7. Fiches à reprendre

Aucune fiche ne présente d'anomalie bloquante. Deux réserves méthodologiques sont consignées pour mémoire.

1. **Le décompte des recherches n'est pas comparable d'une fiche à l'autre** à partir de `S01E21`, le quota `WebSearch` de session ayant été épuisé et remplacé par des récupérations directes comptées dans le même total. Les audits concernés le déclarent explicitement.
2. **Les huit dernières fiches (S01E19 à S01E26) ont été réécrites manuellement**, sans workflow, à partir des audits déjà produits. Les vérifications qu'elles appliquent sont donc celles des audits, écrits antérieurement ; aucune vérification nouvelle n'a été conduite lors de la réécriture. Ce point n'affecte pas la traçabilité — toute correction présente dans ces fiches a sa ligne dans l'audit correspondant — mais il signifie que les corpus de sources n'ont pas été rafraîchis entre l'audit et la réécriture.

## 8. Points de vigilance pour les séries restantes

Ce que `vie` enseigne pour `homme` (1978), `explorateurs` (1996) et `objets` :

- **Tout chiffre spectaculaire est à revérifier par principe.** La série ne s'est jamais trompée par pudeur : ses erreurs numériques vont toutes dans le sens de l'exagération, d'un facteur 10 à un facteur 10³². `homme`, plus ancien de neuf ans, devrait être pire.
- **Chercher les motifs, pas seulement les faits.** Les deux erreurs les plus lourdes de `vie` — le cerveau triunique et la carte HLA — ne sont visibles qu'en lisant plusieurs épisodes ensemble. Un audit fiche par fiche les corrige cinq fois sans jamais les nommer comme système. `homme` (1978), qui traite de préhistoire, portera très probablement un motif équivalent sur l'évolution linéaire de l'hominisation.
- **Les éponymes et les récits de découverte sont le point faible absolu.** `S01E07` accumule quatre erreurs historiques en une seule séquence (Vésale, Servet, Patin, la chronologie de Harvey). `decouvreurs` avait le même profil. Pour `explorateurs`, prévoir un contrôle systématique de chaque date, chaque attribution et chaque anecdote de bûcher.
- **Distinguer ce que l'épisode dit de ce que la fiche source en a fait.** Plusieurs corrections de cette campagne portent sur des incises ajoutées par la fiche et non sur l'épisode — ainsi `S01E05`, où l'incise « l'épisode dit *le diamètre* ; l'ordre de grandeur correspond plutôt à la circonférence » inversait le rapport et avait tort contre l'épisode.
