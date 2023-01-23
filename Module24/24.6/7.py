import random
day_counter = 0
flag = True


class Man:

    def __init__(self, name, home):
        self.name = name
        self.hungry = 50
        self.house = home

    def working(self, home):
        print("{}: иду работать на 8 часов. Сытость -20, деньги +25\n".format(self.name))
        self.hungry -= 20
        home.money += 25

    def eating(self, home):
        print("{}: беру перерыв на покушать на часик. Сытость +25, еда -25\n".format(self.name))
        self.hungry += 25
        home.eat -= 25

    def playing(self):
        print("{}: беру игровую паузу на час. Сытость -5\n".format(self.name))
        self.hungry -= 5

    def shopping(self, home):
        print("{}: иду в магазин за продуктами. Еда +50, деньги -20\n".format(self.name))
        home.eat += 50
        home.money -= 20


class House:
    money = 0
    eat = 50


def stat_print(pers, home):
    print("\nСтатистика игрока {}:\nСытость: {}\nДеньги в доме: {}\n"
          "Еда в доме: {}\n".format(pers.name, pers.hungry, home.money, home.eat))


altalmrich33 = House
vlad = Man("Vlad", altalmrich33)
olya = Man("Olya", altalmrich33)


def game(player, home):
    global flag
    stat_print(player, home)
    if player.hungry < 20:
        if player.hungry < 1:
            print("Вы проиграли! Нужно кормить своего персонажа!")
            flag = False
        else:
            print("{} проголодался, его сытость {}/100\n".format(player.name, player.hungry))
            if home.eat < 10:
                print("Но в доме мало еды, всего {}/100 Нужно идти в магазин!\n".format(home.eat))
                if home.money < 50:
                    print("{} бы сходил в магазин, да вот денег не хватает, их всего {}. "
                          "Нужно идти работать...\n".format(player.name, home.money))
                    player.working(home)
                else:
                    player.shopping(home)
            else:
                player.eating(home)
    elif coub_num == 1:
        player.working(home)
    elif coub_num == 2:
        if altalmrich33.eat > 25:
            player.eating(home)
        else:
            print("Дома недостаточно еды, нужно идти в магазин. Еды дома {}".format(home.eat))
            if home.money < 50:
                print("Дома недостаточно денег, нужно идти работать. Денег дома {}".format(home.money))
                player.working(home)
                player.shopping(home)
            else:
                player.shopping(home)
    else:
        try:
            choise = int(input("Чем заняться персонажу {} сегодня? 1 - работать, 2 - идти в магазин за продуктами, "
                                                                    "3 - играть, 4 - поесть: ".format(player.name)))
            if choise == 1:
                player.working(home)
            elif choise == 2:
                player.shopping(home)
            elif choise == 3:
                player.playing()
            elif choise == 4:
                player.eating(home)
        except ValueError:
            print("Выбор не был сделан. Персонаж {} идет работать!".format(player.name))
            player.working(home)


while True:
    if not flag:
        break
    day_counter += 1
    print(40*"-"+"День {}".format(day_counter)+"-"*40, end="\nНажмите любую кнопку для продолжения...")
    input()
    coub_num = random.randint(1, 6)
    print("-"*88)
    print("Игороку {} на кубике выпал номер {}".format(vlad.name, coub_num))
    game(vlad, altalmrich33)
    for _ in range(1):
        if not flag:
            break
        coub_num = random.randint(1, 6)
        print("Игороку {} на кубике выпал номер {}".format(olya.name, coub_num))
        game(olya, altalmrich33)




