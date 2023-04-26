import math
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def flat_square(self) -> float:
        pass

    @abstractmethod
    def flat_perimetr(self) -> float:
        pass


class Square(Figure):
    """
    Класс описывающий квадрат
    инициализируется двумя сторонами,
    площадью и периметром -- по умолчанию равны нулю

    Фуункции:
    square - возвращает площадь
    perimetr - возвращает периметр
    """
    def __init__(self, size: float) -> None:
        self.__size = size

    def __str__(self) -> str:
        return "Высота: {}, ширина: {}, площадь: {}, периметр: {}".format(self.__size, self.__size, self.flat_square,
                                                                          self.flat_perimetr)

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    @property
    def flat_square(self) -> float:
        return self.__size ** 2

    @property
    def flat_perimetr(self) -> float:
        return self.__size * 4


class Triangle(Figure):
    """
    Класс описывающий треугольник
    Инициализируется высотой и основанием,
    площадью и периметром -- по умолчанию равны нулю

    Фуункции:
    square - возвращает площадь
    perimetr - возвращает периметр
    """
    def __init__(self, basis: float, height: float) -> None:
        self.__basis = basis
        self.__height = height

    def __str__(self) -> str:
        return "Основа: {}, высота: {}, длина сторон: {}, площадь {}, периметр {}".\
            format(self.__basis, self.__height, self.side_long(), self.flat_square, self.flat_perimetr)

    @property
    def basis(self) -> float:
        return self.__basis

    @basis.setter
    def basis(self, new_basis) -> None:
        self.__basis = new_basis

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, new_height) -> None:
        self.__height = new_height

    def side_long(self) -> float:
        return round(math.sqrt((self.__basis / 2) ** 2 + self.__height ** 2), 2)

    @property
    def flat_square(self) -> float:
        return (self.__basis * self.__height) / 2

    @property
    def flat_perimetr(self) -> float:
        return round(self.__basis + self.side_long() * 2, 2)


class Coub(Square):
    """
    Класс описывающий куб
    Инициализируется списком из шести элементов класса квадрата

    Функции:
    площадь куба
    """
    def __init__(self) -> None:
        self.__a = float(input("Введите размеры плоскостей куба: "))
        # super().__init__(size=self.__a) #не понимаю зачем пайчам требует вызов родительского конструктора
        self.__my_coub = [Square(size=self.__a) for square in range(6)]

    def __str__(self) -> str:
        my_str = "\nПечатаю стороны куба:\n"
        for figura in enumerate(self.my_coub):
            my_str += "Плоскость {} –– ".format(figura[0]+1)
            my_str += figura[1].__str__()
            my_str += " \n"
        return my_str

    @property
    def my_coub(self) -> list:
        return self.__my_coub

    @property
    def size(self) -> float:
        return self.__a

    @size.setter
    def size(self, new_size) -> None:
        self.__a = new_size
        for flat in self.my_coub:
            flat.size = new_size

    @property
    def square(self) -> float:
        temp_sum = 0
        for figure in self.my_coub:
            temp_sum += figure.flat_square
        return temp_sum


class Pyramid(Triangle):
    """
    Класс оисывающий пирамиду
    Инициализируется списком из трех элементов класса треугольников

    Функции:
    полная площадь пирамиды
    """
    def __init__(self) -> None:
        self.__basis = float(input("Введите длину основы пирамиды: "))
        self.__height = float(input("Введите высоту пирамиды: "))
        # super().__init__(basis=self.__basis, height=self.__height) #также не ясно зачем с меня требует эту строчку
        self.__my_pyramid = [Triangle(basis=self.basis, height=self.height) for triangle in range(4)]
        self.__my_pyramid.append(Square(size=self.__basis))

    def __str__(self) -> str:
        self.__my_str = "\nПечатаю треугольники пирамиды:\n"
        for figura in enumerate(self.my_pyramid):
            self.__my_str += "Треугольник {}:\n".format(figura[0]+1)
            self.__my_str += "{}\n".format(figura[1].__str__())

        self.__my_str += "Основание пирамиды: {}".format(self.__my_pyramid[4])
        return self.__my_str

    @property
    def my_pyramid(self) -> list:
        return self.__my_pyramid

    @property
    def basis(self) -> float:
        return self.__basis

    @basis.setter
    def basis(self, new_basis) -> None:
        self.__basis = new_basis
        for flat in self.my_pyramid:
            flat.basis = new_basis

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, new_height) -> None:
        self.__height = new_height
        for flat in self.my_pyramid:
            flat.height = new_height

    def square(self) -> float:
        # http://mozgan.ru/Geometry/AreaBodyPyramid
        # формула тоже с этого сайта
        return round((4 * self.basis / 2) * ((self.basis / 2 * math.tan(3.14119 / 4)) +
                                            math.sqrt(self.height**2 + (self.basis / 2 * math.tan(3.14119 / 4))**2)), 3)


print("Квадрат:")
my_square = Square(size=4)
print(my_square)
print(my_square.flat_square)
print(my_square.flat_perimetr)
print("\nТреугольник:")
my_triangle = Triangle(basis=4, height=6)
print(my_triangle)
print(my_triangle.flat_square)
print(my_triangle.flat_perimetr)
print()
print("\nКуб:")
my_coub = Coub()
print(my_coub)
print(my_coub.square)

my_coub.size = 10
print(my_coub)
print("\nПирамида:")
my_pyramid = Pyramid()
print(my_pyramid)
print(my_pyramid.square())

my_pyramid.height = 20
my_pyramid.basis = 14
print(my_pyramid)
