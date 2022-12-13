text = input("Введите текст: ")
symb_dict = {}
new_dict = {}

def rever_dict():
    print("Инвертированный словарь частот:")
    for i_value in symb_dict.values():
        new_dict[i_value] = [i_key for i_key in symb_dict if symb_dict[i_key] == i_value]
    print(new_dict)

for symbol in text:
    if symbol in symb_dict:
        symb_dict[symbol] += 1
    else:
        symb_dict[symbol] = 1

print("Оригинальный словарь частот:")
for i_key in sorted(symb_dict.keys()):
    print(i_key, ":", symb_dict[i_key])

rever_dict()
