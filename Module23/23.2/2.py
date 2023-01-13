file_ages = open("ages.txt", "r", encoding="utf-8")
file_names = open("names.txt", "r", encoding="utf-8")
names_list = list()
ages_list = list()

for i_name in file_names:
    names_list = i_name.strip().split(", ")
    for i_age in file_ages:
        ages_list.append(i_age.strip())

full_dict = dict(zip(names_list, ages_list))
file_ages.close()
file_names.close()

try:
    res_file = open("result.txt", "x", encoding="utf-8")
    res_file.close()
except FileExistsError:
    print("Такой файл уже существует! Открываю его.")

try:
    res_file = open("result.txt", "a", encoding="utf-8")
    for i_key, i_value in full_dict.items():
        try:
            res_file.write("{0} –– {1}\n".format(i_key, i_value))
#            res_file.write(100)
        except TypeError:
            print("Тип данных не соответствует требованиям записи в файл!")
    else:
        print("Запись окончена!")
        res_file.close()
except IsADirectoryError:
    print("Созданный объект является папкой, а не текстовым файлом!")

