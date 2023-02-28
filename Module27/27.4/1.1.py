from typing import Callable, Any


def bread(func: Callable) -> Callable:
    def wrapper(**kwargs) -> Any:
        print("</----------\>")
        func(**kwargs)
        print("<\__/>")

    return wrapper


def additionals(func: Callable) -> Callable:
    def wrapper(**kwargs):
        print(kwargs["add1"])
        func(**kwargs)
        print(kwargs["add2"])

    return wrapper


@bread
@additionals
def burger(**kwargs) -> Any:
    print(kwargs["main1"])


burger(main1="--wurstchen--", add1="#zukinni#", add2="~salat~")
