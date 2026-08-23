# Rapatriement des 18 images de l'épreuve de style, six styles D à I
# À lancer depuis la machine de Guillaume : le CDN de résultat n'est pas joignable
# depuis le conteneur Cowork, il l'est depuis Windows.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_epreuve_DEF.ps1
#
# Les fichiers atterrissent sous assets\S01E01\pilote\images\Style{D..I}\ au nom canonique.
#
# Note : le premier job de P02_StyleE, 7a03883a-e721-46e1-9274-b27a92e53359, est resté
# bloqué en file d'attente sans jamais démarrer, alors que les autres ont rendu en
# quelques secondes. Resoumis à l'identique sous 9d29c767-772c-48ed-8dc5-7707aa9fee20,
# qui est celui utilisé ici. Coût réel de l'épreuve : 38 crédits au lieu de 36.

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ style = "StyleD"; nom = "P02_StyleD.png";   src = "hf_20260822_210423_858617be-5480-4d80-bfd9-ee83e994ba54.png" },
  @{ style = "StyleD"; nom = "P1a-3_StyleD.png"; src = "hf_20260822_210422_9d50db50-2f2a-4d2f-ad9d-258f774490c6.png" },
  @{ style = "StyleD"; nom = "P4b-1_StyleD.png"; src = "hf_20260822_210422_d9b1dda1-7f36-4dcd-8bdd-58eecff4300e.png" },

  @{ style = "StyleE"; nom = "P02_StyleE.png";   src = "hf_20260822_211428_9d29c767-772c-48ed-8dc5-7707aa9fee20.png" },
  @{ style = "StyleE"; nom = "P1a-3_StyleE.png"; src = "hf_20260822_210422_83f8c281-85e3-41db-9d5c-51a8e26f38fe.png" },
  @{ style = "StyleE"; nom = "P4b-1_StyleE.png"; src = "hf_20260822_210424_75502e0d-6bfa-4bd0-b8e3-ee587c1e9162.png" },

  @{ style = "StyleF"; nom = "P02_StyleF.png";   src = "hf_20260822_210423_2fb5be75-f819-43f1-8125-ab394fe44b2e.png" },
  @{ style = "StyleF"; nom = "P1a-3_StyleF.png"; src = "hf_20260822_210422_fcc621cd-b50a-496a-8f30-e52644e821bf.png" },
  @{ style = "StyleF"; nom = "P4b-1_StyleF.png"; src = "hf_20260822_210422_72d1f5e4-c3b3-48dd-9e6f-6be7c22e7a26.png" },

  @{ style = "StyleG"; nom = "P02_StyleG.png";   src = "hf_20260822_212539_007d85a9-6590-40b3-a2c4-e9f420b378fa.png" },
  @{ style = "StyleG"; nom = "P1a-3_StyleG.png"; src = "hf_20260822_212539_30c8aca7-d76c-46ee-9854-c70d69479369.png" },
  @{ style = "StyleG"; nom = "P4b-1_StyleG.png"; src = "hf_20260822_212540_9c6d8fb5-0397-498a-ace2-9f230fd30770.png" },

  @{ style = "StyleH"; nom = "P02_StyleH.png";   src = "hf_20260822_212539_945d72f1-e44c-482d-9662-9014e477c364.png" },
  @{ style = "StyleH"; nom = "P1a-3_StyleH.png"; src = "hf_20260822_212539_5a5744e3-36d8-47d0-9be6-6e954214fcd1.png" },
  @{ style = "StyleH"; nom = "P4b-1_StyleH.png"; src = "hf_20260822_212539_2883831e-f9f2-40ca-8d56-d1712cb02496.png" },

  @{ style = "StyleI"; nom = "P02_StyleI.png";   src = "hf_20260822_212539_7add017a-a369-4f19-bf37-d248a9b58489.png" },
  @{ style = "StyleI"; nom = "P1a-3_StyleI.png"; src = "hf_20260822_212539_b054414b-9f53-4f42-88c1-fc2b07379b62.png" },
  @{ style = "StyleI"; nom = "P4b-1_StyleI.png"; src = "hf_20260822_212540_575a0421-1202-484c-919c-a39c610c1866.png" }
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
    if ($taille -lt 100000) {
      Write-Host ("   SUSPECT, seulement {0:N0} octets" -f $taille) -ForegroundColor Yellow
      $ko++
    } else {
      Write-Host ("   ok, {0:N0} octets" -f $taille)
      $ok++
    }
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red
    $ko++
  }
}

Write-Host ""
Write-Host "Termine. $ok fichiers corrects, $ko a verifier."
