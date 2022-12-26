data = input("Введите данные: ")

if data.isdigit():
    print("Тип данных: int(целочисленные)\nНеизменяемый (immutable)\nId объекта: {0}".format(id(data)))
elif data.startswith("(") and data.endswith(")"):
    print("Тип данных: tuple(кортеж)\nНеизменяемый (immutable)\nId объекта: {0}".format(id(data)))
elif data.startswith("{") and data.endswith("}"):
    print("Тип данных: dict(словарь)\nНеизменяемый (immutable)\nId объекта: {0}".format(id(data)))
elif data.startswith("[") and data.endswith("]"):
    print("Тип данных: list(список)\nИзменяемый (mutable)\nId объекта: {0}".format(id(data)))
else:
    print("Тип данных: str(строка)\nНеизменяемый (immutable)\nId объекта: {0}".format(id(data)))