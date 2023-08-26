def sum_list(num_list):
    total = 0
    # logically add every number into the variable total
    for number in num_list:
        total = total + number
    return total

def times_list(num_list):
    total = 1
    for number in num_list:
        total = total * number
    return total

def find_highest_num(num_list):

    i = 0
    highest_num = 0
    while i < 7:
        if highest_num < num_list[i]:
            highest_num = num_list[i]
        i += 1
    return highest_num

def something(num_list):
    total = 0
    for number in num_list:
        total = total + number
    final_total = total + 20 + 15 + 7
    return final_total

def find_lowest_num(num_list):
    min = num_list[0]
    for i in num_list:
        if i < min:
            min = i
    return min

def find_second_num_list(num_list):
    i = 0
    second_num_list = []
    while i < 7:
        if i % 2 == 1:
            second_num_list.append(num_list[i])
        i = i + 1
    return second_num_list

def find_third_num_list(num_list):
    i = 0
    third_num_list = []
    while i < 7:
        if i % 3 == 2:
            third_num_list.append(num_list[i])
        i = i + 1
    return third_num_list

def main():
    # make a list with 7 random numbers
    num_list = [10,12,13,14,15,16,17]

    # function to add all the numbers in list
    total = sum_list(num_list)
    print("The total is:", total)

    # function to multiply all numbers in list
    product = times_list(num_list)
    print("The product is:", product)

    # function to find the highest number in list
    highest_num = find_highest_num(num_list)
    print("The highest number is:", highest_num)

    # fuction to find the lowest number in list
    lowest_num = find_lowest_num(num_list)
    print("The lowest number is:", lowest_num)

     # revision:
    # make a new function where you add all of the numbers in the list
    # with these numbers too: 20, 15, 7
    final_total = something(num_list)
    print("The revision total is", final_total)

    # function to print every 2nd number in the list
    second_num_list = find_second_num_list(num_list)
    print("The 2nd numbers in the list are", second_num_list)

    # fuction to print every 3rd number in the list
    third_num_list = find_third_num_list(num_list)
    print("The 3rd numbers of the list are", third_num_list)

    # 





main() 


