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




