import json
from typing import Dict, List
"""
Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list, выведите различие.
Иными словами, вам нужно отловить изменение определённых параметров и вывести значение: что изменилось и на что.
Набор ключей в обоих файлах идентичный, различаются лишь значения.

Напишите программу, которая:
загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
выполняет сравнение параметров, указанных в diff_list;
формирует результат в виде словаря;
записывает словарь в JSON-файл с названием result.json.
"""
res_dict: Dict = dict()
res_list: List = list()
diff_list = ['services', 'staff', 'datetime']
my_keys_list: List = list()


def check(key):
    temp_dict1 = old_dict
    for i_key in my_keys_list:
        temp_dict1 = temp_dict1[i_key]

    temp_dict2 = new_dict
    for i_key in my_keys_list:
        temp_dict2 = temp_dict2[i_key]

    print(temp_dict1, "Старый:")
    print(temp_dict2, "Новый:")

    if temp_dict1 != temp_dict2:
        temp_str = "{} изменилось на {}".format(temp_dict1, temp_dict2)
        res_dict[key] = temp_str
        res_list.append(temp_str)


def going(my_dict):
    # нужна рекурсивня функция для глубокого прохода по ключам вложеных словарей
    for i_key in my_dict:
        if i_key in diff_list:
            my_keys_list.append(i_key)
            check(i_key)
            my_keys_list.remove(i_key)
#условие не задевает списки
        # print("Проверка типа:", my_dict[i_key])
        if type(my_dict[i_key]) is (dict or list):
            my_keys_list.append(i_key)
            going(my_dict[i_key])
            my_keys_list.remove(i_key)


with open("json_old.json", "r") as file:
    old_dict = json.load(file)
with open("json_new.json", "r") as file:
    new_dict = json.load(file)

going(old_dict)


print(res_dict)
print(res_list)


"""
В консоли должно вывестись следующее сообщение:
{'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 
'datetime': '2022-01-25T13:00:00+03:00'}

Помимо вывода в консоль, должен быть сформирован JSON-файл с получившимся словарём (result.json).
Обратите внимание: в result представлены не все изменившиеся поля, а лишь те, что объявлены в diff_list.
"""