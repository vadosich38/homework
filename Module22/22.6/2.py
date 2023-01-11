file = open("zen.txt", "r", encoding="utf-8")
for i_string in (file.readlines())[::-1]:
    print(i_string, end="")
file.close()