from typing import Callable, Any


def decorator_with_count(count: int = 1) -> Callable:
    """
    Декоратор декоратора для передачи параметра count, который указывает количество повторений выполнения
    декорируемой функции
    :param count: указывает количество повторений выполнения декорируемой функции
    :return: декоратор с переменной count с декорируемой функцией
    """
    def decorator(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs) -> Any:
            for _ in range(count):
                func(*args, **kwargs)

        return wrapped_func
    return decorator


@decorator_with_count(2)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


@decorator_with_count(4)
def goodbye(name: str) -> None:
    print('Пока, {name}!'.format(name=name))


greeting('Tom')
goodbye('Tom')
