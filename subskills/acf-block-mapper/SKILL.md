---
name: html-to-wordpress-acf-block-mapper
description: Map static HTML sections to ACF Block contracts with code-owned ACF fields, frontend templates, SCSS files, optional JS modules, editor preview behavior, and mandatory visual parity checklists.
---

# ACF Block Mapper

Classify each HTML section. Prefer ACF blocks for editable page sections. Use global template parts for header/footer/navigation. Use reusable components for small repeated UI primitives.

Every ACF block must define:

- registration in `framework/builder/blocks.php`
- fields in `framework/builder/acf-blocks/<block>.php`
- frontend template in `framework/builder/front-end/block-content-<block>.php`
- SCSS in `resources/css/blocks/_<block>.scss`
- optional JS in `resources/js/<block>.js`
- editor preview behavior
- visual parity checklist

Use `../../templates/acf-block-contract.md` per block and write `.html-to-sage/ACF-BLOCKS.md`.

