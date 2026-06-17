#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const HOME = os.homedir();
const INIT_CWD = process.env.INIT_CWD ? path.resolve(process.env.INIT_CWD) : process.cwd();
const STAMP = new Date().toISOString().replace(/[:.]/g, "-");
const IGNORED_NAMES = new Set([
  ".git",
  ".html-to-sage",
  ".specify",
  "specs",
  "stock",
  "node_modules",
  "vendor",
  "__pycache__",
]);

function exists(filePath) {
  try {
    fs.accessSync(filePath);
    return true;
  } catch {
    return false;
  }
}

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function sameFile(source, target) {
  if (!exists(source) || !exists(target)) return false;
  return fs.readFileSync(source).equals(fs.readFileSync(target));
}

function backupIfNeeded(target) {
  if (!exists(target)) return null;
  const backup = `${target}.backup-${STAMP}`;
  fs.copyFileSync(target, backup);
  return backup;
}

function copyFileSafe(source, target, results) {
  ensureDir(path.dirname(target));
  if (sameFile(source, target)) {
    results.skipped.push(target);
    return;
  }
  const backup = backupIfNeeded(target);
  fs.copyFileSync(source, target);
  results.copied.push(target);
  if (backup) results.backups.push(backup);
}

function copyDirSafe(sourceDir, targetDir, results) {
  if (!exists(sourceDir)) return;
  const entries = fs.readdirSync(sourceDir, { withFileTypes: true });
  for (const entry of entries) {
    if (IGNORED_NAMES.has(entry.name) || entry.name.endsWith(".pyc")) continue;
    const source = path.join(sourceDir, entry.name);
    const target = path.join(targetDir, entry.name);
    if (entry.isDirectory()) {
      copyDirSafe(source, target, results);
    } else if (entry.isFile()) {
      copyFileSafe(source, target, results);
    }
  }
}

function register(homeOrProjectRoot, mode, results) {
  const isHome = mode === "home";
  const skillTargetName = "html-to-wordpress-converter";

  const agentSkillTargets = [
    path.join(homeOrProjectRoot, ".claude", "skills", skillTargetName),
    path.join(homeOrProjectRoot, ".codex", "skills", skillTargetName),
    path.join(homeOrProjectRoot, ".cursor", "skills", skillTargetName),
    path.join(homeOrProjectRoot, ".gemini", "skills", skillTargetName),
  ];

  for (const target of agentSkillTargets) {
    copyDirSafe(ROOT, target, results);
  }

  const commandSourceDir = path.join(ROOT, "commands");
  const claudeCommandTarget = path.join(homeOrProjectRoot, ".claude", "commands");
  copyDirSafe(commandSourceDir, claudeCommandTarget, results);

  const codexAliasSource = path.join(ROOT, ".codex", "skills");
  const codexAliasTarget = path.join(homeOrProjectRoot, ".codex", "skills");
  copyDirSafe(codexAliasSource, codexAliasTarget, results);

  if (isHome) {
    results.homeTargets.push(homeOrProjectRoot);
  } else {
    results.projectTargets.push(homeOrProjectRoot);
  }
}

function main() {
  const results = {
    copied: [],
    skipped: [],
    backups: [],
    homeTargets: [],
    projectTargets: [],
  };

  try {
    register(HOME, "home", results);
    if (INIT_CWD && INIT_CWD !== ROOT && INIT_CWD !== HOME) {
      register(INIT_CWD, "project", results);
    }

    console.log("html-to-wordpress-converter registration complete.");
    console.log("");
    console.log("Available commands:");
    console.log("  /developer-wordpress-from-html");
    console.log("  /html-to-wordpress");
    console.log("  /html-to-sage");
    console.log("  $developer-wordpress-from-html");
    console.log("  $html-to-wordpress");
    console.log("  $html-to-sage");
    console.log("");
    console.log("Next steps:");
    console.log("  1. Restart your agent.");
    console.log("  2. Run /developer-wordpress-from-html or $developer-wordpress-from-html.");
    console.log("  3. If commands do not appear, run: node scripts/verify-install.js");
    console.log("");
    console.log(`Copied/updated files: ${results.copied.length}`);
    console.log(`Already current: ${results.skipped.length}`);
    if (results.backups.length) {
      console.log("Backups created before overwriting:");
      for (const backup of results.backups) console.log(`  ${backup}`);
    }
  } catch (error) {
    console.error("Auto-registration failed.");
    console.error(error && error.message ? error.message : error);
    console.error("");
    console.error("Fallback manual instructions:");
    console.error("  Claude Code: copy commands/*.md into ~/.claude/commands/");
    console.error("  Codex: copy developer-wordpress-from-html/SKILL.md into ~/.codex/skills/developer-wordpress-from-html/SKILL.md");
    console.error("  Generic: tell the agent 'Use the html-to-wordpress-converter skill and run developer-wordpress-from-html.'");
    process.exitCode = 0;
  }
}

main();
