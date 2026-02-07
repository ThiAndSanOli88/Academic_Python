#This Program will be a Number Guessing Game
import random
#This will define the numbers of attempts
attempts = 3
guess = range(1, 11)

print(f"You have {attempts} guesses left")

random.seed()
mysteryNum = random.randint(guess.start, guess.stop - 1)

while attempts > 0:
    user_input = input(f"Enter your guess between {guess.start} and {guess.stop - 1}: ") #This will colect the number guessing from the user. 

    if user_input.isnumeric():
        user_guess = int(user_input)
        #Boolean variables to control looping
        if user_guess in guess:
            if user_guess < mysteryNum:
                print(f"{user_guess} is too small.")
                guess = range(user_guess + 1, guess.stop)
            elif user_guess > mysteryNum:
                print(f"{user_guess} is too large.")
                guess = range(guess.start, user_guess)
            else:
                print(f"You correctly guessed the mystery number: {mysteryNum}")
                break

            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} {'guesses' if attempts > 1 else 'guess'} left")
            else:
                print(f"Sorry, game over! The mystery number was: {mysteryNum}")
        else:
            print(f"Invalid input. Please enter a number within the specified range {guess}.")
    else:
        print("Invalid input. Please enter a valid number.")

