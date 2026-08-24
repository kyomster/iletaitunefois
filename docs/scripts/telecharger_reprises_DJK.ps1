# Reprises du 23 août : Foule_StyleK et D02_StyleJ
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_reprises_DJK.ps1
#
# Foule_StyleK : le groupe sortait dupliqué, une seconde rangée flottait au dessus.
#   Négative anti duplication ajoutée, plus une clause positive `ONE SINGLE ROW ... in a single line,
#   nothing above them`. Une négative seule n'aurait pas suffi, c'est une structure.
#
# D02_StyleJ : sortait avec 332 px de bandes noires de chaque côté. Le rognage aurait coûté
#   42 % du champ et fait perdre l'horizon et la profondeur, dont le plan 4b-3 a besoin.
#   Regénéré avec une clause positive de plein cadre et un vocabulaire de pillarbox en négative.
#   Le fichier d'origine reste sous D02_StyleJ.avant-rognage.png.

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ dossier = "assets\S01E01\personnages-episode\StyleK"; nom = "Foule_StyleK.png"; src = "hf_20260823_191944_f51037ab-65e9-4a10-a756-0845a0db2836.png" },
  @{ dossier = "assets\S01E01\decors\StyleJ";              nom = "D02_StyleJ.png";   src = "hf_20260823_191944_69ff4b1f-4cff-4831-887f-ddb72a5c6677.png" }
)

foreach ($img in $images) {
  $dossier = Join-Path $racine $img.dossier
  if (-not (Test-Path $dossier)) { New-Item -ItemType Directory -Path $dossier -Force | Out-Null }
  $cible = Join-Path $dossier $img.nom
  Write-Host "-> $($img.dossier)\$($img.nom)"
  try {
    Invoke-WebRequest -Uri "$cdn/$($img.src)" -OutFile $cible -UseBasicParsing -TimeoutSec 120
    Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length)
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red
  }
}

Write-Host ""
Write-Host "Puis, si la nouvelle D02_StyleJ porte encore des bandes :"
Write-Host "  python docs\scripts\rogner_bandes_noires.py assets\S01E01\decors\StyleJ\D02_StyleJ.png --essai"
