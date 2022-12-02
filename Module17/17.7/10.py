text = input("Введите текст: ")
step = int(input("Введите сдвиг: "))
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
counter = 0
pos = None
secret_messege = ""
for letter in text:
    for letter_alphabet in alphabet:
        counter += 1
        if letter == letter_alphabet:
            pos = counter
            if pos + step > 33:
                pos = (pos - 33)
            secret_messege += alphabet[pos-1+step]
        elif letter == " ":
            secret_messege += " "
            letter = ""

    counter = 0
print("Зашифрованный текст:", secret_messege)