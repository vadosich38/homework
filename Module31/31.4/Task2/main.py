import requests
import json

req = requests.get("https://swapi.dev/api/films/")
my_dict = json.loads(req.text)

print(my_dict["results"][0])
print(my_dict["results"][0]["opening_crawl"])
