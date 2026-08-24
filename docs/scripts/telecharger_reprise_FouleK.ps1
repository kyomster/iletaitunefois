# Reprise 3 de Foule_StyleK, 23 aout 2026.
#
# Tirages 1 et 2 : le groupe sortait DUPLIQUE, une seconde rangee identique au dessus de la premiere.
#   Le tirage 2 portait pourtant la negative anti duplication ET la clause positive
#   `ONE SINGLE ROW ... in a single line, nothing above them`. Les deux ont echoue.
#   Rattrapage local impossible : mesure ligne par ligne, les deux rangees se chevauchent
#   sans discontinuite, les corps de la rangee fantome descendent la ou commencent les tetes
#   de la vraie rangee. Aucune ligne de coupe ne les separe.
#
# Diagnostic : REGLE 2 du depot, ne jamais demander une grille au modele, il ne sait pas compter.
#   « une douzaine de figurants en pied sur fond neutre » EST une demande de grille deguisee.
#   A, B, C, D et J s'en sont tires ; K compose en deux rangees, deux fois sur deux.
#
# Tirage 3 : nombre explicite et petit (SEPT), ligne droite au sol prescrite, et surtout
#   la moitie haute de l'image prescrite VIDE en positif.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\telecharger_reprise_FouleK.ps1

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$cible  = Join-Path $racine "assets\S01E01\personnages-episode\StyleK\Foule_StyleK.png"
$url    = "https://d8j0ntlcm91z4.cloudfront.net/user_3GOjCOBu31lBMfhPtMbERCjKAbF/hf_20260823_194621_209a6a2d-6c81-457e-a304-8c981b13e1ed.png"

Write-Host "-> assets\S01E01\personnages-episode\StyleK\Foule_StyleK.png"
Invoke-WebRequest -Uri $url -OutFile $cible -UseBasicParsing -TimeoutSec 120
Write-Host ("   ok, {0:N0} octets" -f (Get-Item $cible).Length)
Write-Host ""
Write-Host "A verifier : UNE seule rangee, sept figures, toutes de dos, moitie haute vide."
