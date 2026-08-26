# Epreuve de modernite : Db (D affute) et L (peinture animee hybride), 25 aout 2026.
#
# Db — MEME dessin, meme troupe, meme identite que D. Seule la FINITION change.
#   Retire : grain de pellicule, ombrage a l'aerographe, brume, pastel, faible contraste.
#   Ajoute : ombre a bord dur, contraste profond a noirs riches, plans de decor nets,
#            une seule couleur d'accent saturee portee par la LUMIERE, jamais par le tissu.
#   Question posee : ce qui date D est il le dessin, ou seulement son rendu ?
#
# L — style neuf, langage dominant de l'animation des annees 2020 : volumes mis en scene
#   en trois dimensions puis FINIS A LA PEINTURE VISIBLE, touches epaisses qui accrochent
#   la lumiere, silhouettes graphiques, base desaturee percee d'un ou deux accents satures,
#   contre jour dur. C'est ce que le public de 15 a 30 ans associe spontanement a « maintenant ».
#
# Les deux sont produits A SEC, sans reference reinjectee : aucune plaque Db ni L n'existe
# (PLAN-styles-D-E-F.md §2.3). Les briques integrent les RÈGLES 32 (decor sans cadrage),
# 33 (bannieres nues) et 34 (materiau plutot que couleur).
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_epreuve_Db_L.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ style = "StyleDb"; nom = "P02_StyleDb.png";   src = "hf_20260825_101742_c6cac08c-4344-40c8-8564-e2a6d399cdc0.png" },
  @{ style = "StyleDb"; nom = "P1a-3_StyleDb.png"; src = "hf_20260825_101742_9d62f774-aeb0-4060-ab5a-c3b3eaef6808.png" },
  @{ style = "StyleDb"; nom = "P4b-1_StyleDb.png"; src = "hf_20260825_101742_1ddcc023-ab36-4cef-87a1-3a904a474f0a.png" },
  @{ style = "StyleL";  nom = "P02_StyleL.png";    src = "hf_20260825_101742_6ed44703-1b43-4788-9114-8dfdba7539e1.png" },
  @{ style = "StyleL";  nom = "P1a-3_StyleL.png";  src = "hf_20260825_101742_40bb9412-ad69-4c9b-9761-51dac484763c.png" },
  @{ style = "StyleL";  nom = "P4b-1_StyleL.png";  src = "hf_20260825_101742_a1b95e3f-ccbb-46a6-b247-b794f77bc562.png" }
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
Write-Host "A comparer cote a cote avec StyleD sur les MEMES trois plans."
