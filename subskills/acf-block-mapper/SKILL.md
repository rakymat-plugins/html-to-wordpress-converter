---
name: html-to-wordpress-acf-block-mapper
description: Map static HTML sections to ACF Block contracts with code-owned ACF fields, frontend templates, SCSS files, optional JS modules, editor preview behavior, and mandatory visual parity checklists.
---

# ACF Block Mapper

Read `../../references/enterprise-html-to-acf-rules.md` before mapping blocks.

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

Use `../../templates/acf-block-contract.md` per block and write `.html-to-sage/ACF-BLOCKS.md`.
