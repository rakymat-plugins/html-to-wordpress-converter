$ErrorActionPreference = "Stop"

Write-Host "Recommended install:"
Write-Host "  npx skills add rakymat-plugins/html-to-wordpress-converter"
Write-Host ""
Write-Host "Running manual fallback installer..."

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$targetDir = Join-Path $codexHome "skills\html-to-wordpress-converter"
$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

New-Item -ItemType Directory -Force (Split-Path -Parent $targetDir) | Out-Null
Copy-Item -Recurse -Force $sourceDir $targetDir
Write-Host "Installed html-to-wordpress-converter to $targetDir"
if (Get-Command node -ErrorAction SilentlyContinue) {
    node (Join-Path $targetDir "scripts\register-skill.js")
} else {
    Write-Host "Node.js not found. Skipping automatic command registration."
}
Write-Host "Invoke the skill with:"
Write-Host "  /developer-wordpress-from-html"
Write-Host "  /html-to-wordpress"
Write-Host "  /html-to-sage"
Write-Host "Install Spec Kit separately if needed:"
Write-Host "  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"
