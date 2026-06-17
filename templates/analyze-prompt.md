# Spec Kit Analyze Prompt

Use `/speckit.analyze` or `$speckit-analyze`.

Analyze the constitution, specification, plan, and tasks for cross-artifact consistency before implementation.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Check that `references/enterprise-html-to-acf-rules.md` is enforced:

- no giant catch-all block
- no unowned global CSS/JS migration
- no unjustified CPTs
- no hardcoded editable content
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

Fail analysis if any section lacks a WordPress target, ACF contract, CSS ownership, JS ownership, visual QA task, or security escaping notes.

