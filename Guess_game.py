import random

print("Welcome to my 'Number Guessing Game'")

def game():
    try:
        start = int(input("Enter the START number: "))
        stop = int(input("Enter the STOP number: "))
        bet = (input("Number of ties you bet to win (Enter '000' for infinite tries): "))
        
        if (start == stop or stop < start):
            print("Please enter valid inputs...")
            
    except:
        print("Enter valid inputs please...")
        game()

    random_no = random.randint(start,stop)

    if bet=='000':
        bet = 100000  #infinite tries
    else:
        bet = int(bet)
    


    print('\n')
    
    
