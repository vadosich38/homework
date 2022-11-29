people = int(input("Сколько будет людей: "))
rolls = int(input("Сколько есть роликов: "))
people_list = []
rolls_list = []
paar = 0
for _ in range(people):
    size_p = int(input("Введите размер человека: "))
    people_list.append(size_p)

for _ in range(rolls):
    size_r = int(input("Введите размер роликов: "))
    rolls_list.append(size_r)

for i_num in range(len(people_list)):
    min_people = min(people_list)
    if min_people > rolls_list[i_num-paar] or min_people == rolls_list[i_num-paar]:

        people_list.remove(min_people)
        rolls_list.remove(rolls_list[i_num-paar])
        paar += 1


print("Наибольшее кол-во людей, которые могут взять ролики:", paar)