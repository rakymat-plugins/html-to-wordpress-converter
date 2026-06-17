# Implementation Gate

Do not run `/speckit.implement` or `$speckit-implement` until the user explicitly approves implementation.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Required before implementation:

- real Spec Kit constitution exists
- real Spec Kit specification exists
- clarification questions are answered or documented
- technical plan exists
- tasks exist and are grouped section by section
- analyze pass is complete
- `stock/` exists and is read-only source material
- `.html-to-sage/` artifacts exist
- each section has an ACF block/template/CPT/component decision
- enterprise rules are referenced in the implementation tasks
- full editability rules are referenced in the implementation tasks
- global template part rules are referenced in the implementation tasks
- no meaningful text, image URL, button label, or URL from the original HTML remains hardcoded in templates
- every repeated content group uses an ACF repeater or justified CPT
- `PAGES.md` exists for multi-page websites
- `GLOBAL-TEMPLATE-PARTS.md` exists when header/footer/navigation/site-wide UI is present
- header/footer/navigation are Sage template parts/layout partials unless page-level editor control was explicitly approved
- header/footer/navigation are not included in page ACF block order unless that approval is documented in `DECISIONS.md`
- global editable data is sourced from WordPress menus, ACF options pages, theme options, Customizer, or approved plugins, not duplicated page-local ACF fields
- header/footer/navigation markup is not duplicated across page templates, block templates, CPT templates, or partials
- header/footer/navigation CSS and JS live in layout-owned files, not random block-owned files

Visual mismatch is a blocker, not a minor issue.
