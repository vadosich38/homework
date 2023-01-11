file = open("first_tour.txt", "r", encoding="utf-8")
players = dict()
data_tmp = list()

for str_count, i_string in enumerate(file):
    if str_count == 0:
        minimum = int(i_string)
    else:
        s_name, name, count = str(i_string).split(" ")
        if str(count).endswith("\n"):
            count = count[0:len(count)-1]
        if int(count) > minimum:
            players[(name[0]+".", s_name)] = count
file.close()

res_file = open("second_tour.txt", "a", encoding="utf-8")
string1 = str(len(players)) + "\n"
res_file.write(string1)
for string in enumerate(players):
    res_str = " ".join(string[1])
    res_str += str(players[string[1]])
    res_str += "\n"
    res_file.write(str(res_str))

res_file.close()