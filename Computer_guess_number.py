import random
#this is a game where computer guess the number
# if the guessing number matched then game finished otherwise asked to guess the number until matched






#import random module
#define a function
#variable that label function parameter
#second variable that label how many attempts
#define a  while loop for repeated asking to guess the number
#variable that label computer guess number

#use if else elif condition to give hints and declare to guess matched
#use second while loop to if user enter anything else except integer then it asked frequently until entered inger number
#use try except block for prevent program crash when take input


def computer_guess(x):
    user_number=x
    attempts=0
    while True:
        computer_guess=random.randint(1,x)
        attempts+=1
        if computer_guess < user_number:
            print("computer guess is too low ")
        elif computer_guess > user_number:
            print("computer guess is too high ")
        else:
            print(f"congratulations your guess number is correct {computer_guess} in {attempts} attempts")
            break







print("Please pick a number then computer guess that number ")
while True:
      try:

        user_input = int(input("> "))
        computer_guess(user_input)
        break
      except ValueError as e:
          print(f"Please enter the integer number only!")












