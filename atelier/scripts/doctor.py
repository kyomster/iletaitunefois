#!/usr/bin/env python3
"""Les invariants de l'épisode, calculés sur la couche de données — ceux qui nous ont coûté cher.

  python doctor.py            imprime toutes les défaillances, triées par sévérité et rang ; sort 1 s'il y a un BLOQUANT
  python doctor.py --json     la même chose en JSON (lu par next.py et contexte.py)

Sévérités : BLOQUANT (on ne commit pas), ERREUR (à corriger avant de produire), ATTENTION (à savoir).
Chaque défaillance porte une adresse, un message et la réparation attendue.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import donnees as D  # noqa: E402

FORMAT = {"dureeMin": 1200, "dureeMax": 1320, "debitMin": 85, "debitMax": 95, "ratioAnimeMax": 0.40, "blocAnimeMaxSec": 10, "objectionElioAvantSec": 180,
          "gelsMin": 3, "gelsMax": 6, "gagsMin": 10, "gagsMax": 15, "refsMaxParPrompt": 7}
MOTS_BANNIS = ("enfant", "kid", "childlike")


def defaillance(sev, code, adresse, message, reparation, rang=5):
    return {"severite": sev, "code": code, "adresse": adresse, "message": message, "reparation": reparation, "rang": rang}


def controler():
    plans = D.lire("plans")["elements"]
    reps = D.lire("repliques")["elements"]
    idx_plan = {p["numero"]: p for p in plans}
    idx_rep = D.index(reps)
    out = []

    # ---- 1. comptages du format
    total = sum(p["duree"] for p in plans)
    mots = sum(D.mots(r["texte"]) for r in reps)
    debit = mots / (total / 60)
    if not FORMAT["dureeMin"] <= total <= FORMAT["dureeMax"]:
        out.append(defaillance("BLOQUANT", "EPISODE_HORS_DUREE", "S01E01", f"durée utile {total} s hors de {FORMAT['dureeMin']}–{FORMAT['dureeMax']}", "raccourcir ou allonger des plans (jamais un plan muet)", 1))
    if not FORMAT["debitMin"] <= debit <= FORMAT["debitMax"]:
        out.append(defaillance("ERREUR", "EPISODE_HORS_DEBIT", "S01E01", f"débit {debit:.1f} mots/min hors de {FORMAT['debitMin']}–{FORMAT['debitMax']}", "réécrire ou redistribuer le texte dit", 2))
    anime = sum(p["duree"] for p in plans if p["type"] == "ANIMÉ")
    if anime / total > FORMAT["ratioAnimeMax"]:
        out.append(defaillance("ERREUR", "RATIO_ANIME", "S01E01", f"ANIMÉ {100 * anime / total:.1f} % > {100 * FORMAT['ratioAnimeMax']:.0f} %", "basculer des plans en FIXE avec mouvement de caméra", 2))
    for p in plans:
        if p["type"] == "ANIMÉ":
            for b in p["blocs"]:
                if b["duree"] > FORMAT["blocAnimeMaxSec"]:
                    out.append(defaillance("BLOQUANT", "BLOC_TROP_LONG", p["adresse"], f"bloc {b['code'] or '—'} de {b['duree']} s > {FORMAT['blocAnimeMaxSec']} s", "découper le bloc", 1))
        if sum(b["duree"] for b in p["blocs"]) != p["duree"]:
            out.append(defaillance("BLOQUANT", "BLOCS_DUREE", p["adresse"], "la somme des blocs ne fait pas la durée du plan", "corriger les blocs ou la durée", 1))
        for cle, txt in p["fiche"]:
            # les mots bannis le sont dans ce qui deviendra un prompt (CADRE, ACTION, vignettes), pas dans les interdits ni les raccords
            if cle in ("RACCORDS", "INTERDITS", "HORS CADRE", "FABRICATION", None):
                continue
            for m in MOTS_BANNIS:
                if re.search(r"" + m + r"s?", txt, re.I):
                    out.append(defaillance("ATTENTION", "MOT_BANNI", p["adresse"], f"« {m} » dans {cle} : à remplacer par la stature et les proportions au moment d'écrire la brique", "réécrire la description ou la brique", 4))
    if plans[0]["type"] != "ANIMÉ":
        out.append(defaillance("ERREUR", "OUVERTURE_NON_ANIMEE", plans[0]["adresse"], "le premier plan n'est pas ANIMÉ", "premier plan toujours ANIMÉ", 2))
    t14 = sum(p["duree"] for p in plans if p["numero"] < 14)
    elio = [r for r in reps if r["locuteur"] == "ELIO"]
    premier_elio = min(elio, key=lambda r: (r["plan"], r["ordre"]))["plan"] if elio else None
    if premier_elio and sum(p["duree"] for p in plans if p["numero"] < premier_elio) > FORMAT["objectionElioAvantSec"]:
        out.append(defaillance("ERREUR", "OBJECTION_ELIO_TARDIVE", D.adresse_plan(premier_elio), "la première réplique d'Elio tombe après 3:00", "avancer l'objection", 2))
    numeros = [p["numero"] for p in plans]
    if numeros != list(range(1, len(plans) + 1)):
        out.append(defaillance("BLOQUANT", "NUMEROTATION", "S01E01", "les plans ne sont pas numérotés de 1 à n sans trou", "renuméroter", 1))

    # ---- 2. répliques : adresses, verrous, empreintes
    for r in reps:
        if r["plan"] not in idx_plan:
            out.append(defaillance("BLOQUANT", "REPLIQUE_SANS_PLAN", r["adresse"], "réplique rattachée à un plan inexistant", "corriger le plan", 1))
        if r.get("statut") in ("valide", "verrouille") and r.get("empreinte") != D.empreinte(r):
            out.append(defaillance("BLOQUANT", "VERROU_ROMPU", r["adresse"], "réplique verrouillée modifiée sans décision", "restaurer le texte, ou consigner une décision datée et re-valider", 1))
    for p in plans:
        if p.get("statut") in ("valide", "verrouille") and p.get("empreinte") != D.empreinte(p):
            out.append(defaillance("ERREUR", "PLAN_VALIDE_MODIFIE", p["adresse"], "plan validé modifié sans décision", "consigner une décision, re-valider", 2))

    # ---- 3. contrats de continuité
    c = D.lire("contrats")
    for pr in c["promesses"]:
        pay = pr.get("paiement")
        if pr["portee"] == "EPISODE" and not pay:
            out.append(defaillance("ERREUR", "PROMESSE_NON_PAYEE", f"promesse/{pr['key']}", f"« {pr['label']} » plantée au plan {pr['plantedPlan']} n'est jamais payée", "solder la promesse ou l'abandonner explicitement", 1))
        if pay and pay["plan"] <= pr["plantedPlan"]:
            out.append(defaillance("BLOQUANT", "PROMESSE_PAYEE_AVANT", f"promesse/{pr['key']}", "payée avant d'être plantée", "corriger les plans", 1))
        if pr["portee"] == "SERIE" and not pay:
            out.append(defaillance("ATTENTION", "TEASER_ATTEND_EPISODE", f"promesse/{pr['key']}", f"teaser planté au plan {pr['plantedPlan']} : paiement attendu au début de l'épisode suivant", "créer S01E02 et le payer", 7))
    for q in c["questions"]:
        if not q.get("reponse"):
            out.append(defaillance("BLOQUANT", "QUESTION_OUVERTURE_SANS_REPONSE", f"question/{q['key']}", "question posée dans l'ouverture froide sans réponse", "répondre dans l'épisode", 1))
        elif q["reponse"] <= q["askedPlan"]:
            out.append(defaillance("BLOQUANT", "QUESTION_REPONSE_AVANT", f"question/{q['key']}", "réponse avant la question", "corriger les plans", 1))
    beats = c["beats"]
    if not any(b["role"] == "OUVERTURE_FROIDE" for b in beats):
        out.append(defaillance("ERREUR", "PAS_D_OUVERTURE_FROIDE", "S01E01", "aucun beat d'ouverture froide", "déclarer le beat", 2))
    couverts = set()
    for b in beats:
        couverts |= set(range(b["planFrom"], b["planTo"] + 1))
    manquants = sorted(set(numeros) - couverts)
    if manquants:
        out.append(defaillance("ERREUR", "PLANS_HORS_BEAT", "S01E01", f"plans sans beat narratif : {manquants}", "étendre les beats", 3))
    # les objets sur la table : ce que chaque emploi exige contre ce que le registre donne
    rangé = {o["slug"]: o["range"] for o in c["objets"]}
    for u in c["emplois"]:
        n = u["plan"]
        restants = [s for s, rp in rangé.items() if rp > n]
        m = re.search(r"(\w+) objets", u["attendu"])
        NOMBRES = {"huit": 8, "sept": 7, "six": 6, "cinq": 5, "quatre": 4, "trois": 3, "deux": 2, "un": 1}
        if m and m.group(1).lower() in NOMBRES and NOMBRES[m.group(1).lower()] != len(restants) and "restent" in u["attendu"]:
            out.append(defaillance("ERREUR", "OBJETS_TABLE", D.adresse_plan(n), f"l'emploi dit « {u['attendu']} », le registre donne {len(restants)} objets restants", "corriger le plan ou le registre", 2))
        fiche = " ".join(t for _, t in idx_plan[n]["fiche"]) if n in idx_plan else ""
        mm = re.search(r"Table à (\w+) objets", fiche)
        if mm and mm.group(1).lower() in NOMBRES and NOMBRES[mm.group(1).lower()] != len(restants):
            out.append(defaillance("ERREUR", "OBJETS_TABLE", D.adresse_plan(n), f"la fiche dit « table à {mm.group(1)} objets », le registre donne {len(restants)}", "corriger la fiche du plan", 2))

    # ---- 4. faits et périodes
    faits = D.lire("faits")["elements"]
    persos = D.lire("personnages")["elements"]
    idx_fait = D.index(faits)
    par_plan = {}
    for f in faits:
        if f.get("statut") == "ecarte":
            for n in f.get("plans", []):
                out.append(defaillance("BLOQUANT", "FAIT_ECARTE_RATTACHE", D.adresse_plan(n), f"le fait écarté {f['adresse']} est rattaché au plan", "retirer le lien", 1))
        for n in f.get("plans", []):
            if f.get("periode"):
                par_plan.setdefault(n, []).append((f["adresse"], f["periode"]["debut"], f["periode"]["fin"]))
    for n, ps in par_plan.items():
        deb = max(p[1] for p in ps); fin = min(p[2] for p in ps)
        if deb > fin and len(ps) > 1:
            # un plan de montage ou une voix off compare des époques ; une saynète n'en a qu'une : à vérifier, pas à bloquer
            out.append(defaillance("ATTENTION", "PERIODES_MULTIPLES", D.adresse_plan(n), "plusieurs périodes citées : " + ", ".join(p[0] for p in ps), "si le plan est une saynète, un seul fait doit dater la scène (retirer les autres de `plans`)", 5))
    for pe in persos:
        if pe["nature"] == "HISTORIQUE":
            f = idx_fait.get(pe.get("fait") or "")
            if not f or not f.get("periode"):
                out.append(defaillance("ERREUR", "PERSONNAGE_SANS_PERIODE", pe["adresse"], "personnage historique sans fait daté", "rattacher un fait sourcé avec une période", 2))
    for f in faits:
        if not f.get("sources"):
            out.append(defaillance("ATTENTION", "FAIT_SANS_SOURCE", f["adresse"], "fait sans source", "sourcer ou écarter", 4))

    # ---- 5. continuité visuelle et assets
    cont = D.lire("continuite")["elements"]
    assets = D.lire("assets")["elements"]
    idx_asset = D.index(assets)
    for it in cont:
        if not it.get("planche"):
            out.append(defaillance("ERREUR" if it.get("statut") in ("valide", "verrouille") else "ATTENTION", "CONTINUITE_SANS_PLANCHE", it["adresse"], f"« {it['libelle']} » n'a pas de planche de référence (plans {it['plans'][:6]}{'…' if len(it['plans']) > 6 else ''})", "générer la planche et la rattacher", 3))
    for a in assets:
        for adr in a.get("lignes_citees", []):
            r = idx_rep.get(adr)
            if not r:
                out.append(defaillance("BLOQUANT", "ASSET_CITE_LIGNE_INCONNUE", a["adresse"], f"cite {adr} qui n'existe pas", "corriger l'asset", 1))
            elif a["empreintes_citees"].get(adr) != r.get("empreinte"):
                out.append(defaillance("ERREUR", "ASSET_PERIME", a["adresse"], f"la réplique {adr} a changé depuis le rendu", "re-rendre le clip", 2))
            elif r["texte"] not in a["prompt"]:
                out.append(defaillance("BLOQUANT", "PROMPT_NE_CITE_PAS", a["adresse"], f"le prompt ne cite pas {adr} à l'octet", "réécrire le prompt avec la réplique entre guillemets", 1))
        for radr in a.get("references", []):
            if radr not in idx_asset:
                out.append(defaillance("ERREUR", "REFERENCE_INCONNUE", a["adresse"], f"référence {radr} absente", "déclarer l'asset", 3))
        if len(a.get("references", [])) > FORMAT["refsMaxParPrompt"]:
            out.append(defaillance("ERREUR", "TROP_DE_REFERENCES", a["adresse"], "> 7 références", "réduire", 3))
        if a.get("statut") in ("valide", "verrouille") and a.get("empreinte") != D.empreinte(a):
            out.append(defaillance("ERREUR", "ASSET_VALIDE_MODIFIE", a["adresse"], "asset validé modifié sans décision", "consigner une décision", 2))

    # ---- 6. ce qui attend Guillaume
    proposes = [x["adresse"] for coll in ("plans", "repliques", "faits", "personnages", "continuite", "assets", "decisions") for x in D.lire(coll)["elements"] if x.get("statut") == "propose"]
    if proposes:
        out.append(defaillance("ATTENTION", "EN_ATTENTE_DE_VALIDATION", "S01E01", f"{len(proposes)} objets « propose » attendent le mot de Guillaume (ex. {', '.join(proposes[:4])})", "valider ou écarter (donnees.valider)", 6))
    return sorted(out, key=lambda d: ({"BLOQUANT": 0, "ERREUR": 1, "ATTENTION": 2}[d["severite"]], d["rang"], d["adresse"]))


def main():
    out = controler()
    if "--json" in sys.argv:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        for d in out:
            print(f"{d['severite']:9} {d['code']:30} {d['adresse']:34} {d['message']}\n{'':9} → {d['reparation']}")
        nb = {s: sum(1 for d in out if d["severite"] == s) for s in ("BLOQUANT", "ERREUR", "ATTENTION")}
        print(f"\n{nb['BLOQUANT']} bloquant, {nb['ERREUR']} erreur, {nb['ATTENTION']} attention")
    sys.exit(1 if any(d["severite"] == "BLOQUANT" for d in out) else 0)


if __name__ == "__main__":
    main()
