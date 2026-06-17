# ACF Block Rules

Every block must have:

- registration
- code-owned ACF field group
- frontend template
- SCSS file
- optional JS module
- editor preview behavior
- visual parity checklist

Use ACF Pro local field groups. Escape output:

- `esc_html()` for text
- `esc_attr()` for attributes
- `esc_url()` for URLs
- `wp_kses_post()` for trusted rich text

Do not create manual-only ACF configuration in the WordPress admin.

