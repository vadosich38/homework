text = input("Введите текст: ")
symbol = input("Введите дополнительный символ: ")

double_list = [a*2 for a in text]
sign_list = [a+symbol for a in double_list]

print("Список удвоенных символов:", double_list)
print("Склейка с дополнительным символом:", sign_list)