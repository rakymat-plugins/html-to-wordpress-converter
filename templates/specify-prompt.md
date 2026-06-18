# Spec Kit Specify Prompt

Use `/speckit.specify` or `$speckit-specify`.

Specify a conversion project that turns an existing static HTML/CSS/JS website into an editable WordPress Sage theme. The original source must be preserved in `stock/`. Each section must be mapped into an ACF block, global template part, CPT archive/single template, or reusable component. The WordPress editor must allow safe content editing through ACF Pro fields while preserving the original frontend appearance.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Client-editable media from the original HTML must be imported or seedable into the WordPress Media Library and referenced through ACF image/file/gallery fields, global options, CPT fields, menus, or documented WordPress data. The implementation must not depend on permanent hardcoded `stock/` or theme asset URLs for editable images, icons, logos, background images, videos, documents, or galleries.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Reusable sections should be reusable where appropriate. CPTs and taxonomies are allowed only when justified by repeatable, reusable, filterable, archiveable, or independently managed content. The skill must enforce `references/enterprise-html-to-acf-rules.md`, `references/full-acf-editability-rules.md`, and `references/media-library-seeding-rules.md`.
