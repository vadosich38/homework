coutries = int(input("Введите кодичество стран: "))
geo_list = list()
geo_dict = dict()
for i_county in range(coutries):
    geo_list = input("Введите страну и города этой страны: ").split()
    geo_dict[geo_list[0]] = geo_list[1:]

for i_city in range(3):
    city_name = input("Введите название города: ")
    flag = True
    for i_key in geo_dict:
        if city_name in geo_dict[i_key]:
            print("Город {0} расположен в стране {1}.".format(city_name, i_key))
            flag = False
    if flag:
        print("По городу {} данных нет.".format(city_name))