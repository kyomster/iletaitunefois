# Reprise 3 de D02_StyleJ, 23 aout 2026.
#
# Tirage 1 : 332 px de bandes noires laterales, rognage a 42 % de perte, refuse (REGLE 35).
# Tirage 2 : plein cadre correct, mais la rue au centre bas montre des VOITURES GAREES,
#            un passage pieton, des marquages au sol et des lampadaires modernes.
#            La negative `cars, tarmac road, modern buildings` ne les a pas arretes.
# Tirage 3 : le sol est interdit en positif, `THE GROUND IS NEVER VISIBLE, no street, no road,
#            no pavement and no ground anywhere in the frame, only rooftops, chimneys, treetops and sky`.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_reprise_D02J.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$cible  = Join-Path $racine "assets\S01E01\decors\StyleJ\D02_StyleJ.png"
$url    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF/hf_20260823_193310_d085c6da-a350-4a38-ac27-e471624a3c81.png"

Write-Host "-> assets\S01E01\decors\StyleJ\D02_StyleJ.png"
Invoke-WebRequest -Uri $url -OutFile $cible -UseBasicParsing -TimeoutSec 120
Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length)
Write-Host ""
Write-Host "Puis verifier les bandes :"
Write-Host "  python docs\scripts\rogner_bandes_noires.py assets\S01E01\decors\StyleJ\D02_StyleJ.png --essai"
