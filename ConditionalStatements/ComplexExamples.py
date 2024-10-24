# Complex Conditional with Logical Operators
# This program determines if a person can vote based on age and citizenship.


def can_vote(age, citizenship):
    if age >= 18 and citizenship == "yes":
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Using the function
age = 20
citizenship = "yes"
eligibility = can_vote(age, citizenship)
print(eligibility)  # Output: You are eligible to vote.

# Explanation:

# This example uses a logical operator (and) to check multiple conditions: the person must be at least 18 years old and a citizen to be eligible to vote.
# Example 4: Checking for Leap Year (A More Complex Example)
# This program checks if a year is a leap year.


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Using the function
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")  # Output: 2024 is a leap year.

# Explanation:

# This program checks if a year is divisible by 4 (leap year rule) and further narrows down using the 100 and 400 divisibility rules (specific conditions for leap years).
# Example 5: Password Validator (Using Multiple Conditions)
# This program checks if a password meets certain criteria: it must be at least 8 characters long, contain a number, and have both uppercase and lowercase letters.

def validate_password(password):
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
        return "Password is valid."
    else:
        return "Password is invalid."

# Using the function
password = "Pass1234"
validation_result = validate_password(password)
print(validation_result)  # Output: Password is valid.

# Explanation:

# This example uses multiple conditions (len(password) >= 8, any(char.isdigit()), any(char.isupper()), and any(char.islower())) combined with and operators to check if the password is valid.

# Example 6: Bank Withdrawal System (Advanced Example)
# This program simulates a bank system that checks whether the user has enough balance to withdraw money.


def bank_withdrawal(balance, amount):
    if amount <= balance:
        balance -= amount
        return f"Withdrawal successful! Your remaining balance is {balance}."
    else:
        return "Insufficient balance."

# Using the function
current_balance = 1000
withdraw_amount = 500
transaction_result = bank_withdrawal(current_balance, withdraw_amount)
print(transaction_result)  # Output: Withdrawal successful! Your remaining balance is 500.

# Explanation:

# The program checks if the withdrawal amount is less than or equal to the current balance before proceeding. If not, it returns a message indicating insufficient funds.
# Conditional Statements in Daily Life Problems


# Traffic Light:

# If the light is green, drive.
# Else if the light is yellow, prepare to stop.
# Else, stop the car.


traffic_light = "red"
if traffic_light == "green":
    print("Drive.")
elif traffic_light == "yellow":
    print("Prepare to stop.")
else:
    print("Stop the car.")

# Online Shopping:

# If the item is in stock, place the order.
# Else, add the item to the wishlist.

in_stock = True
if in_stock:
    print("Place the order.")
else:
    print("Add to wishlist.")


# Conclusion
# Conditional statements are essential in programming because they allow the program to make decisions based on various conditions. In daily life, we use these decisions constantly (e.g., based on the weather, traffic, or budget). In Python, the if, elif, and else statements allow for flexible and powerful control over program execution based on conditions. By combining these with logical and comparison operators, you can create both simple and complex decision-making structures in your code.