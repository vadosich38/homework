from typing import Callable


def func_1(x: int) -> int:
    return x + 10


def func_2(func: Callable, *args, **kwargs) -> int:
    f_res = func(*args, *kwargs)
    res = f_res ** 2

    return res


print(func_2(func_1, 9))
