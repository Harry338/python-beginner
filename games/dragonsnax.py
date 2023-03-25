import random

print("You are in a dark room in a mysterious castle")
print("In front of you are 3 doors. You must choose one")

player_choice = input("Choose 1, 2, or 3...\n")

if player_choice == "1":
    print("You find a room full of treasure. You're rich!")
    print("GAME OVER, YOU WIN!")
elif player_choice == "2":
    print("THe door opens and an angey ogre hits you with his club.")
    print("GAME OVER, YOU LOSE!")
elif player_choice == "3":
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon to the exit.")


    dragon_choice = input("Choose 1 or 2")

    if dragon_choice == "1":
        treasure_chance = random.randint(1, 10)
        if treasure_chance <= 3: 
            print("You have stolen the gold successfully and escaped to the exit!")
            print("GAME OVER, YOU WIN!")
        else:
            print("The dragon wakes up and eats you. You are delicious")
            print("GAME OVER, YOU LOSE")
    elif dragon_choice == "2":
        exit_chance = random.randint(1, 10)
        if exit_chance <= 5:
            print("The dragon heard your footsteps and woke up!")
            print("The dragon ate you. You are delicious.")
            print("GAME OVER, YOU LOSE!")
        else:
            print("You sneak around the dragon and escape the castle, blinking in the sunshine.")
            print("GAME OVER, YOU WIN!")
    else:
        print("You didn't enter 1 or 2!")

else:
    print("Sorry, you didn't enter 1, 2 or 3!")


print("Run the game again to have another go")