text = input("Введите текст: ")
symb_dict = {}

for symbol in text:
    if symbol in symb_dict:
        symb_dict[symbol] += 1
    else:
        symb_dict[symbol] = 1

for i_key in sorted(symb_dict.keys()):
    print(i_key, ":", symb_dict[i_key])

print("Максимальная частота:", max(symb_dict.values()))