class Robot:

    def __init__(self, model):
        self.__model = model


class VacuumCleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.__bag = 0

    def operate(self):
        x = 1
        while x == 1:
            self.__bag += 1
            print("Пылесошу пол, заполненность мешка: {}".format(self.__bag))
            x = int(input("Введите 0, чтобы остановить или 1 чтобы продолжить: "))
        else:
            x = int(input("Введите 0, чтобы очистить мешок или 1 чтобы оставить полным: "))
            if x == 0:
                self.__clean_bag()

    def __clean_bag(self):
        print("Очищаю мешок")
        self.__bag = 0


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def operate(self):
        print("Защищаю военный объект с применением оружия: {}".format(self.__gun))


class Submarine(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun
        self.__deep = 0

    def operate(self):
        print("Охраняю военный объект на воде с применением оружия: {}. "
              "Нынешняя глубина: {}".format(self.__gun, self.__deep))
        add_deep = int(input("Прикажите погрузиться введя значение более нуля "
                             "или введите 0, чтобы остаться на прежней глубине: "))
        if add_deep > 0:
            self.__deeping(add_deep)
        else:
            print("Остается на прежней глубине, Капитан!")

    def __deeping(self, add_deep):
        self.__deep += add_deep
        print("Погружаюсь на {} метров. Нынещняя глубина: {}".format(add_deep, self.__deep))


cleaner = VacuumCleaner("Пылик2000")
war_robot = WarRobot("Боец2", "Лазер")
war_submarine = Submarine("Глот", "Ядерная торпеда")

cleaner.operate()
war_robot.operate()
war_submarine.operate()

cleaner.operate()
war_robot.operate()
war_submarine.operate()

