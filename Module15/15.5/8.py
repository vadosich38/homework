text = input("Введите текст: ")
symbol_list = list(text)
k = int(input("Введите длину сдвига: "))

def change(k, symbol_list):
    while True:
        text = ""
        for sym_num in range(len(symbol_list)):
            if sym_num+k > len(symbol_list):
                text += symbol_list[(sym_num+k)-(len(symbol_list)+1)]
            else:
                text += symbol_list[sym_num + k - 1]

        print(text)
#        input()
        symbol_list = list(text)

change(k, symbol_list)
