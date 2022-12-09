string = "ab1n32kz2"
nums_set = set(string)

print("Уникальныe цифры в строке:", end = " ")
for symbol in nums_set:
    if '0' <= symbol <= '9':
        print(symbol, end= "")