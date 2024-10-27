# In Python, a constructor is a special method that is automatically called when an object is created. The purpose of a constructor is to initialize the object's attributes with specific values or perform any setup actions needed when an object is instantiated.

# The __init__ Method
# The constructor in Python is the __init__ method. It's a built-in method that Python recognizes as the initializer for a class. When you create a new instance of a class, Python automatically calls __init__.

# Syntax: The __init__ method is defined with the name __init__ and always takes self as its first parameter, which represents the instance being created.


# Example:

class Student:
    def __init__(self, name, age):
        self.name = name  # Assigning the name attribute
        self.age = age    # Assigning the age attribute

# Creating an instance of the Student class
student1 = Student("Alice", 20)
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20



# In this example:

# __init__ takes name and age as parameters in addition to self.
# self.name and self.age assign the values to instance attributes.
# When Student("Alice", 20) is called, Python automatically runs __init__, initializing student1 with name set to "Alice" and age set to 20.
# Key Points About Constructors in Python
# Automatic Initialization: The __init__ method runs automatically whenever a new object of the class is created.

# Parameter Flexibility: The constructor can take any number of parameters. Additional parameters allow you to initialize attributes with specific values when the object is created.

# Optional Parameters: Constructors can include default values for parameters, making some arguments optional.


class Car:
    def __init__(self, color="White", brand="Toyota"):
        self.color = color
        self.brand = brand

car1 = Car()                 # Uses default values
car2 = Car("Red", "Ford")    # Uses provided values

print(car1.color)  # Output: White
print(car2.color)  # Output: Red


# Single Constructor Method: Python classes can have only one __init__ method, as multiple __init__ methods are not supported. However, you can set default values or use conditional logic within __init__ to handle different initialization scenarios.

# The constructor is essential in Python for ensuring that an object’s state is properly set up from the start, making it a foundational part of working with classes and objects.