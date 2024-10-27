# In Python, a class method is a method that’s bound to the class itself, rather than an instance of the class. This means it can access or modify the class state across all instances, rather than the specific data of a single instance. Class methods are created using the @classmethod decorator and always take cls as their first parameter, which represents the class.

# Key Points of Class Methods
# A class method can access and modify class attributes (shared by all instances).
# Class methods can be called on the class itself, without creating an instance.
# They are commonly used for factory methods (methods that return a new instance of the class).
# Example 1: Modifying a Class Attribute

class Dog:
    species = "Canis lupus familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

# Calling the class method without creating an instance
Dog.change_species("Canis familiaris")

# Creating instances to check the updated class attribute
dog1 = Dog("Buddy")
print(dog1.species)  # Output: Canis familiaris

dog2 = Dog("Max")
print(dog2.species)  # Output: Canis familiaris

# In this example:

# species is a class attribute.
# change_species is a class method that allows modifying the species attribute across all instances of the Dog class.
# Example 2: Using a Class Method as a Factory Method
# Class methods are often used to provide alternate constructors, allowing for multiple ways to create an instance.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2023 - birth_year
        return cls(name, age)  # Creates and returns a new instance of Person

# Creating a Person instance using the class method
person1 = Person.from_birth_year("Alice", 1995)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 28


# In this example:

# from_birth_year is a class method that calculates the age based on the birth year and then creates a new instance of Person.