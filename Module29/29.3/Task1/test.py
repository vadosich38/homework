import time
from typing import Callable, Optional


def timer_with_precision(precision: int = 2) -> Callable:
    def timer_decorator(func: Callable) -> Callable:

        def wrapper(*args, **kwargs):
            start_an = time.time()
            res = func(*args, **kwargs)
            finish_an = time.time()
            run_time = finish_an - start_an
            print("Функция работала {} секунд(ы)".format(round(run_time, precision)))
            return res

        return wrapper
    return timer_decorator


@timer_with_precision(precision=5)
def my_func1(num: int) -> int:
    summ = 0
    for i_num in range(10000):
        summ += (((num + i_num ** 2) ** 3) / 100) ** -29
    return summ


@timer_with_precision(precision=10)
def my_func2(num: int) -> int:
    summ = 0
    for i_num in range(10000):
        summ += (((num + i_num ** 2) ** 3) / 100) ** -29
    return summ


@timer_with_precision()
def my_func3(num: int) -> int:
    summ = 0
    for i_num in range(10000):
        summ += (((num + i_num ** 2) ** 3) / 100) ** -29
    return summ


print(my_func1(30))
print(my_func2(30))
print(my_func3(30))
