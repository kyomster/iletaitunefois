# Références D, J et K — audit des 15 images

**23 août 2026.** Point d'arrêt dur de l'étape 3. Les quinze références lues une par une en 1000 px de large, avant d'en dériver quoi que ce soit. Grille : les 13 contrôles de `METHODE-generation-images.md` §20, plus la mise en page attendue par asset.

**Verdict global : 14 validables sur 15, une à reprendre.** Trois corrections de prompt à porter avant les 60 images clés.

---

# 1. Les trois constats transversaux

## 1.1 Le manteau du maigre sort en sarcelle en J et en K

Le badaud maigre porte un **manteau bleu sarcelle délavé** dans les deux styles réalistes. En D il est vert olive, conforme.

Deux styles sur trois sur le même asset : par la RÈGLE 7, la cause est dans le prompt. Elle est claire. La fiche Parieurs dit `threadbare coat` et **ne nomme aucune couleur**. Les négatives `dominant teal outfit, saturated teal clothing` sont posées, et elles n'y font rien, parce que le sarcelle sorti est **désaturé** : il passe sous la négative tout en étant la couleur dominante du personnage.

C'est exactement la RÈGLE 30, constatée jusqu'ici sur des figurants de foule et qui se révèle ici sur un personnage nommé. Correction, à porter dans le bloc identité Parieurs pour tous les styles réalistes :

```
the thin onlooker on the right leaning on a cane, threadbare coat in muted brown and grey only, no blue and no green on any garment, suspicious squint
```

**Ce n'est pas cosmétique.** Le sarcelle vif appartient à Naya, et le maigre est présent au plan 2 et au plan 63. Un personnage d'époque en sarcelle dominant casse la convention de couleur réservée sur laquelle repose l'identification de la troupe.

## 1.2 Les bandes noires ne se corrigent ni en négative, ni en positif

| Image | Bandes |
|---|---|
| `D01_StyleJ` | haut et bas |
| `D02_StyleJ` | gauche et droite |
| `D01_StyleK` | haut et bas, fines |
| les 12 autres | aucune |

La négative `letterbox bars, black bars` était posée. La clause positive `the image fills the entire 16:9 frame edge to edge, no black bars` était posée aussi. **Les deux ont échoué.**

Conclusion : sur un style qui se décrit comme du cinéma, les bandes sont une **propriété du référent**, pas un élément de l'image. Ni une négative ni une clause positive ne les enlèvent. Deux issues, à trancher :

* **rogner en local** après coup, ce qui coûte zéro crédit et se scripte en une ligne ; les plaques repartent alors à 2752 × 1440 environ, à réétirer en 16:9 ;
* **retirer du bloc J tout vocabulaire de format** — `cinema`, `35mm`, `photographed on` — et ne garder que la description optique. Risque : perdre la facture qui fait le style.

La première est la seule sûre. Elle entre en méthode comme corollaire de la RÈGLE 33.

## 1.3 Aucun lettrage sur les quinze

La négative universelle tient. La RÈGLE 33 ne s'était déclenchée que sur des bannières ; aucune plaque de décor ni aucune fiche n'en porte ici.

---

# 2. Style D — 5 sur 5

| Asset | Verdict | Observation |
|---|---|---|
| `D01_StyleD` | ✔ | aube d'octobre, brume basse, ballon gonflé, nacelle posée à part, cordes au sol, allées, aucun personnage. Écart de facture : le rendu est plus **lavis** que le bloc D, qui prescrit un trait brun et un ombrage cel. Sur un décor c'est acceptable ; à vérifier au raccord avec les personnages D. |
| `D02_StyleD` | ✔ | toits de Paris, parc en tache verte, ciel pastel, vide. Même réserve de facture. |
| `Foule_StyleD` | **à surveiller** | fond gris, douze figures, parapluie fermé, aucun visage lisible. **Mais un homme de face au centre a un ovale de peau vide**, et une femme à sa droite est de trois quarts face. Formellement conforme au corollaire de la RÈGLE 26, des figurants sans aucun trait ne sont pas des visages lisibles. Sur un style à visages détaillés, ça se verra en plan rapproché. |
| `Garnerin_StyleD` | ✔ | quatre vues, identité constante, cheveux noués, foulard pâle, habit sombre, culotte, souliers à boucle. Aucune vue fautive. |
| `Parieurs_StyleD` | ✔ | rond à gauche, chapeau à cocarde, maigre à droite, canne et manteau râpé **vert olive**. Conforme à la fiche. |

