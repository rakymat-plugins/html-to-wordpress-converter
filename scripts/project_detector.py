from pathlib import Path

EXCLUDED_DIRS = {
    ".git",
    ".html-to-sage",
    ".specify",
    ".uv-bin",
    ".uv-cache",
    ".uv-tools",
    ".claude",
    ".codex",
    ".cursor",
    ".gemini",
    ".agents",
    "html-to-wordpress-converter",
    "node_modules",
    "stock",
    "vendor",
}


def detect_files(source: Path) -> dict[str, list[str]]:
    patterns = {
        "html": ["*.html", "*.htm"],
        "css": ["*.css", "*.scss"],
        "js": ["*.js", "*.mjs"],
        "images": ["*.png", "*.jpg", "*.jpeg", "*.webp", "*.gif", "*.svg"],
        "fonts": ["*.woff", "*.woff2", "*.ttf", "*.otf"],
        "media": ["*.mp4", "*.webm", "*.mov"],
    }
    result: dict[str, list[str]] = {}
    for key, globs in patterns.items():
        files: list[str] = []
        for pattern in globs:
            files.extend(
                str(path.relative_to(source))
                for path in source.rglob(pattern)
                if path.is_file()
                and not any(part in EXCLUDED_DIRS for part in path.relative_to(source).parts)
            )
        result[key] = sorted(set(files))
    return result
