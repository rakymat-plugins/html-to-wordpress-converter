# Implementation Gate

Do not run `/speckit.implement` or `$speckit-implement` until the user explicitly approves implementation.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Required before implementation:

- real Spec Kit constitution exists
- real Spec Kit specification exists
- clarification questions are answered or documented
- technical plan exists
- tasks exist and are grouped section by section
- analyze pass is complete
- `stock/` exists and is read-only source material
- `.html-to-sage/` artifacts exist
- each section has an ACF block/template/CPT/component decision
- enterprise rules are referenced in the implementation tasks

Visual mismatch is a blocker, not a minor issue.
