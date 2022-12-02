n = int(input("Введите целое число: "))

nums = [1 if index % 2 == 0 else index % 5 for index in range(n)]
print(nums)