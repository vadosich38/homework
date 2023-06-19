class Primes:
    def __init__(self, max):
        self.__fact = 0
        self.__max = max

    def __iter__(self):
        return self

    def __next__(self):
        while self.__fact != self.__max:
            self.__fact += 1
            if (self.__fact < self.__max) and (self.__isprime(num=self.__fact)):
                return self.__fact
            elif self.__fact >= self.__max:
                raise StopIteration

    def __isprime(self, num):
        if num != 2 and num % 2 == 0 or num == 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
        return True


prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
