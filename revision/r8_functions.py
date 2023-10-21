# copy the code from r4_import_random.py
# put the code for dice and coin into separate functions

# put the if conditions and other code into 
#another function called main

# you should have 3 functions in total and a code which starts
# the main function

import random

# coin = random.randint(1,2)
# dice = random.randint(1,6)

# print("Would you like to flip a coin or roll a dice? [1,2]")

# user_choice = int(input("Choose 1 or 2\n"))

# if user_choice == 1:
#     if coin == 1:
#         print('heads')
#     elif coin == 2:
#         print('tails')
    
# elif user_choice == 2:
#     print(dice)


def dice_function(dice):
    print(dice)


def coin_function(coin):
    if coin == 1:
        print('heads')
    elif coin == 2:
        print('tails')

def main():
    coin = random.randint(1,2)
    dice = random.randint(1,6)
    
    print("Would you like to flip a coin or roll a dice? [1,2]")

    user_choice = int(input("Choose 1 or 2\n"))

    if user_choice == 1:
        coin_function(coin)
    elif user_choice == 2:
        dice_function(dice)

main()