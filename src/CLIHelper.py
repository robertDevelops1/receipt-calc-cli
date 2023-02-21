
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

def printUsers():
    pass

def printItems():
    pass

def printAssignments():
    pass

def printSummary():
    pass