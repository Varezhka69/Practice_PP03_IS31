import os
from PIL import Image

class ImageLoader:
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
