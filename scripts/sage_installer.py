from pathlib import Path


def sage_commands(theme_name: str) -> list[str]:
    return [
        f"composer create-project roots/sage {theme_name}",
        "npm install",
        "npm run build",
        "verify public/build/manifest.json exists",
    ]


def framework_paths(theme_root: Path) -> list[Path]:
    relative = [
        "framework/builder/acf-blocks",
        "framework/builder/front-end",
        "framework/post-type",
        "framework/taxonomies",
        "framework/custom-fields",
        "framework/actions",
        "framework/hooks",
        "framework/utilities",
        "resources/css/blocks",
        "resources/css/layout",
        "resources/css/components",
        "resources/css/common",
        "resources/js",
    ]
    return [theme_root / path for path in relative]

