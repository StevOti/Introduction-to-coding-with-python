# Conditional statements
# Signs

# < - less than
# <= - less than or equal to
# > - greater than
# >= - greater than or equal to
# == - equality
# != - not equal to

# Examples of conditional statements

# Compare values which are integers input by the user
x = int(input("What's x ? "))
y = int(input("What's y ?"))

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")

# To shorten the code above wit #or
x = int(input("What's x ? "))
y = int(input("What's y ?"))

if x < y or x < y:
    print("x is not equal to y!")
else:
    print("x is equal to y!")


# Or

x = int(input("What's x ? "))
y = int(input("What's y ?"))

if x == y:
    print("x is equal to y!")
else:
    print("x is not equal to y!")


# The use of #and
# Example

score = int(input("Score:"))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: c")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Now to make the code shorter

score = int(input("Score:"))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: c")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Parity
# Example

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Or write it using bool
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    # or
    return True if n % 2 == 0 else False
    # or
    return n % 2 == 0
    
main()


#  using keyword match
# Example

name = input("What's your name? ")

# Loops

# While loops = loop that is infinite for example

i = 3
while i != 0:
    print("meow")
    i = i - 1

# or 

i = 0

while i < 3:
    print("meow")
    i += 1


# For loop - we will use lists: for example

for i in range(3):
    print("meow")

# or
for i in [1, 2, 3]:
    print("meow")
# or you can use _ instead of the variable i incase you wont be using it later eg
for _ in range(3):
    print("meow")

# If you want to get input that matches a certain expectation, immediately use while True:
# For example:

while True:
    n = int(input("What's n? "))
    if n > 0 :
        continue
    else:
        break
# or 
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# Write a code that asks the user for an input then prints "meow" number of times the user gave

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main()

# Working with lists

# For example

students = ["Steve", "Daisy", "Eddy"]

print(students[0])
print(students[1])
print(students[3])

# or

students = ["Steve", "Daisy", "Eddy"]

for i in students:
    print(i)

# a property called len will list the length of a list
# eg

students = ["Steve", "Daisy", "Eddy"]

for i in range(len(students)):
    print(students[i])

# If you say  print(i, students[i]) it will print the index of each student before the name
# If you say print(i + 1, students[i]), it will print the number and name of each item in the list starting from one

# Using dictionaries
# Example

students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# or

students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

for student in students:
    print(student, students[student], sep = ", ")


# How to represent many dictionaries in a list in code
# A dictionary is a collection of key value pairs eg name can be a key and age the value making key and value pair
# Example

students = {
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
}

print(student["name"], student["house"], student["patronus"])

# Print a square of length 4

def main():
    square(3)

def square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")

        print()

main()

# or
def main():
    square(4)

def square(size):
    for i in range(size):
        print("#" * size)
main()

# or

def main():
    square(4)

def square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print('#' * width)
main()
