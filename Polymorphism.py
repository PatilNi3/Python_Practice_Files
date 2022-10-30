# WHAT IS POLYMORPHISM ?
'''
- The word polymorphism means having many forms.
- It refers to the use of a single type entity (method, operator or object) to represent different types in different
  scenarios.
'''

# -------------------------------------------------------------------------------------------------------------------- #

# POLYMORPHIC LENGTH FUNCTION

# EXAMPLE: 1
'''
print(len('Nitin'))
'''
# EXAMPLE: 2
'''
print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
'''
# EXAMPLE: 3
'''
print(len({"First Name":"Nitin", "Last Name":"Patil"}))
'''

# -------------------------------------------------------------------------------------------------------------------- #

# POLYMORPHISM IN ADDITION OPERATION

# EXAMPLE: 1
'''
Num1 = 23
Num2 = 27

print(Num1+Num2)
'''
# EXAMPLE: 2
'''
Str1 = "Python"
Str2 = "Programming"

print(Str1 + " " + Str2)
'''

# EXPLANATION:
'''
- For integer data types, + operator is used to perform arithmetic addition operation.
- For string data types, + operator is used to perform concatenation.
- Here, we can see that a single operator + has been used to carry out different operations for distinct data types. This 
  is one of the most simple occurrencees of polymorphism in Python, 
'''

# -------------------------------------------------------------------------------------------------------------------- #

# POLYMORPHISM IN CLASS METHODS

# EXAMPLE: 1
'''
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
'''

# EXPLANATION:
'''
- Here, we have created two classes India and USA. They share a similar structure and have same method names "capital()", 
  "language()" and "type()".
- However, notice that we have not created a common superclass or linked the classes together in any way. Even then, we 
  can pack these two different objects into a tuple and iterate through it using a common "country" variable. It is 
  possible due to polymorphism.
'''

# -------------------------------------------------------------------------------------------------------------------- #

# POLYMORPHISM WITH INHERITANCE

# EXAMPLE: 1
'''
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_bird.intro()
obj_bird.flight()

obj_spr = sparrow()
obj_spr.intro()
obj_spr.flight()

obj_ost = ostrich()
obj_ost.intro()
obj_ost.flight()
'''

# EXPLANATION:
'''
- In python, polymorphism lets us define method in the child class that have the same name as the methods in the parent
  class.
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# POLYMORPHISM IS IMPLEMENTED BY 2 CONCEPTS
'''
1. Overloading
2. Overriding
'''

# 1. OVERLOADING:
'''
- When two or more methods in the same class have the same name but different parameters, it's called Overloading.
'''
# Types of Overloading:
'''
1.1 Method overloading
1.2 Constructor overloading
1.3 Operator overlaoding
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 1.1 Method Overloading
'''
- This process of calling the same method in different ways is called Method Overloading.
- Python does not support the Method overloading, because we can't provide datatype as Python is dynamically typed language.
'''

# EXAMPLE: 1
'''
def mul(a, b):
    P = a * b
    print(P)

def mul(a, b, c):
    P = a * b * c
    print(P)

mul(5, 5)           # TypeError: mul() missing 1 required positional argument: 'c'

mul(5, 5, 5)
'''

# EXPLANATION:
'''
- In the above code, we have defined two mul method, but we can only use the second mul method, as python does not 
  support method overloading.
- We may define many methods of the same name and different arguments, but we can only use the latest defined method.
- Calling the other method will produce an error. Like here calling mul(5, 5) will produce an error as the latest 
  defined mul method takes three arguments.
'''

'''
- That does not mean that you cannot call a method with different number of arguments.
- There are a couple of alternatives available in python that make it possible to call the same method but with 
  different number of arguments.
  Like Default argument, Variable length argument
'''

# EXAMPLE: 1
'''
print("by using default argument values")

class Overloading:
    def default_arguments (self, a='Nitin', b='Pythonista'):
        print(a)
        print(b)

obj = Overloading()
obj.default_arguments()
'''

# EXAMPLE: 2
'''
print("by using default argument values and conditional statement")

class Overloading:

    def default_arguments(self, a = None, b = None, c = None):

        if(a != None and b != None and c != None):
             print("3 arguments")

        elif (a != None and b != None):
            print("2 arguments")

        elif a != None:
             print("1 argument")

        else:
            print("0 arguments")

obj = Overloading()

obj.default_arguments('Nitin', 'Patil', 'Pythonista')

obj.default_arguments('Nitin', 'Pythonista')

obj.default_arguments('Pythonista')

obj.default_arguments()
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 1.2 Constructor Overloading
'''
- Constructor overloading means more than one constructor in a class with the same name but a different argument(parameter)
- Python does not support multiple constructors.
'''

# EXAMPLE: 1
'''
class ConstructorOverloading:

    def __init__(self, name):
        self.name = name

    def __init__(self, FirstName, LastName):
        self.fname = FirstName
        self.lname = LastName

    def m1 (self):
        print("This is class method")
        print(self.fname + self.lname)

