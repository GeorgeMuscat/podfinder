from .fantasy import get_all_player_data
import json
from pprint import pprint

def main():
    with open("data.json", "w+") as fp:
        pprint(json.dump(get_all_player_data(), fp))

if __name__ == "__main__":
    main()