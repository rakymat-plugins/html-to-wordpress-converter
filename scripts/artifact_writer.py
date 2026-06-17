from pathlib import Path


VISUAL_RULE = "Every converted WordPress/Sage/ACF section must match the original HTML section 100% in layout, spacing, typography, colors, responsive behavior, animations, image ratios, hover states, and visual hierarchy unless the user explicitly approves a change."


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
        "HTML-AUDIT.md": "Record source files, sections, dependencies, and risks here.",
        "SECTION-MAP.md": "| HTML Section | WordPress Target | ACF Fields | CPT Needed? | CSS Source | JS Source | Visual Match Risk |\n|-------------|------------------|------------|-------------|------------|-----------|-------------------|",
        "CPT-TAXONOMY-MAP.md": "| Content Type | Decision | Justification | Taxonomies | Archive? | Single? | Admin Workflow |\n|--------------|----------|---------------|------------|----------|---------|----------------|",
        "ACF-BLOCKS.md": "Create one ACF block contract per converted section.",
        "ASSET-MAP.md": "Map every image, icon, font, video, SVG, and document from stock/ to its theme or media-library destination.",
        "JS-BEHAVIOR-MAP.md": "Map sliders, modals, accordions, tabs, animations, hover states, data attributes, and block-owned JS modules.",
        "PERFORMANCE-RISKS.md": "Record package, query, image, CSS, JS, Vite build, and asset-loading risks.",
        "SECURITY-CHECKLIST.md": "Record escaping, sanitization, nonce, form, URL, image, and raw-output checks.",
        "VISUAL-QA.md": "Record desktop, tablet, mobile, hover, animation, image-ratio, spacing, typography, console, and link checks.",
        "SAGE-SETUP.md": "Record Sage setup commands and verification here.",
        "SPECKIT-RUNS.md": "Record real Spec Kit commands and outcomes here.",
        "RISKS.md": "Record visual, technical, content, and integration risks here.",
        "DECISIONS.md": "Record user-approved decisions and deviations here.",
    }
    for filename, body in placeholders.items():
        path = state / filename
        if not path.exists():
            write_markdown(path, filename.removesuffix(".md").replace("-", " "), f"{VISUAL_RULE}\n\n{body}")


