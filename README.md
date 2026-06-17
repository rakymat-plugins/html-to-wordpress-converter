# HTML to WordPress Converter

Spec Kit-backed skill for converting static HTML/CSS/JS websites into planned WordPress Sage themes with ACF Blocks.

This repository is not a standalone website converter. It is a reusable agent workflow layer:

- **Spec Kit Core**: constitution, specify, clarify, plan, tasks, analyze, implement.
- **HTML-to-Sage WordPress Extension**: source audit, `stock/`, Sage setup, ACF block mapping, CPT/taxonomy decisions, CSS/JS/assets migration, and visual QA.
- **Agent Adapters**: Claude Code commands, Codex skill files, and generic `SKILL.md` instructions.

## Installation

### Recommended

```bash
npx skills add yousefabdallah171/html-to-wordpress-converter
```

Then restart the agent.

## Commands

Depending on the agent, use one of:

```text
/developer-wordpress-from-html
/html-to-wordpress
/html-to-sage
```

or:

```text
$developer-wordpress-from-html
$html-to-wordpress
$html-to-sage
```

or say:

```text
Use the html-to-wordpress-converter skill.
```

Different agents expose commands differently:

- Claude Code: slash command or skill command
- Codex CLI: skill command may appear as `$command`
- Cursor/Gemini/generic agents: tell the agent to use the `developer-wordpress-from-html` skill

The recommended install path is `npx skills add yousefabdallah171/html-to-wordpress-converter`. Do not manually clone the repository unless you need an advanced/manual setup.

### Advanced / Manual

Use manual installation only when your agent environment does not support `npx skills add`.

macOS/Linux:

```bash
./install.sh
```

Windows PowerShell:

```powershell
.\install.ps1
```

## Spec Kit Requirement

This skill is built on the real GitHub Spec Kit project: <https://github.com/github/spec-kit>.

The skill command should run the bundled helper so `.html-to-sage/SPECKIT-RUNS.md` contains real command output:

```bash
python scripts/workflow.py speckit --project . --integration codex --skills --install --init
```

The helper sets project-local uv paths by default (`.uv-cache`, `.uv-tools`, `.uv-bin`) so restricted Windows user cache folders do not block installation.

Install Spec Kit if it is not already available:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Verify:

```bash
specify --version
```

Initialize Spec Kit inside each target project with the correct agent integration. For Codex skills mode:

```bash
specify init --here --force --integration codex --integration-options="--skills"
```

