# Intake Questions

Apply `references/enterprise-html-to-acf-rules.md`.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Ask before planning:

- Should the conversion be pixel-perfect? Default: yes.
- Are visual improvements allowed? Default: no.
- Should all editable content be in ACF? Default: yes.
- Are CPTs allowed only when justified? Default: yes.
- Should original files be preserved in `stock/`? Default: yes.
- Should root static source files be moved into `stock/` after preservation? Default: yes.
- Project name?
- Theme name?
- WordPress install path?
- One-page or multi-page?
- Which HTML files are in scope?
- Expected editor flexibility level?
- Should sections be reusable across pages?
- Should header/footer/navigation be global Sage template parts? Default: yes.
- Does the user explicitly want page-level editor control over header/footer/navigation? Default: no.
- Are CPTs needed? Possible CPTs: services, projects, products, testimonials, team, branches, FAQs, careers, news, events, downloads.
- Are taxonomies needed?
- Forms: Gravity Forms, Contact Form 7, custom form, or static markup?
- Multilingual support needed?
- CSS approach: Bootstrap, Tailwind, plain SCSS, or existing CSS?
- JS libraries present: jQuery, Slick, GSAP, Swiper, other?
- Must animations be preserved?
- Must SEO metadata be migrated?
- Does WordPress admin UX matter?
- Must ACF field groups be code-only?
- Planning only or implementation later?
- Is this a multi-page site that requires `.html-to-sage/PAGES.md`?
- Should every meaningful content item be editable through ACF or justified CPT fields?
