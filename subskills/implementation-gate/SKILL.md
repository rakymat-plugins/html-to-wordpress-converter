---
name: html-to-wordpress-implementation-gate
description: Approval and QA gate for starting implementation of HTML-to-Sage WordPress conversions only after Spec Kit artifacts exist, tasks are section-by-section, stock is preserved, and visual parity requirements are enforceable.
---

# Implementation Gate

Read `../../references/enterprise-html-to-acf-rules.md`, `../../references/full-acf-editability-rules.md`, `../../references/media-library-seeding-rules.md`, and `../../references/global-template-parts-rules.md` before allowing implementation.

Do not implement until all exist:

- `stock/`
- `.html-to-sage/INTAKE.md`
- `.html-to-sage/PAGES.md` for multi-page websites
- `.html-to-sage/GLOBAL-TEMPLATE-PARTS.md` when header/footer/navigation/site-wide UI exists
- `.html-to-sage/HTML-AUDIT.md`
- `.html-to-sage/SECTION-MAP.md`
- `.html-to-sage/ACF-BLOCKS.md`
- `.html-to-sage/CPT-TAXONOMY-MAP.md`
- `.html-to-sage/ASSET-MAP.md`
- `.html-to-sage/MEDIA-LIBRARY-SEED.md` when the source contains client-editable media
- `.html-to-sage/JS-BEHAVIOR-MAP.md`
- `.html-to-sage/PERFORMANCE-RISKS.md`
- `.html-to-sage/SECURITY-CHECKLIST.md`
- `.html-to-sage/VISUAL-QA.md`
- Spec Kit constitution/spec/plan/tasks/analyze artifacts
- explicit user approval to implement

Implementation gate sentence:

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Fail the gate if any section lacks a comparison method or if a mismatch is accepted without user approval.

Fail the gate if meaningful original content remains hardcoded without a documented user-approved exception.

Fail the gate if client-editable original images, icons, logos, background images, videos, documents, or galleries remain permanent hardcoded theme assets instead of Media Library attachments or documented WordPress data.

Fail the gate if default ACF media fields/previews are empty because original media was not seeded or made restorable from the Media Library.

Fail the gate if header/footer/navigation were converted to page ACF blocks without explicit user approval.

Fail the gate if header/footer/navigation are included in page ACF block order without approval documented in `.html-to-sage/DECISIONS.md`.

Fail the gate if editable global header/footer/navigation data is duplicated in page-local ACF fields instead of WordPress menus, ACF options pages, theme options, Customizer, or approved plugins.

Fail the gate if header navigation or footer link columns are implemented as ACF repeaters when normal WordPress menus can manage them.

Fail the gate if default menus from the original HTML are not seeded idempotently, or if the seeder overwrites editor-assigned menus.

Fail the gate if a theme with a global options page lacks optional menu selector fields for global header/footer menu areas, or if those selectors hardcode menu IDs instead of selecting existing WordPress menus and falling back to Appearance > Menus assignments.

Fail the gate if global option pages contain unused fields, duplicate menu fields, speculative schema/settings fields, icon/class fields without editor need, or fields that do not change the frontend.

Fail the gate if header/footer/navigation markup is duplicated across page templates, block templates, or CPT templates.

Fail the gate if `front-page.php`, `page.php`, `index.php`, Blade page templates, CPT templates, or fallback templates duplicate converted homepage/page sections outside the editor/block content pipeline.

Fail the gate if editing a Home page ACF block in WordPress does not change the frontend Home page.


