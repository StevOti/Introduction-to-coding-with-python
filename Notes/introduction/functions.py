

# Def for define is used to create a function
# for example:
def hello():
    print("hello")

hello()
name = input("What is your name? ")
print(f"Hello, {name}!")

# or we can also represent the same code above as below:
def hello(to):
    print("Hello, " + to + "!")

name = input("What is your name? ")
hello(name)

# Functions can also take parameters/arguments
def greet(name):  # name is a parameter
    print(f"Hello, {name}!")

# To make the argument have a default value, we can do the following:
def greet(name="Guest"):  # name is a parameter with a default value
    print(f"Hello, {name}!")

# scope refers to a variable only existing in the context in which you defined it.

# Now to write the complete function in a conventional way:

def greet():
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(to="Guest"):
    print("Hello, ", to, "!")

greet()  # Call the greet function without an argument, so it will use the default value "Guest"



# Examples of complete functions

# Create a funtion that squares a number

def main():
    num = int(input("Enter a number to be squared: "))  # Convert input to int
    print(f"The square of {num} is ", square(num))  # Call the square function and print the result

def square(n):
    return n * n  # Return the square of the number
    # or return n ** 2
    # or return pow(n, 2)
    # Both methods will give you the same result


main()  # Call the main function to run the program

# Write a code that asks the user for an input then prints "meow" number of times the user gave

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main()