---

# 3. Style J — 5 sur 5, deux réserves

| Asset | Verdict | Observation |
|---|---|---|
| `D01_StyleJ` | ✔ | la plus belle des quinze. Aube brumeuse, ballon rayé, nacelle, cordes, allée de gravier, fabriques de pierre, pas un humain. Bandes noires haut et bas, §1.2. |
| `D02_StyleJ` | ✔ | toits d'ardoise, cheminées fumantes, square vert. Bandes latérales. **Écart d'époque à noter** : réverbères allumés et square régulier, plus proches de 1850 que de 1797. Mineur sur une plaque de fond. |
| `Foule_StyleJ` | ✔ **exemplaire** | douze figurants, **tous de dos sans exception**, aucun visage, fond gris uni. La clause durcie du §5.1 fonctionne. Deux écarts mineurs : le parapluie est **ouvert** alors que la fiche dit `one closed umbrella`, et une robe **orange terreux** à droite, désaturée donc non dominante mais à la limite. |
| `Garnerin_StyleJ` | ✔ | quatre vues du même comédien, même visage, même costume, fond studio uni. **C'est exactement la référence de casting qu'il fallait**, et elle répond à la question ouverte du §3.1 de l'état de préparation : le mécanisme du dépôt fonctionne tel quel sur un visage photoréaliste. |
| `Parieurs_StyleJ` | ✔ avec réserve | rond avec chapeau à cocarde et gilet clair, maigre avec canne et manteau déchiré. Les deux visages sont excellents. **Manteau sarcelle sur le maigre**, §1.1. |

---

# 4. Style K — 4 sur 5, une à reprendre

| Asset | Verdict | Observation |
|---|---|---|
| `D01_StyleK` | ✔ | brume, ballon doré au filet, nacelle d'osier au premier plan, cordes, fabriques néoclassiques. Bandes fines haut et bas. |
| `D02_StyleK` | ✔ | toits, lucarnes, parc au fond, aucune bande. Très bon. |
| `Foule_StyleK` | **✘ À REPRENDRE** | le groupe est **dupliqué** : une seconde rangée identique flotte au dessus de la première, floue. C'est le défaut `repeated figure, ghost figures` que la négative de fiche visait explicitement, et elle n'a pas tenu. Le reste est conforme, tous de dos, aucun visage. **2 crédits.** |
| `Garnerin_StyleK` | ✔ | quatre vues, matière de tissu visible, visage crédible sans caricature, cohérence parfaite entre les vues. |
| `Parieurs_StyleK` | ✔ avec réserve | le rond a un gilet à motif et la cocarde, le maigre la canne et les bottes. Excellents. **Manteau sarcelle sur le maigre**, §1.1. |

---

# 5. Ce qui est acquis, et qui va au delà des images

**La question ouverte sur le style J est répondue.** L'état de préparation §3.1 disait qu'on ne savait pas ce qui verrouillerait l'identité d'un visage photoréaliste sur 79 plans. `Garnerin_StyleJ` montre que le mécanisme du dépôt fonctionne sans changement : quatre vues du même comédien, produites en un tirage, réinjectables comme n'importe quelle fiche. La référence de casting **est** une fiche de personnage, elle n'appelle pas de dispositif nouveau.

Reste à vérifier à l'étape 4 que la ressemblance tient sur vingt plans successifs, ce qu'aucune fiche seule ne peut prouver.

---

# 6. Corrections à porter avant les 60 images clés

1. **Bloc identité Parieurs**, styles réalistes : nommer la couleur du manteau du maigre en positif, §1.1.
2. **Rognage des bandes noires** en local sur `D01_StyleJ`, `D02_StyleJ` et `D01_StyleK`, avant réinjection. Une plaque avec bandes réinjectée impose ses bandes à tous les plans qui la réinjectent (RÈGLE 1).
3. **Reprendre `Foule_StyleK`**, 2 crédits, prompt inchangé, avec en plus la négative `second row of figures, duplicated group, mirrored copy of the group`.

Facultatif, à trancher : reprendre `Foule_StyleD` pour supprimer les deux figures de face à visage vide, et `Foule_StyleJ` pour fermer le parapluie. Ni l'un ni l'autre n'est bloquant.
