# Sage Theme Architecture

The converted theme must use Sage with Acorn, Blade, Vite, SCSS, and ACF Pro.

Required framework layer:

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
```

Frontend structure:

```text
resources/
  css/
    app.scss
    editor.scss
    blocks/
    layout/
    components/
    common/
  js/
    app.js
  views/
    layouts/
    partials/
    components/
    sections/
```

Each block is a feature unit:

```text
framework/builder/acf-blocks/<block>.php
framework/builder/front-end/block-content-<block>.php
resources/css/blocks/_<block>.scss
resources/js/<block>.js
```

