from typing import Callable
import functools
from _datetime import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор логгирования. Выполняет логирование выполняемых методов класса.
    Имя класса получаем через аргумент __qualname__, который возвращает весь путь имен метода до его класса,
    поэтому в сплитовом кортеже от __qualname__ берем нулевой элемент, являющийся классом этого метода.
    :param func: метод класса, который логируется
    :return: обернутый метод
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        class_name = func.__qualname__.split(".")
        print("-"*90, "\nВремя: {} \t Выполяется функция: {} \t Класс метода: {} \t Аргументы метода: {} "
                      "\t Именованные аргументы метода: {} \nДокументация метода: {}\n".
              format(datetime.utcnow(), func.__name__, class_name[0], args[1:], kwargs, func.__doc__))

    return wrapper


def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор, оборачивающий все методы класса в декоратор логирования
    :param decorator: декоратор, в который будут обернуты методы класса
    :return: при объявлении экземпляра класса срабатывает декоратор и возвращает экз. класса с обернутыми методами
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith("__") is False:
                current_method = getattr(cls, i_method)
                logged_method = decorator(current_method)
                setattr(cls, i_method, logged_method)
        return cls

    return decorate


@for_all_methods(decorator=logging)
class MyClass:
    """
    Класс-тест, создан для примера.
    method_1 высчитывает 2 в 10203 степени
    method_2 высчитывает 3 в 10203 степени
    method_3 высчитывает 4 в 10203 степени

    """

    @classmethod
    def method_1(cls, num: int = 5) -> None:
        """
        высчитывает 2 в 10203 степени
        :return: None
        """
        res1 = 2 ** 10203

    @classmethod
    def method_2(cls, num: int = None) -> None:
        """
        высчитывает 3 в 10203 степени
        :return: None
        """
        res2 = 3 ** 10203

    @classmethod
    def method_3(cls) -> None:
        """
        высчитывает 4 в 10203 степени
        :return: None
        """
        res3 = 4 ** 10203


my_test = MyClass()

my_test.method_1(num=5)
my_test.method_2(3)
my_test.method_3()
