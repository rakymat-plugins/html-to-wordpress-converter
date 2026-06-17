# Sage Theme Architecture

The converted theme must use Sage with Acorn, Blade, Vite, SCSS, and ACF Pro.

The delivered theme must also be WordPress clone-ready: cloning the repository or theme folder into `wp-content/themes/<theme-slug>` and activating it must not fail because of missing theme entry files or undocumented dependencies.

Required root files:

```text
style.css        WordPress theme header
functions.php    Composer/autoload and theme bootstrap
index.php        minimum WordPress template fallback
README.md        install commands, required plugins, page/block structure
composer.json    PHP dependencies when Sage/Acorn is used
package.json     frontend build scripts when Vite/SCSS/JS are used
```

When Sage/Acorn routing cannot be verified in the current environment, add standard WordPress template fallbacks such as:

```text
header.php
footer.php
front-page.php
page.php
```

These fallbacks may delegate to shared render helpers, but they must preserve the same header/footer/global UI behavior and avoid hardcoded client-editable content.

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
resources/views/partials/mobile-navigation.blade.php optional
resources/views/partials/global-cta.blade.php optional
resources/css/layout/_header.scss
resources/css/layout/_footer.scss
resources/js/header.js optional
resources/js/navigation.js optional
resources/js/footer.js optional
```

Do not create normal page ACF blocks for header/footer/navigation unless the user explicitly wants page-level editor control. Use WordPress menus, ACF options pages, theme options, Customizer, or approved plugins for editable global data. Do not duplicate that global data in page-local fields.

Each block is a feature unit:

```text
framework/builder/acf-blocks/<block>.php
framework/builder/front-end/block-content-<block>.php
resources/css/blocks/_<block>.scss
resources/js/<block>.js
```
