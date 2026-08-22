# Méthode de génération d'images — consignes opérationnelles

**Version 4, 8 août 2026.** Écrite après quatre campagnes et trois audits visuels complets, sur 235 puis 123 puis 138 images. Ce document remplace les recommandations de `lecons-generation-images-higgsfield.md` sur tout ce qui concerne la structure des prompts.

À lire avant de lancer la moindre génération. Les règles marquées **RÈGLE** ont été validées par un test A/B ou par une corrélation mesurée, pas déduites.

**Nouveautés de la v4** : les règles 10 à 17, nées de la passe corrective du 8 août au soir. La plus importante est la **RÈGLE 14**, qui explique pourquoi la moitié des poses de cette passe sont fautives alors que la méthode était bonne.

---

# 1. La leçon principale : la référence impose sa mise en page

C'est la découverte la plus importante du projet, et elle explique à elle seule la majorité des défauts.

Quand on réinjecte une image de référence, **le modèle ne copie pas seulement le personnage, il copie la disposition de l'image**. Réinjecter une planche turnaround à quatre vues pour demander un personnage seul produit, dans l'ordre de gravité décroissante :

* un turnaround complet à quatre vues au lieu de la pose demandée ;
* le personnage demandé plus des silhouettes fantômes délavées ;
* des membres orphelins, chaussures seules, têtes flottantes, qui sont les vues résiduelles à moitié effacées ;
* dans un cas extrême, un fond entièrement barbouillé et le personnage principal amputé de ses jambes.

**Aucune négative ne corrige ça.** Nous avons essayé `multiple views, turnaround, model sheet layout, repeated figure, ghost figures, duplicate limbs, extra heads` : le taux d'échec est resté identique d'un tour à l'autre, neuf poses sur vingt quatre. La consigne visuelle bat la consigne écrite.

## RÈGLE 1 — une référence à vue unique pour tout sujet unique

Avant de produire des poses, des portraits ou des têtes, générer d'abord une **référence à vue unique** : le personnage seul, de face, debout, centré, sur fond uni. Elle se génère à partir du turnaround, avec cette formule d'ouverture :

```
same character as reference, same art style as reference, but redraw him as ONE SINGLE STANDING FIGURE seen from the front, nothing else in the image:
```

et cette négative :

```
four drawings, multiple views, side view, back view, three quarter view, turnaround, repeated figure, second figure, ghost figures, duplicate limbs, extra heads, disembodied shoes, row of characters
```

C'est **cette** image, et pas le turnaround, qu'on réinjecte ensuite pour toutes les poses et toutes les têtes. Coût : 2 crédits par personnage et par style, soit 24 crédits pour la troupe entière.

Le turnaround reste la référence de vérité pour le **design** du personnage. La référence à vue unique est la référence de travail pour la **production**.

**Mais cette règle ne vaut que si la référence est contrôlée avant usage. Voir RÈGLE 14, qui est la moitié manquante de celle ci.**

---

# 2. Ne jamais demander une grille au modèle

Le modèle ne sait pas compter. Sur douze planches d'expressions demandées en « exactement six têtes en deux rangées de trois », six sont sorties avec sept ou huit têtes. Après durcissement du prompt avec `exactly six, no more and no less` plus les négatives `seven heads, eight heads, four columns, empty slot`, **le taux d'échec est resté rigoureusement le même**.

## RÈGLE 2 — une image par case, assemblage en local

Générer chaque tête, chaque vignette, chaque case **dans sa propre image**, puis assembler la planche soi même par programme.

**Validé en production** : 72 têtes générées séparément, 12 planches assemblées, **douze sur douze ont exactement six têtes, une par case, aucune case vide, aucune tête en trop, ordre des expressions respecté partout**. Zéro échec structurel, contre 50 % au tirage précédent. La règle est acquise.

Formule de cadrage pour une tête isolée :

```
ONE SINGLE head and neck drawing of ONE character, centered, filling the frame, with <expression décrite en termes de traits: forme des yeux, forme de la bouche, angle des sourcils>
```

négative :

```
multiple heads, two heads, grid, row of heads, repeated figure, ghost figures, full body, arms, hands, legs, feet
```

Décrire l'expression **par ses traits graphiques**, pas par son nom. `wide eyed surprise` seul est faible ; `big round wide open eyes and a small round open mouth` marche.

Coût : six fois plus de générations, mais un résultat déterministe au lieu d'un tirage au sort. Une planche d'expressions passe de 2 à 12 crédits. Sur douze planches, 144 crédits contre 24, pour un taux de réussite structurelle qui passe de 50 % à 100 %.

Sur les défauts d'assemblage qui subsistent, voir **RÈGLE 17**.

---

# 3. Ce que les négatives savent faire, et ce qu'elles ne savent pas faire

Distinction validée par trois audits, elle évite de perdre du temps.

## Les négatives marchent sur la présence d'un élément

