# HTML to ACF Mapping Rules

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

