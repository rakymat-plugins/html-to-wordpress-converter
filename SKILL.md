---
name: html-to-wordpress-converter
description: Spec Kit-backed workflow layer for converting existing static HTML/CSS/JS websites into WordPress Sage themes with Acorn, Blade, Vite, SCSS, ACF Pro blocks, justified CPTs/taxonomies, stock-folder preservation, and mandatory 100% visual parity. Use when planning or implementing an HTML-to-Sage WordPress conversion, especially with `/developer-wordpress-from-html`, ACF block mapping, Sage setup, or Spec Kit artifacts.
---

# HTML to WordPress Converter

Use this skill to convert static HTML websites into planned, editable WordPress Sage themes. This skill must not imitate Spec Kit. It uses the real GitHub Spec Kit project as the foundation and adds only a WordPress/Sage/ACF specialization layer.

## Architecture

Layer 1: Spec Kit Core
- `constitution`
- `specify`
- `clarify`
- `plan`
- `tasks`
- `analyze`
- `implement`

Layer 2: HTML-to-Sage WordPress Extension
- HTML source audit
- `stock/` backup folder
- Sage installation
- ACF block mapping
- CPT/taxonomy decisions
- CSS/JS/assets migration
- WordPress Media Library seeding for editable images, icons, videos, documents, and other client media
- visual parity requirements

Layer 3: Agent Adapters
- Claude Code command files
- Codex skill files
- generic `SKILL.md` instructions

## Primary Command

Use `developer-wordpress-from-html/SKILL.md` for the main workflow. If the user's agent supports slash commands, expose it as:

```text
/developer-wordpress-from-html
/html-to-wordpress
/html-to-sage
```

For Codex skill mode, use:

```text
$html-to-wordpress-converter
$developer-wordpress-from-html
$html-to-wordpress
$html-to-sage
```

Different agents expose commands differently. Claude Code may show slash commands or skills. Codex CLI may show `$command` skills. Generic agents should be told: "Use the html-to-wordpress-converter skill and run developer-wordpress-from-html."

## Non-Negotiable Rule

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Treat any visual mismatch as a failed task.

## Required Spec Kit Behavior

Before producing final planning artifacts, run the end-to-end prepare helper:

```bash
python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-path>
```

If the WordPress path is unknown, omit `--wp-path`; the helper must write `.html-to-sage/BLOCKERS.md`, generate planning artifacts, and stop before implementation.

To rerun only Spec Kit setup, run:

```bash
python <skill>/scripts/workflow.py speckit --project . --integration codex --skills --install --init
```

The helper uses project-local uv paths (`.uv-cache`, `.uv-tools`, `.uv-bin`) and can run `specify` from `.uv-bin` after install when the command is not on `PATH`.

The helper verifies Spec Kit:

```bash
specify --version
```

If unavailable, install the real Spec Kit CLI:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then initializes Spec Kit in the target project using the current agent integration:

```bash
specify init --here --force --integration codex --integration-options="--skills"
```

Use the real Spec Kit commands whenever possible:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.analyze
/speckit.implement
```

Codex skills mode may expose equivalent names such as `$speckit-constitution`, `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, and `$speckit-implement`.

## Mandatory Intake Before Planning

Ask only blocking questions before `prepare`; use defaults for the rest and let `prepare` record/update artifacts.

- WordPress install path, if implementation may follow.
- Final Sage theme slug, if the default is not acceptable.
- Whether root static source files may be moved into `stock/`; default: yes.

Defaults: pixel-perfect yes, visual improvements no, editable meaningful content yes, CPTs only when justified yes, preserve originals in `stock/` yes, header/footer/navigation as global template parts yes, implementation requires explicit approval.

## Stock Behavior

Run the stock helper before migration:

```bash
python <skill>/scripts/workflow.py stock --source . --project . --overwrite --move-source
```

This archives the static website files into `stock/` and removes the old root copies so the root does not keep both the original HTML and the preserved stock source. The helper excludes agent folders, generated artifacts, `.git`, `node_modules`, `vendor`, and the skill repository.

## Resource Routing

- Read `developer-wordpress-from-html/SKILL.md` for the end-to-end command.
- Read `references/enterprise-html-to-acf-rules.md` before any planning, mapping, package decision, implementation, or QA work.
- Read `references/full-acf-editability-rules.md` before mapping content into fields or writing implementation tasks.
- Read `references/media-library-seeding-rules.md` before asset planning, ACF field defaults, implementation, or final QA.
- Read `references/global-template-parts-rules.md` before mapping header, footer, navigation, global CTAs, or site-wide repeated UI.
- Read `references/sage-theme-architecture.md` before designing the theme structure.
- Read `references/acf-block-rules.md` before mapping sections into ACF blocks.
- Read `references/wordpress-cpt-taxonomy-rules.md` before proposing CPTs or taxonomies.
- Read `references/qa-visual-match-rules.md` before implementation or final QA.
- Use `scripts/workflow.py --help` for safe local audit/setup artifact generation.

