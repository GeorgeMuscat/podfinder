import requests
BASE_URL = "https://fantasy.nrl.com/data"

s = requests.Session()

def pull_players():
    r = s.get(f"{BASE_URL}/nrl/players.json")
    r.raise_for_status()
    return r.json()

def pull_player_stats(external_player_id: int):
    r = s.get(f"{BASE_URL}/nrl/stats/players/{external_player_id}.json")
    r.raise_for_status()
    return r.json()

def get_all_player_data():
    players = pull_players()

    return [{**player, "match_stats": pull_player_stats(player["id"])} for player in players]

def upsert_player_info(external_player_info: dict):
    # First check if player with the
    pass


def upsert_player_stats(player_stats: dict):
    pass