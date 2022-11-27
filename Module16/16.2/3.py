films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

def search_film(film_name, user_list):
    for film in user_list:
        if film == film_name:
            return True
    return False
def menu():
    user_list = []
    while True:
        print("Ваш текущий топ фильмов:", user_list)
        film_name = input("Название фильма: ")
        print("Команды: добавить, вставить, удалить")
        comand = input("Введите команду: ")

        if comand == "добавить":
            if search_film(film_name, user_list):
                print("Этот фильм уже есть в вашем списке!")
            else:
                user_list.append(film_name)
        elif comand == "удалить":
            if search_film(film_name, user_list):
                user_list.remove(film_name)
            else:
                print("Такого фильма нет в вашем списке!")
        elif comand == "вставить":
            pos = int(input("На какое место: "))
            user_list.insert(pos-1, user_list.pop(user_list.index(film_name)))
    menu()

menu()
