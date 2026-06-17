from pathlib import Path


VISUAL_RULE = "Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change."
EDITABILITY_RULE = "All meaningful content from the original HTML must be editable through ACF fields or justified CPT fields. Templates may contain structure, layout, and behavior hooks, but must not hardcode client-editable content."
PAGES_RULE = "For multi-page HTML websites, generate .html-to-sage/PAGES.md showing every WordPress page, the exact ACF block order, the field groups used, and the original HTML source section for each block."
GLOBAL_PARTS_RULE = "Header, footer, navigation, and other site-wide repeated elements should become Sage template parts or layout partials by default, not normal ACF blocks. Keep editable global data in menus, options, Customizer, theme options, or approved plugins, not page-local ACF fields."


def ensure_state(project: Path) -> Path:
    state = project / ".html-to-sage"
    state.mkdir(parents=True, exist_ok=True)
    return state


def write_markdown(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n{body.rstrip()}\n", encoding="utf-8")


def write_initial_artifacts(project: Path) -> None:
    state = ensure_state(project)
    placeholders = {
        "INTAKE.md": "Record intake answers and assumptions here.",
        "PAGES.md": "For each original HTML page, document the WordPress title, slug, ACF block order, field groups, source sections, template paths, SCSS paths, JS paths, CPT dependencies, and editor instructions. Required for multi-page websites.",
        "HTML-AUDIT.md": "Record source files, sections, dependencies, and risks here.",
        "SECTION-MAP.md": "| Original HTML Section Selector | Section Purpose | WordPress Target | Block Name | ACF Fields | Editable Fields Count | Hardcoded Allowed? | CPT Needed? | CSS Source | JS Source | Visual Match Risk | Notes |\n|--------------------------------|-----------------|------------------|------------|------------|-----------------------|--------------------|-------------|------------|-----------|-------------------|-------|",
        "GLOBAL-TEMPLATE-PARTS.md": "| Source Selector | Element | WordPress Target | Template Part Path | Editable Data Source | ACF Options Fields | Menu Location | CSS Path | JS Path | Appears On | Explicit Page-Level Control Approved? | Visual Match Risk | Notes |\n|-----------------|---------|------------------|--------------------|----------------------|--------------------|---------------|----------|---------|------------|---------------------------------------|-------------------|-------|\n\n## Global Data Sources\n\n| Data Item | Source Selector | WordPress Source | Field/Menu/Form Name | Original Value | Render Location | Fallback | Notes |\n|-----------|-----------------|------------------|----------------------|----------------|-----------------|----------|-------|",
        "CPT-TAXONOMY-MAP.md": "| Content Type | Decision | Justification | Taxonomies | Archive? | Single? | Admin Workflow |\n|--------------|----------|---------------|------------|----------|---------|----------------|",
        "ACF-BLOCKS.md": "Create one ACF block contract per converted section. Include block name, field group key, field list, original HTML values, required/optional status, repeaters, media fields, buttons/links, editor instructions, template path, SCSS path, and JS path.",
        "ASSET-MAP.md": "Map every image, icon, font, video, SVG, and document from stock/ to its theme or media-library destination.",
        "JS-BEHAVIOR-MAP.md": "Map sliders, modals, accordions, tabs, animations, hover states, data attributes, and block-owned JS modules.",
        "PERFORMANCE-RISKS.md": "Record package, query, image, CSS, JS, Vite build, and asset-loading risks.",
        "SECURITY-CHECKLIST.md": "Record escaping, sanitization, nonce, form, URL, image, and raw-output checks.",
        "VISUAL-QA.md": "Record desktop, tablet, mobile, hover, animation, image-ratio, spacing, typography, console, and link checks.",
        "SAGE-SETUP.md": "Record Sage setup commands and verification here.",
        "SPECKIT-RUNS.md": "Run `python <skill>/scripts/workflow.py prepare --source . --project . --theme-name <theme-name> --wp-path <wordpress-install-path>` first. To rerun only setup logging, run `python <skill>/scripts/workflow.py speckit --project . --integration codex --skills --install --init`. Record real Spec Kit commands and outcomes here. Do not fake Spec Kit artifacts.",
        "RISKS.md": "Record visual, technical, content, and integration risks here.",
        "DECISIONS.md": "Record user-approved decisions and deviations here.",
    }
    for filename, body in placeholders.items():
        path = state / filename
        if not path.exists():
            write_markdown(path, filename.removesuffix(".md").replace("-", " "), f"{VISUAL_RULE}\n\n{EDITABILITY_RULE}\n\n{PAGES_RULE}\n\n{GLOBAL_PARTS_RULE}\n\n{body}")


