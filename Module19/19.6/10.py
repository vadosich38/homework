text = input("Введите текст: ")
letters_dict = dict()
counter = 0
for symbol in text:
    letters_dict[symbol] = text.count(symbol)
    if text.count(symbol) % 2 == 0:
        continue
    else:
        counter += 1

if max(letters_dict.values()) % 2 == 0 and counter <= 1:
    print("Палиндром возможен!")
else:
    print("Палиндром невозможен")