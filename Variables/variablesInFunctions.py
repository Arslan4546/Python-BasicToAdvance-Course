# Example 1: Simple Addition Function
# This program takes two numbers as input and returns their sum.


def add_numbers(num1, num2):
    result = num1 + num2  # sum of num1 and num2
    return result

# Using the function
a = 10
b = 5
sum_result = add_numbers(a, b)
print(f"The sum of {a} and {b} is {sum_result}")  # Output: The sum of 10 and 5 is 15

# Explanation:

# The function add_numbers accepts two parameters num1 and num2, adds them, and returns the result. The variables a and b are passed to the function when it's called.

# Example 2: Calculate Area of a Rectangle
# This function calculates the area of a rectangle using its length and width.

def calculate_area(length, width):
    area = length * width  # area formula
    return area

# Using the function
length = 5
width = 3
rectangle_area = calculate_area(length, width)
print(f"The area of the rectangle is {rectangle_area} square units.")  # Output: The area of the rectangle is 15 square units.

# Explanation:

# The function calculate_area computes the area using the formula length * width, with variables passed when calling the function.

# Example 3: Greeting Function with Multiple Parameters
# This program greets a person using their first and last names.

def greet_person(first_name, last_name):
    greeting = f"Hello, {first_name} {last_name}!"
    return greeting

# Using the function
first = "Arslan"
last = "Tariq"
greeting_message = greet_person(first, last)
print(greeting_message)  # Output: Hello, Arslan Raza!

# Explanation:

# The function greet_person takes two variables (first_name and last_name) and combines them into a greeting message.

# Example 4: Find Maximum of Three Numbers
# This program finds the maximum of three numbers.


def find_max(num1, num2, num3):
    max_num = max(num1, num2, num3)  # using Python's built-in max() function
    return max_num

# Using the function
x = 10
y = 15
z = 5
maximum_value = find_max(x, y, z)
print(f"The maximum of {x}, {y}, and {z} is {maximum_value}.")  # Output: The maximum of 10, 15, and 5 is 15.

# Explanation:

# The function find_max takes three variables, uses the built-in max() function to find the largest number, and returns the result.

# Example 5: Check Even or Odd
# This function checks if a number is even or odd.


def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Using the function
num = 9
result = check_even_odd(num)
print(result)  # Output: 9 is odd.

# Explanation:

# The check_even_odd function checks if a number is divisible by 2 using the modulus operator %. It then returns whether the number is even or odd.

# Example 6: Calculate Compound Interest
# This program calculates compound interest using a function.


def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / n) ** (n * time)  # compound interest formula
    return amount

# Using the function
principal_amount = 1000
interest_rate = 0.05  # 5% interest rate
time_period = 5  # 5 years
compoundings_per_year = 12  # compounded monthly

final_amount = calculate_compound_interest(principal_amount, interest_rate, time_period, compoundings_per_year)
print(f"The final amount after {time_period} years is {final_amount:.2f}")  # Output: The final amount after 5 years is 1283.36

# Explanation:

# The calculate_compound_interest function uses the formula for compound interest, takes variables for principal, rate, time, and number of times compounded, and calculates the final amount.

# Example 7: FizzBuzz Function
# A classic FizzBuzz problem where the function prints "Fizz" if a number is divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Using the function
number = 15
fizz_buzz(number)

# Explanation:

# The fizz_buzz function iterates through numbers from 1 to n and checks for divisibility by 3 and 5. It prints the appropriate response based on the conditions.