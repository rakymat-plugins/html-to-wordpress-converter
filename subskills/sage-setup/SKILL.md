---
name: html-to-wordpress-sage-setup
description: Sage setup instructions for installing Roots Sage, configuring Acorn/Blade/Vite/SCSS, creating the custom framework layer, verifying build assets, and preparing WordPress theme structure for ACF blocks.
---

# Sage Setup

Use after planning approval, not during planning-only mode unless verification requires it.

Required setup:

```bash
composer create-project roots/sage <theme-name>
npm install
npm run build
```

Verify `public/build/manifest.json` exists. Then create:

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
resources/css/blocks/
resources/css/layout/
resources/css/components/
resources/css/common/
resources/js/
```

Write `.html-to-sage/SAGE-SETUP.md` with commands, results, failures, and manual WordPress requirements.

