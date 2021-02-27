# Part 2 of Week 06 Lab
# Author: Gillian Kane-McLoughlin

def displayMenu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View student records")
    print ("\t(q) Quit")
    choice = input("Type the corresponding letter (a/v/q): ").strip()

    return choice

def doView():
    print ("Viewing student records")

def doAdd():
    print ("Adding a new student")

choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print ("\nPlease enter a valid option")
    choice = displayMenu()

print ("Quit")