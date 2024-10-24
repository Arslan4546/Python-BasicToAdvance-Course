# Conditional Statements in Python
# Conditional statements allow you to execute a block of code based on whether a condition is True or False. They form the core of decision-making in programming and are used to control the flow of the program. Python uses the if, elif (else if), and else statements for conditional logic.

# Daily Life Example of Conditionals
# Think about making a decision like deciding what to wear based on the weather:

# If it is raining, you take an umbrella.
# Else if it's cold, you wear a jacket.
# Else, you wear regular clothes.
# This is a real-life example of how conditionals are used to guide decisions based on conditions.

# Syntax of Conditional Statements

# if condition:
#     # block of code executed if condition is True
# elif another_condition:
#     # block of code executed if another_condition is True
# else:
#     # block of code executed if no conditions are True

# Example in Code (Daily Life Decision)

weather = "rainy"

if weather == "rainy":
    print("Take an umbrella.")
elif weather == "cold":
    print("Wear a jacket.")
else:
    print("Wear regular clothes.")

# Conditional Operators
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Examples of Conditional Statements
# Example 1: Simple If-Else Statement
# This program checks if a number is positive or negative.


def check_number(number):
    if number > 0:
        return "The number is positive."
    else:
        return "The number is negative."


# Using the function
num = -5
result = check_number(num)
print(result)  # Output: The number is negative.

# Explanation:

# If number is greater than 0, it is positive. Otherwise, it's negative.
# Example 2: Nested If-Else (Checking Grades)
# This program checks a student's grade based on their score.

def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Using the function
student_score = 85
grade = check_grade(student_score)
print(f"The student's grade is {grade}")  # Output: The student's grade is B

# Explanation:

# The program uses elif (else if) to check multiple conditions. If none of the conditions are met, the else block executes, assigning a grade of F.