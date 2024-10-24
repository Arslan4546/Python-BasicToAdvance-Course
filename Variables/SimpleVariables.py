
# Explanation of Variables in Python

# A variable in Python is a symbolic name that refers to a value stored in memory. It's like a container that holds data, which can be of any type (e.g., integers, strings, floats, lists, etc.). Python variables are dynamically typed, meaning you don’t need to declare the type of a variable explicitly. The type is inferred from the value you assign to it.

# Key Points:
# Dynamic Typing: You don't need to specify the type of variable; Python figures it out.


a = 10  # 'a' is an integer
b = "Hello"  # 'b' is a string
c = 3.14  # 'c' is a float

# Variable Naming Rules:

# Must start with a letter or an underscore (_).
# Can contain letters, numbers, and underscores.
# Case-sensitive (a and A are different).
# Should not use reserved keywords (e.g., if, else, while).
# Assignment: Variables are assigned values using the = operator.


x = 5  # assigns 5 to x
name = "John"  # assigns string to name

# Reassigning Variables: Variables can be reassigned new values, even of different types.

num = 5  # num is an integer
num = "five"  # now num is a string

# Complex Examples:
# Example 1: Using Variables in Mathematical Operations


x = 10
y = 3
z = x ** y  # exponentiation (10 raised to the power of 3)
print(f"{x} raised to {y} is {z}")  # Output: 10 raised to 3 is 1000

# Explanation:

# x ** y computes x to the power of y. In this case, 10 raised to 3 results in 1000.
# Example 2: Concatenating Strings with Variables

first_name = "Arslan"
last_name = "Tariq"
full_name = first_name + " " + last_name  # concatenates first_name and last_name
print(f"Full name: {full_name}")  # Output: Full name: Arslan Tariq

# Explanation:

# Variables first_name and last_name are combined using the + operator to form a full name.
# Example 3: List Operations with Variables


numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # adds 6 to the end of the list
numbers[0] = 10  # changes the first element to 10
print(numbers)  # Output: [10, 2, 3, 4, 5, 6]

# Explanation:

# A list numbers is created, modified, and then printed. The append() method adds a new element to the list, and indexing (numbers[0]) changes an existing element.

# Example 4: Using Variables in Functions

def greet(name):
    greeting = "Hello, " + name + "!"
    return greeting

result = greet("Sallu")
print(result)  # Output: Hello, Sallu!

# Explanation:

# The function greet takes a variable name and uses it inside a greeting message. The result is then printed.

# Example 5: Dictionary with Variables

student = {
    "name": "Arslan",
    "age": 25,
    "courses": ["Math", "Science", "History"]
}

# Accessing values using variables
student_name = student["name"]
student_courses = student["courses"]

print(f"Student Name: {student_name}")
print(f"Enrolled Courses: {student_courses}")

# Explanation:

# A dictionary student holds multiple key-value pairs. Variables are used to access and display specific data from the dictionary.