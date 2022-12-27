data = input("Введите строку: ")

def get_type(my_data):
    data_types = {
            int: 'int (целое число), неизменяемый\nНезменяемый (immutable)',
            float: 'float (вещественное число)\nНезменяемый (immutable)',
            str: 'str (строка)\nНезменяемый (immutable)',
            tuple: 'tuple (кортеж)\nНезменяемый (immutable)',
            bool: 'bool (логический тип)\nНезменяемый (immutable)',
            list: 'list (список)\nИзменяемый (mutable)',
            dict: 'dict (словарь)\nИзменяемый (mutable)',
            set: 'set (множество)\nИзменяемый (mutable)',
    }
    return data_types.get(type(eval(my_data)), 'Неизвестный тип')

print("Тип данных:", get_type(data))
print("id объекта:", id(data))