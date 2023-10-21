# Task:
# create a dictionary consisting
# of the following data:
# superman: "kryptonite",
# batman: "nothing",
# flash: "cold temperatures",
# aquaman: "needs to touch water every hour",


# then create the following story:

# print dictionary 
# "Superman: Why do you have a record of our weaknesses"
# "Batman: For safety (goes on with a detailed explanation)"
# "Flash: Hey, why do you have no weakness? Let me fix that for you"
# fix batman's value to "parents"
# print dictionary
# "Aquaman: Now that's a weakness"
# "(Batman quietly fumes)"
# delete batman entry in dictionary
# print dictionary
# "Flash: that's cheating"
# "Batman: I will have my vengeance."
# "Batman: [print flash's value], is quite a weakness too"

weaknesses = {
    "superman":"kryptonite",
    "batman":"nothing",
    "flash":"cold temperatures",
    "aquaman":"needs to touch water every hour",
    }


print("Superman: Why do you have a record of our weaknesses")
print("Batman: For safety (goes on with a detailed explanation)")
print("Flash: Hey, why do you have no weakness? Let me fix that for you")
weaknesses["batman"] = "parents"
print(weaknesses)
print("Aquaman: Now that's a weakness")
print("(Batman quietly fumes)")
del weaknesses["batman"]
print(weaknesses)
print("Flash: that's cheating")
print("Batman: I will have my vengeance.")
print("Batman:", weaknesses["flash"], "is quite a weakness too")