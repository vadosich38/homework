import functools
from typing import Callable, Union
user_permissions = ['admin']


def check_permission(user_name: str) -> Callable:
    """
    Функция-обертка для передачи аргумента в декоратор
    :param user_name: передаваемый документ
    :return: возвращаем декоратор
    """
    def deco(func: Callable) -> Callable:
        """
        Декоратор, выполняющий проверку прав доступа к вызываемым функциям
        :param func: вызываемая функция
        :return: возвращаем обертку вызываемой функции
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            """
            В обертке проверяем права доступа к вызову функции. Если прав недостаточно, выводим сообщение
            о недостаточных правах, иначе выполняем функцию.
            :param args: позиционные аргументы
            :param kwargs: именованные аргументы
            :return: результат выполнения обернутой функции
            """
            if user_name in user_permissions:
                return func(*args, **kwargs)
            print("PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию {}".format(func.__name__))

        return wrapper
    return deco


@check_permission(user_name='admin')
def delete_site():
    print('Удаляем сайт')


@check_permission(user_name='user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
