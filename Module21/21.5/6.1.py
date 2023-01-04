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
def my_func(struct, counter, my_start, my_dict = dict()):
    if my_start > counter:
        return
    else:
        product_name = input("Введите название продукта для нового сайта: ")
        struct["html"]["head"]["title"] = "Куплю/продам {} недорого".format(product_name)
        struct["html"]["body"]["h2"] = "У нас самая низкая цена на {}".format(product_name)
        my_start += 1
        my_dict[product_name] = struct
        for product, site in my_dict.items():
            print("Сайта для {}:".format(product), site)
        my_func(struct, counter, my_start)

sites_count = int(input("Какое количество сайтов: "))
start = 1
my_func(site, sites_count, start)
