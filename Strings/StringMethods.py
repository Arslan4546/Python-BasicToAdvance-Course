# String Methods
# Python provides many built-in string methods to manipulate and operate on strings. Let's explore the most commonly used methods:

# 1. len()
# Description: Returns the length of the string.

# Example:

s = "Hello"
print(len(s))  # Output: 5

# 2. lower()

# Description: Converts the string to lowercase.

# Example:

s = "Hello"
print(s.lower())  # Output: hello

# 3. upper()

# Description: Converts the string to uppercase.

# Example:

s = "Hello"
print(s.upper())  # Output: HELLO

# 4. capitalize()

# Description: Capitalizes the first letter of the string.

# Example:

s = "python is fun"
print(s.capitalize())  # Output: Python is fun

# 5. title()

# Description: Converts the first character of each word to uppercase.

# Example:

s = "python is fun"
print(s.title())  # Output: Python Is Fun

# 6. strip()

# Description: Removes leading and trailing whitespace (or characters).

# Example:


s = "  Hello  "
print(s.strip())  # Output: Hello

# 7. lstrip() / rstrip()

# Description: lstrip() removes leading whitespace, rstrip() removes trailing whitespace.

# Example:
s = "  Hello  "
print(s.lstrip())  # Output: "Hello  "
print(s.rstrip())  # Output: "  Hello"

# 8. replace()

# Description: Replaces all occurrences of a substring with another.

# Example:

s = "Hello World"
print(s.replace("World", "Python"))  # Output: Hello Python

# 9. split()
# Description: Splits the string into a list of substrings based on a delimiter.

# Example:

s = "Python is fun"
print(s.split())  # Output: ['Python', 'is', 'fun']

# 10. join()
# Description: Joins elements of a list into a single string with a specified delimiter.

# Example:


words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: Python is fun

# 11. find()
# Description: Returns the index of the first occurrence of a substring. If not found, returns -1.

# Example:

s = "Hello World"
print(s.find("World"))  # Output: 6

# 12. count()
# Description: Returns the number of occurrences of a substring in the string.
# Example:

s = "banana"
print(s.count("a"))  # Output: 3
# 13. startswith() / endswith()
# Description: Returns True if the string starts/ends with the specified substring, otherwise False.

# Example:

s = "Hello World"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World"))    # Output: True

# 14. isalpha()

# Description: Returns True if all characters in the string are alphabetic.

# Example:

s = "Hello"
print(s.isalpha())  # Output: True

# 15. isdigit()

# Description: Returns True if all characters in the string are digits.

# Example:

s = "12345"
print(s.isdigit())  # Output: True

# 16. islower() / isupper()

# Description: Returns True if all characters are lowercase (islower()) or uppercase (isupper()).

# Example:

s = "hello"
print(s.islower())  # Output: True
print(s.isupper())  # Output: False

# 17. swapcase()

# Description: Swaps the case of each character in the string.

# Example:

s = "Hello World"
print(s.swapcase())  # Output: hELLO wORLD

# 18. zfill()
# Description: Pads the string with zeros on the left, making it of a specified length.
# Example:

s = "42"
print(s.zfill(5))  # Output: 00042


# 19. format()
# Description: Formats the string using placeholders.

# Example:

name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Output: My name is John and I am 30 years old.
# String Operators
# Concatenation: Joining two strings using the + operator.


s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Output: Hello World

# Repetition: Repeating a string using the * operator.


s = "Hello"
print(s * 3)  # Output: HelloHelloHello

# Membership Operators: Checking if a substring exists in a string using in and not in.

s = "Hello World"
print("World" in s)  # Output: True
print("Python" not in s)  # Output: True

# String Immutability

# As mentioned earlier, strings in Python are immutable. This means once a string is created, you cannot modify it. Any operation that modifies a string returns a new string.

# For example:


s = "Hello"
s[0] = 'h'  # This will raise an error, as strings are immutable