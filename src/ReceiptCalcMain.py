from CLIHelper import *


def main():
    printProgramGreeting()
    command = input("Enter a command: ")
    while(command != "q"):
        command = input("Enter a command: ")
        pass
    print("Goodbye!")
    quit()


if __name__ == "__main__":
    main()