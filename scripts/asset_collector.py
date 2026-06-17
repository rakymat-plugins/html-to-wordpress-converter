import shutil
from pathlib import Path


def copy_to_stock(source: Path, project: Path, overwrite: bool = False) -> Path:
    stock = project / "stock"
    if stock.exists() and any(stock.iterdir()) and not overwrite:
        raise FileExistsError(f"{stock} already exists and is not empty")
    stock.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        if item.name in {"stock", ".git", "node_modules", "vendor"}:
            continue
        destination = stock / item.name
        if item.is_dir():
            if destination.exists() and overwrite:
                shutil.rmtree(destination)
            if not destination.exists():
                shutil.copytree(item, destination)
        elif item.is_file():
            if overwrite or not destination.exists():
                shutil.copy2(item, destination)
    return stock

