# La bible de fabrication — écrire une série, la mettre en images, la mettre en vidéo

Ce dépôt contient tout ce qu'il faut pour créer une série animée générée par IA et la produire : la méthode d'écriture, une bibliothèque de dix-sept styles visuels prêts à l'emploi, l'atelier (méthode d'images, stratégie vidéo, RunPod, scripts), et la première série, *Il était une fois — Les Découvreurs*, en style P. Réorganisé le 29 août 2026 au moment du choix du style ; tout ce qui a été appris sur les six autres styles rendus et sur les moteurs essayés est conservé et rangé.

```
ecriture/          la méthode d'écriture générique : fiche épisode → scénario → plan de production ; import Novelcrafter
styles/            17 styles : STYLE.md, style.json (blocs verrouillés, copiés tels quels), exemples validés
atelier/           GUIDE de préparation, METHODE d'images (42 règles), STRATEGIE vidéo (LTX-2.5), RUNPOD, scripts, moteurs écartés, spec studio
iletaitunefois/    la série : bible, troupe, S01E01 (scénario, plan de production, briques, planches, clés, audit, décisions)
```

## Par où commencer

* **Créer une série** : `ecriture/METHODE-ecriture.md`, puis une bible de série sur le modèle de `iletaitunefois/serie/BIBLE-Les-Decouvreurs.md`.
* **Choisir un style** : `styles/README.md` et `styles/COMPARATIF.md` ; chaque style a ses exemples et son verdict.
* **Préparer un épisode** : `atelier/GUIDE-preparation-episode.md` — la porte d'entrée avant la première image, avec la liste de contrôle.
* **Fabriquer les images** : `atelier/METHODE-generation-images.md` d'abord ; les briques de l'épisode ensuite (modèle : `iletaitunefois/S01E01/prompts/briques_pilote.py`).
* **Fabriquer la vidéo et le son** : `atelier/STRATEGIE-video.md`, puis `atelier/RUNPOD.md` pour le rendu.
* **Continuer *Les Découvreurs*** : `iletaitunefois/README.md`.

## Les trois règles qui coûtent le plus cher quand on les oublie

1. **La référence impose sa mise en page.** Le modèle ne copie pas seulement le personnage, il copie la disposition de l'image qu'on lui réinjecte. Aucune négative ne corrige ça. Et un défaut de planche est multiplié par le nombre de réinjections.
2. **Une référence se regarde avant d'en dériver quoi que ce soit.** C'est un point d'arrêt, pas une recommandation.
3. **Ce qui doit rester identique d'un plan à l'autre est une image réinjectée, pas une description.** Un objet de continuité a sa planche, sa description canonique en sept points, et son nom dans le prompt.

## Où vivent les choses

Le dépôt est la **source et la destination de l'information validée** : tout ce qui est appris s'y écrit au moment où c'est acquis, dans le dossier générique (`ecriture/`, `styles/`, `atelier/`) ou dans celui de la série. Le répertoire de travail (`C:\Users\kyoms\Downloads\EpisodeModernise`) garde le brut, le suivi et les mp4. Les blocs de style, les briques et les gardes ne se reformulent jamais : ils se copient, et un prompt corrigé se réécrit en entier.

Nommage des images : `<Asset>_<Style>.png`, `Style` valant `StyleA` … `StyleP`. Le fichier au nom canonique est toujours la version validée la plus récente.

Secrets : un `.env` à la racine, jamais affiché, jamais commité.
