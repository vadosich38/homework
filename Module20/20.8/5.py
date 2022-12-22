familys = {
    ("Ivan", "Volkin"): 23,
    ("Bob", "Robbin"): 43,
    ("Rob", "Bobbin"): 33,
    ("Jack", "Bobbin"): 9,
    ("Semen", "Volkin"): 21,
    ("Ivanna", "Volkina"): 11,
    ("Olya", "Volkina"): 90,
    ("Jesika", "Robbina"): 22,
    ("Alisa", "Robbina"): 12,
    ("Sara", "Robbina"): 8,
}
flag = True
family_name = input("Введите фамилию семьи: ").capitalize()
fem_fam_name = family_name + "a"
for i_key, i_value in familys.items():
    if i_key[1].capitalize() == family_name or i_key[1].capitalize() == fem_fam_name:
        print(i_key[0], i_key[1], i_value)
        flag = False
if flag:
    print("Такой семьи нет в базе данных!")
