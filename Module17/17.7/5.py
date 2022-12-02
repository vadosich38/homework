text = "defhiokh"
print("Текст:", text)

symbol_list = [letter for letter in text]
#index = [x[0] for x in enumerate(symbol_list) if x[1] == "h"]
index = text[text.find('h') + 1:text.rfind('h')]

print("Перевернутый текст:", text[:3]+text[7:3:-1]+text[7:])