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
```

For Codex skill mode, use:

```text
$html-to-wordpress-converter
```

## Non-Negotiable Rule

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Treat any visual mismatch as a failed task.

## Required Spec Kit Behavior

Before producing planning artifacts, verify Spec Kit is available:

```bash
specify --version
```

If unavailable, install the real Spec Kit CLI:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then initialize Spec Kit in the target project using the current agent integration:

```bash
specify init <project-name> --integration <agent>
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

Ask these questions before planning:

- Should the conversion be pixel-perfect? Default: yes.
- Are visual improvements allowed? Default: no.
- Should all editable content be in ACF? Default: yes.
- Are CPTs allowed only when justified? Default: yes.
- Should original files be preserved in `stock/`? Default: yes.

Also collect project name, theme name, WordPress path, one-page or multi-page scope, HTML files, editor flexibility, reusable sections, possible CPTs, taxonomies, forms, multilingual needs, CSS framework, JS libraries, animation requirements, SEO migration, admin UX expectations, and whether the user wants planning only or implementation.

## Resource Routing

- Read `developer-wordpress-from-html/SKILL.md` for the end-to-end command.
- Read `references/enterprise-html-to-acf-rules.md` before any planning, mapping, package decision, implementation, or QA work.
- Read `references/sage-theme-architecture.md` before designing the theme structure.
- Read `references/acf-block-rules.md` before mapping sections into ACF blocks.
- Read `references/wordpress-cpt-taxonomy-rules.md` before proposing CPTs or taxonomies.
- Read `references/qa-visual-match-rules.md` before implementation or final QA.
- Use `scripts/workflow.py --help` for safe local audit/setup artifact generation.

## Implementation Gate

Do not start implementation until Spec Kit constitution, spec, clarification notes, plan, tasks, and analysis exist or the user explicitly accepts a smaller workflow. Stop after planning unless the user explicitly asks to implement.

Apply the enterprise rules from `references/enterprise-html-to-acf-rules.md` to every `SKILL.md`, template, constitution prompt, plan prompt, tasks prompt, analyze prompt, and implementation gate.

