# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and prints their values.

def person_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Your name is {name}, and you are {age} years old.")

person_info()

# Solution
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)


# Exercise 2: Create a function with variable length of arguments
# Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.

# Note: Create this function so that it can receive any number of arguments, process them, and display the value of each individual argument.

# Function call:
# call function with 3 arguments
# func1(20, 40, 60)
# call function with 2 arguments
# func1(80, 100)
# Expected Output:
# Printing values
# 20
# 40
# 60

# Printing values
# 80
# 100

# Solution

# To accept a variable number of positional arguments, allowing functions to take any quantity of these arguments, we use *args as a parameter. 
# (This involves prefixing a parameter name with an asterisk: *).
# Using *args, you can pass any number of positional arguments to the function. Internally, all these passed values are collected and represented as a tuple.

def func1(*args):
    for arg in args:
        print(arg)

# Example calls to the function with different numbers of arguments
func1(10, 20)
func1("hello", 3.14, True)
func1(1, 2, 3, 4, 5)
func1() # Calling with no arguments



# Exercise 3: Return multiple values from a function
# Write a function calculation() that accepts two variables and calculates both their addition and subtraction. 
# The function should then return both the sum and the difference in a single return statement.

# Given:

# def calculation(a, b):
    # Your Code

# res = calculation(40, 10)
# print(res)
# Expected Output

# 50, 30

def calculation(a, b):
    sum = a + b
    difference = a + b
    print(sum, difference)

result = calculation(20, 40)
print(result)


# Reverse each word of a string
# Given:
# str = 'My Name is Jessa'
# Expected Output:
# yM emaN si asseJ

# Exercise to reverse each word  of a string
def reverse_words(Sentence):
    # Split string on whitespace
    words = Sentence.split(" ")

    # iterate list and reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]
    
    # Joining the new list of words
    res_str = " ".join(new_word_list)
    return res_str

# Given String
str1 = "My Name is Jessa"
print(reverse_words(str1))


# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() with the following specifications:

# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000.


# Exercise 2: Read text file into a variable and replace all newlines with space
# Given: Assume you have a following text file (sample.txt).
# Line1
# line2
# line3
# line4
# line5
# Expected Output:
# Line1 line2 line3 line4 line5


with open('sample.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    print(data)

# Write a program to enter the names and times 
# in seconds of runners participating in 100m race 
# heats. The program should prompt for a name, 
# then prompt for their time, e.g.
# Enter time in seconds for King, R: 
# The end of data is signalled by entering xxx for 
# the runner’s name. 
# Print the average time, in seconds, of all 
# the runners.

def main():
    
    sum = get_sum()
    number_of_athletes = get_number_of_runners()

    average = sum / number_of_athletes
    print("The average time is: ", round(average))

def get_sum():
    runner1 = input("Enter runner\'s name: ")
    time1 = int(input(f"Enter time in seconds for {runner1}: "))
    runner2 = input("Enter runner\'s name: ")
    time2 = int(input(f"Enter time in seconds for {runner2}: "))

    sum = int(time1) + int(time2)
    return sum

def get_number_of_runners():
    number_of_runners = int(input("Enter number of runners: "))
    return number_of_runners

if __name__ == "__main__":
    main()






# Load Challenge 66 Tiles required to cover given area incomplete from the Starred challenges (incomplete) folder. 
# The program asks the user to enter the size in m² of an area that needs tiling. The user then selects the size of tiles they want from 
# a range of sizes given in cm. The program tells them how many tiles they will need. (Ten percent is added to the calculated 
# number to allow for tiles that need to be cut, and this number is rounded down to the nearest whole number.)
# Copy and complete the program and save it in your own folder.Test your completed program by entering 
# 20 cm for tile length, 12 cm for tile width and 2.4 m² for area to be covered. The 
# integer number of tiles required, including the 10% extra), is 110.

# Solution
# prgram asks for the size in m²
# allows user to select tile size from a range of sizes in cm
# program tells user how many tiles they will need
# Ten percent(rounded off to the nearest whole number) is added to the result


def main():
    tiled_area = get_tiled_area()
    tile_area = get_tile_area()
    
    number_of_tiles = float(tiled_area) / float(tile_area)
    incomplete_tiles = number_of_tiles * 0.1
    total_tiles = number_of_tiles + incomplete_tiles

    print(round(total_tiles))

def get_tiled_area():
    tiled_area = float(input("Enter total area to be tiled in m²: "))
    return tiled_area


def get_tile_area():
    length = float(input("Enter length in cm: "))
    width = float(input("Enter width in cm: "))
    new_length = length * 0.01
    new_width = width * 0.01
    
    tile_area = new_length * new_width

    return tile_area


if __name__ == "__main__":
    main()


# The program asks the user to enter a number 
# between 1 and 10. If the number is not in this 
# range, keep printing a warning message and 
# asking the user to re-enter the number. Then 
# keep doubling this number until the result is 
# 100,000 or more. Print the final result and the 
# number of times the number was doubled.

def double_number():
    # Ask the user to enter a number between 1 and 10
    while True:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if 1 <= number <= 10:
                break  # valid input
            else:
                print("Number out of range! Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")

    # Keep doubling the number until it reaches or exceeds 100,000
    count = 0
    while number < 100000:
        number *= 2
        count += 1


    # Print the final result
    print(f"\nFinal result: {number}")
    print(f"Number of times doubled: {count}")

double_number()

# Amend the program Challenge 68 
# Double a number repeatedly completed
# so that the user can enter the final 
# target. Include validation to ensure 
# the target entered by the user is 
# between 20 and 100,000. Also 
# include a print statement so that 
# the number, and number of times 
# doubled, is printed each time it 
# is doubled.

def double_number():
    # Ask the user to enter a number between 1 and 10
    while True:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if 1 <= number <= 10:
                break  # valid input
            else:
                print("Number out of range! Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")

    # Keep doubling the number until it reaches or exceeds 100,000
    
    while True:
        target = int(input("Enter a number between 20 and 100000: "))
        if target > 20 and  target < 100000:
            break
        else:
            int(input("Enter a number between 20 and 100000: "))


    count = 0
    while number < target:
        number *= 2
        count += 1
        print(f"The number: {number} and the number of times doubled: {count}")
    
    
double_number()

# Write a program to initialise the list of planets: 
# planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]
# Use the list.append() method to append Uranus and Neptune to the end of list.
# Print the list in the format:
# ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]

planet.append("Uranus")
planet.append("Neptune")
print(planet)



# Write a program to initialise the list:
# ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
# Use a list method to insert "Earth" between "Venus" and "Mars".
# Print the amended list.

planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]

