# Spec Kit Analyze Prompt

Use `/speckit.analyze` or `$speckit-analyze`.

Analyze the constitution, specification, plan, and tasks for cross-artifact consistency before implementation.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Client-editable media from the original HTML must be imported or seedable into the WordPress Media Library and referenced through ACF/options/CPT/menu attachment data. Default ACF previews must not be empty because original media was left as hardcoded theme assets.

Do not over-dynamicize structural markup. ACF field maps should cover content, not every wrapper/class/hook in the DOM.

For multi-page HTML websites, generate `.html-to-sage/PAGES.md` showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block.

Check that `references/enterprise-html-to-acf-rules.md`, `references/full-acf-editability-rules.md`, `references/media-library-seeding-rules.md`, and `references/global-template-parts-rules.md` are enforced:

- no giant catch-all block
- no unowned global CSS/JS migration
- no unjustified CPTs
- no hardcoded editable content
- no meaningful original text, image URL, button label, or button URL hardcoded in templates
- no converted page sections duplicated in `front-page.php`, `page.php`, `index.php`, Blade page templates, CPT templates, or fallback templates outside `the_content()`/Sage editor content rendering
- no Home page frontend path that ignores ACF block edits made in the WordPress editor
- no client-editable original media permanently hardcoded from `stock/` or theme asset paths
- no missing `.html-to-sage/MEDIA-LIBRARY-SEED.md` when the source contains client-editable media
- no empty default ACF media previews caused by unseeded source media
- no edits to `stock/`
- no random class renames or removed behavior hooks
- no page builders
- no dashboard-only ACF field groups
- no bloated unrelated block fields
- no globally loaded block-only slider/animation libraries
- no unpaginated public queries
- no full-size card/grid images
- no raw ACF output
- no missing responsive, hover, image ratio, or animation QA
- no missing field map with original HTML values
- no fields created only for structural wrappers/classes/hooks without editor need
- no missing `PAGES.md` for multi-page sites
- no header/footer/navigation converted into normal page ACF blocks without explicit approval
- no header/footer link columns duplicated as ACF repeaters when WordPress menus are appropriate
- no missing idempotent default menu seeding for original menus
- no unused, duplicate, speculative, or non-working global option fields
- no missing `GLOBAL-TEMPLATE-PARTS.md` for site-wide UI

Fail analysis if any section lacks a WordPress target, ACF contract, editable field map, CSS ownership, JS ownership, visual QA task, or security escaping notes.
