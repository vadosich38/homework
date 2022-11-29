def check ():
    word = input("Введите слово: ")
    symbol_list = list(word)
    myrror_word = ""
    for symbol_num in range(len(symbol_list), 0, -1):
        myrror_word += symbol_list[symbol_num-1]

    if myrror_word == word:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")

check()