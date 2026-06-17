---
name: html-to-wordpress-acf-block-mapper
description: Map static HTML sections to ACF Block contracts with code-owned ACF fields, frontend templates, SCSS files, optional JS modules, editor preview behavior, and mandatory visual parity checklists.
---

# ACF Block Mapper

Read `../../references/enterprise-html-to-acf-rules.md` and `../../references/full-acf-editability-rules.md` before mapping blocks.

Classify each HTML section. Prefer ACF blocks for editable page sections. Use global template parts for header/footer/navigation. Use reusable components for small repeated UI primitives.

Every ACF block must define:

- registration in `framework/builder/blocks.php`
- fields in `framework/builder/acf-blocks/<block>.php`
- frontend template in `framework/builder/front-end/block-content-<block>.php`
- SCSS in `resources/css/blocks/_<block>.scss`
- optional JS in `resources/js/<block>.js`
- editor preview behavior
- visual parity checklist

Do not create one giant block, bloated unrelated fields, dashboard-only ACF field groups, or templates with hardcoded editable content.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Do not map wrappers, CSS classes, layout containers, animation hooks, or JS hooks into fields just because they exist in the HTML. Keep those in the template unless the editor genuinely needs to control them.

Use `../../templates/acf-block-contract.md` per block and write `.html-to-sage/ACF-BLOCKS.md`.
