# Python Practice 3: 
#   Conditionals, Loops, Dictionaries


# Initialize some values and lists
word1 = "kitty"
word2 = "porg"
animals = ["penguin", "kitty", "pupper", "sheepsie", "ducker", "stompy"]
num1 = 101

print()

# Contiditionals
# If-statements
if word1 != word2:
    print("A " + word1 + " is better than a " + word2 + ".")

# If-else statements
if word1 == word2:
    print("A " + word1 + " is the same as a " + word2 + ".")
else:
    print("A " + word1 + " is still better than a " + word2 + ".")

# If-elif-else statements
if len(word1) < 5:
    print("The word " + word1 + " has less than 5 letters.")
elif len(word1) < 10:
    print("The word " + word1 + " has more than 4 letters, but less than 10")
else:
    print("The word " + word1 + " has more than 10 letters.")

# Multiple elifs can be used in an if-elif-else statement
if num1 < 10:
    print("This number is less than ten.")
elif num1 < 100:
    print("This number is at least ten but less than one hundred.")
elif num1 < 1000:
    print("This number is at least one hundred, but less than one thousand.")
else:
    print("This number is greater than one thousand.")


# Loops
# While-loops
# While-loop with Counter
counter = 0
subNum = num1
while counter < 10:
    subNum -= 5
    print("Loop " + str(counter + 1) + ":", subNum)

    counter += 1
print("While-loop finished.")

# For-loop
subNum = num1
for i in range(10):
    subNum -= 5
    print("Loop " + str(i + 1) + ":", subNum)
print("For-loop finished.")

# While-loop with Flag








# Dictionaries