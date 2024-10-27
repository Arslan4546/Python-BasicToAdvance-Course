# In Python, properties allow you to manage the access and modification of attributes more elegantly. The @property decorator lets you define methods that act like attributes. This provides control over how an attribute is accessed and modified without needing to change the way you use it.

# Here’s a breakdown with simple examples:

# 1. Basic Use of @property
# The @property decorator lets you create "getter" methods, allowing an attribute to be accessed like a variable.

# Example:

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Using a private attribute

    @property
    def celsius(self):
        return self._celsius  # Getter method

# Usage
temp = Temperature(25)
print(temp.celsius)  # Accessing as an attribute, outputs: 25


# Here:

# celsius is accessed like an attribute (temp.celsius), but it’s actually managed by a method under the hood.
# The underscore in _celsius indicates it’s intended for internal use only.


# 2. Using @property with a Setter
# The @property decorator can be paired with a setter method, which allows you to validate or modify the data before setting it.

# Example:


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

# Usage
temp = Temperature(25)
temp.celsius = 30        # Valid assignment
print(temp.celsius)      # Outputs: 30
# temp.celsius = -300    # Raises ValueError


# Here:

# @celsius.setter allows us to set celsius while ensuring that the temperature can’t go below absolute zero.
# The setter adds a layer of validation to prevent invalid values.
# 3. Using @property for Derived Attributes
# Properties can also be used to define derived attributes, which are calculated based on other attributes.

# Example:

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32  # Derived attribute

# Usage
temp = Temperature(25)
print(temp.celsius)      # Outputs: 25
print(temp.fahrenheit)   # Outputs: 77.0


# In this example:

# fahrenheit is a derived property calculated from celsius.
# We don’t need a separate attribute for fahrenheit; it’s computed dynamically.
# Summary
# @property creates a getter method that can be accessed like an attribute.
# Setter methods (using @property_name.setter) allow for controlled attribute modification.
# Properties can be used for derived attributes calculated on the fly.
# This lets you add logic to attribute access without changing the interface for interacting with the class.









