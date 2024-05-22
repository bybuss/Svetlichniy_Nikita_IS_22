"""
 перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
вложенных подкаталогов выводить не нужно.

 перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в PZ_7(1).py. Вывести в консоль информацию о размере
файлов в папке test.

 перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).

 перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().

 удалить файл PZ_7(1).py.  fake_PZ_7
"""

import os
import random

path2 = "../test"


def os_files_operations(path: str, operation: str, end_path: str = None) -> None:
    try:
        if operation == "make":
            os.makedirs(path)
        elif operation == "move":
            os.replace(path, end_path)
        elif operation == "rename":
            os.rename(path, end_path)
        elif operation == "remove":
            os.remove(path)
    except FileNotFoundError:
        print("\nТакого файла не существует!\nЗапустите программу еще раз, чтобы создать файл")
        with open(path, "w") as file:
            file.write("bom bom bom")
    except FileExistsError:
        # print("Папка уже существует")
        pass


def get_files_in_folder(path_to_folder: str) -> list[str]:
    return [file for file in os.listdir(path_to_folder) if os.path.isfile(os.path.join(path_to_folder, file))]


files = get_files_in_folder("../PZ_11")
print(f"Список всех файлов в PZ_11: {files}\n")

os_files_operations("../test/test1", "make")
os_files_operations("../PZ_6/PZ_6(1).py", "move", "../test/PZ_6(1).py")
os_files_operations("../PZ_6/PZ_6(2).py", "move", "../test/PZ_6(2).py")
os_files_operations("../PZ_7/test1.txt", "move", "../test/test1/test1.txt")
os_files_operations("../test/test1/test1.txt", "rename", "../test/test1/test.txt")
print("Информацяю о размере файлов в папке test:")
sizes = [print(f"{file} - {os.stat(os.path.join(path2, file)).st_size} байт") for file in os.listdir(path2) if os.path.isfile(os.path.join(path2, file))]

test = min([f"../PZ_11/{file}" for file in files], key=lambda x: len(x))
print(f"\nФайл с самым коротким именем в PZ_11:\n{os.path.basename(test)} - {os.stat(test).st_size} байт")

pdf_files = [file for file in os.listdir("../reports") if file.endswith(".pdf")]
os.startfile(f"{os.path.join("../reports", random.choice(pdf_files))}")

os_files_operations("../PZ_7/fake_PZ_7.txt", "remove")
