word = input("Введите слово: ")
word_list = list(word)
unic_sym_list = []
counter = 0

for sym in word_list:
    for search_sym in word_list:
        if sym == search_sym:
            counter += 1
    if counter < 2:
        unic_sym_list.append(sym)
    counter = 0

print("Уникальных символов:", len(unic_sym_list))