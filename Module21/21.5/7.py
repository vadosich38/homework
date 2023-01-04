data1 = ([[1, 2, [3]], [1], 3])
#data1 = (1, 2, 3, 4, 5)

summ = 0
def my_sum(my_data):
    global summ
    for elem in my_data:
        if isinstance(elem, list):
            my_sum(elem)
        else:
            summ += elem
    return summ

print(my_sum(data1))