data_list = list()
with open("registrations.txt") as file_data:
    for i_data in file_data:
        data_list.append(i_data.strip().split())


for i_data in data_list:
    try:
        if len(i_data) == 0:
            raise IndexError("В строке нет данных")
        if not i_data[0].isalpha():
            raise NameError("Имя содержит запрещенные знаки")
        if "@" not in i_data[1] and "." not in i_data[1]:
            raise SyntaxError("Имейл указан не верно")
        if int(i_data[2]) < 10 or int(i_data[2]) > 99:
            raise ValueError("Возраст больше 99 или меньше 10")
    except IndexError as error_name:
        print("В строке нет данных")
        with open("registrations_bad.log", "a", encoding="utf-8") as res_file:
            res_file.write("Строка {0} вызывает ошибку: {1}\n".format(i_data, error_name))
    except NameError as error_name:
        print("Имя содержит запрещенные знаки")
        with open("registrations_bad.log", "a", encoding="utf-8") as res_file:
            res_file.write("Строка {0} вызывает ошибку: {1}\n".format(i_data, error_name))
    except SyntaxError as error_name:
        print("Имейл указан не верно")
        with open("registrations_bad.log", "a", encoding="utf-8") as res_file:
            res_file.write("Строка {0} вызывает ошибку: {1}\n".format(i_data, error_name))
    except ValueError as error_name:
        print("Возраст больше 99 или меньше 10")
        with open("registrations_bad.log", "a", encoding="utf-8") as res_file:
            res_file.write("Строка {0} вызывает ошибку: {1}\n".format(i_data, error_name))
    else:
        with open("registrations_good.log", "a", encoding="utf-8") as res_file:
            res_file.write("{0} {1} {2}\n".format(i_data[0], i_data[1], i_data[2]))
