from AssignmentManager import AssignmentManager
from CLIHelper import *
from Item import Item
from ItemManager import ItemManager
from ItemCostManager import ItemCostManager
from User import User


def addUser(userId, userManager:UserManager):
    userName = input("Enter the user's name:\n")
    newUser = User(userId,userName)
    userManager.addUser(newUser)

def addItem(itemId, itemManager:ItemManager):
    itemName = input("Enter the item name:\n")
    storeName = input("Enter the store name:\n")
    validInput = False
    while(not validInput):
        itemCost = input("Enter the item cost:\n")
        try:
            try:
                price = float(itemCost)            
                floatSplit = itemCost.rsplit('.')
                if ((len(floatSplit[-1]) <= 2)) :
                    price = round(float(itemCost),2)
                    validInput = True
                else:
                    print("Please enter a price up to 2 decimal points.")
            except:
                if itemCost == "q":
                    validInput2 = False
                    while(not validInput2):
                        userInput = input("Cancel add item? (Y/N)\n").lower()
                        if userInput == "y":
                            return
                        elif userInput == "n":
                            validInput2 = True
                print("Please enter a numeric value.")
        except:
            print("Try again.")
    validInput = False
    while(not validInput):
        itemTax = input("Enter item tax %:\n")
        try:
            tax = float(itemTax)
            if ((tax >= 0) and (tax <= 100)):
                validInput = True
            else:
                print("Please enter a tax value between 0-100.")
        except:
            if itemTax == "q":
                validInput2 = False
                while(not validInput2):
                    userInput = input("Cancel add item? (Y/N)\n").lower()
                    if userInput == "y":
                        return
                    elif userInput == "n":
                        validInput2 = True
            print("Please enter a numeric value.")
    newItem = Item(itemId,itemName,storeName,price,tax)
    itemManager.addItem(newItem)

def addAssignment(assignmentManager:AssignmentManager, userManager:UserManager, itemManager:ItemManager, itemCostManager:ItemCostManager):
    validInput = False
    while (not validInput):
        userId = int(input("Enter the User ID:\n"))
        if userManager.hasUser(userId):
            validInput = True
        else:
            print("Please enter a valid User ID")
    validInput = False
    while (not validInput):
        itemId = int(input("Enter the Item ID:\n"))
        if itemManager.hasItem(itemId):
            validInput = True
        else:
            print("Please enter a valid Item ID")
    assignmentCode = "u{0}i{1}".format(userId,itemId)
    if assignmentManager.hasAssignment(assignmentCode):
        print("Assignment already exists!")
    else:
        user = userManager.getUser(userId)
        item = itemManager.getItem(itemId)
        assignmentManager.addAssignment(user,item)
        itemCostManager.addItem(item)

def main():
    userManager = UserManager()
    itemManager = ItemManager()
    itemCostManager = ItemCostManager()
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
            printAssignments(userManager,assignmentManager)

        elif userInput == "4":
            addUser(userId, userManager)
            userId += 1

        elif userInput == "5":
            addItem(itemId, itemManager)
            itemId += 1

        elif userInput == "6":
            addAssignment(assignmentManager, userManager, itemManager, itemCostManager)
        elif userInput == "h":
            printHelp()

        userInput = input("\nEnter a command:\n")
    print("\nGoodbye!")
    quit()


if __name__ == "__main__":
    main()