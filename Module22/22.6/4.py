import os

my_path = input("Введите путь каталога: ")
counter_dict = {"size": 0, "files": 0, "folders": 0}


def grabber(directory, counter):
    for i_elem in os.listdir(directory):
        new_path = os.path.abspath(os.path.join(directory, i_elem))
        if os.path.isdir(new_path):
            counter["folders"] += 1
            grabber(new_path, counter)
        else:
            counter["size"] += os.path.getsize(new_path)
            counter["files"] += 1
    return counter


if os.path.exists(my_path):
    if not os.path.isdir(my_path):
        print("Вы ввели путь к файлу, а не к папке!")
    else:
        res = grabber(my_path, counter_dict)
        print("Общий размер каталога: {} кб.\nКоличество подкаталогов: {}\nКоличество файлов: {}".
                                                        format(round(res["size"]/1024, 2), res["folders"], res["files"]))
else:
    print("Такого пути не существует!")