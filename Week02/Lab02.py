import random

choices = ["Rock", "Paper", "Scissors"]
playerChoice = int(input("Choose a number between the dollowing: 1-Rock, 2-Paper, 3-Scissors: "))

# Input check
if playerChoice < 1 or playerChoice > 3:
    print("Error: you should choose a number between 2 and 3!")

else:
    # Develop the game logic through if/elif/else
    print("Player 1 (You) have selected: " + choices[playerChoice-1])
    player2Choice = random.randint(1, 3)
    print("Player 2 has selected: " + choices[player2Choice-1])

    if playerChoice == player2Choice:
        print("It's a tie!")
    elif (playerChoice == 1 and computerChoice == 3) or (playerChoice == 1 and computerChoice == 3) 
    elif (playerChoice+1)%3 == player2Choice:
        print("Player 1 loses :(")
        elif (playerChoice+1)%3 == player2Choice:
        print("Player 1 loses :(")