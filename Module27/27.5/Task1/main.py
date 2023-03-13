from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(wrapped=func)
    def wraper():
        input("Как дела? ")
        print("А у меня не очень...")
        func()

    return wraper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
