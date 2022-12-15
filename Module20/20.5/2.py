contacts_dict = dict()

def name_input():
    name = input("Введите имя контакта: ")
    sur_name = input("Введите фамилию контакта: ")
    return name, sur_name

def search(contacts_dict):
    name = name_input()
    if name in contacts_dict:
        print("Номер телефона контакта {0} {1}:".format(name[0], name[1]), contacts_dict[name])
    else:
        command = input("Такого контакта еще нет! Хотите добавить его? '+' - да, '-' - нет: ")
        if command == "+":
            add_contact(contacts_dict)
        elif command == "-":
            print("Вы возращаетесь в главное меню...")
            invite(contacts_dict)
        else:
            print("Такой команды нет! Вы возращаетесь в главное меню..")

def add_contact(contacts_dict):
    name = name_input()
    if name in contacts_dict:
        command = input("Этот контакт уже добавлен в телефонную книгу. Хотите изменить его? \n+ да, - нет: ")
        if command == "+":
            print("Вы хотите изменить контакт:", name[0], name[1], contacts_dict[name])
            command = input("n - если вы хотите изменить имя, p - если вы хотите изменить номер телефона: ")
            if command == "p":
                tel_num = input("Введите новый номер телефона: ")
                contacts_dict[name] = tel_num
                print("Контакт обновлен!")
            elif command == "n":
                temp_contact = contacts_dict.pop(name)
                contacts_dict[name_input()] = temp_contact
                temp_contact = ""
                print("Контакт обновлен!")
        elif command == "-":
            print("Вы возращаетесь в главное меню...")
            invite(contacts_dict)
    else:
        tel_num = input("Введите номер телефона: ")
        contacts_dict[name] = tel_num
        print("Новый контакт добавлен!")

def invite(contacts_dict):
    while True:
        print("\nВаша телефонная книга готова к работе! \n")
        command = input("Введите команду: \n'+' - добавить новый контакт, 'x' - завершить работу, 'o' - найти контакт: ")
        if command == "x":
            break
        elif command == "o" or command == "+":
            menu(contacts_dict, command)
        else:
            print("Ошибка ввода! Такой команды нет.")

def menu(contacts_dict, command):
        if command == "o":
            search(contacts_dict)
        elif command == "+":
            add_contact(contacts_dict)

invite(contacts_dict)
