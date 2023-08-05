
# x = 0
# while x < 10:
#     print(x)
#     x = x + 1

# for loop which counts every number in the range (0,10)
# print for every number 'y' is at 
for y in range(0,10):
    print(y)


# for loops
# while loops

# default for loops
for i in range(0,4):
    print("hello")

for_list = [0,1,2,3]

print(i)
# i = temporary variable which can only be used in the for loop 
# range(0,4) = creates a list of numbers from 0 to a number that is
#              1 less than the 2nd number (4)

shopping_list = ['apple', 'banana', 'crab']
for index in shopping_list:
    print(index)

# nested loops are loops within a loop
# for loops are often in nested loops

first_list = range(0,3)
second_list = range(0,3)

for i in first_list:
    for j in second_list:
        print("1: ", i, "2: ", j)
    
# outside for loop iterates first
# the inside for loop finishes looping / iterating
# then the outside loop continues
