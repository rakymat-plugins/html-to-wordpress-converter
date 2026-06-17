---
name: developer-wordpress-from-html
description: Command workflow for planning and optionally implementing static HTML/CSS/JS website conversion into a WordPress Sage theme using real Spec Kit commands, ACF Blocks, Sage/Acorn/Blade/Vite/SCSS, justified CPTs/taxonomies, stock-folder preservation, and mandatory visual parity.
---

# Developer WordPress From HTML

Use this as `/developer-wordpress-from-html`, `/html-to-wordpress`, `/html-to-sage`, `$developer-wordpress-from-html`, `$html-to-wordpress`, or `$html-to-sage`. It coordinates the full workflow but must keep Spec Kit as the source planning engine.

## Start

1. Ask only the mandatory blocking intake questions before prepare:
   - WordPress install path, if implementation may follow.
   - Final Sage theme slug, if the default `mei-sage` is not acceptable.
   - Whether to allow the default `stock/` move-source behavior.
   Use defaults for the rest and record them in `.html-to-sage/INTAKE.md`.
2. Read `../references/enterprise-html-to-acf-rules.md` and enforce it throughout the workflow.
3. Read `../references/full-acf-editability-rules.md` and enforce full ACF editability.
4. Read `../references/global-template-parts-rules.md` and enforce template-part handling for header/footer/navigation.
5. Confirm these defaults unless the user overrides them:
   - pixel-perfect conversion: yes
   - visual improvements allowed: no
   - all editable content in ACF: yes
   - CPTs only when justified: yes
   - preserve originals in `stock/`: yes
6. Run the end-to-end prepare helper from the target project root:

   ```bash
   python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-path>
   ```

   If `--wp-path` is unknown, omit it. The command must still generate the planning artifacts and write `.html-to-sage/BLOCKERS.md`; stop and ask the user before implementation.

The prepare helper owns:

- source audit
- `stock/` preservation and root source cleanup
- real Spec Kit check/install/init
- `.specify/memory/constitution.md`
- `specs/<feature>/spec.md`
- `specs/<feature>/plan.md`
- `specs/<feature>/research.md`
- `specs/<feature>/data-model.md`
- `specs/<feature>/quickstart.md`
- `specs/<feature>/tasks.md`
- `.html-to-sage/SPECKIT-ANALYZE.md`
- `.html-to-sage/PREPARE-SUMMARY.md`

## Spec Kit Foundation

The prepare helper calls the Spec Kit setup helper. To rerun only Spec Kit setup:

```bash
python <skill>/scripts/workflow.py speckit --project . --integration codex --skills --install --init
```

This must write `.html-to-sage/SPECKIT-RUNS.md` from real command output.

The helper performs:

```bash
specify --version
```

If unavailable and `--install` is set, it attempts:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Initialize with the current agent integration in the current project:

```bash
specify init --here --force --integration codex --integration-options="--skills"
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

If the current agent session cannot see newly installed `$speckit-*` skills until restart, continue using the generated Spec Kit artifacts from `prepare`; do not fake or skip them.

## Required Persistent State

Create and maintain:

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

## Section Classification

Classify every HTML section as one of:

- ACF Block
- Global template part
- CPT archive/single template
- reusable component

Every ACF block must include registration, code-owned fields, frontend template, SCSS file, optional JS module, editor preview behavior, and a visual parity checklist.

Never flatten the full page into one block, never put all CSS/JS into global files without ownership, never remove behavior hooks/classes randomly, and never hardcode editable content in templates.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Header, footer, navigation, mobile menus, global CTAs, and site-wide repeated UI must be mapped as global template parts/layout partials by default. Use ACF blocks only when the user explicitly wants page-level editor control.

Keep global site chrome out of page ACF block order. Store editable global data in WordPress menus, ACF options pages, theme options, Customizer, or approved plugins, and document those sources in `.html-to-sage/GLOBAL-TEMPLATE-PARTS.md` and `.html-to-sage/DECISIONS.md`.

## Stop Conditions

Stop before implementation unless the user explicitly asks for implementation. If `.html-to-sage/BLOCKERS.md` contains unresolved items, ask the user for those answers and do not implement. Treat visual mismatch as failed work.
