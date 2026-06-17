---
name: developer-wordpress-from-html
description: Command workflow for planning and optionally implementing static HTML/CSS/JS website conversion into a WordPress Sage theme using real Spec Kit commands, ACF Blocks, Sage/Acorn/Blade/Vite/SCSS, justified CPTs/taxonomies, stock-folder preservation, and mandatory visual parity.
---

# Developer WordPress From HTML

Use this as `/developer-wordpress-from-html`. It coordinates the full workflow but must keep Spec Kit as the source planning engine.

## Start

1. Ask the mandatory intake questions from `../templates/intake-questions.md`.
2. Confirm these defaults unless the user overrides them:
   - pixel-perfect conversion: yes
   - visual improvements allowed: no
   - all editable content in ACF: yes
   - CPTs only when justified: yes
   - preserve originals in `stock/`: yes
3. Inspect HTML/CSS/JS/assets without modifying originals.
4. Copy originals into `stock/` before any migration work.

## Spec Kit Foundation

Run or instruct the user to run:

```bash
specify --version
```

If unavailable:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Initialize with the current agent integration:

```bash
specify init <project-name> --integration <agent>
```

Then use real Spec Kit commands with the prompts in `../templates/`:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.analyze
```

Only run `/speckit.implement` after explicit user approval.

## Required Persistent State

Create and maintain:

```text
stock/
.html-to-sage/
  INTAKE.md
  HTML-AUDIT.md
  SECTION-MAP.md
  CPT-TAXONOMY-MAP.md
  ACF-BLOCKS.md
  SAGE-SETUP.md
  SPECKIT-RUNS.md
  RISKS.md
  DECISIONS.md
.specify/
specs/
```

## Section Classification

Classify every HTML section as one of:

- ACF Block
- Global template part
- CPT archive/single template
- reusable component

Every ACF block must include registration, code-owned fields, frontend template, SCSS file, optional JS module, editor preview behavior, and a visual parity checklist.

## Stop Conditions

Stop before implementation unless the user explicitly asks for implementation. Treat visual mismatch as failed work.

