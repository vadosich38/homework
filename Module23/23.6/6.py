user_name = input("Введите ваше имя: ")
choice = "start"
while choice != "stop":
    choice = input("Введите ваш выбор: stop - 'Завершить программу', x - 'Посмотреть текущий текст чата', "
                   "o - 'Отправить сообщение': ")
    if choice == "x":
        with open("chat.txt", "r", encoding="utf-8") as chat_file:
            chat_text = chat_file.read()
        print("\n{}".format(chat_text))
    elif choice == "o":
        msg = input("Введите свое сообщение: ")
        with open("chat.txt", "a", encoding="utf-8") as chat_file:
            chat_file.write("{0} пишет: {1}\n".format(user_name, msg))
    else:
        print("Некорректный ввод! Выберите команду из предложенного списка.")

