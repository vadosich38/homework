alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
file = open("text8.txt", "r", encoding="utf-8")
text = file.read().lower()
file.close()

alphabet = {i_elem.lower(): text.count(i_elem.lower()) for i_elem in text if i_elem.lower() in alphabet}
# тот же генератор словаря alphabet вне вида list comprehentions
# for i_elem in text:
#     if i_elem.lower() in alphabet:
#         alphabet[i_elem.lower()] += 1
let_sum = sum(alphabet.values())
let_value = {i_letter: round(alphabet[i_letter] / let_sum, 3) for i_letter in alphabet if alphabet[i_letter] != 0}

#сортировка
let_value = dict(sorted(let_value.items(), key=lambda x: x[0]))
let_value = dict(sorted(let_value.items(), key=lambda x: x[1], reverse=True))


res_file = open("analysis.txt", "w", encoding="utf-8")
res_text = "\n".join(i_paar[0] + " " + str(i_paar[1]) for i_paar in let_value.items())
res_file.write(res_text)
res_file.close()