# Spec Kit Tasks Prompt

Use `/speckit.tasks` or `$speckit-tasks`.

Generate implementation tasks with these phases:

- Phase 0: Intake and source audit
- Phase 1: Stock folder and project workspace
- Phase 2: Sage theme setup and framework structure
- Phase 3: HTML section mapping
- Phase 4: ACF block contracts
- Phase 5: CPT/taxonomy contracts
- Phase 6: global template parts, CSS/JS/assets migration plan
- Phase 7: WordPress editor/admin UX plan
- Phase 8: visual QA and responsive QA plan
- Phase 9: implementation tasks
- Phase 10: final build/test/deployment checklist

Phase 2 must always include:

- install Sage
- create/verify `style.css` with a valid WordPress theme header
- create/verify `functions.php` with Composer/autoload and theme bootstrap
- create/verify `index.php` and standard WordPress fallback templates when Sage/Acorn routing cannot be verified
- configure `vite.config.js` base path
- `npm install`
- `npm run build`
- verify `public/build/manifest.json` exists
- create `framework/` structure
- create builder loader
- create block registration system
- verify theme boots without fatal errors

For each section, create one task group:

- analyze original HTML
- identify fields
- map all meaningful content to ACF fields or justified CPT fields
- create ACF block registration
- create ACF fields in code
- create frontend template
- migrate SCSS
- migrate JS if needed
- compare visually with original
- fix mismatch until 100% match

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Do not create ACF fields for wrappers, CSS classes, layout containers, animation hooks, or JS hooks unless editor control is explicitly required.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Apply `references/enterprise-html-to-acf-rules.md`, `references/full-acf-editability-rules.md`, `references/media-library-seeding-rules.md`, and `references/global-template-parts-rules.md`. Add tasks for `.html-to-sage/PAGES.md`, `.html-to-sage/GLOBAL-TEMPLATE-PARTS.md`, `.html-to-sage/ASSET-MAP.md`, `.html-to-sage/MEDIA-LIBRARY-SEED.md`, `.html-to-sage/JS-BEHAVIOR-MAP.md`, `.html-to-sage/PERFORMANCE-RISKS.md`, `.html-to-sage/SECURITY-CHECKLIST.md`, and `.html-to-sage/VISUAL-QA.md`.

Add a media-library seed task group:

- inventory all original images, icons, logos, background images, videos, PDFs, downloadable files, and gallery assets
- decide whether each item is client-editable Media Library content or non-editable technical theme asset
- create `.html-to-sage/MEDIA-LIBRARY-SEED.md` with original stock path, media type, attachment target, usage, ACF/options/CPT field, default value strategy, alt/title source, and required status
- implement a repeatable seed/import path, preferably a WP-CLI command such as `wp <theme-slug> media seed`
- make the seed path idempotent so repeated runs do not duplicate attachments
- populate or resolve default ACF/options/CPT media values from seeded attachments so block previews are not empty after setup
- verify no client-editable media is permanently hardcoded from `stock/` or theme asset paths
- document the seed command/action in `README.md` and `.html-to-sage/FINAL-REPORT.md`

Create task groups for header/footer/navigation as template parts, not ACF blocks, unless the user explicitly approves page-level editor control.

Add explicit global-template-part tasks for header, footer, navigation, announcement bars, mobile sticky actions, schema, and global site UI. These tasks must ensure the UI renders by default from the theme layout and does not require page-level header/footer blocks.

For each global template part:
- analyze original HTML for the global element
- identify editable global data
- map navigation links to WordPress menu locations
- map logos/contact/social/legal/newsletter/form values to ACF options, theme options, Customizer, or approved plugins
- make global option fields optional when template defaults/fallbacks exist, so the options page can be saved with partial data
- create or update the Sage partial path
- migrate layout SCSS into `resources/css/layout/`
- migrate behavior JS into `resources/js/header.js`, `resources/js/navigation.js`, or `resources/js/footer.js`
- verify the global element is not duplicated in page templates or ACF block templates
- verify it is not listed in page ACF block order unless page-level control was explicitly approved
- compare visually with the original across desktop, tablet, and mobile

Add a final WordPress clone-readiness task group:

- verify the repository/theme folder can be cloned into `wp-content/themes/<theme-slug>`
- verify WordPress recognizes the theme from `style.css`
- verify activation will not fail because `functions.php`, Composer/autoload handling, or template entry files are missing
- verify required plugins are documented in `README.md`
- verify Home page block order and global header/footer/options setup are documented in `README.md`
- create `ready-pages/` and one paste-ready `.md` file per WordPress page with exact Gutenberg ACF block comments in page order
- verify original client-editable media can be seeded into the WordPress Media Library and default ACF block previews show seeded media or documented seeded preview fallbacks
- verify `.gitignore` excludes local agent folders (`.codex/`, `.claude/`, `.cursor/`, `.gemini/`, `.agents/`), skill source folders, uv caches, `node_modules/`, `vendor/`, and build artifacts unless explicitly intended
- verify the reusable skill repo/folder `html-to-wordpress-converter` is not inside the delivered theme and is not installed under `wp-content/themes`
- if WordPress reports a broken theme named `html-to-wordpress-converter`, delete that wrong folder from `wp-content/themes` and install the generated theme repo/folder instead
- run `composer install`, `npm install`, `npm run build`, PHP syntax checks, and WordPress activation/front-end smoke test when the environment supports them
- if the environment cannot run any check, record the skipped check and reason in `.html-to-sage/FINAL-REPORT.md`


