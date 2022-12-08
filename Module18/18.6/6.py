text = input("Введите строку: ")
symbol_list = [symbol for symbol in text]
res = ""

counter = 1
for index in range(len(symbol_list)):
    if not index + 1 > len(symbol_list) - 1:
        if symbol_list[index] == symbol_list[index+1]:
            counter += 1
        else:
            res += "{0}{1}".format(symbol_list[index], counter)
            counter = 1
    else:
        res += "{0}{1}".format(symbol_list[index], counter)
        counter = 1
print(res)