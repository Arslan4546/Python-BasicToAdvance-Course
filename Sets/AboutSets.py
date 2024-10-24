# In Python, a set is an unordered collection of unique elements. Sets are mutable, meaning you can modify them after their creation by adding or removing elements. However, the elements themselves must be immutable (e.g., strings, numbers, or tuples). Sets are defined using curly braces {} or the set() function.

# Key Characteristics of Sets:
# Unordered: There is no defined order of elements in a set.
# Unique elements: A set cannot contain duplicate elements.
# Mutable: You can add or remove elements from a set after it is created.
# Creating Sets:
# You can create a set using either curly braces {} or the set() function.


# Using curly braces
my_set = {1, 2, 3, 4}

# Using set() function
another_set = set([1, 2, 3, 4])
# Set Functions and Methods in Python:
# Below is a list of all the common functions and methods you can use with sets.

# 1. add()
# Description: Adds an element to the set.
# Syntax: set.add(element)

# Example:

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# 2. update()
# Description: Adds multiple elements (from another set, list, or tuple) to the set.
# Syntax: set.update(iterable)

# Example:

my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# 3. remove()
# Description: Removes a specified element from the set. Raises a KeyError if the element is not found.
# Syntax: set.remove(element)
# Example:

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}


# 4. discard()
# Description: Removes a specified element from the set, but does not raise an error if the element is not found.
# Syntax: set.discard(element)
# Example:

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

my_set.discard(4)  # No error even though 4 is not in the set

# 5. pop()
# Description: Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# Syntax: set.pop()
# Example:

my_set = {1, 2, 3}
removed_element = my_set.pop()
print(removed_element)  # Output could be any element (since sets are unordered)

# 6. clear()
# Description: Removes all elements from the set, making it an empty set.
# Syntax: set.clear()
# Example:

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# 7. union()
# Description: Returns a new set with all elements from both sets (duplicates are removed).
# Syntax: set1.union(set2)
# Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}

# 8. intersection()
# Description: Returns a new set with only the elements that are common in both sets.
# Syntax: set1.intersection(set2)
# Example:

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}

# 9. difference()
# Description: Returns a new set with elements in the first set but not in the second set.
# Syntax: set1.difference(set2)
# Example:

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}

# 10. symmetric_difference()
# Description: Returns a new set with elements in either of the sets but not in both (i.e., the elements that are in one set or the other but not both).
# Syntax: set1.symmetric_difference(set2)
# Example:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 4, 5}

# 11. issubset()
# Description: Checks if the first set is a subset of the second set (i.e., if all elements of the first set exist in the second set).
# Syntax: set1.issubset(set2)
# Example:

set1 = {1, 2}
set2 = {1, 2, 3}
result = set1.issubset(set2)
print(result)  # Output: True

# 12. issuperset()
# Description: Checks if the first set is a superset of the second set (i.e., if it contains all elements of the second set).
# Syntax: set1.issuperset(set2)
# Example:

set1 = {1, 2, 3}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True

# 13. isdisjoint()
# Description: Checks if two sets have no elements in common.
# Syntax: set1.isdisjoint(set2)
# Example:

set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True

# 14. copy()
# Description: Returns a shallow copy of the set.
# Syntax: set.copy()
# Example:

my_set = {1, 2, 3}
copy_set = my_set.copy()
print(copy_set)  # Output: {1, 2, 3}

# 15. len()
# Description: Returns the number of elements in the set.
# Syntax: len(set)
# Example:

# my_set = {1, 2, 3}
# print(len(my_set))  # Output: 3
# These functions and methods provide powerful tools for working with sets in Python, making it easier to handle tasks such as eliminating duplicates, performing mathematical set operations, and more.