str_counter = 0
symb_sum = 0

with open("people.txt") as names_file:
    for i_name in names_file:
        try:
            str_counter += 1
            name_len = len(str(i_name).strip())
            if name_len < 3:
                raise ValueError("Ошибка! Имя {0} короче 3 букв и не будет добавлено в сумму! Строка: {1}".
                                                                                format(i_name.strip(), str_counter))
            else:
                symb_sum += name_len
        except ValueError:
            error_msg = "Ошибка! Имя {0} короче 3 букв и не будет добавлено в сумму! Строка: {1}".format\
                                                                                        (i_name.strip(), str_counter)
            with open("logs1.log", "a") as res_file:
                res_file.write(error_msg)
            print(error_msg)
    else:
        print("Сумма букв в именах:", symb_sum)