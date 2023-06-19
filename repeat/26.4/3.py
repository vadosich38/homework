class Primes:
    def __init__(self, cur_num=1, max_num=0):
        self.__max_num = max_num
        self.__curr_num = cur_num

    def __iter__(self):
        return self

    @classmethod
    def __isprime(cls, num):
        if num != 2 and num % 2 == 0 or num == 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        while self.__curr_num < self.__max_num:
            self.__curr_num += 1
            if self.__isprime(self.__curr_num):
                return self.__curr_num
        else:
            raise StopIteration


prime_nums = Primes(max_num=50)
for i_elem in prime_nums:
    print(i_elem, end=' ')

# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47