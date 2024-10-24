# Single-Line if in Python
# A single-line if statement is a concise way to write a conditional expression in Python, often used for simple checks where you want to execute a small piece of code based on a condition. In Python, the basic syntax for a single-line if statement is:

# [expression] if [condition] else [other_expression]
# This is known as a ternary conditional operator (or conditional expression), which allows you to write if-else logic in a single line.

# Syntax:

# result = true_value if condition else false_value
# condition: A logical expression that evaluates to either True or False.
# true_value: The value to be assigned to result if the condition is True.
# false_value: The value to be assigned if the condition is False.

# Usage in Daily Life
# Single-line if statements are useful when you want to make quick decisions based on conditions, such as:

# Checking whether a number is positive, negative, or zero.
# Assigning values to variables based on certain conditions.
# Displaying different messages or results based on user input.

# Simple Examples:
# Example 1: Check if a Number is Even or Odd

num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

# Explanation:

# The condition num % 2 == 0 checks if the number is divisible by 2. If it's true, result is assigned "Even". If false, result is "Odd".

# Example 2: Determine if a Person is an Adult

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Explanation:

# The condition age >= 18 checks if the person is 18 or older. If true, status is "Adult". If false, status is "Minor".

# Complex Examples:
# Example 3: Grading System Using Single-Line if

marks = 75
grade = "A" if marks >= 85 else "B" if marks >= 70 else "C" if marks >= 50 else "D"
print(grade)  # Output: B

# Explanation:

# This example checks multiple conditions in a single line:
# If marks >= 85, the grade is "A".
# If marks >= 70 (but less than 85), the grade is "B".
# If marks >= 50 (but less than 70), the grade is "C".
# Otherwise, the grade is "D".

# Example 4: Check if a String is Empty

text = ""
message = "Text is not empty" if text else "Text is empty"
print(message)  # Output: Text is empty

# Explanation:

# The condition checks if the string text is non-empty. If true, it prints "Text is not empty". If false (i.e., the string is empty), it prints "Text is empty".

# Example 5: Calculating Shipping Cost Based on Weight

weight = 10
shipping_cost = 5 if weight <= 5 else 10 if weight <= 10 else 20
print(f"Shipping cost: ${shipping_cost}")  # Output: Shipping cost: $10

# Explanation:

# This example calculates the shipping cost based on the weight of a package:
# If weight is 5 kg or less, the cost is $5.
# If weight is between 5 and 10 kg, the cost is $10.
# If weight is more than 10 kg, the cost is $20.

# Example 6: Determine Maximum of Two Numbers

a = 15
b = 20
max_value = a if a > b else b
print(f"The maximum value is {max_value}")  # Output: The maximum value is 20

# Explanation:

# The condition checks if a is greater than b. If true, max_value is assigned the value of a; otherwise, it's assigned the value of b.
# Benefits of Single-Line if:
# Conciseness: It allows for cleaner, shorter code when conditions are simple.
# Improves Readability: If the logic is simple enough, it can make the code more readable.
# Saves Space: Useful when you don’t want to break the flow of the code for very simple conditional checks.

# When to Use:
# Use single-line if when the condition is simple and easy to understand.
# Avoid using it for complex logic, as it can make the code harder to read and debug.
