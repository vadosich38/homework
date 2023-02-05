def read_numbers(file_name):
    with open(file_name) as my_file:
        for line in my_file:
            for number in line.split():
                yield int(number)


def main(file_name="numbers.txt"):
    total = 0
    for number in read_numbers(file_name):
        total += number
    return total


print(main())
