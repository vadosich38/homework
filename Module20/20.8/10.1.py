#data1 = {'abc': 123, 'qwe': 222, 'eee': 543}
data1 = ["Tin", "Qer", "Aqe", "Alla"]
data2 = (10, 20, 30, 40)
#data2 = {'abc': 14, 'qwe': 43, 'eee': 22}
my_list_data1 = list(data1)
my_list_data2 = list(data2)

def my_zip(f_str, f_tuple):
    return f_str.pop(0), f_tuple.pop(0)

print("Первые данные:", data1, "\nВторые данные:", data2)
min_len = min(len(my_list_data1), len(my_list_data2))
for paar in range(min_len):
    print(my_zip(my_list_data1, my_list_data2))
# res = dict(my_zip(my_list_data1, my_list_data2))
# print(res)

print("\nОригинальная функция работает так:")
for i_elem in zip(data1, data2):
    print(i_elem)
