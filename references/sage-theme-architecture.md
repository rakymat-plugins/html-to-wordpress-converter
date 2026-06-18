# Sage Theme Architecture

The converted theme must use Sage with Acorn, Blade, Vite, SCSS, and ACF Pro.

The delivered theme must also be WordPress clone-ready: cloning the repository or theme folder into `wp-content/themes/<theme-slug>` and activating it must not fail because of missing theme entry files or undocumented dependencies.

Only the generated WordPress theme repository/folder belongs in `wp-content/themes`. Never place the reusable skill repository `html-to-wordpress-converter` inside `wp-content/themes`; it is not a theme and WordPress will list it as broken because it has no theme `style.css`.

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
page.php
```

Add `front-page.php` only when there is an explicit technical reason. If it exists, it must render normal WordPress editor/block content and global layout only. It must not rebuild converted homepage sections as hardcoded fallback markup.

These fallbacks may delegate to shared render helpers, but they must preserve the same header/footer/global UI behavior and avoid hardcoded client-editable content.

`index.php` is the minimum safe fallback. It may show a neutral empty-site placeholder or maker credit when there are no posts or page contents, but it must not contain converted client website sections.

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

Do not duplicate ACF block output or converted page sections in `front-page.php`, `page.php`, `index.php`, Blade page templates, CPT templates, or fallback templates. Page-owned sections must be inserted into WordPress pages as ACF blocks and rendered through `the_content()` or the Sage equivalent.

Each block is a feature unit:

```text
framework/builder/acf-blocks/<block>.php
framework/builder/front-end/block-content-<block>.php
resources/css/blocks/_<block>.scss
resources/js/<block>.js
```
