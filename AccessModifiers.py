# WHAT IS ACCESS MODIFIER or ACCESS SPECIFIER ?
'''
- Access specifiers or access modifiers in python programming are used to limit the access of class variables and class
  methods outside of class while implementing the concepts of inheritance. This can be achieved by: Public, Private
  and Protected keyword.
- We can easily inherit the properties or behaviour of any class using the concept of inheritance. But some classes also
  holds the data (class variables and class methods) that we don’t want other classes to inherit. So, to prevent that
  data we used access specifiers in python.

• NOTE: Python does not follow Access Modifier rule complitely.
'''

# Keywords of Access Modifier
'''
1. Public
2. Protected
3. Private
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. PUBLIC ACCESS MODIFIER:
'''
- only variable
- We can access it in the class, outside the class and also in other class.
- self.name --> Public by default
'''

# ---------------------------------------------------------------------------- #

# 2. PROTECTED ACCESS MODIFIER:
'''
- Single underscore ( _ ) prefixed to the variable
- We can access it in the same class and in immediate child.
- self._name --> Protected
'''

# ---------------------------------------------------------------------------- #

# 3. PRIVATE ACCESS MODIFIER:
'''
- Double underscore ( __ ) prefixed to the variable
- we can access it in self(own) in the same class.
- self.__name --> Private
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXAMPLE: 1
'''
class student:

    def __init__(self, name, age, std):
        self.name = name                # Public
        self._age = age                 # Protected
        self.__std = std                # Private

    def show(self):
        print(self.name)
        print(self._age)
        print(self.__std)

obj = student('Nitin', 26, '20th')
obj.show()
'''

# EXAMPLE: 2
'''
class student:

    def __init__(self, name, age, std):
        self.name = name                # PUBLIC
        self._age = age                 # PROTECTED
        self.__std = std                # PRIVATE
        
    def show(self):
        pass

obj = student('Nitin', 26, '10th')
print(obj.name)
print(obj._age)
print(obj.__std)                        # AttributeError
'''

# EXAMPLE: 3
'''
class student:

    def __init__(self, name, age, std):
        self.name = name                # PUBLIC
        self._age = age                 # PROTECTED
        self.__std = std                # PRIVATE

    def show(self):
        print(self.name)
        print(self._age)
        print(self.__std)

class professor(student):

    def __init__(self, name, age, std, height):
        super().__init__(name, age, std)
        self.height = height
        self._height = height
        self.__height = height

    def show(self):
        super(professor, self).show()
        print(self.height)
        print(self._height)
        print(self.__height)



obj = professor('Nitin', 26, '20th', '5 ft 10 in')
print(obj.height)
print(obj._height)
print(obj.__height)                     # AttributeError
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# NAME MANGLING
'''
- A process in which any given identifier with one trailing underscore and two leading underscores is textually 
  replaced with the _ClassName__Identifier is known as Name mangling.
'''

# SYNTAX:
'''
obj._classname__variable
'''

# EXAMPLE: 1
'''
class student:

    def __init__(self, name, age, std):
        self.name = name                # Public
        self._age = age                 # Protected
        self.__std = std                # Private

    def show(self):
        pass

obj = student('Nitin', 26, '20th')
print(obj.name)
print(obj._age)
print(obj._student__std)
'''

# EXAMPLE: 2
'''
class student:

    def __init__(self, name, age, std):
        self.name = name                # Public
        self._age = age                 # Protected
        self.__std = std                # Private

    def show(self):
        pass

class professor(student):

    def __init__(self, name, age, std, height):
        super().__init__(name, age, std)
        self.height = height
        self._height = height
        self.__height = height

    def show(self):
        super(professor, self).show()
        pass

obj = professor('Nitin', 16, '10th', '4.5 feet')
print(obj.height)
print(obj._height)
print(obj._professor__height)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXAMPLE:
'''
class Modifiers:

    def __init__(self, name):
        self._protected_member = name

m = Modifiers("NITIN_P29")
print(m._protected_member)

m._protected_member = "NITIN"
print(m._protected_member)
'''

# EXAMPLE:
"""
class Teacher:

    val1 = None
    _val2 = None
    __val3 = None

    def __init__(self, val1, val2, val3):
        self.val1 = val1
        self._val2 = val2
        self.__val3 = val3

    def dispPublicMembers(self):
        print("This is public member: ", self.val1)

    def _dispProtectedMembers(self):
        print("This is protected member: ", self._val2)

    def __dispPrivateMembers(self):
        print("This is private member: ", self.__val3)

    def accessPrivateMembers(self):
        self.__dispPrivateMembers()

class Child(Teacher):

    def __init__(self, val1, val2, val3):
        Teacher.__init__(self, val1, val2, val3)

    def accessProtectedMembers(self):
        self._dispProtectedMembers()



obj1 = Child("Hello", "Simon", 100000)

obj1.dispPublicMembers()
obj1.accessProtectedMembers()
obj1.accessPrivateMembers()

# Explanation:
- After writing the above code in python, the output will appear as “ Hello Simon 100000 ”.
- Here, we have parent class as “Teacher” and derived class as “Child”, and the private members are accessed by making 
  it public member function “def accessPrivateMembers” and it can access private members of the class.
- Also, we have a “Child” class and it inherits the properties of the parent class and also it can access the protected 
  member’s function of “Teacher” class which is the parent class.
"""




# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