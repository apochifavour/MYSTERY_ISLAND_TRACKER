import game
from game import new_game, move, collect_item, light_lighthouse, get_location_description, parse_replay_answer, available_exits


def main():
    while True:
        print("==============================")
        print("  MYSTERY ISLAND")
        print("  THE LOST LIGHTHOUSE")
        print("==============================")

        player_name = input("What is your name? ").strip()

        while not player_name:
            print("Name cannot be empty. Please enter your name.")
            player_name = input("What is your name? ").strip()

        player = new_game(player_name)

        print(f"\nWelcome, {player_name}!")
        print("Find the rope and lantern.")
        print("Use them to reach and light the Lighthouse.")

        while not player["game_over"]:
            print("\n------------------------------")
            print(f"Location: {player['location']}")
            print(f"Energy: {player['energy']}")
            print(f"Inventory: {player['inventory']}")
            print("------------------------------")
            print(get_location_description(player))
            print("------------------------------")
            exits = available_exits(player)
            print("Exits: " + ", ".join(f"go {word}" for word in exits))
            choice = input(
                "Command (go <direction>, collect, light, quit): "
            ).strip().lower()

            if choice == "quit":
                print("Thanks for playing!")
                break

            elif choice == "collect":
                ok, message = collect_item(player)
                print(message)

            elif choice == "light":
                ok, message = light_lighthouse(player)
                print(message)

            elif choice.startswith("go "):
                direction = choice[3:].strip()
                ok, message = move(player, direction)
                print(message)

            else:
                print("I don't understand that.")
                print("Invalid command!")
                print("\nAvailable commands:")
                print("- go <direction>")
                print("- collect")
                print("- light")
                print("- quit")

        if choice == "quit":
            break
        while True:
            answer = parse_replay_answer(
                input("\nDo you want to play again? (yes/no): ")
            )
            if answer is not None:
                break
            print("Please type yes or no.")

        if not answer:
            print("\nThanks for playing Mystery Island!")
            break

        print("\nStarting a new game...\n")

if __name__ == "__main__":
    main()