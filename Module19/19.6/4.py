goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

summ = 0

for i_name in goods:
    for i_articl in store[goods[i_name]]:
        count = i_articl["quantity"]
        summ += count * i_articl["price"]
    print(i_name, "- {0}шт., стоимость {1} руб".format(count, summ))
    count = 0
    summ = 0