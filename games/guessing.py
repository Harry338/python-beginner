import random
number = random.randint(1,20)
guess = -1

while guess != number:
    guess = int(input("I'm thinking of a number between 1 and 20. What is it?"))
    
    # if statements to check if guess is correct
    if guess == number:
        print("Nice! You guessed correctly")
    elif guess < number:
        print("Your number is higher")
    elif guess > number:
        print("Your number is lower")
