import random

player_points = 0
bot_points = 0

print("Rock Paper Scissors Game")

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("\nGame Over")
        print("Your Score:", player_points)
        print("Computer Score:", bot_points)
        break

    mapping = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }

    if choice not in mapping:
        print("Invalid Input")
        continue

    player = mapping[choice]
    computer = random.choice(["rock", "paper", "scissors"])

    print("You:", player)
    print("Computer:", computer)

    if player == computer:
        print("Match Draw")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You Won")
        player_points += 1

    else:
        print("Computer Won")
        bot_points += 1

    print(f"Score -> You: {player_points} | Computer: {bot_points}")