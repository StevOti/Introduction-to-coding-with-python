# integers or int
# signs used in python are as follows:
# + addition
# - subtraction
# * multiplication
# / division
# // floor division (returns the largest integer less than or equal to the division result)
# % modulus (returns the remainder of the division)
# ** exponentiation (raises a number to the power of another number)

# Data types in python
# Python has several built-in data types, including:
# - int: Integer type, used for whole numbers
# - float: Floating-point type, used for decimal numbers
# - str: String type, used for text
# - bool: Boolean type, used for True/False values

# Python supports interactive arithmetic operations/ interactive mode
# You can perform arithmetic operations directly in the Python shell or script.
# For example:
print(2 + 3)  # Addition
print(5 - 2)  # Subtraction
print(4 * 3)  # Multiplication
print(10 / 2)  # Division
print(10 // 3)  # Floor Division
print(10 % 3)  # Modulus
print(2 ** 3)  # Exponentiation



# Example of a simple python mathematical program
# This program takes two numbers as input from the user and performs basic arithmetic operations on them.
# It then prints the results of these operations.
# Take two numbers as input from the user
num1 = float(input("Enter first number: "))  # Convert input to float
num2 = float(input("Enter second number: "))  # Convert input to float

# Perform arithmetic operations
sum = num1 + num2

print("The sum of", num1, "and", num2, "is:", sum)

# or nest the above code in a single line
print("The sum of", num1, "and", num2, "is:", num1 + num2)

# Which version is better?
# The first version is better because it is more readable and easier to understand.


# round() function
# The round() function is used to round a floating-point number to a specified number of decimal places.
# The syntax for the round() function is as follows:
# round(number[, ndigits])... [] this means optional arguments
# where number is the number to be rounded, and ndigits is the number of decimal places to round to (default is 0).
# For example:
num = 3.14159
print(round(num, 2))  # Rounds to 2 decimal places
print(round(num))     # Rounds to nearest integer

# We can also divide big number results with commas for better readability
big_num = 1234567890
print(f"{big_num:,}")  # Outputs: 1,234,567,890

# If you want to specify the number of decimal places in the output, you can use formatted string literals (f-strings) or the format() method.
# For example:
pi = 3.14159
print(f"{pi:.2f}")  # Using f-string to format to 2 decimal places
print("{:.2f}".format(pi))  # Using format() method to format to 2 decimal places