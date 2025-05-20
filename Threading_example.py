from threading import Thread
from shutil import copy2
from pathlib import Path
import time

"""Це приклад на багатопоточність, використання модуля threading для того щоб побачити як працює багатопоточність.
Тут виконується одночасне копіювання 4 файлів з одного каталогу в інший"""

# Шляхи до файлів
source = Path("source/")
source_1 = Path("source/file_1.exe")
source_2 = Path("source/file_2.exe")
source_3 = Path("source/file_3.exe")
source_4 = Path("source/file_4.exe")

# Шляхи переміщення файлів
target = Path("target/")
target_1 = Path("target/file_1.exe")
target_2 = Path("target/file_2.exe")
target_3 = Path("target/file_3.exe")
target_4 = Path("target/file_4.exe")

def copy_file(source: Path, target: Path):
    try:
        print(f"🔄 Початок копіювання: {source.name}")
        copy2(source, target)
        print(f"✅ Завершено копіювання: {source.name}")
    except Exception as e:
        print(f"❌ Помилка копіювання: {source.name}: {e}")

def copy_all_files_multithreaded(source: Path, target: Path):
    threads = []
    for file in source.iterdir():
        if file.is_file():
            target_file = target / file.name
            thread = Thread(target=copy_file, args=(file, target_file))
            threads.append(thread)
            thread.start()

    # Чекаємо завершення всіх потоків
    for thread in threads:
        thread.join()

def copy_files():
    start_time = time.perf_counter()
    copy_file(source_1, target_1)
    copy_file(source_2, target_2)
    copy_file(source_3, target_3)
    copy_file(source_4, target_4)
    end_time = time.perf_counter()
    print(f"⏱️ Усі копіювання завершено за {end_time - start_time:.2f} секунд")

def copy_files_multithreaded():
    # Створюємо потоки
    thread1 = Thread(target=copy_file, args=(source_1, target_1))
    thread2 = Thread(target=copy_file, args=(source_2, target_2))
    thread3 = Thread(target=copy_file, args=(source_3, target_3))
    thread4 = Thread(target=copy_file, args=(source_4, target_4))

    start_time = time.perf_counter()

    # Запускаємо потоки
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Чекаємо завершення обох потоків
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    end_time = time.perf_counter()
    print(f"⏱️ Усі копіювання завершено за {end_time - start_time:.2f} сек.")

def main():
    # Багатопоточне виконання копіювання файлів
    target.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    copy_all_files_multithreaded(source, target)
    end = time.perf_counter()
    print(f"\n⏱️ Усі копіювання завершено за {end - start:.2f} сек.")

    # Інший спосіб багатопоточного виконання копіювання файлів
    # copy_files_multithreaded()

    # Звичайне синхронне виконання копіювання файлів
    # copy_files()


if __name__ == '__main__':
    main()