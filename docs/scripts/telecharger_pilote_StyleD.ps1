# Pilote complet en style D, 18 images, 24 aout 2026.
#
# P03 et P4b-1 ne sont pas dans cette liste : elles ont ete produites la veille comme images
# d'essai de reinjection et sont validees. Les 18 autres completent les 20 du pilote.
#
# P1a-1 a ete regeneree avec la brique corrigee : le premier tirage sortait DEUX nacelles
# d'osier, une accrochee sous le ballon et une seconde posee sur l'herbe. REGLE 29, la plaque
# D01 porte deja sa nacelle et la brique en nommait une dans les props. Corrigee comme 1b-2
# l'avait ete, en nommant l'etat voulu : `ONE single wicker basket only ... no second basket`.
#
# P02 et P1a-3 ecrasent les images d'epreuve du meme nom, produites SANS reference reinjectee.
# C'est voulu, elles ne raccordaient pas avec le reste du pilote.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_pilote_StyleD.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images\StyleD"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ nom = "P1a-1_StyleD.png"; src = "hf_20260824_051713_a3a111d5-da58-4ee1-ae06-01c13c973138.png" },
  @{ nom = "P1a-2_StyleD.png"; src = "hf_20260824_051713_fb3da9af-28c5-4ce2-b5b0-424adc6652da.png" },
  @{ nom = "P1a-3_StyleD.png"; src = "hf_20260824_051713_06063339-3195-40e9-a699-d663ec85ac47.png" },
  @{ nom = "P1a-4_StyleD.png"; src = "hf_20260824_051713_12dad190-440c-43f1-b4ad-e97f87a8f06e.png" },
  @{ nom = "P1b-1_StyleD.png"; src = "hf_20260824_051714_d1b4378c-700d-4e47-80c6-1bb26f6451c9.png" },
  @{ nom = "P1b-2_StyleD.png"; src = "hf_20260824_051713_b4b198dd-991b-461e-b1f4-1a0472dd20e9.png" },
  @{ nom = "P1b-3_StyleD.png"; src = "hf_20260824_051713_aeaaefae-4ccf-4979-be83-bb629c4909e5.png" },
  @{ nom = "P02_StyleD.png";   src = "hf_20260824_051713_037e7bf4-e2a3-4dc1-9752-d58675bb1c52.png" },
  @{ nom = "P02a_StyleD.png";  src = "hf_20260824_051713_2531e608-3e71-40fa-b11c-0cf9b40095f6.png" },
  @{ nom = "P02b_StyleD.png";  src = "hf_20260824_051713_6a5a3b99-c219-4aa5-a59c-82c00b6e5feb.png" },
  @{ nom = "P4a-1_StyleD.png"; src = "hf_20260824_051840_f232e180-10aa-4c64-90dd-3daec1e48162.png" },
  @{ nom = "P4a-2_StyleD.png"; src = "hf_20260824_051840_96bb24e6-6337-4103-a88c-73add04c59ef.png" },
  @{ nom = "P4a-3_StyleD.png"; src = "hf_20260824_051841_43fae580-dc2f-4de7-8c9d-69656a9a41b2.png" },
  @{ nom = "P4b-2_StyleD.png"; src = "hf_20260824_051840_fec3e21b-c7ff-445d-a631-8bd298a71c77.png" },
  @{ nom = "P4b-3_StyleD.png"; src = "hf_20260824_051841_cbbdaf5c-dd99-4bdd-812b-ae5ce3618cd1.png" },
  @{ nom = "P5-1_StyleD.png";  src = "hf_20260824_051840_d8697c15-9d57-41e9-bb24-4140768c6463.png" },
  @{ nom = "P5-2_StyleD.png";  src = "hf_20260824_051840_bb640641-9b32-4dc8-bece-1c67d5e792da.png" },
  @{ nom = "P5-3_StyleD.png";  src = "hf_20260824_051840_4b03b613-24c7-488a-8d8b-140298617a6d.png" }
)

if (-not (Test-Path $base)) { New-Item -ItemType Directory -Path $base -Force | Out-Null }

$ok = 0; $ko = 0
foreach ($img in $images) {
  $cible = Join-Path $base $img.nom
  Write-Host "-> StyleD\$($img.nom)"
  try {
    Invoke-WebRequest -Uri "$cdn/$($img.src)" -OutFile $cible -UseBasicParsing -TimeoutSec 180
    $t = (Get-Item $cible).Length
    if ($t -lt 100000) { Write-Host ("   SUSPECT, {0:N0} octets" -f $t) -ForegroundColor Yellow; $ko++ }
    else { Write-Host ("   ok, {0:N0} octets" -f $t); $ok++ }
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red; $ko++
  }
}

Write-Host ""
Write-Host "Termine. $ok fichiers corrects, $ko a verifier."
Write-Host "Le pilote StyleD doit maintenant compter 20 images."
