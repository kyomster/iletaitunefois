#!/usr/bin/env python3
"""Parseurs purs du dépôt vers des structures Python, pour l'import dans Studio.

Rien n'est complété de mémoire : chaque fonction rend ce que le document dit, et laisse nul ce qu'il ne dit pas.
`python studio_sources.py --verifier` imprime les comptages (plans, durée, répliques, mots, décors, locuteurs, règles)
et échoue si scénario et tableau révisé ne disent pas la même chose.

Sources lues (S01E01 des Découvreurs, série « Il était une fois ») :
  iletaitunefois/S01E01/scenario.md                 plans (#### Plan N — Titre · TYPE, Ns), texte dit, fiche par plan
  iletaitunefois/S01E01/plan-de-production.md       §3 roster des décors, §4 tableau révisé à huit colonnes (blocs)
  iletaitunefois/S01E01/son-et-voix.md              §1 locuteurs
  iletaitunefois/serie/BIBLE-Les-Decouvreurs.md     entrées de bible
  atelier/METHODE-generation-images.md              42 règles (## RÈGLE n, et les chapitres # N. qui portent les règles 3-9, 11-17)
  atelier/STRATEGIE-video.md §4                     9 règles vidéo
  atelier/moteurs-ecartes/VERDICTS.md               moteurs écartés
  iletaitunefois/S01E01/pilote/DECISIONS.md         décisions en vigueur et remplacées
  iletaitunefois/fiches_verifie/_audit/decouvreurs/S01E01_….audit.md   faits sourcés (tableau des corrections)
  styles/*/style.json                               via bibliotheque.charger_styles()
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))
from bibliotheque import charger_styles  # noqa: E402

RACINE = Path(__file__).resolve().parents[2]
EP = RACINE / "iletaitunefois" / "S01E01"
SERIE = RACINE / "iletaitunefois" / "serie"
SCENARIO = EP / "scenario.md"
PRODUCTION = EP / "plan-de-production.md"
SON = EP / "son-et-voix.md"
BIBLE = SERIE / "BIBLE-Les-Decouvreurs.md"
METHODE = RACINE / "atelier" / "METHODE-generation-images.md"
STRATEGIE = RACINE / "atelier" / "STRATEGIE-video.md"
VERDICTS = RACINE / "atelier" / "moteurs-ecartes" / "VERDICTS.md"
DECISIONS = EP / "pilote" / "DECISIONS.md"
AUDIT = RACINE / "iletaitunefois" / "fiches_verifie" / "_audit" / "decouvreurs" / "S01E01_nos-ancetres-les-chinois.audit.md"
FICHE = RACINE / "iletaitunefois" / "fiches_verifie" / "decouvreurs" / "S01E01_nos-ancetres-les-chinois.md"


def lire(p):
    return p.read_text(encoding="utf-8")


def rel(p):
    return p.resolve().relative_to(RACINE).as_posix()


def mots(texte):
    return len(texte.split())


# ---------------------------------------------------------------- scénario
RE_PLAN = re.compile(r"^#### Plan (\d+) — (.+?) · (FIXE|ANIMÉ|POST), (\d+) s\s*$", re.M)
RE_SEQ = re.compile(r"^### (.+?) — plans (\d+) à (\d+)\s*$", re.M)
RE_REPLIQUE = re.compile(r"([A-ZÉÈÀÂÇ'’0-9 ]+?)(?: \(([^)]*)\))? : « (.*?) »")


def scenario_plans():
    """{n: {titre, type_scenario, duree, texte_dit, fiche: {LIEU, CAMÉRA, CADRE, ACTION, RACCORDS, INTERDITS, …}, sequence}}"""
    t = lire(SCENARIO)
    heads = list(RE_PLAN.finditer(t))
    seqs = [(m.group(1), int(m.group(2)), int(m.group(3))) for m in RE_SEQ.finditer(t)]
    plans = {}
    for i, m in enumerate(heads):
        n = int(m.group(1))
        fin = heads[i + 1].start() if i + 1 < len(heads) else t.find("\n## ", m.end())
        corps = t[m.end():fin]
        td = re.search(r"\*\*Texte dit \(verrouillé\)\*\* : (.+)", corps)
        fiche = {}
        for ligne in corps.splitlines():
            mm = re.match(r"^([A-ZÉÈÀ0-9][A-ZÉÈÀ0-9 ]*?) · (.+)$", ligne.strip())
            if mm:
                fiche[mm.group(1)] = mm.group(2).strip()
        plans[n] = {"titre": m.group(2).strip(), "type_scenario": m.group(3), "duree": int(m.group(4)),
                    "texte_dit": td.group(1).strip() if td else "", "fiche": fiche,
                    "sequence": next((s[0] for s in seqs if s[1] <= n <= s[2]), None)}
    return plans


def repliques(texte_dit):
    """[(ordre, locuteur, didascalie, texte)] — un texte dit « — (muet…) » rend une liste vide."""
    if texte_dit.startswith("—") or not texte_dit:
        return []
    out = []
    for i, m in enumerate(RE_REPLIQUE.finditer(texte_dit)):
        out.append((i, m.group(1).strip(), (m.group(2) or "").strip() or None, m.group(3).strip()))
    return out


def scenario_repliques():
    """[(plan, ordre, locuteur, didascalie, texte, voix_off)]"""
    out = []
    for n, p in scenario_plans().items():
        for ordre, loc, did, txt in repliques(p["texte_dit"]):
            out.append((n, ordre, loc, did, txt, bool(did and "off" in did)))
    return out


def scenario_minutage():
    """[(sequence, plan_from, plan_to, timecode, chapitre)] depuis le tableau « Minutage récapitulatif »."""
    t = lire(SCENARIO)
    sec = t[t.find("## Minutage récapitulatif"):]
    out = []
    for ligne in sec.splitlines():
        m = re.match(r"^\| (.+?) \| (\d+)(?: à (\d+))? \| (.+?) \| (.+?) \|$", ligne)
        if m and not ligne.startswith("| Séquence"):
            out.append((m.group(1), int(m.group(2)), int(m.group(3) or m.group(2)), m.group(4), m.group(5)))
    return out


def scenario_registre_objets():
    """[(objet, plan_range)] depuis « Le registre des neuf objets »."""
    t = lire(SCENARIO)
    sec = t[t.find("### Le registre des neuf objets"):t.find("### Constantes de jeu")]
    return [(m.group(1).strip(), int(m.group(2))) for m in re.finditer(r"^\| (.+?) \| (\d+) \|$", sec, re.M) if m.group(1) != "Objet"]


# ---------------------------------------------------------------- plan de production
def production_tableau():
    """{n: {registre, type, blocs: [(code, duree, description, mouvement)], texte_dit}} depuis le §4 (8 colonnes)."""
    t = lire(PRODUCTION)
    sec = t[t.find("## 4. Tableau de plans révisé"):t.find("## 5. Prompts")]
    plans = {}
    for ligne in sec.splitlines():
        if not re.match(r"^\| \d+ \|", ligne):
            continue
        cells = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cells) != 8:
            raise ValueError(f"ligne du tableau à {len(cells)} colonnes : {ligne[:80]}")
        n, bloc, duree, registre, typ, desc, mouv, texte = cells
        n = int(n)
        p = plans.setdefault(n, {"registre": registre, "type": typ, "blocs": [], "texte_dit": ""})
        p["blocs"].append((bloc or None, int(duree), desc, mouv if mouv != "—" else None))
        if texte and texte not in ("—", "") and not p["texte_dit"]:
            p["texte_dit"] = texte
    return plans


def production_decors():
    """{code: {nom, plans: [n…], signalement}} depuis le roster §3 ; les plages « 7 à 15 » sont développées."""
    t = lire(PRODUCTION)
    sec = t[t.find("### Décors"):t.find("### Accessoires")]
    out = {}
    for m in re.finditer(r"^\| (D\d+) · (.+?) \| (.+?) \| (.+?) \|$", sec, re.M):
        plans = []
        for tok in m.group(3).split(","):
            tok = tok.strip().replace("(+ réemploi au", "").replace(")", "")
            r = re.match(r"^(\d+) à (\d+)$", tok)
            if r:
                plans += list(range(int(r.group(1)), int(r.group(2)) + 1))
            elif re.match(r"^\d+$", tok):
                plans.append(int(tok))
            else:
                plans += [int(x) for x in re.findall(r"\d+", tok)]
        out[m.group(1)] = {"nom": m.group(2).strip(), "plans": sorted(set(plans)), "signalement": m.group(4).strip()}
    return out


def plan_vers_decor():
    d = {}
    for code, v in production_decors().items():
        for n in v["plans"]:
            d.setdefault(n, []).append(code)
    return d


# ---------------------------------------------------------------- son et voix
def locuteurs():
    t = lire(SON)
    sec = t[t.find("## 1. Ce qu'il y a à dire"):t.find("## 2.")]
    out = []
    for m in re.finditer(r"^\| \*{0,2}([A-ZÉÈÀ'’ 0-9]+?)\*{0,2} \| ", sec, re.M):
        nom = m.group(1).strip()
        if nom not in ("Locuteur", "Total") and nom not in out:
            out.append(nom)
    return out


# ---------------------------------------------------------------- bible
def bible_entrees():
    """[(numero, titre, corps)] : une entrée par section ## de la bible de la série."""
    t = lire(BIBLE)
    heads = list(re.finditer(r"^## (\d+)\. (.+)$", t, re.M))
    out = []
    for i, m in enumerate(heads):
        fin = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        corps = t[m.end():fin].strip().strip("-").strip()
        out.append((int(m.group(1)), m.group(2).strip(), corps))
    return out


