# Syntax errors are errors that must be corrected in the code and cannot correct themselves
# For example:
# print("hello, world)


# Runtime errors are errors that happen when your code is running and you need to write some additional code defensively to
# detect when these errors happen

# Value errors happen when you for example input an int where you're supposed to input a string
# NameError are also types of errors
# How to handle errors

while True:
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

# The logic above uses a loop and a break to break out of the loop

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
    

main()

# If you want to pass an exception without saying anything... use pass

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
    
main()

# or we can also simplify the code above as

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
    
main()

