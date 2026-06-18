# Analysis / Final Report Template

## Spec Kit Runs

- Constitution:
- Specify:
- Clarify:
- Plan:
- Tasks:
- Analyze:
- Implement:

## Visual Parity Rule

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

## Enterprise Gate

Confirm `references/enterprise-html-to-acf-rules.md` was enforced: no giant catch-all blocks, no unowned global CSS/JS, no unjustified CPTs, no edited `stock/` files, no removed classes/hooks, no casual packages, no unpaginated public queries, no full-size card/grid images, and no raw ACF output.

Confirm `references/full-acf-editability-rules.md` was enforced: no hardcoded meaningful content, every original content item mapped to ACF or justified CPT fields, original HTML values documented, and `PAGES.md` generated for multi-page websites.

Confirm `references/media-library-seeding-rules.md` was enforced: original client-editable media imported or seedable into the WordPress Media Library, `.html-to-sage/MEDIA-LIBRARY-SEED.md` completed, ACF media fields use attachment data, default previews show seeded media or documented fallbacks, and no editable media is permanently hardcoded from `stock/` or theme assets.

Confirm `references/global-template-parts-rules.md` was enforced: header/footer/navigation/global UI mapped to Sage template parts/layout partials by default, editable global data sourced from menus/options/plugins, and `GLOBAL-TEMPLATE-PARTS.md` completed when site-wide UI exists.

Confirm global field minimalism was enforced: header/footer link columns use WordPress menus, default menus are seeded idempotently without overwriting editor-assigned menus, global ACF options contain only rendered/approved fields, and every global option field was verified against the frontend or recorded as skipped.

## Section Results

| HTML Section | WordPress Target | Visual Status | Issues | Approved Changes |
|-------------|------------------|---------------|--------|------------------|

## Block/CPT Summary

## Failed Gates

## Final Decision

Do not mark complete if any visual mismatch remains unapproved.


