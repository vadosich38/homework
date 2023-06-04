from typing import Callable
import functools

app = dict()


def callback(command: str = None) -> Callable:
    def decorator_callback(function: Callable) -> Callable:
        """ Декоратор функции обратного вызова """
        app[command] = function

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            function_call = function(*args, **kwargs)
            return function_call

        return wrapper
    return decorator_callback


@callback(command='//')
def check_all_data() -> str:
    print('Пример функции, которая возвращает ответ сервера 1')
    return 'OK'


@callback(command='!!')
def return_data_status() -> str:
    print("Пример функции, которая возвращает ответ сервера 2")
    return 'Status: OK'


#не корректный вызов первой функции
command = app.get('!//!')
if command:
    response = command()
    print('Ответ:', response)
else:
    print('Такой команды нет')

#корректный вызов первой функции
command = app.get('//')
if command:
    response = command()
    print('Ответ:', response)
else:
    print('Такой команды нет')

#не корректный вызов второй функции
command = app.get('!')
if command:
    response = command()
    print('Статус данных:', response)
else:
    print('Такой команды нет')


#корректный вызов второй функции
command = app.get('!!')
if command:
    response = command()
    print('Статус данных:', response)
else:
    print('Такой команды нет')

print(app)
