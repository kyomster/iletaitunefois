#!/usr/bin/env python3
"""Génère les documents lisibles depuis la couche de données. On n'édite jamais ces documents à la main.

  python rendre.py            écrit scenario.md, plan-de-production.md, son-et-voix.md
  python rendre.py --check    ne réécrit rien ; sort 1 si un document diffère de ce que les données donnent
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import donnees as D  # noqa: E402

CIBLES = {"scenario": D.EP / "scenario.md", "production": D.EP / "plan-de-production.md", "son": D.EP / "son-et-voix.md"}


def duree_txt(s):
    return f"{s // 60}:{s % 60:02d}"


def rendre_scenario(plans, reps):
    scen = D.lire("scenario")
    idx = {p["numero"]: p for p in plans}
    total = sum(p["duree"] for p in plans)
    out = []
    for b in scen["blocs"]:
        if b["type"] == "texte":
            out.append(b["md"].replace("{{nb_plans}}", str(len(plans))).replace("{{duree_utile}}", f"{total // 60} min {total % 60:02d} s"))
        elif b["type"] == "sequence":
            out.append(f"### {b['titre']} — plans {b['de']} à {b['a']}\n")
        elif b["type"] == "plan":
            p = idx[b["numero"]]
            lignes = [f"#### Plan {p['numero']} — {p['titre']} · {p['type_scenario']}, {p['duree']} s", "",
                      f"**Texte dit (verrouillé)** : {D.texte_dit(p, reps)}", ""]
            lignes += [f"{k} · {v}" if k else v for k, v in p["fiche"]]
            lignes.append("")
            out.append("\n".join(lignes))
        elif b["type"] == "minutage":
            seqs = [x for x in scen["blocs"] if x["type"] == "sequence"]
            lignes = ["## Minutage récapitulatif", "", "| Séquence | Plans | Timecode | Chapitre |", "|---|---|---|---|"]
            t = 0
            for s in seqs:
                d = sum(idx[n]["duree"] for n in range(s["de"], s["a"] + 1))
                lignes.append(f"| {s.get('libelle') or s['titre']} | {s['de']} à {s['a']} | {duree_txt(t)} à {duree_txt(t + d)} | {s['chapitre']} |")
                t += d
            lignes += ["", f"**Total : {len(plans)} plans, {total // 1000} {total % 1000:03d} secondes soit {total // 60} min {total % 60:02d} s hors générique.**"]
            out.append("\n".join(lignes))
    return "\n".join(out) + ("\n" if not out[-1].endswith("\n") else "")


def rendre_production(plans, reps):
    prod = D.lire("production")
    decors = D.lire("decors")["elements"]
    out = []
    for b in prod["blocs"]:
        if b["type"] == "texte":
            out.append(b["md"])
        elif b["type"] == "decors":
            lignes = ["| Décor | Plans | Signalement |", "|---|---|---|"]
            for d in decors:
                lignes.append(f"| {d['code']} · {d['nom']} | {d.get('plans_texte') or plages(d['plans'])} | {d['signalement']} |")
            out.append("\n".join(lignes))
        elif b["type"] == "tableau":
            lignes = ["| N° | Bloc | Durée (s) | Registre | Type | Description visuelle | Mouvement caméra | Texte dit |", "|---|---|---|---|---|---|---|---|"]
            for p in plans:
                mine = [l for l in reps if l["plan"] == p["numero"]]
                premier = D.texte_dit(p, reps) if mine else (p.get("muet_tableau") or "—")
                for i, bl in enumerate(p["blocs"]):
                    td = premier if i == 0 else (p.get("suite_tableau") or ["—"] * 9)[i - 1]
                    lignes.append(f"| {p['numero']} | {bl['code'] or ''} | {bl['duree']} | {p['registre']} | {p['type']} | {bl['description']} | {bl['mouvement'] or '—'} | {td} |")
            out.append("\n".join(lignes))
    return "\n".join(out)


def plages(plans):
    """[7,8,…,15,18] → « 7 à 15, 18 » ; les décors D2 gardent leur mention libre dans `signalement`."""
    if not plans:
        return ""
    groupes, debut, prec = [], plans[0], plans[0]
    for n in plans[1:] + [None]:
        if n is not None and n == prec + 1:
            prec = n; continue
        groupes.append(f"{debut} à {prec}" if prec - debut >= 2 else (f"{debut}, {prec}" if prec != debut else str(debut)))
        if n is not None:
            debut = prec = n
    return ", ".join(groupes)


def rendre_son(plans, reps):
    son = D.lire("son")
    total = sum(p["duree"] for p in plans)
    par = {}
    for r in reps:
        d = par.setdefault(r["locuteur"], {"rep": 0, "off": 0, "mots": 0, "car": 0, "plans": []})
        d["rep"] += 1; d["off"] += r["voix_off"]; d["mots"] += D.mots(r["texte"]); d["car"] += len(r["texte"])
        if r["plan"] not in d["plans"]: d["plans"].append(r["plan"])
    tot_m = sum(d["mots"] for d in par.values()); tot_c = sum(d["car"] for d in par.values())
    out = []
    for b in son["blocs"]:
        if b["type"] == "texte":
            out.append(b["md"])
        elif b["type"] == "comptage":
            out.append(f"{tot_m // 1000} {tot_m % 1000:03d} mots entre guillemets, tous attribués (comptage par blancs) ; environ {round(tot_c, -2) // 1000} {round(tot_c, -2) % 1000:03d} caractères ; débit moyen {tot_m / (total / 60):.1f} mots par minute, dans la fourchette 85 à 95 de la méthode.".replace(".", ",", 0))
        elif b["type"] == "locuteurs":
            lignes = ["| Locuteur | Répliques | Mots | Part | Plans |", "|---|---|---|---|---|"]
            for k in sorted(par, key=lambda k: -par[k]["mots"]):
                d = par[k]; nom = f"**{k}**" if k in ("SAM", "ELIO", "NAYA") else k
                rep = f"{d['rep']}, dont **{d['off']} en voix off**" if d["off"] else str(d["rep"])
                pl = f"{len(d['plans'])} plans" if len(d["plans"]) > 3 else ", ".join(map(str, d["plans"]))
                m = f"{d['mots'] // 1000} {d['mots'] % 1000:03d}" if d["mots"] >= 1000 else str(d["mots"])
                lignes.append(f"| {nom} | {rep} | {m} | {100 * d['mots'] / tot_m:.1f} % | {pl} |".replace(".", ",", 1) if "." in f"{100 * d['mots'] / tot_m:.1f}" else f"| {nom} | {rep} | {m} | {100 * d['mots'] / tot_m:.1f} % | {pl} |")
            lignes.append(f"| **Total** | **{len(reps)}** | **{tot_m // 1000} {tot_m % 1000:03d}** | | **{len(par)} locuteurs** |")
            out.append("\n".join(lignes))
        elif b["type"] == "dialogues":
            multi = [p["numero"] for p in plans if len({r["locuteur"] for r in reps if r["plan"] == p["numero"]}) >= 2]
            trois = [p["numero"] for p in plans if len({r["locuteur"] for r in reps if r["plan"] == p["numero"]}) >= 3]
            mot = {2: "deux", 3: "trois", 1: "un"}.get(len(trois), str(len(trois)))
            out.append(f"**{len(multi)} plans font dialoguer deux locuteurs ou plus**, dont {mot} à trois voix : {', '.join(map(str, trois[:-1]))} et {trois[-1]}" + b["suite"])
    return "\n".join(out)


def main():
    plans = D.lire("plans")["elements"]
    reps = D.lire("repliques")["elements"]
    rendus = {"scenario": rendre_scenario(plans, reps), "production": rendre_production(plans, reps), "son": rendre_son(plans, reps)}
    check = "--check" in sys.argv
    ecarts = 0
    for nom, texte in rendus.items():
        cible = CIBLES[nom]
        actuel = cible.read_text(encoding="utf-8") if cible.exists() else ""
        if texte != actuel:
            ecarts += 1
            if check:
                a, b = actuel.split("\n"), texte.split("\n")
                first = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
                print(f"{cible.name} : diffère (lignes {len(a)} → {len(b)}), première différence ligne {first + 1} :\n  fichier  : {a[first][:160] if first < len(a) else '<fin>'}\n  données  : {b[first][:160] if first < len(b) else '<fin>'}")
            else:
                cible.write_text(texte, encoding="utf-8", newline="\n"); print(f"{cible.name} régénéré")
        elif not check:
            print(f"{cible.name} inchangé")
    if check:
        print("aucun écart" if not ecarts else f"{ecarts} document(s) à régénérer")
    sys.exit(1 if (check and ecarts) else 0)


if __name__ == "__main__":
    main()
