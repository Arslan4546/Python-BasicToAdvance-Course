# Encapsulation in Python is an Object-Oriented Programming (OOP) concept that bundles data (attributes) and methods (functions) that operate on that data within a single unit, known as a class. Encapsulation helps protect an object's internal state and behavior, restricting access to certain details and only allowing interaction through defined interfaces.

# In Python, encapsulation is primarily implemented through:

# Public Members: Accessible from outside the class.
# Protected Members: Indicated with a single underscore _, suggesting they should not be accessed directly (convention only).
# Private Members: Indicated with a double underscore __, making them inaccessible directly from outside the class.
# Let’s go through each with examples.

# 1. Public Members
# Public members are accessible from outside the class. Any attribute or method without an underscore is considered public.


class Person:
    def __init__(self, name, age):
        self.name = name   # Public attribute
        self.age = age     # Public attribute

    def display_info(self):   # Public method
        print(f"Name: {self.name}, Age: {self.age}")



# Example usage
person = Person("Alice", 30)
print(person.name)            # Accessing public attribute directly
person.display_info()         # Calling public method


# Output:


# Alice
# Name: Alice, Age: 30
# Here, name and age are public attributes, and display_info is a public method, meaning they can be accessed directly from outside the class.

# 2. Protected Members
# Protected members are indicated with a single underscore _ prefix. This is a convention that suggests they should not be accessed directly from outside the class, but it’s not enforced by Python.


class Person:
    def __init__(self, name, age):
        self._name = name   # Protected attribute
        self._age = age     # Protected attribute

    def _display_info(self):   # Protected method
        print(f"Name: {self._name}, Age: {self._age}")

# Example usage
person = Person("Bob", 25)
print(person._name)           # Accessing protected attribute (not recommended)
person._display_info()        # Calling protected method (not recommended)


# Though accessible, accessing _name and _display_info directly is discouraged. By convention, they are meant to be used only within the class or by subclasses.

# 3. Private Members
# Private members are indicated with a double underscore __ prefix, making them inaccessible from outside the class. This provides stronger encapsulation.


class Person:
    def __init__(self, name, age):
        self.__name = name   # Private attribute
        self.__age = age     # Private attribute

    def __display_info(self):   # Private method
        print(f"Name: {self.__name}, Age: {self.__age}")

    # Public method to access private data
    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Example usage
person = Person("Charlie", 40)
# print(person.__name)       # Error: can't access private attribute
person.get_info()            # Correct way to access private data

# Output:


# Name: Charlie, Age: 40
# In this example:

# __name and __age are private attributes and cannot be accessed directly from outside the class.
# get_info is a public method that provides controlled access to these private attributes.
# Attempting to access __name directly would raise an error. Private members are used to hide sensitive information and only allow controlled access through public methods.






