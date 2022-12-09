small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}
big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)

while True:
    name = input("Введите наименование товара: ")
    if name in big_storage:
        print(name, ":", big_storage.get(name), "шт.")
    else:
        print("Такого товара нет на складе")