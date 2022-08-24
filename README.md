# Python Cheat Sheet
Python cheatsheet with examples. This cheatsheet will continually be updated so be sure to check back frequently!

Useful scripts can be found in [scripts](https://github.com/Brent-Murray/python-cheatsheets/tree/main/scripts) folder.

Table of Contents
----
| [Variables](https://github.com/Brent-Murray/python-cheatsheets#variables)
| [Commenting](https://github.com/Brent-Murray/python-cheatsheets#commenting)
| [Working with Strings](https://github.com/Brent-Murray/python-cheatsheets#working-with-strings)
| [Working with Lists](https://github.com/Brent-Murray/python-cheatsheets#working-with-lists)
| [Working with Tuples](https://github.com/Brent-Murray/python-cheatsheets#working-with-tuples)
| [Arithmetic Operators](https://github.com/Brent-Murray/python-cheatsheets#arithmetic-operators)
| [Comparison Operators](https://github.com/Brent-Murray/python-cheatsheets#comparison-operators)
| [Print Statements](https://github.com/Brent-Murray/python-cheatsheets#print-statements)
| [If Else Statements](https://github.com/Brent-Murray/python-cheatsheets#if-else-statements)
| [Logical Operators](https://github.com/Brent-Murray/python-cheatsheets#logical-operators)
| [Augmented Assignment Operator](https://github.com/Brent-Murray/python-cheatsheets#assignment-operator)
| [For and While Loops](https://github.com/Brent-Murray/python-cheatsheets#for-and-while-loops)
| [Working with Dictionaries](https://github.com/Brent-Murray/python-cheatsheets#working-with-dictionaries)
| [Functions](https://github.com/Brent-Murray/python-cheatsheets#functions)
| [Exceptions](https://github.com/Brent-Murray/python-cheatsheets#exceptions)
| [Python Standard Library and Importing](https://github.com/Brent-Murray/python-cheatsheets#python-standard-library-and-importing)
| [Installing Packages](https://github.com/Brent-Murray/python-cheatsheets#installing-packages)
|

Variables
----
Variables are used to store data in a computers memory temporarily.
```python
my_string = "Hello World"      # a string (a series of characters in between "" or '')
my_integer = 15                # an integer (whole number with no decimal point)
my_float = 6.4                 # a float (a number with a decimal point)
my_boolean = True              # a boolean (either True or False)
```

Commenting
----
Comments are used to add notes to our code. It is important to incorporate comments into your code to allow future users (especially future you) to understand what is going on throughout the script. Comments can be a good way to also add a reminder for yourself or to break up large chunks of code. Using a `#` allows users to comment code which will not be exicuted.
````python
# Comments will not be executed

"""
This is a multiline string.
You can use this to comment out multiple lines.
This works if it is not assigned as a vairable.
"""
````

Working with Strings
----
Strings are a group a characters that are surrounded by either single `''` or double quotes `""`.
````python
my_string = "Hello World"

# Indexing strings
my_string[0]                   # returns first character "H"
my_string[-1]                  # returns last character "d"

# Slicing strings
my_string[2:5]                 # returns characters between index position 2 and 5 (exluding 5) "llo"

# F (formatted) strings
beverage = "coffee"
message = f"My favourite drink is {beverage}"    # F strings allow you to input variables into strings with {}

# String conversion
message.upper()                # converts string to uppercase
message.lower()                # converts string to lowercase
message.title()                # converts string to titlecase (captitalized first letter in every word)
message.replace('o', 'v')      # replaces old character/string with new character/string
message.strip('e')             # strips all characters from string
message.split()                # splits string on whitespace
message.split('d')             # splits string where 'd' occurs

# Finding and checking strings
message.find('o')              # returns index position of first occurance
contains = "drink" in message  # returns boolean (True/False) if string contains character/string
message.startswith('My')       # returns boolean (True/False) if string starts with character/string
message.endswith("coffee")     # returns boolean (True/False) if string ends with character/string
````

Working with Lists
----
Lists are a changeable, ordered sequence of elements in which each element is called an item. A list is defined by values between square brackets `[]` and commas `,` separating each item.
````python
my_list = [5, 3, 4, 6, 10, 15] # a list is defined by []

# Indexing lists
my_list[4]                     # returns 5th item in list
my_list[-2]                    # returns 2nd item from the end

# Slicing lists
my_list[1:4]                   # returns items from list between index position 1 and 4 (excluding 4) [3, 4, 6]

# Manipulating lists
my_list.append(15)             # adds new item to end of list
my_list.insert(2, 15)          # adds new item at index position 2
my_list.remove(15)             # removes item from list (first occurance)
my_list.pop()                  # removes last item from list
my_list.index(10)              # returns the index position of first occurance
my_list.sort()                 # sorts the list
my_list.reverse()              # reverses the list
my_list.copy()                 # returns copy of list
my_list.clear()                # removes all items from list
````

Working with Tuples
----
Tuples are read-only lists that are defined by circle brackets `()` instead of square.
````python
my_tuple = (5, 2, 4)           # tuples are read-only lists and defined by ()
x, y, z = my_tuple             # unpack a tuple into separate variables (also works with lists)
````

Arithmetic Operators
----
Aritmetic operators allow you to perform calculations of two values.
````python
x = 2
y = 10

x + y                          # addition
x - y                          # subtraction
x * y                          # multiplication
x / y                          # division
x ** y                         # exponentation (x to the power of y)
x % y                          # modulus (remainder of division)
````

Comparison Operators
----
Comparison operators compare variables to perform an evaluation. These produce a boolean return (True/False).
````python
x = 8
y = 15

x > y                          # returns boolean (True/False) if greater than
x >= y                         # returns boolean (True/False) if greater than or equal to
x < y                          # returns boolean (True/False) if less than
x <= y                         # returns boolean (True/False) if less than or equal to
x == y                         # returns boolean (True/False) if equal to
x != y                         # returns boolean (True/False) if not equal to
````

Print Statements
----
Print statements allow users to print into the console. This is done by calling the `print()` function.
````python
print("Hello World")           # print statement

statement = "This is a my print statement"
print(statement)               # print variable
````

If Else Statements
----
If Else statements are used to execute the True and False part of the script given a condition. These are defined with `if`, `elif` and `else`.
````python
a = 12

if a > 2:                      # if statement (if requirement is true)
  print("a is greater than 2)
elif a < 2:                    # elif statement (additional if statement if first requirement isn't met)
  print("a is less than 2)
else:                          # else statement (final statement if none of above requirements met)
  print(a is equal to 2)
````

Logical Operators
----
Logical operators are used to combine conditional statements. `and`, `or`, and `not` are logical operators.
````python
a = 15
b = 12

# and operator
if a > 3 and b < 4:            # and operator requires both statements to match
  print("Both requirements match")
else:
  print("The requirements do not match")

# or operator
if a > 3 or b < 4:             # or operator requires either statement to match
  print("Either requirements match)
else:
  print("Neither of the requirements match
  
# using is
a = True
if a is True:                  # variable is True
  print("a is True")
else:
  print("a is False)  

# not operator
if a is not True               # variable is not True
  print("a is not True")
else:
  print("a is not False")
````

Assignment Operator
----
Assignment operators are used to assign values to a variable with one of the [Arithmetic Operators](https://github.com/Brent-Murray/python-cheatsheets#arithmetic-operators).
````python
x = 5
x = x + 5                      # add 5 to x and reassign variable x
x += 5                         # same as above but more concise 
x -= 5                         # subtract 5 from x and reassign x
x *=10                         # multiply x by 10 and reassign x
x /=5                          # divide x by 5 and reassign x
x %=2                          # modulus of x and 2 and reassign x
x **=2                         # power of 2 to x and reassign x
````

For and While Loops
----
`for` and `while` loops iterate through a sequence performing a some sort of function. `for` loops iterate through every item in the defined sequence where `while` loops iterate through the sequence as long as the condition is true. 
````python
# For loop
sequence = range(1, 7)         # range function creates sequence of numbers between values
for i in sequence:             # loop through all items
  print(i)

# While loop
i = 0
while i < 10:                  # loop while condition is met
  print(i)
  i += 1
````

Working with Dictionaries
----
Dictionaries are used to store data in key/value pairs.
````python
my_dict = {                    # define dictionaries with {}
  "First Key": "First Value",  # key and value pairs separated with :
  "Second Key": 2,             # must include , if more key/value pairs needed 
  "Third Key": True
}

my_dict["First Key"]           # returns value of defined key
my_ dict["First Key"] = "New"  # replaces value of defined key
my_dict.keys()                 # returns collection of keys in dictionary
my_dict.values()               # returns collection of values in dictionary
my_dict.items()                # returns collection of key/value pairs

# Create a dictionary from two lists
keys = ["First Key", "Second Key", "Third Key", "Fourth Key"]
values = [1, 2, 3, 4]
my_new_dict = dict(zip(keys, values)) # creates a dictionary from two lists using dict and zip functions
````

Functions
----
Functions are user defined blocks of code that only run when they are called and can perform tasks and return data as a result. `def` is used to define a function.
````python
# Basic Function
def my_basic_function(in_number):     # define a function with def
  print(in_number)                    # what the function does
  
my_basic_function(10)                 # call function
  
# Positional Function (position of the variables matters when calling function)
def my_subtraction_function(first_number, second_number):
  x = first_number - second_number
  
  return x                            # we can return the a variable from function with return

my_subtraction_function(10, 2)        # returns 8
my_subtraction_function(2, 10)        # returns -8
  
# Key Word Function (variable is predefined)
def my_addition_function(first_number, second_number=10):
  x = first_number + second_number
  
  return x

my_addition_function(2)               # returns 12
my_addition_function(2, 15)           # returns 17 
````

Exceptions
----
Exceptions are errors that stop the script from running. To handel these errors `try` and `except` are used where `try` runs the section of code beneath it testing for errors. If an error occurs the `except` block allows for error handling and specific tasks can be performed.
````python
try:                                       # first try this if error occurs go to except
  population = int(input("Population: "))  # int makes variable an integer and input asks user for input in console
  income = int(input("Income: "))
  value = income / population
  print(f"${value:.2f} per person          #:.2f rounds the value variable to two decimal places in F string
except ValueError:                         # ValueError is raised if input is not a valid number
  print("Input is not a valid number")
except ZeroDivisionError:                  # ZeroDivisionError is raised if population is 0
  print("Population cannot be 0")
````

Python Standard Library and Importing
----
Python has a huge library of base packages that we can perfrom common and useful tasks. Some of these useful packages include:
* [os](https://docs.python.org/3/library/os.html#module-os) - various operating system functions
* [sys](https://docs.python.org/3/library/sys.html) - system parameters and functions
* [datetime](https://docs.python.org/3/library/datetime.html) - used for data and time manipulation
* [glob](https://docs.python.org/3/library/glob.html) - used for finding paths with specified patterns
* [random](https://docs.python.org/3/library/random.html) - used for generating pseudo-random numbers
* [statistics](https://docs.python.org/3/library/statistics.html) - mathematical statistics functions
* [itertools](https://docs.python.org/3/library/itertools.html) - has functions for creating iterators for efficient looping
* [shutil](https://docs.python.org/3/library/shutil.html) - used for file managment
````python
import random                         # import entier package with import function
from random import shuffle            # import specific module with from and import
import statistics as stats            # import package and shorten name with as

my_list = [20, 15, 7, 15, 8]
random.choice(my_list)                # use the choice module from random package
shuffle(my_list)                      # uses shuffle module from random without calling random first
mean_list = stast.mean(my_list)       # uses stats (shortend from statistics in import) to run mean module
````

Installing Packages
----
There are many more Python packages that are available one just needs to install them. These can be found from [PyPl](https://pypi.org/) as well as from [Anaconda](https://anaconda.org/anaconda/repo). Instructions for installing packages from PyPl can be found [here](https://packaging.python.org/en/latest/tutorials/installing-packages/) and from Anaconda [here](https://anaconda.org/anaconda/repo/installers). Once a packages has been installed importing them can be done the same way as described in the [Python Standard Library and Importing](https://github.com/Brent-Murray/python-cheatsheets#python-standard-library-and-importing) section.
