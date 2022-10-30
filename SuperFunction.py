# What is Super function ?
'''
- The super function returns a temporary object of the superclass that allows to access all of its methods to its child
  class.
- The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of
  the base class.
- Need not remember or specify the parent class name to access its methods. This function can be used both in single
  and multiple inheritances.
'''

# SYNTAX:
'''
super()
'''

# EXAMPLE: 1
'''
class A:
    def m1(self):
        print("in m1 from A")

class B(A):
    def m1(self):
        super().m1()
        print("in m1 from B")

class C(B):
    def m1(self):
        super().m1()
        print("in m1 from C")

class D(C):
    def m1(self):
        super().m1()
        print("in m1 from D")

class E(D):
    def m1(self):
        super().m1()
        print("in m1 from E")

obj = E()
obj.m1()
'''

# EXAMPLE: 2
'''
class Parent:

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

obj = Parent('Nitin', 50)
obj.show()
'''

# EXAMPLE: 2.1
'''
class Parent:

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

class Child(Parent):

    def __init__ (self, name, age, city, pincode):
        super().__init__(name, age)                             # PARENT CONSTRUCTOR
        self.city = city
        self.pincode = pincode

    def show(self):
        super(Child, self).show()                               # PARENT METHOD
        print(self.city)
        print(self.pincode)

obj = Child('Nitin', 50, 'Sangli', 416410)
obj.show()
'''

# EXAMPLE: 2.2
'''
class Parent:

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

class Child(Parent):

    def __init__ (self, name, age, city, pincode):
        super().__init__(name, age)                             # PARENT CONSTRUCTOR             
        self.city = city
        self.pincode = pincode

    def show(self):
        super(Child, self).show()                               # PARENT METHOD
        print(self.city)
        print(self.pincode)

class GrandChild(Child):

    def __init__(self, name, age, city, pincode, height, weight):
        super().__init__(name, age, city, pincode)              # PARENT CONSTRUCTOR
        self.height = height
        self.weight = weight

    def display(self):
        super(GrandChild, self).show()                          # PARENT METHOD
        print(self.height)
        print(self.weight)

obj = GrandChild('Nitin', 50, 'Sangli', 416410, '5 Feet 10 Inches', 70)
obj.display()
'''

# EXAMPLE: 3
'''
class A:

    name = 'Python'                                             # CLASS VARIABLE

    def m1(self):                                               # CLASS METHOD
        self.course = 'DS'
        print("in m1")

class B(A):

    name = "Java"                                               # CLASS VARIABLE

    def m1(self):                                               # CLASS METHOD
        print(self.name)
        super().m1()
        print(super().name)                                     # PARENT VARIABLE
        print(self.course)

obj = B()
obj.m1()
'''

# EXAMPLE: 4
'''
class A:

    def m1(self):
        self.a = 100
        print("A-m1")

class B(A):

    def m1(self):
        self.a = 500
        print("B-m1")

        super().m1()
        print(self.a)

obj = B()
obj.m1()
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXAMPLE:


'''
class Person:

    def __init__(self, name):
        print(name + " is a cricketer")


class Athlete(Person):

    def __init__(self, name):
        print(name + " is an athlete")


class FamousPerson(Person):

    def __init__(self, name):
        print(name + " is a famous person")


class Sachin(Athlete, FamousPerson):

    def __init__(self):

        Athlete.__init__(self, "Sachin")              # Super constructor

        FamousPerson.__init__(self, "Sachin")         # Super constructor

        Person.__init__(self, "Sachin")               # Super constructor

obj = Sachin()
'''


# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ACCESING/INHERIT ROOT CLASS PROPERTIES INTO VERY BASE CLASS
'''  OR '''
# INHERIT GRAND PARENT CLASS PROPERTIES INTO CHILD CLASS


# EXAMPLE: 1
'''
class A:
    def m1(self):
        print("in m1 from A")

class B(A):
    def m1(self):
        super().m1()
        print("in m1 from B")

class C(B):
    def m1(self):
        super(B, self).m1()
        print("in m1 from C")

obj = C()
obj.m1()
'''

# EXAMPLE: 2
'''
class A:
    def m1(self):
        print("in m1 from A")

class B(A):
    def m1(self):
        super().m1()
        print("in m1 from B")

class C(B):
    def m1(self):
        super().m1()
        print("in m1 from C")

class D(C):
    def m1(self):
        super().m1()
        print("in m1 from D")

class E(D):
    def m1(self):
        super(B, self).m1()
        print("in m1 from E")

obj = E()
obj.m1()
'''

# EXAMPLE: 3
'''
class Parent:

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

class Child(Parent):

    def __init__ (self, name, age, city, pincode):
        super().__init__(name, age)                            # PARENT CONSTRUCTOR
        self.city = city
        self.pincode = pincode

    def show(self):
        super(Child, self).show()
        print(self.city)
        print(self.pincode)

class GrandChild(Child):

    def __init__(self, name, age, city, pincode, height, weight):
        super().__init__(name, age, city, pincode)             # PARENT CONSTRUCTOR
        self.height = height
        self.weight = weight

    def display(self):
        super(Child, self).show()
        print(self.height)
        print(self.weight)

obj = GrandChild('Nitin', 50, 'Sangli', 416410, '5 Feet 10 Inches', 70)
obj.display()
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