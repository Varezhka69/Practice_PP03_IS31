import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import time
import sys

class ImageInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Информация об изображении")

        # Кнопка выбора изображения
        self.btn_select_image = tk.Button(root, text="Выбрать изображение", command=self.load_image)
        self.btn_select_image.pack(pady=20)

        # Метка для отображения информации о изображении
        self.label_info = tk.Label(root, text="", wraplength=300)
        self.label_info.pack(pady=20)

    def load_image(self):
        # Открываем диалог выбора файла
        file_path = filedialog.askopenfilename(title="Выберите изображение",
                                                 filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.gif"),
                                                            ("All files", "*.*")))
        if file_path:
            self.display_image_info(file_path)

    def display_image_info(self, file_path):
        # Измеряем время открытия изображения
        start_time = time.time()

        try:
            # Открываем изображение и получаем его информацию
            with Image.open(file_path) as img:
                width, height = img.size
                img_format = img.format

            loading_time = time.time() - start_time
            info_text = f"Файл: {file_path}\\nФормат: {img_format}\\nРазмер: {width}x{height} пикселей\\n" \
                        f"Время загрузки: {loading_time:.6f} секунд"
            self.label_info.config(text=info_text)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось получить информацию об изображении:\\n{e}")

        # Выводим информацию о размерах использованных библиотек
        self.print_sys_info()

    def print_sys_info(self):
        # Выводим размеры модулей sys и PIL
        print(f"Размер модуля sys: {sys.getsizeof(sys)} байт")
        try:
            from PIL import Image
            print(f"Размер модуля PIL.Image: {sys.getsizeof(Image)} байт")
        except ImportError:
            print("Модуль PIL не найден")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageInfoApp(root)
    root.mainloop()
