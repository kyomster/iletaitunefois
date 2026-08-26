# Epreuve des styles NATIFS ANIMATION : M, N, O — 25 aout 2026.
#
# POURQUOI CES TROIS LA. Les styles « modernes » proposes jusqu'ici (H imprime, I roman
# graphique, E affiche, L peinture) se definissaient tous par une TEXTURE DE SUPPORT :
# trame, grain de papier, grain de toile, touche de pinceau. Ce sont des marqueurs d'image
# FIXE. En animation, une texture qui appartient au support GROUILLE d'une image a l'autre :
# le grain de papier qui danse a 16 im/s est un defaut classique. L'epreuve, qui ne juge que
# trois images fixes, selectionnait donc des qualites qui ne survivent pas au mouvement.
#
# M, N et O sont issus de techniques de PRODUCTION reelles, television ou long metrage, et
# ne portent AUCUNE texture de support. Leurs negatives interdisent explicitement grain de
# papier, toile, trame, touche visible et grain de pellicule. Ce qui les distingue est la
# LUMIERE et le VOLUME, c'est a dire des proprietes qui survivent au mouvement.
#
#   M — 2D de serie moderne a lumiere numerique. Dessin plat et graphique, aplats francs,
#       mais contre jour colore, ombres teintees, halos. La texture est la couleur.
#   N — dessin 2D eclaire en volume. Personnages dessines a plat, puis passe de lumiere
#       volumetrique par dessus : ombres portees, rebond chaud, speculaire sur les tissus.
#       C'est le pont entre A et D que nous n'avions jamais teste.
#   O — 3D a ombrage toon dur. Volumes sculptes, cel shading a deux tons, contour net.
#       Sa modernite tiendra surtout a la CADENCE, que seule la video montrera.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_epreuve_MNO.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ style = "StyleM"; nom = "P02_StyleM.png";   src = "hf_20260825_111304_6d62a7af-636d-4ca3-9e85-89761cb341fd.png" },
  @{ style = "StyleM"; nom = "P1a-3_StyleM.png"; src = "hf_20260825_111304_2401ada4-c7f8-41fb-abec-56d6c46608ec.png" },
  @{ style = "StyleM"; nom = "P4b-1_StyleM.png"; src = "hf_20260825_111304_64a1a0cd-3154-4cb2-8ebb-d4ce27a60fe4.png" },

  @{ style = "StyleN"; nom = "P02_StyleN.png";   src = "hf_20260825_111304_06fac737-1361-4cdc-909f-c51fcdc3b3f8.png" },
  @{ style = "StyleN"; nom = "P1a-3_StyleN.png"; src = "hf_20260825_111304_36dcc9f6-a7ba-42ac-a652-b39e65e5585d.png" },
  @{ style = "StyleN"; nom = "P4b-1_StyleN.png"; src = "hf_20260825_111304_476447ce-d801-41c9-a2c5-7a9a9bfe2da7.png" },

  @{ style = "StyleO"; nom = "P02_StyleO.png";   src = "hf_20260825_111304_e388b372-7076-45bf-87b3-b7847b59f6ac.png" },
  @{ style = "StyleO"; nom = "P1a-3_StyleO.png"; src = "hf_20260825_111304_85d0d23f-23a4-4512-a940-7057943ac873.png" },
  @{ style = "StyleO"; nom = "P4b-1_StyleO.png"; src = "hf_20260825_111306_9003a7fe-db4d-47f6-8bea-464bcaeeef3a.png" }
)

$ok = 0; $ko = 0
foreach ($img in $images) {
  $dossier = Join-Path $base $img.style
  if (-not (Test-Path $dossier)) { New-Item -ItemType Directory -Path $dossier -Force | Out-Null }
  $cible = Join-Path $dossier $img.nom
  Write-Host "-> $($img.style)\$($img.nom)"
  try {
    Invoke-WebRequest -Uri "$cdn/$($img.src)" -OutFile $cible -UseBasicParsing -TimeoutSec 180
    Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length); $ok++
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red; $ko++
  }
}

Write-Host ""
Write-Host "Termine. $ok fichiers corrects, $ko a verifier."
Write-Host "A comparer aux MEMES trois plans en StyleD, StyleDb et StyleL."
