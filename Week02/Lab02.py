import random

choices = ["Rock", "Paper", "Scissors"]
player1Choice = int(input("Choose a number between the dollowing: 1-Rock, 2-Paper, 3-Scissors: "))-1
# unlike in the lab i chose to save player1Choice and player2Choice as integers between 0 and 2 (instead of between 1 and 3)
# this makes the rest of my code easier

# Input check
if player1Choice < 0 or player1Choice > 2:
    print("Error: you should choose a number between 1 and 3!")

else:
    # Develop the game logic through if/elif/else
    print("Player 1 (You) has selected: " + choices[player1Choice])
    player2Choice = random.randint(0, 2)
    print("Player 2 has selected: " + choices[player2Choice])

    # I did something that what we learned in class.
    # instead of creating a separate branch for each possible outcome I wanted to challenge myself to 
    # cover every possible outcome with just 3 branches and minimal lines of code.
    if player1Choice == player2Choice:
        print("It's a tie!")
        print("Player 1's " + choices[player1Choice] + " ties to Player 2's " + choices[player2Choice] + ".")
    elif (player1Choice+1)%3 == player2Choice:
        print("Player 1 loses :( ")
        print("Player 1's " + choices[player1Choice] + " loses to Player 2's " + choices[player2Choice] + ".")
    elif (player1Choice+2)%3 == player2Choice:
        print("Player 1 wins! :) ")
        print("Player 1's " + choices[player1Choice] + " beats Player 2's " + choices[player2Choice] + ".")
