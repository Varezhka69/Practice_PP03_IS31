import time
import sys
from module_image_loader import ImageLoader
from module_image_info import ImageInfo
from module_image_renamer import ImageRenamer

def main():
    image_path = 'path/to/your/image.jpg'  # Укажите путь к вашему изображению

    start_time = time.time()
    image_loader = ImageLoader(image_path)
    load_time = time.time() - start_time
    print(f'Время загрузки изображения: {load_time:.6f} секунд')

    # Получаем информацию об изображении
    start_time = time.time()
    image_info = ImageInfo(image_loader)
    info = image_info.get_image_info()
    info_time = time.time() - start_time
    print(f'Время получения информации об изображении: {info_time:.6f} секунд')
    print(info)

    # Переименовываем изображение
    new_name = 'new_image_name.jpg'
    start_time = time.time()
    renamer = ImageRenamer(image_loader)
    renamer.rename_image(new_name)
    rename_time = time.time() - start_time
    print(f'Время переименования изображения: {rename_time:.6f} секунд')
    print(f'Изображение переименовано в {new_name}')

    # Печатаем размеры модулей
    print(f'Размер модуля ImageLoader: {sys.getsizeof(ImageLoader)} байт')
    print(f'Размер модуля ImageInfo: {sys.getsizeof(ImageInfo)} байт')
    print(f'Размер модуля ImageRenamer: {sys.getsizeof(ImageRenamer)} байт')

if __name__ == "__main__":
    main()
