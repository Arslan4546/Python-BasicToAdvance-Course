# In Python, there isn’t a built-in do-while loop like in some other languages. However, the same behavior can be replicated using a while loop. A do-while loop is a control flow statement that executes a block of code at least once and then repeatedly executes the block, as long as a specified condition remains true.

# Concept of Do-While Loop
# The key feature of a do-while loop is that the code inside the loop runs at least once, regardless of whether the condition is True or False. After the first execution, the loop will continue to run if the condition evaluates to True.

# In Python, we can mimic this by:

# Using a while loop.
# Placing the condition check at the end of the loop using a break statement.
# Basic Structure (Pseudo-code for a Do-While loop)

# while True:
    # Loop body (code to be executed)
    
#     if not condition:
#         break
# The loop will:

# Execute the code inside it at least once.
# Check if the condition is True to continue or False to exit.
# Example 1: Simple Example of Mimicking a Do-While Loop
# Let’s consider a simple scenario where we want the user to enter a number between 1 and 10. We will prompt the user at least once and keep asking until they provide a valid input.

# while True:
#     number = int(input("Enter a number between 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thank you!")
#         break
#     else:
#         print("Invalid number, please try again.")


# Explanation
# The code prompts the user to enter a number at least once.
# If the number is between 1 and 10, it thanks the user and exits the loop.
# If the number is outside the range, it displays an error message and asks the user again.
# Example 2: Complex Example with Calculation
# Let’s look at a more complex scenario where we want to calculate the factorial of a number, but only allow the user to enter positive integers. We’ll keep prompting the user to enter a valid number until they do so.


# while True:
#     number = int(input("Enter a positive integer to calculate its factorial: "))
    
#     # Check if the number is positive
#     if number > 0:
#         # Calculate factorial
#         factorial = 1
#         for i in range(1, number + 1):
#             factorial *= i
#         print(f"The factorial of {number} is {factorial}")
#         break
#     else:
#         print("Please enter a positive integer.")
# Explanation
# This loop prompts the user for a positive integer, ensuring they’ll be asked at least once.
# If the user enters a positive integer, it calculates the factorial and displays it.
# If the user enters a non-positive number, it displays an error message and prompts again.
# Example 3: Mimicking a Do-While Loop with a Countdown
# In this example, let’s create a countdown where we start at a specified number and count down to zero.


# count = 5  # Starting number for countdown

# while True:
#     print(f"Countdown: {count}")
#     count -= 1  # Decrease count by 1 each loop

#     # Break the loop once count reaches zero
#     if count < 0:
#         break


# Explanation

# The countdown starts at 5 and decreases by 1 with each loop iteration.
# Since the while loop is True, it runs at least once.
# When count reaches below zero, the break statement stops the loop.
# In summary, by using a while True loop with a conditional break, we can mimic the do-while structure in Python, ensuring the loop’s body runs at least once before checking the condition. This approach is flexible and works for both simple and complex scenarios.






