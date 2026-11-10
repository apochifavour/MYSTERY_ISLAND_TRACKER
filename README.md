# MYSTERY_ISLAND_TRACKER

# 🏝️ Mystery Island: The Lost Lighthouse

## 📖 About the Game

**Mystery Island: The Lost Lighthouse** is a text-based adventure game built with Python. Players explore a mysterious island, collect useful items, manage their energy, and solve challenges to reach and light the Lighthouse.

The goal is to survive the journey, collect the necessary items, and escape Mystery Island successfully!

## 🎮 Features

- **Player Introduction:** Enter your name before starting the adventure.
- **Name Validation:** Empty names and spaces-only inputs are rejected.
- **Island Exploration:** Move between locations using text commands.
- **Inventory System:** Collect and manage useful items.
- **Energy Management:** Every successful move costs energy.
- **Location Hints:** Receive helpful hints about your current location.
- **Game Over System:** The game ends when the player's energy runs out.
- **Winning Condition:** Reach the Lighthouse with the required item and light it to win.
- **Replay Functionality:** Start a new game after finishing an adventure.
- **Command Validation:** Invalid commands are rejected without changing the player's game state.
- **Automated Tests:** Unit tests verify important game mechanics.

## 🛠️ Technologies Used

- Python 3
- Python3 `unittest` framework
- Git and GitHub

## 📂 Project Structure

```text
mystery-island/
├── game.py
├── main.py
├── tests/
│   └── test_game.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check your Python installation:

```bash
python3 --version
```

### Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd mystery-island
```

### Run the Game

Start the game using:

```bash
python3 main.py
```

Enter your name when prompted, then follow the instructions to explore the island.

## 🕹️ How to Play

The game accepts the following commands:

| Command | Description |
|---|---|
| `go <direction>` | Move to a connected location |
| `collect` | Collect an available item |
| `light` | Attempt to light the Lighthouse |
| `quit` | Exit the game |

**Example commands:**

```text
go jungle
collect
go beach
quit
```

Use the location hints to understand your surroundings and decide what to do next.

### Game Rules

1. Enter a valid name to begin playing.
2. Explore the island using the available movement commands.
3. Collect useful items as you discover them.
4. Manage your energy carefully because successful movement consumes energy.
5. Follow the location hints to help you progress.
6. Obtain the items required to reach and light the Lighthouse.
7. Avoid running out of energy before completing your mission.

## 🧪 Running the Tests

The project uses Python's built-in `unittest` framework.

Run all tests with:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover features such as:

- Initial player state
- Successful movement and energy consumption
- Invalid movement
- Item collection
- Inventory restrictions
- Bridge-crossing requirements
- Lighthouse victory conditions
- Game Over conditions
- Replay state reset
- Player name validation

## 📈 Current Development Progress

The game currently includes the main gameplay loop, player movement, inventory management, energy tracking, name validation, location hints, victory and Game Over conditions, and automated tests.

Further improvements may include more detailed location descriptions, additional challenges, improved player guidance, and expanded test coverage.

## 👨‍💻 Learning Objectives

This project provides practical experience with:

- Python functions and modules
- Variables and data structures
- Conditional statements
- Loops and input validation
- Game-state management
- Writing unit tests
- Debugging Python applications
- Version control with Git
- Test-Driven Development (TDD)

## 🏆 Project Goal

Build a reliable, interactive text-based adventure game while developing strong Python programming, problem-solving, testing, and software engineering skills.



Enjoy exploring Mystery Island!