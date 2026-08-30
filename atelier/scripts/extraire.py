#!/usr/bin/env python3
"""Extraction UNIQUE (30 août 2026) des markdown de S01E01 vers la couche de données.

Après cette extraction, les markdown sont générés par rendre.py et ne s'éditent plus. Le script reste dans le
dépôt comme trace de ce qui a été extrait d'où ; il ne doit plus être relancé sur des fichiers générés.

Ce qu'il produit :
  scenario.json     les blocs du scénario (texte verbatim, séquences, plans, minutage), dans l'ordre
  plans.json        un objet par plan (durée, types, registre, blocs, décor, fiche ligne à ligne)
  repliques.json    une réplique par ligne, adressée, avec son verrou
  decors.json       le roster des décors + les époques saisies (lieux.json)
  production.json   les blocs de plan-de-production.md (texte verbatim, roster, tableau révisé)
  son.json          les blocs de son-et-voix.md (texte verbatim, tableau des locuteurs)
  faits.json, personnages.json, continuite.json, assets.json, contrats.json, attendus.json, decisions.json
  atelier/regles/regles.json
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import donnees as D  # noqa: E402
import studio_sources as S  # noqa: E402
from bibliotheque import charger_briques, charger_styles  # noqa: E402

VALIDE_SCENARIO = "2026-08-22"   # les 79 plans d'origine, arbitrés par Guillaume ; la révision du 29 août est « propose »
PLANS_REVISES = {24, 25, 35, 48}
STUDIO = S.EP / "studio"


# ---------------------------------------------------------------- scénario
def extraire_scenario():
    t = S.lire(S.SCENARIO)
    lignes = t.split("\n")
    blocs, plans, repliques = [], [], []
    texte = []
    seqs = []
    i = 0
    while i < len(lignes):
        l = lignes[i]
        m_seq = re.match(r"^### (.+?) — plans (\d+) à (\d+)$", l)
        m_plan = re.match(r"^#### Plan (\d+) — (.+?) · (FIXE|ANIMÉ|POST), (\d+) s$", l)
        if l == "## Minutage récapitulatif":
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            j = i + 1
            chapitres = {}
            while not lignes[j].startswith("**Total :"):
                mm = re.match(r"^\| (.+?) \| (\d+) à (\d+) \| (.+?) \| (.+?) \|$", lignes[j])
                if mm:
                    chapitres[int(mm.group(2))] = (mm.group(1), mm.group(5))
                j += 1
            for s in seqs:
                s["libelle"], s["chapitre"] = chapitres.get(s["de"], (s["titre"], ""))
            blocs.append({"type": "minutage"})
            i = j + 1
            continue
        if m_seq:
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            seq = {"type": "sequence", "titre": m_seq.group(1), "de": int(m_seq.group(2)), "a": int(m_seq.group(3))}
            seqs.append(seq); blocs.append(seq)
            i += 2 if i + 1 < len(lignes) and lignes[i + 1] == "" else 1   # la ligne vide sous le titre appartient au bloc
            continue
        if m_plan:
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            n = int(m_plan.group(1))
            j = i + 1
            corps = []
            while j < len(lignes) and not re.match(r"^#{2,4} ", lignes[j]):
                corps.append(lignes[j]); j += 1
            # le corps : "", texte dit, "", fiche…, "" ; un séparateur « --- » final appartient au texte suivant
            while corps and corps[-1] == "": corps.pop()
            suite = None
            if corps and corps[-1] == "---":
                corps.pop(); suite = "---"
                while corps and corps[-1] == "": corps.pop()
            assert corps[0] == "" and corps[1].startswith("**Texte dit (verrouillé)** : ") and corps[2] == "", (n, corps[:3])
            td = corps[1][len("**Texte dit (verrouillé)** : "):]
            fiche = [[m.group(1), m.group(2)] if (m := re.match(r"^([A-ZÉÈÀ0-9][A-ZÉÈÀ0-9 ]*?) · (.+)$", c)) else [None, c] for c in corps[3:]]
            plan = {"adresse": D.adresse_plan(n), "numero": n, "titre": m_plan.group(2), "type_scenario": m_plan.group(3), "duree": int(m_plan.group(4)),
                    "sequence": next((s["titre"] for s in seqs if s["de"] <= n <= s["a"]), None), "fiche": fiche}
            reps = S.repliques(td)
            if not reps:
                plan["muet"] = td
            for o, loc, did, txt in reps:
                r = {"adresse": D.adresse_ligne(n, o), "plan": n, "ordre": o, "locuteur": loc, "didascalie": did, "voix_off": bool(did and "off" in did), "texte": txt}
                if n in PLANS_REVISES:
                    r.update({"statut": "propose", "_note": "révision du 29 août 2026, en attente de la signature de Guillaume"})
                else:
                    D.valider(r, quand=VALIDE_SCENARIO, statut="verrouille")
                r["empreinte"] = D.empreinte(r)
                repliques.append(r)
            plans.append(plan)
            blocs.append({"type": "plan", "numero": n})
            if suite:
                texte = [suite, ""]
                # le « --- » est suivi d'une ligne vide puis du prochain titre : on garde "---\n" comme texte
                texte = ["---", ""]
            i = j
            continue
        texte.append(l)
        i += 1
    if texte:
        blocs.append({"type": "texte", "md": "\n".join(texte)})
    # placeholders dans le texte verbatim
    for b in blocs:
        if b["type"] == "texte":
            b["md"] = b["md"].replace("## Découpage détaillé — les 79 plans", "## Découpage détaillé — les {{nb_plans}} plans")
            b["md"] = re.sub(r"\*\*Durée utile : \d+ min \d+ s hors générique\.\*\*", "**Durée utile : {{duree_utile}} hors générique.**", b["md"])
    return {"blocs": blocs}, plans, repliques


# ---------------------------------------------------------------- plan de production
def extraire_production(plans):
    t = S.lire(S.PRODUCTION)
    pt = S.production_tableau()
    for p in plans:
        n = p["numero"]; q = pt[n]
        p["type"] = q["type"]; p["registre"] = q["registre"]
        p["blocs"] = [{"code": b[0], "duree": b[1], "description": b[2], "mouvement": b[3]} for b in q["blocs"]]
        # colonne « Texte dit » du tableau : première ligne du plan = texte dit ou libellé muet ; lignes suivantes = « — »
        sec = t[t.find("## 4. Tableau de plans révisé"):t.find("## 5. Prompts")]
        rows = [l for l in sec.splitlines() if re.match(rf"^\| {n} \|", l)]
        cells = [c.strip() for c in rows[0].strip().strip("|").split("|")]
        p["muet_tableau"] = cells[7] if not [r for r in S.scenario_repliques() if r[0] == n] else None
        p["suite_tableau"] = [[c.strip() for c in r.strip().strip("|").split("|")][7] for r in rows[1:]]
        assert sum(b["duree"] for b in p["blocs"]) == p["duree"], n
    # blocs du document : texte verbatim / roster des décors / tableau
    lignes = t.split("\n")
    blocs, texte = [], []
    i = 0
    while i < len(lignes):
        l = lignes[i]
        if l == "| Décor | Plans | Signalement |":
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            j = i + 2
            while j < len(lignes) and lignes[j].startswith("| D"): j += 1
            blocs.append({"type": "decors"}); i = j; continue
        if l == "| N° | Bloc | Durée (s) | Registre | Type | Description visuelle | Mouvement caméra | Texte dit |":
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            j = i + 2
            while j < len(lignes) and re.match(r"^\| \d+ \|", lignes[j]): j += 1
            blocs.append({"type": "tableau"}); i = j; continue
        texte.append(l); i += 1
    if texte: blocs.append({"type": "texte", "md": "\n".join(texte)})
    return {"blocs": blocs}


def extraire_decors():
    lieux = json.loads((STUDIO / "lieux.json").read_text(encoding="utf-8"))
    out = []
    t = S.lire(S.PRODUCTION)
    brut = {m.group(1): m.group(2) for m in re.finditer(r"^\| (D\d+) · .+? \| (.+?) \| .+? \|$", t[t.find("### Décors"):t.find("### Accessoires")], re.M)}
    for code, d in S.production_decors().items():
        o = {"adresse": f"decor/{code}", "code": code, "nom": d["nom"], "plans": d["plans"], "plans_texte": brut.get(code), "signalement": d["signalement"], "statut": "valide", "valide_le": VALIDE_SCENARIO}
        sur = lieux["surcharges"].get(code)
        if sur:
            o["epoque"] = {k: sur[k] for k in ("eraDebutAnnee", "eraFinAnnee", "eraPrecision")}; o["epoque_source"] = sur["source"]
        if code in lieux.get("aValider", {}):
            o["epoque_a_saisir"] = lieux["aValider"][code]
        o["empreinte"] = D.empreinte(o)
        out.append(o)
    return {"plan_decor": lieux["plan_decor"], "elements": out}


# ---------------------------------------------------------------- son et voix
def extraire_son():
    t = S.lire(S.SON)
    lignes = t.split("\n")
    blocs, texte, i = [], [], 0
    while i < len(lignes):
        l = lignes[i]
        if l == "| Locuteur | Répliques | Mots | Part | Plans |":
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            j = i + 2
            while j < len(lignes) and lignes[j].startswith("|"): j += 1
            blocs.append({"type": "locuteurs"}); i = j; continue
        if l.startswith("2 031 mots entre guillemets"):
            blocs.append({"type": "texte", "md": "\n".join(texte)}) if texte else None; texte = []
            blocs.append({"type": "comptage"}); i += 1; continue
        if l.startswith("**33 plans font dialoguer"):
            if texte: blocs.append({"type": "texte", "md": "\n".join(texte)}); texte = []
            blocs.append({"type": "dialogues", "suite": l[l.find(". Didascalies"):]}); i += 1; continue
        texte.append(l); i += 1
    if texte: blocs.append({"type": "texte", "md": "\n".join(texte)})
    return {"blocs": blocs}


# ---------------------------------------------------------------- le reste, depuis les saisies et les documents
def extraire_faits():
    cfg = json.loads((STUDIO / "faits.json").read_text(encoding="utf-8"))
    out = []
    for f in S.audit_faits():
        cle = f"{f['passe']}.{f['numero']}"
        if cle in cfg["exclus"] or not f["sources"]:
            continue
        per = cfg["periodes"].get(cle)
        o = {"adresse": f"fait/{cle}", "cle": cle, "section_audit": f["section"], "enonce_episode": f["enonce"], "etat_2026": f["etat_2026"],
             "statut_audit": f["statut"], "confiance": f["confiance"], "sources": [{"titre": a, "url": b} for a, b in f["sources"]],
             "periode": per, "plans": cfg["plans"].get(cle, []),
             "statut": "ecarte" if False else "valide", "valide_par": "audit du corpus (4-7 août 2026)", "valide_le": "2026-08-07",
             "source": "iletaitunefois/fiches_verifie/_audit/decouvreurs/S01E01_nos-ancetres-les-chinois.audit.md"}
        o["empreinte"] = D.empreinte(o)
        out.append(o)
    out.append({"adresse": "fait/lenormand-1783", "cle": "lenormand-1783", "section_audit": "Faits énoncés (extrait de 2.52)",
                "enonce_episode": "« c'est De Vinci qui le premier pensa au parachute »",
                "etat_2026": "Louis-Sébastien Lenormand effectue le premier saut public attesté en parachute en 1783, à Montpellier, et forge le mot « parachute » en 1785 ; l'apport propre de Garnerin, le 22 octobre 1797, est la voilure de soie sans armature.",
                "statut_audit": "imprecis", "confiance": "haute", "sources": [{"titre": "Wikipedia EN, Parachute", "url": "https://en.wikipedia.org/wiki/Parachute"}],
                "periode": {"debut": 1783, "fin": 1785, "precision": "ANNEE", "libelle": "1783, mot forgé en 1785"}, "plans": [60],
                "statut": "propose", "_note": "saisi le 30 août 2026 pour dater le personnage Lenormand", "source": "fiche vérifiée S01E01, ligne 117"})
    out[-1]["empreinte"] = D.empreinte(out[-1])
    return {"exclus": cfg["exclus"], "elements": out}


def extraire_personnages():
    d = json.load(open(STUDIO / "dry-run" / "prod-personnages.json", encoding="utf-8"))
    out = []
    sp = S.scenario_repliques()
    for x in d:
        if x["outil"] != "upsert_character":
            continue
        a = x["args"]
        slug = re.sub(r"[^a-z0-9]+", "-", a["name"].lower().replace("é", "e").replace("è", "e").replace("ï", "i").replace("'", "-")).strip("-")
        o = {"adresse": f"perso/{slug}", "nom": a["name"], "portee": a["scope"], "nature": a["nature"], "recurrent": a.get("recurring", False),
             "age": a.get("ageLabel"), "couleur_reservee": a.get("reservedColor"), "totem": a.get("totem"), "fiche_canon": a.get("canonSheet") or {},
             "fait": None, "plans": [], "locuteurs": [], "source": a.get("sourceRef", "").split("@")[0]}
        out.append(o)
    liens = [x["args"] for x in d if x["outil"] == "link_plan_character"]
    locs = [x["args"] for x in d if x["outil"] == "upsert_speaker"]
    # les liens portaient « <id> » en dry-run : on les reconstruit par le même ordre de création
    ordre = [o for o in out]
    FAITS = {"Garnerin": "1.16", "Yuan Huangtou": "1.13", "Moine Huaibing": "1.44", "Lenormand": "lenormand-1783", "Shun": "1.15", "Empereur Gao Yang": "1.13"}
    LOC = {"Sam": ["SAM"], "Naya": ["NAYA"], "Elio": ["ELIO"], "Garnerin": ["GARNERIN"], "L'aide de Garnerin": ["L'AIDE"], "Le badaud rond": ["BADAUD 1"], "Le badaud maigre": ["BADAUD 2"],
           "Fermiers au semoir": ["PAYSAN 1", "PAYSAN 2"], "Pillards": ["PILLARD 1", "PILLARD 2"], "Badauds du pont": ["LE BADAUD", "L'AUTRE"],
           "La sentinelle et le général": ["LA SENTINELLE", "LE GÉNÉRAL"], "Compères faux-monnayeurs": ["COMPÈRE 1"]}
    PLANS = {"Garnerin": [3, 4, 5, 61, 63], "L'aide de Garnerin": [3], "Le badaud rond": [2, 64], "Le badaud maigre": [2, 64], "Foule Directoire": [1, 2, 4, 63, 64],
             "Yuan Huangtou": [44, 45, 47], "Fermiers au semoir": [21, 22], "Pillards": [56, 57], "Porteurs du pont": [50, 51], "Badauds du pont": [51], "Moine Huaibing": [39],
             "Lenormand": [60], "Alchimistes taoïstes": [71], "Charretier Han": [29], "Shun": [55], "La sentinelle et le général": [67], "Compères faux-monnayeurs": [68],
             "Empereur Gao Yang": [44], "Cavaliers antiques sans étrier": [30], "Cavaliers avars": [32], "Passants de Ye": [46]}
    for o in out:
        o["fait"] = f"fait/{FAITS[o['nom']]}" if o["nom"] in FAITS else None
        o["locuteurs"] = LOC.get(o["nom"], [])
        o["plans"] = PLANS.get(o["nom"]) or sorted({r[0] for r in sp if r[2] in o["locuteurs"]})
        o["statut"] = "valide" if o["nom"] in ("Sam", "Naya", "Elio", "Garnerin", "Le badaud rond", "Le badaud maigre", "Foule Directoire", "L'aide de Garnerin") else "propose"
        if o["statut"] == "valide":
            o["valide_par"] = "Guillaume"; o["valide_le"] = "2026-08-27"
        o["empreinte"] = D.empreinte(o)
    return {"elements": out}


def extraire_continuite():
    d = json.load(open(STUDIO / "dry-run" / "prod-continuite.json", encoding="utf-8"))
    out = []
    for x in d:
        a = x["args"]
        planche = {"ballon": "asset/Ballon", "nacelle": "asset/Nacelle"}.get(a["key"])
        statut = "valide" if planche else "propose"
        o = {"adresse": f"continuite/{a['key']}", "cle": a["key"], "libelle": a["label"], "genre": a["kind"], "plans": a["planNumbers"], "planche": planche,
             "description_canonique": "iletaitunefois/S01E01/prompts/assets-et-objets.md §7", "note": a["note"].split(" — ")[0], "statut": statut}
        if planche:
            o["valide_par"] = "Guillaume"; o["valide_le"] = "2026-08-26"
        o["empreinte"] = D.empreinte(o)
        out.append(o)
    return {"elements": out}


def extraire_assets(repliques):
    d = json.load(open(STUDIO / "dry-run" / "prod-assets.json", encoding="utf-8"))
    idx = D.index(repliques)
    Bq = charger_briques(S.EP / "prompts" / "briques_pilote.py")
    clips = {j["clip"]: j for j in json.loads((S.EP / "prompts" / "clips-StyleP.json").read_text(encoding="utf-8"))}
    media = json.loads(Path(r"C:/Users/kyoms/Downloads/EpisodeModernise/pilote/_media_ids.json").read_text(encoding="utf-8"))
    out = []
    for x in d:
        if x["outil"] != "upsert_asset":
            continue
        a = x["args"]
        slug = a["slug"]
        o = {"adresse": f"asset/{slug}", "slug": slug, "genre": a["kind"], "style": a["styleCode"], "moteur": a["engineCode"], "prompt": a["promptPos"], "negatif": a.get("promptNeg"),
             "plans": a.get("plans", []), "references": [], "lignes_citees": [], "empreintes_citees": {}, "fichier": None, "media_id_higgsfield": None, "graine": None, "longueur": None,
             "statut": "valide", "valide_par": "Guillaume", "valide_le": "2026-08-27"}
        if a["kind"] == "REFERENCE":
            o["fichier"] = f"iletaitunefois/S01E01/assets/references/{slug}_StyleP.png"; o["media_id_higgsfield"] = media.get(f"{slug}_StyleP.png")
        elif a["kind"] == "IMAGE_CLE":
            o["fichier"] = f"iletaitunefois/S01E01/assets/cles/{slug}_StyleP.png"; o["references"] = [f"asset/{r}" for r in Bq.REFS.get(slug, [])]
            if not (S.RACINE / o["fichier"]).exists():
                o["fichier"] = None; o["statut"] = "propose"; o.pop("valide_par", None); o.pop("valide_le", None); o["_note"] = "clé de réserve (champ-contrechamp), jamais générée en P"
        else:
            clip = slug[len("clip-"):]
            j = clips[clip]
            o.update({"fichier": f"Downloads/EpisodeModernise/pilote/clips-runpod/StyleP/{clip}_StyleP.mp4 (hors dépôt)", "graine": j["seed"], "longueur": j["length"], "references": [f"asset/{clip}"]})
            o["lignes_citees"] = [D.adresse_ligne(*map(int, x.split("#"))) if "#" in x else x for x in a.get("lignes", [])]
        for adr in o["lignes_citees"]:
            o["empreintes_citees"][adr] = idx[adr]["empreinte"]
        o["empreinte"] = D.empreinte(o)
        out.append(o)
    return {"elements": out}


def extraire_regles():
    out = []
    for r in S.methode_regles():
        out.append({"adresse": f"regle/{r['numero']}", "numero": r["numero"], "domaine": "IMAGE", "titre": r["titre"], "corps": r["corps"], "preuve": r["evidence"], "date": r["date"],
                    "source": r["source"], "statut": "valide", "valide_par": "pilote S01E01", "valide_le": r["date"]})
    for r in S.strategie_regles():
        out.append({"adresse": f"regle/video-{r['ordre']}", "numero": None, "domaine": "VIDEO", "titre": r["titre"], "corps": r["corps"], "preuve": None, "date": "2026-08-27",
                    "source": r["source"], "statut": "valide", "valide_par": "pilote S01E01", "valide_le": "2026-08-27"})
    for v in S.verdicts_moteurs():
        slug = re.sub(r"[^a-z0-9]+", "-", v["moteur"].lower()).strip("-")
        out.append({"adresse": f"moteur/{slug}", "numero": None, "domaine": "MOTEUR", "titre": v["moteur"], "corps": v["corps"], "preuve": v["evidence"], "date": "2026-08-24",
                    "ne_pas_retenter": v["doNotRetry"], "source": v["source"], "statut": "ecarte" if v["doNotRetry"] else "valide", "valide_par": "Guillaume", "valide_le": "2026-08-24"})
    for o in out:
        o["empreinte"] = D.empreinte(o)
    return {"elements": out}


def extraire_decisions():
    out = []
    for d in S.decisions():
        slug = re.sub(r"[^a-z0-9]+", "-", (d["date"] or "sans-date") + "-" + d["titre"].lower()[:50]).strip("-")
        o = {"adresse": f"decision/{slug}", "date": d["date"], "titre": d["titre"], "corps": d["corps"], "statut_decision": d["statut"],
             "remplacee_par": d.get("remplacee_par"), "pourquoi": d.get("pourquoi"), "par": "Guillaume" if "Guillaume" in d["corps"] or d["date"] == "2026-08-29" else "pilote S01E01",
             "a_enteriner": "entériner" in d["corps"].lower(), "statut": "valide" if "entériner" not in d["corps"].lower() else "propose", "source": "iletaitunefois/S01E01/pilote/DECISIONS.md"}
        o["empreinte"] = D.empreinte(o)
        out.append(o)
    return {"elements": out}


def main():
    scen, plans, repliques = extraire_scenario()
    production = extraire_production(plans)
    for p in plans:
        if p["numero"] in PLANS_REVISES:
            p["statut"] = "propose"; p["_note"] = "révision du 29 août 2026, en attente de la signature de Guillaume"
        else:
            D.valider(p, quand=VALIDE_SCENARIO)
        p["empreinte"] = D.empreinte(p)
    D.ecrire("scenario", scen)
    D.ecrire("plans", {"episode": {"code": D.EP_CODE, "titre": "Nos ancêtres les Chinois", "saison": 1, "programme": "Il était une fois", "gabarit": "B"}, "elements": plans})
    D.ecrire("repliques", {"elements": repliques})
    D.ecrire("decors", extraire_decors())
    D.ecrire("production", production)
    D.ecrire("son", extraire_son())
    D.ecrire("faits", extraire_faits())
    D.ecrire("personnages", extraire_personnages())
    D.ecrire("continuite", extraire_continuite())
    D.ecrire("assets", extraire_assets(repliques))
    c = json.loads((STUDIO / "contrats.json").read_text(encoding="utf-8")); D.ecrire("contrats", c)
    a = json.loads((STUDIO / "attendus.json").read_text(encoding="utf-8")); D.ecrire("attendus", a)
    D.ecrire("decisions", extraire_decisions())
    D.REGLES.parent.mkdir(parents=True, exist_ok=True)
    D.ecrire(str(D.REGLES), extraire_regles())
    print(f"scénario : {len(scen['blocs'])} blocs, {len(plans)} plans, {len(repliques)} répliques ; production : {len(production['blocs'])} blocs")


if __name__ == "__main__":
    main()
