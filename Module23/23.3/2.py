import zipfile
alphabet_la = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
alphabet_ki = {"а": 0, "б": 0, "в": 0, "г": 0, "д": 0, "е": 0, "ё": 0, "ж": 0, "з": 0, "и": 0, "й": 0, "к": 0, "л": 0,
               "м": 0, "н": 0, "о": 0, "п": 0, "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0,
               "щ": 0, "ъ": 0, "ы": 0, "ь": 0, "э": 0, "ю": 0, "я": 0}

#генерирую словари с большими буквами
alphabet_upper_la = {letter.upper(): 0 for letter in alphabet_la}
alphabet_upper_ki = {letter.upper(): 0 for letter in alphabet_ki}

#распаковываем архив с файлом
try:
    zip_file = zipfile.ZipFile("voyna-i-mir.zip")
    zip_file.extract("voyna-i-mir.txt")
except (FileNotFoundError, KeyError):
    print("Указаный архив или файл в архиве не обнаружен!")
else:
    zip_file.close()
finally:
    print("Работа с архивом закончена!")

#открываем файл, который экстрактировали с архива
try:
    text_file = open("voyna-i-mir.txt", "r", encoding="utf-8")
    new_text_file = text_file.read()
except FileNotFoundError:
    print("Невозможно открыть текстовый файл, так как он не найден!")
else:
    #считаю буквы в произведении
    for i_string in new_text_file:
        for i_symbol in i_string:
            if i_symbol in alphabet_la:
                alphabet_la[i_symbol] += 1
            elif i_symbol in alphabet_ki:
                alphabet_ki[i_symbol] += 1
            elif i_symbol in alphabet_upper_la:
                alphabet_upper_la[i_symbol] += 1
            elif i_symbol in alphabet_upper_ki:
                alphabet_upper_ki[i_symbol] += 1
    text_file.close()
finally:
    print("Работу с текстовым файлом закончил!")

#считаю сумму букв
sum_lett = sum(alphabet_ki.values()) + sum(alphabet_la.values()) + sum(alphabet_upper_ki.values()) + \
                                                                                    sum(alphabet_upper_la.values())
#высчитываю долю букв в тексте
alphabet_la = {i_letter: round(alphabet_la[i_letter] / sum_lett, 3) for i_letter in alphabet_la
                                                                                    if alphabet_la[i_letter] != 0}
alphabet_ki = {i_letter: round(alphabet_ki[i_letter] / sum_lett, 3) for i_letter in alphabet_ki
                                                                                    if alphabet_ki[i_letter] != 0}
alphabet_upper_la = {i_letter: round(alphabet_upper_la[i_letter] / sum_lett, 3) for i_letter in alphabet_upper_la
                                                                                    if alphabet_upper_la[i_letter] != 0}
alphabet_upper_ki = {i_letter: round(alphabet_upper_ki[i_letter] / sum_lett, 3) for i_letter in alphabet_upper_ki
                                                                                    if alphabet_upper_ki[i_letter] != 0}

#объеденяю и сортирую словарь
ful_alphabet = {**alphabet_upper_la, **alphabet_la, **alphabet_ki, **alphabet_upper_ki}
ful_alphabet = dict(sorted(ful_alphabet.items(), key=lambda x: x[0]))
ful_alphabet = dict(sorted(ful_alphabet.items(), key=lambda x: x[1], reverse=True))

#вывод на экран и запись в файл
res_file = open("analytics_v_i_m.txt", "a", encoding="utf-8")

for i_key, i_value in ful_alphabet.items():
    text = ("Буква {0} во всем произведении занимает такую долю: {1}\n".format(i_key, i_value))
    print(text)
res_file.close()

