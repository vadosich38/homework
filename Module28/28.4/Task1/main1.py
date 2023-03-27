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

    def get_speed(self) -> int:
        return self.__speed

    def set_speed(self, value: int) -> None:
        self.__speed = value

    def change_status(self, value: bool) -> None:
        self.__move_status = value

    def move(self, speed: int) -> None:
        """
        Функция движения трансопрта.
        :param speed: скорость движения транспорта
        :return: None
        """
        if self.__move_status:
            print("Транспорт уже едет, скорость: {}".format(self.get_speed()))
        else:
            self.change_status(value=True)
            self.set_speed(value=speed)
            print("Транспорт начал движение, скорость: {}".format(self.get_speed()))

    def stop(self) -> None:
        self.set_speed(value=0)
        self.change_status(value=False)
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


my_auto = Auto(color="Blau")
my_auto.signal()
my_auto.move(speed=20)
my_auto.stop()
print("-"*90)

my_boat = Boat(color="Green")
my_boat.signal()
my_boat.move(speed=30)
my_boat.stop()
print("-"*90)

my_amfiby = Amfiby(color="Black")
my_amfiby.signal()
my_amfiby.move(speed=25)
my_amfiby.stop()
my_amfiby.musik()
print("-"*90)
