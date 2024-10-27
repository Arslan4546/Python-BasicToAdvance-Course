# The del keyword in Python is used to delete objects, variables, or elements from lists and dictionaries. It doesn’t directly free memory but rather removes the reference to an object, allowing Python’s garbage collector to clean up when there are no more references.

# Here are some simple examples to illustrate the uses of del:

# 1. Deleting Variables
# You can use del to delete variables from the namespace, meaning they will no longer be accessible.


x = 10
print(x)  # Output: 10

del x
# print(x)  # This will raise an error because x is deleted


# 2. Deleting List Elements
# You can use del to remove specific elements from a list by index or delete slices of a list.

# Example: Deleting by Index

numbers = [1, 2, 3, 4, 5]
del numbers[2]  # Deletes the element at index 2
print(numbers)  # Output: [1, 2, 4, 5]


# Example: Deleting a Slice

numbers = [1, 2, 3, 4, 5]
del numbers[1:3]  # Deletes elements from index 1 to 2 (3 is not included)
print(numbers)  # Output: [1, 4, 5]


# 3. Deleting Dictionary Key-Value Pairs
# You can use del to delete specific key-value pairs from a dictionary.


person = {"name": "Alice", "age": 30, "city": "New York"}
del person["age"]
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}

# 4. Deleting Entire Structures
# Using del, you can delete an entire list, dictionary, or any other object. Once deleted, any attempt to access the structure will raise an error.


items = [10, 20, 30]
del items
# print(items)  # This will raise an error because 'items' is deleted


# Summary
# The del keyword in Python is versatile and can:

# Delete variables
# Remove specific elements or slices from lists
# Delete key-value pairs from dictionaries
# Delete entire data structures