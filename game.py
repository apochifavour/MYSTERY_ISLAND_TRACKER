MAP = {
    "Beach":  {"jungle": "Jungle"},
    "Jungle": {"beach": "Beach", "cave": "Cave"},
    "Cave":   {"jungle": "Jungle", "bridge": "Old Bridge"},
    # TODO: 
}

def new_game(name):
    """Return a brand-new player dictionary."""
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],      
        "game_over": False,
        "won": False,
    }

def move(player, direction):
    """Try to move. Return (True, message) on success, (False, message) if rejected."""
    if player["game_over"]:
        return False, "The game is over."
    options = MAP[player["location"]]
    if direction not in options:
        return False, "You can't go that way."  
    player["location"] = options[direction]
    player["energy"] -= 1
    if player["energy"] <= 0:
        player["game_over"] = True
    return True, f"You walk to the {player['location']}."