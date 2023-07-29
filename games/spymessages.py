
# english alphabet

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_to_encrypt = input("Please enter a message to encrypt:\n")

# turns all the letters in the variable to upper case
string_to_encrypt = string_to_encrypt.upper()

shift_amount = int(input("Please enter a whole number from 1-25 to be your shift key. "))

encrypted_string = ""

for letter in string_to_encrypt:
    position = alphabet.find(letter)
    new_position = position + shift_amount
    if letter in alphabet:
        encrypted_string = encrypted_string + alphabet[new_position]
    else:
        encrypted_string = encrypted_string + letter

    print("Your encrypted message is", encrypted_string)


# first get the position of the letter in the alphabet
    # using .find(letter)

    # make a new_position value which is the 
    # sum of the shift_amount and the found position amount

    # for now, print the letter in the alphabet with the new_position 
    # using your knowledge that strings are technically lists