# ---------------------------------------------------------------- règles
RE_REGLE = re.compile(r"^## RÈGLE (\d+) — (.+)$", re.M)
RE_CHAP = re.compile(r"^# (\d+)\. (.+)$", re.M)
RE_DATE = re.compile(r"\((\d{1,2}) (août|juillet|septembre) (2026)\)")
MOIS = {"juillet": "07", "août": "08", "septembre": "09"}


def _date_iso(texte):
    m = RE_DATE.search(texte)
    if not m:
        return None
    return f"{m.group(3)}-{MOIS[m.group(2)]}-{int(m.group(1)):02d}"


def _preuve(corps):
    """Les phrases qui portent une mesure : « n sur m », « n images », « n styles », « n tirages », « n crédits »."""
    phrases = re.split(r"(?<=[.!?])\s+", corps)
    keep = [p for p in phrases if re.search(r"\b\d+\s*(sur|/|images?|styles?|tirages?|crédits?|clips?|planches?|plans?)\b", p)]
    return " ".join(keep).strip() or None


def methode_regles():
    """[{numero, titre, corps, evidence, date, source}] — les 42 règles : 28 explicites `## RÈGLE n`, et les chapitres
    `# N.` de 3 à 9 et 11 à 17 dont le titre EST la règle (numérotation historique de la méthode)."""
    t = lire(METHODE)
    heads = sorted([(m.start(), "regle", int(m.group(1)), m.group(2).strip(), m.end()) for m in RE_REGLE.finditer(t)] +
                   [(m.start(), "chap", int(m.group(1)), m.group(2).strip(), m.end()) for m in RE_CHAP.finditer(t)], key=lambda x: x[0])
    tous = list(re.finditer(r"^#{1,3} .+$", t, re.M))
    regles = {}
    date_chap = None
    for pos, genre, num, titre, end in heads:
        suivant = next((h.start() for h in tous if h.start() > pos and not h.group(0).startswith("### Corollaire")), len(t))
        corps = t[end:suivant].strip().rstrip("-").strip()
        if genre == "chap":
            date_chap = _date_iso(titre) or date_chap
            if num in (3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17):
                regles[num] = {"numero": num, "titre": titre, "corps": corps, "evidence": _preuve(corps), "date": date_chap or "2026-08-08",
                               "source": f"{rel(METHODE)}#{num}"}
        else:
            regles[num] = {"numero": num, "titre": titre, "corps": corps, "evidence": _preuve(corps), "date": _date_iso(titre) or date_chap or "2026-08-08",
                           "source": f"{rel(METHODE)}#RÈGLE-{num}"}
    return [regles[k] for k in sorted(regles)]


