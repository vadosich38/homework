violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

fav_list = []
count = int(input("Сколько песен добавим в список любимых: "))
summ_time = 0

for num in range(count):
    name = input("Введите название песни: ")
    for i_num in range(len(violator_songs)):
        if violator_songs[i_num][0] == name:
            summ_time += violator_songs[i_num][1]
            fav_list.append(violator_songs[i_num][0])
print("Общая продолжительность треклиста:", round(summ_time, 2))
print("Список любимых песен:", fav_list)