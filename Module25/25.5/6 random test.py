import random
flag = True
max_data = 0
break_line = "-"*100
warning_line = "\n", "!" * 100, "\n"


class Roommates:
    __income_sum = 0
    __fur_count = 0
    __food_counter = 0
    __cat_food_counter = 0

    def __init__(self, name, happy=100):
        self.__name = name
        self.__hunger = 30
        self.__happy = happy
        self.__alive = True

    def __str__(self):
        return "\nСытость: {}\nСчастье: {}\n".format(self.get_hunger(), self.get_happy())

    def set_global_cat_food(self, count):
        Roommates.__cat_food_counter += count

    def get_global_cat_food(self):
        return Roommates.__cat_food_counter

    def set_global_income(self, count):
        Roommates.__income_sum += count

    def get_global_income(self):
        return Roommates.__income_sum

    def set_global_fur(self):
        Roommates.__fur_count += 1

    def get_global_fur(self):
        return Roommates.__fur_count

    def set_global_food(self, count):
        Roommates.__food_counter += count

    def get_global_food(self):
        return Roommates.__food_counter

    def get_happy(self):
        return self.__happy

    def get_name(self):
        return self.__name

    def set_happy(self, count):
        if self.__happy + count > 100:
            self.__happy = 100
        elif self.__happy + count < 10:
            self.__happy = 10
        else:
            self.__happy += count

    def set_hunger(self, count):
        if self.__hunger + count > 100:
            self.__hunger = 100
        elif self.__hunger + count < 0:
            self.__hunger = 0
        else:
            self.__hunger += count

    def get_hunger(self):
        return self.__hunger

    def get_alive(self):
        return self.__alive

    def death_hungry(self):
        print("\n{} умирает с голоду!\n".format(self.__name))
        self.__happy = -1
        self.__hunger = -1
        self.__alive = False

    def death_dipretion(self):
        print("{} умирает от депрессии!\n".format(self.__name))
        self.__happy = -1
        self.__hunger = -1
        self.__alive = False

    def cat_pet(self, cat):
        if cat.get_alive():
            print("{} гладит кота! +5 к счастью\n".format(self.get_name()))
            self.__happy += 5
            self.set_hunger(-10)
        else:
            print("{} гладит кота, но тот уже мертв! -5 от счастья\n".format(self.get_name()))
            self.__happy -= 5
            self.set_hunger(-10)

    def eat(self, house):
        if house.get_food() == 1:
            eat_value = 1
        elif house.get_food() > 30:
            eat_value = random.randint(1, 30)
        elif 1 < house.get_food() < 30:
            eat_value = random.randint(1, house.get_food())
        else:
            print("В холодильнике нет еды! {} пропускает прием пищи...".format(self.get_name()))
            eat_value = 0

        house.set_food(count=-eat_value)
        self.set_hunger(count=eat_value)
        Roommates.__food_counter += eat_value
        print("{} съел(а) {} еды. Остаток еды в холодильнике: {}\n".format(self.__name, eat_value,
                                                                           house.get_food()))


class House:
    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cat_food = 30
        self.__dirt = 0

    def __str__(self):
        return "Еды в холодильнике: {}\nКошачей еды: {}\nДенег дома: {}\nСостояние загрязнения дома: {}\n".format\
            (self.__food, self.__cat_food, self.__money, self.__dirt)

    def set_food(self, count):
        self.__food += count

    def get_food(self):
        return self.__food

    def get_dirt(self):
        return self.__dirt

    def set_dirt(self, count):
        if self.__dirt + count < 0:
            self.__dirt = 0
        else:
            self.__dirt += count

    def eat_cat_food(self, cat):
        eat_value = random.randint(1, 10)
        self.__cat_food -= eat_value
        cat.set_hunger(eat_value)
        print("Кот поел {} еды\n".format(eat_value))

    def set_cat_food(self, count):
        if self.__cat_food + count < 0:
            self.__cat_food = 1
        else:
            self.__cat_food += count

    def get_cat_food(self):
        return self.__cat_food

    def get_money(self):
        return self.__money

    def set_money(self, count):
        self.__money += count


class Cat(Roommates):
    def __init__(self, name):
        super().__init__(name, happy=0)

    def __str__(self):
        return "\nСытость кота: {}\n".format(self.get_hunger())

    def sleep(self):
        print("Кот уходит спать....")
        self.set_hunger(count=-10)

    def tear(self, house):
        print("Кот дерет обои! Грязи в доме +5\n")
        house.set_dirt(5)
        self.set_hunger(count=-10)

    def cat_pet(self, cat):
        pass

    def eat(self, house):
        if house.get_cat_food() == 1:
            eat_value = 1
        elif house.get_cat_food() > 1:
            eat_value = random.randint(1, house.get_cat_food())
        else:
            print("Кошачей еды в доме нет! Кот пропускает кормление...")
            eat_value = 0
        house.set_cat_food(-eat_value)
        self.set_hunger(count=eat_value*2)
        print("Кот съел {} еды. "
              "Остаток кошачей еды: {}.".format(eat_value, house.get_cat_food()))
        super().set_global_cat_food(eat_value)


