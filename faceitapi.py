from email.header import Header
from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from urllib import request
from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd
load_dotenv()



faceit_id = os.getenv("FACEIT_PLAYER_ID")
api_key = os.getenv("API_KEY")
game_id = "csgo"

#print(faceit_id, api_key)
HEADER = {"Authorization": f"Bearer {api_key}"}







# Get match stats method
def get_match_stats(player_id, offset):
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

# Get Player History Method
def get_player_hist(player_id, start_time, end_time, offset):
    url = "https://open.faceit.com/data/v4/players/"
    headers=HEADER
    query = f"{player_id}/history?game=csgo&from={start_time}&to={end_time}offset={offset}&limit=10"

    query_url = url + query
    result = requests.get(query_url, headers=HEADER)
    json_result = json.loads(result.content)

    if len(json_result) == 0:
        print("No player history for this match")
        return None
    
    return json_result

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








# TESTS
# Test for get_match_stats
jj_faceit_id = faceit_id        
#obj = get_match_stats(jj_faceit_id, "0")
#print(obj)

# Test for get_player_hist
jj_start_time = "1518825600"
jj_end_time = "1695770460"
#obj1 = get_player_hist(jj_faceit_id, jj_start_time, jj_end_time,"0")
#print(obj1)

# Test for get_match_stats
jj_match_id = "1-eac8e2f3-19c2-46a5-83d9-a43ca18b1ede"
#obj2 = get_match_stats(jj_match_id)
#print(obj2)



# NEEDS FIXING, CANNOT JSON.DUMP FILE
#df = pd.read_json(obj, lines=True)
#print(df)
#with open("./Test.json", 'w') as file:
#    json.dump(obj.json(), file, indent=2)










#obj = requests.get("https://open.faceit.com/data/v4/matches/1-31717cf7-fd79-42c9-8e90-fd3ccf5947b4", headers=HEADER)

#obj1 = requests.get("https://open.faceit.com/data/v4/matches/1-31717cf7-fd79-42c9-8e90-fd3ccf5947b4/stats", headers=HEADER)

#obj2 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=0&limit=1900", headers=HEADER)

#obj3 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=100&limit=1900", headers=HEADER)

#obj4 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=200&limit=1900", headers=HEADER)

#obj5 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=300&limit=1900", headers=HEADER)

#obj6 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=400&limit=1900", headers=HEADER)

#obj7 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=500&limit=1900", headers=HEADER)

#obj8 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=600&limit=1900", headers=HEADER)

#obj9 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=700&limit=1900", headers=HEADER)

#obj10 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=800&limit=1900", headers=HEADER)

#obj11 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=900&limit=1900", headers=HEADER)

#obj12 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1000&limit=1900", headers=HEADER)

#obj13 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1100&limit=1900", headers=HEADER)

#obj14 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1200&limit=1900", headers=HEADER)

#obj15 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1300&limit=1900", headers=HEADER)

#obj16 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1400&limit=1900", headers=HEADER)

#obj17 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1500&limit=1900", headers=HEADER)

#obj18 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1600&limit=1900", headers=HEADER)

#obj19 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1700&limit=1900", headers=HEADER)

#obj20 = requests.get("https://open.faceit.com/data/v4/players/9a3bf080-a281-4e45-b1c8-2a90c7423d25/games/csgo/stats?offset=1800&limit=1900", headers=HEADER)




#print(obj1.json())

#with open("./Test1.json", 'w') as file1:
#    json.dump(obj1.json(), file1, indent=2)


#file = json.load(obj.json())
#print(file)

#print(obj2.json())