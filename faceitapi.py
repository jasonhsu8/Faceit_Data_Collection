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

#obj = requests.get("https://open.faceit.com/data/v4/matches/1-31717cf7-fd79-42c9-8e90-fd3ccf5947b4", headers=HEADER)

#obj1 = requests.get("https://open.faceit.com/data/v4/matches/1-31717cf7-fd79-42c9-8e90-fd3ccf5947b4/stats", headers=HEADER)

#obj2 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=0&limit=1900", headers=HEADER)

obj3 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=100&limit=1900", headers=HEADER)

obj4 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=200&limit=1900", headers=HEADER)

obj5 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=300&limit=1900", headers=HEADER)

obj6 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=400&limit=1900", headers=HEADER)

obj7 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=500&limit=1900", headers=HEADER)

obj8 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=600&limit=1900", headers=HEADER)

obj9 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=700&limit=1900", headers=HEADER)

obj10 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=800&limit=1900", headers=HEADER)

obj11 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=900&limit=1900", headers=HEADER)

obj12 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1000&limit=1900", headers=HEADER)

obj13 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1100&limit=1900", headers=HEADER)

obj14 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1200&limit=1900", headers=HEADER)

obj15 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1300&limit=1900", headers=HEADER)

obj16 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1400&limit=1900", headers=HEADER)

obj17 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1500&limit=1900", headers=HEADER)

obj18 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1600&limit=1900", headers=HEADER)

obj19 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1700&limit=1900", headers=HEADER)

obj20 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1800&limit=1900", headers=HEADER)


#print(obj.json())
#print(obj)

#with open("./Test.json", "w") as file:
#    json.dump(obj.json(), file)


#print(obj1.json())

#with open("./Test1.json", 'w') as file1:
#    json.dump(obj1.json(), file1, indent=2)


#file = json.load(obj.json())
#print(file)

#print(obj2.json())

with open("./Test3.json", 'w') as file3:
    json.dump(obj3.json(), file3, indent=2)

with open("./Test4.json", 'w') as file4:
    json.dump(obj4.json(), file4, indent=2)

with open("./Test5.json", 'w') as file5:
    json.dump(obj5.json(), file5, indent=2)

with open("./Test6.json", 'w') as file6:
    json.dump(obj6.json(), file6, indent=2)

with open("./Test7.json", 'w') as file7:
    json.dump(obj7.json(), file7, indent=2)
   
with open("./Test8.json", 'w') as file8:
    json.dump(obj8.json(), file8, indent=2)
   
with open("./Test9.json", 'w') as file9:
    json.dump(obj9.json(), file9, indent=2)

with open("./Test10.json", 'w') as file10:
    json.dump(obj10.json(), file10, indent=2)

with open("./Test11.json", 'w') as file11:
    json.dump(obj11.json(), file11, indent=2)

with open("./Test12.json", 'w') as file12:
    json.dump(obj12.json(), file12, indent=2)

with open("./Test13.json", 'w') as file13:
    json.dump(obj13.json(), file13, indent=2)

with open("./Test14.json", 'w') as file14:
    json.dump(obj14.json(), file14, indent=2)

with open("./Test15.json", 'w') as file15:
    json.dump(obj15.json(), file15, indent=2)

with open("./Test16.json", 'w') as file16:
    json.dump(obj16.json(), file16, indent=2)

with open("./Test17.json", 'w') as file17:
    json.dump(obj17.json(), file17, indent=2)

with open("./Test18.json", 'w') as file18:
    json.dump(obj18.json(), file18, indent=2)

with open("./Test19.json", 'w') as file19:
    json.dump(obj19.json(), file19, indent=2)

with open("./Test20.json", 'w') as file20:
    json.dump(obj20.json(), file20, indent=2)
   