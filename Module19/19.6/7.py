count_orders = int(input("Введите количество заказов: "))
data_dict = dict()
for order in range(1, count_orders + 1):
    data_list = input("Заказ {}: ".format(order)).split()
    if data_list[0] in data_dict:
        if data_list[1] in data_dict[data_list[0]]:
            data_dict[data_list[0]][data_list[1]] = data_dict[data_list[0]][data_list[1]] + int(data_list[2])
        else:
            data_dict[data_list[0]][data_list[1]] = int(data_list[2])
    else:
        data_dict[data_list[0]] = {data_list[1]:int(data_list[2])}

for castomer in data_dict:
    print(castomer)
    for pizza_name in data_dict[castomer]:
        print("  ",pizza_name, ":", data_dict[castomer][pizza_name])
