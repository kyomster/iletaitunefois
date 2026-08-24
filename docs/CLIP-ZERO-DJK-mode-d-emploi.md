# Clip zéro D, J, K — trancher la question du bloc réduit

**24 août 2026.** Dernier poste non vérifié de toute la chaîne. Six rendus, environ dix minutes de GPU, **zéro crédit**.

---

# 1. La question

Le **style B** a exigé un bloc de style **réduit** pour la vidéo. Avec le bloc complet, qui décrit les personnages, Wan 2.2 se mettait à fabriquer des têtes d'inkman partout dans le plan : **12 clips sur 16 inutilisables**, ramenés à 12 sur 12 corrects avec le bloc réduit.

Des blocs réduits ont été écrits pour D, J et K le 23 août. **Ils n'ont jamais été rendus.** Rien ne dit que ces trois styles souffrent du même défaut, et rien ne dit le contraire.

Lancer les 48 clips sans le savoir, c'est risquer de refaire l'erreur du style B à l'échelle de trois styles.

---

# 2. Le protocole

**Un seul plan, `P1b-2`, dans les trois styles, avec les deux blocs.** Six rendus.

Pourquoi `P1b-2` et pas un autre : c'est **le seul des seize clips dont la présence est `character`**. Deux aides portent une nacelle, en mouvement, dans un plan large. C'est exactement la configuration où le style B avait échoué : le bloc décrit des personnages, et le modèle vidéo en fabrique. Un plan vide comme `P4b-3` ne testerait rien.

**Même graine pour les deux blocs d'un même style**, pour que la seule variable soit le bloc.

Fichier de jobs : `docs/runpod/clip-zero-DJK.json`, six entrées, prêt pour `run_clips_runpod.py`.

| Job | Bloc | Graine |
|---|---|---|
| `P1b-2_StyleD_fiche` | complet | 904697727 |
| `P1b-2_StyleD_reduit` | réduit | 904697727 |
| `P1b-2_StyleJ_fiche` | complet | 1708387364 |
| `P1b-2_StyleJ_reduit` | réduit | 1708387364 |
| `P1b-2_StyleK_fiche` | complet | 1134880663 |
| `P1b-2_StyleK_reduit` | réduit | 1134880663 |

Réglages inchangés : Wan 2.2 I2V A14B fp8, LoRA LightX2V 4 étapes, 1280 × 720, 16 im/s, 49 images, CFG 1, euler simple, shift 5. Voir `RUNPOD-COMFYUI-mode-d-emploi.md` pour le pod.

---

# 3. Ce qu'on regarde, et la décision qui en découle

Trois questions, dans cet ordre :

1. **Le bloc complet fabrique t il des personnages parasites ?** C'est le défaut du style B. Si oui, ce style prend le bloc réduit, comme B.
2. **Le bloc réduit tient il le style sur trois secondes ?** C'est le risque inverse : un bloc trop maigre laisse le modèle ramollir le trait, ajouter du volume et de la lumière rasante dès la deuxième seconde, ce que décrit `PIPELINE-video-et-voix.md` §5.1.
3. **Le style D tient il sans LoRA ?** Hypothèse posée le 23 août : la dérive naturelle de Wan 2.2, vers l'ombrage adouci, la profondeur de champ et le grain, **est la cible du style D**. Si elle se confirme, l'étape 8 de la feuille de route du PIPELINE tombe pour D, ce qui économise l'entraînement du LoRA. C'est un argument de coût et de délai, pas de goût.

**La décision se pose par style, pas globalement.** `STYLES_BLOC_REDUIT_OBLIGATOIRE` dans `build_clips_pilote.py` ne contient aujourd'hui que `StyleB` ; on y ajoute ce que l'essai désigne, et rien d'autre.

---

# 4. Après

Si les six passent, les 48 clips partent en un lot, trois styles, environ 1 h 20 de GPU par style et 3 à 6 $ en tout. Puis les trois montages, puis l'analyse par mesure de `analyse_montage.py`, une image par seconde plus transcription horodatée, et un relecteur indépendant qui reçoit le scénario exact.

C'est à ce moment là seulement que le style se choisit.
