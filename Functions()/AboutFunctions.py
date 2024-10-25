# In Python, a function is a block of reusable code that performs a specific task. Functions make code modular, organized, and easier to read and debug. You define a function using the def keyword, followed by the function name, parentheses ( ) (which can hold parameters), and a colon :. The function body (indented) contains the code the function will execute when called.

# Syntax:

def function_name(parameters):
    # function body
    return value  # optional

# How Functions Work:

# Define the function: Declare the function with a name and, optionally, parameters.
# Call the function: Execute the function by its name followed by parentheses ( ), passing arguments if needed.
# Example 1: A Simple Function
# Let’s start with a simple example where we define a function that prints a greeting.


# Define the function
def greet():
    print("Hello, welcome to Python!")

# Call the function
greet()


# Explanation
# greet is the name of the function.
# When we call greet(), Python executes the code within the function, printing the message.
# Example 2: Function with Parameters
# This example shows a function that takes a parameter to customize the greeting.


def greet(name):
    print(f"Hello, {name}! Welcome to Python!")

# Call the function with an argument
greet("Arslan")

# Explanation
# The function greet now takes a parameter name.
# When we call greet("Arslan"), "Arslan" is passed as an argument to name, and the function prints "Hello, Arslan! Welcome to Python!".
# Example 3: Function with Return Value
# Here, we define a function that takes two numbers, adds them, and returns the result.

def add_numbers(a, b):
    return a + b

# Call the function and store the result in a variable
result = add_numbers(5, 3)
print(result)  # Output: 8

# Explanation
# add_numbers takes two parameters, a and b.
# return a + b gives back the sum of a and b to where the function was called.
# result stores the returned value, which we print.
# Example 4: Complex Function with Default Parameters and Multiple Returns
# In this example, let’s create a function that calculates the area and perimeter of a rectangle. We’ll also use default parameters for cases when only one value is provided.

def rectangle_properties(length, width=1):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Call the function with two arguments
area, perimeter = rectangle_properties(5, 3)
print("Area:", area)        # Output: 15
print("Perimeter:", perimeter)  # Output: 16

# Call the function with one argument, using the default width
area, perimeter = rectangle_properties(5)
print("Area with default width:", area)        # Output: 5
print("Perimeter with default width:", perimeter)  # Output: 12

# Explanation
# rectangle_properties calculates both area and perimeter of a rectangle.
# width has a default value of 1, so if width isn’t provided, the function uses 1.
# The function returns two values, which we can store separately using tuple unpacking.
# Example 5: Complex Function with Recursion (Factorial Calculation)
# In this example, we use recursion (a function calling itself) to calculate the factorial of a number.


def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n * factorial(n - 1)

# Call the function
# result = factorial(5)
# print(result)  # Output: 120
# Explanation
# factorial is a recursive function.
# The base case checks if n is 0 or 1, where the factorial is 1.
# Otherwise, it calculates n * factorial(n - 1), repeatedly calling itself with decremented values until reaching the base case.
# When we call factorial(5), it calculates 
# 5
# ×
# 4
# ×
# 3
# ×
# 2
# ×
# 1
# =
# 120
# 5×4×3×2×1=120.


# Summary of Key Points
# Functions encapsulate code, making it reusable and modular.
# Functions can take parameters and return values.
# Default parameters allow flexibility when some arguments are optional.
# Recursive functions call themselves and need a base case to avoid infinite recursion.
# With these examples, you should now have a solid understanding of how to use functions in Python, from simple to complex scenarios!