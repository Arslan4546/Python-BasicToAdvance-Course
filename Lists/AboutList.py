# List in Python
# A list is one of Python's most versatile and commonly used data structures. It is an ordered collection of items, which can be of different types (integers, strings, floats, etc.). Lists are mutable, meaning that the items within the list can be changed after the list is created.

# Key Properties of Lists:

# Ordered: Lists maintain the order of the items.
# Mutable: You can modify (add, update, remove) elements in the list.
# Allows Duplicates: Lists can store multiple occurrences of the same item.

# Syntax:

my_list = [1, 2, 'apple', 3.5, True]

# List Methods in Python
# Below is a comprehensive list of methods available for lists in Python, along with explanations and examples.

# 1. append()
# Description: Adds an element to the end of the list.
# Syntax: list.append(item)
# Example:

fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 2. extend()
# Description: Extends the list by appending elements from another iterable (like another list, tuple, or string).
# Syntax: list.extend(iterable)
# Example:

fruits = ['apple', 'banana']
fruits.extend(['cherry', 'orange'])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 3. insert()
# Description: Inserts an element at a specified position.
# Syntax: list.insert(index, item)
# Example:

fruits = ['apple', 'banana']
fruits.insert(1, 'cherry')
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# 4. remove()
# Description: Removes the first occurrence of the specified value.
# Syntax: list.remove(item)
# Example:

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry']

# 5. pop()
# Description: Removes and returns the item at the specified index (or the last item if the index is not provided).
# Syntax: list.pop([index])
# Example:

fruits = ['apple', 'banana', 'cherry']
item = fruits.pop(1)
print(item)    # Output: 'banana'
print(fruits)  # Output: ['apple', 'cherry']

# 6. clear()
# Description: Removes all elements from the list.
# Syntax: list.clear()
# Example:

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # Output: []

# 7. index()
# Description: Returns the index of the first occurrence of the specified value.
# Syntax: list.index(item, [start, end])
# Example:

fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1

# 8. count()
# Description: Returns the number of occurrences of a specified value.
# Syntax: list.count(item)
# Example:

fruits = ['apple', 'banana', 'apple', 'cherry']
count = fruits.count('apple')
print(count)  # Output: 2

# 9. sort()
# Description: Sorts the list in ascending order (or descending if specified).

# Syntax: list.sort([key=None, reverse=False])

# Example:

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

# For descending order:

numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]

# 10. reverse()
# Description: Reverses the elements of the list.
# Syntax: list.reverse()
# Example:

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# 11. copy()
# Description: Returns a shallow copy of the list.
# Syntax: list.copy()
# Example:

fruits = ['apple', 'banana', 'cherry']
new_list = fruits.copy()
print(new_list)  # Output: ['apple', 'banana', 'cherry']

# List Slicing (Not a method, but a useful technique)
# Lists can be sliced using the following syntax:


# list[start:stop:step]
# start: Starting index (inclusive)
# stop: Ending index (exclusive)
# step: The amount to step through the list
# Example:


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])      # Output: [2, 3, 4, 5]
print(numbers[::2])      # Output: [0, 2, 4, 6, 8]

# Conclusion
# Python lists are highly flexible and come with a range of methods that allow you to manipulate them efficiently. Whether you're adding, removing, or searching for elements, lists are fundamental to Python programming and are essential for managing collections of data.