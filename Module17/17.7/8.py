import random
sticks_count = random.randint(5, 25)
print("Всего палочек:", sticks_count)

push_count = random.randint(1, 3)
print("Бросков:", push_count)
res_list = ["|" for _ in range(sticks_count)]
print("Изначальный спсиок:", res_list)

for res in range(push_count):
    l_res = random.randint(1, 3)
    r_res = random.randint(6, sticks_count)
    print("Сбиваю палки с", l_res, "по", r_res)
    res_list = ["." if x+1 >= l_res and x+1 <= r_res else "|" for x in range(sticks_count) ]

print("Список на выход:", res_list)
