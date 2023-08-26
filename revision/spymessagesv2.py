alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

given_string = input("Enter a message to encrypt:\n")

# update the variable with all uppercase letters
given_string = given_string.upper()

# gets the shift amount from user
shift_amount = int(input("Please enter an interger to shift from 1-25:\n"))

final_encryption = ""

for current_character in given_string:
    if(current_character in alphabet):
        # just finding the index of each character in the alphabet
        current_position = alphabet.find(current_character)
        # finding the new character position after shift
        new_position = current_position + shift_amount
        # finding new character with the new character position
        new_character = alphabet[new_position]
    else: 
        new_character = current_character
    # add new character to the final_encryption variable
    final_encryption = final_encryption + new_character

print("Your encrypted message is",final_encryption)
