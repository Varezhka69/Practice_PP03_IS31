import os
from datetime import datetime

class ImageInfo:
    def __init__(self, image_loader):
        self.image_loader = image_loader

    def get_image_info(self):
        """Возвращает информацию об изображении: размер, разрешение, дата создания."""
        if self.image_loader.image is None:
            raise ValueError("Изображение не загружено.")

        info = {
            'Размер (байты)': os.path.getsize(self.image_loader.image_path),
            'Разрешение': self.image_loader.image.size,  # (ширина, высота)
            'Дата создания': self.get_creation_date()
        }
        return info

    def get_creation_date(self):
        """Возвращает дату создания изображения."""
        creation_time = os.path.getctime(self.image_loader.image_path)
        return datetime.fromtimestamp(creation_time)
