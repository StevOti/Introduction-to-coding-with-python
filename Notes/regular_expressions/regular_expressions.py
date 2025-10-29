# A regular expression(regex) is a pattern used to match some kind of data often user input
# For example, when a user types out an email, you may want to validate that they indeed typed an email address
# Using regular expressions we can define patterns in our code to compare them against data that we're receiving
# from somewhere else, even if its cleaning up a mixed up data
# For example,

email = input("what's your email? ").strip()

if '@' in email:
    print("Valid")
else:
    print("Invalid")

# We can improve this,

email = input("what's your email? ").strip()

if '@' in email and "." in email:
    print("Valid")
else:
    print("Invalid")

# But all these codes are still buggy, lets explain how we want the user to type the email specifically
email = input("what's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

# And we can be more precise when we say
email = input("what's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

# There's a library in pthon for regualr expressions, called re
# It allows you to check for, define and replce patterns
# Examples
# re.search(pattern, string, flags=0) is a versatile functions, that allows you to passs three arguments, we refined the code as below

import re

email = input("what's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

# The pattern parameter can take the special symbols below:
# . - any character except newline
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetition
# {m} - m repetitions
# {m, n} - m-n repetitions

# So to refine this code
import re

email = input("what's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")

# The .*@.* is a regular expression, meaning, zero or more characters(.) followed by @ then followed by zero or more characters
# But the equivalent of plus is ..* so incase we want to refine the code we say

import re

email = input("what's your email? ").strip()

if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")

# but if you want to use the +, you can change the code to

import re

email = input("what's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")


# We can use \.edu if we want all the user emails to end in edu 
# and a r before the string to tell python not to interpret any backslashes
import re

email = input("what's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

# There are more special symbols is re module
# ^ - matches the start of a string
# $ - matches the end of a string or just before a new line at the end of a string

# Now to refine the code further, to make sure the user only inputs an email in the requested format
import re

email = input("what's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Regular expressions also supports the following syntax
# [] - set of characters
# [^] - complementing the set

# To refine the code further,
# we use [^@] which has the effect of saying this is set of characters except the @

import re

email = input("what's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# We can still improve the code further:
# To specify a set of characters in the alphabet, A-Z is for capitalized letters, 0-9 for numbers
# and _ for underscores

import re

email = input("what's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Some of these patterns are built in as shortcuts so you dont have to write them
# for example, instead we can use, \w to represent a word, symbol or underscore character

import re

email = input("what's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Here's a partial list of the patterns that you can use within regular expressions
# \d = decimal digit
# \D = not a decimal digit
# \s = whitespace characters
# \S = not a whitespace character
# \w = word character, as well as numbers and the underscore
# \W = not a word character

# To represent more domains we can say,
# if re.search(r"^\w+@\w+\.(org|edu|com|gov)$", email):

# A|B means either a or b
# (...) a group
# (?:...) non-capturing version

# To make the user input email be all lower case,

import re

email = input("what's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email.lower()):
    print("Valid")
else:
    print("Invalid")

# or

import re

email = input("what's your email? ").strip().lower()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# or we can use the flags argument
# The flag arguments you can pass include:
# re.IGNORECASE - treats the user's input in case insensitive manner
# re.MULTILINE - matches multiple lines of text
# re.DOTALL - configure any characters plus new lines
# in this case we can demonstrate using re.IGNORECASE


import re

email = input("what's your email? ").strip().lower()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# To handle more dots in the user's email
# The ? in the regular expression r"^\w+@(\w+\.)?\w+\.edu$" shows that this (\w+\.) or characters 
# that appear in the parenthesis can either be there or not be there at all
import re

email = input("what's your email? ").strip().lower()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# re.match = automatically starts matching from the start of a string
# re.fullmatch = automatically matches all the characters



# Reformating user input data into the format we want
# The code below checks for a comma in the user input(name) and reformats the input to what we want

import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print("hello, {name}")


# We can refine the code further
import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + "" + matches.group(1)
print("hello, {name}")

# We can refine the code further by using the := operator called walrus operator
import re

name = input("What's your name? ").strip()
if matches:= re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


# We can use replace to replace extract an unwanted word and replace it with another

# For example, we can recover a twitter username from url
url = input("URL:").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")


# we can also use removeprefix
url = input("URL:").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")

# To capture/clean up set of info, we can use re.sub
# Any time you are expecting the user to use a special character and dont want it to be interpreted by the code, 
# just use the forward slash (\)

import re

url = input("URL:").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# Another scenerio, if you run the code below... it returns none instead of username
import re

url = input("URL:").strip()
matches = re.search(r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))

# To fix this we, we matched the subdomain-(www\.)? which is now considered as group 1, therefore the 
# username grouped as (.+) will be group 2. this will now return the username

import re

url = input("URL:").strip()
matches = re.search(r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))

# To refine the code further with walrus operator, we can also use the non capturing (?:...) to remove the www.

import re

url = input("URL:").strip()
if matches:= re.search(r"^https?://?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
