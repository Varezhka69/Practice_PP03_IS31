import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


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
        try:
            # Открываем изображение и получаем его информацию
            with Image.open(file_path) as img:
                width, height = img.size
                format = img.format

            # Отображаем информацию
            info_text = f"Файл: {file_path}\\nФормат: {format}\\nРазмер: {width}x{height} пикселей"
            self.label_info.config(text=info_text)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось получить информацию об изображении:\\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageInfoApp(root)
    root.mainloop()