def strategie_regles():
    t = lire(STRATEGIE)
    sec = t[t.find("## 4. Les règles de prompt vidéo"):t.find("## 5.")]
    out = []
    for m in re.finditer(r"^(\d+)\. \*\*(.+?)\*\*[,.]? ?(.+)$", sec, re.M):
        out.append({"ordre": int(m.group(1)), "titre": m.group(2).strip(" ,.:"), "corps": m.group(3).strip().lstrip(" :,.").strip(), "source": f"{rel(STRATEGIE)}#4"})
    return out


NE_PAS_RETENTER = {"Wan 2.2 I2V A14B": True, "Wan 2.2 S2V": True, "InfiniteTalk / MultiTalk (MeiGen, sur Wan 2.1)": True,
                   "MiniMax H3": False, "LTX-2.3": True, "Modèles fermés par API Higgsfield": False}


def verdicts_moteurs():
    t = lire(VERDICTS)
    heads = list(re.finditer(r"^## (.+?)(?: — `(.+?)`| — pas de dossier)?\s*$", t, re.M))
    out = []
    for i, m in enumerate(heads):
        nom = m.group(1).strip()
        if nom == "Ce qui ne s'est pas fait":
            continue
        fin = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        corps = t[m.end():fin].strip().strip("-").strip()
        out.append({"moteur": nom, "dossier": m.group(2), "corps": corps, "doNotRetry": NE_PAS_RETENTER.get(nom, False),
                    "evidence": _preuve(corps), "source": rel(VERDICTS)})
    return out


