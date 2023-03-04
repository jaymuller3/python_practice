# Python Practice 4: 
#   Dictionaries


# Dictionaries
animalDict = {"penguins": "cute", "kitties": "warm", "puppers": "sweet"}
print(animalDict)
print("According to the animal dictionary, penguins are: " \
      + "\"" + animalDict["penguins"] + "\"!")
# Sidenote: in the string above, note the escape character \" 
# to add quotes to the string

# Adding a key-value pair to a dictionary
animalDict["sheepsies"] = "kind"
animalDict["duckers"] = "evil"
animalDict["porgs"] = "freaky"
print(animalDict)

# Modifying key-value pair in a dictionary
animalDict["duckers"] = "wahwahwahwahwah"

# Note that dictionaries are not sorted in alphabetical order by default

# Deleting key-value pair from dictionary
del animalDict["porgs"]
print(animalDict)

# Iterating through a dictionary
print()
print("Animal name - Trait ")
print("--------------------")
for animal, trait in animalDict.items():
    print(animal + " - " + trait)


# Using conditional to confirm data is stored within dictionary
# Example 1 - item is found within the dictionary
word = "penguins"

if word in animalDict:
    print(word.title() + " are " + animalDict[word] + "!") 
else:
    print("Sorry this word does not exist within this dictionary.")

# Example 2 - item is not found within the dictionary
word = "porgs"

if word in animalDict:
    print(word.title() + " are " + animalDict[word] + "!") 
else:
    print("Sorry this word does not exist within this dictionary.")

# Example 3 - item is confirmed not to be in the dictionary
if word not in animalDict:
    print("Confirmation that this word does not exist within "
          "this dictionary.") 
else:
    print("Despite their freakiness, " + word + " are in this dictionary.")


# P2
#   A: Create a dictionary using the name of podcasts as the key, and
#      a list of the hosts of the podcast as the value
#  
#   B: Print the key-value pairs, but with the key as the heading, and
#      each host as an individual printed separately, using title-case
#      for the name of both the podcast and each host