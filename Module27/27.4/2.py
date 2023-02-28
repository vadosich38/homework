from typing import Callable, Dict
ADDITIONAL: Dict[str, Callable] = dict()


def filter_dec(func: Callable) -> Callable:
    ADDITIONAL[func.__name__] = func
    return func


@filter_dec
def say_hello(name: str) -> str:
    return "Hallo, {}".format(name)


@filter_dec
def say_bay(name: str) -> str:
    return "Bay, {}".format(name)


print(say_bay("Alex"))
print(say_hello("Olga"))
print(ADDITIONAL)
