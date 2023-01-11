file = open("text.txt", "r", encoding="utf-8")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                                                                                            "v", "w", "x", "y", "z"]
new_data_list = list()

for str_num, i_string in enumerate(file):
    for i_symbol in i_string:
        if i_symbol.lower() in alphabet:
            index = alphabet.index(i_symbol.lower()) + str_num + 1
            if i_symbol.islower():
                new_data_list.append(alphabet[index])
            else:
                new_data_list.append(alphabet[index].upper())
        else:
            new_data_list.append(i_symbol)
new_data = "".join(new_data_list)
file.close()

output_file = open("cipher_text.txt", "w", encoding="utf-8")
output_file.write(new_data)
output_file.close()
