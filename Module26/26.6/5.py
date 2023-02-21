import os


def str_counter():
    count_all = 0
    count_in_file = 0
    path = os.getcwd()
    files_in_dir = os.listdir(path)
    for file in files_in_dir:
        if file.endswith(".py"):
            with open(file, "r", encoding="utf-8") as my_file:
                for i_line in my_file:
                    if i_line.startswith("#") or i_line == "":
                        continue
                    else:
                        count_in_file += 1
                else:
                    count_all += count_in_file
                    yield "В файле {} {} строк".format(file, count_in_file)
                    count_in_file = 0
    else:
        return print("Всего {} строк во всех файлах директории".format(count_all))


for i_file_data in str_counter():
    print(i_file_data)