class Kid(Roommates):
    def __init__(self, name):
        super().__init__(name, happy=0)

    def eat(self, house):
        if house.get_food() == 1:
            eat_value = 1
        elif house.get_food() > 15:
            eat_value = random.randint(1, 15)
        elif 1 < house.get_food() < 15:
            eat_value = random.randint(1, house.get_food())
        else:
            print("В холодильнике нет еды! {} пропускает прием пищи...".format(self.get_name()))
            eat_value = 0

        house.set_food(count=-eat_value)
        self.set_hunger(count=eat_value*2)
        super().set_global_food(eat_value)
        print("{} съел(а) {} еды. Остаток еды в холодильнике: {}\n".format(self.get_name(), eat_value,
                                                                           house.get_food()))

    def floor_eat(self):
        print("{} нашел что-то на полу и ест. +10 к счастью, +5 к сытости")
        self.set_hunger(count=5)
        self.set_happy(count=10)

    def play(self):
        print("{} играет! +20 к счастью")
        self.set_happy(20)

    def sleep(self):
        print("{} ушел спать...")

    def death_hungry(self):
        print("\n{} умирает с голоду! Но его вовремя спасают социальные службы и забирают в дет. дом...\n".format
              (self.get_name()))
        self.__happy = -1
        self.__hunger = -1
        self.__alive = False

    def death_dipretion(self):
        print("{} умирает от депрессии! Но его вовремя спасают социальные службы и забирают в дет. дом...\n".format
              (self.get_name()))
        self.__happy = -1
        self.__hunger = -1
        self.__alive = False


class Husband(Roommates):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        print("{} играет! +20 к счастью".format(self.get_name()))
        self.set_happy(20)
        self.set_hunger(count=-10)

    def work(self, house):
        print("{} идет работать! +150 к деньгам, -10 от счастья\n".format(self.get_name()))
        self.set_happy(count=-10)
        house.set_money(count=150)
        self.set_hunger(count=-10)
        super().set_global_income(count=150)


class Wife(Roommates):
    def shopping(self, house):
        if house.get_money() >= 40:
            print("{} идет в магазин за продуктами. Денег -40, еды в холодильнике +30, кошачей еды +10".format
                  (self.get_name()))
            house.set_money(count=-30)
            house.set_food(count=30)

            house.set_money(count=-10)
            house.set_cat_food(count=10)
            self.set_hunger(count=-10)

        else:
            print("Денег не достаточно чтобы купить все. Покупаю еду на все оставшиеся деньги 25% коту и 75% людям\n")
            available_money = house.get_money()
            print("{} идет в магазин за продуктами. Денег -{}, еды в холодильнике +{}, кошачей еды +{}".format
                  (self.get_name(), available_money, round(available_money*0.75, 0), round(available_money*0.25, 0)))
            house.set_money(count=-round(available_money*0.75, 0))
            house.set_food(count=round(available_money*0.75, 0))

            house.set_money(count=-round(available_money*0.25, 0))
            house.set_cat_food(count=round(available_money*0.25, 0))
            self.set_hunger(count=-10)

    def buy_fur(self, house):
        if house.get_money() > 350:
            self.set_happy(60)
            house.set_money(-350)
            self.set_hunger(-10)
            print("{} купила шубу за 350 денег."
                  "\nДенег дома осталось: {}"
                  "\nСчастье {} выросло на 60"
                  " и сейчас составляет {}\n".format(self.get_name(), house.get_money(), self.get_name(),
                                                     self.get_happy))
            super().set_global_fur()
        else:
            print("Денег для покупки шубы не достаточно и вместо шубы {} решила купить продукты домой".format
                  (self.get_name()))

    def cleaning(self, house):
        clean_value = random.randint(1, 100)
        house.set_dirt(-clean_value)
        print("{} убралась, в доме стало чище на {}. "
              "Общее состояние грязи дома: {}\n".format(self.get_name(), clean_value, house.get_dirt()))
        self.set_hunger(-10)


husband_1 = Husband(name="Степан")
wife_1 = Wife(name="Галина")
kitty_1 = Cat(name="Мурзик")
kitty_2 = Cat(name="Тузик")
kitty_3 = Cat(name="Барбос")
kid_1 = Kid(name="Георгий")
altalmrich32 = House()


