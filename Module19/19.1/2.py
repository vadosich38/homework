stud_info = input("Введите информацию о студенте: ")
stud_list = stud_info.split()
stud_dict = dict()

stud_dict["Имя"] = stud_list[0]
stud_dict["Фамилия"] = stud_list[1]
stud_dict["Город"] = stud_list[2]
stud_dict["ВУЗ"] = stud_list[3]
stud_dict["Оценки"] = stud_list[4:]

for i_info in stud_dict:
    print(i_info, "-", stud_dict[i_info])