planets.insert(2, "Earth")
print(planets)

# Write a program to initialise and print the list of planets: 
# planet = ["Mercury", "Venus", "Earth", "Mars", 
# "Jupiter", "Saturn"]
# Then print the list with each planet on a separate line starting 
# with Saturn, and ending with Mercury

planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]

n = len(planet)

for i in range(n):
    print(planet[i])


# The program below generates 20 random floating point numbers between 0 and 1. Using these 
# numbers, random numbers between 0 and 200, and between 50 and 250 are generated. The three 
# sets of numbers are printed in neat columns.
#Program name: Level 6 Example 7 Formatting printed columns
import random

for index in range (20):
    num1 = random.random() #returns a random number between 0 and 1
    num2 = num1 * 200		#returns a random number between 0 and 200
    num3 = num1 * 200 + 50 #returns a random number between 50 and 250
#print num1 to 4 decimal places,
#num2 to 2 decimal places, num3 to 1 decimal place
#each number occupies 20 spaces and is right aligned
print("{:>20.4f}{:>20.2f}{:>20.1f}".format(num1,num2,num3))

# Write a program that allows a user to enter two numbers area1 and area2, e.g. 2.347 and 1, 
# representing average daily rainfall in two different areas. Print a heading, and print the numbers with 
# two decimal places on one line, each in a 10-character space. 
# Enter average daily rainfall for area 1: 2.347
# c: 1
#  Area1 Area2
#  2.35 1.00

region1 = "Area1"
region2 = "Area2"
area1 = float(input("Enter average daily rainfall for area 1: "))
area2 = float(input("Enter average daily rainfall for area 2: "))

print(f"{region1:>10}{region2:>10}")
print(f"{area1:>10.2f}{area2:>10.2f}")


#Program name: Level 9 Example 2 Bubble sort (fish)
fish = ["parrotfish", "grouper", "boxfish", "damselfish", "snapper", "ray"]
#get number of items in the list
numItems = len(fish)
passNumber = numItems - 1
swapMade = True
while passNumber > 0 and swapMade:
    swapMade = False
    for j in range(passNumber):
        if fish[j] > fish[j + 1]:
            temp = fish[j]
            fish[j] = fish[j + 1]
            fish[j + 1] = temp
            swapMade = True
    passNumber = passNumber - 1
print("\nSorted list:\n",fish)


# Define a subprogram that will ask the user to pick a low and a high number, and then 
# generate a random number between those two values and store it in a variable called “comp_num”. 
# Define another subprogram that will give the instruction “I am thinking of a number…” and then ask the user to 
# guess the number they are thinking of. 
# Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. 
# If it is, it should display the message “Correct, you win”, otherwise it should
# keep looping, telling the user if they are too low or too high and asking them to guess again until they 
# guess correctly

import random

def get_num():
    high = int(input("Enter a high number: "))
    low = int(input("Enter a low number: "))
    comp_num = random.randint(low, high)
    return comp_num

def guess_num():
    guess = int(input("I am thinking of a number…Guess the number: "))
    return guess

def check_same(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, you win")
            try_again = False
        elif comp_num < guess:
            guess = int(input("Too low. Try again: "))
        else:
            guess = int(input("Too high. Try again: "))

def main():
    numbers = get_num()
    input = guess_num()
    check_same(numbers, input)

main()