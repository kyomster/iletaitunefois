# Les quatre reprises des pilotes J et K, 24 aout 2026.
#
# P02_StyleJ et P02b_StyleJ : le manteau du maigre sortait BLEU SARCELLE sur P02 et brun sur
#   P02b, soit une rupture de raccord entre deux plans qui se suivent en champ contrechamp.
#   La couleur nommee en positif (REGLE 34) a tenu en D et en K et a cede en J. Sur un rendu
#   photorealiste, une veste d'ouvrier bleu passe est HISTORIQUEMENT PLAUSIBLE : le referent la
#   ramene malgre la consigne, comme les bannieres brodees et les voitures de Paris avant elle.
#   Corollaire de la REGLE 34 : on decrit le MATERIAU et l'usure, pas la teinte.
#     `his coat made of undyed coarse brown wool, worn thin and patched at the elbows,
#      the colour of raw sacking and dust, no dyed fabric on him`
#
# P5-1_StyleJ : la brique demandait un tres gros plan sur la main qui saisit le couteau ; le
#   modele a rendu un plan moyen de Garnerin portant un panier d'osier vide. `Framing: very
#   close shot` ne suffit pas seul. Durci en decrivant ce que le cadre CONTIENT :
#     `The frame is filled edge to edge by the hand, the forearm and the woven side of the
#      basket; no face, no head, no shoulders and no full body anywhere in the frame.`
#
# P1a-3_StyleK : le ballon sortait au sol au lieu de la contre plongee sur la couronne. Meme
#   traitement, on decrit le contenu du cadre plutot que l'angle.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_reprises_pilotes_JK.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$base   = Join-Path $racine "assets\S01E01\pilote\images"
$cdn    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF"

$images = @(
  @{ style = "StyleJ"; nom = "P02_StyleJ.png";   src = "hf_20260824_064526_ef148272-9ab8-492f-9dfe-85d35754fb11.png" },
  @{ style = "StyleJ"; nom = "P02b_StyleJ.png";  src = "hf_20260824_064525_819b098b-dd7f-4e4a-89f9-1cfed441004c.png" },
  @{ style = "StyleJ"; nom = "P5-1_StyleJ.png";  src = "hf_20260824_064525_0df86368-1147-4aa1-8578-c1aa8841b3f0.png" },
  @{ style = "StyleK"; nom = "P1a-3_StyleK.png"; src = "hf_20260824_064526_44fdd145-cdb6-4eb8-8a15-8c427985bdc0.png" }
)

$ok = 0; $ko = 0
foreach ($img in $images) {
  $cible = Join-Path (Join-Path $base $img.style) $img.nom
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
Write-Host "A verifier ensuite, si P02b porte encore des bandes :"
Write-Host "  python docs\scripts\rogner_bandes_noires.py assets\S01E01\pilote\images\StyleJ\P02b_StyleJ.png --essai"
