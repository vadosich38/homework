oper_lst = list()
res_lst = list()
sum_res = 0
def calculating(operation_str, string_num, res_lst):
    temp = str(operation_str)
    try:
        temp = str(operation_str[0]) + str(operation_str[1]) + str(operation_str[2])
        res = eval(temp)
    except IndexError as error_msg:
        print("\nВозникла ошибка: {0}. В строке недостаточно информации для выполнения операции! "
              "Номер строки {1}.".format(error_msg, string_num + 1))
        correction(string_num, res_lst, temp)
    except NameError as error_msg:
        print("\nВозникла ошибка: {0}. В строке некорректные данные для выполнения операции! "
              "Номер строки {1}".format(error_msg, string_num + 1))
        correction(string_num, res_lst, temp)
    except SyntaxError as error_msg:
        print("\nВозникла ошибка: {0}. В строке некорректный операнд для выполнения операции! "
              "Номер строки {1}".format(error_msg, string_num + 1))
        correction(string_num, res_lst, temp)
    else:
        res_lst.append(res)
        print("Операция в строке {0} выполнена успешно! Результат операции: {1}".format(string_num + 1, res))
def correction(string_num, res_lst, error_str):
    print("Некорректная строка:", error_str)
    while True:
        choice = input("Желаете исправить ошибку в строке? y - да, n - нет: ")
        if choice == "y":
            temp = input("Введите корректную строку через пробелы: ")
            tmp_lst = temp.strip().split()
            calculating(tmp_lst, string_num, res_lst)
            return
        elif choice == "n":
            return
        else:
            print("Вы ввели некоретный ответ. Выберите команду из предложенного списка!")

with open("calc7.txt", "r", encoding="utf-8") as my_file:
    for i_string in my_file:
        oper_lst.append(i_string.strip().split())

for str_num, operation in enumerate(oper_lst):
    calculating(operation, str_num, res_lst)
else:
    sum_res = sum(res_lst)
    print("Сумма всех корректных результатов:", sum_res)


