# Python Practice 2: 
#   Strings, Lists


# Strings
word = "kitty"

# All Caps
word = word.upper()
print(word)

# All lowercase
word = word.lower()
print(word)

# Title-case
phrase = "kitties are great"
print(phrase.title())

# Strings with Math Operators
# Plus-sign concatenates
word1 = "kitties"
word2 = "are"
word3 = "wonderful"
print(word1 + " " + word2 + " " + word3 + "!")

# Multiplication-sign multiplies the number of times the string appears
multiplier = 3
phrase1 = word.title() * multiplier
print(phrase1)


# Lists
# Initalizing a list
animals = ["penguins", "kitties", "puppers"]
print(animals)

# Accessing items in list
# Prints first item in list
# Note: Lists always start at value zero
print(animals[0])

# Prints last item in list
print(animals[-1])

# "Slicing" Lists
# Prints first 2 items in list
# Note: Always add 1 to the value you want to end on
# e.g. First 10 items in the list would be animals[:10] - 0 through 9+1
print(animals[:2])

# Prints starting from the second item and prints until end of the list
print(animals[1:])

# Finding the length of a list
print(len(animals))

# Appending items to the end of the list
animals.append("duckers")
print(animals)

# Insert items into the middle of the list
animals.insert(2, "sheepsies")
print(animals)

# Making a "deep" copy of a list
animalsCopy = animals[:]
print("Printing original list: ", animals)
print("Printing copied list: ", animalsCopy)

# Removing items from the list using location
del animals[1]
print(animals)

animals.pop(-1)
print(animals)

# Removing items from the list using value
animals.remove("sheepsies")
print(animals)

# Showing original vs. copied lists
print("Printing original list: ", animals)
print("Printing copied list: ", animalsCopy)
print()

# Shallow vs. Deep Copies
animalsShallow = animals
print("Printing original list: ", animals)
print("Printing deep copied list: ", animalsCopy)
print("Printing shallow copied list: ", animalsShallow)
print()

# Modifying value of item in list by location
animalsShallow[1] = "duckers"
print("Printing original list: ", animals)
print("Printing deep copied list: ", animalsCopy)
print("Printing shallow copied list: ", animalsShallow)