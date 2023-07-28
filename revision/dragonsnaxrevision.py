# make at least 3 rooms
# 1 room must have at least 2 sub rooms
# 1 room / subroom must have at least a riddle
# 1 room / subroom must be the winning exit
# 1 room / subroom must be the doom room (loses automatically)

# you do not need to use a while loop for this, but you can if you want

import random

questionlist = ["How many days of the year have 28 days?", "What goes up but never comes down?", "What is always spelt incorrect?", "I have a tail and a head, but no body. What am I?"]
answerlist = ["12", "age", "incorrect", "coin"]

print("You are in a abandoned mansion.")
print("In front of you there are 4 doors. You must choose one.")

player_choice = 0

player_choice = int(input("Choose 1, 2, 3 or 4\n"))

if player_choice == 1:
    riddle = random.randint (0,4)
    print("You enter the room and you see a giant Sphinx")
    print("The Sphinx says, Riddle me this,", questionlist[riddle])
    value = input("Give me a one worded and lowercase answer\n")
    if value == answerlist[riddle]:
        print("Good Job! You escaped!")
    elif value != answerlist[riddle]:
        print("You lost. You're trapped forever.")
elif player_choice == 2:
    print("You see a bright light ahead of you, you escaped!")
    print("Game Over, You won!")
elif player_choice == 3:
    print("You ran into a homeless man that was living in the mansion!")
    print("You got attacked and rot inside forever.")
    print("Game Over, You Lose!")
elif player_choice == 4:
    print("You got lucky! You found the rich man's treasure!")
    print("But there are security cameras everywhere!")
    print("Would you like to:")
    print("1) Take the risk")
    print("2) Leave it alone and escape freely")

    rob = input("Choose 1 or 2\n")
    
    if rob == 1:
        rob_chance = random.randint(1,10)
        if rob_chance <= 3:
            print("Not a chance! The cameras spotted you! You were locked up!")
        
    elif rob == 1:
        rob_chance = random.randint(1,10)
        if rob_chance <= 5:
            print("You escaped successfully sneaking past the cameras!")
    
    
    else: 
        print("You didn't enter 1 or 2!")

else: 
    print("You didn't enter 1, 2, 3, or 4!")

print("Run the game again if you want to try again!")
        
    
    
    





