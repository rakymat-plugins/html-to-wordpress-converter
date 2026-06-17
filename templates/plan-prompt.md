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

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, and visual hierarchy unless the user explicitly approves a change.

Include this table:

| HTML Section | WordPress Target | ACF Fields | CPT Needed? | CSS Source | JS Source | Visual Match Risk |
|-------------|------------------|------------|-------------|------------|-----------|-------------------|

