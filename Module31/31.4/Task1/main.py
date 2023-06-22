import requests
import json

link = "https://swapi.dev/api/people/3/"

req = requests.get(link) #запрос на страницу (парсинг страницы)
my_dict = json.loads(req.text) #провел десереализацию json в словарь
my_dict["name"] = "Vladyslav" #в словаре заменил имя
print(my_dict)

#записал файл json на диск
with open("my_file.json", "w") as file:
    json.dump(my_dict, file, indent=4)

link2 = my_dict["homeworld"] #в add_req записал значение homeworld из словаря
req2 = requests.get(link2) #в req2 спарсил страницу
my_json2 = json.loads(req2.text) #провел десереализацию json в словарь
print(my_json2)

#записал файл json на диск
with open("my_file2.json", "w") as file:
    json.dump(my_json2, file, indent=4)
