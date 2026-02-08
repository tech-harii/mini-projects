import random

print("Welcome to my 'Number Guessing Game', Player :)")

def game():
    while True:
        # Getting valid inputs from user-side
        while True:
            try:
                start = int(input("Enter the STARTING number: "))
                stop = int(input("Enter the ENDING number: "))

                if start >= stop:
                    print("STARTING must be less than ENDING. Try again.\n")
                    continue

                bet = input("Number of tries you bet to win (Enter '000' for infinite tries): ")
                
                if bet != '000':
                    bet = int(bet)
                    if bet <= 0:
                        print("Number of tries must be positive.\n")
                        continue

                break
            except ValueError:
                print("Enter valid inputs please...\n")

        random_no = random.randint(start, stop)

        # To Handle infinite attempts
        if bet == '000':
            attempts_left = float('inf') # attempts_left --> infinity*
        else:
            attempts_left = bet

        attempts_used = 0

        print(f"\nI have chosen a number between {start} and {stop}. Start guessing!\n")

        # Guessing loop
        while attempts_left > 0:
            try:
                user_ans = int(input("Enter your guess, player :) = "))
                attempts_used += 1

                if (user_ans == random_no):
                    print("Congrats! You've guessed correctly! :)")
                    print(f"You guessed it in {attempts_used} attempts.\n")
                    break

                elif (user_ans < random_no):
                    print("Too low!")

                else:
                    print("Too high!")

                attempts_left -= 1

                if attempts_left != float('inf'):
                    print(f"Attempts left: {attempts_left}\n")

            except ValueError:
                print("Please enter a valid number.\n")

        else:
            print("Oops! You've run out of attempts! :( )")
            print(f"The correct number was {random_no}\n")

        # To Play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing, Player! :) ")
            break

game()