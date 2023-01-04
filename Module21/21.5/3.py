num_pos = int(input("Введите позицию искомого числа: "))

def fibonaci(position, counter_pos=2):
    global fibonaci_list
    new_num = fibonaci_list[-1] + fibonaci_list[-2]
    fibonaci_list.append(new_num)

    counter_pos += 1
    if counter_pos == position:
        return print(new_num), print(fibonaci_list)
    else:
        fibonaci(position, counter_pos)

fibonaci_list = [1, 1]
fibonaci(num_pos)