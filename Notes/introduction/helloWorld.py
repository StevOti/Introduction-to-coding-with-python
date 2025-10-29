# Ask user for the name
name = input("What is your name? ")
# here the name variable stores the user's input

# Greet the user
print("Hello, " + name + "!")

# We can also represent the same code in a single line as below:
print ("Hello, " + input("What is your name? ") + "!")
# or
print("Hello,", name + "!")
# or
print(f"Hello, {name}!")



# What you can pass to a function, or what the input function can take, is called an argument/parameter.
# In this case, the argument is the string "What is your name? "
# *objects, the * means the argument can be of any type, not just strings.
# For example, you can pass an integer, float, list, dictionary, etc.
# \n is a special character that represents a new line. \ is an escape character.
# So, when you use \n in a string, it tells Python to move to the next line.


#String-methods
# String methods are functions that are built into Python and can be used to manipulate strings.
# For example, the upper() method converts a string to uppercase, and the lower() method converts a string to lowercase,
# and the title() method capitalizes the first letter of each word in a string, and the strip() method removes any leading or trailing whitespace from a string.
# Here are some examples of string methods:
print(name.upper())  # Converts the name to uppercase
print(name.lower())  # Converts the name to lowercase
print(name.title())  # Capitalizes the first letter of each word in the name
print(name.strip())  # Removes any leading or trailing whitespace from the name


# You can also chain string methods together, like this:
# print(name.strip().title())   Strips whitespace and then capitalizes the first letter of each word

# E.g
name = input("What is your full name? ").strip().title()
print(f"Hello, {name}!")

# Split strings
# The split() method splits a string into a list of substrings based on a specified delimiter (default is space).
# For example:
first, last = name.split()  # Splits the name into first and last name
print(f"Hello, {first}! Your last name is {last}.")