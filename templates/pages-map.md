# Pages Map

Apply `references/full-acf-editability-rules.md`.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

## Page: <Page Title>

Original file:

```text
stock/<file>.html
```

Suggested WordPress page title:

```text
<Title>
```

Suggested WordPress slug:

```text
/<slug>/
```

Required ACF block order:

1. `<block-name>`

Block details:

| Order | Block Name | ACF Field Group | Source HTML Section | Template File | SCSS File | JS File |
|------|------------|-----------------|---------------------|---------------|-----------|---------|

Required CPT dependencies:

- None unless justified.

Editor instructions:

- Create the WordPress page with the suggested title and slug.
- Add blocks in the listed order.
- Fill each block using the mapped ACF fields.
- Do not manually paste HTML into the editor.
