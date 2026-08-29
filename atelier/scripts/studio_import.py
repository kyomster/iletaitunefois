#!/usr/bin/env python3
"""Import du dépôt dans Studio, par étapes ordonnées, rejouable, avec point d'arrêt après chaque étape.

Étapes (dans l'ordre) : structure, format, styles, bible, apprentissages, decisions, locuteurs, lieux, plans,
repliques, faits, contrats, prose. Après chaque étape : `check` puis `doctor` ; arrêt sur défaillance bloquante
hors de `--attendus`.

Usage :
  python studio_import.py --dry-run [--etape=plans | --jusqua=repliques] [--plans=1-6]
  python studio_import.py --etape=structure
  python studio_import.py --jusqua=repliques --plans=1-6 --attendus=CONT_QUESTION_OUVERTURE_SANS_REPONSE
  python studio_import.py --enchainer --jusqua=prose
  python studio_import.py --verify            relit Studio et compare aux sources du dépôt (aucune écriture)

Le dry-run écrit un JSON par étape dans iletaitunefois/S01E01/studio/dry-run/ (sans jeton). Les écritures réelles
sont journalisées (empreinte des arguments, _commit) dans studio/journal.jsonl ; un appel déjà journalisé est sauté,
sauf --force. Rien n'est complété de mémoire : ce que les documents ne disent pas reste nul et va dans rapport.md.
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))
import studio_sources as S  # noqa: E402
from bibliotheque import charger_styles  # noqa: E402
from studio_client import RefusStudio, Studio, deja_journalise  # noqa: E402

RACINE = S.RACINE
STUDIO_DIR = S.EP / "studio"
JOURNAL = STUDIO_DIR / "journal.jsonl"
RAPPORT = STUDIO_DIR / "rapport.md"
DRY = STUDIO_DIR / "dry-run"

UNIVERS = {"slug": "il-etait-une-fois", "title": "Il était une fois…"}
SHOW = {"slug": "il-etait-une-fois", "title": "Il était une fois — version 2026"}
SAISON = {"number": 1, "title": "Les Découvreurs"}
EPISODE = {"season": 1, "number": 1, "code": "S01E01", "title": "Nos ancêtres les Chinois", "gabarit": "B",
           "briefRef": "iletaitunefois/fiches_verifie/decouvreurs/S01E01_nos-ancetres-les-chinois.md"}
SHOW_SLUG = SHOW["slug"]
EP_CODE = EPISODE["code"]
ETAPES = ["structure", "format", "styles", "bible", "apprentissages", "decisions", "locuteurs", "lieux", "plans", "repliques", "faits", "contrats", "prose"]
KIND = {"FIXE": "FIXE", "ANIMÉ": "ANIME", "POST": "POST"}
REGISTRE = {"CADRE": "CADRE", "ÉPOQUE": "EPOQUE", "MIXTE": "MIXTE"}


def sha_court():
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=RACINE, capture_output=True, text=True).stdout.strip()
    except Exception:
        return "?"


SHA = sha_court()


def ref(chemin, ancre=None):
    return f"{chemin}@{SHA}" + (f"#{ancre}" if ancre else "")


def md_plain(s):
    return re.sub(r"\*\*|\*|`", "", s).strip()


# ---------------------------------------------------------------- l'exécuteur
class Import:
    def __init__(self, dry, force, plans_filtre, attendus):
        self.dry, self.force, self.filtre, self.attendus = dry, force, plans_filtre, attendus
        self.appels = []
        self.rapport = []
        self.studio = None if dry else Studio(journal=str(JOURNAL))
        self.faits_ids = {}

    def dans_filtre(self, n):
        return self.filtre is None or n in self.filtre

    def note(self, texte):
        self.rapport.append(texte)

    def ecrire(self, outil, args, cle=None):
        """Une écriture : en dry-run elle est consignée, sinon envoyée (sauf déjà journalisée)."""
        args = {k: v for k, v in args.items() if v is not None}
        self.appels.append({"outil": outil, "args": args})
        if self.dry:
            return {"_dry": True}
        if not self.force and deja_journalise(JOURNAL, outil, args):
            return {"_deja": True}
        out = self.studio.appeler(outil, args)
        return out

    def lire(self, outil, args=None):
        if self.dry:
            return {}
        return self.studio.appeler(outil, args or {})

    def controle(self, etape):
        if self.dry:
            return True
        chk = self.lire("check", {"show": SHOW_SLUG, "episode": EP_CODE})
        bloquantes = [d for d in (chk.get("bloquantes") or chk.get("defaillances") or []) if isinstance(d, dict)]
        codes = sorted({d.get("code") for d in bloquantes if d.get("code")})
        hors = [c for c in codes if c not in self.attendus]
        print(f"  check après {etape} : {codes or 'rien'}" + (f" — HORS ATTENDUS : {hors}" if hors else ""))
        self.note(f"- check après `{etape}` : {codes or 'rien'}")
        return not hors

    def sauver_dry(self, etape):
        DRY.mkdir(parents=True, exist_ok=True)
        (DRY / f"{etape}.json").write_text(json.dumps(self.appels, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  dry-run : {len(self.appels)} appels → {DRY / (etape + '.json')}")
        self.appels = []

    # ------------------------------------------------------------ étapes
    def structure(self):
        univers = {u.get("slug") for u in (self.lire("list_universes").get("univers") or [])}
        if UNIVERS["slug"] not in univers:
            self.ecrire("create_universe", UNIVERS)
        shows = {s.get("slug") for s in (self.lire("list_shows").get("programmes") or [])}
        if SHOW_SLUG not in shows:
            self.ecrire("create_show", {**SHOW, "universe": UNIVERS["slug"]})
        show = self.lire("get_show", {"slug": SHOW_SLUG}) if not self.dry and SHOW_SLUG in shows else {}
        prog = show.get("programme") or show.get("show") or show
        saisons = {s.get("number") for s in (show.get("saisons") or prog.get("saisons") or show.get("seasons") or [])}
        if SAISON["number"] not in saisons:
            self.ecrire("create_season", {"show": SHOW_SLUG, **SAISON})
        eps = {e.get("code") for e in (self.lire("list_episodes", {"show": SHOW_SLUG}).get("episodes") or [])} if not self.dry else set()
        if EP_CODE not in eps:
            self.ecrire("create_episode", {"show": SHOW_SLUG, **EPISODE})

    def format(self):
        valeurs_show = {
            "langue": "fr", "dureeEpisodeSec": 1260, "dureeEpisodeToleranceSec": 60,
            "debitMotsParMinuteMin": 85, "debitMotsParMinuteMax": 95, "budgetMotsTolerance": 0.05,
            "registres": ["CADRE", "EPOQUE", "MIXTE"], "kinds": ["FIXE", "ANIME", "POST"],
            "voiceMode": "INTEGREE",
            "ratioAnimeMax": 0.40, "blocAnimeMaxSec": 10, "refsMaxParPrompt": 7,
            "image": {"engine": "nano_banana_pro", "ratio": "16:9", "resolution": "2k"},
            "video": {"engineCode": "ltx-2.5-i2v-2passes", "imagesParSeconde": 24, "resolution": [1280, 704], "longueurFormule": "8n+1", "dureeClipMaxSec": 10, "passes": 2},
        }
        actuel = self.lire("get_format", {"show": SHOW_SLUG}) if not self.dry else {}
        fmt = actuel.get("format") or actuel.get("valeurs") or {}
        if not fmt or any(fmt.get(k) != v for k, v in valeurs_show.items()):
            self.ecrire("set_format", {"scope": "SHOW", "show": SHOW_SLUG, "values": valeurs_show, "sourceRef": ref("ecriture/METHODE-ecriture.md", "5-et-5bis")})
        valeurs_saison = {"objectionElioAvantSec": 180, "gelsParEpisode": [3, 6], "gagsParEpisode": [10, 15], "styleRetenu": "StyleP",
                          "muetMinSec": 480, "muetMaxSec": 720}
        actuel_s = self.lire("get_format", {"show": SHOW_SLUG, "season": 1}) if not self.dry else {}
        fmt_s = actuel_s.get("format") or actuel_s.get("valeurs") or {}
        if any(fmt_s.get(k) != v for k, v in valeurs_saison.items()):
            self.ecrire("set_format", {"scope": "SEASON", "show": SHOW_SLUG, "season": 1, "values": valeurs_saison, "sourceRef": ref("iletaitunefois/serie/BIBLE-Les-Decouvreurs.md")})
        self.note("- format : `ratioAnimeMax`, `blocAnimeMaxSec`, `image`, `refsMaxParPrompt` sont conservés par Studio mais lus par aucune règle (à rapporter à l'auteur du serveur).")

    def styles(self):
        existants = {s.get("code") for s in (self.lire("list_styles", {"show": SHOW_SLUG}).get("styles") or [])} if not self.dry else set()
        for code, st in charger_styles().items():
            if code in existants:
                continue
            notes = ""
            stylemd = RACINE / "styles" / st["dossier"] / "STYLE.md"
            if stylemd.exists():
                m = re.search(r"\*\*Verdict[^*]*\*\*[ :]*(.+)", stylemd.read_text(encoding="utf-8"))
                notes = md_plain(m.group(1))[:600] if m else ""
            self.ecrire("upsert_style", {
                "show": SHOW_SLUG, "code": code, "label": st["nom"], "family": st["famille"],
                "formulaEn": st["scene"], "sceneBlockEn": st.get("personnage") or None, "eraTreatment": st.get("epoque") or None,
                "negativeBase": ", ".join(x for x in (st.get("negative"), st.get("neg_epoque"), st.get("neg_universelle")) if x) or None,
                "attributes": {k: st.get(k) for k in ("lettre", "dossier", "variante_identite", "retenu_pour", "personnage_epoque", "lumiere", "clip", "negative", "neg_epoque", "neg_universelle") if st.get(k) is not None},
                "notes": (f"Retenu pour : {st['retenu_pour']}. " if st.get("retenu_pour") else "") + notes or None,
                "sourceRef": ref(f"styles/{st['dossier']}/style.json"),
            })
        self.note("- styles : `formulaEn` = bloc `scene` du style.json, `sceneBlockEn` = bloc `personnage` ; verrouillés dès la création par Studio.")

    def bible(self):
        existantes = self.lire("list_bible", {"show": SHOW_SLUG}) if not self.dry else {}
        deja = {(e.get("category"), e.get("key")): e for e in (existantes.get("entrees") or existantes.get("entries") or [])}
        CAT = {1: ("NARRATION", "serie.pitch", True), 2: ("NARRATION", "gabarits", False), 3: ("NARRATION", "dispositif.verification", False),
               4: ("ECRITURE", "ecriture.regles-serie", False), 8: ("PERSONNAGES", "cast.troupe", True), 9: ("ECRITURE", "toujours-jamais", False),
               10: ("PRODUCTION", "production.contraintes-ia", True)}
        for num, titre, corps in S.bible_entrees():
            cat, key, prompt = CAT.get(num, ("NARRATION", f"section.{num}", False))
            if (cat, key) in deja and md_plain(deja[(cat, key)].get("body", "")) == md_plain(corps):
                continue
            value = {"secondes": 180} if num == 4 else None
            self.ecrire("upsert_bible_entry", {"show": SHOW_SLUG, "category": cat, "key": key, "title": titre, "body": corps, "value": value,
                                               "enforceable": False, "affectsPrompt": prompt, "severity": "ERREUR" if num in (8, 9) else "ATTENTION",
                                               "sourceRef": ref("iletaitunefois/serie/BIBLE-Les-Decouvreurs.md", str(num))})
        # méthode générique d'écriture : sections 0, 5, 5 bis, 6, 7, 11
        t = S.lire(RACINE / "ecriture" / "METHODE-ecriture.md")
        heads = list(re.finditer(r"^## (\d+(?: bis)?)\. (.+)$", t, re.M))
        for i, m in enumerate(heads):
            fin = heads[i + 1].start() if i + 1 < len(heads) else len(t)
            corps = t[m.end():fin].strip().strip("-").strip()
            key = "methode." + m.group(1).replace(" ", "")
            if ("METHODE", key) in deja and md_plain(deja[("METHODE", key)].get("body", "")) == md_plain(corps):
                continue
            self.ecrire("upsert_bible_entry", {"show": SHOW_SLUG, "category": "METHODE", "key": key, "title": m.group(2).strip(), "body": corps,
                                               "value": {"secondes": 10} if m.group(1) == "5 bis" else None, "enforceable": False,
                                               "affectsPrompt": m.group(1) in ("5 bis", "11"), "severity": "ERREUR" if m.group(1) in ("5 bis", "7") else "ATTENTION",
                                               "sourceRef": ref("ecriture/METHODE-ecriture.md", m.group(1).replace(" ", "-"))})
        self.note("- bible : aucune entrée `enforceable` (le serveur refuse une règle exécutable sans fonction) ; `decoupage.bloc.dureeMax` non exécutable car la règle serveur teste la durée du plan, pas des blocs.")

    def apprentissages(self):
        existants = self.lire("list_learnings", {"show": SHOW_SLUG}) if not self.dry else {}
        deja = {(a.get("number"), a.get("title")) for a in (existants.get("apprentissages") or existants.get("learnings") or [])}
        deja_titres = {t for _, t in deja}
        for r in S.methode_regles():
            if (r["numero"], r["titre"]) in deja:
                continue
            self.ecrire("upsert_learning", {"show": SHOW_SLUG, "category": "IMAGE", "title": r["titre"], "body": r["corps"], "kind": "REGLE",
                                            "doNotRetry": False, "number": r["numero"], "evidence": r["evidence"], "sourceRef": ref(r["source"]), "date": r["date"]})
            if not r["evidence"]:
                self.note(f"- règle {r['numero']} : aucune preuve chiffrée dans le corps (evidence nulle)")
        for r in S.strategie_regles():
            if r["titre"] in deja_titres:
                continue
            self.ecrire("upsert_learning", {"show": SHOW_SLUG, "category": "VIDEO", "title": r["titre"], "body": r["corps"], "kind": "REGLE",
                                            "doNotRetry": False, "sourceRef": ref(r["source"]), "date": "2026-08-27"})
        for v in S.verdicts_moteurs():
            titre = f"Moteur écarté : {v['moteur']}"
            if titre in deja_titres:
                continue
            self.ecrire("upsert_learning", {"show": SHOW_SLUG, "category": "VIDEO", "title": titre, "body": v["corps"], "kind": "RESULTAT_NEGATIF",
                                            "doNotRetry": v["doNotRetry"], "evidence": v["evidence"], "sourceRef": ref(v["source"]), "date": "2026-08-24"})
        ASTUCES = [
            ("L'API S3 de RunPod refuse HeadObject et supprime dossier par dossier", "`download_file` de boto3 échoue (403 sur HeadObject) : lire `get_object` directement. `DeleteObject` sur un dossier non vide échoue : supprimer par profondeur décroissante. `DeleteObjects` (lot) répond 307.", "atelier/RUNPOD.md"),
            ("La transcription se trompe sur les nombres : elle place, elle ne juge pas", "« Dix francs » est ressorti « Dis Franck » sur trois montages justes. La transcription horodatée sert à placer les mots et à repérer une bande son inventée ; la prononciation d'un nombre ou d'un nom propre se juge à l'oreille.", "atelier/STRATEGIE-video.md"),
            ("Quand EU-RO-1 n'a pas de GPU, on attend plutôt que de déménager", "Le volume et ses 37 Go de modèles y résident : attendre la capacité (boucle de relance) coûte moins que 45 minutes de retéléchargement dans un autre datacenter.", "atelier/RUNPOD.md"),
            ("Un défaut de planche est multiplié par le nombre de réinjections", "Une planche Foule fautive à 2 crédits a coûté 16 crédits de clés et sept clips : on regarde la planche avant d'en dériver quoi que ce soit.", "iletaitunefois/S01E01/pilote/AUDIT.md"),
        ]
        for titre, corps, src in ASTUCES:
            if titre in deja_titres:
                continue
            self.ecrire("upsert_learning", {"show": SHOW_SLUG, "category": "OUTILS", "title": titre, "body": corps, "kind": "ASTUCE", "doNotRetry": False,
                                            "sourceRef": ref(src), "date": "2026-08-27"})

    def decisions(self):
        for d in S.decisions():
            if d["statut"] == "en vigueur":
                kind = "CHOIX_STYLE" if "style" in d["titre"].lower() and "P" in d["titre"] else ("CHOIX_TECHNIQUE" if any(k in d["titre"].lower() for k in ("moteur", "runpod", "higgsfield", "vidéo", "raccord", "bloc")) else "ARBITRAGE")
                decided = "Guillaume" if "Guillaume" in d["corps"] or kind == "CHOIX_STYLE" else "pilote S01E01 (non attribué)"
                outcome = {"date": d["date"], "resume": md_plain(d["corps"])[:1500], "aEnteriner": "entériner" in d["corps"].lower()}
            else:
                kind = "REMPLACEE"; decided = "pilote S01E01"
                outcome = {"date": d["date"], "remplaceePar": d["remplacee_par"], "pourquoi": d["pourquoi"]}
            self.ecrire("record_decision", {"show": SHOW_SLUG, "kind": kind, "title": d["titre"], "outcome": outcome, "decidedBy": decided,
                                            "note": f"{ref('iletaitunefois/S01E01/pilote/DECISIONS.md')} — {d['statut']}"})
        self.note("- décisions : `record_decision` n'a aucune lecture côté serveur ; le dédoublonnage repose sur journal.jsonl seulement.")

    def locuteurs(self):
        reps = S.scenario_repliques()
        noms = S.locuteurs()
        if self.filtre is not None:
            noms = [n for n in noms if any(r[2] == n and r[0] in self.filtre for r in reps)]
        for nom in noms:
            self.ecrire("upsert_speaker", {"show": SHOW_SLUG, "name": nom})

    def lieux(self):
        cfg = json.loads((STUDIO_DIR / "lieux.json").read_text(encoding="utf-8"))
        sp = S.scenario_plans()
        bible_plateau = S.lire(S.SCENARIO)
        deb = bible_plateau.find("## Bible de plateau"); fin = bible_plateau.find("## Découpage détaillé")
        plateau = bible_plateau[deb:fin]
        for code, d in S.production_decors().items():
            if self.filtre is not None and not any(n in self.filtre for n in d["plans"]):
                continue
            desc = f"{d['nom']} · plans {', '.join(map(str, d['plans']))}"
            m = re.search(r"^### (.+?\(décor " + code.replace("D", "D") + r"\b.*?)$", plateau, re.M)
            if m:
                bloc = plateau[m.end():]
                bloc = bloc[:bloc.find("\n### ")] if "\n### " in bloc else bloc
                desc = m.group(1) + "\n" + bloc.strip()
            era = None
            for n in d["plans"]:
                if n in sp and "LIEU" in sp[n]["fiche"]:
                    era = sp[n]["fiche"]["LIEU"]; break
            sur = cfg["surcharges"].get(code, {})
            args = {"show": SHOW_SLUG, "episode": EP_CODE, "code": code, "name": d["nom"], "era": era or "non écrit dans le scénario", "description": desc,
                    "eraDebutAnnee": sur.get("eraDebutAnnee"), "eraFinAnnee": sur.get("eraFinAnnee"), "eraPrecision": sur.get("eraPrecision")}
            self.ecrire("upsert_location", args)
            if not sur:
                self.note(f"- lieu {code} : époque non chiffrée (texte libre : « {era} »)" + (f" — {cfg['aValider'][code]}" if code in cfg.get("aValider", {}) else ""))

    def plans(self):
        cfg = json.loads((STUDIO_DIR / "lieux.json").read_text(encoding="utf-8"))
        sp, pt, pd = S.scenario_plans(), S.production_tableau(), S.plan_vers_decor()
        for n in sorted(sp):
            if not self.dans_filtre(n):
                continue
            s, p = sp[n], pt[n]
            fiche = s["fiche"]
            synopsis = f"{s['titre']} — " + " ".join(f"{k} · {v}" for k, v in fiche.items() if k in ("LIEU", "CADRE", "CADRE ET ACTION", "ACTION"))
            mouv = next((b[3] for b in p["blocs"] if b[3]), None) or fiche.get("CAMÉRA")
            decors = pd.get(n, [])
            code_decor = cfg["plan_decor"].get(str(n), decors[0] if len(decors) == 1 else None)
            if code_decor is None and n not in (6,):
                self.note(f"- plan {n} : décor non tranché ({decors or 'aucun au roster'})")
            blocs = " | ".join(f"{b[0] or '—'} · {b[1]} s · {b[2]}" for b in p["blocs"])
            board = [f"TYPE SCÉNARIO · {s['type_scenario']} (plan de production : {p['type']}) · REGISTRE · {p['registre']}", f"BLOCS · {blocs}"]
            if p["type"] == "POST" and p["blocs"][0][3]:
                board.append(f"POST · {p['blocs'][0][3]}")
            for k in ("RACCORDS", "INTERDITS", "HORS CADRE"):
                if k in fiche:
                    board.append(f"{k} · {fiche[k]}")
            args = {"show": SHOW_SLUG, "episode": EP_CODE, "number": n, "durationSec": sum(b[1] for b in p["blocs"]),
                    "kind": KIND[p["type"]], "register": REGISTRE[p["registre"]], "synopsis": synopsis[:4000],
                    "locationCode": code_decor, "cameraMove": mouv, "boardNote": "\n".join(board)[:4000]}
            sur = cfg["surcharges"].get(code_decor or "", {})
            if sur.get("eraDebutAnnee") is not None and code_decor in ("D1", "D2", "D34"):
                args.update({"sceneAnneeDebut": sur["eraDebutAnnee"], "sceneAnneeFin": sur["eraFinAnnee"], "scenePrecision": sur["eraPrecision"]})
            self.ecrire("upsert_plan", args)

    def repliques(self):
        for n, ordre, loc, did, txt, off in S.scenario_repliques():
            if not self.dans_filtre(n):
                continue
            self.ecrire("upsert_line", {"show": SHOW_SLUG, "episode": EP_CODE, "plan": n, "order": ordre, "speaker": loc, "text": txt,
                                        "voiceOff": off, "didascalie": did})

    def faits(self):
        cfg_p = STUDIO_DIR / "faits.json"
        cfg = json.loads(cfg_p.read_text(encoding="utf-8")) if cfg_p.exists() else {"periodes": {}, "plans": {}}
        STATUT = {"confirme": "VERIFIE", "imprecis": "VERIFIE", "errone": "VERIFIE", "depasse": "VERIFIE", "non_tranche": "A_VERIFIER"}
        CONF = {"haute": "ETABLI", "moyenne": "PROBABLE", "basse": "DISPUTE"}
        for f in S.audit_faits():
            cle = f"{f['passe']}.{f['numero']}"
            if cle in cfg.get("exclus", {}):
                self.note(f"- fait {cle} : exclu — {cfg['exclus'][cle]}")
                continue
            if not f["sources"]:
                self.note(f"- fait {f['passe']}.{f['numero']} : renvoi ({', '.join(f['renvoi']) or 'sans source'}), non importé")
                continue
            titre, url = f["sources"][0]
            autres = " ; ".join(t + (f" — {u}" if u else "") for t, u in f["sources"][1:])
            stype = "WEB" if url else ("OUVRAGE" if re.search(r"\*[^*]+\*|\d{4}", titre) else "ARTICLE")
            if "*" in titre and re.search(r"\*(PNAS|Isis|Nature|Veget|Journal|Revue)", titre):
                stype = "ARTICLE"
            note = f"Correction {f['passe']}.{f['numero']} de l'audit ({f['section']}) ; statut de l'épisode : {f['statut']}." + (f" Autres sources : {autres}." if autres else "")
            if "kitepatents" in (url or ""):
                note += " Source proscrite comme source unique par le référentiel du corpus."
            per = cfg.get("periodes", {}).get(f"{f['passe']}.{f['numero']}", {})
            base = {"show": SHOW_SLUG, "episode": EP_CODE, "sourceType": stype, "sourceTitle": md_plain(titre)[:300], "sourceUrl": url,
                    "confidence": CONF.get(f["confiance"], "PROBABLE"), "periodeDebutAnnee": per.get("debut"), "periodeFinAnnee": per.get("fin"),
                    "periodePrecision": per.get("precision"), "whenLabel": per.get("libelle")}
            cle = f"{f['passe']}.{f['numero']}"
            out = self.ecrire("upsert_fact", {**base, "claim": md_plain(f["etat_2026"])[:2000], "detail": md_plain(f["enonce"])[:2000],
                                              "status": STATUT.get(f["statut"], "A_VERIFIER"), "note": note})
            if isinstance(out, dict) and (out.get("id") or out.get("factId")):
                self.faits_ids[cle] = out.get("id") or out.get("factId")
            if f["statut"] == "errone":
                out2 = self.ecrire("upsert_fact", {**base, "claim": md_plain(f["enonce"])[:2000], "detail": "Ce que l'épisode d'origine affirmait ; réfuté par la vérification 2026.",
                                                   "status": "ECARTE", "note": f"Énoncé erroné de l'épisode, correction {cle} : " + md_plain(f["etat_2026"])[:800]})
                if isinstance(out2, dict) and (out2.get("id") or out2.get("factId")):
                    self.faits_ids[cle + ".ecarte"] = out2.get("id") or out2.get("factId")
        if not self.dry:
            # les identifiants viennent de la base (upsert_fact ne les rend pas tous) : la note porte « Correction p.n »
            for fait in (self.lire("list_facts", {"show": SHOW_SLUG, "episode": EP_CODE}).get("faits") or []):
                m = re.search(r"Correction (\d\.\d+)", fait.get("note") or "")
                if m and fait.get("status") != "ECARTE":
                    self.faits_ids.setdefault(m.group(1), fait["id"])
        for cle, plans in cfg.get("plans", {}).items():
            fid = self.faits_ids.get(cle)
            if not fid:
                if not self.dry:
                    self.note(f"- fait {cle} : identifiant inconnu (import antérieur ?), lien non posé")
                continue
            for n in plans:
                if self.dans_filtre(n):
                    self.ecrire("link_fact", {"show": SHOW_SLUG, "episode": EP_CODE, "factId": fid, "plan": n})
        if self.faits_ids:
            (STUDIO_DIR / "faits-ids.json").write_text(json.dumps(self.faits_ids, ensure_ascii=False, indent=1), encoding="utf-8")

    def contrats(self):
        c = json.loads((STUDIO_DIR / "contrats.json").read_text(encoding="utf-8"))
        ok = lambda a, b: self.filtre is None or (a in self.filtre and b in self.filtre)
        for b in c["beats"]:
            if ok(b["planFrom"], b["planTo"]):
                self.ecrire("upsert_narrative_beat", {"show": SHOW_SLUG, "episode": EP_CODE, "code": b["code"], "role": b["role"], "ordre": b["ordre"],
                                                      "planFrom": b["planFrom"], "planTo": b["planTo"], "sourceRef": ref("iletaitunefois/S01E01/scenario.md", "minutage") + " — " + b["sourceRef"]})
        for p in c["promesses"]:
            if not self.dans_filtre(p["plantedPlan"]):
                continue
            args = {"show": SHOW_SLUG, "key": p["key"], "label": p["label"], "kind": p["kind"], "portee": p["portee"], "episode": p.get("episode"),
                    "plantedEpisode": p["plantedEpisode"], "plantedPlan": p["plantedPlan"], "status": p.get("status", "PLANTEE"), "note": p["note"], "sourceRef": ref(p["sourceRef"])}
            self.ecrire("upsert_promesse", args)
            if p.get("paiement") and self.dans_filtre(p["paiement"]["plan"]):
                self.ecrire("set_promesse_paiement", {"show": SHOW_SLUG, "key": p["key"], "portee": p["portee"], "porteeEpisode": p.get("episode"),
                                                      "episode": p["paiement"]["episode"], "plan": p["paiement"]["plan"]})
        for q in c["questions"]:
            if self.dans_filtre(q["askedPlan"]):
                self.ecrire("upsert_open_question", {"show": SHOW_SLUG, "episode": EP_CODE, "key": q["key"], "label": q["label"], "askedPlan": q["askedPlan"],
                                                     "status": "POSEE", "sourceRef": ref(q["sourceRef"])})
                if self.dans_filtre(q["reponse"]):
                    self.ecrire("answer_open_question", {"show": SHOW_SLUG, "episode": EP_CODE, "key": q["key"], "plan": q["reponse"]})
        if self.filtre is None or c["objets_sur_table_depuis"] in self.filtre:
            existantes = self.lire("list_state_facts", {"show": SHOW_SLUG, "episode": EP_CODE}) if not self.dry else {}
            if not (existantes.get("etats") or existantes.get("stateFacts")):
                for e in c["echelles"]:
                    self.ecrire("upsert_state_scale", {"show": SHOW_SLUG, "kind": e["kind"], "ordre": e["ordre"], "monotone": e["monotone"], "portee": e["portee"],
                                                       "usageMinimum": e.get("usageMinimum"), "sourceRef": ref(e["sourceRef"])})
                for o in c["objets"]:
                    subj = f"objet:{o['slug']}"
                    self.ecrire("upsert_state_fact", {"show": SHOW_SLUG, "episode": EP_CODE, "subject": subj, "kind": "POSSESSION", "key": "table",
                                                      "value": "sur-la-table", "fromPlan": c["objets_sur_table_depuis"], "sourceRef": ref(c["objets_sourceRef"])})
                    if self.dans_filtre(o["range"]):
                        self.ecrire("upsert_state_fact", {"show": SHOW_SLUG, "episode": EP_CODE, "subject": subj, "kind": "POSSESSION", "key": "table",
                                                          "value": "rangee", "fromPlan": o["range"], "sourceRef": ref(c["objets_sourceRef"])})
                for u in c["emplois"]:
                    if not self.dans_filtre(u["plan"]):
                        continue
                    for o in c["objets"]:
                        requiert = "rangee" if o["range"] <= u["plan"] else "sur-la-table"
                        self.ecrire("upsert_state_usage", {"show": SHOW_SLUG, "episode": EP_CODE, "subject": f"objet:{o['slug']}", "kind": "POSSESSION", "key": "table",
                                                           "plan": u["plan"], "requiert": requiert, "sourceRef": ref(u["sourceRef"]) + " — " + u["attendu"]})
            else:
                self.note("- contrats : états des objets déjà en base, non renvoyés (créations non rejouables)")
        self.note(f"- contrats : {c['alerte_etrier']}")
        self.note("- contrats : l'échelle CONVICTION d'Elio est une proposition non validée, non envoyée (contrats.json → propositions)")

    def prose(self):
        base = {"scope": "SHOW", "show": SHOW_SLUG, "lang": "fr", "license": None, "active": True, "sourceRef": ref("iletaitunefois/serie/CHARTE-prose.md", "4-5")}
        REGLES = [
            {"category": "CONTRAINTE_SERIE", "key": "mots-de-fabrication", "title": "Aucun mot de fabrication ne survit dans la prose",
             "explanation": "Le manuscrit ne dit jamais plan, cadre, raccord, contrechamp, caméra, plongée, gros plan, vignette, clip, image clé, décor, D1…D4, interdits, animé, fixe, désaturé, saturé, palette, style, registre : la consigne technique devient une sensation.",
             "fixHint": "Remplacer la consigne par ce que le lecteur voit ou ressent : « On voyait tout le parc d'un coup » pour un plan très large, « Il n'y avait plus au monde que cette main et cette corde » pour un gros plan.",
             "detector": {"type": "mots", "valeurs": ["hors cadre", "contrechamp", "contre plongée", "gros plan", "image clé", "raccord", "caméra", "vignette", "clip", "désaturé", "palette", "registre"], "casse": False},
             "weight": 3, "severity": "ERREUR", "applyOrder": 5,
             "examples": {"mauvais": "Gros plan sur la main qui serre la corde.", "bon": "Il n'y avait plus au monde que cette main et cette corde."}},
            {"category": "CONTRAINTE_SERIE", "key": "anachronisme-parachute", "title": "Personne ne prononce « parachute » avant que Lenormand ne forge le mot",
             "explanation": "Zéro anachronisme de langage dans les scènes d'époque : en 1797 on dit citoyen et on compte en francs ; le mot parachute n'existe qu'à partir de 1785 et dans la bouche de ceux qui le connaissent.",
             "fixHint": "Dans une scène antérieure à 1785, nommer l'objet par sa forme (la voilure, la toile, les chapeaux de paille).",
             "detector": None, "severity": "ERREUR", "applyOrder": 5},
            {"category": "CONTRAINTE_SERIE", "key": "couleurs-reservees", "title": "Sable, sarcelle et orange vif appartiennent à la troupe",
             "explanation": "Un vêtement d'époque n'est jamais de ces trois couleurs ; on écrit la matière : laine écrue, chanvre, toile à sac, soie crème.",
             "fixHint": "Remplacer la couleur réservée par une matière ou une teinte d'époque.", "detector": None, "severity": "ATTENTION", "applyOrder": 5},
            {"category": "CONTRAINTE_SERIE", "key": "et-puis", "title": "Chaîne mais/donc : jamais « et puis » entre deux étapes",
             "explanation": "Chaque étape du récit est reliée à la précédente par mais ou donc, jamais par simple juxtaposition.",
             "fixHint": "Réécrire la transition avec la conséquence (donc) ou l'opposition (mais) qui la justifie.",
             "detector": {"type": "connecteur", "interdits": ["et puis"], "autorises": ["mais", "donc"]}, "weight": 2, "severity": "ERREUR", "applyOrder": 10},
            {"category": "TYPOGRAPHIE", "key": "guillemets-francais", "title": "Guillemets français, jamais droits",
             "explanation": "Le texte dit est cité entre « et » ; les guillemets droits sont une trace de fabrication.", "fixHint": "Remplacer \" par « » avec espaces insécables.",
             "detector": {"type": "typographie", "sous_type": "guillemets_droits"}, "weight": 1, "severity": "ATTENTION", "applyOrder": 60},
            {"category": "JUGEMENT", "key": "bible-de-plateau-invisible", "title": "La bible de plateau est invisible mais respectée",
             "explanation": "Naya à gauche, Elio à droite, Sam au fond ; la porte côté Naya, la fenêtre et la sacoche côté Elio ; Sam sans barbe et sans lunette, pansement main droite ; la table porte exactement les objets non rangés ; une seule nacelle. On l'écrit en mouvement, jamais en notice.",
             "fixHint": "Vérifier la géographie et le compte des objets à chaque retour dans la pièce.", "detector": None, "severity": "ATTENTION", "applyOrder": 50},
        ]
        existantes = self.lire("list_prose_rules", {"show": SHOW_SLUG, "lang": "fr"}) if not self.dry else {}
        deja = {r.get("key") for r in (existantes.get("regles") or existantes.get("rules") or [])}
        for r in REGLES:
            if r["key"] in deja:
                continue
            self.ecrire("upsert_prose_rule", {**base, **r})
        prose = S.EP / "novelcrafter" / "S01E01-prose-novelcrafter.md"
        if prose.exists():
            t = prose.read_text(encoding="utf-8")
            chap = [m.start() for m in re.finditer(r"^## ", t, re.M)]
            deja_v = {v.get("label") for v in (self.lire("list_voice_samples", {"show": SHOW_SLUG}).get("echantillons") or [])} if not self.dry else set()
            for i, lab in ((0, "prose S01E01 — ouverture froide"), (6, "prose S01E01 — le cadre")):
                if i < len(chap) and lab not in deja_v:
                    fin = chap[i + 1] if i + 1 < len(chap) else len(t)
                    corps = t[chap[i]:fin]
                    corps = corps[corps.find("\n") + 1:].strip()[:2500]
                    self.ecrire("upsert_voice_sample", {"show": SHOW_SLUG, "label": lab, "lang": "fr", "sample": corps, "sourceRef": ref(S.rel(prose))})
            self.note("- prose : échantillons de voix pris dans la prose validée de S01E01 (hypothèse : le serveur attend « votre propre écriture » ; à remplacer par des textes de Guillaume s'il en a)")


# ---------------------------------------------------------------- pilotage
def parse_plans(expr):
    out = set()
    for part in expr.split(","):
        if "-" in part:
            a, b = part.split("-"); out |= set(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def main():
    argv = sys.argv[1:]
    opts = {a.split("=", 1)[0].lstrip("-"): (a.split("=", 1)[1] if "=" in a else True) for a in argv if a.startswith("--")}
    dry = bool(opts.get("dry-run"))
    filtre = parse_plans(opts["plans"]) if isinstance(opts.get("plans"), str) else None
    attendus = set(opts["attendus"].split(",")) if isinstance(opts.get("attendus"), str) else set()
    if opts.get("verify"):
        return verify()
    if isinstance(opts.get("etape"), str):
        etapes = [opts["etape"]]
    else:
        fin = opts.get("jusqua") if isinstance(opts.get("jusqua"), str) else ETAPES[-1]
        etapes = ETAPES[:ETAPES.index(fin) + 1]
    STUDIO_DIR.mkdir(parents=True, exist_ok=True)
    imp = Import(dry, bool(opts.get("force")), filtre, attendus)
    rapport = [f"# Rapport d'import Studio — {date.today().isoformat()}", "", f"Dépôt `{SHA}` ; dry-run : {dry} ; plans : {sorted(filtre) if filtre else 'tous'} ; étapes : {', '.join(etapes)}", ""]
    code = 0
    for et in etapes:
        print(f"== {et}")
        try:
            getattr(imp, et)()
        except RefusStudio as e:
            print(f"  REFUS {e.code} — {e.message}" + (f" — {json.dumps(e.details, ensure_ascii=False)[:400]}" if e.details else ""))
            print(f"  appel : {e.outil} {json.dumps(e.arguments, ensure_ascii=False)[:600]}")
            imp.note(f"- **REFUS** à l'étape `{et}` : `{e.code}` — {e.message}")
            code = 2 if e.code not in ("RESEAU", "HTTP_AUTH") else 3
            break
        if dry:
            imp.sauver_dry(et)
        else:
            nb = len(imp.appels); imp.appels = []
            print(f"  {nb} écritures")
            if not imp.controle(et):
                code = 1
                if not opts.get("enchainer"):
                    break
        if not opts.get("enchainer") and not dry and et != etapes[-1]:
            print("  point d'arrêt (relancer avec --enchainer pour continuer sans s'arrêter)")
            break
    if not dry:
        try:
            doc = imp.lire("doctor", {"show": SHOW_SLUG, "episode": EP_CODE})
            rapport.append("## doctor\n\n```\n" + json.dumps(doc, ensure_ascii=False, indent=1)[:6000] + "\n```\n")
        except RefusStudio as e:
            rapport.append(f"doctor : refus {e.code}")
    rapport += ["## Notes", ""] + imp.rapport
    RAPPORT.write_text("\n".join(rapport) + "\n", encoding="utf-8", newline="\n")
    print(f"rapport : {RAPPORT}")
    sys.exit(code)


def verify():
    st = Studio()
    story = st.appeler("read_story", {"show": SHOW_SLUG, "code": EP_CODE})
    plans = story.get("plans") or []
    local = {(n, o): t for n, o, _, _, t, _ in S.scenario_repliques()}
    ecarts = 0
    for p in plans:
        for l in p.get("repliques") or p.get("lines") or []:
            k = (p.get("number") or p.get("numero"), l.get("order") if l.get("order") is not None else l.get("ordre"))
            if local.get(k) != (l.get("text") or l.get("texte")):
                ecarts += 1; print("écart", k)
    c = st.appeler("counts", {"show": SHOW_SLUG, "code": EP_CODE})
    print(json.dumps(c, ensure_ascii=False, indent=1)[:1500])
    print(f"{len(plans)} plans relus, {ecarts} écarts de texte")
    sys.exit(1 if ecarts else 0)


if __name__ == "__main__":
    main()
