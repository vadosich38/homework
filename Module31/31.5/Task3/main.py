import requests
import json


my_req = requests.get("https://swapi.dev/api/starships/")
data_dict = json.loads(my_req.text)

for elem in data_dict['results']:
    if elem['name'] == "Millennium Falcon":
        data_dict = elem

my_dict = {'max_atmosphering_speed': data_dict['max_atmosphering_speed'], 'ship_name': data_dict['name'],
           'starship_class': data_dict['starship_class'], 'pilots': list()}

for pilot in data_dict['pilots']:
    pilot_req = requests.get(pilot)
    pilot_data = json.loads(pilot_req.text)

    homeworld_req = requests.get(pilot_data['homeworld'])
    homeworld_data = json.loads(homeworld_req.text)

    my_dict['pilots'].append({'height': pilot_data['height'], 'homeworld': homeworld_data['name'],
                              'homeworld_url': pilot_data['homeworld'], 'mass': pilot_data['mass'],
                              'name': pilot_data['name']})

print(my_dict)
with open("starship.json", "w") as file:
    json.dump(my_dict, file, indent=4)
