# Trois images d'essai en style D, 23 aout 2026.
#
# Pourquoi trois et pas vingt. C'est la premiere fois que les references D, J et K sont
# REINJECTEES dans un prompt de plan. La discipline du depot dit de ne jamais lancer un lot
# entier sur un mecanisme non verifie (le clip zero du PLAN-pilote-execution). Une image par
# famille de reference suffit a valider les trois cas :
#
#   P1a-1  D01 + Foule      le decor au sol et la foule sans visage
#   P03    D01 + Garnerin   le decor au sol et un personnage nomme a visage
#   P4b-1  D02 seul         le decor ciel, registre de lumiere TENSION
#
# Si les trois passent, les 57 autres partent en confiance. Cout de l'essai : 6 credits.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_essai_pilote_D.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images\StyleD"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ nom = "P1a-1_StyleD.png"; src = "hf_20260823_203103_e5f1ab00-4bea-4097-b390-e1b86b4162b5.png" },
  @{ nom = "P03_StyleD.png";   src = "hf_20260823_203103_5c3a42ee-721a-49a9-80b3-eb19ce589075.png" },
  @{ nom = "P4b-1_StyleD.png"; src = "hf_20260823_203103_c5e44a41-cb3c-4f9d-b002-18d08cf0b694.png" }
)

if (-not (Test-Path $base)) { New-Item -ItemType Directory -Path $base -Force | Out-Null }

foreach ($img in $images) {
  $cible = Join-Path $base $img.nom
  Write-Host "-> StyleD\$($img.nom)"
  try {
    Invoke-WebRequest -Uri "$cdn/$($img.src)" -OutFile $cible -UseBasicParsing -TimeoutSec 120
    Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length)
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red
  }
}

Write-Host ""
Write-Host "Note : P4b-1_StyleD ecrase l'image d'epreuve du meme nom, produite SANS reference."
Write-Host "C'est voulu, elle ne raccordait pas avec le reste du pilote."
