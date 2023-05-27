
# a program where there is a loop which inserts what the user 
# types into a list and when the user presses done, it ends the 
# loop and prints the list

# clue files:
# - guessing.py for while loops
# - furtherlists.py for adding, printing and making lists

# 1) establish a logic
# i.e:
#       a) make a list
#       b) ask the question / get an input
#       c) add it into the list
#       d) keep on asking the asking the question


banana = []
apple = input("") # apple

while apple != "done": 
    banana.append(apple)
    apple = input("") # apple

for item in banana:
    print(item)









