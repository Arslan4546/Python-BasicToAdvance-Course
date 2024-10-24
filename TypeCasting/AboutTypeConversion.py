# In Python, type conversion refers to the process of converting one data type to another. Python provides two types of type conversion:

# Implicit Type Conversion (Automatically handled by Python)
# Explicit Type Conversion (Manually done by the programmer)
# 1. Implicit Type Conversion
# Python automatically converts one data type to another without the user's intervention.

#  For example:

# Implicit Type Conversion
x = 10    # int
y = 2.5   # float

# Adding int and float, Python automatically converts int to float
result = x + y 
print(result)   # Output: 12.5
print(type(result))  # Output: <class 'float'>


# 2. Explicit Type Conversion
# This is when we manually convert a data type into another using Python’s built-in functions.

# Common Type Conversion Functions:
# int(): Converts a value to an integer.
# float(): Converts a value to a floating-point number.
# str(): Converts a value to a string.
# list(): Converts an iterable to a list.
# tuple(): Converts an iterable to a tuple.
# set(): Converts an iterable to a set.
# dict(): Converts a list of key-value pairs to a dictionary.
# chr(): Converts an integer to its Unicode character.
# ord(): Converts a character to its Unicode integer.
# hex(): Converts an integer to a hexadecimal string.
# oct(): Converts an integer to an octal string.


# Examples of Explicit Type Conversion:
##1. Integer to Float

a = 5   # int
b = float(a)  
print(b)  # Output: 5.0
##2. Float to Integer

a = 5.67  
b = int(a)  
print(b)  # Output: 5
##3. String to Integer/Float

s = "123"
i = int(s)  
f = float(s)  
print(i)  # Output: 123
print(f)  # Output: 123.0
##4. Integer to String

a = 100  
s = str(a)  
print(s)  # Output: "100"
##5. List to Tuple

lst = [1, 2, 3]  
tpl = tuple(lst)  
print(tpl)  # Output: (1, 2, 3)
##6. Tuple to List

tpl = (1, 2, 3)  
lst = list(tpl)  
print(lst)  # Output: [1, 2, 3]
##7. List to Set

lst = [1, 2, 2, 3]  
st = set(lst)  
print(st)  # Output: {1, 2, 3}
##8. Set to List

st = {1, 2, 3}  
lst = list(st)  
print(lst)  # Output: [1, 2, 3]
##9. List of Tuples to Dictionary

lst = [('a', 1), ('b', 2)]
dct = dict(lst)
print(dct)  # Output: {'a': 1, 'b': 2}
##10. Integer to Character (Unicode)

a = 65  
ch = chr(a)  
print(ch)  # Output: 'A'
##11. Character to Integer (Unicode)

ch = 'A'
a = ord(ch)  
print(a)  # Output: 65
##12. Integer to Hexadecimal

a = 255  
hex_value = hex(a)  
print(hex_value)  # Output: '0xff'
##13. Integer to Octal

a = 255  
oct_value = oct(a)  
print(oct_value)  # Output: '0o377'

# These are the most commonly used type conversions in Python.