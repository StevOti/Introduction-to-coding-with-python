# Unit tests are test cases written to test your program
# Unit testing is testing individual units(functions) of your program
# For example refer to calculator.py and test_calculator.py

# calculator.py
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n + n # This is where the error is, its supposed to be n*n

if __name__ == "__main__":
    main()

# test_calculator.py

from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 square was not 4")

    if square(3) != 9:
        print("3 square was not 9")


if __name__ == "__main__":
    main()

# Assert is a keyword in python that allows you to assert that something is true...
# if its true, no error appears, but if its false, an error appears
# we can use the below
# test_calculator.py

from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()

# If we run the test_calculator.py, we get an assertionError,
# To fix this we do the following
# test_calculator.py

from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")


if __name__ == "__main__":
    main()

# Refine the code by writing it as below
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")


if __name__ == "__main__":
    main()


# pytest is a third party program that you can download and install that will automate the testing of your
# codes so long as you write the tests
# Advantage - It adapts some conventions so that you dont manually write so many lines of codes to test

# To simplify our test_calculator.py,
from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# The above test will stop at the first fail, which is in the square of 3, to make the unit test attempt all the tests is the program,
# we can do the below

from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# When all the tests pass, meaning your program/ functions passed all the tests. but this does not mean that the code is 100% perfect.
# You can create unit tests in different files or even in one file


# To add a test for typeError in the program, that is when a user enters a string = "cat" instead of an int value... strings cant be multiplied

# calculator.py
def main():
    x = input("What's x? ")
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()


# test_calculator.py
import pytest

from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")



# Example case
# Lets test this program below

# hello.py
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()


# test_hello.py
from hello import hello

def test_default():
    assert hello("Stephen") == "hello, Stephen"

def test_argument():
    assert hello() == "hello, world"


# To test the program using a list, you can say:
from hello import hello

def test_default():
    assert hello("Stephen") == "hello, Stephen"

def test_argument():
    for name in ["Stephen", "Daisy", "Edwin"]:
        assert hello(name) == f"hello, {name}"



# We can also test our programs using a folder that we have written our unit tests
# In this case we create a folder called test and a new file called test_hello.py

# test/test_hello.py
from hello import hello

def test_default():
    assert hello("Stephen") == "hello, Stephen"

# To be able to test the hello.py file with the new test file in the folder test, we have to create a new file
# in the folder test called __init__.py
# __init__.py tells python to treat the folder its in like a package(a directory with many modules)
# Once you do that you can just run the command "pytest test"... this will test all the test modules we have written in the folder test
# for our program
