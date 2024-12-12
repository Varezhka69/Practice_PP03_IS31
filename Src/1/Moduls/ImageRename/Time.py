import os
import time
import sys

class ImageLoader:
    def __init__(self, imagepath):
        self.imagepath = imagepath

    def load_image(self):
        # Здесь должен быть код загрузки изображения
        pass

class ImageRenamer:
    def __init__(self, imageloader):
        self.imageloader = imageloader

    def renameimage(self, newname):
        """Переименовывает изображение."""

        # Измеряем время создания нового пути
        start_time = time.time()
        newpath = os.path.join(os.path.dirname(self.imageloader.imagepath), newname)
        elapsed_time_newpath = time.time() - start_time

        # Измеряем время переименования файла
        start_time = time.time()
        os.rename(self.imageloader.imagepath, newpath)
        elapsed_time_rename = time.time() - start_time

        # Измеряем время обновления пути и загрузки нового изображения
        start_time = time.time()
        self.imageloader.imagepath = newpath  # Обновляем путь к изображению
        self.imageloader.load_image()  # Загружаем новое изображение
        elapsed_time_load = time.time() - start_time

        # Выводим результаты
        print(f"Время на создание нового пути: {elapsed_time_newpath:.6f} секунд")
        print(f"Время на переименование файла: {elapsed_time_rename:.6f} секунд")
        print(f"Время на обновление пути и загрузку изображения: {elapsed_time_load:.6f} секунд")

        # Выводим размер объекта
        print(f"Размер объекта 'ImageLoader': {sys.getsizeof(self.imageloader)} байт")
        print(f"Размер объекта 'ImageRenamer': {sys.getsizeof(self)} байт")
