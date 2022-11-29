guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    print("Сейчас на вечеринке", len(guests), "гостей")
    print(guests)
    ans = input("Гость пришел или ушел? ")
    if ans == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    elif ans == "пришел":
        name = input("Введите имя гостя: ")

        if len(guests) <= 5:
            guests.append(name)
            print("Привет,", name)
        else:
            print("Прости, Гоша, но мест нет.")
    elif ans == "ушел":
        name = input("Введите имя гостя: ")
        print("Пока", name)
        guests.remove(name)

