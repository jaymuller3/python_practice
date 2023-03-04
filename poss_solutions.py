# py_prac_1
# P1: Calculate 5% sales tax on item costing $9.99

# P2: Find maximum value that a 32-bit number can have
# Hint: the starting value of a binary number is zero

# P3: Find the remainder of 23 divided by 7

# py_prac_2
# P1: Create a list of 5 colors

# P2: Create a deep copy of list

# P3: Append a color to the original list

# P4: Remove a color from the copied list

# P5: Print both lists to show that copied list is a deep copy

# P6: Print a slice of original list from the second to fourth items

# P7: Print the length of the original list


# py_prac_3
# P1: Create a list of 10 colors and iterate through the list, printing
#     each item using a for loop

# P2
#   A: Create a while loop using a boolean flag that iterates through
#      the colors list and stops when chosen color within the list is found

#   B: Iterate through the list again using a color not in the list
#      and notify the user that the color does not exist in the list

# P3
#   A: Create two lists, the first a list of 10 colors.  The second,
#      a list of 3 favorite colors, two of which are in the original 
#      list of colors, and one that is not.
#
#   B: Iterate through both lists to determine which favorite colors
#      appear in the colors list, and print both the color name and
#      the position in which the color appears.



# py_prac_4
# P1
hosts = {
    "mythical morning" : ["rhett", "link"],
    "try guys" : ["eugene", "keith", "zach"],
    "cortex" : ["cgp grey", "myke"]
}

for show, host in hosts.items():
    print(show.title() + ":")
    print("---------")
    for i in host:
        print("    " + i.title())