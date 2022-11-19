n = int(input("Введите целое положительное число: "))

def summ (n, counter):
    summ = 0
    for num in range(counter_f(n), 0, -1):
        summ = summ + n // 10 ** (num-1)
        n -= (n // 10 ** (counter_f(n)-1)) * 10 ** (counter_f(n)-1)
    return(summ)

def counter_f (n):
    counter = 0
    while n > 0:
        n = n // 10
        counter += 1
    return(counter)

print("Кол-во цифр в числе:", counter_f(n))
print("Сумма цифр:", summ(n, counter_f(n)))
print("Разность суммы и кол-ва цифр:", summ(n, counter_f(n)) - counter_f(n))