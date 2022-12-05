text = input("Введите текст: ").lower()
step = int(input("Введите сдвиг: "))
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

char_list = ((alphabet[(alphabet.index(sym) + step) % 33] if sym != " " else " ") for sym in text)
secret_messege = "".join(char_list)

print("Зашифрованный текст:", secret_messege)