# Inheritance is a feature in Python that allows a class (called a child class or derived class) to inherit attributes and methods from another class (called a parent class or base class). This enables code reuse and creates a hierarchy of classes. The child class can also have its own attributes and methods or override those of the parent class.

# Types of Inheritance
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance
# Let's go through each type with examples.

# 1. Single Inheritance
# In single inheritance, a child class inherits from only one parent class.


# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an object of the Dog class
dog = Dog()
dog.speak()   # Output: Animal speaks
dog.bark()    # Output: Dog barks


# In this example:

# Dog inherits the speak method from Animal, and it has its own bark method.


# 2. Multiple Inheritance
# In multiple inheritance, a child class inherits from more than one parent class.


# Parent class 1
class Flyer:
    def fly(self):
        print("Flying")

# Parent class 2
class Swimmer:
    def swim(self):
        print("Swimming")

# Child class
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck quacks")

# Creating an object of the Duck class
duck = Duck()
duck.fly()    # Output: Flying
duck.swim()   # Output: Swimming
duck.quack()  # Output: Duck quacks


# In this example:

# Duck inherits from both Flyer and Swimmer and can use methods from both.


# 3. Multilevel Inheritance
# In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another class, creating a chain.

# Base class
class Vehicle:
    def move(self):
        print("Vehicle moves")

# Intermediate class
class Car(Vehicle):
    def drive(self):
        print("Car drives")

# Child class
class ElectricCar(Car):
    def charge(self):
        print("Electric car charges")

# Creating an object of ElectricCar
tesla = ElectricCar()
tesla.move()    # Output: Vehicle moves
tesla.drive()   # Output: Car drives
tesla.charge()  # Output: Electric car charges


# In this example:

# ElectricCar inherits from Car, which inherits from Vehicle.


# 4. Hierarchical Inheritance
# In hierarchical inheritance, multiple child classes inherit from the same parent class.


# Parent class
class Bird:
    def lay_egg(self):
        print("Bird lays egg")

# Child class 1
class Sparrow(Bird):
    def chirp(self):
        print("Sparrow chirps")

# Child class 2
class Ostrich(Bird):
    def run(self):
        print("Ostrich runs")

# Creating objects of Sparrow and Ostrich
sparrow = Sparrow()
sparrow.lay_egg()    # Output: Bird lays egg
sparrow.chirp()      # Output: Sparrow chirps

ostrich = Ostrich()
ostrich.lay_egg()    # Output: Bird lays egg
ostrich.run()        # Output: Ostrich runs

# In this example:

# Both Sparrow and Ostrich inherit from Bird.


# 5. Hybrid Inheritance
# Hybrid inheritance is a combination of two or more types of inheritance. Python uses the Method Resolution Order (MRO) to handle hybrid inheritance situations.


# Base class
class Animal:
    def eat(self):
        print("Animal eats")

# Intermediate class 1
class Mammal(Animal):
    def nurse(self):
        print("Mammal nurses its young")

# Intermediate class 2
class WingedAnimal(Animal):
    def fly(self):
        print("Winged animal flies")

# Child class
class Bat(Mammal, WingedAnimal):
    def hang(self):
        print("Bat hangs upside down")

# Creating an object of the Bat class
bat = Bat()
bat.eat()     # Output: Animal eats
bat.nurse()   # Output: Mammal nurses its young
bat.fly()     # Output: Winged animal flies
bat.hang()    # Output: Bat hangs upside down


# In this example:

# Bat inherits from both Mammal and WingedAnimal, which both inherit from Animal.