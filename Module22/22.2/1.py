import os
path = input("Введите путь: ")

if os.path.exists(path):
    if os.path.isdir(path):
        print("Это директория")
    elif os.path.islink(path):
        print("Это ссылка")
    elif os.path.isfile(path):
        print("Это файл\nРазмер файла:", os.path.getsize(path), "байт")
    else:
        print("Неизвестный тип")

else:
    print("Такой путь не существует!")