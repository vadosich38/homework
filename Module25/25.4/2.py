class CanFly:
    def __init__(self, high=0, speed=0):
        self.high = high
        self.speed = speed

    def take_off(self):
        print("Взлетела")
        pass

    def flying(self):
        print("Летит")
        pass

    def set_down(self):
        self.high = 0
        self.speed = 0
        print("Посадка")

    def data_print(self):
        print("Высота: {}, скорость: {}".format(self.high, self.speed))


class Butterfly(CanFly):
    def take_off(self):
        self.high = 1
        print("Взлетела")

    def flying(self):
        self.speed = 0.5
        print("Летит")


class Rocket(CanFly):
    def take_off(self):
        self.high = 500
        self.speed = 1000
        print("Взлетела")

    def set_down(self):
        self.high = 0
        self.speed = 0
        print("Ракета достигла цели, произошел взрыв!")

    def air_boom(self):
        self.high = 0
        self.speed = 0
        print("Ракети взорвалась в воздухе и не достигла цели!")


obj1 = Butterfly()
obj2 = Rocket()

obj1.data_print()
obj1.take_off()
obj1.data_print()
obj1.flying()
obj1.data_print()
obj1.set_down()
obj1.data_print()
print()
obj2.data_print()
obj2.take_off()
obj2.data_print()
obj2.flying()
obj2.data_print()
obj2.set_down()
obj2.data_print()
