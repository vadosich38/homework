file = open("numbers.txt", "r", encoding="utf-8")
summ = 0

for i_string in file:
    for i_symbol in i_string:
        if i_symbol.isdigit():
            summ += int(i_symbol)
file.close()

res_file = open("answer.txt", "a")
res_file.write(str(summ))
res_file.close()