# In Python, a static method is a method inside a class that doesn't require access to either the instance (self) or the class (cls). Static methods are defined using the @staticmethod decorator, and they can be called on the class itself or on its instances without affecting the class or instance state. They are generally used for utility functions related to the class but don't need to access or modify any class or instance variables.

# Key Points about Static Methods
# No Access to self or cls: Static methods do not receive the self or cls parameters. This means they can't access or modify instance attributes or class attributes.
# Namespace Convenience: Although they don't interact with the instance or class, static methods are logically grouped with the class. This keeps the related functionality in one place, even if the method does not alter the state of the class.
# Utility Functions: They are typically used for operations that make sense to perform in the context of the class but don't need any information about specific instances.
# How to Define and Use Static Methods
# To define a static method, use the @staticmethod decorator above the method definition. Here's an example:


class MathUtility:
    # Static method for a general mathematical operation
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Using the static method
result = MathUtility.add_numbers(5, 10)  # Output: 15
print(result)

# In this example:

# add_numbers is a static method that takes two parameters, a and b, and returns their sum.
# This method can be called directly on the MathUtility class without creating an instance of the class.
# Example with Real-world Context
# Static methods are especially useful for class-related tasks that don't involve specific instances. For instance, suppose you have a TemperatureConverter class that can convert between Fahrenheit and Celsius.


class TemperatureConverter:
    # Static method for converting Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    # Static method for converting Fahrenheit to Celsius
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Using static methods without instantiating the class
temp_f = TemperatureConverter.celsius_to_fahrenheit(30)  # Output: 86.0
temp_c = TemperatureConverter.fahrenheit_to_celsius(86)  # Output: 30.0

print(temp_f)
print(temp_c)


# In this example:

# celsius_to_fahrenheit and fahrenheit_to_celsius are static methods. They perform conversions without needing any class or instance-specific data.
# They are utility methods that logically belong to TemperatureConverter but do not change its state or require instance attributes.
# Summary of Static Methods
# Static methods are ideal for utility tasks related to a class.
# They’re defined with @staticmethod and don't take self or cls as parameters.
# You can call them directly on the class or instance, but they do not interact with class or instance attributes.





