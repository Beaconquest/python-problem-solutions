# python execrises from www.practicepython.org

# Execrise 8

while True:
    
    player_1 = str(input("Player 1 Rock, Paper, Scissors"))
    player_2 = str(input("Player 2 Rock, Paper, Scissors"))
  

    if player_1 == player_2:
        print(f"Both selected {player_1}, go again.")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif game == "no":
            break
    elif player_1 == "rock" and player_2 == "paper":
        print("Player 2 wins!")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif  game == "no":
            break
    elif player_1 == "rock" and player_2 == "scissors":
        print("Player 1 Wins!")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif game == "no":
            break
    elif player_1 == "paper" and player_2 == "rock":
        print("Player 1 wins!")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif game == "no":
            break
    elif player_1 == "paper" and player_2 == "scissors":
        print("Player 2 Wins!")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif game == "no":
            break
    elif player_1 == "scissors" and player_2 == "paper":
        print("Player 1 wins!")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif game == 'no':
            break
    if player_1 == "scissors" and player_2 == "rock":
        print("Player 2 Wins!")
        game = input("Would you like to play again?")
        if game == "yes":
            continue
        elif game == "no":
            break

print("Game Over!")