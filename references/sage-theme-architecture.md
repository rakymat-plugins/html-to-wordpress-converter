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

Global site UI belongs in Sage partials and layout assets:

```text
resources/views/partials/header.blade.php
resources/views/partials/footer.blade.php
resources/views/partials/navigation.blade.php
resources/css/layout/_header.scss
resources/css/layout/_footer.scss
resources/js/header.js optional
resources/js/navigation.js optional
resources/js/footer.js optional
```

Do not create normal page ACF blocks for header/footer/navigation unless the user explicitly wants page-level editor control. Use WordPress menus and ACF options/theme options for editable global data.

Each block is a feature unit:

```text
framework/builder/acf-blocks/<block>.php
framework/builder/front-end/block-content-<block>.php
resources/css/blocks/_<block>.scss
resources/js/<block>.js
```
