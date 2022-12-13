text = input("Введите строку: ")
add_text = ""
flag = True
for symbol in text:
    if text != text[::-1]:
        add_text += symbol
        new_text = text + add_text[::-1]
        if new_text == new_text[::-1]:
            print("Палиндром возможен!")
            flag = False
            break
        else:
            flag = True
    else:
        print("Текст уже является палиндромом!")
        flag = False
        break
if flag:
    print("Палиндром невозможен!")

#aabc