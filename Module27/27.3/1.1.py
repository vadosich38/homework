from typing import Callable, Any


def decorator(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        for _ in range(2):
            func(*args, **kwargs)

    return wrapped_func


@decorator
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
