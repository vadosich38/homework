summ = 0


def counting(file_name):
    with open(file_name, "r", encoding="utf-8") as my_file:
        for line in my_file:
            for number in line.split():
                yield int(number)


for num in counting(file_name="numbers.txt"):
    summ += num
else:
    print(summ)

