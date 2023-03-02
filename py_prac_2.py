# Python Practice 2: 
#   Strings, Lists, Conditionals, Loops, Dictionaries


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
animals = ["penguins", "kitties", "puppers"]
print(animals)

# Prints first item in list
# Note: Lists always start at value zero
print(animals[0])

# Prints last item in list
print(animals[-1])

# Finding the length of a list
print(len(animals))

# "Slicing" Lists
# Prints first 2 items in list
# Note: Always add 1 to the value you want to end on
# e.g. First 10 items in the list would be animals[:10] - 0 through 9+1
print(animals[:2])

# Prints starting from the second item and prints until end of the list
print(animals[1:])