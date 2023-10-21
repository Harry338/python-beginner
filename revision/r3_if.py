# Task:
# Code a program which asks this riddle:
# "What walks on four legs in the morning, 
# two legs in the afternoon, three legs in the evening, 
# and no legs at night?"

# Before the program asks for user input it should print this:
# "Give your answer in all lower case."

# if the user types: "human"
# the program will say: "you are correct!"
# however if the user types something different, 
# the program will say: "you are incorrect"

# riddle = ("What walks on four legs in the morning, two legs in the afternoon, three legs in the evening, and no legs at night?\n")
# answer = ("human") -

# print("Give your answer in all lowercase")
# input(riddle) - 
# if input == answer: -
#     print("You're correct!")
# elif input != answer: -
#     print("You're incorrect")

print("What walks on four legs in the morning, two legs in the afternoon, three legs in the evening, and no legs at night?")
user_answer = input()

if user_answer == "human":
    print("You are correct!")
elif user_answer != "human":
    print("You are wrong")