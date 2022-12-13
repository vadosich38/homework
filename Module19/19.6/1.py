violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
def menu():
    minutes = 0
    count = int(input("Сколько песен выбрать? "))
    for i_num in range(count):
        name = input("Введите название песни: ")
        if name in violator_songs:
            minutes += violator_songs[name]
        else:
            print("Такой песни нет! Начните заново.")
            menu()
    return minutes

print("Общее время звучания песен:", round(menu(), 2))