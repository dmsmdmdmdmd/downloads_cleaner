from pathlib import Path
from .organizer import organize_downloads


def main():
    downloads_path = Path(r"D:\Загрузки")
    print(f"📁 Сортировка файлов в: {downloads_path}")

    organize_downloads(downloads_path)

    print("✨ Готово! Папка «Загрузки» приведена в порядок.")


if __name__ == "__main__":
    main()