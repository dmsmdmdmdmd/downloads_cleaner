import argparse
from pathlib import Path
from .organizer import organize_downloads
from .gui import run_gui


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="Путь к папке для сортировки")
    parser.add_argument("--gui", action="store_true", help="Запуск графического интерфейса")
    args = parser.parse_args()

    # Запуск GUI
    if args.gui:
        run_gui()
        return

    # Запуск CLI
    download_path = Path(args.path) if args.path else Path.home() / "Downloads"

    organize_downloads(download_path)
    print("Сортировка завершена")


if __name__ == "__main__":
    main()