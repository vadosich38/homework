from typing import Callable
import functools


def singleton(cls: Callable) -> Callable:
    """Синглтон, контролирует, чтобы объект класса создавался не более одного раза.
    Если же объект уже создан, в ответ на новую попытку создать объект класса, возвращается старый объект класса"""
    @functools.wraps(cls)
    def decorated_class(*args, **kwargs):
        if not decorated_class.instance:
            decorated_class.instance = cls()
        return decorated_class.instance(*args, **kwargs)

    decorated_class.instance = None
    return decorated_class


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)

#Результат:
#1986890616688
#1986890616688
#True