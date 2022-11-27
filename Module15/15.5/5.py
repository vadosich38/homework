films_list = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
favorite_films_list = []
search_name_film = ""

while True:
    search_name_film = input("Введите название фильма: ")
    if search_name_film == ".":
        break
    flag = True
    for film_name in films_list:
        if film_name == search_name_film:
            flag = False
            favorite_films_list.append(search_name_film)
            print("Фильм добавлен в список любимых фильмов!")
    if flag:
        print("Ошибка! Такой фильм не найден!")

print("Список любимых фильмов:", favorite_films_list)