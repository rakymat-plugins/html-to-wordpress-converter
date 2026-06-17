# /html-to-wordpress

Alias for `/developer-wordpress-from-html`.

Run the HTML-to-Sage WordPress conversion workflow:

1. Ask only blocking choices first: WordPress install path, final theme slug, and whether source files may be moved into `stock/`.
2. Run:

   ```bash
   python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-install-path>
   ```

3. If WordPress path is unknown, omit `--wp-path`; the helper writes `.html-to-sage/BLOCKERS.md` and stops before implementation.
4. Stop before implementation unless the user explicitly approves implementation.

Route to `developer-wordpress-from-html/SKILL.md` in the `html-to-wordpress-converter` skill repository.
