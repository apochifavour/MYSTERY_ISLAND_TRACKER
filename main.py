from game import new_game, move

def main():
    name = input("What is your name? ").strip()
    player = new_game(name)
    while not player["game_over"]:
        print(f"\nLocation: {player['location']} | Energy: {player['energy']}")
        choice = input("Command (go <direction>, quit): ").strip().lower()
        if choice == "quit":
            break
        elif choice.startswith("go "):
            ok, message = move(player, choice[3:])
            print(message)
        else:
            print("I don't understand that.")   # state unchanged

if __name__ == "__main__":
    main()