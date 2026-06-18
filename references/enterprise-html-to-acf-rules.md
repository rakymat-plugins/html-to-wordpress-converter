# Enterprise HTML to ACF Rules

This reference is mandatory for every HTML-to-Sage WordPress conversion. Read it before planning, mapping blocks, modeling CPTs, migrating CSS/JS, implementing, or writing final QA.

Also read `full-acf-editability-rules.md` before mapping content to fields or deciding whether any content can remain hardcoded.

Also read `media-library-seeding-rules.md` before planning asset migration, ACF image/file/gallery fields, default media values, or final QA.

Also read `global-template-parts-rules.md` before mapping header, footer, navigation, global CTA, or any site-wide repeated UI.

## Non-Breakable Rules

The original HTML is the visual source of truth.

Never flatten all HTML into one giant ACF block, put all CSS into `app.scss`, put all JS into `app.js` without ownership, create CPTs without justification, hardcode editable content inside templates, hardcode client-editable media from `stock/` or theme asset URLs, edit files inside `stock/`, remove classes needed for styling, rename classes randomly, change spacing/typography/colors/image ratios/animations/breakpoints/layout, replace working static behavior with worse WordPress behavior, depend on manual-only WordPress admin setup, create ACF fields only from the dashboard, use Elementor/WPBakery/page builders, create bloated blocks with 40 unrelated fields, load sliders or animation libraries globally if used by only one block, query all posts without pagination, use `get_posts(-1)` for public sections, load full-size images when thumbnails are enough, ignore escaping/sanitization, or ignore responsive behavior.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

## Required ACF Block Structure

Every block must follow this structure:

```text
framework/builder/acf-blocks/{block-name}.php
framework/builder/front-end/block-content-{block-name}.php
resources/css/blocks/_{block-name}.scss
resources/js/{block-name}.js optional
```

Every block must be registered in `framework/builder/blocks.php` with name, title, description, render callback, category, icon, keywords, supports, mode if needed, and `enqueue_assets` only if block-specific assets are required.

Use a shared render callback pattern unless there is a real reason not to:

```php
function theme_acf_block_render_callback($block, $content = '', $is_preview = false, $post_id = 0) {
    $slug = str_replace('acf/', '', $block['name']);
    $template = locate_template("framework/builder/front-end/block-content-{$slug}.php");

    if ($template) {
        include $template;
    }
}
```

## Required ACF Field Rules

Every ACF field group must be registered in code with `acf_add_local_field_group`.

Field keys must be unique and stable:

```text
group_{block_name}
field_{block_name}_{field_name}
```

Define only fields needed by that section. Use WYSIWYG only when rich editing is actually required. Do not use flexible content unless explicitly justified. Do not create one universal section-builder field that destroys structure.

Every ACF block must include editor notes covering what the block controls, recommended image dimensions, max repeater count when relevant, button/link behavior, and any visual parity dependency on item count.

## HTML Content Mapping

Classify HTML as editable content, structural markup, behavior hooks, or global elements.

Editable content becomes ACF fields. Structural markup stays in templates. Behavior hooks must be preserved. Global elements become template parts unless the user explicitly wants editor control inside page content.

Headers, footers, navigation, mobile menus, global CTAs, and repeated site-wide UI should become Sage template parts/layout partials by default. Their editable data should come from WordPress menus, ACF options pages, Customizer/theme options, or approved plugins, not page-local ACF blocks.

Do not over-dynamicize everything. Not every div needs a field.

Client-editable images, icons, logos, background images, videos, documents, and galleries must be imported or seedable into the WordPress Media Library and referenced through ACF attachment/file/gallery fields, options, CPT fields, menus, or documented WordPress data. Technical non-editable decorative assets may stay in theme resources.

## CPT Decision Rules

CPTs are allowed only when content is reused across pages, needs its own URL, needs archives, needs filtering/searching, needs categories/tags, is managed regularly by non-technical editors, or is too large for a page-local repeater.

Examples:

