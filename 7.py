a = int(input("Введите начало периода (год): "))
b = int(input("Введите конец периода (год): "))
counter = 0

for year in range (a, b+1):
    first_num = year // 1000
    sec_num = (year - first_num*1000) // 100
    third_num = ((year - (first_num * 1000)) - (sec_num * 100)) // 10
    four_num = year % 10


    if first_num == sec_num == third_num:
        print("Несчастливый год:", year)
    elif first_num == third_num == four_num:
        print("Несчастливый год:", year)
    elif sec_num == third_num == four_num:
        print("Несчастный год:", year)

