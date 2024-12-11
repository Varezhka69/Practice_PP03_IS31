import os
from PIL import Image
from datetime import datetime

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.load_image()

    def load_image(self):
        """Загружает изображение и проверяет его наличие."""
        if os.path.exists(self.image_path):
            self.image = Image.open(self.image_path)
        else:
            raise FileNotFoundError(f"Файл {self.image_path} не найден.")

    def get_image_info(self):
        """Возвращает информацию об изображении: размер, разрешение, дата создания."""
        if self.image is None:
            raise ValueError("Изображение не загружено.")

        info = {
            'Размер (байты)': os.path.getsize(self.image_path),
            'Разрешение': self.image.size,  # (ширина, высота)
            'Дата создания': self.get_creation_date()
        }
        return info

    def get_creation_date(self):
        """Возвращает дату создания изображения."""
        creation_time = os.path.getctime(self.image_path)
        return datetime.fromtimestamp(creation_time)

    def rename_image(self, new_name):
        """Переименовывает изображение."""
        new_path = os.path.join(os.path.dirname(self.image_path), new_name)

        os.rename(self.image_path, new_path)
        self.image_path = new_path  # Обновляем путь к изображению
        self.load_image()  # Загружаем новое изображение
