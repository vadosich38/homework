flag = False


class Potato:
    stages = {0: "пустая клумба", 1: "росток", 2: "зелёная", 3: "зрелая"}

    def __init__(self, index):
        self.index = index
        self.stage = 0

    def stage_info(self):
        print("Картошка {} сейчас {}".format(self.index, Potato.stages[self.stage]))

    def is_ripe(self):
        if self.stage == 3:
            return True
        elif self.stage == 0:
            return None
        else:
            return False


class PotatoGarden:

    def __init__(self, count):
        self.pot_list = [Potato(index) for index in range(1, count + 1)]

    def grow_all_row(self, choise=0):
        if not all([x_potato.is_ripe() for x_potato in self.pot_list]):
            for y_potato in self.pot_list:
                y_potato.stage += 1
                y_potato.stage_info()
        elif choise == 1:
            print("Cобираем урожай!")
            for m_potato in self.pot_list:
                m_potato.stage = 0
                m_potato.stage_info()
        else:
            self.all_potato_stage_status()

    def all_potato_stage_status(self):
        if all([j_potato.is_ripe() for j_potato in self.pot_list]):
            return "Вся картошка поспела, можно собирать!"
        elif [j_potato.is_ripe() for j_potato in self.pot_list] == [None for _ in range(len(self.pot_list))]:
            return "Грядка пустая!"
        else:
            return "Картошка еще не поспела!"


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        self.harvest = []

    def care(self):
        print("Садовник {} засеевает грядку!".format(self.name))
        self.garden.grow_all_row()

    def harvesting(self):
        self.harvest.extend(self.garden.pot_list)
        self.garden.grow_all_row(1)


def check_free(obj):
    if obj.garden.all_potato_stage_status() == "Грядка пустая!":
        try:
            choise = int(input("Грядка садовника {} пустая! Хотите засадить грядку картошкой? 1 - да, 2 - нет: "
                               .format(obj.name)))
            if choise == 1:
                obj.care()
                print("{}\n".format(obj.garden.all_potato_stage_status()))
            else:
                print("Грядка остается пустой!\n")
            action = 0
        except ValueError:
            print("Выбор не сделан! Грядка остается пустой.\n")
    elif not obj.garden.all_potato_stage_status() == "Вся картошка поспела, можно собирать!":
        print("У садовника {} растет картошка!".format(obj.name))
        obj.garden.grow_all_row()
        print("{}\n".format(obj.garden.all_potato_stage_status()))


def check_ready(obj):
    if obj.garden.all_potato_stage_status() == "Вся картошка поспела, можно собирать!":
        try:
            action = int(input("У садовника {} созрела грядка. Собрать урожай? 1 - да, 2 - нет: "
                               .format(obj.name)))
            if action == 1:
                obj.harvesting()
                print("Количество урожая: {}\n".format(len(obj.harvest)))
            else:
                print("Урожай остается в почве...")
        except ValueError:
            print("Выбор не сделан, урожай остается в почве!\n")


gardener1 = Gardener("Оля", PotatoGarden(5))
gardener2 = Gardener("Влад", PotatoGarden(5))

for i_month in range(1, 13):
    if flag == True:
        break
    for i_date in range(1, 31):
        print("{}Сегодня {} число. Месяц {}\n".format(" " * 40, i_date, i_month) + "-" * 100)
        x = input("Нажмите любую клавишу для продолжения...\n")
        if x.lower() == "закончить игру":
            winner_points = max(len(gardener1.harvest), len(gardener2.harvest))
            winner_name = gardener1.name if (len(gardener1.harvest) > len(gardener2.harvest)) else gardener2.name

            print("Завершаю игру... Результаты игры:\nПобедил фермер {}, набрав {} очков собранного урожая"
                  .format(winner_name, winner_points))
            flag = True
            break

        else:
            check_free(gardener1)
            check_free(gardener2)

            check_ready(gardener1)
            check_ready(gardener2)
