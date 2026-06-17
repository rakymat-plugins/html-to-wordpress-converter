---
name: html-to-wordpress-implementation-gate
description: Approval and QA gate for starting implementation of HTML-to-Sage WordPress conversions only after Spec Kit artifacts exist, tasks are section-by-section, stock is preserved, and visual parity requirements are enforceable.
---

# Implementation Gate

Do not implement until all exist:

- `stock/`
- `.html-to-sage/INTAKE.md`
- `.html-to-sage/HTML-AUDIT.md`
- `.html-to-sage/SECTION-MAP.md`
- `.html-to-sage/ACF-BLOCKS.md`
- `.html-to-sage/CPT-TAXONOMY-MAP.md`
- Spec Kit constitution/spec/plan/tasks/analyze artifacts
- explicit user approval to implement

Implementation gate sentence:

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, and visual hierarchy unless the user explicitly approves a change.

Fail the gate if any section lacks a comparison method or if a mismatch is accepted without user approval.

