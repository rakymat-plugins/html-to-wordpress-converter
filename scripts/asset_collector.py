import shutil
from pathlib import Path

from project_detector import EXCLUDED_DIRS, detect_files


def _eligible_paths(source: Path) -> list[Path]:
    files: set[Path] = set()
    detected = detect_files(source)
    for items in detected.values():
        for item in items:
            files.add(source / item)

    for dirname in ("assets", "images", "img", "media", "fonts"):
        directory = source / dirname
        if directory.is_dir():
            for path in directory.rglob("*"):
                if path.is_file() and not any(part in EXCLUDED_DIRS for part in path.relative_to(source).parts):
                    files.add(path)

    return sorted(files)


def copy_to_stock(source: Path, project: Path, overwrite: bool = False, move_source: bool = False) -> Path:
    stock = project / "stock"
    if stock.exists() and any(stock.iterdir()) and not overwrite:
        raise FileExistsError(f"{stock} already exists and is not empty")
    stock.mkdir(parents=True, exist_ok=True)

    eligible = _eligible_paths(source)
    for item in eligible:
        destination = stock / item.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if overwrite or not destination.exists():
            shutil.copy2(item, destination)

    if move_source:
        for item in eligible:
            if stock in item.parents or item == stock:
                continue
            item.unlink(missing_ok=True)
        for dirname in ("assets", "images", "img", "media", "fonts"):
            directory = source / dirname
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
    return stock
