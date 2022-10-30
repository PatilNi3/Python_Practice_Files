# WHAT IS CLASS ?
'''
- A class is like an object constructor or a blueprint for creating a object.
- A python class is a group of attributes and methods. Attributes are represented by variable that contains data and
  Method that performs an action or task. Methos is similar to function.
- To creating a class we use keyword "class:"
- Syntax: class <Class_name>:
'''

# EXAMPLE:
'''
class MyFirstClass:
    cls = "Uber Auto"           # CLASS VARIABLE
'''

# WHAT IS OBJECT ?
'''
- Object represents the base class name from where all classes in python are derived.
- This class is also derived from object class.
- Objects are optional.
- To create object we use class
- Syntax: object_name = Class_name()
'''

# EXAMPLE:
'''
obj = MyFirstClass()
print(obj.cls)
'''

# __init__() function
'''
- It is a built-in function and we call this as a constructor.
- All classes have a function called __init__(), which is always executed when the class is being initiated.
- Use the __init__() function to assign values to object properties or other operations that are necessary to do when 
  the object is being created.
'''

#  EXAMPLE:
'''
class FamilyMan:
    def __init__(self, name, age):          # self -> self is a variable which refers to current class instance/object.
        self.naam = name                    # INSTANCE VARIABLE
        self.umar = age                     # INSTANCE VARIABLE

FM = FamilyMan('Nitin', 26)

print(FM.naam)
print(FM.umar)
'''

# OBJECT METHOD
'''
- Object can also contain methods. Methods in object are functon that belongs to the object.
- Syntax: objectname.Method_name
'''

# EXAMPLE:
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def MyFun(self):                    # CLASS/INSTANCE METHOD
        print(self.name)
        print(self.age)

Obj = Person('Neha', 25)
Obj.MyFun()
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXAMPLE: 1
'''
class MyClass:
    x = 25

obj = MyClass()
print(obj.x)
'''

# EXAMPLE: 2
'''
class Person:
    def __init__(self, Name, Age):
        self.your_name = Name
        self.your_age = Age

obj1 = Person('Neha', 27)
obj2 = Person('Ruchita', 30)

print(obj1.your_name, obj1.your_age)
print(obj2.your_name, obj2.your_age)
'''

# EXAMPLE: 3
'''
class Mobile:

    Android = "Nothing Phone 1"
    IOS = "I Phone 15"

    def favourite(self):
        print("Budget friendly: ", self.Android)
        print("Premium: ", self.IOS)

choice = Mobile()

choice.favourite()
'''

# EXAMPLE: 4
'''
class Employee:

    def __init__(self, Name, Age, City):
        self.Emp_Name = Name
        self.Emp_Age = Age
        self.Emp_City = City

    def show(self):
        print("New employee name:", self.Emp_Name)
        print("His age:", self.Emp_Age)
        print("His current working location:", self.Emp_City)

obj = Employee('Nitin', 26, 'Banglore')

obj.show()
'''

# EXAMPLE: 5
'''
class Dog:

    animal = 'kutta'

    def __init__(self, breed):
        self.breed = breed

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

obj = Dog("Pug")
obj.setcolor("brown")
print(obj.getcolor())
print(obj.breed)
print(obj.animal)
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