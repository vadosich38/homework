from typing import Iterable
import os
flag = True


def gen_files_path(start_path: str ="/Users/vladyslav/Downloads", search: str = "") -> Iterable[str]:
    global flag
# собираем в переменную список объктов по указанному адресу и спрозодим циклом по именам объектов,
# сразу записываем новый путь
    path_files = os.listdir(os.path.join(os.sep, start_path))
    for file_name in path_files:
        new_path = os.path.abspath(os.path.join(os.sep, start_path, file_name))
        # если имя объекта равно искомому и это папка, то рекурсивно вызывваем этот же генератор для печати содержания.
        # Также возвращаем адрес найденной папки с искомым именем.
        # flag переключаем в False чтобы больше не вызывать передачу последующих файлов
        if file_name == search and os.path.isdir(new_path):
            flag = False
            print("\nПапка найдена!")
            yield f"Адрес папки: {new_path}"
            print("\nСодержимое папки:")

            new_files = os.listdir(new_path)
            for i_file in new_files:
                yield i_file

        elif file_name == search:
            return "Объект с искомым именем является файлом, а не папкой..."

        elif os.path.isdir(new_path):
            print(f"\nПереходим в следущую директорию: {new_path}")
            new_dir = gen_files_path(start_path=new_path, search=search)
            for j_file in new_dir:
                print(j_file)
        if flag:
            yield f"\nОбъект в директории: {new_path}"

    else:
        return


print("Печатаем: ")
my_search = gen_files_path(search="homework")
for i_path in my_search:
    print(i_path)
