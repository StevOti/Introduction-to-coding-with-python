# Python gives you flexibility on how to solve problems with code
# Assuming we want to build a function that requests for the name and house

name = input("Name:")
house = input("House:")
print(f"{name} from {house}")

# Then we put our program above in a def function called main
def main():
    name = input("Name:")
    house = input("House:")
    print(f"{name} from {house}")


# Then we change the input sections to be their own functions called get_name
# and get_house so that we can build on them

def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


# Then we expand on the undefined functions get_name and get_house

def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    name = input("Name:")
    return name

def get_house():
    house = input("House:")
    return house

# We can then simplify the get_name and get_house function
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name:")
    
def get_house():
    return input("House:")

if __name__ == "__main__":
    main()

# Since get_name and get_house are simple functions, we can combine then into one function that returns house and name values
# then now we pass the get_student function in the main function so that we can access the name and house values
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name:")
    house = input("House:")
    return name, house

if __name__ == "__main__":
    main()

# We have just used a a tuple, a type of data in python that is a collection of values
# Now we change the tuple we accessed in the main function to student
def main():
    student = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name:")
    house = input("House:")
    return (name, house)

if __name__ == "__main__":
    main()


# Now we access the name and house parameters in the student by changing the print as follows
# the [0] and [1] are the locations of the parameters in that tuple
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name:")
    house = input("House:")
    return (name, house)

if __name__ == "__main__":
    main()

# Assuming we want to make a change to one of the user input, we can use if statements to make sure we override 
# the user input
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name:")
    house = input("House:")
    return (name, house)

if __name__ == "__main__":
    main()

# when you run this program you get the error: "TypeError: 'tuple' object does not support item assignment"
# This shows the immutability of tuples meaning you cant change the location of the values returned.
# To fix this error we can use [] instead of (name, house) returned in the get_student function

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name:")
    house = input("House:")
    return [name, house]

if __name__ == "__main__":
    main()

# We can improve our program by refining the get_student by using a dictionary since it has key and value pairs and 
# the values are not restricted in their locations
# Then we access the keys in the student by changing the main function as follows.
def main():
    student = get_student()
    print(f"{student["name"]} from {student[house]}")

def get_student():
    student = {}
    student = ["name"] = input("Name: ")
    student = ["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()

# The program wont run because python will raise a syntax error because of the double quotes in the main function as below

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student = ["name"] = input("Name: ")
    student = ["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()

# We can shorten the code by refining the get_student function

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = ["name"] = input("Name: ")
    house = ["house"] = input("House: ")
    return {"name" : name, "house" : house}

if __name__ == "__main__":
    main()

# Dictionaries are mutable, meaning you can change whatever is in them just like lists
# Now we can return the if statement that enabled us to override one input

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclay"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name" : name, "house" : house}

if __name__ == "__main__":
    main()


# We have stored the data in a tuple, list and dictionary, there's another way to create or own data types as well and actually give them names.
# Thats using a class - kind of like a blueprint for pieces of data(object)
# Classes allow you to invent your own data types in python and give them names.
# We use the word class to define custom containers with custom names for data
# In our code lets create a class for students and define it
# That means we will remove the name and house parameters from the get_student function and use the Student class in that function

# Classes have attributes = properties of sort that allow you to specify values inside of them
# They are accessed using a . ie student.name and student.house
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house  }")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()

# The above code shows we have created  our data type called Student
# In student = Student(), we are now creating the objects of that class Student
# object is also called and instance.
# 

# Just by defining a class you get a function whose name is identical to the class
# In our case its Student
# We have refined our code by calling the Student function

class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house  }")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()

# Classes come with methods or functions inside of them that you can define and they just behave in a special way.
# These functions allow you to determine behaviour in a standard way.
# Lets now define our class Student

# To inialize the contents of an object from a class

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house  }")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()


