text = input("Введите текст: ")
step = int(input("Введите сдвиг: "))
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
secret_messege = ""

char_list = ((alphabet[(alphabet.index(sym) + step) % 33] if sym != " " else " ") for sym in text)
for char in char_list:
    secret_messege += char

print("Зашифрованный текст:", secret_messege)