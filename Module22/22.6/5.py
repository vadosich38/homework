import os

text = input("Введите текст: ")
def my_write(file_path, user_text):
    file = open(file_path, 'w', encoding="utf-8")
    file.write(user_text)
    file.close()
def save(data):
    my_path = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ")
    new_path = "/"
    for i_path in my_path.split():
        new_path = os.path.join(new_path, i_path)
    if not os.path.exists(new_path):
        return print("Такого пути не существует!")

    file_name = input("Введите название файла: ")
    new_file_path = os.path.join(new_path, file_name)

    if os.path.exists(new_file_path):
        print("Такой файл уже существует!")
        choice = int(input("Введите 0, если хотите перезаписать файл. Введите 1, если хотите оставить старый файл: "))
        if choice == 0:
            my_write(new_file_path, data)
            return print("Файл успешно сохранен")
        elif choice == 1:
            return print("Строка не сохранена")
        else:
            return print("Некорректный ввод, такой команды не существует!")
    else:
        my_write(new_file_path, data)
        return print("Файл успешно сохранен")

save(text)