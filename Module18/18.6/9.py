text = "Хотя ,. возм:ожно и нет."
words_list = []
temp_text = ""
new_messege = ""

for symbol in text:
    if symbol == "." \
            or symbol == "!" \
            or symbol == "," \
            or symbol == "?" \
            or symbol == "!?" \
            or symbol == "..." \
            or symbol == ",." \
            or symbol == ":" \
            or symbol == " ":
        new_messege += temp_text[::-1] + symbol
        temp_text = ""
    else:
        temp_text += symbol
print("Новое сообщение: {}".format(new_messege))
