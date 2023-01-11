file = open("first_tour.txt", "r", encoding="utf-8")
players = list()
minimum = int(file.readline())

#example_list = [('S', 'Ivanov', 80), ('P', 'Segeev', 92), ('V', 'Petrov', 98), ('M', 'Vasiliev', 78)]
def my_sort(data):
    return data[2]

for str_count, i_string in enumerate(file):
    s_name, name, count = str(i_string).strip().split()
    count = int(count)
    if int(count) > minimum:
        players.append((name[0], s_name, count))
file.close()
players.sort(key=my_sort)

res_file = open("second_tour.txt", "a", encoding="utf-8")
res_file.write(str(len(players)) + "\n")
for str_num, string in enumerate(players[::-1]):
    res_file.write(f"{str_num + 1}) {players[-(str_num+1)][0]}. {players[-(str_num+1)][1]} {players[-(str_num+1)][2]}\n")
res_file.close()