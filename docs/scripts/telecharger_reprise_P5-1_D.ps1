# Reprise de P5-1_StyleD, 24 aout 2026.
#
# Le premier tirage portait « D2 » ECRIT EN GROSSES LETTRES sur un second ballon au fond.
# REGLE 28 : un code de decor ne tient pas sur un tres gros plan, il devient du texte.
# La correction du 22 aout avait developpe D2 en clair sur 5-2 et 5-3, et avait OUBLIE 5-1.
# En styles A, B et C ce plan est sorti correct par chance, donc personne ne l'avait vu.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_reprise_P5-1_D.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$cible  = Join-Path $racine "assets\S01E01\pilote\images\StyleD\P5-1_StyleD.png"
$url    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF/hf_20260824_052809_63974ebb-2e22-4447-bd78-f2986f60199c.png"

Write-Host "-> StyleD\P5-1_StyleD.png"
Invoke-WebRequest -Uri $url -OutFile $cible -UseBasicParsing -TimeoutSec 180
Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length)
Write-Host ""
Write-Host "A verifier : aucun texte, un seul ballon, ciel et toits flous derriere."
