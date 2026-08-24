# Pilotes complets en styles J et K, 40 images, 24 aout 2026.
#
# Les deux corrections de brique decouvertes sur le pilote D sont DANS le generateur et
# s'appliquent donc ici sans rien refaire : la nacelle unique de P1a-1 (REGLE 29) et le
# developpement de D2 sur P5-1 (REGLE 28). C'etait l'argument pour produire un style
# entier avant les deux autres : les deux defauts ont ete payes une fois, pas trois.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_pilotes_JK.ps1
#
# A verifier en priorite sur J : l'anachronisme. Deux des trois plaques J avaient ramene
# des bandes de cinema puis des voitures et un passage pieton. Tout plan J qui montre le
# sol d'une ville reelle est suspect.

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ style = "StyleJ"; nom = "P1a-1_StyleJ.png"; src = "hf_20260824_054443_567515d6-980a-4cf1-b659-9bf8837c40b5.png" },
  @{ style = "StyleJ"; nom = "P1a-2_StyleJ.png"; src = "hf_20260824_054442_3bfdee20-9b07-4db7-a6b6-aea99cfa7b89.png" },
  @{ style = "StyleJ"; nom = "P1a-3_StyleJ.png"; src = "hf_20260824_054442_d4ee377e-84af-46bf-b9cd-51ebad8efe40.png" },
  @{ style = "StyleJ"; nom = "P1a-4_StyleJ.png"; src = "hf_20260824_054442_da53c7db-9ae3-4374-bb85-f5be8e5b1c68.png" },
  @{ style = "StyleJ"; nom = "P1b-1_StyleJ.png"; src = "hf_20260824_054442_35ca70e5-3d46-4d94-8aad-b3af46900c5e.png" },
  @{ style = "StyleJ"; nom = "P1b-2_StyleJ.png"; src = "hf_20260824_054442_b45ae3ea-6bbc-41a6-8055-7ee4dfae38d4.png" },
  @{ style = "StyleJ"; nom = "P1b-3_StyleJ.png"; src = "hf_20260824_054442_a962e18d-cf47-4cb5-b923-a3599a6f793f.png" },
  @{ style = "StyleJ"; nom = "P02_StyleJ.png"; src = "hf_20260824_054442_9e17efd4-603e-43a1-97d9-756561a4c966.png" },
  @{ style = "StyleJ"; nom = "P02a_StyleJ.png"; src = "hf_20260824_054442_1dff4a72-d520-4a4a-a047-c6b39df286a0.png" },
  @{ style = "StyleJ"; nom = "P02b_StyleJ.png"; src = "hf_20260824_054442_d9453fd0-edd3-48ac-b28d-b95c9e3b5f3b.png" },
  @{ style = "StyleJ"; nom = "P03_StyleJ.png"; src = "hf_20260824_054634_90ee025d-0f11-4efe-a8e8-c0601d0ed536.png" },
  @{ style = "StyleJ"; nom = "P4a-1_StyleJ.png"; src = "hf_20260824_054634_aac4bc2f-86f3-4658-aa3a-206acb282db0.png" },
  @{ style = "StyleJ"; nom = "P4a-2_StyleJ.png"; src = "hf_20260824_054634_07b85474-0de5-4b9d-ba9b-1ea21a99a56a.png" },
  @{ style = "StyleJ"; nom = "P4a-3_StyleJ.png"; src = "hf_20260824_054634_21add7b5-6af7-45d5-8e16-f149c8205d13.png" },
  @{ style = "StyleJ"; nom = "P4b-1_StyleJ.png"; src = "hf_20260824_054634_b7dcb648-4c82-4154-bdc5-5c6276fc6751.png" },
  @{ style = "StyleJ"; nom = "P4b-2_StyleJ.png"; src = "hf_20260824_054634_b8d425ff-955c-48ba-af7b-fbddfabde13d.png" },
  @{ style = "StyleJ"; nom = "P4b-3_StyleJ.png"; src = "hf_20260824_054634_8a40dc1b-ef78-4fdf-9fce-487778d82e04.png" },
  @{ style = "StyleJ"; nom = "P5-1_StyleJ.png"; src = "hf_20260824_054634_6aded956-4dd6-431a-a408-bf479f66d256.png" },
  @{ style = "StyleJ"; nom = "P5-2_StyleJ.png"; src = "hf_20260824_054634_b029d23c-68ee-4c15-909e-c0fca51f62af.png" },
  @{ style = "StyleJ"; nom = "P5-3_StyleJ.png"; src = "hf_20260824_054634_4e7c5c63-cec5-4f65-a387-2bc42e7066bb.png" },
  @{ style = "StyleK"; nom = "P1a-1_StyleK.png"; src = "hf_20260824_054829_e1f61900-d1b7-4f26-a0cc-c89854c6dc7a.png" },
  @{ style = "StyleK"; nom = "P1a-2_StyleK.png"; src = "hf_20260824_054829_b2841373-a8fa-416f-b9f1-72c407101a18.png" },
  @{ style = "StyleK"; nom = "P1a-3_StyleK.png"; src = "hf_20260824_054829_a472a104-ceaf-4897-8188-2f93474c811b.png" },
  @{ style = "StyleK"; nom = "P1a-4_StyleK.png"; src = "hf_20260824_054829_7df213e6-ac92-4514-9ad3-19c1b6e08359.png" },
  @{ style = "StyleK"; nom = "P1b-1_StyleK.png"; src = "hf_20260824_054829_6a209b44-76d3-4c09-98ed-01ba3fedc4b8.png" },
  @{ style = "StyleK"; nom = "P1b-2_StyleK.png"; src = "hf_20260824_054829_0c138b2b-8cfb-44bd-b7e5-e5b12bd11fe5.png" },
  @{ style = "StyleK"; nom = "P1b-3_StyleK.png"; src = "hf_20260824_054829_aabcf505-7182-4a4c-9734-9c0e701d426b.png" },
  @{ style = "StyleK"; nom = "P02_StyleK.png"; src = "hf_20260824_054829_cb15ae6b-f9fe-4d0b-a46c-c79c22e35527.png" },
  @{ style = "StyleK"; nom = "P02a_StyleK.png"; src = "hf_20260824_054829_5c70a6eb-dbc6-4a04-a3eb-7d84206701d4.png" },
  @{ style = "StyleK"; nom = "P02b_StyleK.png"; src = "hf_20260824_054830_c1d2a9a7-5c9a-4f37-a630-ec074834ddde.png" },
  @{ style = "StyleK"; nom = "P03_StyleK.png"; src = "hf_20260824_055026_ca20a512-1232-4e4c-8e8f-f9610cb02e7a.png" },
  @{ style = "StyleK"; nom = "P4a-1_StyleK.png"; src = "hf_20260824_055026_c06ff1ee-291d-4092-98f6-83531a4e7448.png" },
  @{ style = "StyleK"; nom = "P4a-2_StyleK.png"; src = "hf_20260824_055026_8c10b17d-d972-477e-9176-8cf38e80f2e9.png" },
  @{ style = "StyleK"; nom = "P4a-3_StyleK.png"; src = "hf_20260824_055026_044ef4d5-80ac-41f3-b12d-bc7445c96d76.png" },
  @{ style = "StyleK"; nom = "P4b-1_StyleK.png"; src = "hf_20260824_055026_0e2db459-f7f1-4df3-9756-54261d0b01ba.png" },
  @{ style = "StyleK"; nom = "P4b-2_StyleK.png"; src = "hf_20260824_055026_a7f2955c-0d32-4e99-b48d-fe9498cd99d7.png" },
  @{ style = "StyleK"; nom = "P4b-3_StyleK.png"; src = "hf_20260824_055026_8f6d47d4-85f0-4484-b8d3-0dacc6178936.png" },
  @{ style = "StyleK"; nom = "P5-1_StyleK.png"; src = "hf_20260824_055026_b33b62ac-801f-414d-91af-056cc5122ff8.png" },
  @{ style = "StyleK"; nom = "P5-2_StyleK.png"; src = "hf_20260824_055027_a7094a58-db09-45c3-bd6e-aa4a37a2e280.png" },
  @{ style = "StyleK"; nom = "P5-3_StyleK.png"; src = "hf_20260824_055026_500c5188-1a83-49aa-8065-313fabf7ec5d.png" }
)

$ok = 0; $ko = 0
foreach ($img in $images) {
  $dossier = Join-Path $base $img.style
  if (-not (Test-Path $dossier)) { New-Item -ItemType Directory -Path $dossier -Force | Out-Null }
  $cible = Join-Path $dossier $img.nom
  Write-Host "-> $($img.style)\$($img.nom)"
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
Write-Host "Les pilotes StyleJ et StyleK doivent compter 20 images chacun."
