import time
import sys
from PIL import Image

def get_image_info(file_path):
    # Начинаем измерение времени
    start_time = time.perf_counter()

    # Открываем изображение и получаем его информацию
    with Image.open(file_path) as img:
        width, height = img.size
        img_format = img.format

    # Время после открытия изображения
    open_time = time.perf_counter()

    # Получаем информацию о размере изображения в байтах
    size_in_bytes = sys.getsizeof(img.tobytes())

    # Время после получения информации
    info_time = time.perf_counter()

    # Возвращаем отформатированное сообщение с информацией об изображении и временными показателями
    return (f"Файл: {file_path}\\n"
            f"Формат: {img_format}\\n"
            f"Размер: {width}x{height} пикселей\\n"
            f"Размер в байтах: {size_in_bytes}\\n"
            f"Время открытия изображения: {open_time - start_time:.6f} секунд\\n"
            f"Время получения информации: {info_time - open_time:.6f} секунд")
