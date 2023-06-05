import functools
from typing import Callable

count = 0


def dec_counter(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        global count
        count += 1
        print("Функция {} была вызвана {} раз".format(func.__name__, count))
        res = func(*args, **kwargs)
        return res
    return wrapper


@dec_counter
def say_hallo():
    print("Hallo!")


say_hallo()
say_hallo()
say_hallo()

print(dir())
