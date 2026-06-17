---
name: html-to-wordpress-converter
description: Spec Kit-backed workflow layer for converting existing static HTML/CSS/JS websites into WordPress Sage themes with Acorn, Blade, Vite, SCSS, ACF Pro blocks, justified CPTs/taxonomies, stock-folder preservation, and mandatory 100% visual parity. Use when planning or implementing an HTML-to-Sage WordPress conversion, especially with `/developer-wordpress-from-html`, ACF block mapping, Sage setup, or Spec Kit artifacts.
---

# HTML to WordPress Converter

Use this skill to convert static HTML websites into planned, editable WordPress Sage themes. This skill must not imitate Spec Kit. It uses the real GitHub Spec Kit project as the foundation and adds only a WordPress/Sage/ACF specialization layer.

## Architecture

Layer 1: Spec Kit Core
- `constitution`
- `specify`
- `clarify`
- `plan`
- `tasks`
- `analyze`
- `implement`

Layer 2: HTML-to-Sage WordPress Extension
- HTML source audit
- `stock/` backup folder
- Sage installation
- ACF block mapping
- CPT/taxonomy decisions
- CSS/JS/assets migration
- visual parity requirements

Layer 3: Agent Adapters
- Claude Code command files
- Codex skill files
- generic `SKILL.md` instructions

## Primary Command

Use `developer-wordpress-from-html/SKILL.md` for the main workflow. If the user's agent supports slash commands, expose it as:

```text
/developer-wordpress-from-html
/html-to-wordpress
/html-to-sage
```

For Codex skill mode, use:

```text
$html-to-wordpress-converter
$developer-wordpress-from-html
$html-to-wordpress
$html-to-sage
```

Different agents expose commands differently. Claude Code may show slash commands or skills. Codex CLI may show `$command` skills. Generic agents should be told: "Use the html-to-wordpress-converter skill and run developer-wordpress-from-html."

## Non-Negotiable Rule

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Treat any visual mismatch as a failed task.

## Required Spec Kit Behavior

Before producing final planning artifacts, run the end-to-end prepare helper:

```bash
python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-path>
```

If the WordPress path is unknown, omit `--wp-path`; the helper must write `.html-to-sage/BLOCKERS.md`, generate planning artifacts, and stop before implementation.

To rerun only Spec Kit setup, run:

```bash
python <skill>/scripts/workflow.py speckit --project . --integration codex --skills --install --init
```

The helper uses project-local uv paths (`.uv-cache`, `.uv-tools`, `.uv-bin`) and can run `specify` from `.uv-bin` after install when the command is not on `PATH`.

The helper verifies Spec Kit:

```bash
specify --version
```

If unavailable, install the real Spec Kit CLI:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then initializes Spec Kit in the target project using the current agent integration:

```bash
specify init --here --force --integration codex --integration-options="--skills"
```

Use the real Spec Kit commands whenever possible:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Codex skills mode may expose equivalent names such as `$speckit-constitution`, `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, and `$speckit-implement`.

## Mandatory Intake Before Planning

Ask only blocking questions before `prepare`; use defaults for the rest and let `prepare` record/update artifacts.

- WordPress install path, if implementation may follow.
- Final Sage theme slug, if the default is not acceptable.
- Whether root static source files may be moved into `stock/`; default: yes.

Defaults: pixel-perfect yes, visual improvements no, editable meaningful content yes, CPTs only when justified yes, preserve originals in `stock/` yes, header/footer/navigation as global template parts yes, implementation requires explicit approval.

## Stock Behavior

Run the stock helper before migration:

```bash
python <skill>/scripts/workflow.py stock --source . --project . --overwrite --move-source
```

This archives the static website files into `stock/` and removes the old root copies so the root does not keep both the original HTML and the preserved stock source. The helper excludes agent folders, generated artifacts, `.git`, `node_modules`, `vendor`, and the skill repository.

## Resource Routing

- Read `developer-wordpress-from-html/SKILL.md` for the end-to-end command.
- Read `references/enterprise-html-to-acf-rules.md` before any planning, mapping, package decision, implementation, or QA work.
- Read `references/full-acf-editability-rules.md` before mapping content into fields or writing implementation tasks.
- Read `references/global-template-parts-rules.md` before mapping header, footer, navigation, global CTAs, or site-wide repeated UI.
- Read `references/sage-theme-architecture.md` before designing the theme structure.
- Read `references/acf-block-rules.md` before mapping sections into ACF blocks.
- Read `references/wordpress-cpt-taxonomy-rules.md` before proposing CPTs or taxonomies.
- Read `references/qa-visual-match-rules.md` before implementation or final QA.
- Use `scripts/workflow.py --help` for safe local audit/setup artifact generation.

## Implementation Gate

Do not start implementation until `workflow.py prepare` has completed, `.html-to-sage/BLOCKERS.md` has no unresolved implementation blockers, Spec Kit constitution/spec/plan/tasks/analyze artifacts exist, and the user explicitly asks to implement.

Apply the enterprise rules from `references/enterprise-html-to-acf-rules.md` to every `SKILL.md`, template, constitution prompt, plan prompt, tasks prompt, analyze prompt, and implementation gate.

Apply the full editability rules from `references/full-acf-editability-rules.md` to prevent hardcoded client-editable content and to require `.html-to-sage/PAGES.md` for multi-page websites.

Apply the global template part rules from `references/global-template-parts-rules.md` so headers, footers, navigation, and site-wide UI become Sage partials/layout template parts by default, not page ACF blocks. Keep their editable data in WordPress menus, ACF options pages, theme options, Customizer, or approved plugins; do not duplicate global values in page-local ACF fields.

