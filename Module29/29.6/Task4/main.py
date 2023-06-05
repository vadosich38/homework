from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Переданные арги и кварги в декоратор: {} {}".format(args, kwargs))
        return decorator

    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    return func


# При вызове decorated_decorator(100, 'рублей', 200, 'друзей') функция decorated_decorator вызывает декоратор
# decorator_with_args_for_any_decorator с переданными аргументами (100, 'рублей', 200, 'друзей').
# Этот вызов возвращает внутреннюю функцию wrapper.
@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
