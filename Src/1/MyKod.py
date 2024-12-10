import os
from PIL import Image
from datetime import datetime

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = self.open_image()

    def open_image(self):
        try:
            return Image.open(self.image_path)
        except Exception as e:
            print(f"Ошибка при открытии изображения: {e}")
            return None

    def get_image_info(self):
        if self.image:
            image_info = {}
            image_info['size'] = os.path.getsize(self.image_path)  # размер в байтах
            image_info['resolution'] = self.image.size  # разрешение (ширина, высота)
            creation_time = os.path.getctime(self.image_path)
            image_info['creation_date'] = datetime.fromtimestamp(creation_time)  # дата создания
            return image_info
        return None

    def rename_image(self, new_name):
        if self.image:
            dir_name = os.path.dirname(self.image_path)
            new_image_path = os.path.join(dir_name, new_name)
            try:
                os.rename(self.image_path, new_image_path)
                self.image_path = new_image_path  # обновляем путь к изображению
                print(f"Изображение переименовано в: {new_image_path}")
            except Exception as e:
                print(f"Ошибка при переименовании: {e}")
