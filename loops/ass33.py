import random

def display_matchsticks(matchsticks):
    print("Matchsticks remaining:", matchsticks)
    print("| " * matchsticks)
    print()

def user_move():
    while True:
        try:
            move = int(input("Your move (1-4 matchsticks): "))
            if 1 <= move <= 4:
                return move
            else:
                print("Invalid move. Please choose between 1 and 4 matchsticks.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(matchsticks):
    # Simple computer strategy: Always leave a multiple of 4 matchsticks.
    number = random.randint(1, 4)
    matchsticks=number
    return (matchsticks)

matchsticks = 21

while matchsticks > 0:
        display_matchsticks(matchsticks)

        # User's move
        user_matches = user_move()
        matchsticks -= user_matches

        if matchsticks <= 0:
            print("Congratulations! You win!")
            break

        display_matchsticks(matchsticks)

        # Computer's move
        computer_matches = computer_move(matchsticks)
        print("Computer's move:", computer_matches)
        matchsticks -= computer_matches

        if matchsticks <= 0:
            print("Oops! You lose. Better luck next time.")
            break

