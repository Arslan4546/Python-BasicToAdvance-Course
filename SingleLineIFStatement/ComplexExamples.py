# Complex Example 7: Determine if a Year is a Leap Year (Single Line)

year = 2024
is_leap_year = True if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else False
print(f"{year} is a leap year: {is_leap_year}")  # Output: 2024 is a leap year: True

# Explanation:

# The condition checks if the year is divisible by 4 and either not divisible by 100, or divisible by 400. This is the rule for determining leap years.
# Complex Example 8: Find the Largest of Three Numbers (Single Line)

a = 10
b = 15
c = 12
largest = a if a > b and a > c else b if b > c else c
print(f"The largest number is {largest}")  # Output: The largest number is 15

# Explanation:

# The condition compares three numbers. If a is greater than both b and c, a is assigned as the largest; if not, it checks if b is greater than c. If neither condition is true, c is the largest.

# Single-line if statements provide a clean and efficient way to handle conditional expressions. They are highly useful for situations where you want to make quick decisions without writing long, multiline if-else blocks. However, they should be used with caution to maintain code readability.






