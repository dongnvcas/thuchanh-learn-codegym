import random
check = True
while check:
    turn = random.randint(0,1)
    current_number = 0
    player_choice = 0
    computer_choice = 0
    if turn == 0:
        current_player = "human"
    else:
        current_player = "computer"
    print(f"Current player is: {current_player}")
    while current_number <= 21:
        print(f"Current number is: {current_number}")
        if current_player == "human":
            player_choice = int(input("Please input your choice: "))
            if player_choice in range(1,4):
                current_number += player_choice
                if current_number >= 21:
                    print("Computer win")
                    break
                else:
                    current_player = "computer"
            else:
                print("Please input the correct number")
        else:
            computer_choice = random.randint(1,3)
            print(f"Computer choice is: {computer_choice}")
            current_number += computer_choice
            current_player = "human"
            if current_number >= 21:
                print("Player win")
                break
            else:
                current_player = "human"
    recheck = True
    while recheck:
        game_finish = input("Do you want to continue playing? Y/N: ")
        if game_finish.upper() == "Y":
            check = True
            recheck = False
        elif game_finish.upper() == "N": 
            print("Game over. Thank you")
            check = False
            recheck = False
        else:
            recheck = True
            print("Please input Y or N only")