* La négative universelle anti texte a fait passer le lettrage parasite de plus de 40 images à zéro sur les 138 dernières, à une exception près (les gribouillis du carnet de Naya en style B, qui se lisent comme de l'écriture). **C'est le meilleur retour sur investissement de tout le projet.**
* Les lunettes de Sam : zéro occurrence sur des centaines de planches, sur quatre campagnes.
* Le bâton non demandé de Huaibing, les cordes aux poignets de Yuan Huangtou, la bibliothèque peinte derrière l'insert sacoche, le mot « TRAVEL » sur l'écusson : tous supprimés du premier coup.

## Les négatives ne marchent pas sur la structure ni sur le nombre

* Compter des objets : échec total, trois tours de suite.
* Interdire une mise en page : échec total quand la référence porte cette mise en page.
* **Contre exemple aggravant** : sur le charretier style B, la consigne `exactly two arms and two hands` plus la négative `third arm, extra arm` n'a pas produit deux bras, elle a produit **zéro bras** et trois pâtés noirs flottants. Une contrainte de compte ne se contente pas d'échouer, elle peut faire basculer l'image dans un état pire que le défaut d'origine.

**RÈGLE 3** : si un défaut porte sur une structure, un nombre ou une mise en page, changer la méthode de production. Si un défaut porte sur la présence d'un élément, une négative suffit.

---

# 4. Prescrire en positif plutôt qu'interdire

Elio sortait avec une tête de méchant sur sept planches sur huit malgré la négative `angry scowl, villain expression, mean face`. En remplaçant l'interdiction par une prescription positive :

```
open curious face, relaxed eyebrows, warm friendly half smile, playful and cheeky but never hostile
```

le défaut a disparu sur les huit planches du tour suivant.

**RÈGLE 4** : pour une expression, une posture ou une attitude, décrire ce qu'on veut. La négative seule laisse le modèle libre de tout le reste de l'espace, y compris de ce qu'on voulait éviter.

Corollaire constaté : la prescription doit exister **sur chaque personnage concerné**, pas seulement sur celui qui a posé problème.

Second corollaire, découvert sur les planches d'expressions : **une expression négative demandée explicitement rouvre la porte**. Le « sceptique » d'Elio ressort en sourcils tombants et bouche tombante, c'est à dire en méchant, dans deux styles sur trois, parce que le sceptique se décrit spontanément par des traits qui descendent. Formulation qui marche : **un seul sourcil HAUT et arqué, l'autre neutre, petite moue de côté**, sans jamais abaisser les deux sourcils ensemble.

---

# 5. Une consigne de style qui fuit devient une légende

Cas observé plusieurs fois : on lit littéralement `CEL SHADING - TWO TONES`, `MUTED EARTH TONES ONLY` imprimés sur des planches qui, ironie, ne respectent pas ces consignes.

**RÈGLE 5** : bannir des prompts les mots qui décrivent un document de production. `model sheet`, `character sheet`, `reference sheet`, `turnaround` sont lus comme « planche annotée » et déclenchent le lettrage. Décrire la disposition visuellement :

* pas `full body turnaround: front view, three quarter view, side profile, back view`
* mais `four drawings of the same character standing side by side in one row, seen from the front, from three quarters, from the side, and from the back`

Négative universelle, à coller sur **toute** image sans exception :

```
text, title, caption, lettering, words, letters, labels, annotations, role labels, view labels, color swatches, palette chips, size chart, watermark, signature, border, frame, margin
```

Compléter par `date, year, numbers, digits, cartouche, inscription` sur les décors, voir RÈGLE 11.

Exception unique rencontrée : la gravure La Loubère, où le bandeau de titre est voulu. Dans ce cas, retirer les termes de texte de la négative pour cette image seule, et le noter.

---

# 6. La palette s'applique à la lumière, pas aux costumes

Erreur commise et qui a coûté un tour. En durcissant la charte du style C, la palette ambre ocre orange brûlé a été écrite comme si elle s'appliquait à toute l'image. Elio est ressorti entièrement orange et marron, veste comprise, sa casquette orange ne se distinguait plus de rien.

**RÈGLE 6** : formuler explicitement la portée de la palette.

```
the warm amber palette applies ONLY to the lighting and the shadow tones, each garment keeps its OWN local color
```

et nommer les couleurs locales en majuscules dans le bloc identité quand elles sont menacées : `VERY DARK CHARCOAL track jacket`, `PALE CYAN BLUE glowing screen`, `still clearly BROWN LEATHER under the frost`.

---

# 7. Corriger dans la description, pas dans la négative

Quand un objet sort au repos alors qu'il devait être en action, la négative ne sert à rien. Il faut réécrire la description positive.

* Le ballon de D01 sortait dégonflé au sol. `a large gas balloon FULLY INFLATED, taut and round, floating and swaying above the ground at the end of its ropes` a réglé le problème du premier coup.
* Le singe de D05v2 était absent. `a monkey sitting on the tree stump, cracking a nut with a stone held in its hands, the monkey clearly the main subject of the shot` a réglé le problème.
* Les étriers de D12 : après deux échecs en style B, la formule qui a marché nomme aussi les pièces voisines et exige les chevaux vivants : `two living saddled horses, the saddles have NO stirrups at all, nothing hangs below the saddle flaps, the stirrup leathers are also absent`. **Corrigé du premier coup, chevaux présents et étriers absents.**

**RÈGLE 7** : un même prompt fautif produit le même échec dans tous les styles. Si un défaut apparaît dans deux styles sur trois, c'est le texte du décor qu'il faut corriger, pas relancer l'image.

---

# 8. Négatives trop larges, et positifs trop larges

La base négative des décors bannissait `characters, people, figures`. Le mot `figures` faisait disparaître les chevaux avec les humains sur D10, D11, D12 et D22.

**RÈGLE 8** : nommer ce qu'on refuse, pas une catégorie qui déborde. `people, human figures, riders, drivers` au lieu de `characters, people, figures`.

**Complément v4 : le piège existe aussi dans le POSITIF.** L'ouvreur de décor `empty plate with no characters` effaçait les animaux exigés par la scène. Écrire `a plate with no people and no riders, the only living creatures in the shot are two horses`. Vérifier l'ouvreur, pas seulement la liste `Avoid:`.

Vérifier enfin qu'une description ne contredit pas sa propre négative : D33 demandait des « silhouettes lointaines optionnelles » alors que la négative interdisait tout personnage. Le modèle arbitre alors au hasard, et le résultat n'est pas reproductible.

---

# 9. Le sujet unique doit être borné dans les deux sens

Pour une planche de têtes, il faut interdire le corps entier : sans `full body, legs, feet` en négative, le modèle dessine des corps.

Pour une pose destinée au détourage, il faut interdire le décor : sans `background scenery, decor, ground, cast shadow on the background`, le modèle plante un décor derrière le personnage.

Pour un insert en gros plan, il faut borner le cadrage : écrire `ONLY a hand and a forearm in frame, nothing else`.

Corollaire de cadrage constaté sur les poses : **ne jamais laisser une main coupée en deux par le bord du cadre**. Sur Sam Bis style B portrait, les moufles sont tranchées net au bord bas, le pouce n'est pas vérifiable et le raccord est impossible. Écrire `hands either fully inside the frame or entirely out of frame, never cut mid hand`.

---

# 10. Un axe de composition contraire au ratio produit un découpage

**La découverte la plus rentable de la passe corrective.** Le décor D25 est resté cassé dans les trois styles et sur deux tours : pillarbox vertical en A, triptyque à coutures en B, planche de montage avec vignette dupliquée et traits de coupe en C. D15 en style C sortait coupé par deux bandes noires. Aucune négative anti découpage n'y a rien changé.

La cause n'était pas dans le modèle, elle était dans la fiche : **les deux descriptions contenaient `vertical composition from ... down to ...` dans un cadre 16:9**. Une consigne de composition contraire au ratio du cadre est lue comme une demande de panneau vertical, et le modèle la satisfait en découpant l'image.

## RÈGLE 10 — ne jamais décrire un axe contraire au ratio du cadre

Placer les éléments par leur **position dans le cadre**, bord haut et bord bas, et écrire explicitement que toute la hauteur tient dans une seule image horizontale. Formule d'ouverture qui a marché :

```
one single continuous wide cinematic shot filling the entire frame edge to edge, one unified scene, no divisions
```

et la négative :

```
split screen, triptych, diptych, panel divisions, vertical bands, black bars, pillarbox, letterbox, collage, storyboard grid, cut marks, duplicated vignette
```

**Résultat : les quatre plans qui résistaient depuis deux tours sont sortis corrects du premier coup.** C'est la seule fois où une négative de mise en page a fonctionné, et seulement parce que la cause positive avait été retirée en même temps.

---

# 11. Un nom propre avec une date invite un cartouche

Le décor D19 portait un cartouche « TAICHENG 549 » en lettres latines, dans deux styles, malgré la négative anti texte. La date figurait dans la description du lieu.

**RÈGLE 11** : bannir dates, années et toponymes des prompts de décor. Décrire le lieu génériquement, et ajouter `date, year, numbers, digits, cartouche, inscription` à la négative anti texte. Corrigé du premier coup.

---

# 12. L'exposition se prescrit en positif, et jamais au prix du cadrage

Vingt et une plaques de style B sur 46 avaient moins de 10 % de pixels au dessus de 120/255 : aucune zone de valeur moyenne où poser un personnage.

**RÈGLE 12** : prescrire la valeur au positif plutôt qu'interdire l'obscurité au négatif.

```
keep a readable midtone value on the foreground and on the ground plane so a character can be composited on top, the scene is dimly lit but never crushed
```

négative d'appoint : `underexposed, crushed blacks, no midtones, pitch black`. C'est une application directe de la RÈGLE 7 à un défaut de lumière.

**Piège associé, constaté sur D14v4** : l'exposition a bien été corrigée, mais le modèle a résolu le problème en resserrant sur un gros plan de gouvernail, sans sol ni quai. La plaque est correctement exposée et inutilisable. **Toujours accoler à la consigne d'exposition une consigne de plan large et de surface praticable** : `wide shot, keep an open usable ground or deck surface across the lower foreground`.

---

# 13. Une correction doit nommer ce qu'elle conserve

Trois régressions de cette passe viennent toutes du même geste : un correctif rédigé pour réparer un défaut, appliqué à la lettre, qui a emporté au passage l'élément utile du plan.

* `INS-sacoche` style C : le correctif demandait un plan produit centré. Le plan produit est parfait. **La main qui glissait un objet dans la sacoche, qui était le sujet de l'insert, a disparu.**
* `KITE-hibou` style B : le correctif demandait un prop isolé sur fond neutre. Le fond est parfait. **La pointe basse du cerf volant est tranchée par le bord du cadre.**
* `D02` style A : le correctif demandait de faire lire l'altitude. L'altitude se lit. **Toute l'image est passée en dominante sable, la couleur réservée de Sam, et le rendu est devenu un croquis au trait fin sans contour épais.**

**RÈGLE 13** : un prompt correctif n'est pas un prompt de remplacement. Réécrire le prompt complet, avec le correctif inséré dedans, et rappeler dans la même phrase l'élément fonctionnel du plan, le socle de style et les couleurs interdites. Terminer tout correctif de cadrage par `nothing cropped, nothing touching the frame edge, even margins on all four sides`.

---

# 14. La référence à vue unique doit être auditée AVANT d'en dériver quoi que ce soit

**La règle la plus coûteuse à avoir été apprise deux fois.** La v3 de ce document disait déjà, au protocole, « la regarder aussi ». Cela n'a pas été fait : les 12 références, les 24 poses et les 72 têtes ont été lancées dans la même session, sans rapatriement intermédiaire. L'audit a montré une **corrélation de un pour un** entre le défaut d'une référence et le défaut de ses deux poses dérivées.

| Référence | Défaut de la référence | Défaut hérité par ses poses |
|---|---|---|
| `REF_Naya_StyleA` | quatre paires de jambes orphelines | trois paires de jambes fantômes sur les deux poses |
| `REF_Sam_StyleC` | deux têtes fantômes en haut du cadre | deux à trois têtes fantômes sur les deux poses |
| `REF_SamBis_StyleB` | deux sacoches, harnais croisé | deux sacoches et harnais croisé en plein pied |
| `REF_SamBis_StyleC` | palette bleu froid et violet | palette bleu froid sur les deux poses |
| `REF_Elio_StyleC` | rendu style A sur fond beige | rendu style A sur les deux poses |
| `REF_Naya_StyleB` | mains en boules noires pleines, deux carnets | mains en boules et deux carnets en plein pied |

**RÈGLE 14** : entre l'étape référence et l'étape dérivés, il y a un **rapatriement et un contrôle à l'œil obligatoires**. C'est un point d'arrêt, pas une recommandation. Le coût du contrôle est de quelques minutes ; le coût de son omission a été ici de 96 images générées sur des références fautives, soit 192 crédits, dont la moitié est à refaire.

Corollaire opérationnel : **ne jamais lancer référence et dérivés dans la même session d'agent.** Un agent qui a les deux phases dans sa consigne enchaînera, parce qu'il ne peut pas voir les images depuis le conteneur.

---

# 15. Le style C ne s'obtient pas en nommant la palette

Constat qui tranche une question ouverte depuis trois campagnes. Dans cette passe :

* **aucune des six références censées être en style C ne l'est réellement.** Elles sortent en style A recoloré, contours noirs épais et aplats teal et marine ou beige.
* **les planches d'expressions en style C le tiennent réellement**, peau ambre et orange brûlé, ombres sarcelle profond, bords durs.

Les deux séries ont été lancées le même soir, avec la même charte nommée. La différence est dans la formulation : les prompts de têtes décrivaient **concrètement les deux tons, zone par zone**, alors que les prompts de références se contentaient de nommer la palette.

**RÈGLE 15** : décrire le rendu du style C par ses opérations graphiques, pas par le nom de sa palette.

```
1990s cel animation, exactly two flat tones per zone with hard edged shadow shapes, the lit tone and the shadow tone separated by a crisp ink boundary, amber ochre and burnt orange for the lit areas, deep teal for every shadow, no gradient, no airbrush, no painterly rendering, no cool blue, no purple
```

## Mais cela ne suffit pas sur un personnage en pied. Troisième échec.

**Test fait, résultat négatif, à ne pas refaire à l'identique.** Les quatre références de style C ont été relancées avec ce bloc écrit mot pour mot, sans réinjection de référence, plus la clause de portée de palette et les négatives anti dérive. Elles sont **toutes les quatre ressorties en style A recoloré** : contour noir épais uniforme, aplats pleins, aucune forme d'ombre à bord dur sur le visage, le cou ou les plis, aucune ombre sarcelle. Mises côte à côte avec les versions de style A, la seule différence est la couleur du fond.

Trois campagnes, trois formulations, trois échecs. Le diagnostic n'est donc plus « la charte est mal écrite » :

* sur un **personnage détouré en pied sur fond plat**, il n'y a presque pas de grandes surfaces à ombrer, et le modèle retombe systématiquement sur son mode « cartoon vectoriel à contour épais », qui est exactement le style A ;
* sur une **tête en gros plan**, il y a du volume à rendre, et le style C sort correctement du premier coup. Les douze planches d'expressions le prouvent.

**Ce qui reste à essayer, dans cet ordre, et pas avant d'avoir tranché la question de fond ci dessous :**

1. **Retirer le contour noir épais du prompt C.** C'est lui qui appelle le mode style A. Écrire `thin dark ink line, or no outline at all on the shadow boundaries`.
2. **Nommer l'ombre comme une forme, pas comme un ton** : `a hard edged shadow shape cutting across the face under the hat brim, another down the left side of the torso, another under each garment fold, each shadow shape is a flat desaturated deep teal version of the local color, with a straight crisp boundary and no blending`.
3. **Ajouter la référence culturelle** plutôt que la description technique : `hand painted animation cel from a 1990s theatrical feature, gouache on acetate`.
4. Si les trois échouent, **accepter que le style C ne se distingue du style A que sur les plans rapprochés** et le décider explicitement, plutôt que de payer un quatrième tour.

Question de fond à trancher avant de relancer : **le style C se justifie t il encore ?** Il coûte un tiers du budget d'images et, sur les plans de personnage en pied, il est visuellement indiscernable du style A depuis trois campagnes.

---

# 16. En style B, la main se prescrit main par main

Sur les planches d'époque en style B, la consigne moufle à pouce donnée une fois par personnage n'a corrigé qu'une main sur quatre chez les fermiers, une sur quatre chez les alchimistes propres. Les mains **qui tiennent un objet** sont celles qui ratent le plus.

Même famille, même échec : les sourcils. `no eyebrows` en description n'a rien donné sur Garnerin, ni sur trois autres planches B, où deux traits obliques nets subsistent.

**RÈGLE 16** : en style B, prescrire par élément et pas par personnage.

```
each hand is a rounded black mitten with a clear notch separating ONE small thumb, the thumb must be visible in silhouette on BOTH hands of EACH person, including the hands that are holding an object
```

```
the face contains ONLY two solid black dot eyes and one small simple closed mouth line, absolutely nothing else: no eyebrows, no line above the eyes, no nose, no cheek line, no wrinkle, no open mouth, no tongue
```

négatives : `mitten without thumb, solid black ball hand, teardrop hand, floating hand, hand without arm` et `eyebrows, brows, eyelids`.

## Le pouce, lui, n'est toujours pas obtenu. Troisième échec.

**Test fait, résultat négatif.** Les trois références de style B ont été relancées avec cette formule, plus la clause de lisibilité `the thumb notch is large and clearly readable even at small size`. Résultat : la structure est parfaite, un seul personnage, une seule sacoche, un seul carnet vierge, mains bien attachées aux bras, **et sur les six mains des trois images, aucun pouce n'est lisible**. Ce sont des moufles noires arrondies pleines.

C'est un défaut de **forme fine dans une silhouette pleine**, à un endroit qui occupe une trentaine de pixels dans une image de 2752 de large. Le modèle ne dispose pas de la résolution d'attention pour l'y placer.

Deux voies réalistes, la seconde étant probablement la bonne :

1. **Générer les mains à part**, en gros plan, comme on a fait pour les têtes, et les composer. Lourd et probablement disproportionné.
2. **Retirer le pouce de la charte du style B.** L'inkman est un pictogramme ; une moufle noire arrondie sans pouce est parfaitement lisible et parfaitement cohérente. Le pouce est une exigence que la chaîne de production ne sait pas tenir, et il a coûté trois tours.

Recommandation : trancher pour la voie 2 et corriger la fiche, ou assumer la voie 1 sur les seuls plans où une main est au premier plan.

Question ouverte à trancher une fois pour toutes : **les planches d'expressions en style B ajoutent des sourcils et des paupières sur les cases 3 à 6**, et les yeux points deviennent des yeux cerclés à pupille sur la case surprise. Soit la charte inkman est officiellement assouplie pour les sourcils d'expression, soit les six expressions doivent passer uniquement par la taille et la position des points et par la forme de la bouche. Tant que ce n'est pas tranché, le style B produira des incohérences à chaque tour.

---

# 17. L'assemblage local se fait sur alpha, pas au collage de rectangles

Les 12 planches assemblées sont structurellement parfaites, mais sept d'entre elles laissent voir des **rectangles de fond de teinte différente** derrière certaines cases, à bords francs, et plusieurs cases décrochent d'échelle malgré la normalisation.

**RÈGLE 17** : deux passes obligatoires à l'assemblage.

1. **Détourer chaque case sur alpha** avant collage, puis peindre le fond de la planche en une seule passe unie. Recopier le rectangle source, même remis à l'échelle, importe forcément sa teinte de fond propre.
2. **Normaliser l'échelle sur la boîte englobante du sujet**, pas sur la taille de l'image, et écarter les valeurs aberrantes plutôt que de prendre la médiane brute : une case peut être cadrée buste alors que les cinq autres sont cadrées tête, et elle tire alors toute la normalisation.

Vérifier aussi la **continuité du costume** entre les six cases : sur une planche, la case 4 porte un manteau ouvert à large col quand les cinq autres portent une veste zippée. Le col doit être décrit à l'identique dans les six prompts.

---

# 17 bis. Quatre règles nées de la passe 5

## RÈGLE 18 — un accessoire nommé deux fois sort en double

Découverte nette. En corrigeant le côté de la sacoche de Sam Bis, la clause corrective a été ajoutée **en plus** de la description de la sacoche déjà présente dans son bloc identité. Résultat sur les deux images : **deux sacoches**, l'une derrière l'autre en style A, deux sacs superposés de couleurs différentes en style C. Le même mécanisme avait produit le harnais croisé au tour précédent.

Quand on ajoute une clause corrective sur un accessoire, **fusionner** la clause avec la description existante et supprimer l'ancienne. Ne jamais laisser deux phrases décrire le même objet dans un prompt. C'est le corollaire direct de la RÈGLE 13 : le prompt correctif remplace, il ne s'empile pas.

Sur la latéralité elle même, la formule qui donne le repère spectateur fonctionne en style A et échoue en style C : `his LEFT hip, which appears on the RIGHT side of the image from the viewer point of view`. Un tirage sur deux, donc à vérifier systématiquement à l'œil plutôt qu'à supposer acquis.

## RÈGLE 19 — supprimer l'objet porteur de texte, pas son texte

Le mot « TRAVEL » est revenu sur les deux inserts sacoche, en styles B et C, cinq occurrences au total, malgré la négative anti texte au complet et malgré une clause positive demandant des écussons en formes colorées unies.

Cause : le prompt nomme des `patches` et des `stickers`. Un écusson et un autocollant sont, pour le modèle, des objets qui portent une inscription par définition. La négative anti texte ne peut pas gagner contre la nature de l'objet.

**RÈGLE 19** : quand du lettrage revient malgré la négative universelle, retirer du prompt la **classe d'objet** qui porte habituellement du texte, plutôt que d'essayer de la faire taire. Écrire `plain worn leather satchel with no patches, no stickers, no badges, no labels of any kind`.

## RÈGLE 20 — en style B, une main qui touche un objet mange son bras

C'est la famille de défauts la plus résistante du projet, quatre tours d'affilée. Sur le charretier, la formule d'ancrage `each shoulder has a thin continuous black line arm going down from it` a rétabli **un** bras sur deux. Le bras manquant est systématiquement celui dont la main touche un objet ou le corps : la moufle est absorbée par la masse noire de l'objet et le trait de bras disparaît avec elle. Même chose sur Garnerin en vue de profil, sur les mains des alchimistes soudées à la fiole, et sur les deux moufles de Naya fusionnées autour du carnet.

**RÈGLE 20** : en style B, ne jamais composer une pose où les deux mains touchent quelque chose. Garder au moins un bras **libre et écarté du corps**, et écrire l'écart : `the object is held at arm's length, clearly away from the torso, with visible empty space between the arm and the body`. Le trait de bras a besoin d'espace vide autour de lui pour exister.

## RÈGLE 21 — une planche s'assemble d'un seul tirage de cases

Les quatre planches de style B ont été réparées en regénérant seulement les cases 3 à 6. Les cases 1 et 2, conservées, ne raccordent plus : Sam Bis est presque chauve sur les deux anciennes et porte une masse de cheveux noire pleine sur les quatre nouvelles ; Naya passe de boucles au trait lâche à des boucles denses ; la case 2 est plus grande que les cinq autres sur deux planches.

**RÈGLE 21** : quand une planche doit être reprise, **regénérer les six cases dans le même lot**, avec le même prompt de base. Le surcoût de deux images est très inférieur au coût d'une planche qui ne raccorde pas. Corollaire : ne jamais mélanger dans une planche des cases issues de deux tours différents.

## RÈGLE 22 — une variante d'un même plan se rédige en positif, élément par élément

Pour produire une version « suie » d'une planche « propre », la formule `same picture as the reference in every respect, with ONE single change` ne suffit pas seule. Testée deux fois, elle a laissé dériver le bras porteur de gauche à droite, la robe du maître de courte à longue, l'assistant d'une tunique à un kimono croisé, une touffe de cheveux devenue trois, et le fond du beige au gris taupe.

Ce qui marche : **rappeler nommément, dans le prompt de la variante, chaque élément qui avait dérivé au tour précédent**, en positif. La négative `changed hairstyle` ne dit pas au modèle quelle coiffure garder, la description positive si. Écrire la coiffure, le vêtement, la chaussure et le ton de fond **mot pour mot identiques** dans les deux prompts, et les conserver dans un carnet de phrases verrouillées.

Phrases verrouillées du projet, à recopier telles quelles :

```
maître, style B  : one small solid black top knot bun on the crown of his round white head and a long thin grey beard drawn as a few loose ink strokes hanging from his chin, nothing else on his head
assistant, style B : exactly ONE small solid black tuft of hair on the crown of his round white head and a plain narrow cream cloth headband tied across his forehead, nothing else on his head
```

Corollaire acquis : **la réinjection de la version propre est ce qui fait tenir le plan.** En style C, la version suie regénérée depuis la propre est revenue au même plan du premier coup, là où la génération depuis le texte échouait à chaque fois.

## RÈGLE 23 — relire la clause invariante contre chaque clause variable

Une clause de charte recopiée sur les six cases d'une planche peut contredire une seule case sur six, et cette contradiction ne se voit qu'en relisant les deux blocs ensemble. Cas vécu : la clause `each eye is a completely solid black filled disc` collée sur les six cases contredisait la case 6, où les yeux doivent devenir deux arcs. Le modèle arbitre alors au hasard, c'est le mécanisme du chapitre 8.

**Avant tout lot de planche, relire la clause invariante en regard de chacune des six descriptions d'expression**, et retirer de la clause invariante ce qui heurte une case, quitte à faire une version dérogatoire pour cette case seule.

Même piège dans l'autre sens : une base négative de style collée sur un cadrage restreint réintroduit des termes qui exigent l'élément que le cadrage exclut. Sur une tête isolée, la base négative du style B contenait `missing hand, missing arm, hand without arm`, ce qui rappelle les mains dans un cadre où elles sont interdites. **Purger la base des familles d'objets hors champ avant de l'assembler.** Même chose sur une planche à quatre vues, où `multiple views`, `repeated figure` et `model sheet layout` interdisent littéralement ce qu'on demande.

## RÈGLE 24 — normaliser CHAQUE case sur SA propre mesure, sur la largeur de tête

L'assemblage local a produit deux défauts successifs, tous deux réparés, et tous deux instructifs.

**Premier défaut, les rectangles de fond.** Coller le rectangle source dans la case importe forcément sa teinte de fond propre, et la jonction se voit. Correctif validé : détourer chaque case sur un masque alpha, obtenu par différence avec la couleur de fond estimée aux quatre coins, morphologie d'ouverture pour nettoyer, léger flou pour adoucir le bord, puis coller **avec** ce masque sur une planche peinte d'une seule couleur. Le défaut a disparu sur onze planches sur douze.

**Second défaut, l'échelle.** Ne pas normaliser sur la **hauteur de boîte englobante** : elle inclut le buste, dont la ligne de coupe varie d'une génération à l'autre, et la mesure est donc bruitée. Mesurer plutôt la **largeur de la tête**, prise comme la médiane de l'extension horizontale du masque sur la bande située entre 15 et 40 pour cent sous le sommet de la boîte, puis mettre chaque case à l'échelle pour que cette largeur soit constante, et aligner le sommet de la boîte à une hauteur fixe dans la case.

**Le piège qui m'a coûté deux tours** : calculer une mesure de référence médiane sur les six cases puis l'appliquer à toutes. Cela ne normalise rien, cela applique le même facteur partout. Le facteur d'échelle doit être calculé **par case, à partir de la mesure de cette case**. Ajouter un garde fou qui borne le facteur entre 0,75 et 1,35 fois le facteur médian, pour qu'une mesure aberrante ne fasse pas exploser une vignette.

## RÈGLE 25 — une grande surface de peau en gros plan attire un visage

Défaut repéré tardivement, sur deux images livrées : les inserts `INS-sacoche_StyleA` et `INS-sacoche-givre_StyleA` portaient **un visage grimaçant dessiné sur le dos de la main**, yeux, nez et bouche ouverte, formé à partir des plis des phalanges. Personne ne l'avait demandé, et rien dans le prompt n'y invitait.

Le mécanisme est de la paréidolie : sur un gros plan, le dos d'une main est une grande surface claire, lisse, entourée d'un contour fermé, avec deux ou trois lignes de plis au milieu. C'est exactement la structure d'un visage de dessin animé, et le modèle la complète. Le même risque existe sur tout aplat de peau large en gros plan : un dos, un ventre, une épaule, une paume.

**RÈGLE 25** : dès qu'une image cadre une grande surface de peau nue, prescrire son vide en positif et nommer le défaut en négatif.

```
the back of the hand is a smooth plain skin surface with only two or three simple thin knuckle lines drawn on it and absolutely nothing else, no marks, no dark shapes, no features of any kind on the skin
```

```
face on the hand, eyes on the hand, mouth on the hand, teeth on the hand, nose on the hand, facial features on skin, knuckles forming a face, a creature on the hand, second face, extra face, pareidolia
```

Corrigé du premier coup sur les deux images. Corollaire de la RÈGLE 22 : le défaut était présent à l'identique sur la version givrée parce qu'elle dérive de la version propre. **Un défaut de la version d'origine se retrouve mécaniquement dans toutes ses variantes**, donc on répare l'origine puis on regénère la variante par réinjection, jamais l'inverse.

Corollaire d'audit, plus inconfortable : ce visage traînait depuis la première campagne et aucun des passages d'audit ne l'avait vu, parce que la grille de contrôle regardait la sacoche, le lettrage et le fond, mais pas la main. **Ajouter à la grille une ligne générique : rien d'anormal nulle part, y compris hors de la zone du sujet.**

---

# 18. Protocole de production, dans l'ordre

1. **Générer les turnarounds**, quatre vues, référence de design.
2. **Les rapatrier et les REGARDER.**
3. **Générer une référence à vue unique** par personnage et par style, depuis le turnaround validé.
4. **POINT D'ARRÊT. Les rapatrier et les REGARDER.** Voir RÈGLE 14. Ne rien lancer d'autre avant.
5. **Produire les dérivés** en réinjectant la référence à vue unique validée, jamais le turnaround.
6. **Les planches à cases** se produisent case par case, puis s'assemblent en local, sur alpha, avec normalisation d'échelle.
7. **Rapatrier et auditer** avant de passer à la phase suivante.

## Sur le rapatriement et l'audit

Les images restent dans la galerie Higgsfield. Le CDN de sortie et tous les domaines Higgsfield sont bloqués depuis un conteneur d'agent : **aucun script, aucune CLI ne peut les télécharger, et aucune vérification visuelle n'est possible tant qu'elles n'y sont pas**. La seule voie qui marche est le navigateur de l'utilisateur, via un `fetch` puis un `<a download>` sur une URL de blob, ce qui permet au passage de renommer les fichiers. Chrome aplatit les sous dossiers, donc télécharger à plat puis ranger.

Chaîne qui fonctionne, de bout en bout :

1. `jobs_wait` avec `timeout_seconds: 0` par groupes de 12 pour récupérer les `result_url`. Le nom de fichier est de la forme `hf_AAAAMMJJ_HHMMSS_<job_id>.png`, l'horodatage n'est pas déductible du job_id, il faut donc interroger.
2. Installer le téléchargeur dans la page Higgsfield, charger la file en trois blocs, lancer. Compter environ 1,1 seconde par image.
3. Ranger sur le disque par `device_bash`, en déplaçant les anciennes versions vers `_to_delete` avant d'écrire les nouvelles, le pont ne pouvant pas effacer.
4. Générer des vignettes JPEG à 900 pixels, les zipper, les remonter par `device_stage_files`, puis répartir l'audit entre plusieurs agents. Un agent regarde confortablement une trentaine d'images.

**RÈGLE 9** : rapatrier un échantillon TÔT, pas à la fin. Générer 235 images en aveugle puis découvrir un défaut systématique coûte infiniment plus cher que de contrôler douze planches maîtresses avant de lancer les dérivés.

## Sur les identifiants

Noter l'identifiant de job **au moment où on lance**, avec un index stable qui dit quel asset c'est. Une fois la génération passée, retrouver une image dans l'historique est lent et fragile. Trois identifiants consignés dans un document n'existaient pas, découverts seulement au moment de télécharger : les planches correspondantes n'avaient jamais été générées.

---

# 19. Réglages qui marchent

```
model: nano_banana_pro        ← identifiant à SOUMETTRE
aspect_ratio: 16:9            ← 1:1 pour les têtes isolées
resolution: 2k                → sortie 2752 x 1536
use_unlim: false
count: 1
```

**Point de confusion à lever, il a fait trébucher deux agents.** On soumet `nano_banana_pro`. La réponse du serveur affiche `model: nano_banana_2`, qui est le nom du **moteur** : c'est normal et c'est le bon. Le piège est à la soumission : **demander `nano_banana_2` route vers `nano_banana_flash`, un moteur allégé, au même prix.** Vérifier ce qu'on envoie, pas ce qu'on reçoit.

Lots de douze au maximum, c'est un plafond dur. Un lot peut renvoyer « Out of credits » à tort quand la file est chargée, sans rapport avec le solde : resoumettre par lots de quatre.

**Tarification, mesurée sur plus de cent générations : 2 crédits par image, avec ou sans réinjection de référence.** La réinjection ne majore rien. Un devis qui la facture plus cher est faux, et la crainte du surcoût ne doit jamais dissuader de réinjecter une référence validée.

Deux modes d'échec à surveiller : le faux positif `nsfw` sur les portraits rapprochés, levé en retirant les descripteurs morphologiques du visage comme `light stubble` et `strong jaw` ; et le job bloqué en `in_progress`. Sur ce dernier, précision acquise : **un job isolé encore en cours alors que tout son lot est sorti n'est pas une file chargée, c'est un job mort.** Trois minutes suffisent à trancher, et la resoumission part sur une file vide donc aboutit en quelques secondes. Ne jamais attendre plus longtemps.

## Sur le poste de travail

Deux contraintes de l'environnement, apprises à la dure :

* **Un processus lancé en arrière plan sur la machine de l'utilisateur ne survit pas à l'appel qui l'a lancé.** Un `nohup ... &` meurt avec son appel, et les sondages suivants voient un faux positif parce que `pgrep` remonte sa propre ligne de commande. Tout traitement local doit tenir dans la durée d'un appel, donc être découpé, par exemple un personnage par appel plutôt que douze planches d'un coup.
* Le traitement d'image sur le dossier monté est lent. Estimer les masques sur une version **réduite au quart**, puis remettre le masque à l'échelle : le résultat est identique à l'œil et le temps passe de plusieurs minutes à quelques secondes.

---

# 20. Grille de contrôle visuel

À passer sur chaque image avant de la valider comme référence ou de la livrer.

1. Aucun texte nulle part, y compris aucun gribouillis qui se lit comme de l'écriture sur un carnet ou une étiquette.
2. Le bon nombre de sujets : un seul pour une pose, deux pour une paire, quatre vues pour un turnaround, six têtes pour une planche assemblée.
3. Aucun fragment fantôme, membre dupliqué, chaussure orpheline ni tête flottante, y compris faible et en arrière plan. Rehausser le contraste pour vérifier.
4. Aucun accessoire dupliqué : une sacoche, un carnet, une tablette, jamais deux.
5. Style B : moufle noire arrondie à petit pouce sur **chaque** main, deux bras rattachés aux épaules sur chaque vue, visage réduit à deux points et une bouche.
6. Style C : deux tons à bords durs, palette ambre ocre à ombres sarcelle, jamais de violet, de bleu froid, de vert prairie ni de dégradé.
7. Style A : contours noirs épais et aplats, jamais de trait fin ombré ni de croquis.
8. Couleurs réservées jamais dominantes sur un décor, un personnage ou un accessoire d'époque : sable de Sam, sarcelle vif de Naya, orange vif d'Elio.
9. Décors vides de toute présence humaine, sauf exception documentée.
10. Plein cadre 16:9, aucune bande, aucun panneau, aucune bordure, rien qui touche le bord.
11. Sur une plaque destinée au compositing : existe t il une surface au sol en valeur moyenne où poser un personnage.
12. Les quatre personnages d'un même style, mis côte à côte, doivent avoir l'air d'appartenir à la même série.
13. **Balayage libre pour finir** : parcourir l'image entière, hors de la zone du sujet, et se demander simplement s'il y a quoi que ce soit d'anormal. Les douze points ci dessus cherchent des défauts connus ; celui ci cherche les autres. C'est ainsi qu'un visage dessiné sur le dos d'une main a survécu à trois campagnes d'audit.

---

# 21. Règles nées du pilote S01E01 (22 août 2026)

Acquises sur les 54 images clés des plans 1 à 6, trois styles, 73 jobs. Détail et preuves dans `S01E01-pilote-audit.md`.

## RÈGLE 26 — une négative de foule ne se pose jamais sur un plan où un personnage nommé montre son visage

`readable faces, facial features, eyes` agit sur toute l'image. Sur P02 (deux badauds nommés + foule), le style C a obéi à la négative et effacé les visages des deux badauds ; A et B avaient arbitré dans l'autre sens. Retirée, le bloc positif de foule (`NO FACE VISIBLE ON ANY FIGURE`) a suffi : badauds avec visage, foule sans. C'est le cas particulier de la RÈGLE 23 (clause invariante contre clause variable). Corollaire vérifié en pleine résolution : des figurants vus de face **sans aucun trait** ne sont pas des « visages lisibles ».

## RÈGLE 27 — un figurant nommé sans sa référence dérive

1a‑2 était le seul plan de foule sans la fiche Foule réinjectée (« a few crowd figures »). Résultat : robe orange vif et veste sarcelle vif en A, figurants de face à yeux points en B. Avec la fiche Foule en deuxième référence, les deux styles sont rentrés dans le rang du premier coup. Dès qu'un figurant est nommé, même « a few », la fiche Foule se réinjecte.

## RÈGLE 28 — un code de décor ne tient pas sur un très gros plan

Sur 5‑2 et 5‑3 en style A, `Decor: D2, out of focus behind` a donné un mur, une rue, et une fois un **panneau portant « D2 »**. La référence D02 n'a presque pas de surface pour s'imposer quand la corde remplit le cadre, et le code devient du texte. Accoler au code une description en clair, `Decor: D2, the sky and the rooftops of Paris far below, out of focus behind`, a réglé les deux images du premier coup. B et C n'avaient pas eu le problème : le défaut est probabiliste, la correction ne coûte rien, on l'applique partout où le décor est flou derrière un gros plan.

## RÈGLE 29 — la plaque de décor impose ses accessoires

La plaque D01 montre le ballon **avec** sa nacelle ; les briques 1b demandaient qu'on porte la nacelle vers le ballon. Trois styles sur trois ont produit deux nacelles. Aucune négative ne l'aurait corrigé (RÈGLE 1). Nommer l'état voulu dans la brique, `toward the balloon hanging above with no basket under it yet` et `no other balloon or basket in the background`, a suffi sur cinq images sur cinq. Quand une brique contredit un élément de la plaque réinjectée, on écrit l'état voulu de cet élément, on ne le tait pas.

## RÈGLE 30 — sur un plan rapproché de figurants, les couleurs réservées reviennent : on nomme les couleurs en positif

4a‑2 en style A (« three onlookers, close shot on their backs ») a donné deux fois de suite, sur deux graines, les trois figurants en **sable, sarcelle et orange vif** — la palette des trois héros, bien que la brique ne les nomme pas et que les négatives `dominant sand / teal / vivid orange outfit` soient posées. Dès que trois figurants occupent le premier plan, le modèle leur prête les couleurs qu'il a le plus vues dans les références ; une négative n'y fait rien (RÈGLE 1). Écrire les couleurs voulues en clair, `their coats in muted brown, grey and dark green only, no bright color on any garment`, a réglé l'image au tir suivant. Complète la RÈGLE 27 (réinjecter la fiche Foule) : la fiche tient la foule de fond, pas les figurants mis en avant.

## RÈGLE 31 — une image clé de dialogue se génère bouches fermées

Les clés P02/P03 d'origine montraient les bouches ouvertes (on avait demandé « en train de parler »). Tout clip vidéo qui part de cette image hérite des bouches ouvertes : l'auditeur a la bouche ouverte pendant que l'autre parle, et le sous-clip d'attente « personne ne parle » montre deux bouches ouvertes. Vérifié à l'image près par extraction d'une image par seconde (audit lot 7). Depuis le lot 8, la brique d'un plan de dialogue dit `both with their mouths firmly closed in a neutral pause` ; c'est le prompt vidéo, et lui seul, qui ouvre la bouche du locuteur. Corollaire : une image clé décrit un **état de repos**, jamais l'action que le clip devra faire.

## Observations sans règle

* Le **style C tient sa palette sur les plans larges** dès qu'une plaque C est réinjectée : la RÈGLE 15 décrit les planches personnages sur fond neutre, pas les plans de scène.
* Le **style B** est le plus robuste sur la foule : têtes vierges sans exception sur six plans.
* Faux positif `nsfw` possible même sur un paysage vide ; resoumettre à l'identique suffit, et ce n'est pas débité.
* Un job isolé en `in_progress` six minutes après son lot était bien mort ; la resoumission a abouti en quarante secondes. La règle des trois minutes tient.
