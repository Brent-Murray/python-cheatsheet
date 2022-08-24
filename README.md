# python-cheatsheets
Useful python cheatsheets and code examples

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

# Get character from string
my_string[0]                   # returns first character "H"
my_string[-1]                  # returns last character "d"

# Slicing strings
my_string[2:5]                 # returns characters between index position 2 and 5 (exluding 5) "llo"

# F (formatted) strings
beverage = "coffee"
message = f"My favourite drink is {beverage}"

# String conversion
message.upper()                # converts string to uppercase
message.lower()                # converts string to lowercase
message.title()                # converts string to titlecase (captitalized first letter in every word)
message.replace('o', 'v')      # replaces 'o' with 'p'

# Finding and checking strings
message.find('o')              # returns index position of first occurance
contains = "drink" in message  # returns boolean (True/False) if string contains character/string
```

