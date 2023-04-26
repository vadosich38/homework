from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный родительский метод Фигура
    """
    def __init__(self, x: int, y: int, length: int, width: int) -> None:
        self.x_pos = x
        self.y_pos = y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, move_x, move_y) -> None:
        self.x_pos += move_x
        self.y_pos += move_y

    def __str__(self) -> str:
        return "Фигура: {}\nх: {}\nу: {}\nдлина: {}\nширина: {}\n".format(self.__class__.__name__, self.x_pos,
                                                                          self.y_pos, self.length, self.width)


class ResizeblMixin:
    """
    Класс примесь, изменение размеров объекта
    """
    def resize(self, new_length: int, new_width: int):
        print("Изменяю размеры фигуры {}".format(self.__class__.__name__))
        self.length = new_length
        self.width = new_width


class Rectangle(Figure, ResizeblMixin):
    """
    Класс прямоугольник с переопределенными методами конструктора и движения.
    Роители: класс Фигура, класс Миксин
    """
    def __init__(self, x, y, length, width) -> None:
        super().__init__(x, y, length, width)

    def move(self, move_x, move_y) -> None:
        print("Изменяю координаты фигуры {}".format(self.__class__.__name__))
        self.x_pos += move_x
        self.y_pos += move_y


class Square(Figure, ResizeblMixin):
    """
    Класс квадрат с переопределенными методами конструктора и движения.
    Роители: класс Фигура, класс Миксин
    """
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__(x, y, size, size)

    def move(self, move_x, move_y) -> None:
        print("Изменяю координаты фигуры {}".format(self.__class__.__name__))
        self.x_pos += move_x
        self.y_pos += move_y


# rect1 = Rectangle(x=1, y=0, length=10, width=22)
# rect2 = Rectangle(x=0, y=22, length=2, width=12)
# square1 = Square(x=0, y=4, size=5)
# square2 = Square(x=11, y=3, size=55)

# list = [rect1, rect2, square1, square2]

for figure in [Rectangle(x=1, y=0, length=10, width=22), Rectangle(x=0, y=22, length=2, width=12),
               Square(x=0, y=4, size=5), Square(x=11, y=3, size=55)]:
    print("-"*90)
    print(figure)
    print("-"*90)

    figure.move(-4, 44)
    print(figure)
    print("-"*90)

    new_length1 = figure.length * 2
    new_width1 = figure.width * 2
    figure.resize(new_length=new_length1, new_width=new_width1)
    print(figure)
    print("-"*90)
