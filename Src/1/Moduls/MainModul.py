from module_image_loader import ImageLoader
from module_image_info import ImageInfo
from module_image_renamer import ImageRenamer

def main():
    image_path = 'path/to/your/image.jpg'  # Укажите путь к вашему изображению
    image_loader = ImageLoader(image_path)

    # Получаем информацию об изображении
    image_info = ImageInfo(image_loader)
    info = image_info.get_image_info()
    print(info)

    # Переименовываем изображение
    new_name = 'new_image_name.jpg'
    renamer = ImageRenamer(image_loader)
    renamer.rename_image(new_name)
    print(f'Изображение переименовано в {new_name}')

if __name__ == "__main__":
    main()
