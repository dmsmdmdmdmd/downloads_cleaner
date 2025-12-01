import os
import shutil
from pathlib import Path
from .config import CATEGORIES, DEFAULT_DIR_NAME


def get_category(file_suffix: str) -> str:
    file_suffix = file_suffix.lower()
    for category, extensions in CATEGORIES.items():
        if file_suffix in extensions:
            return category
    return DEFAULT_DIR_NAME


def organize_downloads(download_path: Path):
    if not download_path.exists():
        raise FileNotFoundError(f"Папка {download_path} не найдена")

    for item in download_path.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            target_dir = download_path / category
            target_dir.mkdir(exist_ok=True)

            new_path = target_dir / item.name

            # защитимся от перезаписи
            if new_path.exists():
                new_path = target_dir / f"{new_path.stem}_copy{new_path.suffix}"

            shutil.move(str(item), str(new_path))
            print(f"[OK] {item.name} → {category}/")