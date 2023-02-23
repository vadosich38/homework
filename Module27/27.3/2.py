import time
from typing import Callable


def timer(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        start_an = time.time()
        res = func(*args, **kwargs)
        finish_an = time.time()
        run_time = finish_an - start_an
        print("Функция работала {} секунд(ы)".format(round(run_time, 4)))
        return res

    return wrapper

@timer
def my_func1(num: int) -> int:
    summ = 0
    for i_num in range(10000):
        summ += (((num + i_num ** 2) ** 3) / 100) ** -29
    return summ


print(my_func1(20))
