string1 = input("Введите строку: ")
string2 = input("Введите строку: ")
flag = False

if len(string1) != len(string2):
    print("Строки разной длины не могут быть идентичны!")
elif string1 == string2:
    print("Строки уже идентичны!")
else:
    for i_num in range(len(string1)-1):
        string2 = string2[-1] + string2[:len(string2)-1]
        if string1 == string2:
            print("Строки идентичны после {0} сдвигов".format(i_num+1))
            print("Строка один: {0}. Строка два: {1}".format(string1, string2))
            flag = True
    if not flag:
        print("Строки не могут быть идентичны!")