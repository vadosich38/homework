site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
def search_key(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = search_key(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result

user_key = input("Искомый ключ: ")
res = search_key(site, user_key)

if res:
    print(res)
else:
    print("Такого ключа нет")
