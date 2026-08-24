# Pilote S01E01 en style D — audit des 20 images clés

**24 août 2026.** Grille : les 13 contrôles de `METHODE-generation-images.md` §20. Images lues une par une, fichiers dans `assets/S01E01/pilote/images/StyleD/`, toutes en 2752 × 1536. Prompts dans `prompts/S01E01-pilote-prompts-DJK.md`.

**Verdict : 19 validables sur 20.** Une reprise, `P5-1`, pour un défaut qui a une histoire.

---

# 1. Le défaut, et ce qu'il révèle

## `P5-1` portait « D2 » écrit en grosses lettres sur un second ballon

Gros plan sur la main qui saisit le couteau. Au fond, un **deuxième ballon** dont l'enveloppe porte **« D2 »** en capitales hautes de trois cents pixels.

C'est la RÈGLE 28 mot pour mot : *un code de décor ne tient pas sur un très gros plan, la référence D02 n'a presque pas de surface pour s'imposer et le code devient du texte.* Et la négative universelle anti lettrage n'y fait rien, parce que le modèle ne lit pas `D2` comme une consigne mais comme le contenu de l'image.

**Le plus instructif est l'historique.** La correction du 22 août avait développé `D2` en clair sur `P5-2` et `P5-3`, exactement pour cette raison, et **avait oublié `P5-1`**. Les trois briques étaient censées être traitées ensemble ; deux l'ont été. En styles A, B et C le plan est sorti correct par chance, donc personne ne l'a vu, et le défaut est resté dormant dans le générateur pendant deux jours.

> **Corollaire de la RÈGLE 28.** Une correction qui vise une classe de plans se vérifie **sur toute la classe**, pas sur les plans où le défaut s'était manifesté. Ici la classe est « tout plan dont le décor est flou derrière un très gros plan », soit 5‑1, 5‑2, 5‑3 et 4b‑2. Trois avaient été corrigés, un non.

Brique corrigée, avec le développement en clair **et** la clause anti second ballon déjà présente sur 1b‑3 et 5‑2 :

```
Decor: D2, the sky and the rooftops of Paris far below, out of focus behind, no other balloon and no other basket anywhere in the frame.
```

---

# 2. Ce que l'audit confirme de positif

* **La correction de `P1a-1` a pris.** Une seule nacelle, posée sur l'herbe sous le ballon, plus aucun panier parasite. La RÈGLE 29 se corrige bien en nommant l'état voulu.
* **`P1b-2` tient le piège le plus difficile du pilote.** Deux aides portent UNE nacelle vers un ballon qui n'a **qu'un cerceau vide** sous lui. C'est le plan qui avait donné deux nacelles dans les trois styles A, B et C en août. La clause `toward the balloon hanging above with no basket under it yet` fonctionne.
* **`P1a-3` sort en contre plongée sur la couronne**, avec les bannières en aplats et **sans aucun lettrage**. La RÈGLE 32 tient, et la RÈGLE 33 ne se déclenche pas sur un style non réaliste : les bannières de D sont des banderoles peintes, pas des étendards brodés.
* **Aucun visage lisible dans aucune foule**, sur les sept plans qui en portent une. La clause d'origine des styles A, B et C est confirmée sûre sur un style à visages détaillés.
* **RÈGLE 31 respectée.** `P02` a les deux bouches fermées ; `P02a` et `P02b`, les clés de champ contrechamp, ont la bouche du locuteur ouverte, ce qui est la décision du 22 août pour la synchro labiale.
* **Le raccord avec les plaques est excellent.** Les onze plans qui réinjectent D01 partagent la même aube brumeuse, les mêmes arbres nus d'octobre, la même architecture au fond. Les six qui réinjectent D02 partagent le même Paris ambré.
* **Aucun lettrage sur les vingt**, hors le défaut de `P5-1`.

---

# 3. Une réserve de raccord, à trancher au montage

`P5-2` est en **ciel bleu pâle et ville grise**, alors que `P5-1` et `P5-3`, qui l'encadrent immédiatement, sont en **ambre chaud**. Les trois sont dans le même bloc et donc dans le même registre TENSION, mais le tirage de 5‑2 a interprété `palette pulled to warm amber or to near black` du côté froid.

Ce n'est pas un défaut de prompt, c'est une variance de tirage sur une clause qui offre deux issues. Deux façons de la fermer :

* **au montage**, par un étalonnage de 5‑2 vers l'ambre, gratuit ;
* **au prompt**, en retirant `or to near black` du registre TENSION de D, ce qui supprime l'alternative mais durcit tous les plans en l'air.

La première est préférable tant que le style n'est pas choisi.

---

# 4. Le compte

| Poste | Images | Crédits |
|---|---|---|
| Essai de réinjection, 3 plans | 3 | 6 |
| Lot principal | 18 | 36 |
| Reprise de `P5-1` | 1 | 2 |
| **Pilote D complet** | **20 images** | **44 crédits** |

Solde après le pilote D : **642 crédits**.

---

# 5. Ce qui attend J et K

Les deux corrections de brique découvertes ici, `P1a-1` et `P5-1`, sont **dans le générateur** et s'appliqueront donc automatiquement à J et à K. C'est le bénéfice d'avoir produit un style entier avant les deux autres : les deux défauts ont été payés une fois, pas trois.

Reste à surveiller, spécifique à J : les vingt plans passent par un décor réel, et deux des trois plaques J avaient déjà ramené des anachronismes. Le contrôle d'époque sera le poste lourd de l'audit J.
