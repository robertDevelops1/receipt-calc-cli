from AssignmentManager import AssignmentManager
from CLIHelper import *
from ItemManager import ItemManager
from ItemCostManager import ItemCostManager
from User import User


def addUser(userId, userManager:UserManager):
    userName = input("Enter the item name:\n")
    newUser = User(userId,userName)
    userManager.addUser(newUser)

def addItem(itemId, itemManager:ItemManager):
    itemName = input("Enter the item name:\n")
    storeName = input("Enter the store name:\n")
    validInput = False
    while(not validInput):
        itemCost = input("Enter the item cost:\n")
        #check if two decimal points
    itemTax = input("Enter item tax %:\n")

def main():
    userManager = UserManager()
    itemManager = ItemCostManager()
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
            addUser(userId, userManager)
            userId += 1

        

        elif userInput == "h":
            printHelp()

        userInput = input("\nEnter a command:\n")
    print("Goodbye!")
    quit()


if __name__ == "__main__":
    main()