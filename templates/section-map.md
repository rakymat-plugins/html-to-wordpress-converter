# Section Map

Apply `references/enterprise-html-to-acf-rules.md` and `references/full-acf-editability-rules.md`.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

| Original HTML Section Selector | Section Purpose | WordPress Target | Block Name | ACF Fields | Editable Fields Count | Hardcoded Allowed? | CPT Needed? | CSS Source | JS Source | Visual Match Risk | Notes |
|--------------------------------|-----------------|------------------|------------|------------|-----------------------|--------------------|-------------|------------|-----------|-------------------|-------|

