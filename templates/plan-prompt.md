# Spec Kit Plan Prompt

Use `/speckit.plan` or `$speckit-plan`.

Plan the technical conversion using Sage, Acorn, Blade, Vite, SCSS, ACF Pro, and a framework layer:

```text
framework/
  builder/
    acf-blocks/
    front-end/
    blocks.php
    index.php
  post-type/
  taxonomies/
  custom-fields/
  actions/
  hooks/
  utilities/
resources/
  css/
    blocks/
    layout/
    components/
    common/
  js/
  views/
```

The plan must include Sage installation using `composer create-project roots/sage <theme-name>`, Vite asset pipeline, Blade templates, ACF Pro programmatic fields, SCSS modular migration, JS module migration, CPT/taxonomy modeling only when justified, and QA gates.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Do not over-dynamicize the DOM: wrappers, classes, layout containers, animation hooks, and JS hooks should stay in templates unless the editor explicitly needs to control them.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Apply `references/enterprise-html-to-acf-rules.md`, `references/full-acf-editability-rules.md`, `references/media-library-seeding-rules.md`, and `references/global-template-parts-rules.md`. The plan must include PAGES, GLOBAL-TEMPLATE-PARTS, ASSET-MAP, MEDIA-LIBRARY-SEED, JS-BEHAVIOR-MAP, PERFORMANCE-RISKS, SECURITY-CHECKLIST, and VISUAL-QA artifacts.

The plan must include a WordPress Media Library seed/import strategy for all original client-editable images, icons, logos, background images, videos, documents, and galleries. Templates and ACF previews must use attachment data or seeded field values, not permanent hardcoded `stock/` or theme asset URLs for editable media.

Header, footer, navigation, mobile menus, global CTAs, and site-wide repeated UI should become Sage template parts/layout partials by default. Use WordPress menus, ACF options pages, Customizer/theme options, or approved plugins for editable global data. Do not turn them into page ACF blocks unless the user explicitly approves page-level editor control.

The plan must state that header, footer, navigation, announcement bars, mobile sticky actions, schema, and other global site UI render by default from Sage layout partials and are editable through global options, menus, theme settings, Customizer, or approved plugins.

The plan must state that global options fields are optional when defaults/fallbacks exist. Header/footer/logo/contact/schema fields should not block saving the options page merely because one link, logo, footer item, or schema value is empty.

The plan must keep page-owned ACF block order separate from global site chrome. If a header/footer/nav appears in the original HTML file, map it in `GLOBAL-TEMPLATE-PARTS.md`, not in the page ACF block order, unless explicit page-level control was approved and documented in `DECISIONS.md`.

The plan must include a final WordPress clone-readiness phase. The phase must verify that the theme can be cloned into `wp-content/themes/<theme-slug>` and activated, with valid `style.css`, `functions.php`, render templates or verified Sage/Acorn routing, documented required plugins, documented install/build commands, and ignored local agent/skill/cache/dependency folders.

The plan must explicitly distinguish the generated WordPress theme repo/folder from the reusable skill repo. It must state that `html-to-wordpress-converter` is a skill repository and must not be cloned or copied into `wp-content/themes`. If a WordPress admin screen shows a broken theme named `html-to-wordpress-converter`, the remediation is to delete that wrong folder from `wp-content/themes` and install the actual generated theme folder.

The plan must include a `ready-pages/` deliverable: one `.md` file per WordPress page containing paste-ready Gutenberg ACF block comments in the exact page block order.

The plan must include this media seed table in `.html-to-sage/MEDIA-LIBRARY-SEED.md`:

| Original Stock Path | Media Type | WordPress Attachment Target | Used By | ACF Field/Option/CPT Field | Default Value Strategy | Alt/Title Source | Required? | Notes |
|---------------------|------------|-----------------------------|---------|----------------------------|------------------------|------------------|-----------|-------|

Include this table:

| Original HTML Section Selector | Section Purpose | WordPress Target | Block Name | ACF Fields | Editable Fields Count | Hardcoded Allowed? | CPT Needed? | CSS Source | JS Source | Visual Match Risk | Notes |
|--------------------------------|-----------------|------------------|------------|------------|-----------------------|--------------------|-------------|------------|-----------|-------------------|-------|

Also include this global-template table when global site UI exists:

| Source Selector | Element | WordPress Target | Template Part Path | Editable Data Source | ACF Options Fields | Menu Location | CSS Path | JS Path | Appears On | Explicit Page-Level Control Approved? | Visual Match Risk | Notes |
|-----------------|---------|------------------|--------------------|----------------------|--------------------|---------------|----------|---------|------------|---------------------------------------|-------------------|-------|


