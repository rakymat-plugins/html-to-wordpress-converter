# Spec Kit Constitution Prompt

Use `/speckit.constitution` or `$speckit-constitution` with this content.

Create governing principles for converting an existing static HTML/CSS/JS website into a WordPress Sage theme using Acorn, Blade, Vite, SCSS, ACF Pro, and code-owned ACF field groups.

Include this exact non-negotiable rule:

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Constitution articles:

1. HTML Visual Parity First
   - Every section must be visually identical to the original HTML version.
   - No redesign.
   - No improvement.
   - No layout simplification.
   - No spacing changes.
   - No typography changes.
   - No color changes.
   - No animation removal unless approved.
2. Section-by-Section Conversion
   - Each HTML section must be converted into one of: ACF Block, global template part, CPT archive/single template, reusable component.
3. Sage Architecture Enforcement
   - The theme must use Sage, Acorn, Blade, Vite, SCSS, ACF Pro, and code-owned ACF field groups.
4. ACF Block Contract
   - Every ACF block must define fields, frontend template, SCSS file, optional JS module, editor preview behavior, and visual parity checklist.
5. No Unjustified CPTs
   - CPTs are only allowed when content is repeatable, reusable, filterable, archiveable, or needs an independent admin workflow.
6. Stock Folder Protection
   - All original HTML/CSS/JS/assets must be copied into `stock/`.
   - The `stock/` folder is read-only source material. Never edit it.
7. QA Gate
   - Implementation is not complete until every converted section is compared against the original HTML.

Also include secure escaping/sanitization in PHP templates, responsive QA, accessibility basics, performance budgets, and editor usability.

Also enforce `references/enterprise-html-to-acf-rules.md`: no giant catch-all blocks, no unowned global CSS/JS, no page builders, no manual-only ACF setup, no random class renames, no unjustified packages, no unpaginated public queries, and no raw ACF output.


