import math


class Car:
    def __init__(self, x, y, corner):
        self.x = x
        self.y = y
        self.__corner = corner
        self.__adometr = 0
        self.__fuel = 100

    def driving(self, distance, corner, passagers=0):
        new_x = self.x + distance * math.cos(corner)
        new_y = self.y + distance * math.sin(corner)
        print("Автомобиль собирается проехать {} киллометров в направлении точки x:{} y:{}".format
                                                                                            (distance, new_x, new_y))
        self.expens_fuel(distance, new_x, new_y)

    def get_adometr(self):
        return self.__adometr

    def set_adometr(self, distance):
        self.__adometr += distance

    def set_fuel(self, expens):
        self.__fuel -= expens

    def get_fuel(self):
        return self.__fuel

    def expens_fuel(self, distance, x, y, passagers=0):
        expens = (distance / 100) * 10
        if self.__fuel > expens:
            self.set_fuel(expens)
            self.set_adometr(distance)
            self.x = x
            self.y = y
            print("\nАвтомобиль проехал {} киллометров."
                  "\nОбщий пробег автомобиля: {} киллометров."
                  "\nПотрачено топлива: {} л."
                  "\nОстаток топлива в баке {} л."
                  "\nНовое положение автомобиля x:{} y:{}\n".format(distance, self.get_adometr(), expens, self.__fuel,
                                                                  self.x, self.y))
        else:
            difference = expens - self.__fuel
            print("Автомобиль не может проехать {} киллометров. Недостаточно топлива в баке! Нужно дозаправить еще "
                  "{} литров".format(distance, difference))


class Bus(Car):
    def __init__(self, x, y, corner):
        super().__init__(x=x, y=y, corner=corner)
        self.__passagers = 0
        self.__money = 0

    def go_to(self, count):
        self.__passagers += count

    def come_out(self, count):
        self.__passagers -= count

    def driving(self, distance, corner, passagers=0):
        new_x = self.x + distance * math.cos(corner)
        new_y = self.y + distance * math.sin(corner)
        print("Автобус собирается проехать {} киллометров в направлении точки x:{} y:{}".format
                                                                                            (distance, new_x, new_y))
        self.expens_fuel(distance, new_x, new_y, passagers)

    def set_money(self, income):
        self.__money += income

    def expens_fuel(self, distance, x, y, passagers=0):
        self.go_to(passagers)
        income = passagers * 10
        self.set_money(income)
        expens = (distance / 100) * 10
        if self.get_fuel() > expens:
            self.set_fuel(expens)
            self.set_adometr(distance)
            self.x = x
            self.y = y
            print("\nАвтобус проехал {} киллометров."
                  "\nОбщий пробег автобуса : {} киллометров."
                  "\nПотрачено топлива: {} л."
                  "\nОстаток топлива в баке {} л."
                  "\nПеревезено пассажиров: {} человек"
                  "\nВсего заработано денег: {}"
                  "\nНовое положение автобуса x:{} y:{}\n".format(distance, self.get_adometr(), expens, self.get_fuel(),
                                                                  self.__passagers, self.__money, self.x, self.y))
            self.come_out(passagers)
        else:
            difference = expens - self.get_fuel()
            print("Автобус не может проехать {} киллометров. Недостаточно топлива в баке! Нужно дозаправить еще "
                  "{} литров".format(distance, difference))


bmw = Car(x=0, y=0, corner=1)
bmw.driving(distance=10, corner=11)
bmw.driving(distance=100, corner=121)
bmw.driving(distance=1000, corner=10)
print("-"*90)

bus18 = Bus(x=0, y=0, corner=0)
bus18.driving(distance=100, corner=1, passagers=10)
bus18.driving(distance=90, corner=90, passagers=1)
bus18.driving(distance=19, corner=100, passagers=15)
bus18.driving(distance=1000, corner=200, passagers=100)
