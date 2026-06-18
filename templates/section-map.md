# Section Map

Apply `references/enterprise-html-to-acf-rules.md`, `references/full-acf-editability-rules.md`, `references/media-library-seeding-rules.md`, and `references/global-template-parts-rules.md`.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Client-editable media must be imported or seedable into the WordPress Media Library and referenced through ACF/options/CPT/menu attachment data, not permanent hardcoded `stock/` or theme asset URLs.

Do not map wrappers, classes, layout hooks, animation hooks, or JS hooks into ACF fields unless editor control is explicitly required.

Header, footer, navigation, and other site-wide repeated UI should be classified as global template parts/layout partials by default, not normal ACF blocks.

| Original HTML Section Selector | Section Purpose | WordPress Target | Block Name | ACF Fields | Editable Fields Count | Hardcoded Allowed? | CPT Needed? | CSS Source | JS Source | Visual Match Risk | Notes |
|--------------------------------|-----------------|------------------|------------|------------|-----------------------|--------------------|-------------|------------|-----------|-------------------|-------|
