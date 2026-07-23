#!/usr/bin/env sh
set -eu

echo "Recommended install:"
echo "  npx skills add rakymat-plugins/html-to-wordpress-converter"
echo ""
echo "Running manual fallback installer..."

TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills/html-to-wordpress-converter"
mkdir -p "$(dirname "$TARGET_DIR")"
cp -R "$(dirname "$0")" "$TARGET_DIR"
echo "Installed html-to-wordpress-converter to $TARGET_DIR"
if command -v node >/dev/null 2>&1; then
  node "$TARGET_DIR/scripts/register-skill.js"
else
  echo "Node.js not found. Skipping automatic command registration."
fi
echo "Invoke the skill with:"
echo "  /developer-wordpress-from-html"
echo "  /html-to-wordpress"
echo "  /html-to-sage"
echo "Install Spec Kit separately if needed:"
echo "  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"
