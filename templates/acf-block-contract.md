# ACF Block Contract

Apply `references/enterprise-html-to-acf-rules.md` and `references/full-acf-editability-rules.md`.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Do not create fields for wrappers, CSS classes, layout containers, animation hooks, or JS hooks unless the user explicitly needs editor control over them.

## Block

- Name:
- Purpose:
- Source HTML section:
- Registration path: `framework/builder/blocks.php`
- Fields path: `framework/builder/acf-blocks/<block>.php`
- Frontend path: `framework/builder/front-end/block-content-<block>.php`
- SCSS path: `resources/css/blocks/_<block>.scss`
- JS path:
- Editor preview behavior:
- Editor notes:
- Recommended image dimensions:
- Max repeater count:
- Visual parity dependencies:

## Fields

| Field | Type | Original Value | Source | Required | Notes |
|-------|------|----------------|--------|----------|-------|

## Repeaters

## Media

## Links and Buttons

## Hardcoded Content Exceptions

Record any content intentionally left hardcoded and the approved reason.

## Visual Parity Checklist

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

- Desktop compared
- Tablet compared
- Mobile compared
- Animation compared
- Typography compared
- Spacing compared
- Colors compared



