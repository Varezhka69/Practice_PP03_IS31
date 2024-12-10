import os

class ImageRenamer:
    def __init__(self, image_loader):
        self.image_loader = image_loader

    def rename_image(self, new_name):
        """Переименовывает изображение."""
        new_path = os.path.join(os.path.dirname(self.image_loader.image_path), new_name)

        os.rename(self.image_loader.image_path, new_path)
        self.image_loader.image_path = new_path  # Обновляем путь к изображению
        self.image_loader.load_image()  # Загружаем новое изображение
