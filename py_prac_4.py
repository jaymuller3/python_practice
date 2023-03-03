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