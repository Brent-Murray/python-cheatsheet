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
