# Stratégie de mise en vidéo — ce qui est retenu, et pourquoi

Consolidé le 27 août 2026 à partir de la stratégie du 24 août, du pipeline vidéo et voix du 22 août et des essais E1 à E8. Indépendant du style et de la série : tout ce qui est propre à *Il était une fois* est dans `iletaitunefois/`. Les moteurs essayés puis écartés sont dans `moteurs-ecartes/VERDICTS.md`.

---

## 1. Le moteur : LTX-2.5, partout, voix libres

**LTX-2.5** (Lightricks, 22B distillé int8, dépôt Hugging Face *gated* → jeton `HUGGING_FACE` du `.env`) rend **tous** les plans, muets et dialogues, vidéo et audio dans la même passe. Choisi le 23 août contre Wan 2.2 (bouches non tenables, figurants surgis, LoRA d'accélération qui fige), contre InfiniteTalk (abandonné par Guillaume après E1b) et contre MiniMax H3 (très bon sur le dialogue, mais hallucine sur les plans muets). Sur les six plans muets les plus difficiles du pilote, LTX-2.5 a été propre douze fois sur douze.

**Voix libres** : les voix des dialogues sont **générées par LTX-2.5 avec l'image** (décision du 24 août). Deux raisons mesurées : l'intonation suit l'action, et la voix est **dans l'acoustique de la scène** — extérieur, foule, distance — là où une piste enregistrée en studio sonne « studio avec de l'écho » et devrait être retraitée au montage. Les six montages du pilote disent leurs quatre répliques mot pour mot.

Ce que ça implique pour la chaîne : il n'existe **aucune prise audio séparée** sur un plan de dialogue. Ce qui s'audite, c'est le clip, par transcription (§7).

---

## 2. Les trois modes de voix, tous validés techniquement

| Mode | Ce qui se passe | Quand l'utiliser | État |
|---|---|---|---|
| **Libre** | la voix naît dans le clip, timbre choisi par le prompt (`grave voice`, `clear worried voice`) | par défaut | **retenu** |
| **Gelé** (IA2V) | une piste audio fournie est encodée puis gelée ; les lèvres suivent, la piste sort inchangée | quand une voix doit être verrouillée à l'identique | validé sur E8 (P02 A/B, P03 A) |
| **Référencée** (`LTXVReferenceAudio` + ID-LoRA talkvid) | la voix est générée au timbre d'une référence de ~5 s | un monologue, une voix à tenir sur un épisode | tourne sur 2.5, une voix par rendu, peut dériver de langue |

Le mode gelé se monte ainsi : `LTXVAudioVAEEncode → SetLatentNoiseMask (SolidMask à 0) → LTXVConcatAVLatent` dans les deux passes, sampler `euler` (pas ancestral), CFG vidéo 1 / audio 1. `LTXVSetAudioRefTokens` n'est pas dans le cœur de ComfyUI et n'est pas nécessaire. Graphe exécutable : `scripts/run_ltx_voix_runpod.py` ; bootstrap avec l'ID-LoRA : `runpod/bootstrap_pod_ltx25_idlora.sh`.

**Point ouvert pour un épisode entier** : la tenue d'une même voix sur 21 minutes. Les voix libres tiennent sur 60 secondes ; sur la longueur, trois leviers restent à mesurer — le timbre nommé dans chaque prompt, le mode référencé, ou la sélection de graines. Les enregistrements ElevenLabs des personnages restent la **référence de timbre**.

---

## 3. Le graphe LTX-2.5

`scripts/run_ltx25_runpod.py`, réécriture au format API du template officiel `video_ltx2_5_i2v.json`. Deux passes :

* **passe 1**, demi-résolution, 9 sigmas manuels `1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0` ;
* **upsampler latent ×2** (`ltx-2.5-latent-spatial-upscaler-x2`, dossier `latent_upscale_models/`, pas `upscalers/`) ;
* **passe 2**, 4 sigmas `0.85, 0.7250, 0.4219, 0.0`.

`LTXVDualCFGGuider` cfg vidéo 1 / audio 1, `euler_ancestral` (muets et voix libres), VAE vidéo et VAE audio du modèle, `CreateVideo` 24 i/s. Clés d'image en **1280 × 704** (multiples de 32), longueur en **8n + 1** images. Cinq fichiers, 37 Go : transformer int8 (21,5 Go), encodeur gemma4-12b int8 (15,4 Go), deux VAE, upsampler.

Ces valeurs sont **le graphe**, au même titre que le bloc de style est le style : deux clips rendus avec deux réglages ne sont pas comparables. Ne pas en changer un sans repasser une comparaison côte à côte.

---

## 4. Les règles de prompt vidéo

Toutes mesurées sur le pilote ; les numéros renvoient à `atelier/METHODE-generation-images.md` quand une règle d'image s'applique aussi au mouvement.

1. **Prompt court**, 25 à 80 mots utiles : le style en une ligne (bloc `clip` du `style.json`, réduit à la facture — le bloc complet décrit des personnages et en fait apparaître), l'action concrète avec vitesse et direction, la caméra explicite (`Camera: static` compte), la consigne de présence, l'ambiance sonore en clair.
2. **Une seule action continue par clip**, `Single continuous shot, no cut`. LTX-2.5 insère une coupe vers 5 à 6 secondes sur un plan de dialogue (multishot natif, quatre rendus sur cinq) : pas de « then… then… » séquencés, négative `camera cut, scene change`, ou couper le plan en deux rendus.
3. **La consigne de présence est prescrite par plan** : `none` (rien ni personne n'apparaît), `hands` (seules les mains déjà là bougent), `crowd` (dos, chapeaux, châles, aucun visage ne se tourne), `character`. La ligne générique collée sur tous les clips faisait surgir des personnages dans les plans vides.
4. **La garde des objets est collée sur tous les prompts** : `Every object visible is already present in the first frame: no new object appears, nothing is taken out, put on, handed over or produced, and no object is duplicated` (RÈGLE 40). Un prompt de mouvement décrit un déplacement, jamais une possession.
5. **Négative anti-anachronisme systématique** : `car, cars, vehicle, carriage, modern object, anachronism, extra people, new characters, camera cut, scene change`.
6. **Un prompt de dialogue CITE les répliques exactes entre guillemets**, avec la langue et le timbre : `says in French, grave voice: "Il va se tuer, je vous dis."`, et nomme qui écoute bouche fermée. Décrire la scène sans citer le texte fait inventer un charabia — payé une heure de pod sur dix clips.
7. **L'image clé est un état de repos** (RÈGLE 31), bouches fermées ; l'action est dans le prompt vidéo. Et **l'action de la clé porte la réplique** : relire la réplique et demander « que fait-il en le disant ? » avant de figer la clé.
8. **Quand deux actions donnent la même image, on change l'action** (corollaire RÈGLE 40) — une main sur un chapeau se lit aussi bien « tenir » que « poser ».
9. **Un prompt corrigé se réécrit en entier** (RÈGLE 13) : deux consignes contradictoires dans le même prompt, et c'est l'ancienne qui gagne.

Le gabarit exécutable est `scripts/assembler_clips.py` ; les gardes y sont collées par le code, pas par la vigilance (RÈGLE 41).

---

## 5. Musique et effets — décidés, pas encore produits

**Eleven Music, offre en libre service** (décision du 22 août). Motif juridique avant artistique : c'est le seul générateur dont les données d'entraînement ont été licenciées dès le départ (accords Merlin et Kobalt). Une seule plateforme, un seul pool de crédits pour la voix de référence, la musique et les effets. `force_instrumental` partout.

**Périmètre de diffusion : YouTube et web uniquement.** Les offres en libre service excluent le cinéma, la télévision et la radio ; si un diffuseur se manifeste, passer à Eleven Music Enterprise et **régénérer toute la musique**. Dette connue et bornée. Corollaire à tenir dès maintenant : conserver le prompt et la référence audio de chaque morceau dans l'index, comme les graines de clips.

**Le thème se génère une fois** puis sert de référence audio à toutes les variations (Audio Reference, Music Finetunes) : une source, des dérivés, jamais deux définitions concurrentes. Prévoir un thème, quelques pièces courtes pour les plages sans parole, deux ou trois lits d'ambiance réutilisables — pas un morceau par plan.

**Eleven SFX v2** pour les effets : 0,5 à 30 s en 48 kHz, bouclage sans couture, quatre variantes par requête, licence commerciale complète sans exclusion télé. Trois familles : **ambiances bouclées** (une de 8 s couvre 44 s de plan), **sons signature** réutilisés (le gel d'Elio, la sacoche), **effets ponctuels**. Une cinquantaine de générations pour un épisode entier. Ce n'est pas un bruiteur : ne pas l'appliquer aux clips en masse. Les quatre variantes se départagent à l'oreille — c'est une tâche d'audition humaine, à prévoir au planning.

Les voix générées dans les clips emportent leur ambiance ; au montage, l'ambiance LTX se garde ou se remplace par la piste SFX.

---

## 6. Montage

1. Assemblage dans l'ordre du tableau de plans, bloc par bloc ; les clips d'un bloc bout à bout sans transition, les coupes sont nettes par construction.
2. Plans FIXE : l'image clé et son mouvement de caméra de montage, sur la durée exacte de la colonne Durée.
3. Plans POST : traitement appliqué à la source indiquée.
4. Voix générées dans les clips ; musique et ambiances en dernier.
5. Le master reste en PNG ou ProRes ; le H.264 est un format de livraison.

Le **montage de contrôle** — les clips concaténés à 24 i/s — est l'instrument de jugement d'une séquence : la moitié des défauts du pilote ne se voyaient que là. Il se fabrique avec ffmpeg (concat après réencodage homogène 1280×704, 24 i/s, AAC 48 kHz) et se vérifie avant tout envoi.

---

## 7. La vérification, non optionnelle

Chaque montage passe par `scripts/analyse_montage.py <montage.mp4> <dossier>` : une image par seconde, la piste audio, la transcription ElevenLabs horodatée (`scribe_v1`) et la ligne de temps images ↔ mots. Puis :

* relecture de la planche-contact **plan par plan, à pleine résolution sur deux images par plan** — le survol de la planche laisse passer une nacelle accrochée avant d'être apportée ;
* relecture indépendante par un agent, **avec le scénario exact** — une consigne inexacte fabrique de faux défauts ; tout verdict d'agent se recontrôle sur la planche avant d'être rapporté ;
* comparaison de la transcription au texte attendu, avec la réserve connue : **la transcription se trompe sur les nombres et les noms propres** (« Dix francs » → « Dis Franck ») ; ils se jugent à l'oreille ;
* contrôle de continuité de chaque élément de référence d'un bout à l'autre, et de la chaîne physique de la scène (`GUIDE-preparation-episode.md` §1).

---

## 8. Une session de rendu, du début à la fin

1. `python scripts/runpod_s3.py ls models/` — vérifier sans GPU que les modèles sont sur le volume (37 Go, EU-RO-1).
2. `GPUS=… DISK_GB=60 python scripts/runpod.py create <nom> <clé.pub>` — pod SECURE, volume monté sur `/workspace`. Si EU-RO-1 n'a pas de capacité, **attendre** (boucle de réessai) plutôt que déménager : un autre datacenter coûte 45 minutes de retéléchargement.
3. `scp` du bootstrap, `bash boot.sh` : ComfyUI prêt en ~2 minutes, rien de lourd à télécharger.
4. Clés en 1280 × 704 + `jobs.json` ; `python scripts/run_ltx25_runpod.py submit <url> <index.csv> <jobs.json>` — la ligne d'index s'écrit **au lancement**.
5. Rapatriement par `runpod_s3.py dl`, puis **`rmdir out/`** : les sorties ne restent pas sur le volume.
6. **`runpod.py terminate`**, puis `list` vide vérifié. Coût au journal.
7. Montage, `analyse_montage.py`, vérification §7, reprises ciblées (graine +1, prompt réécrit en entier).

Mesures de référence : ~30 s par clip sur RTX PRO 6000 Blackwell, ~1 min sur A100 80 Go ; 18 clips ≈ 1,6 $ de GPU quand les modèles sont résidents (≈ 4 $ quand il fallait les retélécharger).

---

## 9. Ce que les autres moteurs ont donné

| Moteur | Verdict | Coût P02 8 s |
|---|---|---|
| **LTX-2.5** | **retenu** — propre, rapide, audio natif | ~0,05 $ |
| MiniMax H3 (skill officiel, français) | très bon dialogue, plus « joué » ; hallucine sur les plans muets | ~0,25 $ |
| InfiniteTalk (Wan 2.1) | fait taire l'auditeur, mais rendu jugé insuffisant ; abandonné | ~0,5 $ |
| Wan 2.2 I2V | bouches non tenables (issue ouverte n° 77), figurants surgis, LoRA qui fige | ~0,03 $ |
| Wan 2.2 S2V | anime le visage le plus visible, pas le locuteur | — |
| Veo 3.1 Lite, Wan 2.7, Seedance 2.0 Mini, Kling 3.0 (API) | bons, voix générées propres, texte exact pour Wan 2.7 et Seedance ; aucune voix à nous | 12 à 20 crédits |

Détail, scripts et graphes : `moteurs-ecartes/`. Ils restent réutilisables si LTX déçoit sur un cas précis — H3 en premier pour un dialogue qu'on veut plus vivant.
