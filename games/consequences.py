import random

woman = ["A scientist", "A queen", "A pirate", "A giant rabbit"]
man = ["a police officer", "an artist", "your grandfather", "a killer robot"]

place = ["on Pluto.", "at the supermarket.", "in a spooky, bat-filled cave."]
she_wore = ["scuba diving gear.", "fairy wings.", "a paper bag."]
he_wore = ["a purple suit.", "a shark costume.", "a beach towel."]
woman_says = ["'who are you?'", "'How many beans make five?'", "'Why?'"]
man_says = ["'Beep Boop!'", "'Don't eat frogs!'", "'What time do you call this?'"]
consequence = ["world peace.", "chaos.", "a giant foot squashed them.", "rainbows."]
world_says = ["'Errant nonsense!'", "'Cheese is trending now.'", "'I'm melting!'"]

certain_woman = random.choice(woman)
certain_man = random.choice(man)

input("\nPress enter to play\n")

# printing certain woman meeting a certain man at a place
print(random.choice(woman), "met", random.choice(man), random.choice(place))

# print: "She was wearing", a certain female clothing
print(certain_woman, "wore", random.choice(she_wore))

# print: "He was wearing", a certain male clothing
print(certain_man, "wore", random.choice(he_wore))

# print: "She said,", a certain woman dialogue
print(certain_woman, "said", random.choice(woman_says))

# print: "He said,", a certain man dialogue
print(certain_man, "said", random.choice(man_says))

# print: "The consequence was", a certain consequence
print("the consequence was", random.choice(consequence))

# print: "The world said,", a certain world dialogue
print(random.choice(world_says), "the world said,")
