class Robot:
    """
    Материнский класс роботов. Распечатывает сообщение, что объект является роботом
    """

    def __init__(self, model: str):
        self.__model = model

    def get_model(self) -> str:
        """
        Функция возврата модели робота
        :return: модель робота
        """
        return self.__model

    def __str__(self) -> str:
        return "Я - робот! Модель: {}".format(self.get_model())


class FlyingRobot(Robot):
    """
    Материнский класс летающих роботов. Родитель: Robot (робот).

    Args:
        model (str):
    """
    def __init__(self, model: str) -> None:
        super().__init__(model)
        self.__speed: int = 0
        self.__hight: int = 0
        self.__flying: bool = False

    def fly_up(self) -> None:
        """
        функция взлета объекта
        :return: None
        """
        if not self.__flying:
            self.set_hight(count=30)
            self.set_status(status=True)
            print("Успешно взлетел!")
        else:
            print("Ваш робот уже взлетел и парит в небе")

    def flying(self, speed: int) -> None:
        """
        Функция полета
        :param speed: передаем скорость полета объекта
        :return: None
        """
        self.set_speed(count=speed)
        print("Робот летит со скоростью {}".format(self.get_speed()))

    def stop(self) -> None:
        """
        Функция остановки объекта на месте в небе
        :return: None
        """
        if self.__speed != 0:
            self.set_speed(count=-self.get_speed())
            print("Робот остановился в небе")
        else:
            print("Ваш робот уже остановлен и парит в небе")

    def get_status(self) -> bool:
        """
        Функция получения состояния объекта
        :return: None
        """
        return self.__flying

    def landing(self) -> None:
        """
        Функция посадки объекта
        :return: None
        """
        if not self.get_status:
            print("Ваш робот уже посажен на землю")
        else:
            if self.__speed != 0:
                self.stop()

            self.set_speed(count=-self.get_speed())
            self.set_hight(count=-self.get_hight())
            self.set_status(status=False)
            print("Успешно приземлился. Скорость: {}\nВысота: {}\n".format(self.get_speed(), self.get_hight()))

    def set_status(self, status: bool) -> None:
        """
        Функция установки состояния объекта
        :param status: сам статус
        :return: None
        """
        self.__flying = status

    def set_speed(self, count: int) -> None:
        """
        Функция установки скорости объекта
        :param count: переданая скорость
        :return: None
        """
        self.__speed += count

    def get_speed(self) -> int:
        """
        Функция получения скорости объекта
        :return: скорость (int)
        """
        return self.__speed

    def set_hight(self, count) -> None:
        """
        Функция установки высоты объекта
        :param count: переданая высота
        :return: None
        """
        self.__hight += count

    def get_hight(self) -> int:
        """
        Функция получения высоты
        :return: высота (int)
        """
        return self.__hight

    def __str__(self) -> str:
        return "Я - летающий робот. Модель: {}".format(self.get_model())


class WarRobot(FlyingRobot):
    """
    Класс военный робот. Родитель: FlyingRobot (летающий робот)
    """
    def __init__(self, weapon: str, model: str) -> None:
        super().__init__(model=model)
        self.__weapon: str = weapon

    def get_weapon(self) -> str:
        """
        Функция возврщает название оружия робота
        :return: название оружия (str)
        """
        return self.__weapon

    def __str__(self) -> str:
        return "Я - военный летающий робот. Модель: {}".format(self.get_model())

    def operate(self) -> None:
        """
        Функция задачи военного робота.
        :return: None
        """
        print("Веду защиту защиту военного объекта с воздуха с помощью {}".format(self.get_weapon))


class ScoutRobot(FlyingRobot):
    """
    Класс робота-разведчика. Родитель: FlyingRobot (летающий робот)
    """
    def __init__(self, model: str) -> None:
        super().__init__(model=model)
        self.__position: int = 0

    def set_position(self, distance: int) -> None:
        """
        Функция установки положения робота.
        :param distance: дистанция, которую пролетел робот (int)
        :return: None
        """
        self.__position += distance

    def __get_position(self) -> int:
        """
        Функция получения позиции робота.
        :return: позицию робота (int)
        """
        return self.__position

    def operate(self) -> None:
        """
        Функция основной задачи робота-разведчика.
        :return: None
        """
        print("Веду разведку с воздуха")
        self.set_position(distance=1)


#создаю робота и печатаю его сообщение
my_robot = Robot(model="Т800")
print(my_robot)
print("-"*90)

#создаю летающего робота
my_flying_robot = FlyingRobot(model="T200")
#печатаю его
print(my_flying_robot)
#вызываю взлет и полет скорость 30
my_flying_robot.fly_up()
my_flying_robot.flying(speed=30)
#останавливаю и сажу робота
my_flying_robot.stop()
my_flying_robot.landing()
print("Высота робота: ", my_flying_robot.get_hight())
print("Скорость робота: ", my_flying_robot.get_speed())
print("-"*90)

#создаю боевого робота с оружием Пушка
my_war_robot = WarRobot(weapon="Пушка", model="T1000")
#печатаю его
print(my_war_robot)
#вызываю взлет и полет скорость 30
my_war_robot.fly_up()
my_war_robot.flying(speed=30)
#вызываю боевую задачу робота
my_war_robot.operate()
#останавливаю и сажу робота
my_war_robot.stop()
my_war_robot.landing()
print("-"*90)

#создаю робота-разведчика
my_scout_robot = ScoutRobot(model="T1200")
#печатаю его
print(my_scout_robot)
#вызываю взлет и полет скорость 30
my_scout_robot.fly_up()
my_scout_robot.flying(speed=30)
#вызываю боевую задачу робота
my_scout_robot.operate()
#останавливаю и сажу робота
my_scout_robot.stop()
my_scout_robot.landing()