def decisions():
    """[{date, titre, corps, statut: 'en vigueur'|'remplacée', remplacee_par, pourquoi}]"""
    t = lire(DECISIONS)
    vig = t[t.find("## En vigueur"):t.find("## Remplacées")]
    heads = list(re.finditer(r"^### (?:(\d{4}-\d{2}-\d{2}) — )?(.+)$", vig, re.M))
    out = []
    for i, m in enumerate(heads):
        fin = heads[i + 1].start() if i + 1 < len(heads) else len(vig)
        out.append({"date": m.group(1), "titre": re.sub(r"\*\*", "", m.group(2)).strip(), "corps": vig[m.end():fin].strip(), "statut": "en vigueur"})
    rem = t[t.find("## Remplacées"):]
    for ligne in rem.splitlines():
        mm = re.match(r"^\| (\d+ août) \| (.+?) \| (.+?) \| (.+?) \|$", ligne)
        if mm:
            out.append({"date": f"2026-08-{int(mm.group(1).split()[0]):02d}", "titre": re.sub(r"\*\*", "", mm.group(2)).strip(),
                        "corps": "", "statut": "remplacée", "remplacee_par": mm.group(3).strip(), "pourquoi": mm.group(4).strip()})
    return out


# ---------------------------------------------------------------- faits (audit du corpus)
STATUTS = {"✅": "confirme", "⚠️": "imprecis", "❌": "errone", "🕰️": "depasse", "❓": "non_tranche"}


def _sources(cell):
    """« Titre — URL ; Titre — URL » → [(titre, url)] ; un renvoi « *cf.* correction 22 » → []."""
    if "*cf.*" in cell and "http" not in cell:
        return []
    out = []
    for part in re.split(r"\s;\s", cell):
        m = re.match(r"^(.*?)\s*—\s*(https?://\S+)\s*$", part.strip())
        if m:
            out.append((m.group(1).strip(" *"), m.group(2).strip()))
        elif part.strip():
            out.append((part.strip(" *"), None))
    return out


def audit_faits():
    """[{numero, passe, section, enonce, statut, etat_2026, sources: [(titre, url)], confiance, renvoi}]"""
    t = lire(AUDIT)
    sec = t[t.find("## Corrections appliquées"):t.find("## Non tranché")]
    passe = 1
    out = []
    for ligne in sec.splitlines():
        if ligne.startswith("### Seconde passe"):
            passe = 2
        m = re.match(r"^\| (\d+) \| (.+?) \| (.+?) \| (\S+) \| (.+?) \| (.+?) \| (.+?) \|$", ligne)
        if not m:
            continue
        stat = STATUTS.get(m.group(4).strip(), m.group(4).strip())
        etat, src = m.group(5).strip(), m.group(6).strip()
        renvoi = re.findall(r"correction[s]? (\d+(?:(?:, | et )\d+)*)", etat) if "*cf.*" in etat else []
        out.append({"numero": int(m.group(1)), "passe": passe, "section": m.group(2).strip(), "enonce": m.group(3).strip(),
                    "statut": stat, "etat_2026": etat, "sources": _sources(src), "confiance": m.group(7).strip(), "renvoi": renvoi})
    return out


