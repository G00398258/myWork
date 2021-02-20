# program that stores student name and list of courses in a dict
# Author: Gillian Kane-McLoughlin

student = {
    "Name" : "Mary",
    "modules" : [
        {"Course" : "Programming",
    "Score": 45
    },
    {"Course" : "History",
    "Score" : 99
    } 
    ]
}

print ("Student: {} \nModules: ".format(student["Name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["Course"], module["Score"]))