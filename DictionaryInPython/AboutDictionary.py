# In Python, a dictionary is a collection of key-value pairs. Each key-value pair maps the key to its associated value, and the keys in a dictionary must be unique, immutable data types (like strings, numbers, or tuples), while the values can be of any type (including lists, other dictionaries, etc.).

# Dictionaries are defined using curly braces {}, with each key-value pair separated by a colon (:), and pairs are separated by commas.

# Syntax:

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Characteristics:
# Unordered: Before Python 3.7, dictionaries were unordered. Since Python 3.7, dictionaries maintain the insertion order.
# Mutable: You can change, add, or remove items.
# Key-Value Pairs: Each key has a unique value associated with it.

# Example:


my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'London'
}

# Common Dictionary Methods and Functions:
# dict(): Creates a new dictionary.


# new_dict = dict(name='Tom', age=25)
# len(dict): Returns the number of items (key-value pairs) in the dictionary.


# len(my_dict)  # Output: 3
# dict[key]: Accesses the value associated with the specified key. If the key does not exist, it raises a KeyError.


# my_dict['name']  # Output: 'John'
# dict.get(key[, default]): Returns the value associated with the key. If the key is not found, it returns None or the specified default value.


# my_dict.get('age')  # Output: 30
# my_dict.get('gender', 'Not found')  # Output: 'Not found'
# dict.keys(): Returns a view object that displays all the keys in the dictionary.


# my_dict.keys()  # Output: dict_keys(['name', 'age', 'city'])
# dict.values(): Returns a view object that displays all the values in the dictionary.


# my_dict.values()  # Output: dict_values(['John', 30, 'London'])
# dict.items(): Returns a view object that displays a list of key-value pairs in tuples.


# my_dict.items()  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'London')])
# dict.update([other_dict]): Updates the dictionary with the elements from another dictionary or iterable of key-value pairs.

# my_dict.update({'age': 31, 'job': 'Engineer'})
# # Updated dictionary: {'name': 'John', 'age': 31, 'city': 'London', 'job': 'Engineer'}
# dict.pop(key[, default]): Removes the key and returns its value. If the key is not found, it returns the specified default value, or raises a KeyError if no default is provided.


# my_dict.pop('age')  # Output: 30
# dict.popitem(): Removes and returns the last inserted key-value pair as a tuple. This method reflects the insertion order since Python 3.7.

# my_dict.popitem()  # Output: ('job', 'Engineer')
# dict.clear(): Removes all elements from the dictionary, leaving it empty.

# my_dict.clear()  # Output: {}
# dict.copy(): Returns a shallow copy of the dictionary.

# copy_dict = my_dict.copy()
# dict.fromkeys(seq[, value]): Creates a new dictionary with keys from the sequence seq and values set to value (which defaults to None).

# new_dict = dict.fromkeys(['name', 'age', 'city'], 'Unknown')
# # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# Additional Features:
# Membership Operators: You can check if a key exists in a dictionary using in.


# 'name' in my_dict  # Output: True
# Dictionary Comprehension: You can generate dictionaries using comprehension.


squares = {x: x*x for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Example Usage:

# Creating a dictionary
person = {'name': 'Alice', 'age': 28, 'city': 'Paris'}

# Accessing a value
print(person['name'])  # Output: Alice

# Updating a value
person['age'] = 29

# Adding a new key-value pair
person['job'] = 'Developer'

# Checking if a key exists
if 'name' in person:
    print('Name exists')

# Removing a key-value pair
person.pop('city')

# Dictionaries are incredibly useful in Python for storing and managing data in a flexible and efficient way!