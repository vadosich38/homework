from typing import Callable
import functools


def counter(func: Callable, *args, **kwargs) -> Callable:
    """
    Декоратор. Создает и инкременирует счетчик вызова функции в обертке
    :param func: функция в обертке
    :param args: аргументы позиционные
    :param kwargs: именованные аргументы
    :return: результат выполнения функции в обертке
    """
    @functools.wraps(wrapped=func)
    def wrapper() -> Callable:
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def my_func() -> None:
    """
    Функция печатает приветствие
    :return: ничего
    """
    print("Привет!")


my_func()
my_func()
my_func()

print(my_func.__name__, "was called", my_func.count, "times.")

my_func()
my_func()
my_func()

print(my_func.__name__, "was called", my_func.count, "times.")
