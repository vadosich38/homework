num = int(input("Введите число: "))
my_dict = dict()
for num in range(1, num+1):
    my_dict[num] = num**2
print(my_dict)
