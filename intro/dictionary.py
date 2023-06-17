


# Dictionaries are similar to lists, but require a {key : value} link for each item
# Each key represents the item's name and are usually in anstring or integer format
# While the label / pair of the key can be in any data type
# Data types include:
#    string, integers, booleans, lists, dictionaries

# create dictionary
powers = {
    "The Pigeon":"flight", 
    "Brainzar":"mind reader", 
    "Cyborg":"controls machines"
    }

# print item in dictionary by using its associated key (string)
print(powers["The Pigeon"])

# add item to dictionary
powers["Laser Girl"] = "shoot lasers"

# print entire dictionary
print(powers)

# delete item in dictionary
del powers["The Pigeon"]

# changing the value of an item in dictionary
powers["Brainzar"] = "seeing the future"

