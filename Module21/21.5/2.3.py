import random
import string

data1 = {1, 2, 3}
data2 = {"a": 1, "r": 11, "weq": 33, "po": 11}

def my_zip(my_data1, my_data2, i=0):
    global list_out
    try:
        list_out.append((tuple(my_data1)[i], tuple(my_data2)[i]))
        i += 1
        my_zip(my_data1, my_data2, i)
    except IndexError:
        print(list_out)
list_out = list()
my_zip(data1, data2)