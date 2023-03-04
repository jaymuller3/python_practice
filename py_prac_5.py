# Python Practice 5: 
#   Functions, User Input


# Note: User input is stored as a string, 
#       even when the input is a number

def intro():
    print("Welcome to my program")


def printOpt():
    print("What would you like to do?")
    print("1 - Learn about the program")
    print("2 - Run the program")
    print("3 - Exit the program")


def userInputVal(selection):
    options = ["1", "2", "3"]

    while selection not in options:
        print("I'm sorry, that is not a valid selection")
        print("Please selection an option using a number from the menu below")
        printOpt()
        selection = input("Enter your selection here: ")
    
    return selection


def main():
    userNum = 0

    while userNum != "3":
        intro()
        printOpt()
        userNum = input("Enter your selection here: ")
        userInputVal(userNum)
    
    print("Thanks for using the program.\nGoodbye!")


main()