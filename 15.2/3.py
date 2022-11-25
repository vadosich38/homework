n = int(input("Сколько собак участвует в бегах: "))
points_list = []
counter = 0

for _ in range(n):
    dog_points = int(input("Введите очки собаки: "))
    points_list.append(dog_points)

max = points_list[0]
min = points_list[0]
max_counter = 0
min_counter = 0
#проверка
print("Список очков собак:", points_list)

for points in points_list:
    if points > max:
        max = points
        max_counter = counter
    if points < min:
        min = points
        min_counter = counter
    counter += 1

print("Минимум очков:", min, ", у собаки под номером в списке:", min_counter+1)
print("Максимум очков:", max, ", у собаки под номером в списке:", max_counter+1)

points_list[max_counter], points_list[min_counter] = points_list[min_counter], points_list[max_counter]
print("Обновленный список очков собак:", points_list)


#повторная проверка
counter = 0
max = points_list[0]
min = points_list[0]
max_counter = 0
min_counter = 0

for points in points_list:
    if points > max:
        max = points
        max_counter = counter
    if points < min:
        min = points
        min_counter = counter
    counter += 1

print("Минимум очков:", min, ", у собаки под номером в списке:", min_counter+1)
print("Максимум очков:", max, ", у собаки под номером в списке:", max_counter+1)



