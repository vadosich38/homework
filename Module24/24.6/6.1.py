import resurces61


def res_print(data):
    for i_num, i_elem in data.items():
        print("{}: {}".format(i_num, i_elem.name))


my_water = resurces61.Water()
my_land = resurces61.Land()
my_fire = resurces61.Fire()
my_air = resurces61.Air()

res_dict = {1: my_water, 2: my_land, 3: my_fire, 4: my_air}

while True:
    print("Доступные ресурсы:")
    res_print(res_dict)
    print("\nНапишите что с чем соеденить. Например: 2 + 4")
    answer = input()
    elem1 = answer[0]
    elem2 = answer[-1]
    try:
        new_elem = res_dict[int(elem1)] + res_dict[int(elem2)]
        print(new_elem.answer)
        if new_elem not in res_dict.values():
            res_dict[len(res_dict) + 1] = new_elem
    except Exception as a:
        print("Сложение выполнить невозможно так как возникла ошибка {}".format(a))
