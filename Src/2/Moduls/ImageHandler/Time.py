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
# Пример использования
if __name__ == "__main__":
    # Путь к изображению
    image_path = 'C:/Users/Nout/Pictures/Безымянный.png'  # Замените на путь к вашему файлу изображения
try:
    info = get_image_info(image_path)
    print(info)
except FileNotFoundError:
        print(f"Файл {image_path} не найден.")
except Exception as e:
        print(f"Произошла ошибка: {e}")