- 3 testimonials only on homepage: ACF repeater
- many testimonials reused across pages: CPT
- page-specific FAQ: ACF repeater
- searchable knowledge base: CPT
- simple service cards: ACF repeater
- services with single pages: CPT
- small leadership section: repeater
- full team directory: CPT
- products/projects/news/events: usually CPTs

Document every CPT decision in `.html-to-sage/CPT-TAXONOMY-MAP.md` with reason, fields, taxonomies, archive route, single route, admin labels, and query performance notes.

## Performance Rules

Never load everything globally.

CSS belongs in `common/`, `layout/`, `components/`, or `blocks/` according to ownership. Section-specific styles go in `resources/css/blocks/_<block>.scss`.

JS belongs in block-specific modules when behavior is block-owned. Initialize only when the block exists. Avoid global document query spam, duplicate slider initialization, inline JS, and huge animation libraries unless already required and approved.

Use `wp_get_attachment_image()` where possible, request correct image sizes, preserve aspect ratio, lazy load below-the-fold images, avoid full-size images in cards/grids, and document recommended image sizes per block.

Never use `posts_per_page => -1` on public pages unless justified. Paginate archives and listings, use `WP_Query` responsibly, cache expensive queries if needed, and avoid N+1 post meta calls.

Enqueue third-party libraries only when needed. Do not bundle unused original JS libraries. Remove dead CSS after visual matching. Build with Vite and verify `public/build/manifest.json`.

## Security Rules

Escape every template output:

- `esc_html()` for plain text
- `esc_attr()` for attributes
- `esc_url()` for URLs
- `wp_kses_post()` for trusted rich text
- `wp_get_attachment_image()` for images where possible

Never echo raw ACF fields unless intentionally using `wp_kses_post()`.

Custom forms must use nonces, sanitize input, validate server-side, and never expose secrets in theme files.

## Scalability Rules

The generated theme must be maintainable across 100+ websites. Use consistent naming, keep one responsibility per block, document every block contract, keep reusable helpers in `framework/utilities/`, prefix or namespace global functions, keep block templates small, split repeated UI into partials/components, keep `stock/` read-only, keep `.html-to-sage/` artifacts updated, and keep Spec Kit artifacts as source of truth.

Do not create project-specific hacks in generic templates, hardcode client names everywhere, create unbounded repeaters without notes, mix block logic with CPT registration, mix CSS for unrelated sections, or create undocumented magic behavior.

## Package Rules

Before adding any package, ask whether it is already used in the original HTML, needed for more than one block, replaceable by native CSS/JS, maintained, bundle-size appropriate, and compatible with WordPress/Sage/Vite.

Allowed by default: ACF Pro, Sage/Acorn dependencies, Vite, SCSS. Bootstrap, jQuery, Slick, Swiper, and GSAP are allowed only if the project already uses them or the user approves and the decision is documented.

Write all package decisions in `.html-to-sage/DECISIONS.md`.

## Visual QA Rules

Every section task is incomplete until desktop, tablet, mobile, hover states, animations, image ratios, spacing, typography, section order, assets, console, and links are checked.

If Playwright or browser screenshots are available, create screenshot comparison tasks.

Visual mismatch is a blocker, not a minor issue.

## Required Artifacts

The skill must generate or update:

```text
.html-to-sage/HTML-AUDIT.md
.html-to-sage/SECTION-MAP.md
.html-to-sage/ACF-BLOCKS.md
.html-to-sage/CPT-TAXONOMY-MAP.md
.html-to-sage/GLOBAL-TEMPLATE-PARTS.md
.html-to-sage/ASSET-MAP.md
.html-to-sage/MEDIA-LIBRARY-SEED.md
.html-to-sage/JS-BEHAVIOR-MAP.md
.html-to-sage/PERFORMANCE-RISKS.md
.html-to-sage/SECURITY-CHECKLIST.md
.html-to-sage/VISUAL-QA.md
.html-to-sage/DECISIONS.md
```

Each artifact must be useful for continuing in a new agent session.
