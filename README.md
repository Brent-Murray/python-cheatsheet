# python-cheatsheets
Python cheatsheet with examples. This cheatsheet will continually be updated so be sure to check back frequently!

Useful scripts can be found in [scripts](https://github.com/Brent-Murray/python-cheatsheets/tree/main/scripts) folder.

Table of Contents
----
| [Variables](https://github.com/Brent-Murray/python-cheatsheets#variables) | [Commenting](https://github.com/Brent-Murray/python-cheatsheets#commenting) | [Working with Strings](https://github.com/Brent-Murray/python-cheatsheets#working-with-strings) |
| [Working with Lists](https://github.com/Brent-Murray/python-cheatsheets#working-with-lists) | [Arithmetic Operators](https://github.com/Brent-Murray/python-cheatsheets#arithmetic-operators) | [Comparison Operators](https://github.com/Brent-Murray/python-cheatsheets#comparison-operators) |
[Print Statements](https://github.com/Brent-Murray/python-cheatsheets#print-statements)

Variables
----
```python
my_string = "Hello World"      # a string (a series of characters in between "" or '')
my_integer = 15                # an integer (whole number with no decimal point)
my_float = 6.4                 # a float (a number with a decimal point)
my_boolean = True              # a boolean (either True or False)
```
Commenting
----
````python
# Using a # allows you to comment your code
# Comments will not be executed

"""
This is a multiline string.
You can use this to comment out multiple lines.
This works if it is not assigned as a vairable.
"""
````

Working with Strings
----
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

Arithmetic Operators
----
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
````python
print("Hello World")           # print statement

statement = "This is a my print statement"
print(statement)               # print variable
````
