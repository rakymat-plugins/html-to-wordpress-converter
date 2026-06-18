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
- media library seeding rules are referenced in the implementation tasks
- global template part rules are referenced in the implementation tasks
- no meaningful text, image URL, button label, or URL from the original HTML remains hardcoded in templates
- `.html-to-sage/MEDIA-LIBRARY-SEED.md` maps original client-editable images, icons, logos, background images, videos, documents, and galleries to WordPress Media Library attachment targets and ACF/options/CPT field usage
- a repeatable seed/import path exists for original client-editable media, and default ACF/options/CPT media values or editor preview fallbacks resolve from seeded Media Library attachments
- no client-editable media is permanently hardcoded from `stock/` or theme asset paths
- every repeated content group uses an ACF repeater or justified CPT
- `PAGES.md` exists for multi-page websites
- `GLOBAL-TEMPLATE-PARTS.md` exists when header/footer/navigation/site-wide UI is present
- header/footer/navigation are Sage template parts/layout partials unless page-level editor control was explicitly approved
- header/footer/navigation are not included in page ACF block order unless that approval is documented in `DECISIONS.md`
- global editable data is sourced from WordPress menus, ACF options pages, theme options, Customizer, or approved plugins, not duplicated page-local ACF fields
- header navigation and footer link columns use WordPress menus when they are normal label/URL links
- default menus are seeded idempotently when original menus exist, and the seeder does not overwrite editor-assigned menus
- global option fields are limited to real rendered fields or approved integrations; unused, duplicate, speculative, or non-working fields are removed
- every global option field has been changed in the admin and verified on the frontend, or the skipped verification is recorded in `.html-to-sage/FINAL-REPORT.md`
- global options pages can be saved with partial data when defaults/fallbacks exist; header/footer/logo/contact/schema option fields must not be unnecessarily required
- header/footer/navigation markup is not duplicated across page templates, block templates, CPT templates, or partials
- header/footer/navigation CSS and JS live in layout-owned files, not random block-owned files
- WordPress clone-readiness is verified: valid theme `style.css`, bootstrap `functions.php`, render templates or verified Sage/Acorn routing, required plugins in README, install/build commands in README, and ignored local agent/skill/cache/dependency folders
- the reusable skill repository `html-to-wordpress-converter` is not copied into the delivered theme and is not installed as a WordPress theme; a broken WordPress theme named `html-to-wordpress-converter` is a failed readiness check
- `ready-pages/` exists and includes one paste-ready `.md` file per WordPress page with the exact Gutenberg ACF block comments in page order
- default block previews do not appear empty because original media was left outside the WordPress Media Library
- if PHP, Composer, Node, WordPress, or browser checks cannot be run in the current environment, `.html-to-sage/FINAL-REPORT.md` records exactly what was skipped and why

Visual mismatch is a blocker, not a minor issue.
