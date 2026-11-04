from game import new_game, move, collect_item, light_lighthouse


def main():
    while True:
        print("==============================")
        print("  MYSTERY ISLAND")
        print("  THE LOST LIGHTHOUSE")
        print("==============================")

        name = input("What is your name? ").strip()

        player = new_game(name)

        print(f"\nWelcome, {name}!")
        print("Find the rope and lantern.")
        print("Use them to reach and light the Lighthouse.")

        while not player["game_over"]:
            print("\n------------------------------")
            print(f"Location: {player['location']}")
            print(f"Energy: {player['energy']}")
            print(f"Inventory: {player['inventory']}")
            print("------------------------------")

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

        if choice == "quit":
            break

        replay = input(
            "\nDo you want to play again? (yes/no): "
        ).strip().lower()

        if replay != "yes":
            print("\nThanks for playing Mystery Island!")
            break

        print("\nStarting a new game...\n")


if __name__ == "__main__":
    main()