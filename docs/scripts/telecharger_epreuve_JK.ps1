# Rapatriement des 6 images des styles J et K
# À lancer depuis la machine de Guillaume : le CDN de résultat n'est pas joignable
# depuis le conteneur Cowork, il l'est depuis Windows.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_epreuve_JK.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ style = "StyleJ"; nom = "P02_StyleJ.png";   src = "hf_20260823_110021_5fe7c85e-4020-49c4-8556-756dd978d486.png" },
  @{ style = "StyleJ"; nom = "P1a-3_StyleJ.png"; src = "hf_20260823_110021_595fadb0-d639-4290-8724-0be2eba59c65.png" },
  @{ style = "StyleJ"; nom = "P4b-1_StyleJ.png"; src = "hf_20260823_110021_74ed90a2-271b-415f-a492-e9ee65e3d28b.png" },

  @{ style = "StyleK"; nom = "P02_StyleK.png";   src = "hf_20260823_110108_703c4cb8-9566-4243-a0e7-1b26ed4b6f0a.png" },
  @{ style = "StyleK"; nom = "P1a-3_StyleK.png"; src = "hf_20260823_110108_912d624f-1a56-461d-8178-59ad980b37fd.png" },
  @{ style = "StyleK"; nom = "P4b-1_StyleK.png"; src = "hf_20260823_110108_c476e3b7-e739-4041-8c54-e894a35e5c09.png" }
)

$ok = 0; $ko = 0
foreach ($img in $images) {
  $dossier = Join-Path $base $img.style
  if (-not (Test-Path $dossier)) { New-Item -ItemType Directory -Path $dossier -Force | Out-Null }
  $cible = Join-Path $dossier $img.nom
  Write-Host "-> $($img.style)\$($img.nom)"
  try {
    Invoke-WebRequest -Uri "$cdn/$($img.src)" -OutFile $cible -UseBasicParsing -TimeoutSec 120
    $taille = (Get-Item $cible).Length
    if ($taille -lt 100000) { Write-Host ("   SUSPECT, {0:N0} octets" -f $taille) -ForegroundColor Yellow; $ko++ }
    else { Write-Host ("   ok, {0:N0} octets" -f $taille); $ok++ }
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red; $ko++
  }
}

Write-Host ""
Write-Host "Termine. $ok fichiers corrects, $ko a verifier."
Write-Host ""
Write-Host "Styles abandonnes le 23 aout : E, F, H. Pour supprimer leurs images :"
Write-Host "  Remove-Item -Recurse -Force '$base\StyleE','$base\StyleF','$base\StyleH'"
