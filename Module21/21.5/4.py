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

search_key = input("Введите искомый ключ: ")
deep = int(input("Введите максимальную глубину поиска (0 - не устанавливать глубину): "))

def key_search(key, struct, **kwargs):
    if "max_deep" in kwargs:
        kwargs["fact_deep"] += 1

    if key in struct:
        return struct[key]
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict) and (kwargs["fact_deep"] <= kwargs["max_deep"]):
                result = key_search(key, sub_struct, max_deep=kwargs["max_deep"], fact_deep=kwargs["fact_deep"])
                if result:
                    return result
        else:
            result = None

    return result

if deep == 0:
    res = key_search(search_key, site)
    if res:
        print(res)
    else:
        print("Такой ключ не найден")
else:
    res = key_search(search_key, site, max_deep=deep, fact_deep=1)
    if res:
        print(res)
    else:
        print("Такой ключ не найден!")