text = input("Введите строку: ")
answer = ""
for index, value in enumerate(text):
    if value == "~":
        answer += "{} ".format(index)
print("Ответ: {}".format(answer))