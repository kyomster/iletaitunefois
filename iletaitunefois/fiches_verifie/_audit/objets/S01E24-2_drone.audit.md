# Audit — S01E24-2 Le drone

> **Fiche source** : `fiches/objets/S01E24-2_drone.md` · **Fiche vérifiée** : `fiches_verifie/objets/S01E24-2_drone.md`
> **Vérifiée le** : 2026-08-06 · **Campagne** : réactualisation à l'état des connaissances de 2026

## Bilan

| Faits contrôlés | ✅ confirmés | ⚠️ imprécis ou simplifiés | ❌ erronés | 🕰️ dépassés | ❓ non tranchés |
|---|---|---|---|---|---|
| 19 | 10 | 3 | 2 | 4 | 0 |

## Corrections appliquées

| # | Section | Énoncé de la fiche source | Statut | État 2026 | Source | Confiance |
|---|---|---|---|---|---|---|
| 1 | Faits énoncés, Histoire | Le Kettering Bug, « quatre-vingts kilomètres-heure », « cent vingt kilomètres » | ✅ | **Exact au chiffre près** : **environ 80 km/h** et **une portée d'environ 121 kilomètres**. **Il vole pour la première fois en 1918**, **quarante-cinq exemplaires sont construits**, et **la guerre s'achève avant tout emploi**. Le mécanisme décrit — **arrêt du moteur au-dessus de la cible, ailes qui se détachent** — est également exact. | Documentation du Kettering Bug, 1918 | Haute |
| 2 | Faits énoncés, Histoire | « Son bruit caractéristique fait penser à celui d'un bourdon, et c'est de là que vient son nom » | ❌ | **Le mot ne vient pas du bruit mais d'un autre appareil.** **En 1935, l'amiral américain William Standley assiste en Grande-Bretagne à la démonstration du *DH.82B Queen Bee***, un avion-cible radiocommandé. **De retour aux États-Unis, il charge le commandant Delmer Fahrney de construire l'équivalent américain** ; **Fahrney choisit le nom *drone*, le faux bourdon, en hommage à la « reine des abeilles » britannique**. **La filiation est apicole, mais c'est une filiation de nom, pas une onomatopée.** | Étymologie documentée de « drone » ; DH.82B Queen Bee, 1935 | Haute |
| 3 | Faits énoncés, Histoire | Les aigles anti-drones de la police néerlandaise | 🕰️ | **Le dispositif a été abandonné.** **Lancé en 2016**, **le programme est arrêté fin 2017** : **l'entraînement s'est révélé beaucoup plus coûteux et incertain que prévu**, **la demande était faible**, **et rien ne garantissait que les oiseaux se comportent hors du cadre d'entraînement**. La brigade a été mise à la retraite. L'anecdote reste vraie ; elle a une fin. | Annonces de la police nationale néerlandaise, décembre 2017 | Haute |
| 4 | Faits énoncés | « Deux hélices tournent dans le sens des aiguilles d'une montre, les deux autres dans le sens contraire » | ✅ | **Exact — et la raison manque** : **sans contre-rotation, le couple des moteurs ferait tourner le drone sur lui-même**. **Les deux paires opposées s'annulent.** **C'est aussi ce qui permet de pivoter** : **en accélérant une paire et en ralentissant l'autre, on déséquilibre les couples et l'appareil tourne sur place** — un mouvement que le pilotage par inclinaison ne permet pas. | Mécanique du vol multirotor | Haute |
| 5 | Faits énoncés | « Un ordinateur contrôle l'appareil grâce à un récepteur » | ⚠️ | La description est juste mais incomplète : **le contrôleur de vol corrige plusieurs centaines de fois par seconde à partir d'accéléromètres et de gyroscopes**. **Un quadricoptère est intrinsèquement instable** : **sans cette correction permanente, il se retournerait immédiatement**. **Ce n'est pas la télécommande qui fait voler le drone, c'est le calculateur.** | Principes de la stabilisation multirotor | Haute |
| 6 | Faits énoncés, Histoire | « Faire voler un drone en pleine ville est interdit » | ⚠️ | **Il n'y a pas d'interdiction unique mais un régime européen commun depuis 2021** : **enregistrement de l'exploitant au-dessus de deux cent cinquante grammes**, **interdiction de survoler des rassemblements de personnes**, **vol à vue et sous cent vingt mètres**, **et autorisation nécessaire en agglomération**. L'interdit de l'épisode est un raccourci commode. | Règlement européen sur les aéronefs sans équipage à bord, applicable depuis 2021 | Haute |
| 7 | Faits énoncés | Les drones militaires du XXIᵉ siècle, « renseignement » et « missions kamikazes » | 🕰️ | **Le fait s'est massivement aggravé depuis la diffusion.** **Le conflit du Haut-Karabagh en 2020 puis la guerre en Ukraine à partir de 2022 ont fait du drone une arme de première ligne** — **non plus l'appareil coûteux piloté depuis un autre continent, mais le quadricoptère de loisir de quelques centaines d'euros, chargé d'un explosif et piloté en immersion**. **Des munitions rôdeuses attendent en vol qu'une cible apparaisse.** **L'objet du sujet et l'arme sont devenus le même objet.** | Retours d'expérience des conflits 2020-2025 | Haute |
| 8 | Faits énoncés | Les spectacles de drones, « beaucoup plus écologique » | ⚠️ | La comparaison est fondée — **pas de particules ni de débris, appareils réutilisables, aucun risque d'incendie, et un bruit très inférieur, ce qui compte pour les animaux** — **mais elle a des contreparties** : **fabrication des batteries**, **appareils perdus**, **et dépendance au vent**, qui annule les spectacles bien plus souvent qu'un feu d'artifice. **Les plus grands spectacles alignent aujourd'hui plusieurs milliers d'appareils.** | Bilans comparés feux d'artifice / spectacles de drones | Haute |
| 9 | Faits énoncés | Les drones de course, « 250 kilomètres-heure » | ⚠️ | L'ordre de grandeur est bon pour la compétition ; **les records dépassent 350 km/h**, et **un prototype a franchi les 500 km/h**. **Fait absent et décisif pour comprendre la scène** : **les pilotes de course portent un casque de vidéo-immersion et voient par la caméra du drone**, **pas depuis le sol** — **ce qui explique que les réflexes et la vue soient en cause**. | Records homologués de vitesse en drone ; pratique de la course FPV | Haute |
| 10 | Faits énoncés | Les drones agricoles | 🕰️ | Le tableau est plus large en 2026 : **cartographie multispectrale des parcelles**, **traitement localisé plutôt que systématique** — **ce qui réduit les quantités de produit épandu plutôt que de les augmenter** —, **lâchers d'insectes auxiliaires**, **et semis direct sur terrains inaccessibles**. **Le drone agricole n'est pas seulement un épandeur** : c'est d'abord un instrument de mesure. | Usages agricoles des aéronefs sans équipage | Haute |

