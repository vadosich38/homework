from typing import Callable, Any


def decorator(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        result = ""
        for _ in range(2):
            greet = func(*args, **kwargs)
            result += str(greet) + "\n"
        return result

    return wrapped_func

@decorator
def greeting(name: str) -> str:
    my_str = "Привет " + name + "!"
    return my_str


print(greeting('Tom'))
