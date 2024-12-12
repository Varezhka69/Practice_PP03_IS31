import os
import sys
from PIL import Image
from datetime import datetime
import time

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.load_image()

    def measure_time(func):
        """Декоратор для измерения времени выполнения функции."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Время выполнения {func.__name__}: {execution_time:.6f} секунд")
            return result
        return wrapper

    @measure_time
    def load_image(self):
        """Загружает изображение и проверяет его наличие."""
        if os.path.exists(self.image_path):
            self.image = Image.open(self.image_path)
        else:
            raise FileNotFoundError(f"Файл {self.image_path} не найден.")

    @measure_time
    def get_image_info(self):
        """Возвращает информацию об изображении: размер, разрешение, дата создания."""
        if self.image is None:
            raise ValueError("Изображение не загружено.")

        info = {
            'Размер (байты)': os.path.getsize(self.image_path),
            'Разрешение': self.image.size,  # (ширина, высота)
            'Дата создания': self.get_creation_date()
        }
        print(f"Размер объекта get_image_info в памяти: {sys.getsizeof(info)} байт")
        return info

    @measure_time
    def get_creation_date(self):
        """Возвращает дату создания изображения."""
        creation_time = os.path.getctime(self.image_path)
        return datetime.fromtimestamp(creation_time)

    @measure_time
    def rename_image(self, new_name):
        """Переименовывает изображение."""
        new_path = os.path.join(os.path.dirname(self.image_path), new_name)

        os.rename(self.image_path, new_path)
        self.image_path = new_path  # Обновляем путь к изображению
        self.load_image()  # Загружаем новое изображение
