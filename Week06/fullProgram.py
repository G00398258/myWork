# Part 5 of Week 06 Lab
# Author: Gillian Kane-McLoughlin

def displayMenu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View student records")
    print ("\t(q) Quit")
    choice = input("Type the corresponding letter (a/v/q): ").strip()

    return choice

def doView():
    print ("Viewing student records:")
    print (students)

def readModules():
    modules = []
    moduleName = input("\tPlease enter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["Name"] = moduleName
        module["Grade"] = int(input("\tPlease enter the grade received out of 100: "))
        modules.append(module)

        # Next module
        moduleName = input("\tPlease enter the next module name (blank to quit): ").strip()

    return modules

def doAdd(students):
    print ("Adding a new student:")
    newStudent = {}
    newStudent["Name"] = input("\tEnter Name: ")
    newStudent["Modules"] = readModules()

    students.append(newStudent)

# Main Program
students = []
choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView()
    elif choice != "q":
        print ("\nPlease enter a valid option")
    choice = displayMenu()

print ("Goodbye")