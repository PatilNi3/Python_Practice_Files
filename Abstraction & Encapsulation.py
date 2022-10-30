# WHAT IS ABSTRACTION ?
'''
- Abstraction is used to hide the internal functionality of the function from the users. The users only interact with
  the basic implementation of the function, but inner working is hidden.
'''

# Why Abstraction is used ?
'''
- In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
- It also enhances the application efficiency.
'''

# ABSRACT CLASS:
'''
- A class which contains one or more abstract methods is called an abstract class.
- While we are designing large functional units we use an abstract class.
'''

# ABSTRACT METHOD:
'''
- An abstract method is a method that has a declaration but does not have an implementation.
- When we want to provide a common interface for different implementations of a component, we use an abstract method. 
'''

# SYNTAX:
'''
from abc import ABC

class <class_name>(ABC):
'''

# EXAMPLE: 1
'''
from abc import ABC, abstractmethod

class Car(ABC):                                 # Abstract base class
    def mileage(self):                          # Abstract method
        pass
    def price(self):
        pass

class Tesla(Car):                               # Subclass
    def mileage(self):                          # Abstract method
        print("The mileage is 267kmpc")

    def price(self):
        print("Above 1 cr")

class Toyota(Car):                              # Subclass
    def mileage(self):                          # Abstract method
        print("The mileage is 24kmpl ")

class Honda(Car):                               # Subclass
    def mileage(self):                          # Abstract method
        print("The mileage is 25kmpl ")

class Hyundai(Car):                             # Subclass
    def mileage(self):                          # Abstract method
        print("The mileage is 25kmpl ")

T = Tesla()
T.mileage()
T.price()

Ty = Toyota()
Ty.mileage()
Ty.price()

H = Honda()
H.mileage()

Hy = Hyundai()
Hy.mileage()
'''
# EXPLANATION:
'''
- In the above code, we have imported the abc module to create the abstract base class(ABC). 
- We created the Car class that inherited the ABC class and defined an abstract method named mileage(). 
- We have then inherited the base class from the four different subclasses and implemented the abstract method differently. 
- We created the objects to call the abstract method.
'''

# EXAMPLE: 2
'''
from abc import ABC

class Polygon(ABC):                               # Abstract base class
    def sides(self):                              # Abstract method
        pass


class Triangle(Polygon):                          # Subclass
    def sides(self):                              # Abstract method
        print("Triangle has 3 sides")

class Square(Polygon):                            # Subclass
    def sides(self):                              # Abstract method
        print("Square has 4 sides")

class Pentagon(Polygon):                          # Subclass
    def sides(self):                              # Abstract method
        print("Pentagon has 5 sides")

class Hexagon(Polygon):                           # Subclass
    def sides(self):                              # Abstract method
        print("Hexagon has 6 sides")

T = Triangle()
T.sides()

S = Square()
S.sides()

P = Pentagon()
P.sides()

H = Hexagon()
H.sides()
'''

# NOTE:
'''
- We can not create the object to call the Abstract Base Class
- An Abstract class can contain the both methods normal and abstract method.
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ENCAPSULATION - ENCAPSULATION - ENCAPSULATION - ENCAPSULATION - ENCAPSULATION
'''
- Encapsulation describes the concept of bundling data and methods within a single unit.
- A CLASS is a example of Encapsulation, in which Methods and Attributes are binds in singLe unit.
  For example: If you are creating a class , it means you are implementing the Encapsulation.
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