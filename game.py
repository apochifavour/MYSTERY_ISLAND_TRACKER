MAP = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}


DESCRIPTIONS = {
    "Beach": (
        "You are standing on the Beach, where your journey begins. "
        "You can travel to the Jungle."
    ),

    "Jungle": (
        "You are in the Jungle. You can collect a rope here. "
        "You can return to the Beach or travel to the Cave."
    ),

    "Cave": (
        "You are inside a dark Cave. You can collect a lantern here. "
        "You can return to the Jungle or travel to the Old Bridge."
    ),

    "Old Bridge": (
        "You are standing at the Old Bridge. "
        "You need a rope to cross towards the Lighthouse. "
        "You can return to the Cave."
    ),

    "Lighthouse": (
        "You have reached the Lighthouse. "
        "You need a lantern to light it. "
        "You can return to the Old Bridge."
    )
}


def get_location_description(player):
    location = player["location"]
    inventory = player["inventory"]

    if location == "Jungle" and "rope" in inventory:
        return (
            "You have already collected the rope. "
            "You can return to the Beach or travel to the Cave."
        )

    if location == "Cave" and "lantern" in inventory:
        return (
            "You have already collected the lantern. "
            "You can return to the Jungle or travel to the Old Bridge."
        )

    if location == "Old Bridge" and "rope" in inventory:
        return (
            "You have your rope! "
            "You are ready to cross towards the Lighthouse."
        )

    if location == "Lighthouse" and "lantern" not in inventory:
        return (
            "You have reached the Lighthouse. "
            "You need a lantern to light it."
        )

    if location == "Lighthouse" and "lantern" in inventory:
        return (
            "You have your lantern! "
            "You are ready to light the Lighthouse and complete your adventure."
        )

    return DESCRIPTIONS[location]


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


def is_valid_name(name):
    return bool(name.strip())


def move(player, direction):
    if player["game_over"]:
        return False, "The game is over."

    current_location = player["location"]

    # Allow lowercase and uppercase directions.
    direction = direction.strip().lower()

    # Convert direction to the correct map location.
    destinations = {
        location.lower(): location
        for location in MAP[current_location]
    }
    if current_location == "Cave":
        destinations["bridge"] = "Old Bridge"
        
    if direction not in destinations:
        return False, "You cannot travel in that direction."

    destination = destinations[direction]

    # The player needs a rope to cross to the Old Bridge.
    if current_location == "Cave" and destination == "Old Bridge":
        if "rope" not in player["inventory"]:
            return False, "You need a rope to cross to the Old Bridge."

    player["location"] = destination
    player["energy"] -= 1

    if player["energy"] <= 0:
        player["game_over"] = True
        return True, "You have run out of energy. Game over!"

    return True, f"You moved to {destination}."


def collect_item(player):
    if player["game_over"]:
        return False, "The game is over."

    location = player["location"]

    if location not in player["items"]:
        return False, "There is nothing to collect here."

    item = player["items"].pop(location)

    player["inventory"].append(item)

    return True, f"You collected the {item}!"


def light_lighthouse(player):
    if player["game_over"]:
        return False, "The game is over."

    if player["location"] != "Lighthouse":
        return False, "You must reach the Lighthouse first."

    if "lantern" not in player["inventory"]:
        return False, "You need a lantern to light the Lighthouse."

    player["game_over"] = True
    player["won"] = True

    return True, "Congratulations! You lit the Lighthouse and won the game!"
