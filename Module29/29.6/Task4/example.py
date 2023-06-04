from functools import wraps
from typing import Callable


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        @wraps(func)
        def wrapper(func: Callable) -> Callable:
            print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
            result = func
            return result

        return wrapper

    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable):
    @wraps(func)
    def wrapper(func: Callable) -> Callable:
        return func()

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)