from typing import IO
from abc import ABC


class File(ABC):
    """
    Абстрактный класс контекст-менеджер для открытия и закрытия текстового файла
    """
    def __init__(self, file_name: str, reg: str, coding: str):
        # print("Открытие и закрытие файла")
        self.my_file = open(file=file_name, mode=reg, encoding=coding)

    def __enter__(self) -> IO[str]:
        return self.my_file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.my_file.close()
        return True


with File(file_name='mm_file.txt', reg='w', coding="utf-8") as file:
    file.write('Всем привет! Я тут!')

with File(file_name="mm_file.txt", reg="r", coding="utf-8") as file:
    text = file.readline()
    print("В файле записан текст:", text)
