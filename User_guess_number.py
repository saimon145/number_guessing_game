#import random module
#define a function
#variable that label random number and second variable that label how many attempts
#define awhile loop for repeated asking to guess the number
#print  user to enter guess number
#use try catch block for prevent program crash
#use if else elif condition to give hints and declare to guess matched
#use second while loop to if user enter anything else except integer then it asked frequently until entered inger number
#use try except block for prevent program crash when take input

import random
def guess_number_game(x):
    computer_guess =random.randint(1, x)
    attempts=0
    while True:
        print(f"Guess a number between 1 and {x}: ")
        try:
            user_input = int(input("> "))
        except ValueError:
            print(f"please enter a valid integer number :")
            continue
        attempts+=1
        if user_input < computer_guess:
            print(f"your guess is too low")
        elif user_input > computer_guess:
            print(f"your guess is too high")
        else:
            print(f"congratulations your guess  is right {computer_guess} in {attempts} attempts")
            break
print(f"please enter the  number that computer randomly pick between 1 to your entered number:")
while True:
    try:

        number_limit = int(input("> "))
        guess_number_game(number_limit)
        break


    except ValueError:
        print("please enter a valid integer number :")





