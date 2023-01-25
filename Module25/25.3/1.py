class Ship:

    def __init__(self, model):
        self.__model = model

    def go(self):
        print("Корабль куда-то идет....")

    def get_model(self):
        return self.__model


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def __str__(self):
        return "Боевой корабль {} готов выполнить боевую задачу с применением {}".format(self.get_model(), self.__gun)

    def attack(self):
        print("Военный корабль атакует с помощью оружия {}".format(self.__gun))


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.__load = 0

    def __str__(self):
        return "Грузовой корабль {} готов выполнить задачу и доставить груз. " \
               "Загруз корабля: {}".format(self.get_model(), self.__load)

    def loading(self):
        self.__load += 1
        print("Грузим корабль! Сейчас корабль загружен на {} тонн".format(self.__load))

    def un_loading(self):
        while self.__load > 0:
            self.__load -= 1
        else:
            print("Корабль разгружен. Загруз корабля {} тонн".format(self.__load))


cargo_ship = CargoShip("Патрон")
print("Модель корабля:", cargo_ship.get_model())
print(cargo_ship)
cargo_ship.go()
cargo_ship.loading()
cargo_ship.un_loading()
print(cargo_ship)

print()

war_ship = WarShip("Адмирал Бабун", "Бластер")
print("Модель корабля:", war_ship.get_model())
print(war_ship)
war_ship.attack()
war_ship.go()
print(war_ship)