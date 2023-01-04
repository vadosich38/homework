site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}
def key_search(struct, key, new_data):
    if key in struct:
        struct[key] = new_data
        return struct
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = key_search(sub_struct, key, new_data)
                if result:
                    return struct

number_sites = int(input("Введите количество сайтов: "))
goods = dict()

for _ in range(number_sites):
    product_name = input("Введите название товара: ")
    key = {'title': "Куплю / продам {} недорого".format(product_name), 'h2': "y нас самая низкая цена на {}".format(product_name)}
    for i in key:
        key_search(site, i, key[i])
    name_of_product = "Сайт для {}:".format(product_name)
    goods[name_of_product] = site
    for key, value in goods.items():
        print(key)
        print(value)

