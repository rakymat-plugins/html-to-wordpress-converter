# Media Library Seeding Rules

Use this reference for every static HTML to Sage + ACF Blocks conversion that includes images, icons, logos, videos, PDFs, downloadable files, or other media.

## Core Rule

Client-editable media from the original HTML must be imported or seedable into the WordPress Media Library and referenced through WordPress attachment data.

Do not make editable images, logos, icons, background images, videos, documents, or galleries depend on permanent hardcoded URLs from `stock/` or theme asset folders.

## Media Destinations

Use the WordPress Media Library for:

- logos and brand marks
- hero images and background images
- profile photos
- card images and card icons when the client may replace them
- gallery and slider images
- testimonial photos
- authority, partner, and client logos
- video poster images
- uploaded video files when locally hosted
- PDFs, brochures, certificates, and downloadable files
- social/share icons when the client controls the icon asset
- decorative images when the client may need to replace them

Theme assets may be used for:

- fonts in `resources/fonts/`
- non-content UI sprites or purely technical decorative SVG shapes
- CSS-only patterns and masks
- icons from an approved code icon library
- build/runtime assets that editors should never replace

If there is doubt, treat the media as client-editable and seed it into the Media Library.

## Required Seed Path

Every generated theme with source media must include one documented seed/import path. Prefer one of:

- a WP-CLI command registered by the theme, for example `wp <theme-slug> media seed`
- a guarded admin/tooling action that imports missing media once
- a documented PHP seed script that uses WordPress APIs

The seed path must:

- read source files from preserved `stock/` or a documented seed assets folder
- import files with WordPress APIs such as `media_handle_sideload()` or equivalent
- create or update a media manifest
- avoid duplicate uploads when run more than once
- preserve useful filenames, alt text, captions, and titles from the original HTML where available
- never require editors to manually re-upload every default image just to see block previews

## Manifest

Generate `.html-to-sage/MEDIA-LIBRARY-SEED.md` and keep `.html-to-sage/ASSET-MAP.md` aligned.

Use this table:

| Original Stock Path | Media Type | WordPress Attachment Target | Used By | ACF Field/Option/CPT Field | Default Value Strategy | Alt/Title Source | Required? | Notes |
|---------------------|------------|-----------------------------|---------|----------------------------|------------------------|------------------|-----------|-------|

`Default Value Strategy` should explain whether the implementation seeds:

- page/block field values
- global option values
- CPT field values
- attachment IDs looked up from a manifest
- editor preview fallbacks from seeded attachments

## ACF Field Usage

ACF media fields should use WordPress attachment data:

- image fields should return arrays or IDs and render with `wp_get_attachment_image()` where possible
- file/video/document fields should return arrays or IDs and render escaped URLs/titles
- galleries and repeaters should store attachment IDs/arrays, not raw HTML
- background images should still be ACF image fields, then rendered as escaped inline style URLs or CSS variables from attachment URLs
- icons should be image/SVG fields, select fields from an approved icon library, or seeded attachment fields depending on editability

Avoid raw URL text fields for media unless the source is intentionally external, such as YouTube/Vimeo URLs.

## Defaults and Editor Previews

Default block previews must not appear empty just because the original media stayed in theme assets.

For each block/global option that has original media, provide one of:

- seeded ACF field values for the default page/options setup
- editor preview fallback that resolves a seeded attachment from the manifest
- documented seed instructions that populate the relevant fields before editor use

If a user replaces a seeded image, the original should still be restorable from the Media Library without re-cloning the theme.

## Forbidden Patterns

Do not:

- hardcode `stock/` URLs in frontend templates
- hardcode client-editable media URLs from `resources/images/` in block templates
- leave ACF image fields empty while showing a different hardcoded image on the frontend
- require editors to manually find and upload all original default images after activation
- make media defaults depend on local absolute paths
- duplicate the same media on every seed run

## QA Gate

Before final delivery, verify:

- source media is listed in `.html-to-sage/MEDIA-LIBRARY-SEED.md`
- client-editable media appears in the WordPress Media Library after the seed/import step
- ACF image/file/gallery fields use attachment data
- default block previews show the original seeded media or a documented seeded preview fallback
- no frontend templates reference `stock/`
- no client-editable original media is permanently hardcoded as a theme asset
- `.html-to-sage/FINAL-REPORT.md` records the media seed command/action and whether it was run
