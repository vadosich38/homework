def check():
    flag = True
    ip_list = input("Введите айпи адрес: ").split(".")
    if len(ip_list) < 4 or "," in ip_list:
        print("Адрес - это четыре числа, разделённые точками")
        flag = False
    else:
        for num in ip_list:
            if num.isdigit():
                if int(num) < 0 or int(num) > 255:
                    print("Ошибка! Неверное значение: {0} должно быть в диапазоне от 0 до 250!".format(num))
                    flag = False
            else:
                print("Ошибка! Значение {0} должно быть в диапазоне от 0 до 250!".format(num))
                flag = False
        if flag:
            print("Адрес корректный!")
check()