The workflow uses real Spec Kit commands whenever possible:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Codex skill mode may expose equivalent aliases such as `$speckit-constitution`, `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, and `$speckit-implement`.

## Primary Command

```text
/developer-wordpress-from-html
```

The command asks only blocking intake questions, audits the static source, creates planning artifacts, initializes Spec Kit, and stops before implementation unless explicitly approved.

## How It Works

1. The command routes to `SKILL.md`.
2. `SKILL.md` loads the `developer-wordpress-from-html` workflow.
3. The workflow runs the bundled prepare helper.
4. The helper audits the source HTML and moves preserved static source into `stock/`.
5. The helper checks/installs/initializes real Spec Kit.
6. The helper generates Spec Kit constitution/spec/plan/research/data-model/quickstart/tasks/analyze artifacts.
7. The workflow stops before implementation unless approved.

Preferred planning command:

```bash
python scripts/workflow.py prepare --source . --project . --theme-name mei-sage --wp-path <wordpress-install-path>
```

If the WordPress path is not known yet, omit `--wp-path`. The workflow will generate `.html-to-sage/BLOCKERS.md` and stop before implementation.

Useful prepare options:

- `--copy-source`: preserve source in `stock/` without removing root copies.
- `--skip-stock`: do not copy or move source files.
- `--no-install-speckit`: do not attempt Spec Kit installation.
- `--no-init-speckit`: do not attempt Spec Kit initialization.
- `--no-overwrite-stock`: keep existing files in `stock/`.

## Stock Folder Behavior

The preferred stock command is:

```bash
python scripts/workflow.py stock --source . --project . --overwrite --move-source
```

This preserves static source files under `stock/` and removes the original root copies so the root can become the WordPress/Sage project. The helper excludes `.git`, `.html-to-sage`, `.specify`, agent folders, `node_modules`, `vendor`, and this skill repository.

The `prepare` command runs this behavior automatically by default.

## Troubleshooting: Command Not Showing

If the command does not appear:

1. Restart the agent.

2. Re-run:

   ```bash
   npx skills add yousefabdallah171/html-to-wordpress-converter
   ```

3. Verify install:

   ```bash
   node scripts/verify-install.js
   ```

4. Use direct prompt fallback:

   ```text
   Use the html-to-wordpress-converter skill and run developer-wordpress-from-html.
   ```

5. Manual Claude Code fallback:

   Copy commands from:

   ```text
   commands/
   ```

   into:

   ```text
   ~/.claude/commands/
   ```

6. Manual Codex fallback:

   Copy:

   ```text
   developer-wordpress-from-html/SKILL.md
   ```

   into:

   ```text
   ~/.codex/skills/developer-wordpress-from-html/SKILL.md
   ```

7. Project-local fallback:

   Create:

   ```text
   .claude/commands/developer-wordpress-from-html.md
   ```

   and paste the command router content from `commands/developer-wordpress-from-html.md`.

## Non-Negotiable Rule

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Visual mismatch is a failed task.

## Enterprise Rules

Every agent must read `references/enterprise-html-to-acf-rules.md` before planning or implementation. It prevents common failures: one giant block, unowned global CSS/JS, unjustified CPTs, dashboard-only ACF fields, edited `stock/` files, removed classes/hooks, casual packages, unpaginated queries, full-size card images, raw ACF output, and incomplete responsive/hover/animation QA.

## Header, Footer, And Global UI

Header, footer, navigation, mobile menus, global CTAs, language switchers, search overlays, and other site-wide UI must be mapped to Sage template parts/layout partials by default, not normal page ACF blocks.

Editable global data belongs in WordPress menus, ACF options pages, theme options, Customizer, or approved plugins. Do not duplicate global content in page-local ACF fields unless the user explicitly approves page-level editor control and the decision is documented.

## WordPress Clone Readiness

Final delivery must verify that the theme works when cloned into `wp-content/themes/<theme-slug>` and activated.

The workflow must check or document:

- valid WordPress theme header in `style.css`
- `functions.php` bootstrap
- render templates or verified Sage/Acorn routing
- required plugins and install/build commands in `README.md`
- Home page block order and global header/footer setup in `README.md`
- ignored local agent folders, skill folders, uv caches, dependency folders, and build outputs
- the reusable skill repo `html-to-wordpress-converter` is not placed in `wp-content/themes`; if WordPress shows a broken theme named `html-to-wordpress-converter`, delete that wrong folder and clone the actual generated theme repository instead
- `.html-to-sage/FINAL-REPORT.md` listing checks run and any checks skipped because the environment lacks PHP, Composer, Node, WordPress, or a browser

## Output Artifacts

The workflow creates durable project state for handoff between agent sessions:

```text
stock/
.html-to-sage/
  INTAKE.md
  PAGES.md
  HTML-AUDIT.md
  SECTION-MAP.md
  GLOBAL-TEMPLATE-PARTS.md
  CPT-TAXONOMY-MAP.md
  ACF-BLOCKS.md
  ASSET-MAP.md
  JS-BEHAVIOR-MAP.md
  PERFORMANCE-RISKS.md
  SECURITY-CHECKLIST.md
  VISUAL-QA.md
  SAGE-SETUP.md
  SPECKIT-RUNS.md
  RISKS.md
  DECISIONS.md
.specify/
specs/
```

## Safety

- Never edit files inside `stock/`.
- Never start implementation before planning artifacts exist.
- Never create CPTs without documented justification.
- Never use page builders.
- Never fake Spec Kit artifacts when real Spec Kit can be installed and used.
