# Spec Kit Tasks Prompt

Use `/speckit.tasks` or `$speckit-tasks`.

Generate implementation tasks with these phases:

- Phase 0: Intake and source audit
- Phase 1: Stock folder and project workspace
- Phase 2: Sage theme setup and framework structure
- Phase 3: HTML section mapping
- Phase 4: ACF block contracts
- Phase 5: CPT/taxonomy contracts
- Phase 6: CSS/JS/assets migration plan
- Phase 7: WordPress editor/admin UX plan
- Phase 8: visual QA and responsive QA plan
- Phase 9: implementation tasks
- Phase 10: final build/test/deployment checklist

Phase 2 must always include:

- install Sage
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
- create ACF block registration
- create ACF fields in code
- create frontend template
- migrate SCSS
- migrate JS if needed
- compare visually with original
- fix mismatch until 100% match

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, and visual hierarchy unless the user explicitly approves a change.

