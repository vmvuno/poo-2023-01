import os
import re


def count_classes(path: str = os.getcwd()) -> None:
    dir_files = os.listdir(path)
    class_count = 0
    t_directories_count = 0

    for file in dir_files:
        a_path = os.path.join(path, file)
        if os.path.isdir(a_path) and re.search(r't\d{2}$', a_path):
            t_directories_count += 1
            inner_dir_files = os.listdir(a_path)
            for inner_file in inner_dir_files:
                if re.search(r'.py$', inner_file):
                    with open(os.path.join(a_path, inner_file),
                              encoding='utf8') as file_handle:

                        content = file_handle.readlines()

                    for line in content:
                        if re.search(r'^class .*:', line.strip()):
                            class_count += 1

    print(f'Há {class_count} classe{"" if class_count < 2 else "s"} '
          f'distribuídas em {t_directories_count} '
          f'diretório{"" if t_directories_count < 2 else "s"} '
          f'com formato t[n]')
