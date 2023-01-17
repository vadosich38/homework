oper_lst = list()
res_lst = list()
with open("calc.txt", "r", encoding="utf-8") as my_file:
    for i_string in my_file:
        oper_lst.append(i_string.strip().split())

for str_num, operation in enumerate(oper_lst):
    try:
        temp = str(operation[0]) + str(operation[1]) + str(operation[2])
        res = eval(temp)
    except IndexError as error_msg:
        print("Возникла ошибка: {0}. В строке недостаточно информации для выполнения операции! "
              "Номер строки {1}".format(error_msg, str_num+1))
    except NameError as error_msg:
        print("Возникла ошибка: {0}. В строке некорректные данные для выполнения операции! "
              "Номер строки {1}".format(error_msg, str_num+1))
    except SyntaxError as error_msg:
        print("Возникла ошибка: {0}. В строке некорректный операнд для выполнения операции! "
              "Номер строки {1}".format(error_msg, str_num+1))
    else:
        res_lst.append(res)
        print("Операция в строке {0} выполнена успешно! Результат операции: {1}".format(str_num+1, res))
else:
    sum_res = sum(res_lst)
    print("Сумма всех корректных результатов:", sum_res)

