aliens = 2
password = "ALIENS"

print("\nQuickly! Aliens are invading the planet.")
print("You need to activate the global defence platforms.")
print("Hope you know the password, for Earth's sake...\n")
print("--------------------------------------------------")
print("       WELCOME TO THE GLOBAL DEFENCE NETWORK")
print("--------------------------------------------------\n")

# .upper() : converts strongs to all uppercase
guess = input("Please enter the password: "). upper()

while guess != password:
    print("\nINCORRECT PASSWORD.\n")
    
    # aliens = aliens ^ 2 
    # * = shift 8
    # ^ = shift 6
    aliens = aliens ** 2
    print("There are", aliens, "aliens now on Earth. Try again!")

    # if there are more than 8 billion aliens, break the loop
    if aliens > 8 * 10**9:
        break

    # give clue if there are more than 200 aliens
    if aliens > 200 and aliens < 60000:
        option = input("Choose a clue you want: A, B, or C")
        if option == "A":
            print("It begins the letter A")
        elif option == "B":
            print("They look weird.")
        elif option == "C":
            print("Best hint ever!")
            print("You are being attacked by them right now.")
        else: 
            print("You wasted your only other chance. No clue for you.")

    # if there are more than 60,000 aliens, give hint.
    if aliens > 6 * 10**4:
        print("\nPassword hint: the things that are attacking us.\n")
    
    # print guess input line again 
    guess = input("Quick! Please enter the password: "). upper()

    # after while loop breaks, check the number of aliens and print a certain line
    if aliens > 8 * 10**9:
        print("NOOOOOOOOO! The aliens have outnumbered us. All is lost...")
    else: 
        print("HOOORAY! We won the fight and the world is saved!")
