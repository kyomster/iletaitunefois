# Style P — anime de serie television moderne. 25 aout 2026.
#
# NOTE DE METHODE, importante. Aucune marque, aucun titre de serie, aucun nom d'auteur ne
# figure dans le prompt (PLAN-styles-D-E-F.md §2.1). Ce qui est decrit est une TECHNIQUE de
# production : contour noir d'epaisseur constante, cel shading a deux ou trois tons a bords
# durs, formes de personnage simples et lisibles, palette claire et saturee, compositing
# numerique (bloom doux, ciel degrade, voile de lumiere), decors peints plus riches que les
# personnages, mise en scene concue pour l'animation limitee. Une technique n'appartient a
# personne ; un design appartient a quelqu'un.
#
# POURQUOI CE STYLE EST PERTINENT ICI
#
# 1. Il tombe exactement entre A et O, les deux que vous avez shortlistes : couleur propre,
#    ombre a bord dur, aucune texture de support. A le fait a plat, O en volume sculpte,
#    P le fait en dessin anime de serie avec compositing.
# 2. Il est NATIF ANIMATION et ne porte aucune texture qui grouille en mouvement.
# 3. Il est concu pour la PRODUCTION DE MASSE en animation limitee, exactement la contrainte
#    de 79 plans et 300 rendus par episode.
# 4. La troupe s'y transpose bien : Sam, Naya et Elio sont faits de grandes formes lisibles
#    et de couleurs reservees franches, ce qui est precisement la grammaire de cet idiome.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_epreuve_P.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images\StyleP"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ nom = "P02_StyleP.png";   src = "hf_20260825_143822_4985c565-3e0a-4c5b-aa66-7b9313f2736b.png" },
  @{ nom = "P1a-3_StyleP.png"; src = "hf_20260825_143822_ce0c83fa-3734-41de-8276-92844b21fe65.png" },
  @{ nom = "P4b-1_StyleP.png"; src = "hf_20260825_143823_26a6f5d5-fecb-4a11-8aed-4d28b691b93f.png" }
)

if (-not (Test-Path $base)) { New-Item -ItemType Directory -Path $base -Force | Out-Null }

foreach ($img in $images) {
  $cible = Join-Path $base $img.nom
  Write-Host "-> StyleP\$($img.nom)"
  try {
    Invoke-WebRequest -Uri "$cdn/$($img.src)" -OutFile $cible -UseBasicParsing -TimeoutSec 180
    Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length)
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red
  }
}

Write-Host ""
Write-Host "A comparer aux MEMES trois plans en StyleA et StyleO, votre shortlist."
