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

Install Spec Kit if it is not already available:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Verify:

```bash
specify --version
```

Initialize Spec Kit inside each target project with the correct agent integration:

```bash
specify init <project-name> --integration <agent>
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

The command asks intake questions, audits the static source, creates planning artifacts, initializes Spec Kit, and stops before implementation unless explicitly approved.

## How It Works

1. The command routes to `SKILL.md`.
2. `SKILL.md` loads the `developer-wordpress-from-html` workflow.
3. The workflow checks Spec Kit.
4. The workflow audits the source HTML.
5. The workflow generates planning artifacts.
6. The workflow stops before implementation unless approved.

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

## Output Artifacts

The workflow creates durable project state for handoff between agent sessions:

```text
stock/
.html-to-sage/
  INTAKE.md
  PAGES.md
  HTML-AUDIT.md
  SECTION-MAP.md
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
