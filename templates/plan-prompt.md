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

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Apply `references/enterprise-html-to-acf-rules.md` and `references/full-acf-editability-rules.md`. The plan must include PAGES, ASSET-MAP, JS-BEHAVIOR-MAP, PERFORMANCE-RISKS, SECURITY-CHECKLIST, and VISUAL-QA artifacts.

Include this table:

| Original HTML Section Selector | Section Purpose | WordPress Target | Block Name | ACF Fields | Editable Fields Count | Hardcoded Allowed? | CPT Needed? | CSS Source | JS Source | Visual Match Risk | Notes |
|--------------------------------|-----------------|------------------|------------|------------|-----------------------|--------------------|-------------|------------|-----------|-------------------|-------|


