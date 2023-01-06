import os

dir = input("Ищем в: ")
file_name = input("Введите имя файла: ")

def my_open(num, list):
    file = open(list[num-1], "r")
    for string in file:
        print(string, end="")
def search_file(directory, file, dir_list=[]):
    print("Переходим в", directory)

    for i_elem in os.listdir(directory):
        path = os.path.join(directory, i_elem)
        print("     Смотрим путь:", path)
        if i_elem == file:
            dir_list.append(path)
        elif os.path.isdir(path):
            print("\nЭто директория")
            search_file(path, file)

    return dir_list

if os.path.exists(dir):
    res_list = search_file(dir, file_name)
    if res_list:
        print("\nРезультат поиска:")
        for index, res_dir in enumerate(res_list):
            print("Файл {0}: {1}".format(index+1, res_dir))
        choose = int(input("Какой файл считать: "))
        my_open(choose, res_list)
    else:
        print("\nФайл не найден!")
else:
    print("Такой директории не существует!")
