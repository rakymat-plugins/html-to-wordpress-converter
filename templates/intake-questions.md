# Intake Questions

Apply `references/enterprise-html-to-acf-rules.md`.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Ask only blocking choices before running `workflow.py prepare`:

- WordPress install path? Required before implementation; if unknown, omit `--wp-path` and stop after planning.
- Final Sage theme slug? Default: `mei-sage`.
- May root static source files be moved into `stock/` after preservation? Default: yes.

Apply these defaults automatically unless the user explicitly changes them:

- Pixel-perfect conversion: yes.
- Visual improvements allowed: no.
- All meaningful client-editable content must use ACF fields, ACF options, WordPress menus, approved plugin fields, or justified CPT fields.
- Structural wrappers, container classes, grid classes, animation hooks, JS hooks, ARIA structure, and technical layout markup stay in templates.
- CPTs are allowed only when justified by reuse, archive/single URLs, filtering, search, independent admin workflow, or cross-page management.
- Original files must be preserved in `stock/`.
- Header, footer, navigation, announcement bars, mobile sticky CTAs, schema data, and site-wide UI are global Sage template parts/options/menus by default.
- Page-level editor control over header/footer/navigation: no.
- ACF field groups are code-owned.
- Implementation does not start until the user explicitly approves it.

Record assumptions and answers in `.html-to-sage/INTAKE.md`. If a blocker remains unresolved, write it to `.html-to-sage/BLOCKERS.md` and do not implement.
