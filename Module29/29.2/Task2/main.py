import os
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def in_dir(new_directory: str) -> Iterator:
    current_directory = os.getcwd()

    try:
        os.chdir(new_directory)
    except FileNotFoundError as ex:
        print("!!!Возникла ошибка: {}\nДиректория не изменена!!!".format(ex))
    finally:
        yield
        os.chdir(current_directory)


# with in_dir("/Users/vladyslav/Downloads"):
with in_dir("C:\\"):
    print(os.listdir())

print(os.listdir())
