# Global Template Parts Rules

Use this reference when mapping headers, footers, navigation, global CTAs, repeated contact strips, language switchers, search overlays, cookie bars, and other site-wide UI from static HTML into Sage.

## Core Rule

Header, footer, navigation, and other site-wide repeated elements should become Sage template parts or layout partials by default, not normal ACF blocks.

This is a hard classification rule for normal website chrome. A header or footer is not a page section just because it appears in the original HTML file. Treat it as global site structure unless the user explicitly asks for page-level insertion, reordering, or per-page variation.

Header, footer, navigation, announcement bars, mobile sticky actions, schema, and other global site UI must render by default from the theme layout on every applicable page. Editors should not need to add a header block or footer block for normal site chrome to appear.

All meaningful global UI content must remain editable through WordPress menus, ACF options pages, theme options, Customizer, or approved plugins. This includes logos, image alt text, brand names, subtitles, navigation links, CTA labels and URLs, phone numbers, emails, addresses, map links, footer columns, legal text, schema/business data, social links, and contact links.

Structural wrappers, layout classes, ARIA structure, animation hooks, and JS hooks stay in the template partials unless the editor explicitly needs control over them.

Use ACF blocks for header/footer only when the user explicitly wants editors to insert, remove, reorder, or vary those elements per page. Most sites should keep them in:

```text
resources/views/partials/header.blade.php
resources/views/partials/footer.blade.php
resources/views/partials/navigation.blade.php
resources/views/partials/mobile-navigation.blade.php optional
resources/views/partials/global-cta.blade.php optional
resources/css/layout/_header.scss
resources/css/layout/_footer.scss
resources/js/header.js optional
resources/js/navigation.js optional
resources/js/footer.js optional
```

## Classification

Classify global HTML as:

- `global template part`: header, footer, nav, mobile menu, global search, global CTA, cookie banner
- `layout partial`: repeated page shell, wrapper, breadcrumb, sidebar shell
- `ACF block`: page-owned reusable section that editors add inside page content
- `component`: small repeated UI piece used by blocks or template parts

Do not classify a site header or footer as an ACF block merely because it contains editable content. Editable global content still belongs to global data sources, not page-local block fields.

The default theme layout should include global partials when they exist:

```text
@include('partials.announcement') optional
@include('partials.header')
@include('partials.footer')
@include('partials.mobile-sticky') optional
@include('partials.schema-local-business') optional
```

## Editable Data

Editable global content should be stored in the right WordPress-owned place:

- navigation links: WordPress menus registered in `app/setup.php`
- logo: Customizer, theme option, ACF options page, or theme setting
- footer contact details: ACF options page or theme options
- social links: ACF options page or options model
- newsletter/form embed: Gravity Forms or approved form plugin
- language switcher: WPML/Polylang/plugin integration
- copyright text: theme option or ACF options field

Template parts render this global data. They should not hardcode client-editable global content.

Do not store global header/footer values in page-level ACF fields. That makes editors repeat the same data on every page and breaks global consistency.

## ACF Options Contract

Use ACF options pages for global editable content when appropriate. Document:

- option page name
- field group key
- field names
- original HTML values
- source selectors
- render locations
- fallback behavior

Recommended artifact:

```text
.html-to-sage/GLOBAL-TEMPLATE-PARTS.md
```

Also document global menu locations and option fields in `.html-to-sage/DECISIONS.md` whenever there is a meaningful choice, such as ACF options page versus Customizer or Gravity Forms versus static newsletter markup.

## CSS and JS Ownership

Header/footer CSS belongs in `resources/css/layout/`, not `resources/css/blocks/`.

Header/footer JS belongs in small layout modules such as `resources/js/header.js`, `resources/js/navigation.js`, or `resources/js/footer.js`. Initialize only when the relevant element exists.

Do not place header/footer behavior inside random block modules.

Do not duplicate header/footer markup in `page.blade.php`, individual page templates, ACF block templates, or CPT templates. Render it through the layout and partial system once.

## Visual Parity

Header/footer template parts must match the original static HTML globally:

- desktop, tablet, and mobile navigation
- sticky behavior
- dropdowns/mega menus
- active states
- hover/focus states
- logo sizing
- menu spacing
- footer columns
- social icons
- form embeds
- responsive collapse behavior
- scroll locking and off-canvas behavior
- search overlay behavior
- language switcher output
- accessibility states such as `aria-expanded`

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

## Anti-Patterns

Never:

- create a `header` ACF block for normal site navigation without explicit user approval
- create a `footer` ACF block for normal site footer without explicit user approval
- hardcode menu links in Blade when WordPress menus are appropriate
- put header/footer CSS in block SCSS files
- duplicate header/footer markup across page templates
- make editors rebuild global navigation on every page
- hide global data in page-local fields
- list header/footer blocks in page block order unless explicit per-page control was approved
- hardcode logos, phone numbers, emails, social URLs, footer column links, newsletter IDs, or legal text when they are client-editable
