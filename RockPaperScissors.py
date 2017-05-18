keepPlaying = True

while keepPlaying:
    player1 = input("Player 1 plays: ")
    player2 = input("Player 2 plays: ")

    if player1 == player2:
        print("Draw")
    elif player1 == "rock":
        if player2 == "paper":
            print("Player 2 wins")
        elif player2 == "scissors":
            print("Player 1 wins")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")
        elif player2 == "scissors":
            print("Player 2 wins")
    elif player1 == "scissors":
        if player2 == "rock":
            print("Player 2 wins")
        elif player2 == "paper":
            print("Player 1 wins")

    keepPlaying = input("Continue playing?") in ["true", "t", "yes", "y"]

