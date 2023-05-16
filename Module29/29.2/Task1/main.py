import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    except Exception as ex:
        print("Ошибка {}".format(ex))
    finally:
        print("Время выполнения: {}".format(time.time()-start))


with timer() as t1:
    my_list1 = [x for x in range(100000) if x % 2 == 0]
    my_list2 = [x if x // 2 == 0 else x ** 4 for x in range(100000)]

with timer() as t2:
    my_list3 = [x for x in range(1000000) if x % 2 == 0]
    my_list4 = [x if x // 2 == 0 else x ** 4 for x in range(1000000)]


with timer() as t3:
    my_list5 = [x for x in range(10000000) if x % 2 == 0]
    my_list6 = [x if x // 2 == 0 else x ** 4 for x in range(10000000)]
