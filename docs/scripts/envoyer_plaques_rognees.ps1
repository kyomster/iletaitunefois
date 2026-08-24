# Envoi des deux plaques ROGNEES vers Higgsfield, 23 aout 2026.
#
# Pourquoi ce script existe. Treize des quinze references peuvent etre reinjectees par leur
# job_id de generation, sans rien envoyer. Mais D01_StyleJ et D01_StyleK ont ete ROGNEES en
# local pour retirer leurs bandes noires (REGLE 35) : le job_id pointe encore sur la version
# AVEC bandes, et une plaque a bandes reinjectee impose ses bandes aux vingt plans (REGLE 1).
# Il faut donc envoyer les fichiers corriges. Mon conteneur n'a pas acces au reseau Higgsfield,
# ni en lecture ni en ecriture ; votre machine, si.
#
#   powershell -ExecutionPolicy Bypass -File docs\scripts\envoyer_plaques_rognees.ps1
#
# Les URL signees expirent le 24 aout a 19 h 57 UTC. Passe ce delai, redemandez les moi.

$racine = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

$envois = @(
  @{ fichier = "assets\S01E01\decors\StyleJ\D01_StyleJ.png"; media_id = "775d2912-8caa-4cca-b2dd-82f08c2400b4"; url = "https://fast-and-furious-input-prod-20250325165756276100000002.s3.amazonaws.com/user_3GOjCOBu31lBMfhPtMbERCjKAbF/775d2912-8caa-4cca-b2dd-82f08c2400b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYPNTVMCG7DMHYTCK%2F20260823%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T195743Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCmV1LW5vcnRoLTEiRzBFAiEA%2FFcNlNEfmAZEPFf2gvJ%2F2gxGirKWZYEtW5pUCtSX6%2BcCIAK283Yvs%2BcRBXF%2Fm4FXI4%2BVUbRFW6iyRQtnKKkeAdpnKrAFCNj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNTgyODgxNzMwNzAxIgxTddqT5qrLt8IlxHsqhAUw0oF4ANHe%2B%2FlOyPLvXfs7qDYLTEFhyHVJjFce%2FAWp%2F4nZl9d1TksaNZGHNi%2BEh9bFqaOlCITUc1DnunOJ%2FQAOR5CAPGQ%2BwXS%2BndZNv0mdrHaueFDlNuBT0V7cJ%2BLRlSTIttgys1oYvry%2BGZ8Zi6lZ1tji6pygBnC7H3tfL6YUc1X1OEPxt3%2FmwOtOuG8FQXfvrcLqJwsA0tC82BeVC1bQADJAu3mMnznMpGtxwQ2SSmx0S6qAG1zLeJWyEwgFt8eKQ4wtZiCt%2FAKw8ZNLudlUomiBQlkr%2BXco3eg3k8MlOOgJmjEVBo0NKWRWroeg4RBCbYSMLSPMzysQTEc4LVdvIXBnwZKc%2FWucglEq%2FPQtuVWayJnfRmrt4h9tNbUCI0jhAMhrs6ZcT8g2EqrOJz%2BCFb8Aw3tLcN%2FVz5bqz4kPzmEMusW8SXwgLafQr1V%2B1Cft3Vt3bAScdtbfI9ygpo5bStByyR2AgIYy00iVKuU9%2FCO%2FbXl5TWgngFRCn6nfaVxPnByuWciCYfjqnvLrqAehwEEVvchjVoNxX%2BKW13XCBmnEIEERElLFYuQMgbipvgNvvNK8pFQO1rFlzpUuEyd4g3l92smPb7oW0JsHTe2DwU5jSfu8xMWoAN%2B%2FbNcCyDWS4FkCJSsBUlBuO2Pa6yXLXPamF0%2ByWH5VGeClCu7MG8AM2OB7kBjc7xP%2F8GCQrTwBYZCVI8XCF7T%2BnODoLaJhwssq%2FYClEAijibSQ%2FecOSh6BrBipGlXiBEMamvPk0uJPDhGE2fCes4gcnIMxig5FBuaZu3uJp%2FddW%2F0HsH0DnxjB9r8hsIyNSVrOfPEZK9B5MkEWIobbSQ6wb8xWXWbnTNvviDDUk6zUBjqQASvS12YxFWX6Qxi%2FwKi2Gu6QEjLLUsQwUc179Q2Md9KX2jDRtg%2F4vREZCRBss2fBdIa6JeIO0iGvUs0FkYSqMFEgdgkYUx%2FaOrx43eSN1nJXFA%2BjcSM1yA1JKDe30jS1XwuWqiG8vAkZBVPgmsG9cYedvnSPumK4VVVbzZwkJf8Bp0o2LNC%2Bpvm5Qr%2BOzQcmxA%3D%3D&X-Amz-Signature=957763644f416ddde428c64e114c4bfd33c8389df4ba35894d25f75b1420458f" },
  @{ fichier = "assets\S01E01\decors\StyleK\D01_StyleK.png"; media_id = "b0b4fffb-47eb-489a-9b28-68304d66e4c2"; url = "https://fast-and-furious-input-prod-20250325165756276100000002.s3.amazonaws.com/user_3GOjCOBu31lBMfhPtMbERCjKAbF/b0b4fffb-47eb-489a-9b28-68304d66e4c2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYPNTVMCGXAQU5FHY%2F20260823%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T195743Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCmV1LW5vcnRoLTEiSDBGAiEAlKivO7Keya2ArPVzK1UOTYtKJn2ap7g%2BI09F%2B5KCcxkCIQDcal0qn%2FJbWbXlijZ7swc3EKEHMKA24k3R95gxYrKtvSqwBQjY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU4Mjg4MTczMDcwMSIMnFV0rpIKbQ7GLuSJKoQFjFceE8IaQEB56knNOhsQ7MnYjJ6uTfAf%2FufECg1wM3ruX%2Bj1%2BfAmEhc6doqgaJoeZJvxE5aAq%2Fh2XrU2TarQ9S1rb1pTH4V8d4NIcqj%2FsNCu8JA0XILI5zm9xyhsWc6pkUNfweY32M57BqI4Y2n4rS%2FJkJjMHAq7mYE7hKdASN3KuCpDYxgcXEXKNYGSwEew6iu8HSoekk2ZigUSt9Q7KdhSXl%2F9Ff00khlzUBbuh%2Fsv2V5kOpiGp4gLsbOcbNHEwbNqebYZsZwIWIo1TDYZWzp7WL6OrYFFlnS8zfmgsYDkh5xeHNSWIf9X8Yrr0WyEMCCejvweufky0jjII6Qi%2FAjdWYmGZwWR1RCGWPcGyAdmJJFoUuydY9Om1L3McCWLP6nthmne2ids892ETC%2FZO2Vh5MPha6kTqJ4y%2FGkGnWZWpadLcrZGnoZXgW2p26NocJtsG8hF9BCirqDcdkdczas3gTQgnBssZxr8rCA0nJ5fsrrdVUQiOZ7dIKxAN3xrorLJghNDU0bkzhJwNXf4DUgbbLP9iTxyN%2FQuQOypeDouZ8nGJLDAQ1I9n5B0vKW1bB2%2F7BxH5QegqDJQfijhWzoNawNKFpaMXjI8eYn9MoAAxPEQXraF8c5vgCRChDHupYCqLUZKRPQAlKF8d3mpye0Y%2B8cy%2FyMw89WTh38xu8g7bEm6YFfiC4Let504ZG7PqIHvnXDgNh6fOZSulGyu6q0yT%2BvjFTtoG5%2B%2FUjWLPH%2B2n1ZZvyDh5hXHEE4Mud7HqAkGjxR4T9pwqqZ%2BqYpTyPYai2ilci8eL%2F86xKCwQRr7qBZm7aDg3CefQ7dQlrDEf1W%2FmA69iQD3dFNfsK2F%2FB%2FKOhkwwJOs1AY6jwE8kCDl33nRv%2Fj1TEvSraIuomxMfeOaqHXkzbLGS6VktlTjIEu5QB4Crd2X9B9YALhHgG490dGJrtr9Hkm4KAesP2Og8JCUbHjbo529K8xK1ngSL%2FaipaHhkjRa4nnVCkprfmCCI6DugmNcSHcm2%2BQoS%2FwMBVCoi4sXLYgY2i%2FB1O%2FV1qsTFNtPuAD0l3YulQ%3D%3D&X-Amz-Signature=da929891d958e8214eb012902f0d88467ab1e40991ac87cd7520e8ac6edb2245" }
)

foreach ($e in $envois) {
  $chemin = Join-Path $racine $e.fichier
  Write-Host "-> $($e.fichier)  ($([math]::Round((Get-Item $chemin).Length/1MB,1)) Mo)"
  try {
    Invoke-WebRequest -Uri $e.url -Method Put -InFile $chemin -ContentType "image/png" -UseBasicParsing -TimeoutSec 300 | Out-Null
    Write-Host "   envoye, media_id $($e.media_id)" -ForegroundColor Green
  } catch {
    Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red
  }
}

Write-Host ""
Write-Host "Termine. Dites le moi : je confirme les deux media_id cote Higgsfield et je lance les 60 images."
