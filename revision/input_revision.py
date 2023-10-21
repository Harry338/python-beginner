



# 1) Create a program, which gets the user input and prints it
user_input = input("Input something\n")
print(user_input)

# 2) Create a list with 5 numbers and print the list itself
num_list = [1,2,3,4,5]
print(num_list)

# 3) Print each item in the list you created above through a loop
for i in num_list:
    print(i)

# 4) Create 2 more lists with 5 items each
#       (one with only strings and the other with just numbers)
num_list_2 = [6,7,8,9,10]
shopping_list = ["apple", "brush", "banana", "pear", "book"]

# 5) Make a program which asks the user, which list they want to print 
#       and print the list they want (with the loop method)

list_input = input("Which list do you want?\n")

if list_input == "num":
    for i in num_list:
        print(i)
elif list_input == "2":
    for i in num_list_2:
        print(i)
elif list_input == "shopping":
    for i in shopping_list:
        print(i)

# 6) Choose a list of numbers you just made and 
#       print the squared value of each item (use a while loop for this)
num = 0

while num < 5:
    squared = num_list[num] ** 2
    print(squared)
    num += 1

# 7) Make 2 lists with 4 numbers in each and print each and print the multiplication of every
#       item combination between the 2 list
#       for eg:
#           a = [1,2,3], b = [4,5,6]
#           1*4, 1*5, 1*6, 2*4, 2*5, 2*6

num_list_a = [11,10,12,13,14]
num_list_b = [15,16,17,18,10]

product = []

for num_a in num_list_a:
    for num_b in num_list_b:
        times = num_a * num_b
        product.append(times)
print(product)

# 8) Print out the common number in the two lists (10)
for num_a in num_list_a:
    for num_b in num_list_b:
        if num_a == num_b:
            print(num_a)


