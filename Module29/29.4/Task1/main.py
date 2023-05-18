import functools
import time
from datetime import datetime


def my_decorator(cls):
    """Декоратор класса, выводит время инициализации объекта класса и список методов класса"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Время инициализации объекта класса {}: {}".format(cls.__name__, datetime.utcnow()))
        print("Список методов инициализировнного класса: {}".format(dir(cls)))

        return instance

    return wrapper


@my_decorator
class Calc:
    """
    Класс-пример. Инициализируется числом, которое используется в методах класса:
    метод coub печатает куб числа
    метод square печатает квадрат числа
    """
    def __init__(self, max_num: int):
        self.__max_num = max_num

    def coub(self):
        print(self.__max_num ** 3)

    def square(self):
        print(self.__max_num ** 2)


my_calc = Calc(max_num=5)
time.sleep(5)
my_calc1 = Calc(max_num=10)
