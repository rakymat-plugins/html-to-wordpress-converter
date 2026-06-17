---
name: html-to-wordpress-html-audit
description: Audit static HTML/CSS/JS/assets before converting to Sage WordPress, preserving originals in stock, identifying sections, dependencies, forms, animations, responsive behavior, and visual parity risks.
---

# HTML Audit

Read `../../references/enterprise-html-to-acf-rules.md` before auditing.

Inspect source files without changing them. Copy all original HTML/CSS/JS/assets into `stock/` before migration. Treat `stock/` as read-only.

Create `.html-to-sage/HTML-AUDIT.md` with:

- HTML files and page roles
- section inventory
- CSS files and likely scope
- JS files and dependencies
- images, fonts, videos, SVGs, icons
- forms and validation behavior
- animations and interactive widgets
- responsive breakpoints
- visual parity risk notes
- asset ownership and image ratio risks
- JS behavior ownership and hover/animation risks

Use `scripts/workflow.py audit --source <source> --project <target>` for a safe first pass.
