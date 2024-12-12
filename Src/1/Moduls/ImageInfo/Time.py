import os
import time
from datetime import datetime

class ImageInfo:
    def __init__(self, image_loader):
        self.image_loader = image_loader

    def get_image_info(self):
        """Возвращает информацию об изображении: размер, разрешение, дата создания."""
        if self.image_loader.image is None:
            raise ValueError("Изображение не загружено.")

        # Замеряем время получения размера изображения
        start_time = time.time()
        size_bytes = os.path.getsize(self.image_loader.image_path)
        time_size = time.time() - start_time

        # Замеряем время получения разрешения
        start_time = time.time()
        resolution = self.image_loader.image.size  # (ширина, высота)
        time_resolution = time.time() - start_time

        # Замеряем время получения даты создания
        start_time = time.time()
        creation_date = self.get_creation_date()
        time_creation_date = time.time() - start_time

        info = {
            'Размер (байты)': size_bytes,
            'Разрешение': resolution,  # (ширина, высота)
            'Дата создания': creation_date,
            'Время получения размера (с)': time_size,
            'Время получения разрешения (с)': time_resolution,
            'Время получения даты создания (с)': time_creation_date
        }
        return info

    def get_creation_date(self):
        """Возвращает дату создания изображения."""
        creation_time = os.path.getctime(self.image_loader.image_path)
        return datetime.fromtimestamp(creation_time)
