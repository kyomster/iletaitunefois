#!/usr/bin/env python3
"""Seconde vague d'import dans Studio (outils livrés le 30 août 2026) : moteurs et graphes, personnages, continuité
visuelle, assets et prompts tels qu'envoyés, attendus par plan, voix, musique et effets, épreuve comparative.

Même mécanique que studio_import.py (dont il hérite) : étapes ordonnées, --dry-run, journal, rapport.

Usage :
  python studio_import_prod.py --dry-run [--etape=assets | --jusqua=son]
  python studio_import_prod.py --jusqua=epreuve --enchainer
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import studio_import as B  # noqa: E402
import studio_sources as S  # noqa: E402
from bibliotheque import charger_briques, charger_styles  # noqa: E402
from studio_client import RefusStudio  # noqa: E402

SHOW, EP = B.SHOW_SLUG, B.EP_CODE
RACINE, STUDIO_DIR, ref, md_plain = B.RACINE, B.STUDIO_DIR, B.ref, B.md_plain
ETAPES = ["moteurs", "personnages", "continuite", "assets", "attendus_plans", "voix", "son", "epreuve"]
BRIQUES = S.EP / "prompts" / "briques_pilote.py"
CLIPS_JSON = S.EP / "prompts" / "clips-StyleP.json"
MEDIA_IDS = Path(r"C:/Users/kyoms/Downloads/EpisodeModernise/pilote/_media_ids.json")
PLAN_DU_CLIP = {"P1a": 1, "P1b": 1, "P02": 2, "P02a": 2, "P02b": 2, "P03": 3, "P4a": 4, "P4b": 4, "P5": 5}
FAMILLES = {"AC": "_defaut", "B": "inkman", "JK": "realiste", "P": "aplats"}   # variantes d'identité → familles de style


def plan_de(code):
    return PLAN_DU_CLIP[code.split("-")[0]]


class ImportProd(B.Import):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.ids = {}  # slug/clé → identifiant en base

    # ------------------------------------------------------------ moteurs
    def moteurs(self):
        existants = {(e.get("code"), e.get("status")) for e in (self.lire("list_engines", {}).get("moteurs") or self.lire("list_engines", {}).get("engines") or [])} if not self.dry else set()
        codes = {c for c, _ in existants}
        sys.path.insert(0, str(RACINE / "atelier" / "scripts"))
        from run_ltx25_runpod import SIG1, SIG2, api_prompt_ltx25
        gabarit = {"prompt": "<PROMPT>", "negative": "<NEGATIVE>", "seed": 0, "length": 49, "width": 1280, "height": 704, "fps": 24, "style": "<STYLE>", "clip": "<CLIP>"}
        graphe_ltx = api_prompt_ltx25(gabarit, "<IMAGE_1280x704>.png")
        wan_dir = RACINE / "atelier" / "moteurs-ecartes" / "wan22"
        MOTEURS = [
            {"code": "nano-banana-pro", "label": "Nano Banana Pro (Higgsfield)", "medium": "IMAGE", "provider": "higgsfield", "modelRef": "nano_banana_pro",
             "params": {"aspect_ratio": "16:9", "resolution": "2k", "count": 1, "use_unlim": False, "refsMaxParPrompt": 7, "negatives": "en fin de prompt après « Avoid: »", "sortie": "2752x1536"},
             "status": "RETENU", "notes": "Seul moteur d'image : la continuité avec les assets validés en dépend (décision du 22 août 2026).", "sourceRef": ref("atelier/METHODE-generation-images.md", "19")},
            {"code": "ltx-2.5-i2v-2passes", "label": "LTX-2.5 image→vidéo, deux passes, voix libres", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "Lightricks LTX-2.5 22B distilled int8 (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot)",
             "graph": graphe_ltx,
             "params": {"width": 1280, "height": 704, "fps": 24, "longueur": "8n+1 images", "passes": 2, "sigmasPasse1": SIG1, "sigmasPasse2": SIG2, "sampler": "euler_ancestral", "cfgVideo": 1.0, "cfgAudio": 1.0,
                        "upscaler": "ltx-2.5-latent-spatial-upscaler-x2 (latent_upscale_models/)", "encodeur": "gemma4-12b int8", "vae": ["ltx-2.5-video-vae-bf16", "ltx-2.5-audio-vae-bf16"], "i2vStrengthPasse1": 0.7, "imgCompression": 18,
                        "voiceMode": "INTEGREE", "gabaritPrompt": "atelier/scripts/assembler_clips.py", "tempsParClip": "~30 s RTX PRO 6000, ~1 min A100"},
             "status": "RETENU", "notes": "Retenu le 24 août 2026 (E7 : propre 12/12 sur les plans muets ; E8 : les trois modes de voix marchent). Le graphe est celui de run_ltx25_runpod.py, valeurs de prompt/graine/image en gabarit.", "sourceRef": ref("atelier/STRATEGIE-video.md", "3")},
            {"code": "ltx-2.5-ia2v-audio-gele", "label": "LTX-2.5 audio gelé (IA2V) — nos pistes ElevenLabs", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "Lightricks LTX-2.5 22B distilled int8",
             "params": {"principe": "LTXVAudioVAEEncode → SetLatentNoiseMask (0) → LTXVConcatAVLatent dans les deux passes, euler, CFG 1/1", "script": "atelier/scripts/run_ltx_voix_runpod.py"},
             "status": "CANDIDAT", "notes": "Validé sur E8 (P02 A/B, P03 A) : la piste ElevenLabs sort intacte, les lèvres suivent. En repli si une voix doit être verrouillée à l'identique.", "sourceRef": ref("atelier/STRATEGIE-video.md", "2")},
            {"code": "ltx-2.5-idlora-voix-referencee", "label": "LTX-2.5 voix référencée (LTXVReferenceAudio + ID-LoRA talkvid)", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "Lightricks LTX-2.5 + ID-LoRA 2.3 talkvid",
             "params": {"identityGuidance": 2, "reference": "~5 s d'audio, une voix par rendu", "bootstrap": "atelier/runpod/bootstrap_pod_ltx25_idlora.sh"},
             "status": "CANDIDAT", "notes": "Tourne sur 2.5 ; une voix par rendu, peut dériver de langue. Pour un monologue ou une voix à tenir sur un épisode.", "sourceRef": ref("atelier/STRATEGIE-video.md", "2")},
            {"code": "wan22-i2v-a14b", "label": "Wan 2.2 I2V A14B fp8 + LightX2V 4 étapes", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "Comfy-Org/Wan_2.2_ComfyUI_Repackaged i2v high+low noise fp8",
             "graph": json.loads((wan_dir / "wan22_i2v_api.json").read_text(encoding="utf-8")),
             "params": {"width": 1280, "height": 720, "fps": 16, "longueur": "4n+1", "steps": 4, "cfg": 1.0, "sampler": "euler/simple", "shift": 5.0, "lora": "lightx2v 4 steps rank64 high+low"},
             "status": "ECARTE", "notes": "ÉCARTÉ le 23 août 2026 : l'auditeur ouvre la bouche pendant la réplique de l'autre (issue n° 77 du dépôt Wan 2.2), des personnages surgissent dans les plans vides, le LoRA d'accélération fige le mouvement. Ne pas retenter pour un dialogue.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
            {"code": "wan22-flf2v", "label": "Wan 2.2 première+dernière image (WanFirstLastFrameToVideo)", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "mêmes experts I2V que wan22-i2v-a14b",
             "graph": json.loads((wan_dir / "wan22_flf2v_api.json").read_text(encoding="utf-8")),
             "params": {"width": 1280, "height": 720, "fps": 16}, "status": "ECARTE",
             "notes": "ÉCARTÉ : morphe la caméra et la foule entre deux cadrages différents ; deux images identiques donnent un clip figé. Ne sert qu'avec deux clés distinctes dans le même cadrage.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
            {"code": "wan22-s2v", "label": "Wan 2.2 S2V (speech-to-video)", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "wan2.2_s2v_14B_fp8_scaled + wav2vec2",
             "params": {"width": 1280, "height": 720, "fenetre": "77 images ≤ 4,8 s"}, "status": "ECARTE",
             "notes": "ÉCARTÉ le 22 août 2026 : anime le visage le plus visible, pas le locuteur ; aucun masque ni choix du personnage.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
            {"code": "infinitetalk-wan21", "label": "InfiniteTalk / MultiTalk (MeiGen) sur Wan 2.1", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "Wan 2.1 I2V 14B 720p fp8 + InfiniteTalk-Multi (nœuds Kijai)",
             "params": {"fenetre": 81, "steps": 6, "cfg": 1, "shift": 11, "tempsParPlan8s": "~22 min A100"}, "status": "ECARTE",
             "notes": "ABANDONNÉ par Guillaume le 23 août 2026 : rendu insuffisant (bouches inkman peu alignées, voiture moderne hallucinée), 22 min par plan. L'ordre des pistes audio doit suivre l'ordre des masques.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
            {"code": "minimax-h3", "label": "MiniMax H3 (I2V et R2V, natif ComfyUI)", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "MiniMax H3 + LoRA turbo",
             "params": {"width": 1344, "height": 768, "fps": 24, "formatPrompt": "skill h3-prompt-writing : <d>[French] …</d>, (S1)/(S2) par timbre"}, "status": "CANDIDAT",
             "notes": "Second choix pour un dialogue plus « joué » (Guillaume, 23 août 2026) ; hallucine sur les plans muets (tête géante 4a-1 B, débris 5-2 A). Toujours au format du skill.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
            {"code": "ltx-2.3", "label": "LTX-2.3 I2V (prédécesseur ouvert)", "medium": "VIDEO", "provider": "runpod-comfyui", "modelRef": "LTX-2.3 dev fp8 + LoRA distillée",
             "params": {"width": 1280, "height": 704, "fps": 25}, "status": "ECARTE",
             "notes": "REMPLACÉ par 2.5 dès le jeton Hugging Face obtenu ; a fait tomber ComfyUI une fois au chargement.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
            {"code": "higgsfield-api-video", "label": "Modèles fermés par API Higgsfield (Veo 3.1 Lite, Wan 2.7, Kling 3.0, Seedance 2.0 Mini)", "medium": "VIDEO", "provider": "higgsfield", "modelRef": "veo3_1_lite | wan2_7 | kling3 | seedance2_mini",
             "params": {"credits": "12 à 20 par plan de 8 s", "referenceAudio": "aucune (Wan 2.7 : une seule)"}, "status": "ECARTE",
             "notes": "ÉCARTÉS le 23 août 2026 : tiennent le style et disent le texte, mais aucun ne prend nos voix ; coût dix fois celui d'un pod. Option « voix générées » si l'on renonce au contrôle des voix.", "sourceRef": ref("atelier/moteurs-ecartes/VERDICTS.md")},
        ]
        for m in MOTEURS:
            if m["code"] in codes:
                continue
            self.ecrire("upsert_engine", m)

    # ------------------------------------------------------------ personnages
    def _blocs_episode(self):
        """Blocs identité des personnages d'époque dans assets-et-objets.md §2 : {nom: {famille: bloc}} + à la volée."""
        t = S.lire(S.EP / "prompts" / "assets-et-objets.md")
        sec = t[t.find("## 2.1"):t.find("# 3.") if "# 3." in t else len(t)]
        out, plans = {}, {}
        heads = list(re.finditer(r"^## 2\.\d+ (.+?) \((plans? [^)]+)\)", sec, re.M))
        for i, h in enumerate(heads):
            fin = heads[i + 1].start() if i + 1 < len(heads) else len(sec)
            corps = sec[h.end():fin]
            blocs = {}
            for st, fam in (("A", "_defaut"), ("B", "inkman"), ("C", "cel-2d")):
                m = re.search(r"\*\*Style " + st + r"\*\*\s*```\n(.*?)\n```", corps, re.S)
                if m:
                    blocs[fam] = m.group(1).strip()
            nom = h.group(1).split(",")[0].split("(")[0].strip()
            out[nom] = blocs
            plans[nom] = sorted({int(x) for x in re.findall(r"\d+", h.group(2))})
        for m in re.finditer(r"^\* \*\*(.+?)\*\* \(plans? ([\d, ]+)\) : `(.+?)`", t, re.M):
            out[m.group(1)] = {"_defaut": m.group(3).strip()}
            plans[m.group(1)] = sorted({int(x) for x in re.findall(r"\d+", m.group(2))})
        return out, plans

    def personnages(self):
        existants = self.lire("list_characters", {"show": SHOW, "episode": EP}) if not self.dry else {}
        deja = {(c.get("nom") or c.get("name")): c.get("id") or c.get("characterId") for c in (existants.get("personnages") or existants.get("characters") or [])}
        Bq = charger_briques(BRIQUES)
        tr = S.lire(RACINE / "iletaitunefois" / "serie" / "troupe-recurrente.md")

        def bloc_troupe(nom, style):
            m = re.search(r"^## " + re.escape(nom) + r" — .*?\n(?:.*?\n)*?" + style + r" :\s*```\n(.*?)\n```", tr, re.M | re.S)
            return m.group(1).strip() if m else None
        TROUPE = [
            ("Sam", {"_defaut": bloc_troupe("SAM", "Styles A et C"), "inkman": bloc_troupe("SAM", "Style B"),
                     "incarnation-contemporaine": bloc_troupe("SAM BIS", "Styles A et C"), "incarnation-contemporaine-inkman": bloc_troupe("SAM BIS", "Style B"),
                     "marqueurs": "chapeau à large bord, veste sable, sacoche à étiquettes ; sans barbe, aucune lunette nulle part ; pansement du jour sur la main droite",
                     "negatives": "whip, coiled rope, bullwhip, revolver, gun, glasses, eyeglasses, goggles, sunglasses, any eyewear, full beard, elderly man, walking stick, staff, cane"},
             "sable", "sacoche à étiquettes", "mid thirties"),
            ("Naya", {"_defaut": bloc_troupe("NAYA", "Styles A et C"), "inkman": bloc_troupe("NAYA", "Style B"),
                      "marqueurs": "boucles volumineuses, sweat sarcelle, carnet",
                      "negatives": "flat solid black hair silhouette, hair drawn as one solid shape, solid black hair mass, bare legs, straight hair, pigtails, school uniform, pastel colors on her outfit, teenager proportions"},
             "sarcelle vif", "carnet", "10 ans"),
            ("Elio", {"_defaut": bloc_troupe("ELIO", "Styles A et C"), "inkman": bloc_troupe("ELIO", "Style B"),
                      "marqueurs": "casquette orange visière avant, deux bandes, tablette translucide levée à hauteur de tête",
                      "negatives": "angry scowl, frowning glare, villain expression, mean face, sharp pointed angry eyebrows, sneer, smirk of contempt, backwards cap, removed cap, floating cap, bare head, glasses, smartphone, missing tablet"},
             "orange vif", "tablette", "12 ans"),
        ]
        for nom, canon, couleur, totem, age in TROUPE:
            if nom in deja:
                self.ids[f"perso:{nom}"] = deja[nom]; continue
            out = self.ecrire("upsert_character", {"scope": "SHOW", "show": SHOW, "name": nom, "nature": "FICTION", "recurring": True,
                                                   "ageLabel": age, "reservedColor": couleur, "totem": totem, "canonSheet": canon,
                                                   "sourceRef": ref("iletaitunefois/serie/troupe-recurrente.md", "C")})
            self._garder(f"perso:{nom}", out)
        # personnages d'époque de S01E01
        blocs, plans_de = self._blocs_episode()
        faits = {}
        if not self.dry:
            for f in (self.lire("list_facts", {"show": SHOW, "episode": EP}).get("faits") or []):
                m = re.search(r"Correction (\d\.\d+)", f.get("note") or "")
                if m and f.get("status") != "ECARTE":
                    faits.setdefault(m.group(1), f["id"])
        ident = {k: {FAMILLES[v]: b for v, b in blocs_.items()} for k, blocs_ in Bq.IDENT.items()}
        EPISODE = [
            # (nom, nature, plans, canonSheet, fait historique, locuteurs)
            ("Garnerin", "HISTORIQUE", [3, 4, 5, 61, 63], {**blocs.get("GARNERIN", {}), **ident["GARNERIN"]}, "1.16", ["GARNERIN"]),
            ("L'aide de Garnerin", "FICTION", [3], {**ident["AIDE"], "de-face": ident["AIDE_FACE"]["_defaut"]}, None, ["L'AIDE"]),
            ("Le badaud rond", "FICTION", [2, 64], {**blocs.get("BETTING ONLOOKERS", {}), **ident["PARIEURS_ROND"]}, None, ["BADAUD 1"]),
            ("Le badaud maigre", "FICTION", [2, 64], {**blocs.get("BETTING ONLOOKERS", {}), **ident["PARIEURS_MAIGRE"]}, None, ["BADAUD 2"]),
            ("Foule Directoire", "FIGURANT", [1, 2, 4, 63, 64], {**blocs.get("DIRECTOIRE CROWD", {}), **ident["FOULE"]}, None, []),
            ("Yuan Huangtou", "HISTORIQUE", plans_de.get("YUAN HUANGTOU", [44, 45, 47]), blocs.get("YUAN HUANGTOU", {}), "1.13", []),
            ("Fermiers au semoir", "FIGURANT", plans_de.get("SEED DRILL FARMERS", [21, 22]), blocs.get("SEED DRILL FARMERS", {}), None, ["PAYSAN 1", "PAYSAN 2"]),
            ("Pillards", "FIGURANT", plans_de.get("LOOTERS", [56, 57]), blocs.get("LOOTERS", {}), None, ["PILLARD 1", "PILLARD 2"]),
            ("Porteurs du pont", "FIGURANT", plans_de.get("BRIDGE PORTERS", [50, 51]), blocs.get("BRIDGE PORTERS", {}), None, []),
            ("Badauds du pont", "FIGURANT", plans_de.get("Bridge onlookers", [51]), blocs.get("Bridge onlookers", {}), None, ["LE BADAUD", "L'AUTRE"]),
            ("Moine Huaibing", "HISTORIQUE", plans_de.get("MONK HUAIBING", [39]), blocs.get("MONK HUAIBING", {}), "1.44", []),
            ("Lenormand", "HISTORIQUE", plans_de.get("LENORMAND", [60]), blocs.get("LENORMAND", {}), "2.52", []),
            ("Alchimistes taoïstes", "FIGURANT", plans_de.get("TAOIST ALCHEMISTS", [71]), blocs.get("TAOIST ALCHEMISTS", {}), None, []),
            ("Charretier Han", "FIGURANT", plans_de.get("HAN CARTER", [29]), blocs.get("HAN CARTER", {}), None, []),
            ("Shun", "HISTORIQUE", plans_de.get("Shun", [55]), blocs.get("Shun", {}), "1.15", []),
            ("La sentinelle et le général", "FIGURANT", plans_de.get("Sentry and general", [67]), blocs.get("Sentry and general", {}), None, ["LA SENTINELLE", "LE GÉNÉRAL"]),
            ("Compères faux-monnayeurs", "FIGURANT", plans_de.get("Counterfeiters", [68]), blocs.get("Counterfeiters", {}), None, ["COMPÈRE 1"]),
            ("Empereur Gao Yang", "HISTORIQUE", plans_de.get("Emperor Gao Yang", [44]), blocs.get("Emperor Gao Yang", {}), "1.13", []),
            ("Cavaliers antiques sans étrier", "FIGURANT", plans_de.get("Ancient riders", [30]), blocs.get("Ancient riders", {}), None, []),
            ("Cavaliers avars", "FIGURANT", plans_de.get("Avar horsemen", [32]), blocs.get("Avar horsemen", {}), None, []),
            ("Passants de Ye", "FIGURANT", plans_de.get("Passersby of Ye", [46]), blocs.get("Passersby of Ye", {}), None, []),
        ]
        for nom, nature, plans, canon, fait, locuteurs in EPISODE:
            if not canon:
                self.note(f"- personnage « {nom} » : aucun bloc identité trouvé dans le dépôt, fiche canon vide")
            if nom in deja:
                self.ids[f"perso:{nom}"] = deja[nom]
            else:
                out = self.ecrire("upsert_character", {"scope": "EPISODE", "show": SHOW, "season": 1, "episode": EP, "name": nom, "nature": nature, "recurring": False,
                                                       "historicalFactId": faits.get(fait) if fait else None, "canonSheet": canon or None,
                                                       "sourceRef": ref("iletaitunefois/S01E01/prompts/personnages-episode.md") + " ; " + ref("iletaitunefois/S01E01/prompts/briques_pilote.py", "IDENT")})
                self._garder(f"perso:{nom}", out)
                if fait and not faits.get(fait) and not self.dry:
                    self.note(f"- personnage « {nom} » : fait historique {fait} introuvable en base")
            cid = self.ids.get(f"perso:{nom}")
            for n in plans:
                if self.dans_filtre(n):
                    self.ecrire("link_plan_character", {"show": SHOW, "episode": EP, "plan": n, "characterId": cid or "<id>", "role": nature.lower()})
            for loc in locuteurs:
                self.ecrire("upsert_speaker", {"show": SHOW, "name": loc, "characterId": cid or "<id>"})
        for nom in ("Sam", "Naya", "Elio"):
            cid = self.ids.get(f"perso:{nom}")
            self.ecrire("upsert_speaker", {"show": SHOW, "name": nom.upper(), "characterId": cid or "<id>"})
            reps = S.scenario_repliques()
            for n in sorted({r[0] for r in reps if r[2] == nom.upper()}):
                if self.dans_filtre(n):
                    self.ecrire("link_plan_character", {"show": SHOW, "episode": EP, "plan": n, "characterId": cid or "<id>", "role": "troupe"})
        self.note("- personnages : Sam, Naya, Elio liés aux plans où ils PARLENT (les plans CADRE muets où ils sont présents restent à créditer) ; Sam Bis = clé « incarnation-contemporaine » de la fiche canon de Sam")

    def _garder(self, cle, out):
        if isinstance(out, dict):
            for k in ("id", "characterId", "assetId", "engineId", "voiceId", "cueId", "trialId"):
                if out.get(k):
                    self.ids[cle] = out[k]; return
            for k in ("personnage", "character", "asset", "moteur", "engine", "voix", "voice", "epreuve", "trial", "element", "item"):
                if isinstance(out.get(k), dict) and out[k].get("id"):
                    self.ids[cle] = out[k]["id"]; return

    # ------------------------------------------------------------ continuité visuelle
    def continuite(self):
        existants = {e.get("key") for e in (self.lire("list_continuity_items", {"show": SHOW, "episode": EP}).get("elements") or self.lire("list_continuity_items", {"show": SHOW, "episode": EP}).get("items") or [])} if not self.dry else set()
        src = ref("iletaitunefois/S01E01/prompts/assets-et-objets.md", "7")
        cadre = sorted(n for n, c in S.plan_vers_decor().items() if "D3" in c)
        ITEMS = [
            ("ballon", "Ballon de Garnerin", "OBJET", [1, 2, 3, 4, 5, 6, 61, 62, 63, 64], "§7.1 VALIDÉ — planche Ballon_StyleP"),
            ("nacelle", "Nacelle", "OBJET", [1, 2, 3, 4, 5, 6, 61, 62, 63, 64], "§7.2 VALIDÉ — planche Nacelle_StyleP à deux vues"),
            ("couteau", "Couteau de Garnerin", "OBJET", [3, 5, 61], "§7.3 À GÉNÉRER"),
            ("parachute", "Parachute : fuseau replié puis voilure ouverte", "OBJET", [1, 2, 3, 4, 5, 6, 61, 62, 63, 64], "§7.4 À GÉNÉRER — gréé entre le ballon et la nacelle, jamais au plancher"),
            ("sacoche-de-sam", "Sacoche de Sam", "OBJET", cadre, "§7.5 À ARBITRER"),
            ("hibou-de-papier", "Hibou de papier (cerf-volant de Yuan Huangtou)", "OBJET", [44, 45, 47, 75], "§7.8 À ARBITRER"),
            ("semoir", "Semoir à trois rangs et soc de fonte", "MACHINE", [21, 22], "§7.9 À ARBITRER"),
            ("collier-d-epaule", "Collier d'épaule", "OBJET", [28, 29], "§7.10 À ARBITRER"),
            ("parasols-et-sacs", "Parasols et sacs des pillards", "OBJET", [56, 57], "§7.11 À ARBITRER"),
            ("tablette-d-elio", "Tablette d'Elio", "OBJET", cadre, "§7.12 À ARBITRER"),
            ("carnet-de-naya", "Carnet de Naya", "OBJET", cadre, "§7.12 À ARBITRER"),
            ("carnet-de-sam", "Carnet de terrain de Sam", "OBJET", cadre, "§7.12 À ARBITRER"),
        ]
        c = json.loads((STUDIO_DIR / "contrats.json").read_text(encoding="utf-8"))
        for o in c["objets"]:
            ITEMS.append((f"objet-{o['slug']}", o["slug"].replace("-", " "), "OBJET", [n for n in cadre if 9 <= n <= o["range"]], "§7.6 À ARBITRER — un des neuf objets de la table"))
        for key, label, kind, plans, note in ITEMS:
            if key in existants:
                continue
            if self.filtre is not None and not any(n in self.filtre for n in plans):
                continue
            out = self.ecrire("upsert_continuity_item", {"show": SHOW, "episode": EP, "key": key, "label": label, "kind": kind, "planNumbers": plans, "note": f"{note} — {src}"})
            self._garder(f"cont:{key}", out)
        self.note("- continuité : couteau et parachute n'ont pas de planche (§7.3, §7.4 « À GÉNÉRER ») ; prepare_batch refusera les lots des plans 1 à 6 tant qu'elles n'existent pas — c'est le contrôle voulu")

    # ------------------------------------------------------------ assets
    def assets(self):
        from assembler_prompts import assemble as assemble_cle
        from assembler_refs import assemble_ref
        Bq = charger_briques(BRIQUES)
        st = charger_styles()["StyleP"]
        media_ids = json.loads(MEDIA_IDS.read_text(encoding="utf-8")) if MEDIA_IDS.exists() else {}
        existants = {}
        if not self.dry:
            for a in (self.lire("list_assets", {"show": SHOW, "episode": EP}).get("assets") or []):
                existants[(a.get("slug"), a.get("styleCode"))] = a.get("id")
        # planches de référence
        refs_plans = {"D01": [1, 2, 3, 4, 61, 62, 63, 64], "D02": [4, 5, 6, 61], "Foule": [1, 2, 4, 63, 64], "Garnerin": [3, 4, 5, 61, 63], "Parieurs": [2, 64],
                      "Ballon": [1, 2, 3, 4, 5, 6, 61, 62, 63, 64], "Nacelle": [1, 2, 3, 4, 5, 6, 61, 62, 63, 64]}
        for nom in Bq.REFS_DEFAUT:
            j = assemble_ref(nom, st, Bq)
            slug = nom
            if (slug, "StyleP") in existants:
                self.ids[f"asset:{slug}"] = existants[(slug, "StyleP")]; continue
            out = self.ecrire("upsert_asset", {"show": SHOW, "episode": EP, "slug": slug, "kind": "REFERENCE", "styleCode": "StyleP", "promptPos": j["params"]["prompt"],
                                               "engineCode": "nano-banana-pro", "plans": refs_plans.get(nom, []), "shared": nom in ("D01", "D02", "Ballon", "Nacelle"),
                                               "providerMediaIds": {"higgsfield": media_ids[f"{nom}_StyleP.png"]} if f"{nom}_StyleP.png" in media_ids else None})
            self._garder(f"asset:{slug}", out)
        # images clés, prompt assemblé tel qu'envoyé (blocs de style + briques + clauses + Avoid)
        for name, bloc, brique in Bq.BRIQUES:
            j = assemble_cle(name, bloc, brique, st, Bq, media_ids)
            slug = name
            if (slug, "StyleP") in existants:
                self.ids[f"asset:{slug}"] = existants[(slug, "StyleP")]; continue
            prompt = j["params"]["prompt"]
            pos, neg = (prompt.split(" Avoid: ", 1) + [None])[:2]
            out = self.ecrire("upsert_asset", {"show": SHOW, "episode": EP, "slug": slug, "kind": "IMAGE_CLE", "styleCode": "StyleP", "promptPos": pos, "promptNeg": neg,
                                               "engineCode": "nano-banana-pro", "plans": [plan_de(name)]})
            self._garder(f"asset:{slug}", out)
            for ordre, r in enumerate(Bq.REFS[name]):
                self.ecrire("link_asset_ref", {"sourceId": self.ids.get(f"asset:{slug}", "<id>"), "targetId": self.ids.get(f"asset:{r}", "<id>"), "order": ordre})
        # clips, prompts exactement rendus (montage v7)
        for j in json.loads(CLIPS_JSON.read_text(encoding="utf-8")):
            slug = f"clip-{j['clip']}"
            if (slug, "StyleP") in existants:
                self.ids[f"asset:{slug}"] = existants[(slug, "StyleP")]; continue
            plan = plan_de(j["clip"])
            lignes = [f"{EP}/plan-{plan}/ligne-{o}" for o in (0, 1)] if j["clip"] in ("P02", "P03") else None  # adresse narrative de Studio
            out = self.ecrire("upsert_asset", {"show": SHOW, "episode": EP, "slug": slug, "kind": "CLIP_VIDEO", "styleCode": "StyleP", "promptPos": j["prompt"], "promptNeg": j["negative"],
                                               "engineCode": "ltx-2.5-i2v-2passes", "plans": [plan], "lignes": lignes})
            self._garder(f"asset:{slug}", out)
            self.ecrire("link_asset_ref", {"sourceId": self.ids.get(f"asset:{slug}", "<id>"), "targetId": self.ids.get(f"asset:{j['clip']}", "<id>"), "order": 0})
        # planches d'objets rattachées aux éléments de continuité
        for key, nom in (("ballon", "Ballon"), ("nacelle", "Nacelle")):
            if self.ids.get(f"asset:{nom}"):
                self.ecrire("link_continuity_ref", {"show": SHOW, "episode": EP, "key": key, "refAssetId": self.ids[f"asset:{nom}"]})
        self.note("- assets : les prompts des planches et des clés sont réassemblés par assembler_refs/assembler_prompts sur les briques actuelles ; ceux des clips sont les prompts exactement rendus (clips-StyleP.json). Graines des clips : dans clips-StyleP.json, à porter sur les jobs lors de la reprise des médias.")

    # ------------------------------------------------------------ attendus
    def attendus_plans(self):
        cfg = json.loads((STUDIO_DIR / "attendus.json").read_text(encoding="utf-8"))
        for plan, items in cfg.items():
            if plan.startswith("_") or not self.dans_filtre(int(plan)):
                continue
            for i, it in enumerate(items):
                self.ecrire("upsert_plan_expectation", {"show": SHOW, "episode": EP, "plan": int(plan), "order": i, "kind": it["kind"], "text": it["text"], "critical": it["critical"]})
        self.note("- attendus : saisis pour les plans 1 à 6 seulement ; plans 7 à 80 à saisir avec les briques de chaque séquence")

    # ------------------------------------------------------------ voix
    def voix(self):
        existantes = {v.get("code") for v in (self.lire("list_voices", {"show": SHOW}).get("voix") or self.lire("list_voices", {"show": SHOW}).get("voices") or [])} if not self.dry else set()
        VOIX = [("V-grave", "Voix grave de référence (P1 rond péremptoire, P3 grave autoritaire)", "ohItIVrXTBI80RrUECOD", ["BADAUD 1", "GARNERIN"]),
                ("V-claire", "Voix claire de référence (P2 maigre méfiant, P4 jeune clair)", "jvSOBXJ1cP2sdvT5RgUP", ["BADAUD 2", "L'AIDE"])]
        for code, label, pid, locuteurs in VOIX:
            if code not in existantes:
                self.ecrire("upsert_voice", {"show": SHOW, "code": code, "label": label, "provider": "elevenlabs", "providerVoiceId": pid, "model": "eleven_v3",
                                             "settings": {"usage": "référence de timbre en mode INTEGREE (voix libres LTX-2.5) ; enregistrement des quatre répliques du pilote", "verrouillee_par_guillaume": False},
                                             "sourceRef": ref("iletaitunefois/S01E01/son-et-voix.md", "2")})
            for loc in locuteurs:
                self.ecrire("assign_voice", {"show": SHOW, "speaker": loc, "code": code})
        self.note("- voix : deux voix ElevenLabs de référence seulement (non entérinées) ; le casting à huit voix (V1 Sam, V2 Elio, V3 Naya, P1 à P5) attend les identifiants ElevenLabs de Guillaume")

    # ------------------------------------------------------------ musique et effets
    def son(self):
        src = ref("iletaitunefois/S01E01/son-et-voix.md", "3-4")
        cues = self.lire("list_music_cues", {"show": SHOW, "episode": EP}) if not self.dry else {}
        deja = {c.get("label") for c in (cues.get("plages") or cues.get("cues") or [])}
        MUS = [("Thème des Découvreurs", "THEME", None, None, None, False, "Le thème de la série, généré une fois (Eleven Music, force_instrumental) ; sert de référence audio à toutes les variations. Enthousiasme de conteur, fin grave possible."),
               ("Ouverture froide : attente et tension au parc Monceau", "PIECE", 1, 1, 18, True, "Aube, brume, foule qui attend ; tension retenue, pas de mélodie triomphale."),
               ("L'ascension puis la lame sur la corde", "PIECE", 4, 5, 28, True, "Montée du ballon puis suspens de la lame ; le climax se coupe avant le verdict."),
               ("La crue du fleuve Jaune et le renflouage", "PIECE", 39, 39, 32, True, "Force de l'eau puis ingéniosité du moine Huaibing."),
               ("Le vol du prince", "PIECE", 45, 46, 44, True, "La plus longue plage : un homme suspendu à un hibou de papier, cruauté et beauté."),
               ("La fuite des pillards", "PIECE", 57, 57, 14, True, "Comédie par le bas, rythme de course."),
               ("La descente et le verdict de Garnerin", "PIECE", 62, 63, 38, True, "Le parachute s'ouvre, la nacelle descend, la foule retient son souffle."),
               ("Le teaser final", "PIECE", 80, 80, 10, True, "Sacoche fermée, cerf-volant dans le soir, fondu au noir."),
               ("Lit d'ambiance : le cadre", "LIT", None, None, None, False, "Lit discret sous la voix off et les dialogues de la pièce du cadre."),
               ("Lit d'ambiance : le récit d'époque", "LIT", None, None, None, False, "Lit désaturé sous la voix off des saynètes historiques."),
               ("Lit d'ambiance : la Chine des inventions", "LIT", None, None, None, False, "Couleur locale sobre, sans cliché, sous les montages de vignettes.")]
        for label, kind, a, b, d, nd, brief in MUS:
            if label in deja:
                continue
            self.ecrire("upsert_music_cue", {"show": SHOW, "episode": EP, "label": label, "kind": kind, "planFrom": a, "planTo": b, "durationSec": d, "noDialogue": nd, "brief": brief + f" — {src}"})
        sfx = self.lire("list_sfx_cues", {"show": SHOW, "episode": EP}) if not self.dry else {}
        deja_s = {c.get("label"): c.get("id") for c in (sfx.get("effets") or sfx.get("cues") or [])}
        AMB = ["le cadre intérieur", "le parc au petit matin", "le vent d'altitude", "la campagne antique", "le fleuve en crue", "la ville Song la nuit", "l'atelier et ses fours", "la steppe"]
        SIG = [("le gel d'Elio", [15, 25, 27, 34, 53]), ("la sacoche qui s'ouvre et se referme", [9, 23, 29, 34, 37, 64, 65, 68, 70, 73, 74]), ("la tablette d'Elio", []), ("le crayon de Naya", []), ("la porte du cadre", [8]), ("le carton titre", [6])]
        PON = [("la corde tranchée", 5), ("le ballon qui s'arrache", 4), ("la crue", 39), ("le cerf-volant", 43), ("le pont de bambou", 50), ("les fusées", 71), ("les fours", 70), ("la grange en feu", 54)]
        for label in AMB:
            if f"Ambiance : {label}" not in deja_s:
                self.ecrire("upsert_sfx_cue", {"show": SHOW, "episode": EP, "family": "AMBIANCE_BOUCLEE", "label": f"Ambiance : {label}", "loop": True, "brief": f"Ambiance bouclée sans couture (Eleven SFX v2), 8 à 30 s, couvre une plage entière — {src}", "shared": True})
        for label, plans in SIG:
            lab = f"Signature : {label}"
            if lab not in deja_s:
                self.ecrire("upsert_sfx_cue", {"show": SHOW, "episode": EP, "family": "SIGNATURE", "label": lab, "loop": False, "brief": f"Son de marque conçu une fois, réutilisé à chaque occurrence — {src}", "shared": True})
        for label, n in PON:
            lab = f"Effet : {label}"
            if lab not in deja_s and self.dans_filtre(n):
                self.ecrire("upsert_sfx_cue", {"show": SHOW, "episode": EP, "family": "PONCTUEL", "label": lab, "loop": False, "brief": f"Effet ponctuel du plan {n} — {src}", "shared": False})
        # les identifiants se relisent en base (upsert_sfx_cue ne les rend pas sous une clé connue)
        if not self.dry:
            deja_s = {c.get("label"): c.get("id") for c in (self.lire("list_sfx_cues", {"show": SHOW, "episode": EP}).get("effets") or [])}
        for label, plans in SIG:
            cid = deja_s.get(f"Signature : {label}")
            for n in plans:
                if self.dans_filtre(n):
                    self.ecrire("link_sfx_usage", {"cueId": cid or "<id>", "show": SHOW, "episode": EP, "plan": n})
        for label, n in PON:
            if self.dans_filtre(n):
                self.ecrire("link_sfx_usage", {"cueId": deja_s.get(f"Effet : {label}") or "<id>", "show": SHOW, "episode": EP, "plan": n})

    # ------------------------------------------------------------ épreuve comparative (le pilote)
    def epreuve(self):
        arms = [{"style": s, "moteur": "wan22-i2v-a14b", "montage": f"montage_Style{s}.mp4", "date": "2026-08-22"} for s in "ABC"] + \
               [{"style": s, "moteur": "ltx-2.5-i2v-2passes", "montage": f"montage_Style{s}_v7.mp4", "date": "2026-08-24"} for s in "ABDJK"] + \
               [{"style": "P", "moteur": "ltx-2.5-i2v-2passes", "montage": "montage_StyleP_v7.mp4", "date": "2026-08-27", "retenu": True}]
        out = self.ecrire("upsert_trial", {"show": SHOW, "episode": EP, "label": "Pilote S01E01 — plans 1 à 6, six styles, quatre moteurs",
                                           "question": "Quel style pour la série, quel moteur vidéo, quelle méthode de dialogue ? Tranché par Guillaume : style P (29 août), LTX-2.5 voix libres (24 août).",
                                           "planNumbers": [1, 2, 3, 4, 5, 6], "arms": arms,
                                           "artifacts": {"montages": [a["montage"] for a in arms], "dossier": ["Downloads/EpisodeModernise/pilote/montages/"], "audit": [ref("iletaitunefois/S01E01/pilote/AUDIT.md")], "decisions": [ref("iletaitunefois/S01E01/pilote/DECISIONS.md")]}})
        self._garder("trial", out)
        if not self.dry:
            r = self.ecrire("request_validation", {"kind": "CHOIX_STYLE", "show": SHOW, "episode": EP,
                                                   "title": "Pilote S01E01 — entériner le style P et le moteur LTX-2.5 (décisions des 24 et 29 août 2026)",
                                                   "question": "Le choix est fait hors session (record_decision) ; cette session le rend opposable : sa clôture fournit la décision qui tranche l'épreuve (close_trial) et fixe le style actif.",
                                                   "payload": {"style": "StyleP", "moteur": "ltx-2.5-i2v-2passes", "epreuve": self.ids.get("trial")},
                                                   "writeScope": [f"trial:{self.ids.get('trial', '?')}", "style:StyleP", "engine:ltx-2.5-i2v-2passes"], "expiresInDays": 14, "openedBy": "Claude (import du 30 août 2026)"})
            self.note(f"- épreuve : session CHOIX_STYLE ouverte → {r.get('url')} ; à sa clôture : close_trial(trialId, decisionId)")


