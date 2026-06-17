#!/usr/bin/env sh
set -eu

echo "Recommended install:"
echo "  npx skills add yousefabdallah171/html-to-wordpress-converter"
echo ""
echo "Running manual fallback installer..."

TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills/html-to-wordpress-converter"
mkdir -p "$(dirname "$TARGET_DIR")"
cp -R "$(dirname "$0")" "$TARGET_DIR"
echo "Installed html-to-wordpress-converter to $TARGET_DIR"
echo "Invoke the skill with:"
echo "  /developer-wordpress-from-html"
echo "Install Spec Kit separately if needed:"
echo "  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"