## Implementation Gate

Do not start implementation until `workflow.py prepare` has completed, `.html-to-sage/BLOCKERS.md` has no unresolved implementation blockers, Spec Kit constitution/spec/plan/tasks/analyze artifacts exist, and the user explicitly asks to implement.

Apply the enterprise rules from `references/enterprise-html-to-acf-rules.md` to every `SKILL.md`, template, constitution prompt, plan prompt, tasks prompt, analyze prompt, and implementation gate.

Header, footer, navigation, announcement bars, mobile sticky actions, schema, and global site UI must render by default from the theme layout. Do not make editors add header/footer blocks to normal pages unless they explicitly approve page-level control. Make all meaningful global UI content editable through ACF options, WordPress menus, theme settings, Customizer, or approved plugins.

Global header/footer fields must be minimal and directly used. Use WordPress menus for navigation and footer link columns instead of ACF repeaters. Do not create unused option fields, duplicate menu fields, or schema fields that do not affect the frontend. Every global option must have a visible render location or documented integration, and implementation must verify that changing it in the admin changes the frontend.

When a global settings/options page exists, provide optional menu selector fields for each global menu area, such as header navigation and footer columns. These fields must select existing WordPress menus by menu ID, seed once from assigned default menus when empty, fall back to Appearance > Menus location assignments when blank, and never hardcode menu IDs.

Global options fields should be optional when defaults/fallbacks exist. Do not block saving a global settings page because logo, CTA links, footer links, contact data, or schema values are partially empty.

Apply the full editability rules from `references/full-acf-editability-rules.md` to prevent hardcoded client-editable content and to require `.html-to-sage/PAGES.md` for multi-page websites.

Apply the media library seeding rules from `references/media-library-seeding-rules.md`. Any original image, icon, logo, background image, gallery item, video, document, or other client-editable media must be imported or seedable into the WordPress Media Library and referenced through ACF attachment/file/gallery fields, options, menus, CPT fields, or documented WordPress data. Do not rely on permanent hardcoded theme asset URLs for client media.

Apply the global template part rules from `references/global-template-parts-rules.md` so headers, footers, navigation, and site-wide UI become Sage partials/layout template parts by default, not page ACF blocks. Keep their editable data in WordPress menus, ACF options pages, theme options, Customizer, or approved plugins; do not duplicate global values in page-local ACF fields.

Page templates must not duplicate converted ACF block sections. `front-page.php`, `page.php`, Blade page templates, CPT templates, and other fallback templates must render WordPress editor/block content through the normal content pipeline (`the_content()` or the Sage equivalent) and shared global layout only. Do not hardcode a homepage rebuild, section fallback, or alternate copy of any converted page section in `front-page.php` or another template. If a generic `index.php` fallback is needed, it may show only a neutral placeholder/credit screen when no content exists; it must not contain converted client website sections.

## WordPress Clone Readiness Gate

The delivered theme must work when the repository or theme folder is cloned into `wp-content/themes/<theme-slug>` and activated in WordPress.

Before final delivery, verify or document:

- `style.css` contains a valid WordPress theme header.
- `functions.php` loads Composer when present and bootstraps theme setup/framework files.
- The theme has a valid render path after activation: either standard WordPress templates such as `index.php`, `header.php`, `footer.php`, and `page.php`, or a verified Sage/Acorn Blade routing setup that works after `composer install`. Add `front-page.php` only when explicitly needed, and never as a hardcoded converted homepage fallback.
- Page templates render page/editor block content as the single source of truth. No `front-page.php` or fallback template may hardcode converted homepage sections or duplicate ACF block output outside the editor.
- Global header/footer/navigation render by default on normal pages without requiring page ACF header/footer blocks.
- Header/footer menu locations are registered and seeded idempotently when original menu links exist, without overwriting editor-assigned menus.
- Header/footer menu source selectors are available in global settings when the project has a global options page, and blank selectors fall back to Appearance > Menus location assignments.
- Global ACF options are limited to real non-menu editable values, and no unused fields remain in the options page.
- Required plugins are listed in `README.md`, especially ACF PRO.
- Install commands are listed in `README.md`: `composer install`, `npm install`, and `npm run build` when applicable.
- Original client-editable media has a documented Media Library seeding/import path, a media manifest, and ACF defaults or seeded field values so default block previews are not empty after setup.
- No local agent folders, skill source folders, uv caches, `node_modules/`, `vendor/`, or build artifacts are committed unless explicitly intended.
- The reusable skill repository itself (`html-to-wordpress-converter`) is never copied, nested, or cloned into `wp-content/themes`; if WordPress shows `html-to-wordpress-converter` as a broken theme, that folder is the skill repo in the wrong place and must be removed from the WordPress themes directory.
- `ready-pages/` exists with one paste-ready `.md` file per WordPress page, containing the exact Gutenberg/ACF block markup in page order.
- `.html-to-sage/FINAL-REPORT.md` records which activation/build/visual checks were run and which could not be run in the current environment.