while flag is True:
    for year in range(2023, 2026):
        if not flag:
            break
        else:
            for month in range(1, 13):
                if not flag:
                    break
                else:
                    input("Начинается новый месяц! Введите любой символ для продолжения")
                    for day in range(1, 31):
                        if husband_1.get_alive() or wife_1.get_alive() or kitty_1.get_alive():
                            print(break_line)
                            print("Начался новый день! Сегодня на календаре {}й день {}го месяца, год {}\n".format
                                  (day, month, year))
                            print(break_line)
# проверяю уровень голода каждого жильца
                            if husband_1.get_hunger() == 0 or kid_1.get_hunger() or wife_1.get_hunger() == 0 or \
                                    kitty_1.get_hunger() == 0 or kitty_2 == 0 or kitty_3 == 0:
                                print(warning_line)
                                print("Члены семьи умирают с голоду! \nСытость мужа: {}"
                                      "\nСытость жены: {}\nСытость ребенка: {}"
                                      "\nСытость кота {}: {}\nСытость кота {}: {}\nСытость кота {}: {}".format
                                    (husband_1.get_hunger(), wife_1.get_hunger(), kid_1.get_hunger(),
                                     kitty_1.get_name(), kitty_1.get_hunger(), kitty_2.get_name(), kitty_2.get_hunger(),
                                     kitty_3.get_name(), kitty_3.get_hunger()))
                                if husband_1.get_hunger() == 0:
                                    husband_1.death_hungry()
                                if wife_1.get_hunger() == 0:
                                    wife_1.death_hungry()
                                if kitty_1.get_hunger() == 0:
                                    kitty_1.death_hungry()
                                if kid_1.get_hunger() == 0:
                                    kid_1.death_hungry()
                                if kitty_2.get_hunger() == 0:
                                    kitty_2.death_hungry()
                                if kitty_3.get_hunger() == 0:
                                    kitty_3.death_hungry()

# проверяю уровень грязи в доме
                            if altalmrich32.get_dirt() > 90:
                                print(warning_line)
                                print("Дома грязно: {}\nСчастье жильцов падает на 10".format(altalmrich32.get_dirt()))
                                wife_1.set_happy(-10)
                                husband_1.set_happy(-10)
                                kid_1.set_happy(-10)
# проверяю уровень счастья каждого жильца
                            if husband_1.get_happy() == 10 or wife_1.get_happy() == 10 or kid_1.get_happy() == 10:
                                print(warning_line)
                                print("Члены семьи умирают от депрессии! \nУровень счастья мужа: {}"
                                      "\nУровень счастья жены: {}\nУровень счастья ребенка: {}".format
                                      (husband_1.get_happy(), wife_1.get_happy(), kid_1.get_happy()))
                                if husband_1.get_happy() == 10:
                                    husband_1.death_dipretion()
                                if wife_1.get_happy() == 10:
                                    wife_1.death_dipretion()
                                if kid_1.get_happy() == 10:
                                    kid_1.death_dipretion()
# выбираем действие для каждого персонажа
                            print(f"Состояние дома:\n{altalmrich32}")
# муж
                            print(break_line, "\n")
                            if husband_1.get_alive():
                                print(f"Показатели {husband_1.get_name()}: {husband_1}")
                                print("Выберите действие для {}: 1: Погладить кота, 2: Поесть, 3: Работать, "
                                      "4: Играть".format(husband_1.get_name()))
                                # choise = int(input("Ваш выбор: "))
                                choise = random.randint(1, 4)

                                if choise == 1:
                                    husband_1.cat_pet(kitty_1)
                                elif choise == 2:
                                    husband_1.eat(house=altalmrich32)
                                elif choise == 3:
                                    husband_1.work(house=altalmrich32)
                                elif choise == 4:
                                    husband_1.play()
                                else:
                                    print("Некорректный ввод! {} идет работать!\n".format(husband_1.get_name()))
                                    husband_1.work(altalmrich32)
                            else:
                                print("Муж умер...пора искать нового!")
# жена
                            print("-" * 100, "\n")
                            if wife_1.get_alive():
                                print(f"Показатели {wife_1.get_name()}:", wife_1)
                                print("Выберите действие для {}: 1: Погладить кота, 2: Поесть, "
                                      "3: Сходить в магазин за продуктами, 4: Купить шубу, 5: Убирать дома".
                                      format(wife_1.get_name()))
                                # choise = int(input("Ваш выбор: "))
                                choise = random.randint(1, 5)
                                if choise == 1:
                                    wife_1.cat_pet(kitty_1)
                                elif choise == 2:
                                    wife_1.eat(house=altalmrich32)
                                elif choise == 3:
                                    wife_1.shopping(house=altalmrich32)
                                elif choise == 4:
                                    wife_1.buy_fur(house=altalmrich32)
                                elif choise == 5:
                                    wife_1.cleaning(house=altalmrich32)
                                else:
                                    print("Некорректный ввод! {} идет в магазин!\n".format(wife_1.get_name()))
                                    wife_1.shopping(altalmrich32)
                            else:
                                print("Жена умерла...")
