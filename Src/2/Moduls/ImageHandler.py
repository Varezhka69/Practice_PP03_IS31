from PIL import Image

def get_image_info(file_path):
    # Открываем изображение и получаем его информацию
    with Image.open(file_path) as img:
        width, height = img.size
        format = img.format

    # Возвращаем отформатированное сообщение с информацией об изображении
    return f"Файл: {file_path}\\nФормат: {format}\\nРазмер: {width}x{height} пикселей"
