def check():
    delete = 0
    start = 0
    n = int(input("Сколько людей в кругу: "))
    k = int(input("Какой номер выбывает: "))
    people = []

    for man in range(1, n + 1):
        people.append(man)

    for mult in range(len(people)):
        if len(people) == 1:
            print("\nОставшийся победитель:", people)
            break
        else:
            print("\nТекущий круг:", people)
            print("Счет начинается с номера", people[start])
            delete = (start + k - 1) % len(people)
            print("Выбывает человек под номером", people[delete])
            people.pop(delete)

            if len(people) <= delete:
                start = 0
            else:
                start = delete

check()

