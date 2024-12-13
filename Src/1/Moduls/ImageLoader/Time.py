import os
import time
from PIL import Image
import sys

class ImageLoader:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.load_image()

    def load_image(self):
        """Загружает изображение и проверяет его наличие."""
        start_time = time.time()

        if os.path.exists(self.image_path):
            self.image = Image.open(self.image_path)
            load_time = time.time() - start_time
            print(f"Изображение загружено за {load_time:.6f} секунд.")
        else:
            raise FileNotFoundError(f"Файл {self.image_path} не найден.")

    def get_image_size(self):
        """Возвращает размер загруженного изображения в байтах."""
        if self.image is not None:
            image_size = sys.getsizeof(self.image)
            print(f"Размер объекта изображения: {image_size} байт.")
            return image_size
        else:
            raise ValueError("Изображение не загружено.")
#Пример использования
        if __name__ == "__main__":
            # Укажите путь к изображению
            image_path = "path/to/your/image.jpg"
        
            try:
                # Создаем экземпляр ImageLoader
                loader = ImageLoader(image_path)
        
                # Получаем размер изображения
                size = loader.get_image_size()
                print(f"Размер изображения в байтах: {size}")
        
            except FileNotFoundError as e:
                print(e)
            except ValueError as e:
                print(e)
