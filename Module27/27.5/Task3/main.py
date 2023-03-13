import datetime
import os
import functools
from typing import Callable, Any


def logging(func: Callable, **kwargs) -> Callable:
    """
    Декоратор для логирования функции. Выводит в консоль минформацию, какая выполняется функция и ее документацию.
    При возникновении ошибки создает файл лог и записывает в него имя функции и имя ошибки. Функция должна продолжать
    свое выполнение.
    :param func:
    :param kwargs:
    :return:
    """
    @functools.wraps(wrapped=func)
    def wrapper(*args, **kwargs) -> Any:
        print("Выполняется функция {}\nДокументация функции: {}".format(func.__name__, func.__doc__))
        try:
            return func(*args, **kwargs)
        except Exception as exp_name:
            with open("log.txt", "a", encoding="utf-8") as log_file:
                log_file.write("{}: При выполнении функции {} возникла ошибка: {}\n".format(
                    datetime.datetime.now(), func.__name__, exp_name))

    return wrapper


if os.path.exists("log.txt"):
    os.remove("log.txt")


@logging
def my_func(zahler: int, nenner: int) -> float:
    """
    Функция выполняющая деление двух чисел
    :param zahler: числитель
    :param nenner: знаменатель
    :return: результат деления числителя на знаменатель
    """
    res = zahler / nenner
    print("Продолжение")
    return res


@logging
def my_func2(num1: int, num2: int) -> int:
    """
    Выполняется умножение элемента 1 на элемент 2
    :param num1: значение 1
    :param num2: значение 2
    :return: результат умножения
    """
    res = num1 * num2
    print("Продолжение 2")
    return res


print(my_func(zahler=10, nenner="f"))
print()
print(my_func2(num1=10, num2="f"))