def fiche_dates_clefs():
    """[(libelle_date, evenement)] — texte libre, jamais analysé ici (les années se saisissent dans faits.json)."""
    t = lire(FICHE)
    sec = t[t.find("## Dates clefs"):t.find("## Gags")]
    return [(m.group(1).strip(), m.group(2).strip()) for m in re.finditer(r"^\| (.+?) \| (.+?) \|$", sec, re.M) if m.group(1) != "Date"]


# ---------------------------------------------------------------- vérification
def verifier():
    sp = scenario_plans()
    pt = production_tableau()
    reps = scenario_repliques()
    ecarts = []
    if set(sp) != set(pt):
        ecarts.append(f"plans : scénario {sorted(set(sp) - set(pt))} / tableau {sorted(set(pt) - set(sp))}")
    duree_s = sum(p["duree"] for p in sp.values())
    duree_t = sum(b[1] for p in pt.values() for b in p["blocs"])
    if duree_s != duree_t:
        ecarts.append(f"durée : scénario {duree_s} s / tableau {duree_t} s")
    for n in sorted(sp):
        if n in pt:
            ds = sp[n]["duree"]; dt = sum(b[1] for b in pt[n]["blocs"])
            if ds != dt:
                ecarts.append(f"plan {n} : {ds} s au scénario, {dt} s au tableau")
            if sp[n]["texte_dit"] != pt[n]["texte_dit"] and not (sp[n]["texte_dit"].startswith("—") and not pt[n]["texte_dit"]):
                ecarts.append(f"plan {n} : texte dit différent entre scénario et tableau")
    blocs_longs = [(n, b[0], b[1]) for n, p in pt.items() for b in p["blocs"] if p["type"] == "ANIMÉ" and b[1] > 10]
    if blocs_longs:
        ecarts.append(f"blocs ANIMÉ > 10 s : {blocs_longs}")
    anime = sum(b[1] for p in pt.values() if p["type"] == "ANIMÉ" for b in p["blocs"])
    nb_mots = sum(mots(r[4]) for r in reps)
    locs = sorted({r[2] for r in reps})
    decl = locuteurs()
    if set(locs) != set(decl):
        ecarts.append(f"locuteurs : scénario {sorted(set(locs) - set(decl))} / son-et-voix {sorted(set(decl) - set(locs))}")
    sans_decor = [n for n in sp if n not in plan_vers_decor()]
    multi = {n: c for n, c in plan_vers_decor().items() if len(c) > 1}
    regles = methode_regles()
    t14 = sum(sp[n]["duree"] for n in sp if n < 14)
    print(f"plans {len(sp)} · durée {duree_s} s ({duree_s // 60} min {duree_s % 60:02d}) · ANIMÉ {anime} s ({100 * anime / duree_s:.1f} %)")
    print(f"répliques {len(reps)} · mots {nb_mots} · débit {nb_mots / (duree_s / 60):.1f} mots/min · locuteurs {len(locs)}")
    print(f"lignes du tableau {sum(len(p['blocs']) for p in pt.values())} · décors {len(production_decors())} · plans sans décor {sans_decor} · plans à deux décors {multi}")
    print(f"objection d'Elio (plan 14) à {t14 // 60}:{t14 % 60:02d} · règles {len(regles)} ({[r['numero'] for r in regles if not r['evidence']]} sans preuve chiffrée)")
    print(f"faits de l'audit {len(audit_faits())} · décisions {len(decisions())} · styles {len(charger_styles())} · entrées de bible {len(bible_entrees())}")
    for e in ecarts:
        print("ÉCART :", e)
    return not ecarts


if __name__ == "__main__":
    if "--verifier" in sys.argv:
        sys.exit(0 if verifier() else 1)
    print(json.dumps({"plans": len(scenario_plans()), "repliques": len(scenario_repliques())}, ensure_ascii=False))