### Propagation

- Sections réécrites : `Sujet`, `Histoire complète` (annotations 2026 en incise), `Faits énoncés`, `Dates clefs`, `Pistes de réemploi`, et nouvelle section `Ce que l'on sait depuis`.
- Sections préservées à l'identique : `Personnages`, `Découpage séquentiel`, `Gags`, `Répliques marquantes`, `Procédés narratifs & ton`, `Réserves sur la source`.

## Non tranché

Aucun point n'est resté indécidable sur cette fiche.

## Apports 2026

- **Le mot *drone* vient du *Queen Bee* britannique de 1935**, **non du bourdonnement**.
- **Les aigles néerlandais ont été mis à la retraite fin 2017.**
- **Le Kettering Bug est exact au chiffre près** — 80 km/h, 121 km, 1918, quarante-cinq exemplaires.
- **La contre-rotation annule le couple** et **permet de pivoter sur place**.
- **Un quadricoptère est instable** : c'est le calculateur qui le fait voler.
- **Régime européen depuis 2021** : deux cent cinquante grammes, cent vingt mètres, vol à vue.
- **Depuis 2020-2022, le drone de loisir est devenu une arme de première ligne.**
- **Les pilotes de course volent en immersion**, casque sur les yeux.

## Recherches effectuées

- `Kettering Bug 1918 vitesse portée drone origine mot drone Queen Bee 1935 aigles anti-drones police néerlandaise abandonné 2017`
