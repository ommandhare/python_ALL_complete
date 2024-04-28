import random

target_number = random.randint(0, 100)

attempts=0
game_won=False

print("Welcome to the Number Guessing Game!")


while not game_won:
    user_guess = int(input("Guess the number between 0 and 100: "))
    attempts += 1
    if attempts >7 :
        print("you loss the game ")
    else:
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            game_won = True

print("Thanks for playing!")
