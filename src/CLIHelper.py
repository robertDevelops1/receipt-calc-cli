
from AssignmentManager import AssignmentManager
from ItemManager import ItemManager
from UserManager import UserManager


def printProgramGreeting():
    title = """
            ██████╗ ███████╗ ██████╗███████╗██╗██████╗ ████████╗     ██████╗ █████╗ ██╗      ██████╗    ██╗   ██╗ ██╗    ██████╗  ██████╗ 
            ██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██║     ██╔════╝    ██║   ██║███║   ██╔═████╗██╔═████╗
            ██████╔╝█████╗  ██║     █████╗  ██║██████╔╝   ██║       ██║     ███████║██║     ██║         ██║   ██║╚██║   ██║██╔██║██║██╔██║
            ██╔══██╗██╔══╝  ██║     ██╔══╝  ██║██╔═══╝    ██║       ██║     ██╔══██║██║     ██║         ╚██╗ ██╔╝ ██║   ████╔╝██║████╔╝██║
            ██║  ██║███████╗╚██████╗███████╗██║██║        ██║       ╚██████╗██║  ██║███████╗╚██████╗     ╚████╔╝  ██║██╗╚██████╔╝╚██████╔╝
            ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝╚═╝        ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝      ╚═══╝   ╚═╝╚═╝ ╚═════╝  ╚═════╝                                                                                             
            \n"""
    print(title)
    printHelp()

def printHelp():
    """    
    1) - view all users
    2) - view all items
    3) - view all assignments
    4) - add user
    5) - add item
    6) - assign item to user
    0) - view everything
    h) - help
    q) - close program
    """        
    string = "Available Commands\n" + "1) - view all users\n" + "2) - view all items\n" + "3) - view all assignments\n" + "4) - add user\n" + "5) - add item\n" + "6) - assign item to user\n" + "0) - view everything\n" + "h) - help\n" + "q) - quit program\n"
    print(string)

def printUsers(manager:UserManager):
    users = manager.getUsers()
    if len(users) == 0:
        print("No users registered!")
    else:
        for user in users.values():
            print(user)
            print("\n")

def printItems(manager:ItemManager):
    items = manager.getItems()
    if len(items) == 0:
        print("No items registered!")
    else:
        for user in items.values():
            print(user)
            print("\n")

def printAssignments(manager:AssignmentManager):
    assignments = manager.getAssignments()
    if len(assignments) == 0:
        print("No assignments registered!")
    else:
        for user in assignments.values():
            print(user)
            print("\n")

def printSummary():
    pass