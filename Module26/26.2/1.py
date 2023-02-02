my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_itterator = iter(my_list)

while True:
    try:
        print(my_itterator.__next__())
    except StopIteration:
        break
