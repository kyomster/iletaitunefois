# Rapatriement des 15 références des styles D, J et K
# À lancer depuis la machine de Guillaume : le CDN de résultat n'est pas joignable
# depuis le conteneur Cowork, il l'est depuis Windows.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_references_DJK.ps1
#
# Les décors atterrissent sous assets\S01E01\decors\Style{D,J,K}\
# Les personnages sous assets\S01E01\personnages-episode\Style{D,J,K}\
#
# POINT D'ARRÊT DUR. Ces quinze images se regardent une par une AVANT d'en dériver
# quoi que ce soit. C'est la RÈGLE 14, celle qui a coûté 96 images la dernière fois.

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ dossier = "assets\S01E01\decors\StyleD";              nom = "D01_StyleD.png";      src = "hf_20260823_131040_947ba125-c3d6-4f85-ab79-6367a0e2ca55.png" },
  @{ dossier = "assets\S01E01\decors\StyleD";              nom = "D02_StyleD.png";      src = "hf_20260823_131040_3be9ee1d-af65-4617-bd32-a324ff458fb4.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleD"; nom = "Foule_StyleD.png";    src = "hf_20260823_131040_6c8ba721-f57d-48fd-9d53-e505bde25973.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleD"; nom = "Garnerin_StyleD.png"; src = "hf_20260823_131040_10ba3179-09db-42c0-9b38-b6392ab84d98.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleD"; nom = "Parieurs_StyleD.png"; src = "hf_20260823_131040_9bef805e-8d77-48c5-ae16-d0f41a11bde6.png" },

  @{ dossier = "assets\S01E01\decors\StyleJ";              nom = "D01_StyleJ.png";      src = "hf_20260823_131040_8a3a5275-8fea-4e64-9445-73046328431b.png" },
  @{ dossier = "assets\S01E01\decors\StyleJ";              nom = "D02_StyleJ.png";      src = "hf_20260823_131040_dc4adb60-f515-4c83-8e24-5d33f9683fda.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleJ"; nom = "Foule_StyleJ.png";    src = "hf_20260823_131040_7c489220-0657-4f2d-91df-904086fbbe73.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleJ"; nom = "Garnerin_StyleJ.png"; src = "hf_20260823_131040_9cb5e549-d909-4b4e-bf17-64e4fed8649a.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleJ"; nom = "Parieurs_StyleJ.png"; src = "hf_20260823_131041_d3d82174-6895-4dbc-b333-fdb28698f2b8.png" },

  @{ dossier = "assets\S01E01\decors\StyleK";              nom = "D01_StyleK.png";      src = "hf_20260823_131123_dcd2ec9e-cd88-481c-8337-cdd7f75282ba.png" },
  @{ dossier = "assets\S01E01\decors\StyleK";              nom = "D02_StyleK.png";      src = "hf_20260823_131123_2a71e5d1-a6a0-4fc6-8a94-cea8216d4688.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleK"; nom = "Foule_StyleK.png";    src = "hf_20260823_131123_cdc6b0c9-22cc-4c3c-b485-d0ac18bf1ee3.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleK"; nom = "Garnerin_StyleK.png"; src = "hf_20260823_131123_ee5ef5ca-15f0-4aa8-83da-6d8de357b1e4.png" },
  @{ dossier = "assets\S01E01\personnages-episode\StyleK"; nom = "Parieurs_StyleK.png"; src = "hf_20260823_131123_44c06d60-a159-4f50-883b-d66d7b2d5b3d.png" }
)

$ok = 0; $ko = 0
foreach ($img in $images) {
  $dossier = Join-Path $racine $img.dossier
  if (-not (Test-Path $dossier)) { New-Item -ItemType Directory -Path $dossier -Force | Out-Null }
  $cible = Join-Path $dossier $img.nom
  Write-Host "-> $($img.dossier)\$($img.nom)"
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
Write-Host "POINT D'ARRET : ne rien deriver de ces images avant de les avoir regardees une par une."
