from typing import Callable, Any, Optional
import functools
import time
file_name: str = input("Введите адрес сайта (имя файла): ")
saved_text: Optional[str] = None


def stopper(func: Callable, **kwargs: Any) -> Callable:
    """
    Функция декоратор, делает задержку перед выполнением обернутой функции
    :param func: обернутвая функция
    :param kwargs: именованые аргументы
    :return: обернутая функция
    """
    @functools.wraps(wrapped=func)
    def wrapper(**kwargs: Any) -> Any:
        time.sleep(15)
        check = func(kwargs["name"])
        if check is None:
            print("-"*90)
            print("Текст сайта записан.\nЗаписаный текст: \n{}".format(saved_text))
        elif check:
            print("-"*90)
            print("Текст на сайте изменился.\nНовый текст: \n{}".format(saved_text))
        elif not check:
            pass
    return wrapper


@stopper
def my_func(name: str) -> Any:
    """
    Функция првоерки изменений в файле (сайт)
    :param name: название файла с кодом сайта
    """
    global saved_text
    with open(name, "r", encoding="utf-8") as file:
        site_text = file.read()

    if saved_text:
        if not saved_text == site_text:
            saved_text = site_text
            return True
        else:
            return False
    else:
        saved_text = site_text
        return None


while True:
    my_func(name=file_name)
