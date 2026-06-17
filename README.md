# HTML to WordPress Converter

Reusable agent skill repository for planning static HTML/CSS/JS website conversions into WordPress Sage themes with ACF Blocks.

This package is built on top of the real GitHub Spec Kit project: <https://github.com/github/spec-kit>. Spec Kit is the foundation; this repository is the WordPress/Sage/ACF specialization layer.

## Layers

1. **Spec Kit Core**: constitution, specify, clarify, plan, tasks, analyze, implement.
2. **HTML-to-Sage WordPress Extension**: source audit, `stock/`, Sage setup, ACF mapping, CPT/taxonomy decisions, migration planning, visual QA.
3. **Agent Adapters**: Claude Code commands, Codex skill files, and generic `SKILL.md` instructions.

## Install Spec Kit

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Verify:

```bash
specify --version
```

Initialize in a target project:

```bash
specify init <project-name> --integration <agent>
```

Use the real Spec Kit commands:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Codex skill mode may expose `$speckit-constitution`, `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, and `$speckit-implement`.

## Primary Command

```text
/developer-wordpress-from-html
```

The command asks intake questions, audits the static source, creates planning artifacts, initializes Spec Kit, and stops before implementation unless explicitly approved.

## Non-Negotiable Rule

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Visual mismatch is a failed task.

## Enterprise Rules

Every agent must read `references/enterprise-html-to-acf-rules.md` before planning or implementation. It prevents common failures: one giant block, unowned global CSS/JS, unjustified CPTs, dashboard-only ACF fields, edited `stock/` files, removed classes/hooks, casual packages, unpaginated queries, full-size card images, raw ACF output, and incomplete responsive/hover/animation QA.


