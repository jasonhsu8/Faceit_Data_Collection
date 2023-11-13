from email.header import Header
from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from urllib import request
from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd
load_dotenv()




# api_key
api_key = os.getenv("API_KEY")
game_id = "csgo"

print(api_key) #check to see if it works

HEADER = {"Authorization": f"Bearer {api_key}"}





# Get Match Stats Method
def get_match_stats(match_id):
    url = "https://open.faceit.com/data/v4/matches/"
    headers=HEADER
    query = f"{match_id}/stats"

    query_url = url + query
    result = requests.get(query_url, headers=HEADER)
    json_result = json.loads(result.content)

    if len(json_result) == 0:
        print("No stats for this match")
        return None
    
    return json_result





# Get match stats method
def get_player_match_stats(player_id, offset):
    url = "https://open.faceit.com/data/v4/players/"
    headers=HEADER
    query = f"{player_id}/games/csgo/stats?offset={offset}&limit=100"

    query_url = url + query
    result = requests.get(query_url, headers=HEADER)
    json_result = json.loads(result.content)

    if len(json_result) == 0:
        print("No stats for this match")
        return None
    
    return json_result








# get_match_stats
player = "liam"
match_id = "1-6984856f-57a1-4167-a88f-e96ae8ca828a"
obj = get_match_stats(match_id)
with open(f"./Match_Id_{player}.json", 'w') as file:
    json.dump(obj, file, indent=2)


# Check
player_id = os.getenv("FACEIT_PLAYER_ID")
print(player_id) #check to see if it works



# get_player_match_stats
liam_faceit_id = player_id    
offset = 900
offset_100 = offset + 100
player = "liam"
obj = get_player_match_stats(liam_faceit_id, offset)
with open(f"./Match_Stats_{offset}_{offset_100}_{player}.json", 'w') as file:
    json.dump(obj, file, indent=2)