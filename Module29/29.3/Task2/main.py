from typing import Callable, Any, Optional
import functools
import time
file_name: str = input("Введите адрес сайта (имя файла): ")
saved_text: Optional[str] = None


def dec_with_time(_func=None, *, stop_time: int = 1) -> Callable:
    def stopper_decorator(func: Callable) -> Callable:
        """
        Функция декоратор, делает задержку перед выполнением обернутой функции
        :param func: обернутвая функция
        :return: обернутая функция
        """
        @functools.wraps(wrapped=func)
        def wrapper(**kwargs: Any) -> Any:
            # print("Ждем {} секунд".format(stop_time))
            time.sleep(stop_time)
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
    if _func is None:
        return stopper_decorator
    return stopper_decorator(_func)


@dec_with_time(stop_time=5)
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
