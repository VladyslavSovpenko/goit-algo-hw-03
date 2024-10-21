import os
import shutil
import sys
from pathlib import Path


def copy_files_recursively(src_dir, dst_dir):
    Path(dst_dir).mkdir(parents=True, exist_ok=True)

    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        if os.path.isdir(item_path):
            try:
                copy_files_recursively(item_path, dst_dir)
            except Exception as e:
                print(f"Помилка доступу до директорії: {item_path}, {e}")

        elif os.path.isfile(item_path):
            try:
                file_extension = os.path.splitext(item)[1].lower()
                extension_dir = os.path.join(dst_dir, file_extension[1:] if file_extension else 'unknown')
                Path(extension_dir).mkdir(parents=True, exist_ok=True)

                shutil.copy2(item_path, extension_dir)
            except Exception as e:
                print(f"Помилка копіювання файлу: {item}, {e}")
        else:
            print(f"Невідомий тип: {item_path}")


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.isdir(src_dir):
        print(f"Помилка: Вихідна директорія {src_dir} не існує або недоступна.")
        sys.exit(1)

    try:
        copy_files_recursively(src_dir, dst_dir)
        print("Копіювання завершено.")
    except Exception as e:
        print(f"Загальна помилка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
