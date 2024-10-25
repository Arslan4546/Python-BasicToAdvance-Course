# A for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or any other iterable object. This loop repeats a block of code for each item in the sequence until it reaches the end.

# Here's the basic syntax of a for loop in Python:


# for item in sequence:
    # Code to execute for each item

# Simple Example
# Let's start with a basic example to understand how a for loop works.

# Example 1: Iterating over a list of numbers
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

# Explanation:

# The loop goes through each item in the numbers list.
# Each item (or num) in the list is printed.


# Output:


# 1
# 2
# 3
# 4
# 5
# This loop stops when it has gone through all items in the list.

# Looping with the range() Function
# The range() function can generate a sequence of numbers, which is often used in loops when you want to repeat something a specific number of times.


# Example 2: Looping with range

# for i in range(5):
#     print("Iteration:", i)
# Explanation:

# range(5) generates numbers from 0 to 4 (5 numbers in total).
# The loop prints each number, showing the current iteration.

# Output:

# makefile

# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4

# Complex Example: Nested for Loops
# Let's look at a more advanced example with nested for loops, which are loops within loops.

# Example 3: Multiplication table using nested for loops

for i in range(1, 4):  # Outer loop for rows (1 to 3)
    for j in range(1, 4):  # Inner loop for columns (1 to 3)
        print(f"{i} * {j} = {i * j}")
    print()  # Blank line after each row


# Explanation:

# The outer loop runs for each row (from 1 to 3).
# For each iteration of the outer loop, the inner loop multiplies i by each value of j (from 1 to 3).
# The result is printed, and a blank line separates each row for readability.
# Output:


1 * 1 = 1
1 * 2 = 2
1 * 3 = 3

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9

# More Complex Example: Looping through a Dictionary
# You can use a for loop to iterate over dictionary keys and values.


# Example 4: Looping through a dictionary
student_scores = {
    'Alice': 85,
    'Bob': 78,
    'Clara': 92
}

# for name, score in student_scores.items():
#     print(f"{name} scored {score}")
# Explanation:

# The .items() method returns both the key and the value from the dictionary, allowing you to unpack each key-value pair as name and score.
# The loop prints each student’s name and their score.
# Output:


# Alice scored 85
# Bob scored 78
# Clara scored 92
# Complex Example: Using for Loop with break and continue
# You can control a loop’s behavior with break (to exit the loop) and continue (to skip to the next iteration).

# Example 5: Breaking and Continuing in a loop
for i in range(10):
    if i == 5:
        break  # Exit the loop completely when i is 5
    elif i % 2 == 0:
        continue  # Skip this iteration if i is even
    print(i)


# Explanation:

# The loop iterates from 0 to 9.
# If i equals 5, break exits the loop entirely.
# If i is even (divisible by 2), continue skips the current iteration.
# Output:


# 1
# 3
# Explanation of Output: Only odd numbers less than 5 are printed because:

# The continue statement skips even numbers.
# The break statement exits the loop when i reaches 5.