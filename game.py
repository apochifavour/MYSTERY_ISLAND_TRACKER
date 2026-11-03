
MAP = {
    "Beach": {"jungle": "Jungle"},
    "Jungle": {
        "beach": "Beach",
        "cave": "Cave"
    },
    "Cave": {
        "jungle": "Jungle",
        "bridge": "Old Bridge"
    },
    "Old Bridge": {
        "cave": "Cave",
        "lighthouse": "Lighthouse"
    },
    "Lighthouse": {
        "bridge": "Old Bridge"
    }
}


def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "items": {
            "Jungle": "rope",
            "Cave": "lantern"
        },
        "game_over": False,
        "won": False
    }


def move(player, direction):
    if player["game_over"]:
        return False, "The game is over."

    options = MAP[player["location"]]

    if direction not in options:
        return False, "You can't go that way."

    if (
        player["location"] == "Cave"
        and direction == "bridge"
        and "rope" not in player["inventory"]
    ):
        return False, "You need a rope to cross the bridge."

    player["location"] = options[direction]
    player["energy"] -= 1

    if player["energy"] <= 0:
        player["game_over"] = True
        return True, "You have run out of energy! GAME OVER. You lost!"

    return True, f"You walk to the {player['location']}."


def collect_item(player):
    if player["game_over"]:
        return False, "The game is over."

    location = player["location"]

    if location in player["items"]:
        item = player["items"].pop(location)
        player["inventory"].append(item)

        return True, f"You collected a {item}!"

    return False, "There is nothing to collect here."


def light_lighthouse(player):
    if player["game_over"]:
        return False, "The game is over."

    if player["location"] != "Lighthouse":
        return False, "You are not at the Lighthouse."

    if "lantern" not in player["inventory"]:
        return False, "You need a lantern to light the Lighthouse."

    player["game_over"] = True
    player["won"] = True

    return True, "Congratulations! You lit the Lighthouse and escaped Mystery Island!"
