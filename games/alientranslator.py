alien_dictionary = {
    "we":"vorag", 
    "come":"thang", 
    "in":"zon", 
    "peace":"argh", 
    "hello":"kodar", 
    "can":"znak", 
    "i":"az", 
    "borrow":"liftit", 
    "some":"zum", 
    "rocket":"upgoman", 
    "fuel":"kakboom", 
    "please":"selpin", 
    "don't":"baaaaaaaaaaarn", 
    "shoot":"flabil", 
    "welcome":"unkip", 
    "our":"mandig", 
    "new":"brang", 
    "alien":"marangin", 
    "overlords":"bap"
    }


# Extra Challenge
# Add the word: "like" with the alien word: "wefrgf" into 
# the dictionary. 


# Code Logic:

alien_dictionary["like"] = "wefrgf"

english = input("Please enter an English word or phrase to translate: \n")
english = english.lower().split()

alien_words = []
for word in english:
    if(word in alien_dictionary):
        alien_words.append(alien_dictionary[word])
    else: 
        # add english word into alien_words instead
        alien_words.append(word)
    
# .join() joins every item in a list together into 1 string
alien_sentence = " ".join(alien_words)

# prints out: "Translation:", (the actual alien sentence)
print("Translation: \n", alien_sentence)



