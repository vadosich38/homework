data1 = {1: 12, 2: 32, 13: 22, 12: "qw"}
data2 = "abwqewqc"

def convert(my_data):
    my_list = list(my_data)
    return my_list

data1 = convert(data1)
data2 = convert(data2)
def min_search(my_data1, my_data2):
    return min(len(my_data1), len(my_data2))

def my_zip(my_data1, my_data2):
    paars = ((my_data1[index], my_data2[index])
            for index in range(min_search(my_data1, my_data2)))
    paars_list = list(paars)
    return paars_list

print(my_zip(data1, data2))

