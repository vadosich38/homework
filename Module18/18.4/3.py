text = input("Введите текст: ")
counter = [0, 0]

for symbol in text:
    if symbol == " ":
        continue
    elif symbol.isupper():
        counter[0] += 1
    else:
        counter[1] += 1
if counter[0] > counter[1]:
    print(text.upper())
else:
    print(text.lower())
