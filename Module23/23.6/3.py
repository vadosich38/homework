import random
summ = 0

while summ < 777:
    num = int(input("Введите число: "))
    try:
        summ += num
        num_gen = random.randint(1, 14)
        if num_gen == 2:
            raise Exception
        else:
            with open("res3.txt", "a", encoding="utf-8") as res_file:
                res_file.write("{}\n".format(num))
    except Exception:
        print("Возникла ошибка!")
        raise
else:
    print("Сумма:", summ)
