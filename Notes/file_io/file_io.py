# The concept of file i/o is all about writing code that can read from a file, that is load infomation from,
# or write to, or save info to files
# Using lists we can save data

# For example

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")

# We want to save the names entered by the user to a file... we do the following
# open - function that opens a file programmatically so that the programmer can read info from it and write info to it

name = input("What's your name? ")

file = open("names.txt", "w") # open function will open a file called names.txt and the w will enable the use to write
file.write(name) # This will now write on the file created in the previous line of code
file.close() # This will close the file after writing is complete

# This program deletes the old file and recreates a new file with new content in it.
# To change this,
# append means add to the bottom name on the list.

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()

# To make the names have spaces and pile up horizontally
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# Instead of calling the "file.close()" function, we can use with, to close the file just to make sure nothing goes wrong with the file
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Now to write code that can read the file,
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())

# To remove the new lines created by the print function we use line.rstrip()

# To refine the code and make it shorter,
with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())

# To sort the list of names saved, we:
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):   # to sort in reverse order we use sorted(names, reverse=True)
    print(f"hello, {name}")

# We can also make the above code shorter by:

with open("names.txt") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip())

# We can use csv files(comma seperated values) to store multiple pieces of information that are related in the same file
# When using ms excel, google spreadsheet, we can use such csv files
# For example:
# We create a new csv file with the data below
# students.csv 
# Hermione, Gryffindor
# Harry, Gryffindor
# Don, Gryffindor
# Draco, Slytherin
# and students.py
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# The split(",") will return the individual parts, to the left and to the right, in each line of code
# The above code now reads and formats a csv file
# To refine the code above, 
# to assign automatically two variables, that is name and house instead of only row

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# In order to sort out the list of output

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


# It will be better to sort out our list by the students name and not by the string statement
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student ["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

# or shorten the code,

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

# Now in order to sort the lists of the dictionaries, we can define a new function get_name as below and introduce a key whose value 
# is whatever the return value of get_name is
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

def get_name(student):
    return student ["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


# To sort by house,
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

def get_house(student):
    return student ["house"]


for student in sorted(students, key=get_house): # and to reverse the order we just add reverse = True.
    print(f"{student['name']} is in {student['house']}")


# you're defining something, be it a variable or a function, and immediately using it, 
# but never want again to use it further, we can use a lambda function - a function with no name.
# lamdba is used to call functions which might not be needed again

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


# In this new case, 
# students.csv
# Harry,"Number Four, Privet Drive"
# Ron,The Burrow
# Draco,Malfoy Manor

# students.py
students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name" : name, "home" : home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# When you run the above code you will get a value error because of the csv file, the first line has three values seperated in commas.
# To fix this error, we;
# csv module - is used to manipulate the data in csv files. csv module has a fucntion called reader used to read csv files

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name" : name, "home" : home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# If the column names are already present in the csv file, we use
# csv DictReader - which iterates over the file, top to bottom, loading in each line of text not as a list fo column,
# but as a dictionary of column

# students.csv
# name,home
# Harry,"Number Four, Privet Drive"
# Ron,The Burrow
# Draco,Malfoy Manor

# students.py
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name" : row["name"], "home" : row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# To write on csv files
# students.py
import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# or we can use csv DictWriter which is a dictionary writer,

import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name" : name, "home" : home})

# Other files used to store data in python are binary files
# Binary file - is a file that really just 0s and 1s, and they can be laid out in any pattern you want
# particularly if you want to store graphical or audio or video info, not textual info
# Pillow library - allows you to navigate image files and perform operations on image files
# Lets create gif files costume2.gif and costume1.gif
# Then create costumes.py

# costumes.py

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)