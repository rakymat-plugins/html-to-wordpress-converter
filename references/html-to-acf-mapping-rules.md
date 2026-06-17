# HTML to ACF Mapping Rules

All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content.

Do not turn every wrapper, class, or layout hook into an ACF field. ACF is for content editors; templates own structure, containers, classes, grid markup, JS hooks, and animation hooks unless the user explicitly asks for editor control.

Map static content into editable ACF fields conservatively:

- headings: text
- paragraphs: textarea or WYSIWYG
- buttons: link
- images: image array
- files: file
- cards: repeater
- grouped settings: group
- toggles: true_false
- galleries: repeater or gallery field

Preserve original DOM structure when visual parity depends on it. Do not simplify markup if it changes layout, spacing, animation hooks, or CSS selectors.

Preserve original HTML values in ACF block contracts and field maps where possible.