def main():
    argv = sys.argv[1:]
    opts = {a.split("=", 1)[0].lstrip("-"): (a.split("=", 1)[1] if "=" in a else True) for a in argv if a.startswith("--")}
    dry = bool(opts.get("dry-run"))
    filtre = B.parse_plans(opts["plans"]) if isinstance(opts.get("plans"), str) else None
    attendus = set(opts["attendus"].split(",")) if isinstance(opts.get("attendus"), str) else set()
    etapes = [opts["etape"]] if isinstance(opts.get("etape"), str) else ETAPES[:ETAPES.index(opts["jusqua"]) + 1] if isinstance(opts.get("jusqua"), str) else ETAPES
    imp = ImportProd(dry, bool(opts.get("force")), filtre, attendus)
    B.DRY.mkdir(parents=True, exist_ok=True)
    code = 0
    for et in etapes:
        print(f"== {et}")
        try:
            getattr(imp, et)()
        except RefusStudio as e:
            print(f"  REFUS {e.code} — {e.message}" + (f" — {json.dumps(e.details, ensure_ascii=False)[:400]}" if e.details else ""))
            print(f"  appel : {e.outil} {json.dumps(e.arguments, ensure_ascii=False)[:600]}")
            imp.note(f"- **REFUS** à l'étape `{et}` : `{e.code}` — {e.message}")
            code = 2; break
        if dry:
            imp.sauver_dry(f"prod-{et}")
        else:
            print(f"  {len(imp.appels)} écritures"); imp.appels = []
            if not imp.controle(et):
                code = 1
                if not opts.get("enchainer"):
                    break
        if not opts.get("enchainer") and not dry and et != etapes[-1]:
            print("  point d'arrêt (--enchainer pour continuer)"); break
    rapport = STUDIO_DIR / "rapport-prod.md"
    rapport.write_text("# Rapport d'import Studio — seconde vague\n\n" + "\n".join(imp.rapport) + "\n", encoding="utf-8", newline="\n")
    print(f"rapport : {rapport}")
    sys.exit(code)


if __name__ == "__main__":
    main()
