# Strings in Python
# In Python, a string is a sequence of characters enclosed within either single quotes ('...'), double quotes ("..."), or triple quotes ('''...''' or """..."""). Strings are one of the most common data types used in Python, and they are immutable, meaning once a string is created, it cannot be modified.

# Creating Strings:

# Single quotes
string1 = 'Hello'

# Double quotes
string2 = "Hello"

# Triple quotes (used for multi-line strings)
string3 = '''Hello
World'''

# Another way to create a string is by using the str() function
string4 = str(12345)  # Converts an integer to a string


# Accessing and Slicing Strings
# You can access characters in a string using indexing (starting from 0) and slice parts of the string using slicing ([start:end:step]).


s = "Python"

# Accessing characters
print(s[0])  # Output: P
print(s[-1])  # Output: n (negative index starts from the end)

# Slicing
print(s[1:4])  # Output: yth
print(s[:3])   # Output: Pyt (slicing from start)
print(s[3:])   # Output: hon (slicing till end)
print(s[::-1])  # Output: nohtyP (reversing the string)