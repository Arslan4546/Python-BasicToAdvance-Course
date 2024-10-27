# Recursion in Python is a programming technique where a function calls itself in order to solve a problem. Recursion is helpful when a problem can be divided into smaller, similar subproblems. Each recursive call should bring the solution closer to a base case, where the problem is small enough to be solved directly without further recursion.

# Basic Structure of Recursion in Python

def recursive_function(parameters):
    if base_case_condition:
        return base_case_value
    else:
        # Recursive call
        return recursive_function(modified_parameters)
    

# Example 1: Simple Recursion (Factorial of a Number)

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120

# Example 2: Complex Recursion (Fibonacci Sequence)

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. It can be defined recursively as:

def fibonacci(n):
    if n <= 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print(fibonacci(5))  # Output: 5


# Explanation
# Base Cases: If 

# expanding further until the base cases are reached.
# Limitations and Performance
# Recursive Fibonacci is computationally expensive because it recalculates values multiple times. Using techniques like memoization (caching previously computed results) or iterative solutions can significantly optimize the calculation of Fibonacci numbers for larger inputs.