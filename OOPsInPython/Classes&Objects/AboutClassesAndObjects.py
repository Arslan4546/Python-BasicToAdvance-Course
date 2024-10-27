# What is a Class?
# A class is a blueprint or template used to create objects. It defines the properties and behaviors that the objects created from it will have. Classes organize data and functions in a structured way, enabling us to work with them as one unit.


class ClassName:
    # Class attributes and methods here
    pass

# Example of a Class

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer method to create instance attributes
    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute

    # Method to describe the dog
    def description(self):
        return f"{self.name} is {self.age} years old."
    


# In this example:

# Dog is the class name.
# species is a class attribute (shared by all dogs).
# name and age are instance attributes (unique to each dog).
# description is a method that operates on the instance attributes.
# What is an Object?
# An object is an instance of a class. When a class is defined, no memory or storage is allocated until an object of that class is created. Each object has:

# Its own unique data (defined by instance attributes).
# Access to class attributes and methods defined in the class.
# Creating Objects
# To create an object, we simply call the class as if it were a function.


dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

# Here:

# dog1 and dog2 are two objects (or instances) of the Dog class.
# dog1.name is "Buddy" and dog1.age is 5.
# dog2.name is "Milo" and dog2.age is 3.
# Each object can access its own data and methods defined in the class.

# Accessing Object Data and Methods

# print(dog1.description())  # Outputs: Buddy is 5 years old.
# print(dog2.description())  # Outputs: Milo is 3 years old.


# Summary
# Class: A blueprint defining common properties and behaviors. It defines what attributes and methods the objects created from it will have.
# Object: An instance of a class, with its own specific data based on the class’s blueprint.
# Classes and objects allow Python programs to be more modular, organized, and closer to real-world representations by grouping related data and behavior.