# "Clever" if statements are concise and creative ways to solve problems using conditional expressions. These often involve more advanced techniques like using the power of Python’s built-in functions, list comprehensions, or using conditions in ways that simplify the code while maintaining readability.

# Here are some examples of clever if statements in Python:

# Example 1: Assign Default Value if Variable is None

x = None
y = x if x is not None else 10
print(y)  # Output: 10

# Explanation:

# This checks if x is None, and if it is, assigns a default value (10) to y. If x had a value, y would take that instead.
# Example 2: Short-Circuit if (Avoiding Division by Zero


a = 10
b = 0
result = a / b if b != 0 else "Division by zero error"
print(result)  # Output: Division by zero error

# Explanation:

# This avoids a ZeroDivisionError by checking if b is zero before performing the division. If b is zero, a friendly error message is returned instead.
# Example 3: Toggle a Boolean Value


status = True
status = not status if status else status
print(status)  # Output: False

# Explanation:

# A clever way to toggle a boolean variable (status). If status is True, it will be toggled to False. If it’s already False, it remains the same.

# Example 4: Return Multiple Conditions in a Single Line

x = 7
result = "Negative" if x < 0 else "Zero" if x == 0 else "Positive"
print(result)  # Output: Positive

# Explanation:

# This is a multi-conditional expression in a single line. It checks if x is negative, zero, or positive, and returns the corresponding result. It combines multiple conditions into a concise expression.

# Example 5: Choose the Shortest List

list1 = [1, 2, 3]
list2 = [4, 5]
shortest_list = list1 if len(list1) < len(list2) else list2
print(shortest_list)  # Output: [4, 5]

# Explanation:

# This selects the list with the smallest length between list1 and list2. The condition checks the length of each list, and the shorter list is assigned to shortest_list.

# Example 6: Get the First Non-None Value (Null Coalescing)

a = None
b = None
c = 5
result = a or b or c
print(result)  # Output: 5

# Explanation:

# This is a clever way to find the first non-None (or truthy) value from a sequence of variables. It returns the first variable that is not None. In this case, since both a and b are None, c is returned.

# Example 7: List Comprehension with Conditional Check

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # Output: [2, 4, 6]

# Explanation:

# This uses a single-line if inside a list comprehension to filter only the even numbers from a list. It’s a concise way to apply conditional logic to each element in a list.

# Example 8: Multiple Variables in Single Conditional

a, b = 3, 7
result = "Both are even" if a % 2 == 0 and b % 2 == 0 else "At least one is odd"
print(result)  # Output: At least one is odd

# Explanation:

# This checks the parity (even or odd) of two variables, a and b. If both are even, it returns "Both are even", otherwise it returns "At least one is odd". It's a clean way to handle multiple conditions in a single line.

# Example 9: Choose a Discount Based on Age

age = 17
discount = 50 if age < 18 else 20
print(f"Discount: {discount}%")  # Output: Discount: 50%

# Explanation:

# This clever if checks a customer’s age and assigns a discount accordingly. If the customer is younger than 18, they get a 50% discount; otherwise, they get a 20% discount.

# Example 10: Swap Two Variables (Clever if Alternative)


a, b = 10, 20
a, b = (b, a) if a < b else (a, b)
print(a, b)  # Output: 20 10

# Explanation:

# A clever way to swap two variables using a single-line if statement. If a is less than b, their values are swapped. If not, their values remain unchanged.

# Example 11: Check for Palindrome in a Single Line

word = "radar"
is_palindrome = True if word == word[::-1] else False
print(is_palindrome)  # Output: True

# Explanation:

# This checks if a string is a palindrome (reads the same forwards and backwards) using slicing (word[::-1] to reverse the string). If the word matches its reverse, the condition returns True; otherwise, it returns False.

# Example 12: Return Custom Messages Based on Condition

score = 85
message = ("Excellent" if score >= 90 else "Good" if score >= 70 else "Needs Improvement")
print(message)  # Output: Good

# Explanation:

# A multi-level condition evaluates the score. If the score is 90 or above, it returns "Excellent", if 70 or above but less than 90, it returns "Good", and otherwise, "Needs Improvement".

# Example 13: Print Different Messages Based on Multiple Conditions

temperature = 25
clothing = "T-shirt" if temperature > 20 else "Jacket" if temperature > 10 else "Coat"
print(f"Wear a {clothing}")  # Output: Wear a T-shirt

# Explanation:

# This selects the appropriate clothing based on the temperature. If the temperature is greater than 20 degrees, it suggests a "T-shirt", otherwise "Jacket" or "Coat" depending on how cold it is.

# Example 14: Check Multiple Boolean Conditions with Single-Line if

is_raining = True
has_umbrella = False
can_go_out = "Stay at home" if is_raining and not has_umbrella else "Go out"
print(can_go_out)  # Output: Stay at home

# Explanation:

# This uses logical and and not to combine two boolean conditions. If it’s raining and you don’t have an umbrella, the result is "Stay at home". Otherwise, you can "Go out".

# Example 15: Assign Value Based on Multiple Numeric Conditions

speed = 85
speed_message = "Too Fast" if speed > 100 else "Fast" if speed > 60 else "Normal"
print(speed_message)  # Output: Fast

# Explanation:

# This checks the speed of a vehicle and assigns a message accordingly. If the speed is greater than 100, it says "Too Fast", if it’s over 60 but less than or equal to 100, it says "Fast", otherwise, it returns "Normal".

# Key Takeaways:
# Clever if statements often make code more concise and can handle multiple conditions elegantly in a single line.
# They are perfect for quick logic decisions where long-form if-else blocks might be overkill.
# However, readability is important. If the logic gets too complex, it’s better to stick to traditional if-else statements for clarity.





