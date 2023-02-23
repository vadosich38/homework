import time
from typing import Callable, Any


def my_func1(num: int) -> int:
    summ = 0
    for i_num in range(10000):
        summ += (((num + i_num ** 2) ** 3) / 100) ** -29
    return summ


def timer(func: Callable, *args, **kwargs) -> Any:
    start_an = time.time()
    res = func(*args, *kwargs)
    finish_an = time.time()
    run_time = finish_an - start_an

    print("Функция работала {} секунд(ы)".format(round(run_time, 4)))

    return res


print(timer(my_func1, 20))
