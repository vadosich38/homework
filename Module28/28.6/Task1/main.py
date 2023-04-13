from abc import ABC, abstractmethod


class Mixin:
    """
    Класс примесь для магнитолы в транспорт
    """
    def musik(self) -> None:
        print("Проигрываю музыку")


class Transport(ABC):
    """
    Абстрактный родительский класс Транспорт.
    """
    def __init__(self, color: str) -> None:
        """
        Конструктор транспорта.
        :param color: передает цвет транспорта
        """
        self.__color = color
        self.__speed = 0
        self.__move_status = False

    def __str__(self) -> str:
        return "\nЦвет транспорта: {}".format(self.__color)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        self.__speed = value

    @property
    def status(self):
        return self.__move_status

    @status.setter
    def status(self, value: bool) -> None:
        self.__move_status = value

    def move(self, speed: int) -> None:
        """
        Функция движения трансопрта.
        :param speed: скорость движения транспорта
        :return: None
        """
        if self.__move_status:
            print("Транспорт уже едет, скорость: {}".format(self.__speed))
        else:
            self.status = True
            self.speed = speed
            print("Транспорт начал движение, скорость: {}".format(self.__speed))

    def stop(self) -> None:
        self.speed = 0
        self.status = False
        print("Трансопорт останавливается")

    @abstractmethod
    def signal(self):
        print("Транспорт подает сигнал!")


class Auto(Transport):
    """
    Класс Машина
    """
    def signal(self) -> None:
        print("Машина подает сигнал!")


class Boat(Transport):
    """
    Класс Лодка
    """
    def signal(self) -> None:
        print("Лодка подает сигнал!")


class Amfiby(Transport, Mixin):
    """
    Класс Амфибия
    """
    def signal(self) -> None:
        print("Амфибия подает сигнал!")


my_auto = Auto(color="Blue")
print(my_auto)
my_auto.color = "Green"
my_auto.signal()
my_auto.move(speed=20)
my_auto.stop()
print(my_auto)
print("-"*90)

my_boat = Boat(color="Lila")
print(my_boat)
my_boat.color = "Blue"
my_boat.signal()
my_boat.move(speed=30)
my_boat.stop()
print(my_boat)
print("-"*90)

my_amfiby = Amfiby(color="Black")
print(my_amfiby)
my_amfiby.color = "White"
my_amfiby.signal()
my_amfiby.move(speed=25)
my_amfiby.stop()
my_amfiby.musik()
print(my_amfiby)
print("-"*90)
