file = open("zen.txt", "r", encoding="utf-8")
min_lett = ""
min = 1000000
def counter(data):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    flag_word = False
    c_strings = 0
    c_words = 0
    c_letters = 0
    for i_string in data:
        for i_symbol in i_string:
            if (i_symbol == " " or i_symbol == "." or i_symbol == "!") and flag_word :
                c_words += 1
                flag_word = False
            elif i_symbol.lower() in alphabet:
                alphabet[i_symbol.lower()] += 1
                c_letters += 1
                flag_word = True
        else:
            c_strings += 1
    return c_strings, c_words, c_letters, alphabet
res = counter(file)
file.close()

for i_letter in res[3]:
    if res[3][i_letter] > 0 and res[3][i_letter] < min:
        min = res[3][i_letter]
        min_lett = i_letter

print("Строк {}, слов {}, букв {}".format(res[0], res[1], res[2]))
print("Реже всего встречается буква: {0}, она встречается {1} раз".format(min_lett, res[3][min_lett]))