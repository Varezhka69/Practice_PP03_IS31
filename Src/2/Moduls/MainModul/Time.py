import tkinter as tk
import time
import sys
from gui import ImageInfoApp

def measure_time_and_memory(func):
    """Декоратор для измерения времени и памяти."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало времени
        start_memory = sys.getsizeof(args) + sys.getsizeof(kwargs)  # Начальный размер

        result = func(*args, **kwargs)  # Вызов функции

        end_time = time.time()  # Конец времени
        end_memory = sys.getsizeof(result)  # Размер результата

        print(f"Время выполнения: {end_time - start_time:.6f} секунд")
        print(f"Используемая память: {end_memory - start_memory} байт")
        return result
    return wrapper

@measure_time_and_memory
def main():
    root = tk.Tk()
    app = ImageInfoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
