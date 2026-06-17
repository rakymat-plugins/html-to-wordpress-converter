# CSS and JS Migration Rules

CSS must be assigned to:

- global/common
- layout
- component
- block

Keep section-specific CSS in `resources/css/blocks/_<block>.scss`.

JS must be audited by dependency. Preserve behavior and animations unless the user approves a change. Put section behavior in `resources/js/<block>.js` and import it from `resources/js/app.js`.

Do not replace Slick, GSAP, Swiper, jQuery, or other dependencies merely for preference if replacement risks visual mismatch.