# obj1 = ConstructorOverloading('Nitin')                       # TypeError
# obj1.m1()

obj2 = ConstructorOverloading('Nitin', 'Patil')
obj2.m1()
'''

# EXPLANATION:
'''
- In the above example, we created an object with two parameters passed. Those two parameters are passed to the second 
  constructor
- If we define the object with a single parameter, we get an error. Python does not consider the first constructor.
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 1.3 Operator Overloading
'''
int + int = addition
str + str = concatination

- Operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because '+' 
  operator is overloaded by int class and str class.
'''

# EXAMPLE: 1
'''
class Operator:

    def __init__(self, a):
        self.a = a

a1 = Operator(25)

a2 = Operator(75)

# print(a1 + a2)      # TypeError
print(25 + 75)
'''

'''
- In above example, in the first print statement we are try to add two objects (a1, a2) and operator does not allows us 
  to add such rather than int, float, str; that's why we get TypeError.
- In second print statement, we adding two int and operator allows us to do such operation.
- This is all beacause magic method or dender method which runs internally.
  For eg.: + --> __add__(self, others)
           - --> __sub__(self, others)
           * --> __mul__(self, others)
           / --> __div__(self, others)
'''

# EXAMPLE: 1 -UPDATED
'''
class operator:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

a1 = operator(25)

a2 = operator(75)

print(a1 + a2)
'''

# EXAMPLE: 1.1
'''
class operator:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

    def __truediv__(self, other):
        return self.a / other.a

    def __floordiv__(self, other):
        return self.a // other.a

    def __mod__(self, other):
        return self.a % other.a

    def __pow__(self, other):
        return self.a ** other.a

    # def __and__(self, other):
    #     return self.a & other.a
    #
    # def __or__(self, other):
    #     return self.a | other.a

a1 = operator(75)

a2 = operator(75)

print(a1 + a2)

print(a1 - a2)

print(a1 * a2)

print(a1 / a2)

print(a1 // a2)

print(a1 % a2)

print(a1 ** a2)
'''

# EXAMPLE: 2
'''
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

Obj1 = complex(1, 2)
Obj2 = complex(2, 3)
Obj3 = Obj1 + Obj2
print(Obj3)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. OVERRIDING:
'''
- When two or more methods in the same class have the same name and same parameters, it's called Overriding.
'''
# Types of Overriding:
'''
2.1 Method Overriding
2.2 Constructor Overriding
2.3 Operator Overriding
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 2.1 Method Overriding
'''
- When we have two methods with the same name that each perform different tasks.
- The child class has access to the properties and functions of the parent class method.
'''

# EXAMPLE: 1
'''
class operation:

    def m1(self):             # METHOD
        print("first method")

    def m1(self):             # METHOD
        print("second method")

obj = operation()
obj.m1()
'''

# EXAMPLE: 2
'''
class operation:                      # CLASS_1
    def m1(self):                     # METHOD
        print("first method")

class update(operation):              # CLASS_2
    def m1(self):                     # METHOD
        super().m1()
        print("second method")

obj = update()
obj.m1()
'''

# EXAMPLE: 3
'''
class Parent():

    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)

class Child(Parent):

    def __init__(self):
        self.value = "Inside Child"

    def show(self):
        print(self.value)


obj2 = Child()
obj2.show()
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 2.2 Constructor Overriding

# EXAMPLE: 1
'''
class Mother:

    def __init__(self):
        self.money = 23000
        print("This is mother class constructor.")

    def show(self):
        print("Mother class instance method.")

class Son(Mother):

    def __init__(self):
        self.money = 11000
        print("This is son class constructor.")

    def display(self):
        print("Son class instance method.")

obj = Son()
'''


# EXPLANATION:
'''
- Python constructor overriding mean one method will overrides the other. The parent class and child class both have the 
  constructor and the child will override the parent constructor.
- After writing the above example, the output will appear as a "This is son class constructor.". Here the child class 
  constructor overrides the parent class constructor and it prints the message of the child class.
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 2.3 Operator Overriding
'''
Operator overriding is not possible in Python because python is not fully OOP (Object Oriented Programming) language.
'''
# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

# OOP's Syllabus:
'''
1. Method Overriding
2. Method Overloading
3. Operator Overloading
'''
