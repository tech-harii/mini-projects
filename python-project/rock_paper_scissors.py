import random    #importing library

def game():

    player_wins =0
    bot_wins = 0
    tie = 0

    weapon = ['rock','paper','scissors']
    print("*REMEMBER* :\nType 'quit' or 'q' in order to finish the game and view the SCOREBOARD")
    while True:
        
        user_option = input("Enter 'Rock' / 'Paper' / 'Scissors' : ").lower()      # user chooses their response

        if(user_option == 'quit' or user_option == 'q'):
            print(f"\nGame Session Over ---\nSCOREBOARD:\nWINS : {player_wins}\nLOSES : {bot_wins}\nDRAWS : {tie}\n")
            print("Thanks for Playing! Play again sometime :)\n")
            break

        if user_option not in weapon:         
            print("Enter valid response please...")
            continue
        
        bot_option = weapon[random.randint(0,2)]

        if (user_option == bot_option):
            tie +=1
            print(f"You both chose {user_option}\nx Match Drawn! x\n")
            continue

        elif ( (user_option == 'rock' and bot_option == 'scissors') or (user_option == 'scissors' and bot_option == 'paper') or (user_option == 'paper' and bot_option == 'rock')):
            player_wins +=1
            print(f"You chose {user_option}\nMatch WON!  :)\n")
            continue
        else:
            bot_wins +=1
            print(f"Bot chose {bot_option}\nMatch LOST!  :(\n")
            continue
        
game()