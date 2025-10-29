# Modules are libraries that typically have one or more functions or other features built into it
# They normally encourage reusability of code
# How do you load the modules to your own program so that you can use, you use import
# import allows you to import the content of and functions from the module
# Examples:
# a. random
# random.choice iterates between a list of choices/parameters and returns one of the values with equal probability
import random

coin = random.choice(["heads", "tails"])
print(coin)

# from is used to import functions from a module and it allows you to be a little bit specific. eg
from random import choice

coin = choice(["heads", "tails"])
print(coin)

# random.randint(a, b) used to get back an int between a and b inclusive. For example:
import random

number = random.randint(1, 10)
print(number)


# random.shuffle(x) takes in a list of values and then shuffles them. For example
import random

cards = ["jack", "king", "queen"]
random.shuffle(cards)
for card in cards:
    print (card)


# statistics library - all sorts of functions for calculating means, modes, median, and other statistical arithmetics
# for example:
import statistics

print(statistics.mean([100, 90]))

# command-line arguments - allow you to provide arguments that is input to the program just when executing it in the command-line
# Example:
# sys
# eg. sys.argv: describing the list of all the words the human typed in at the prompt before they hit enter. argv(argument vector)
# before hitting enter you enter the required type of words
import sys

print("hello, my name is", sys.argv[1])

# we used [1] in sys.argv[1] because index 0 has the name of the program
# To handle the index error in the code above(the error that occurs when a user doesnt enter any word and just clicks enter)

import sys

try:
    print("hello, my name is", sys.argv[1])
except:
    print("Two few arguments")

# or

import sys

if len(sys.argv) < 2:
    print("Two few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# To refine the code above and check for errors
# sys.exit to exit the execution of the program

import sys

if len(sys.argv) < 2:
    sys.exit("Two few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
print("hello, my name is", sys.argv[1])

# Slicing - through multiple words
# If the user is requested to type multiple words in the cmd line and you want the program to access specific words
# in the user's response we do as follows:
# To specify the word to print we use [1:] to start from the value at index 1 to last
# If you use [1:-1], it will eliminates the last digit from the list

import sys

if len(sys.argv) < 2:
    sys.exit("Two few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
    
    


# Packages- there are a lot of third party libraries called packages
# PYPI python programming index-pypi.org
# Example: cowsay- package in python that allows a cow say something on your screen
# pip is a program that comes with python that allows you to download/install the files through the command-line
# To download cowsay, type on the command-line "pip install cowsay"
# To use the package

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello " + sys.argv[1])

# you can also use trex instead of cow to make a trex on the cmd
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello " + sys.argv[1])


# creating your own python packages/module
# You can store it in your locally in your pc or cloud or make it an open source for others to use
# For example

# hello.py

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# execute.py

import sys
# from hello.py import hello
# uncomment the above line of code

if len(sys.argv) == 2:
    hello(sys.argv[1])

# The above code imports main funtion from hello.py and uses it in the execute.py file

# To use __name__ - a special variable whose value is automatically set by python to be "main" 
# when you run a file from the cmd line

# hello.py

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()

# execute.py
import sys
# from hello.py import hello
# uncomment the above line of code

if len(sys.argv) == 2:
    hello(sys.argv[1])
