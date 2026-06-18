# Global Template Parts Map

Apply `references/global-template-parts-rules.md`.

Header, footer, navigation, and other site-wide repeated elements should become Sage template parts or layout partials by default, not normal ACF blocks.

Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change.

Do not list header, footer, navigation, mobile menu, or other global site chrome as page ACF blocks unless the user explicitly approved page-level editor control.

Use WordPress menus for header navigation and footer link columns when they are normal label/URL links. Do not duplicate those links in ACF repeaters.

If a global settings/options page exists, document optional menu selector fields for each menu area. Selectors must choose existing WordPress menus by menu ID, fall back to Appearance > Menus location assignments when blank, and avoid hardcoded menu IDs.

| Source Selector | Element | WordPress Target | Template Part Path | Editable Data Source | ACF Options Fields | Menu Location | CSS Path | JS Path | Appears On | Explicit Page-Level Control Approved? | Visual Match Risk | Notes |
|-----------------|---------|------------------|--------------------|----------------------|--------------------|---------------|----------|---------|------------|---------------------------------------|-------------------|-------|

## Global Data Sources

| Data Item | Source Selector | WordPress Source | Field/Menu/Form Name | Original Value | Render Location | Fallback | Notes |
|-----------|-----------------|------------------|----------------------|----------------|-----------------|----------|-------|
