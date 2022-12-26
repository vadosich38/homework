def factorial(my_num):
    if my_num == 1:
        return 1
    return my_num * factorial(my_num-1)

print(factorial(5))