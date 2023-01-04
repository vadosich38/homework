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
def my_func(struct):
    product_name = input("Введите название продукта для нового сайта: ")
    struct["html"]["head"]["title"] = "Куплю/продам {} недорого".format(product_name)
    struct["html"]["body"]["h2"] = "У нас самая низкая цена на {}".format(product_name)
    return print(struct)

count = int(input("Какое количество сайтов: "))

for _ in range(count):
    my_func(site)
