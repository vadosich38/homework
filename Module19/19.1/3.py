contacts_dict = dict()
while True:
    command = input("Введите команду: \n+ - добавить новый контакт, x - завершить работу, = o - найти контакт: ")
    if command == "x":
        break
    elif command == "o":
        name = input("Введите имя контакта: ")
        if name in contacts_dict:
            print("Номер телефона контакта {}:".format(name), contacts_dict[name])
        else:
            print("Такого контакта еще нет!")
    elif command == "+":
        name = input("Введите имя контакта: ")
        if name in contacts_dict:
            command = input("Этот контакт уже добавлен в телефонную книгу. Хотите изменить его номер телефона? \n+ да, - нет: ")
            print("Записаный номер телефона:", contacts_dict[name])
            if command == "+":
                tel_num = input("Введите номер телефона: ")
                contacts_dict[name] = tel_num
                print("Контакт обновлен!")
            elif command == "-":
                continue
            else:
                print("Ошибка ввода! Такой команды нет. Вы возвращаетесь в главное меню.")
        else:
            tel_num = input("Введите номер телефона: ")
            contacts_dict[name] = tel_num
            print("Новый контакт добавлен!")
    else:
        print("Ошибка ввода! Такой команды нет.")
