synonyms1 = dict()
synonyms2 = dict()
def menu():
    action = input("Выберите действие: + - добавить пару, ? - найти синоним, x - закончить работу: ")
    if action == "+":
        words_list = input("Введите слова: ").split(" - ")
        synonyms1[words_list[0]] = words_list[1]
        synonyms2[words_list[1]] = words_list[0]
        menu()
    elif action == "?":
        word = input("Введите искомое слово: ")
        if word.capitalize() in synonyms1:
            print("Синоним {0} - {1}".format(word.capitalize(), synonyms1[word.capitalize()]))
            menu()
        elif word.capitalize() in synonyms2:
            print("Синоним {0} - {1}".format(word.capitalize(), synonyms2[word.capitalize()]))
            menu()
        else:
            print("Такого слова нет в словаре!")
            menu()
    elif action == "x":
        print("Завершение работы...")
    else:
        print("Такой команды нет!\n")
        menu()


menu()