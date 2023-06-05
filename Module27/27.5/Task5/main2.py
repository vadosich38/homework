from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор. Создает и инкременирует счетчик вызова функции в обертке
    :param func: функция в обертке
    :return: результат выполнения функции в обертке
    """
    @functools.wraps(wrapped=func)
    def wrapper(*args, **kwargs) -> Callable:
        wrapper.count += 1
        print(func.__name__, "was called", wrapper.count, "times.")
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

#print(my_func.__name__, "was called", my_func.count, "times.")

my_func()
my_func()
my_func()

#print(my_func.__name__, "was called", my_func.count, "times.")
