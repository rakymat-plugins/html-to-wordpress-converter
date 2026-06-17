$ErrorActionPreference = "Stop"

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$targetDir = Join-Path $codexHome "skills\html-to-wordpress-converter"
$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

New-Item -ItemType Directory -Force (Split-Path -Parent $targetDir) | Out-Null
Copy-Item -Recurse -Force $sourceDir $targetDir
Write-Host "Installed html-to-wordpress-converter to $targetDir"
Write-Host "Install Spec Kit separately if needed:"
Write-Host "uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"

