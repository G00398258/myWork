# Part 4 of Week 06 Lab
# Author: Gillian Kane-McLoughlin

def readModules():
    modules = []
    moduleName = input("\tPlease enter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["Name"] = moduleName
        module["Grade"] = int(input("Please enter the grade received out of 100: "))
        modules.append(module)

        # Next module
        moduleName = input("\t Please enter the next module name (blank to quit): ").strip()

    return modules
