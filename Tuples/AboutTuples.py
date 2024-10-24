# Concept of Tuples in Python
# A tuple is a data structure in Python that is used to store multiple items in a single variable. Tuples are similar to lists but with one key difference: tuples are immutable, meaning that once they are created, their elements cannot be changed. Tuples are defined by placing the elements inside parentheses () and separating them with commas.

# Characteristics of Tuples:
# Immutable: Cannot modify, add, or remove elements after creation.
# Ordered: Elements have a defined order, which will not change.
# Allows Duplicates: A tuple can have items with the same value.
# Can store different data types: Elements of different types (e.g., strings, integers, etc.) can be stored in a tuple.

# Example of Tuple:

# my_tuple = (1, "hello", 3.14, True)
# You can access elements in a tuple using indexing, slicing, and other methods similar to lists.

# Advantages of Tuples:
# Faster than lists: Since they are immutable, Python can optimize their performance.
# Used as keys in dictionaries: Since tuples are immutable, they can be used as dictionary keys, whereas lists cannot.
# List Methods in Python
# A list in Python is a mutable, ordered sequence of items. Lists can store items of different types and allow operations like adding, removing, and modifying elements. Lists are defined using square` brackets [].

# Below are common list methods:

# append():

# Adds an element to the end of the list.
# Example:

my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]

# extend():

# Adds all elements of an iterable (list, tuple, etc.) to the end of the list.
# Example:

my_list = [1, 2, 3]
my_list.extend([4, 5])  # [1, 2, 3, 4, 5]

# insert():

# Inserts an element at a specified position.

my_list = [1, 2, 3]
my_list.insert(1, "a")  # [1, 'a', 2, 3]

# remove():

# Removes the first occurrence of a specified element.
# Example:

my_list = [1, 2, 3, 2]
my_list.remove(2)  # [1, 3, 2]

# pop():

# Removes and returns the element at the specified position. If no index is specified, it removes and returns the last element.
# Example:

my_list = [1, 2, 3]
my_list.pop()  # 3, list becomes [1, 2]
my_list.pop(0)  # 1, list becomes [2]

# clear():

# Removes all elements from the list, making it empty.
# Example:

my_list = [1, 2, 3]
my_list.clear()  # []

# index():

# Returns the index of the first occurrence of a specified element. Raises an error if the element is not found.
# Example:

my_list = [1, 2, 3]
index_of_2 = my_list.index(2)  # 1

# count():

# Returns the number of times a specified element occurs in the list.
# Example:

my_list = [1, 2, 3, 2, 2]
count_of_2 = my_list.count(2)  # 3

# sort():

# Sorts the elements of the list in ascending or descending order. The sort happens in-place.
# Example:

my_list = [3, 1, 2]
my_list.sort()  # [1, 2, 3]
my_list.sort(reverse=True)  # [3, 2, 1]

# reverse():

# Reverses the elements of the list in-place.
# Example:

my_list = [1, 2, 3]
my_list.reverse()  # [3, 2, 1]

# copy():

# Returns a shallow copy of the list.

# Example:

my_list = [1, 2, 3]
new_list = my_list.copy()  # [1, 2, 3]

# list comprehension:

# Although not a method, list comprehension is a powerful technique to generate or modify lists.

# Example:

# squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
# Example of Lists with Methods:

# my_list = [10, 20, 30, 40]

# Append 50 to the list
my_list.append(50)  # [10, 20, 30, 40, 50]

# Insert 25 at index 2
my_list.insert(2, 25)  # [10, 20, 25, 30, 40, 50]

# Remove the first occurrence of 20
my_list.remove(20)  # [10, 25, 30, 40, 50]

# Reverse the list
my_list.reverse()  # [50, 40, 30, 25, 10]

# Sort the list in ascending order
my_list.sort()  # [10, 25, 30, 40, 50]

# Clear the list
# my_list.clear()  # []
# Both tuples and lists are versatile, but the choice between them depends on whether you need mutability (choose lists) or immutability (choose tuples).