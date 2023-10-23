from email.header import Header
from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from urllib import request
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

faceit_id = os.getenv("FACEIT_PLAYER_ID")
api_key = os.getenv("API_KEY")

print(faceit_id, api_key)


HEADER = {"Authorization": f"Bearer {api_key}"}

obj = requests.get("https://open.faceit.com/data/v4/matches/1-31717cf7-fd79-42c9-8e90-fd3ccf5947b4", headers=HEADER)

obj1 = requests.get("https://open.faceit.com/data/v4/matches/1-31717cf7-fd79-42c9-8e90-fd3ccf5947b4/stats", headers=HEADER)

obj2 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=0&limit=1900", headers=HEADER)

#print(obj.json())
#print(obj)

with open("./Test.json", "w") as file:
    json.dump(obj.json(), file)


#print(obj1.json())

#with open("./Test1.json", 'w') as file1:
#    json.dump(obj1.json(), file1, indent=2)


#file = json.load(obj.json())
#print(file)

print(obj2.json())

with open("./Test2.json", 'w') as file2:
    json.dump(obj2.json(), file2, indent=2)
    