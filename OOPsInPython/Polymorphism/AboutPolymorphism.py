# Polymorphism in Python refers to the ability of different classes to be treated as instances of the same class through shared methods, even if they implement those methods differently. This allows for more flexible and reusable code.

# Example 1: Polymorphism with Functions
# Suppose we have different classes for animals, and each has its own sound method:

class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"
    
# Now, we can use a function that calls sound without needing to know the specific class of the object:


def make_sound(animal):
    print(animal.sound())

# Using polymorphism with different objects
dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!


# Here, make_sound works with any object that has a sound method, demonstrating polymorphism.

# Example 2: Polymorphism with Inheritance
# Polymorphism can also work with inheritance, where subclasses override a method from a parent class with their own implementation:


class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


# Now, each subclass can be used polymorphically as an Animal:

def animal_speak(animal):
    print(animal.speak())

# Creating instances
dog = Dog()
cat = Cat()

animal_speak(dog)  # Output: Woof!
animal_speak(cat)  # Output: Meow!

# The animal_speak function treats both Dog and Cat as Animal instances, even though each subclass has its own speak method.