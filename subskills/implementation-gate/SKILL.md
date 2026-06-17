---
name: html-to-wordpress-implementation-gate
description: Approval and QA gate for starting implementation of HTML-to-Sage WordPress conversions only after Spec Kit artifacts exist, tasks are section-by-section, stock is preserved, and visual parity requirements are enforceable.
---

# Implementation Gate

Read `../../references/enterprise-html-to-acf-rules.md` and `../../references/full-acf-editability-rules.md` before allowing implementation.

Do not implement until all exist:

- `stock/`
- `.html-to-sage/INTAKE.md`
- `.html-to-sage/PAGES.md` for multi-page websites
- `.html-to-sage/HTML-AUDIT.md`
- `.html-to-sage/SECTION-MAP.md`
- `.html-to-sage/ACF-BLOCKS.md`
- `.html-to-sage/CPT-TAXONOMY-MAP.md`
- `.html-to-sage/ASSET-MAP.md`
- `.html-to-sage/JS-BEHAVIOR-MAP.md`
- `.html-to-sage/PERFORMANCE-RISKS.md`
- `.html-to-sage/SECURITY-CHECKLIST.md`
- `.html-to-sage/VISUAL-QA.md`
- Spec Kit constitution/spec/plan/tasks/analyze artifacts
- explicit user approval to implement

Implementation gate sentence:

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Fail the gate if any section lacks a comparison method or if a mismatch is accepted without user approval.

Fail the gate if meaningful original content remains hardcoded without a documented user-approved exception.


