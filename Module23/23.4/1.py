names_file = open("people.txt", "r", encoding="utf-8")
summ = 0
for i_string in names_file:
    try:
        name_lenth = len(i_string)
        if str(i_string).endswith("\n"):
            name_lenth -= 1
        if name_lenth < 3:
            raise ValueError('Имя {} короче 3 букв. Программа завершается!'.format(i_string.strip()))
        else:
            summ += name_lenth
    except BaseException:
        print("Обнаружена ошибка!")
        raise
else:
    print("Сумма:", summ)