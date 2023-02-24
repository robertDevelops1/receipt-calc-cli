from AssignmentManager import AssignmentManager
from CLIHelper import *
from ItemManager import ItemManager
from User import User


def main():
    userManager = UserManager()
    itemManager = ItemManager()
    assignmentManager = AssignmentManager()
    userId = 0
    itemId = 0
    printProgramGreeting()
    userInput = input("Enter a command:\n")
    while(userInput != "q"):
        print("\n")
        if userInput == "1":
            printUsers(userManager)
        elif userInput == "2":
            printItems(itemManager)
        elif userInput == "3":
            printAssignments(assignmentManager)
        elif userInput == "4":
            userInput = input("Enter a name:\n")
            newUser = User(userId,userInput)
            userManager.addUser(newUser)
            userId += 1
        elif userInput == "h":
            printHelp()
        userInput = input("\nEnter a command:\n")
    print("Goodbye!")
    quit()


if __name__ == "__main__":
    main()