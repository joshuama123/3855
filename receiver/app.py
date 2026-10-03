import connexion
from connexion import NoContent
import json
import os 

# placeholder data if data.json doesn't exist
empty_data = {
    "match_events": 0,
    "player_kills_events": 0,
    "match": [],
    "player_kills": []
}

def report_match(body):
    print("Received match event: ", body)

    if os.path.isfile("data.json"):
        with open("data.json", "r") as f:
            curr_data = json.load(f)
    else:
        curr_data = empty_data

    curr_data["match"].append(body)
    curr_data["match_events"] += 1

    with open("data.json", "w") as f:
        json.dump(curr_data, f, indent=2)

    return (NoContent, 201)

def report_player_kill(body):
    print("Received player kills event: ", body)

    if os.path.isfile("data.json"): 
        with open("data.json", "r") as f:
            curr_data = json.load(f)
    else:
        curr_data = empty_data

    curr_data["player_kills"].append(body)
    curr_data["player_kills_events"] += 1

    with open("data.json", "w") as f:
        json.dump(curr_data, f, indent=2)

    return NoContent, 201

app = connexion.AsyncApp(__name__, specification_dir='')
app.add_api("fortnite.yaml", strict_validation=True, validate_responses=True)
