# Styles D, J et K — ce qui manque pour produire le pilote

**23 août 2026.** Réponse à une question simple : les trois styles retenus ont ils de quoi produire les plans 1 à 6 ?

**Non.** Réponse d'origine : ils avaient leurs blocs de style, et rien d'autre.

**Mise à jour du 23 août au soir** : tout ce qui ne coûte pas de crédit est fait. Les deux générateurs connaissent les six styles, les onze corrections de l'audit sont portées, les registres de tension sont écrits, et les deux nouvelles règles sont dans la méthode. Vérifié par exécution à blanc, sans régression sur A, B et C.

**Il manque encore les images** : 5 références et 20 images clés par style, soit 150 crédits pour les trois. Le détail suit, sections barrées pour ce qui est fait.

---

# 1. Une bonne nouvelle d'abord : la troupe n'est pas un préalable

Le pilote est en **registre ÉPOQUE de bout en bout**, sauf le carton du plan 6. Sam, SamBis, Naya et Elio **n'apparaissent dans aucun des six plans**. Les 40 assets de bible par style, les turnarounds, les six expressions ne bloquent donc pas le pilote.

Cela corrige ce que `PLAN-styles-D-E-F.md` laissait entendre en ordonnant l'étape 2 avant l'étape 4. Les deux sont en réalité **indépendantes** :

* l'épreuve de troupe est le **test le moins cher** pour éliminer un style, 8 crédits ;
* le pilote est le test le plus **complet**, mais il ne dit rien de la troupe.

On peut donc lancer le pilote sans la troupe. On ne peut pas lancer l'**épisode** sans elle.

---

# 2. Ce qui existe pour D, J et K

| Élément | État |
|---|---|
| Bloc de style, traitement d'époque, base négative | ✔ `PLAN-styles-D-E-F.md` §4.1, §4.7, §4.8 |
| Traitement de lumière à deux registres | ✔ **pour les trois**, écrits le 23 août |
| Briques des 20 plans | ✔ invariantes, communes à tous les styles, dans `prompts/S01E01-pilote-prompts-assembles.md` |
| Briques de mouvement des 16 clips | ✔ invariantes, dans `scripts/build_clips_pilote.py` |
| Voix ElevenLabs des plans 2 et 3 | ✔ indépendantes du style, 4 mp3 dans `pilote/audio/` |
| Graphes ComfyUI I2V et FLF2V | ✔ indépendants du style, `docs/runpod/` |
| Générateurs de prompts, image et clip | ✔ étendus aux six styles le 23 août, vérifiés sans régression |
| Images clés | **3 sur 20 par style**, et il faut de toute façon refaire les vingt, §3.2 |

---

# 3. Ce qui manque, poste par poste

## 3.1 Les cinq références à réinjecter — **FAIT, les 15 validées le 23 août**

Les quinze existent et sont validées une par une, audit dans `S01E01-references-DJK-audit.md`. Coût réel **38 crédits** au lieu de 30 : `Foule_StyleK` et `D02_StyleJ` ont demandé trois tirages chacune, pour deux défauts de structure qui ont chacun donné un corollaire de méthode.

Table §5 de `S01E01-pilote-prompts-3-styles.md`, pour mémoire :

| Brique | Fichier attendu | Plans qui la réinjectent |
|---|---|---|
| Décor sol | `decors/Style{D,J,K}/D01_Style*.png` | 1a, 1b, 2, 3, 4a |
| Décor ciel | `decors/Style{D,J,K}/D02_Style*.png` | 4b, 5 |
| Foule | `personnages-episode/Style*/Foule_Style*.png` | 1a, 1b, 2, 4a |
| Garnerin | `personnages-episode/Style*/Garnerin_Style*.png` | 3, 4a, 4b, 5 |
| Parieurs | `personnages-episode/Style*/Parieurs_Style*.png` | 2 |

C'est le poste le plus structurant : **sans ces cinq plaques, les vingt plans dérivent**, c'est la RÈGLE 27 et la RÈGLE 29. Et chacune est un point d'arrêt : elle se regarde avant qu'on en dérive quoi que ce soit.

