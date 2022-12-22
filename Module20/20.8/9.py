lines_count = int(input("Сколько строк в протоколе?: "))
my_dict = dict()

for num in range(lines_count):
    temp_list = input("{} запись: ".format(num+1)).split()
    if temp_list[1] in my_dict:
        if int(temp_list[0]) > int(my_dict[temp_list[1]][0]):
            my_dict[temp_list[1]] = (temp_list[0], num)
    else:
        my_dict[temp_list[1]] = (temp_list[0], num)
def sort(dict1):
    max = 0
    for i_key, i_value in dict1.items():
        if int(i_value[0]) > max:
            max = int(i_value[0])
            max_key = i_key
            maxstring_index = int(i_value[1])
        elif int(i_value[0]) == max:
            if i_value[1] < maxstring_index:
                max = int(i_value[0])
                max_key = i_key
                maxstring_index = int(i_value[1])
    return max_key

for place in range(3):
    print("\n{0} место: {1} –– {2}".format(place+1, sort(my_dict), my_dict.pop(sort(my_dict))[0]))