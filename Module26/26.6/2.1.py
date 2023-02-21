list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

result = next((x, y) for x in list_1 for y in list_2 if x * y == to_find)
print("Found!!!", result)
