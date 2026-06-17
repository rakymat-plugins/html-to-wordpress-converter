# Full ACF Editability Rules

Use this reference for every static HTML to Sage + ACF Blocks conversion.

## Core Rule

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

## No Hardcoded Meaningful Content

Never hardcode meaningful content in Blade/PHP templates:

- headings and subheadings
- paragraphs
- button labels and URLs
- images, background images, icons, image alt text, logos, gallery items
- cards, stats, testimonials, FAQs, tabs, accordion items, slider items
- social links, contact info, phone numbers, emails, addresses, map links
- video URLs, badges, labels, menu-like section links
- decorative images if the client may need to replace them

Allowed to stay hardcoded:

- structural wrapper divs
- container/grid classes
- animation and JS hook classes
- ARIA structure when not content-specific
- purely technical classes
- layout markup
- SVG shape markup only when decorative and not content-controlled

If there is doubt, make it editable.

## Field Mirroring

For every HTML section, ACF fields must mirror the original content structure.

Example source section:

- `h1` title
- paragraph
- two buttons
- hero image
- 3 feature cards

Required ACF shape:

- `title`: text
- `description`: textarea or WYSIWYG
- `primary_button`: link
- `secondary_button`: link
- `hero_image`: image
- `cards`: repeater
  - `card_icon`: image/SVG/icon field
  - `card_title`: text
  - `card_text`: textarea
  - `card_link`: optional link

Do not create vague fields such as `content_block_1`, `section_data`, `html_content`, `custom_html`, or `text_1`.

## Original Values

When generating ACF field definitions and block contracts, preserve original HTML values as default/reference values where possible.

Every field map must include:

| Field | Type | Original Value | Source | Required | Notes |
|------|------|----------------|--------|----------|-------|

## Multi-Page Pages Map

If the original HTML website has more than one page, generate `.html-to-sage/PAGES.md`.

For every page, document:

- original HTML file
- suggested WordPress page title
- suggested WordPress slug
- required ACF block order
- block field groups
- source HTML section for each block
- template, SCSS, and JS paths
- required CPT dependencies
- editor instructions

Editors must be able to rebuild the same pages from documented WordPress pages and ACF blocks without pasting HTML into the editor.

## Reuse Across Pages

For multi-page websites:

- detect all HTML pages
- identify shared header, footer, navigation, CTA, repeated hero variants, repeated cards, and repeated contact blocks
- avoid duplicate blocks for the same design pattern
- reuse the same ACF block when layout is the same but content differs
- create variants only when layout differences are real

## Implementation Gate

Before implementation is complete, verify:

- no meaningful text from original HTML remains hardcoded in templates
- no image URL from `stock/` is directly hardcoded in templates
- no button label or URL is hardcoded
- every section has a matching ACF field group
- every repeated content group uses repeater/CPT correctly
- `PAGES.md` exists for multi-page websites
- `ACF-BLOCKS.md` lists all fields for every block
- `SECTION-MAP.md` links every HTML section to a WordPress target
- the WordPress editor can rebuild the same pages using documented block order

Record exceptions in `.html-to-sage/DECISIONS.md`.
