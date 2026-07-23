#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const HOME = os.homedir();
const CWD = process.cwd();

const checks = [
  ["Claude command", path.join(HOME, ".claude", "commands", "developer-wordpress-from-html.md")],
  ["Claude alias", path.join(HOME, ".claude", "commands", "html-to-wordpress.md")],
  ["Claude alias", path.join(HOME, ".claude", "commands", "html-to-sage.md")],
  ["Codex main skill", path.join(HOME, ".codex", "skills", "html-to-wordpress-converter", "SKILL.md")],
  ["Codex command skill", path.join(HOME, ".codex", "skills", "developer-wordpress-from-html", "SKILL.md")],
  ["Codex alias skill", path.join(HOME, ".codex", "skills", "html-to-wordpress", "SKILL.md")],
  ["Codex alias skill", path.join(HOME, ".codex", "skills", "html-to-sage", "SKILL.md")],
  ["Cursor skill", path.join(HOME, ".cursor", "skills", "html-to-wordpress-converter", "SKILL.md")],
  ["Gemini skill", path.join(HOME, ".gemini", "skills", "html-to-wordpress-converter", "SKILL.md")],
  ["Project Claude command", path.join(CWD, ".claude", "commands", "developer-wordpress-from-html.md")],
  ["Project Codex skill", path.join(CWD, ".codex", "skills", "html-to-wordpress-converter", "SKILL.md")],
];

function present(filePath) {
  try {
    fs.accessSync(filePath);
    return true;
  } catch {
    return false;
  }
}

console.log("html-to-wordpress-converter install verification");
console.log("");

let found = 0;
for (const [label, filePath] of checks) {
  const ok = present(filePath);
  if (ok) found += 1;
  console.log(`${ok ? "OK " : "MISS"} ${label}: ${filePath}`);
}

console.log("");
console.log("Available commands:");
console.log("  /developer-wordpress-from-html");
console.log("  /html-to-wordpress");
console.log("  /html-to-sage");
console.log("  $developer-wordpress-from-html");
console.log("  $html-to-wordpress");
console.log("  $html-to-sage");
console.log("");

if (found === 0) {
  console.log("No registered files were found.");
  console.log("Troubleshooting:");
  console.log("  1. Re-run: npx skills add rakymat-plugins/html-to-wordpress-converter");
  console.log("  2. Restart your agent.");
  console.log("  3. Claude fallback: copy commands/*.md into ~/.claude/commands/");
  console.log("  4. Codex fallback: copy developer-wordpress-from-html/SKILL.md into ~/.codex/skills/developer-wordpress-from-html/SKILL.md");
  console.log("  5. Generic fallback: say 'Use the html-to-wordpress-converter skill and run developer-wordpress-from-html.'");
} else {
  console.log(`Found ${found} registration target(s). Restart your agent if commands are still hidden.`);
}

