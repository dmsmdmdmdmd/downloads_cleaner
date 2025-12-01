import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from .organizer import organize_downloads


class DownloadsCleanerGUI:
    def __init__(self, root):
        self.root = root
        root.title("Downloads Cleaner")
        root.geometry("450x220")
        root.resizable(False, False)

        self.path_var = tk.StringVar()

        # Заголовок
        tk.Label(root, text="Выберите папку для сортировки", font=("Arial", 12)).pack(pady=10)

        # Поле ввода пути
        self.entry = tk.Entry(root, textvariable=self.path_var, width=45)
        self.entry.pack(pady=5)

        # Кнопка выбора папки
        tk.Button(root, text="Выбрать папку", command=self.choose_folder).pack(pady=5)

        # Кнопка сортировки
        tk.Button(root, text="Начать сортировку", command=self.start_sorting, bg="#4caf50", fg="white").pack(pady=15)

    def choose_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_var.set(folder_selected)

    def start_sorting(self):
        path = self.path_var.get()

        if not path:
            messagebox.showwarning("Ошибка", "Вы не выбрали папку!")
            return

        download_path = Path(path)

        if not download_path.exists():
            messagebox.showerror("Ошибка", "Папка не существует!")
            return

        try:
            organize_downloads(download_path)
            messagebox.showinfo("Готово", "Сортировка завершена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")


def run_gui():
    root = tk.Tk()
    app = DownloadsCleanerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
