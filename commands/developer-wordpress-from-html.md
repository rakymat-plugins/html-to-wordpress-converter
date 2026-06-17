# /developer-wordpress-from-html

Run the HTML-to-Sage WordPress conversion workflow.

Route to `developer-wordpress-from-html/SKILL.md` in the `html-to-wordpress-converter` skill repository and follow the same workflow:

1. Ask only blocking choices first: WordPress install path, final theme slug, and whether source files may be moved into `stock/`.
2. Run the real workflow helper:

   ```bash
   python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-install-path>
   ```

   If WordPress path is unknown, omit `--wp-path`; the helper must write `.html-to-sage/BLOCKERS.md` and stop before implementation.

3. Let the helper audit HTML/CSS/JS/assets, preserve/move source into `stock/`, check/install/init real Spec Kit, and generate Spec Kit constitution/spec/plan/research/data-model/quickstart/tasks/analyze artifacts.
4. Enforce visual parity, full ACF editability, justified CPTs, global template parts, and stock protection.
5. Stop before implementation unless the user explicitly approves implementation and blockers are resolved.

Required aliases for this same workflow:

- `/developer-wordpress-from-html`
- `/html-to-wordpress`
- `/html-to-sage`
- `$developer-wordpress-from-html`
- `$html-to-wordpress`
- `$html-to-sage`

If slash commands are unavailable, tell the agent: "Use the html-to-wordpress-converter skill and run developer-wordpress-from-html."
