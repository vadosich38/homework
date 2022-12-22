#some_string = 'О Дивный Новый мир!'
#some_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
some_list = [100, 200, 300, 'буква', 0, 2, 'а']
#some_dict = {"key1": "0", "key2": "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "11"}
simpl_dig = list()

def is_prime(num, nums_list):
    flag = False
    if num == 2:
        nums_list.append(num)
        flag = True
    elif num == 3:
        nums_list.append(num)
        flag = True
    elif num < 2 or num % 2 == 0 or num % 3 == 0:
        flag = False
    else:
        q = int(num ** 0.5) + 2
        for i in nums_list:
            if i > q:
                flag = False
                break
            elif num % i == 0:
                flag = False
                break
            else:
                flag = True
                nums_list.append(num)
                break
    return flag


def crypt(text):
    return [text[index] for index, value in enumerate(text) if is_prime(index, simpl_dig)]

print(crypt(some_list))