# кот1
                            print(break_line, "\n")
                            if kitty_1.get_alive():
                                print(f"Показатели {kitty_1.get_name()}:", kitty_1)
                                print("Выберите действие для {}: 1: Спать, 2: Поесть, 3: Драть обои".format
                                      (kitty_1.get_name()))
                                # choise = int(input("Ваш выбор: "))
                                choise = random.randint(1, 3)
                                if choise == 1:
                                    kitty_1.sleep()
                                elif choise == 2:
                                    kitty_1.eat(house=altalmrich32)
                                elif choise == 3:
                                    kitty_1.tear(house=altalmrich32)
                                else:
                                    print("Некорректный ввод! {} идет спать!\n".format(kitty_1.get_name()))
                                    kitty_1.sleep()
                            else:
                                print("Кот {} не выдержал такой жизни и покинул этот мир...".format(kitty_1.get_name()))
# кот2
                                print(break_line, "\n")
                                if kitty_2.get_alive():
                                    print(f"Показатели {kitty_2.get_name()}:", kitty_2)
                                    print("Выберите действие для {}: 1: Спать, 2: Поесть, 3: Драть обои".format
                                          (kitty_2.get_name()))
                                    # choise = int(input("Ваш выбор: "))
                                    choise = random.randint(1, 3)
                                    if choise == 1:
                                        kitty_2.sleep()
                                    elif choise == 2:
                                        kitty_2.eat(house=altalmrich32)
                                    elif choise == 3:
                                        kitty_2.tear(house=altalmrich32)
                                    else:
                                        print("Некорректный ввод! {} идет спать!\n".format(kitty_2.get_name()))
                                        kitty_2.sleep()
                                else:
                                    print("Кот не выдержал такой жизни и покинул этот мир...".format(kitty_2.get_name()))
# кот3
                                    print(break_line, "\n")
                                    if kitty_3.get_alive():
                                        print(f"Показатели {kitty_3.get_name()}:", kitty_3)
                                        print("Выберите действие для {}: 1: Спать, 2: Поесть, 3: Драть обои".format
                                              (kitty_3.get_name()))
                                        # choise = int(input("Ваш выбор: "))
                                        choise = random.randint(1, 3)
                                        if choise == 1:
                                            kitty_3.sleep()
                                        elif choise == 2:
                                            kitty_3.eat(house=altalmrich32)
                                        elif choise == 3:
                                            kitty_3.tear(house=altalmrich32)
                                        else:
                                            print("Некорректный ввод! {} идет спать!\n".format(kitty_3.get_name()))
                                            kitty_3.sleep()
                                    else:
                                        print("Кот не выдержал такой жизни и покинул этот мир...".format
                                              (kitty_3.get_name()))
# ребенок
                            print(break_line, "\n")
                            if kid_1.get_alive():
                                print(f"Показатели {kid_1.get_name()}:", kid_1)
                                print("Выберите действие для {}: 1: Спать, 2: Поесть, 3: Поесть с пола, 4: Игать".format
                                      (kitty_1.get_name()))
                                # choise = int(input("Ваш выбор: "))
                                choise = random.randint(1, 4)
                                if choise == 1:
                                    kid_1.sleep()
                                elif choise == 2:
                                    kid_1.eat(house=altalmrich32)
                                elif choise == 3:
                                    kid_1.floor_eat()
                                elif choise == 4:
                                    kid_1.play()
                                else:
                                    print("Некорректный ввод! {} идет спать!\n".format(kid_1.get_name()))
                                    kid_1.sleep()
                            else:
                                print("Ребенка забрали в детский дом...")
                            altalmrich32.set_dirt(5)
                        else:
                            print(break_line)
                            print("Все умерли! Начинать новый день больше не для кого...жизнь тлен...")
                            print(break_line)
                            flag = False
                            max_data = ((year-2023) * 12 * 30) + ((month - 1) * 30) + day
                            break

print(break_line, "\nСтатистика вашей игры:\nВсего игровых дней: {}\nВсего съедено еды: {} \nВсего заработано денег: {}"
      "\nВсего куплено шуб: {}\nВсего съедено кошачей еды: {}".format(max_data, wife_1.get_global_food(),
                                                                      wife_1.get_global_income(),
                                                                      wife_1.get_global_fur(),
                                                                      wife_1.get_global_cat_food()))
