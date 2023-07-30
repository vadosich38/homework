import json
from typing import Dict, List, Any

res_dict: Dict = dict()
diff_list = ['services', 'staff', 'datetime']


def check(value_to_check_1: Dict, value_to_check_2: Dict, key: Any) -> None:
    """
    Функция сравнивает значения переданых values словаря
    Если значения не одинаковы, в словарь изменений res_dict записывается новая версия значения под тем же ключем
    :param value_to_check_1: первое значение к сравнению
    :param value_to_check_2: второе значение к сравнению
    :param key: ключ, которому соответствуют значения для сравнения
    :return: None
    """
    if value_to_check_1 != value_to_check_2:
        res_dict[key] = value_to_check_2


def going(go_new: Dict, go_old: Dict) -> None:
    """
    Рекурсивная функция, которая проходит по словарю и его вложеным словарям
    Если ключ словаря является искомым (тем, что нужно проверять на изменения в содержании), вызывается
    функция проверки check
    :param go_new: первый словарь к сравнению
    :param go_old: второй словарь к сравнению
    :return: None
    """
    if isinstance(go_new, dict):
        for key in go_new:
            if isinstance(go_new[key], dict):
                going(go_new=go_new[key], go_old=go_old[key])

            if key in diff_list:
                check(value_to_check_1=go_new[key], value_to_check_2=go_old[key], key=key)


with open("json_old.json", "r") as old_file, open("json_new.json", "r") as new_file:
    old_dict = json.load(old_file)
    new_dict = json.load(new_file)

going(go_new=old_dict, go_old=new_dict)
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(res_dict, file, ensure_ascii=False, indent=4)

print(res_dict)
