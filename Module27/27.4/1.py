from typing import Callable, Any


def bread(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print("</----------\>")
        func(*args, **kwargs)
        print("<\__/>")

    return wrapper


def additionals(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrapper


@bread
@additionals
def burger() -> Any:
    print("--ветчина--")


burger()
