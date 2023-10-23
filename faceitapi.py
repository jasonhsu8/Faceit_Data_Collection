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

print(obj.json())
print(obj)

#file = json.load(obj.json())
#print(file)