# student = Student(name, house) = constructor call
# It is a line of code that is going to construct/instantiate a student object
# It is going to use the Student class as a template so that all students have names and homes
# __init__ is the function that is being called when student = Student(name, house) is being executed
# The self parameter in the __init__ function gives you access to the objects was just created

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house  }")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# Now lets validate if the name and house data have been entered by the user in the Student class
# We can raise exceptions when there's an error using raise. so we raise the error in class
# Then we use try and except to validate that in the get_student()
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("No name was entered")
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house  }")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     try:
#         return Student(name, house)
#     except ValueError:
#         ...

# if __name__ == "__main__":
#     main()



# But for now lets just raise the error
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house  }")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# To add the middle and last name, this is what we do
class Student:
    def __init__(self, first, middle, last, house):
        if not first:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.first = first
        self.middle = middle
        self.last = last
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house  }")

def get_student():
    first = input("First Name: ")
    middle = input("Middle Name: ")
    last = input("Last Name: ")
    house = input("House: ")
    return Student(first, middle, last, house)

if __name__ == "__main__":
    main()


# if you use this line print(student) to print the objects, it will also display the address of the objects,
# To override this we use __str__ method - is a special method that if you define in your class, python will just automatically call
# this function for you anytime another function wants to see your object as a string
# So we define __str__ under the __init__ method

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# The good thing about classes is that they can also have functions built in called methods
# We will now create our own method that returns an emoji thats appropriate for each of the students patronus called charm

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🚬"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()

# We can also use the student.house to change the value of the object house in the main function as follows:
# Meaning classes dont limit the programmer from changing/overwritting the values of the objects created

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# A property = is an attribute that has more defense mechanisms(functionalities implemented by the programmer) put in place to prevent
# messing up
# They are attributes that programmers have little bit more control of
# To use it we use @property
# Decorators = are functions that modify the behavior of other functions

# In our example, we will create a function house
# We created a getter - is a function in a class that gets some attributes
# and setter - is a function in a class that sets some value

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# The reason to use getters and setters, is to have some control so that someone can not try mannually set a value to your objects

# We can also create setters and getters for name

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# Python majorly focuses on conventions and not hard constraints
# Sometimes you want some functionality to be associated with the class itself, no matter what the specific objects or values are
# We use @classmethod = a decorator/ function that you can use to specify that this method is not by default implicitly an instance method
# but has access to the object itself but does know what class it's in
# Meaning
# Lets create a file called hat.py
# We are assigning the name harry to a random house in the code
import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, " is in ", random.choice(self.houses))

# instantiate hat object
hat = Hat()
hat.sort("Harry")


# we can refine our code by using @classmethod = it exists within that class itself and there's only one copy for all of the objects thereof
# There is no instantiating the method in this way

import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, " is in ", random.choice(cls.houses))


Hat.sort("Harry")


# Now to use some of the ideas we learnt to clean up the student.py
# It will now be 

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)



if __name__ == "__main__":
    main()


# Inheritance = this is where you can have one class borrow attributes(methods) from another class if they have all those in common
# We open a new file called wizard.py
# To make the student and professor class inherit the name object from the wizard class, we can do this

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")


# Operator Overlading = this is where you can take any common symbols in the keyboard and you can 
# implement your own interpretation thereof, ie + does not have to equal addition and - does not have to 
# equal minus
# To demonstrate this, we create a new file called vault.py
class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0):
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

galleons = potter.galleons + weasly.galleons
sickels = potter.sickels + weasly.sickels
knuts = potter.knuts + weasly.knuts

total = Vault(galleons, sickels, knuts)
print(total)


# There is a way to add weasly's and potter's vault values using operator overloading
# object.__add__(self, other) self= will be referring to the object on the left side of the operator(+)
# while other will refer to the one on the right side of the operator(+)

class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0):
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickels = self.sickels + other.sickels
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickels, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

galleons = potter.galleons + weasly.galleons
sickels = potter.sickels + weasly.sickels
knuts = potter.knuts + weasly.knuts

total = potter + weasly
print(total)

# This is now the implementation of operator overloading
