# make a program which asks you one random addition math question
# and asks you until you get the answer correct
# every time you run the porgram, you should get a new question

# the program should end when you get the answer correct

# clue files:
#  - guessing.py for using import random and using while loops

import random

number1 = random.randint(1, 40)
number2 = random.randint(1, 40)
answer = (number1 + number2)

print("What is", number1, "+", number2, "?")
guess = int(input()) 

while guess != answer:
    guess = int(input("Try again! You're Wrong :(\n"))

if guess == answer:
    print("Your're correct!")
else: 
    print("You're wrong! Try again!")
