#some_string = 'О Дивный Новый мир!'
#some_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#some_list = [100, 200, 300, 'буква', 0, 2, 'а']
some_dict = {"key1": "A", "key2": "B", 2: "A", 3: "B", 4: "A", 5: "B", 6: "A", 7: "B", 8: "A", 9: "B", 10: "A", 11: "B"}

def crypt(text):
    new_list = list()
    if isinstance(text, dict):
        for index, key in enumerate(text.keys()):
            if index % 2 == 0:
                temp = str(key) + ":" + some_dict[key]
                new_list.append(temp)
    else:
        for index, value in enumerate(text):
            if index % 2 == 0:
                new_list.append(value)
    return new_list

print(crypt(some_dict))