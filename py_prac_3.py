# Python Practice 3: 
#   Conditionals, Loops


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
# Note: Loops will continue looping until condition is no longer true.
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
# Example 1
subNum = num1
for i in range(10):
    subNum -= 5
    print("Loop " + str(i + 1) + ":", subNum)
print("For-loop finished.")

# Example 2
# Iterating through a list
print("A list of animals:")
for i in range(len(animals)):
    print("\t" + animals[i])
print("That's all of them!")

# While-loop with Flag
# Example 1
found = False
wordNeeded = "ducker"
i = 0
while found == False or i < len(animals):
    i += 1
    if wordNeeded == animals[i]:
        print("Found "+ wordNeeded + " at position " + str(i + 1) + "!")
        found = True
        break
    else: 
        print("This is not the word that is needed.")
    
    if i >= len(animals):
        print("I'm sorry, the word you need is not in this list.")

# Example 2
found = False
wordNeeded = "porg"
i = 0
while found == False and i < len(animals):
    if wordNeeded == animals[i]:
        print("Found "+ wordNeeded + " at position " + str(i + 1) + "!")
        found = True
        break
    else: 
        print("This is not the word that is needed.")
    
    i += 1

    if i >= len(animals):
        print("I'm sorry, the word you need is not in this list.")