---
name: developer-wordpress-from-html
description: Alias skill command for html-to-wordpress-converter. Use when the user invokes $developer-wordpress-from-html or asks to convert static HTML into a Sage WordPress theme with ACF Blocks and Spec Kit planning.
---

# Developer WordPress From HTML

Use the `html-to-wordpress-converter` skill and route to `developer-wordpress-from-html/SKILL.md`.

Run the automatic HTML-to-Sage WordPress prepare workflow:

1. Ask only blocking choices first: WordPress install path, final theme slug, and whether source files may be moved into `stock/`.
2. Run:

   ```bash
   python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-install-path>
   ```

3. If WordPress path is unknown, omit `--wp-path`; the helper writes `.html-to-sage/BLOCKERS.md` and stops before implementation.
4. Let `prepare` audit HTML/CSS/JS/assets, preserve/move source into `stock/`, check/install/init real Spec Kit, and generate constitution/spec/plan/research/data-model/quickstart/tasks/analyze artifacts.
5. Stop before implementation unless the user explicitly approves implementation and blockers are resolved.
