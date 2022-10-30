# What is Inheritance?
'''
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- Parent class is the class being inherited from, also called base class and Child class is the class that inherits
  from another class, also called derived class.
- Inheritance provides the reusability of a code. We don't have to write the same code again and again. Also, it allows
  us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B
  would automatically inherit from class A.
'''

# Types of Inheritance:
'''
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hybrid Inheritance
5. Hierarchical Inheritance
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. SINGLE INHERITANCE
'''
- Single Inheritance: Single inheritance enables a derived class to inherit properties from a single parent class.
'''

# EXAMPLE:
'''
class A:
    def m1(self):
        print("from m1")
class B(A):
    def m2(self):
        print("from m2")

obj = B()
obj.m2()
obj.m1()
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 2. MULTILEVEL INHERITANCE
'''
- In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived 
  class. This is similar to a relationship representing a child and a grandfather.
'''

# EXAMPLE: 1
'''
class A:
    def m1(self):
        print("from m1")

class B(A):
    def m2(self):
        print("from m2")

class C(B):
    def m3(self):
        print("from m3")

obj = C()
obj.m3()
obj.m2()
obj.m1()
'''

# EXAMPLE: 2
'''
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfathername = grandfather_name

class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        self.fathername = father_name

        Grandfather.__init__(self, grandfather_name)

class Child(Father):
    def __init__(self, child_name, father_name, grandfather_name):
        self.childname = child_name

        Father.__init__(self, father_name,grandfather_name)

    def print_name(self):
        print("Grand_Father_Name: ", self.grandfathername)
        print("Father_Name: ", self.fathername)
        print("Child_Name: ", self.childname)



obj = Child('C', 'AB', 'ABC')

obj.print_name()
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 3. MULTIPLE INHERITANCE
'''
- When a class can be derived from more than one base class.
- In multiple inheritance, all the features of the base classes are inherited into the derived class.
'''

# EXAMPLE: 1
'''
class A:
    def fun1(self):
        print("from m1")

class B:
    def fun2(self):
        print("from m2")

class C(A, B):
    def fun3(self):
        print("from m3")

obj = C()
obj.fun3()
obj.fun2()
obj.fun1()
'''

# EXAMPLE: 2
'''
class Mother:
    Mother_Name = ""
    def mother(self):
        print(self.Mother_Name)

class Father:
    Father_Name = ""
    def father(self):
        print(self.Father_Name)

class Daughter(Mother, Father):
    def parents(self):
        print("Mother: ", self.Mother_Name)
        print("Father: ", self.Father_Name)



obj = Daughter()

obj.Mother_Name = "Kavvu"
obj.Father_Name = "Dhruv"

obj.parents()
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 4. HYBRID INHERTANCE
'''
- This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.
'''

# EXAMPLE: 1
'''
class A:
    def o1(self):
        print("from m1")

class B(A):
    def o2(self):
        print("from m2")

class C(B):
    def o3(self):
        print("from m3")

class D:
    def o4(self):
        print("from m4")

class E(B, D):
    def o5(self):
        print("from m5")

obj = E()
obj.o5()
obj.o4()
obj.o2()
obj.o1()
'''

# EXAMPLE: 2
'''
class Principal:
    def func1(self):
        print("This function is in principal.")
 
class HoD(Principal):
    def func2(self):
        print("This function is in hod.")
 
class Teacher(Principal):
    def func3(self):
        print("This function is in teacher.")
 
class Student(HoD, Principal):
    def func4(self):
        print("This function is in student.")
 
 

object = Student()
object.func1()
object.func2()
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 5. HIERARCHICAL INHERITANCE
'''
- When more than one derived classes are created from a single base class.
'''

# EXAMPLE:
'''
class A:
    def a(self):
        print("from class A")

class B(A):
    def b(self):
        print("from class B")

class C(A):
    def c(self):
        print("from calss C")

class D(A):
    def d(self):
        print("from class D")



obj = D()

obj.a()
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# MRO (METHOD RESOLUTION ORDER)
'''
- In the multi-inheritance, a class can consist of many functions, so the Method Resolution Order technique is used to 
  search the order in which the base class is executed.
- First, it is searched in the current class. If not found, the search moves to parent classes. This is left-to-right 
  and finally to the system object.
'''

# EXAMPLE: 1
'''
class A:
    def lr(self):
        print("In class A")

class B(A):
    def lr(self):
        print("In class B")

class C(A):
    def lr(self):
        print("In class C")

class D(B, C):
    pass



obj = D()

obj.lr()
'''

# EXAMPLE: 2    # Assignment given by Sir
'''
# E - D - P - Q - C - B - X - Y - A - SYSTEM

class A:
    def m1(self):
        print("from m1")

class Y(A):
    def m2(self):
        print("from m2")

class X(Y):
    def m3(self):
        print("from m3")

class B(X):
    def m4(self):
        print("from m4")

class C(B):
    def m5(self):
        print("from m5")

class Q(C):
    def m6(self):
        print("from m6")

class P(Q):
    def m7(self):
        print("from m7")

class D(P):
    def m8(self):
        print("from m8")

class E(D):
    def m9(self):
        print("from m9")


print(E.__mro__)
'''

# In another way

'''
class A:pass
class Y(A):pass
class X(Y):pass
class B(X):pass
class C(B):pass
class Q(C):pass
class P(Q):pass
class D(P):pass
class E(D):pass


print(E.__mro__)
'''

# EXAMPLE:
'''
# A - B - D - E - C - F - O - SYSTEM

class O:pass
class F(O):pass
class C(F):pass
class E(C):pass
class D(F):pass
class D(E):pass
class B(D):pass
class A(B):pass


print(A.__mro__)            # tuple
print(A.mro())              # list
'''

# EXAMPLE: 3  TRICKY
'''
class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass


print(D.__mro__)
'''

# EXAMPLE: 4
'''
class A:
  def myname(self):
    print(" I am a class A")

class B(A):
  def myname(self):
    print(" I am a class B")
      
class C(A):
  def myname(self):
    print("I am a class C")

class D(B, C):
  pass


print(D.__mro__)
'''

# EXAMPLE: 5  COMPLEX
'''
class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)
'''

# EXAMPLE: 6
'''
class D: pass
class E: pass
class F: pass
class B(D, E): pass
class C(D, F): pass
class A(B, C): pass

print(A.__mro__)
'''

# EXAMPLE: 7
'''
class A: pass
class B: pass
class C(A, B): pass
class D(C, B): pass

print(D.__mro__)
'''
# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