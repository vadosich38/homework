const = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = const * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print("Невозможно преобразовать к числу")
except IndexError:
    print("Выход за границы списка")
