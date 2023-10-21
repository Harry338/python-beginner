# Task:
# Code a program which asks the following:
# Would you like to flip a coin or roll the dice? [1, 2]

# if the user types 1, 
# the program will either give "heads" or "tails"

# if the user types 2, 
# the program will give a random number between 1 and 6 inclusive.

# if the user types something different, then it will 

import random

coin = random.randint(1,2)
dice = random.randint(1,6)

print("Would you like to flip a coin or roll a dice? [1,2]")

user_choice = int(input("Choose 1 or 2\n"))

if user_choice == 1:
    if coin == 1:
        print('heads')
    elif coin == 2:
        print('tails')
    
elif user_choice == 2:
    print(dice)
    