**Cas particulier de J, tranché.** On se demandait ce qui verrouillerait l'identité d'un visage photoréaliste sur 79 plans. `Garnerin_StyleJ` répond : quatre vues du même comédien, même visage, même costume, en un tirage, réinjectables comme n'importe quelle fiche. **La référence de casting est une fiche de personnage**, elle n'appelle aucun dispositif nouveau. Reste à vérifier à l'étape 4 que la ressemblance tient sur vingt plans successifs, ce qu'aucune fiche seule ne prouve.

**Coût de contrôle propre à J, découvert aux reprises.** Deux des trois plaques J ont porté un défaut qui vient du photoréalisme lui même, des bandes de cinéma puis des voitures et un passage piéton dans une rue de Paris. Sur les 46 décors d'un épisode, **tout plan J qui montre le sol d'une ville réelle devra être contrôlé pour l'anachronisme**. D et K n'ont pas ce coût.

## 3.2 Les images clés — 17 manquantes par style, 34 crédits

Il en faut 20 : `P1a-1` à `P1a-4`, `P1b-1` à `P1b-3`, `P02`, `P02a`, `P02b`, `P03`, `P4a-1` à `P4a-3`, `P4b-1` à `P4b-3`, `P5-1` à `P5-3`.

Les 3 existantes sont des images d'épreuve produites **sans référence réinjectée** et avec un décor développé en clair. Elles ne raccorderont pas avec les 17 autres, qui elles réinjecteront les plaques. **Il faut les refaire toutes les vingt**, donc 40 crédits par style et non 34.

## 3.3 Les deux scripts — **fait le 23 août**

Les deux générateurs connaissent désormais les six styles, et acceptent `--styles=StyleD,StyleJ,StyleK` pour n'en assembler qu'une partie.

* `scripts/build_prompts_pilote.py` — blocs de style, traitements d'époque, bases négatives de D, J et K ; **table `LUMIERE` et `REGISTRE_LUMIERE`**, qui appliquent le registre JOUR ou TENSION selon le bloc du plan et non selon le tirage ; variante d'identité `JK` pour la foule des styles réalistes ; clause de bannières de la RÈGLE 33 posée sur P1a-3 en J et K seulement.
* `scripts/build_clips_pilote.py` — mêmes six styles dans `STYLE` et `STYLE_REDUCED`, plus une constante `STYLES_BLOC_REDUIT_OBLIGATOIRE` qui ne contient que `StyleB`, le seul cas vérifié.

**Vérification par exécution à blanc, faite.** 120 prompts d'image et 48 clips assemblés avec des media_id factices. Les 60 prompts A, B et C sortent **identiques au caractère près** à `prompts/S01E01-pilote-prompts-assembles.md`, et les 48 clips A, B et C ont les mêmes modes, longueurs et graines que `prompts/S01E01-pilote-clips-prompts.md`. Aucune régression.

**Le `STYLE_REDUCED` reste un piège ouvert.** Le style B a exigé un bloc **réduit** pour la vidéo : le bloc complet faisait fabriquer des têtes d'inkman partout par Wan 2.2, 12 clips sur 16 inutilisables, 12 sur 12 corrects avec le bloc réduit. Des blocs réduits ont été écrits pour D, J et K, mais **ils ne sont pas vérifiés**, et rien ne dit que ces trois styles souffrent du même défaut. À trancher sur **un** clip d'essai par style, jamais sur les seize.

## 3.4 Les corrections de l'audit — **portées le 23 août**

