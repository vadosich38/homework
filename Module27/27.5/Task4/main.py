import functools
from typing import Callable, Optional, Any


def debbug(func: Callable, *args, **kwargs) -> Callable:
    """
    Декоратор. Выводит имя декорируемой функции
    (вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает.
    После этого выводится результат её выполнения
    :param func: входящая функция
    :return: обернутая функция
    """
    @functools.wraps(wrapped=func)
    def wrapper(*args, **kwargs) -> Any:
        args_repr = [a for a in args]
        kwargs_repr = [f"{key}={value}" for key, value in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        res = func(*args, **kwargs)
        print("Вызывается '{}' ({})\n'{}' вернула '{}'".format
              (func.__name__, signature, func.__name__, res))
        return print(func(*args, **kwargs))

    return wrapper


@debbug
def greeting(name: str, age: Optional[int] = None) -> str:
    """
    Функция приветсвия.
    :param name: имя, значения по-умолчанию нет
    :param age: возраст, по-умолчанию None
    :return: возвращает текст приветствия
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
