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


# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() with the following specifications:

# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000.




