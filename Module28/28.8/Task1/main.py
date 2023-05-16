from abc import ABC
import os
from typing import IO


class File(ABC):
    """
    Абстрактный класс контекст-менеджер для открытия и закрытия файла, если открываемого файла не существует,
    он создается в папке выполнения кода
    """
    def __init__(self, file_name: str, reg: str, coding: str) -> None:
        """

        :param file_name: имя рабочего файла
        :param reg: режим работы с файлом
        :param coding: кодировка файла
        """
        self.__file_name = file_name
        self.__reg = reg
        self.__coding = coding
        print("Инициализация")

    def __enter__(self) -> IO[str]:
        """
        Проверяем существует ли в корне указаный файл, если нет, создаем его, открываем и возвращаем.
        Если файл существует, просто открываем переданый файл и возвращаем его.
        :return: файловый объект
        """

        print("Открытие файла")
        if not os.path.exists(self.__file_name):
            self.__my_file = open(file=self.__file_name, mode="x", encoding=self.__coding)
        else:
            self.__my_file = open(file=self.__file_name, mode=self.__reg, encoding=self.__coding)

        return self.__my_file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Закрываем открытый файл
        Все ошибки связанные с файловой системой "пропускаются"

        :param exc_type: тип ошибки
        :param exc_val: значение ошибки
        :param exc_tb: след ошибки
        :return:
        """
        print("Закрытие файла")

        self.__my_file.close()

        #проверяю закрыт ли файл
        print("Файл закрыт: {}".format(self.__my_file.closed))

        if exc_type == OSError:
            return True


with File(file_name="filename.txt", reg="w", coding="utf-8") as my_file_out:
    my_file_out.write("www")
    #вызываю ошибку типов, чтобы првоерить как обрабатываются ошибки
    my_file_out.write(223)
    my_file_out.write("sss")
