# Part 3 of Week 06 Lab
# Author: Gillian Kane-McLoughlin

students = []

def readModules():
    return []

def doAdd(students):
    newStudent = {}
    newStudent["Name"] = input("Enter Name: ")
    newStudent["Modules"] = readModules()

    students.append(newStudent)

# test
doAdd(students)

print (students)