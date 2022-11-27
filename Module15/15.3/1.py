s = input("Введите текст: ")
symbol_list = list(s)
s = ""
sym_counter = 0
c_counter = 0

for symbol in symbol_list:
    if symbol == ":":
        s += ";"
        c_counter += 1
    else:
        s += symbol
    sym_counter += 1

print("Исправленная строка:", s)
print("Кол-во замен:", c_counter)