import random

LOWER_BOUND = 1
UPPER_BOUND = 100
target_number = random.randint(LOWER_BOUND, UPPER_BOUND)
guessed_correctly = False

print("Welcome to the Number Guessing Game!")

while not guessed_correctly:
    guess = int(input(f"Guess a number between {LOWER_BOUND} and {UPPER_BOUND}: "))
    
    if guess < target_number:
        print("Your guess is too low.")
    elif guess > target_number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You've guessed the number correctly.")
        guessed_correctly = True