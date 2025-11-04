# These are extra learning points in python
# Among other data types, a set is also one of them
# Set - this is a collection of values where there are no duplicates
# To demonstrate this, we create a file called houses.py
students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# Here we used sorted the houses properly without repeating the duplicates
# We could use more that's built in python to solve such problems
# We could use a set() where the duplicates are automatically eliminated as seen below

students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)


# Other features include
# global variables =  whereby you put a variable outside all of your functions, perhaps near the top of your file
# To demonstrate this we create a file bank.py
balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()

# If you run the code above we get the error below:
# UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value
# A local variable is one that exists in the context of a function
# Now to demonstrate the use of a global variable, which are outside the context of a function,
balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

# Lets improve our code using oop convention
class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -=n


def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)

if __name__ == "__main__":
    main()

# Constants - variables that once declared cannot be changed
# To demonstrate we create a file meow.py
for i in range(3):
    print("Meow")

# We can declare a constant as below
MEOWS = 3

for i in range(MEOWS):
    print("Meow")

# we can also write the code as below
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

# Type hints
# mypy - is a programme that is popular for checking whether or not your  code is adhereing to your own type hints

def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# when we run the code we get a TypeError because the input returns an int and not str
# We can fix this by adding a type hint to the function that explicitly specifies for meow what type of variable should be passed in
# We just pass this n: int as an argument
def meow(n: int):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# Then we run mypy, this will help us identify the bugs in our code before we/user can actually experience the errors
# Now the corrected code is
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)

# In the scenerio below
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# When we run the code, it prints the meows thrice then None because at the moment the meow function has a side effect,
# it just prints out meow some number of times,
# it doesnt explicitly return a value, as it would, literally when there was the return keyword there
# This shows that by default, when a function does not return a value in python, its implicit return value is None
# print(meows) this is the line printing None
# To correct this using type hints;
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# But when you run mypy meow.py, you still get an error in this line meows: str = meow(number),
# To fix it;
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")



# Another feature of python, called docstrings
# Docstring, when formally documenting a function, you use tripple quotation marks then comment then close with triple closing quotation
# This will help python, if it detects such comments, it will assume its a documentation fpr that function and in the python ecosystem
# there are some tools that you can then use to analyse your code automatically, extract these docstrings and even generate webpages
# or pdfs of documentation for your functions/code without writing from scratch

# For example

def meow(n: int) -> str:
    """
    Meows n times.

    :param n: number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

# Other features of python,
# We want to modify the code to be able to use command line arguments instead of input
# for example the code below
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("Usage: meows.py")

# if you run python meow.py -n 3, it will print meow three times,
# if you run python meow.py -n 2, it will print meow two times,

# What if we want to support not only -n but a couple of other cmd line arguments,
# we can use a tool called argparse - handles/allows user to pass in configurations options at the command line
# For example:
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")

# If i run python meow.py, it will bring an error but if you run python meow.py -n 3 it will work.
# We can provide documentation on how to use our program in this scenerio by doing the following
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")

# This will produce the a documentation on how to use the program or how it runs
# We can further refine the code by; we specified on our code that if the user does not enter a value then the code will
# just print one meow(default=1) and (type=int) will make sure the value is converted to an int automatically
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()


for _ in range(args.n):
    print("meow")


# Another feature of python,
# Unpacking = unpacking a single value that comes back from a list or a data structure,
# and putting it immediately into two variables.
# file is unpack.py
first, _ = input("What's your name? ").split(" ")
print("hello, {first}")

# Other ways to unpack,
# For example
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")

# Lets unpack the coins list into multiple variables

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")

# Lets unpack the coins in a dictionary
# for example the code below
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons":100, "sickles":50, "knuts":25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# Unpacking will be: we pass ** unline * in lists
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons":100, "sickles":50, "knuts":25}

print(total(**coins), "Knuts")


# Other features in python

# *args, **kwargs = the single and double asterisk is also used as a visual indicator in python when a function itself might take
# variable number of arguments.
# *args= when passed as an argument in a function shows that the function takes a variable number of positional arguments(args from left to right)
# **kwargs = function takes a number of key-word arguments(named-parameters) that can be called optionally and individually by name
# for example:
def f(*args, **kwargs):
    print("Positional: ", args)


f(100, 50, 25)

# But if we increase the arguments from three to four by adding a new number, 5, it will still work,
def f(*args, **kwargs):
    print("Positional: ", args)


f(100, 50, 25, 5)

# We can also print the named args

def f(*args, **kwargs):
    print("Named: ", kwargs)


f(galleons=100, sickles=50, knuts=25)


# Other features in python:
# map = to demostrate this we use the example below
# yell.py
def main():
    yell("This is cs50")

def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__":
    main()

# lets modify the function yell to take a list of words by upacking the list and making the uppercased
def main():
    yell(["This", "is", "cs50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

# we can now modify the code further by using the new conventions of unpacking we learnt, we remove the [] in the main function,
#  and add *words in place of words in the yell function
def main():
    yell("This", "is", "cs50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

# map = function is to apply some function to every element of some sequence.
# Back to our example: yell.py to demonstrate the map function to make the list of parameters uppercased
def main():
    yell("This", "is", "cs50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()

# Another feature of python:
# list comprehensions = refers to the ability in python for you to very easily construct a list on the fly
# without using a loop, without calling append
# Lets demonstrate this by adding this line of code [words.upper() for word in words] to our code example
def main():
    yell("This", "is", "cs50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()


# To demonstrate further, we will create a file called gryffindors.py, we want to filter out the griffindor students
students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

# Filter function can be used to do the same,
# Lets demonstrate
students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

def is_griffindor(s):
    if s["house"] == "Gryffindor":
        return True
    else:
        return False
    
# Then we refined the code to reduce the amount of lines

students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

def is_griffindor(s):
    return s["house"] == "Gryffindor"
        

# so now we can use the filter function
# filter expects a function that returns a true or false

students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

def is_griffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_griffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])


# To sort the students by their names we update as follows:
students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

def is_griffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_griffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

# we can refine the code further to reduce lines of code by:
students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"}
]

gryffindors = filter(lambda s:s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

# Another python feature is:
# dictionary comprehensions = enables us to be able to create a dictionary on the fly without having to create
# dictionary, or a for loop, iterating through the lists and inserting more keys and values to the dictionary, we can do it all at once
# We will use our file gryffindors.py and update it with new code as follow:
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name":student, "house": "Gryffindor"})

print(gryffindors)

# We can also do as follows

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name":student, "house": "Gryffindor"} for student in students]

print(gryffindors)

# If we want to produce a bigger dictionary instead of a list containing dictionaries,
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student:"Gryffindor" for student in students}

print(gryffindors)


# Another feature:
# enumerate = allows you to number a list by iterating over a sequence, by finding both the value one at a time and the index thereof
# for example:
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


# we can modify the code above to demonstrate the enumarate function as follows
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

# Final feature
# generators: 
# to demonstrate lets create a new file sleep.py
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in  range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()

# If you run the code and enter a big number eg a million, the program will hang, because we ran out of memory
# so to fix this we can use generators function
# generators = it can generate a massive amount of data for users, but you can return just a little bit of that data at a time.
# And you yourself can implent the code in almost the same way, but you dont have to worry about too much data getting returned all at once
# This all boils down to keyword yield = allows you to return one value at time from the loop
# To fix this, we can

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
