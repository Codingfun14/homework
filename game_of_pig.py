import random

def turn():
    player_score = 0
    round_score = 0
    computer_score = 0
    turn = 1

    print(f"Turn is {turn}")
    print(f"Your current score is: {player_score}")
    print(f"This round you have: {round_score}")
    print(f"Would you like to roll (r) or bank (b): ", end=" ")

    user_choice = input()
    
    if user_choice == "r":
        dice_value = random.randint(1, 6)
        if dice_value == 1:
            print("You rolled a 1! You get a zero for this round")
            round_score = 0
            turn += 1
        else:
            print(f"You rolled a {dice_value}.")
            round_score += dice_value
            return player_score

    if user_choice == "b":
        player_score += round_score
        round_score = 0
        turn += 1
    else:
        print("Invalid option. This will cost you a turn")
        turn += 1

    if turn == 2:
        print("computer turn")
        dice_value = random.randint(1, 6)
        if dice_value == 1:
            print("Computer rolled a 1!")
            round_score = 0
            return computer_score
        else:
            round_score += dice_value
            print(f"Computer rolled a {dice_value} so round score: {round_score}")
            computer_score += round_score
            print(f"Computer banked {round_score} points.")
            return computer_score


    while player_score < 100 and computer_score < 100:
        turn()

        if player_score >= 100:
            print("Good job! You win.")
            break

        if computer_score >= 100:
            print("You lost to the computer!!!")
            break