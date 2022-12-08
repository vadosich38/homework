start = "№@$%^&*()."
file_name = input("Введите имя файла: ")
flag1 = True
flag2 = True

for symbol in start:
    if file_name.startswith(symbol):
        print("Ошибка: название начинается на один из специальных символов")
        flag1 = False
        break

if not (file_name.endswith(".txt") or file_name.endswith(".docx")):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
    flag2 = False

if flag1 and flag2:
    print("Файл назван верно")





