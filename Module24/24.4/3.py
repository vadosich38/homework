

class Potato:
    stages = {0: "Пустая клумба", 1: "Росток", 2: "Зелёная", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.stage = 0

    def stage_info(self):
        print("Картошка {} сейчас {}".format(self.index, Potato.stages[self.stage]))

    def is_ripe(self):
        if self.stage == 3:
            return True
        else:
            return False


class PotatoGarden:

    def __init__(self, count):
        self.pot_list = [Potato(index) for index in range(1, count+1)]

    def grow_all_row(self):
        if not all([x_potato.is_ripe() for x_potato in self.pot_list]):
            for y_potato in self.pot_list:
                y_potato.stage += 1
                y_potato.stage_info()
        else:
            self.all_potato_stage_status()

    def all_potato_stage_status(self):
        if all([j_potato.is_ripe() for j_potato in self.pot_list]):
            return "Вся картошка поспела, можно собирать!"
        else:
            return "Картошка еще не поспела!"


row1 = PotatoGarden(5)
row2 = PotatoGarden(5)

for i in range(3):
    print("Картошка растет!")
    row1.grow_all_row()
    print("{}\n".format(row1.all_potato_stage_status()))