1. ✔ **RÈGLES 32 et 33** versées dans `METHODE-generation-images.md`, nouvelle section 22. Le dépôt compte désormais 33 règles, le décompte est à jour dans le README, le runbook et l'index.
2. ✔ **D**, traitement JOUR amputé de `bright daylight, saturated blue sky with tall billowing cumulus clouds`. L'heure appartient au décor, le traitement ne règle que la qualité de la lumière.
3. ✔ **D**, retour à la clause de foule des styles A, B et C. L'épreuve a montré que la variante en silhouettes floues ne prenait pas, et que la clause d'origine est sûre même sur un style à visages détaillés.
4. ✔ **J**, `the image fills the entire 16:9 frame edge to edge, no black bars` posé en positif dans le bloc de style.
5. ✔ **J et K**, clause de bannières posée sur P1a-3.
6. ✔ **J et K**, foule durcie en positif.
7. ✔ **J et K**, registre de lumière TENSION écrit, ils n'en avaient aucun, section 3.5.

## 3.5 Les registres de tension — **écrits le 23 août**

D avait deux traitements de lumière et l'épreuve a montré qu'ils se distinguent franchement ; J et K n'en avaient aucun. Les deux en ont désormais un, `PLAN-styles-D-E-F.md` §4.7 et §4.8, appliqué automatiquement par le générateur sur les blocs 4b et 5.

C'est en K que ce traitement compte le plus : la démonstration du §8 bis de l'audit est que **la forme ne fait pas le registre, la lumière le fait**.

---

# 4. Le compte

| Poste | Par style | Trois styles |
|---|---|---|
| 5 références | 10 crédits | **38 dépensés**, 8 de reprises |
| 20 images clés | 40 crédits | 120 |
| **Total images** | | **158** |
| 16 clips sur RunPod | 1 à 2 $ de GPU | 3 à 6 $ |

**Solde réel au 23 août au soir : 694 crédits**, et non 788 comme annoncé plus haut dans la journée. Le relevé des transactions explique l'écart au crédit près :

| Poste | Crédits |
|---|---|
| Solde après l'épreuve des styles | 800 |
| Deux images Nano Banana Pro à 9 h 13, hors chaîne | −4 |
| Essais vidéo à 10 h 17 et 10 h 19 : Veo 3.1 Lite, Kling v3.0, deux Seedance 2.0 Mini, deux Wan 2.7, deux remboursements | −60 |
| Styles J et K, 6 images | −12 |
| Les 15 références D, J, K | −30 |
| Reprises, `Foule_StyleK` deux fois et `D02_StyleJ` deux fois | −8 |
| **Solde au 23 août au soir** | **686** |

Les 64 crédits des deux premières lignes ne viennent pas de la chaîne du pilote. **Il reste de quoi finir**, mais la marge n'est plus celle annoncée : trois pilotes à 120 crédits laissent 574 crédits, contre 506 pour l'épisode complet. **La marge est donc de 68 crédits**, ce qui ne laisse pas de place à un troisième tirage sur beaucoup de plans. Si elle se resserre encore, la réponse n'est pas de rogner sur les points d'arrêt mais de **descendre à deux pilotes** au lieu de trois.

Travail de code et d'écriture avant la première génération : **fait le 23 août, zéro crédit dépensé.** Reste, avant de générer quoi que ce soit, à produire les cinq références par style et à décider comment verrouiller l'identité d'un visage en style J.

---

# 5. L'ordre que je recommande

1. ~~Porter les corrections et les deux dictionnaires.~~ **Fait le 23 août**, vérifié sans régression sur A, B et C.
2. ~~Écrire le registre de tension de J et de K.~~ **Fait le 23 août.**
3. **Les cinq références, dans les trois styles.** 30 crédits. **Point d'arrêt dur** : on les regarde une par une avant d'en dériver quoi que ce soit. C'est la règle qui a coûté 96 images la dernière fois.
4. **Les 20 images clés, dans les trois styles.** 120 crédits. Point d'arrêt.
5. **Un clip d'essai par style**, pour trancher la question du `STYLE_REDUCED` avant de lancer les seize.
6. **Les 48 clips, puis les trois montages.**

L'épreuve de troupe, 12 images et 24 crédits, peut se lancer **en parallèle** de tout ceci, puisqu'elle n'est pas sur le chemin critique du pilote. Elle reste le moyen le moins cher d'éliminer un style avant d'avoir payé 150 crédits.
