# Lab for Week 06
# Author: Gillian Kane-McLoughlin

def displayMenu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View student records")
    print ("\t(q) Quit")
    choice = input("Type the corresponding letter (a/v/q): ").strip()

    return choice

# Testing displayMenu function
choice = displayMenu()
print ("You chose option", choice)