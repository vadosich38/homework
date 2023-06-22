import requests
import json
from typing import Dict


my_dict: Dict = dict()


def get_pilot_data() -> None:
    for pilot in data_dict['pilots']:
        pilot_data = json.loads(requests.get(pilot).text)
        pilot_homeworld_data = json.loads(requests.get(pilot_data['homeworld']).text)

        my_dict['pilots'].append({'height': pilot_data['height'], 'homeworld': pilot_homeworld_data['name'],
                                  'homeworld_url': pilot_data['homeworld'], 'mass': pilot_data['mass'],
                                  'name': pilot_data['name']})


data_dict = json.loads(requests.get("https://swapi.dev/api/starships/").text)
for elem in data_dict['results']:
    if elem['name'] == "Millennium Falcon":
        data_dict = elem

        my_dict = {'max_atmosphering_speed': data_dict['max_atmosphering_speed'], 'ship_name': data_dict['name'],
                   'starship_class': data_dict['starship_class'], 'pilots': list()}
        get_pilot_data()
        break

print(my_dict)
with open("starship.json", "w") as file:
    json.dump(my_dict, file, indent=4)
