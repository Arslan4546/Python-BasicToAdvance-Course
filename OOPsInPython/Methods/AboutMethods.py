# In Python, methods are functions defined inside a class that describe the behaviors or actions that objects of that class can perform. They allow interaction with the object’s data (attributes) and help manage and manipulate it.

# Types of Methods in Python
# Instance Methods
# Class Methods
# Static Methods
# Let’s break down each type with details and examples.

# 1. Instance Methods
# Definition: Instance methods are the most common methods, and they are used to perform operations that utilize or modify the instance’s data (attributes).
# Accessing: These methods have access to both instance attributes and class attributes.
# Syntax: The first parameter of an instance method is always self, which represents the specific instance calling the method.


# Example

class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Creating an instance of Student
student1 = Student("Alice", 21)
student1.display_info()  # Output: Student Name: Alice, Age: 21



# In this example:

# display_info is an instance method that uses self to access the instance’s name and age.




# 2. Class Methods

# Definition: Class methods are methods that work with the class itself rather than with instances of the class. They are commonly used to access or modify class-level data, which is shared among all instances of the class.
# Accessing: Instead of self, class methods take cls as their first parameter, representing the class itself.
# Syntax: Class methods are defined with the @classmethod decorator.

# Example

class Student:
    # Class attribute
    school_name = "Greenwood High School"

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

# Accessing class method
Student.change_school_name("Blue Ridge School")
print(Student.school_name)  # Output: Blue Ridge School


# In this example:

# change_school_name is a class method that changes the class attribute school_name.
# The @classmethod decorator tells Python this is a class method, not an instance method.


# 3. Static Methods

# Definition: Static methods are methods that don’t modify class or instance data and typically perform independent operations related to the class.
# Accessing: They don’t take self or cls as parameters because they don’t operate on instance or class-level attributes.
# Syntax: Static methods are defined with the @staticmethod decorator.


# Example


class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Accessing static method
result = MathOperations.add(5, 10)
print(result)  # Output: 15


# In this example:

# add is a static method that performs addition without using any class or instance data.
# The @staticmethod decorator tells Python it’s a static method.
# Summary
# Instance Methods: Operate on instance data; take self as the first parameter.
# Class Methods: Operate on class data; take cls as the first parameter, and are marked with @classmethod.
# Static Methods: Perform independent operations that don't use instance or class data, and are marked with @staticmethod.
# Each method type serves a specific role in managing and utilizing the data within a class.






