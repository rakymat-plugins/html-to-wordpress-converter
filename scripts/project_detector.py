from pathlib import Path


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
            files.extend(str(path.relative_to(source)) for path in source.rglob(pattern) if path.is_file())
        result[key] = sorted(set(files))
    return result

