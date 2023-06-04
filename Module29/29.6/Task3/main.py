from typing import Callable
from datetime import datetime
import time
import functools


def logger(func: Callable, data_format: str) -> Callable:
    """
    Декоратор логгер. Выполрняет логирование по заданому формату даты и засекает время работы функции
    :param func: логируемая функция
    :param data_format: формат вывода даты
    :return: возвращает обертку декоратора
    """
    @functools.wraps(func)
    def dec_logger(*args, **kwargs) -> int:
        func_name = func.__qualname__.split(".")

        my_format = data_format
        for i_symbol in my_format:
            if i_symbol.isalpha():
                my_format = my_format.replace(i_symbol, "%"+i_symbol)

        print("Запускается '{}.{}'. Дата и время запуска: {}. ".format(func_name[0], func_name[1],
                                                                       datetime.now().strftime(my_format)))
        start_time = time.time()
        res = func(*args, **kwargs)
        print("Завершение '{}.{}', время работы = {}. \n".format(func_name[0], func_name[1],
                                                                 round(time.time()-start_time, 3)))
        return res

    return dec_logger


def log_methods(d_format: str) -> Callable:
    """
    Декоратор, оборачивающий не магические методы класса в декоратор логирования
    :param d_format: формат даты, переданый при декорировании
    :return: возвращает обертку декоратора
    """
    @functools.wraps(logger)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith("__"):
                current_method = getattr(cls, i_method)
                decorated_method = logger(func=current_method, data_format=d_format)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print("Тут метод test_sum_1")
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника.")

    @classmethod
    def test_sum_2(cls):
        print("Тут метод test_sum_2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
B.test_sum_2()
