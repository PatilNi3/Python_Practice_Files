# WHAT IS FUNCTION IN PYTHON ?
'''
- A function is a group of related statements that performs a specific task.
- Functions help break our program into smaller and modular part. As our program grows larger and larger, functions make
  it more organized and manageable.
- A function is a block of code which only runs when it is called.
- We can pass data, known as parameters, into a function. A function can return data as a result.
- We create a function using "def" keyword.
'''

# there are two types of function:
# 1. Built in function
# 2. User defined function

# SYNTAX:
'''
def function_name(parameters):
    statement or body
'''
# Syntax Explaned:
'''
- Keyword 'def' that marks the start of the function header.
- A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
- Parameters (arguments) through which we pass values to a function. They are optional.
- A colon (:) to mark the end of the function header.
- One or more valid python statements that make up the function body.
'''

# EXAMPLE:

# Creating a FUNCTION
'''
def My_first_function():
    print("☺ I have just created my first function in Python. ☺")

# Calling a FUNCTION

My_first_function()
'''

# RETURN STATEMENT
'''
- The return statement is used to exit a function and go back to the place from where it was called.
- This statement can contain an expression that gets evaluated and the value is returned.
- return[Expression_list]
'''

# EXAMPLE: 1
'''
def my_function(X):
    return 5 * X

print(my_function(5))
'''

# EXAMPLE: 2
'''
def absolute_value(num):

    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# PARAMETERS AND ARGUMENT
'''
- The terms parameter and argument can be used for the same thing: information that are passed into a function.
- A parameter is the variable listed inside the parentheses in the function definition.
- Arguments are the values passed inside the parenthesis of the function.
'''

# EXAMPLE: 1
'''
def my_function(food):                     # Formal Argument
  for x in food:
    print(x)

fruits = ["Apple", "Banana", "Cherry"]     # Actual Argument

my_function(fruits)
'''

# EXAMPLE: 2
'''
def add():
    x = 10
    y = 20
    z = x + y
    print(z)

add()
'''

# EXAMPLE: 3
'''
def add():
    x = int(input("Enter first no.: "))
    y = int(input("Enter second no.:  "))
    z = x + y
    print("Addition of this two no. is: ",z)
add()
'''

# EXAMPLE: 4
'''
def add(x, y):
    z = x + y
    print(z)

add(50, 50)
'''


# EXAMPLE: 5
'''
def add(x, y, p):
    z = x + y
    print(z)
    
add(25, 75, 50)
'''

# EXAMPLE: 6
'''
def add(a, b, c):
    x = a + b + c
    print(x)

result = add(1000, 1000, 1000)
'''

# DIFFERENT METHODS

# 1. With no argument no return type
'''
def add():
    x = 25
    y = 50
    z = x + y
'''

# 2. With no argument and with return value
'''
def add():
    x = 25
    y = 50
    z = x + y
    return z               # try print(z)
add()
'''

# 3. Argument with no return value
'''
def add(x, y):
    print(x + y)
add(10, 20)
'''

# 4. Argument with return value
'''
def add(x, y):
    return(x + y)
print(add(10, 20))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# TYPES OF ARGUMENT
'''
1. Positional Argument
2. Default Argument
3. Variable length Argument (*args)
4. Keyword Argument
5. Variable length keyword Argument (**kwargs)
'''

# 1. POSITIONAL ARGUMENT
'''
- Positional argument means that the argument must be provided in a correct position in a function call.
'''

# EXAMPLE: 1
'''
def My_Car (car_name, variant, price):            # Formal argument

    print("Car Name: ", car_name)
    print("Car Variant: ", variant)
    print("Car Price: ", price)

# My_Car()                                          # No arguments

# My_Car('Mercedes Benz')                           # Insufficient arguments

My_Car('Mercedes Benz', 'C-Class', '61 Lakh')     # Actual argument
'''

# EXAMPLE: 2
'''
def skill (course, duration, package):

    print("Course Name: ", course)
    print("Course Duration in Months: ", duration)
    print("Package in LPA (min.): ", package)

skill('Data Science', 5, 18)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. DEFAULT ARGUMENT
'''
- If we call the function without argument, it uses the default value.
- A default argument is a parameter that assumes a default value if a value is not provided in the function call for 
  that argument.
- Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments 
  to its right must also have default value.
'''

# EXAMPLE: 1
'''
def My_Car (car_name, variant, price, airbag = 6):

    print("Car Name: ", car_name)
    print("Car Variant: ", variant)
    print("Car Price: ", price)
    print("No. of Airbags: ", airbag)

My_Car('Mercedes Benz', 'C-Class', '61 Lakh')
'''

# EXAMPLE: 2
'''
def skill (course, duration, package, designation = 'Developer'):

    print("Course Name: ", course)
    print("Course Duration in Months: ", duration)
    print("Package in LPA (min.): ", package)
    print("Designation: ", designation)

skill('Data Science', 5, 18, 'Data Scientist')
'''

# EXAMPLE: 3
'''
def about_pune (city, population, famous = 'Education' , metro):

    print("City Name: ", city)
    print("Population of City in million: ", population)
    print("Famous for: ", famous)
    print("Metro availability: ", metro)

about_pune('Pune', 7.8, 'Education', 'Yes')
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. VARIABLE LENGTH ARGUMENT (*args)
'''
- Sometimes, we do not know in advance the number of arguments that will be passed into a function.
- Python allows us to handle this kind of situation through function calls with Variable Length Arguments (*args). 
- Add asterisk(*) before the parameter name in the function definition.
'''

# EXAMPLE: 1
'''
def weekend (*days):

    print(*days)

weekend('Saturday', 'Sunday')
'''

# EXAMPLE: 2
'''
def ThreeIdiots(*girls):

  print("Drisha's mother " + girls[2])

ThreeIdiots("Nitin", "Neha", "Ruchita")
'''

# EXAMPLE: 3
'''
def greetings (*namaste):

    for i in namaste:
        print("Thank You", i, "for listening me.")

greetings ('Neha', 'Ruchita')
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 4. KEYWORD ARGUMENT
'''
- You can also send arguments with the key = value syntax.
- The idea is to allow the caller to specify the argument name with values so that caller does not need to remember the 
  order of parameters.
'''

# EXAMPLE: 1
'''
def car_details(name,price,color,wheel):

    print("car_name:", name)
    print("car_price:", price)
    print("car_color:", color)
    print("no_of_wheel:", wheel)

car_details(name='Mercedes Benz', price='61,00,000', color='Matt Red', wheel= 4)        # within the order

car_details(wheel= 4, color='Matt Red', price='61,00,000', name='Mercedes Benz')        # out of order

car_details('Mercedes Benz', '61,00,000', color='Matt Red', wheel= 4)                   # 2 positional, 2 keyword
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 5. VARIABLE LENGTH KEYWORD ARGUMENT (**kwargs)
'''
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments.
'''

# EXAMPLE: 1
'''
def personal_details (**kwargs):

    print(kwargs)

personal_details (Name= 'Nitin', Education= 'BE', City= 'Sangli')
'''

# EXAMPLE: 2
'''
def myFun(**kwargs):
    for key, value in kwargs.items():
        print({key, value})

myFun(first='Hi', mid='My self', last='Nitin')
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# TYPES OF VARIABLE
'''
1. Local variable
2. Global variable
'''

# 1. LOCAL VARIABLE:
'''
- Local variables are those which are defined inside a function and its scope is limited to that function only.
- It cannot be accessed anywhere outside the function.
'''

# EXAMPLE: 1
'''
def function1():
    N = "Fevicol"
    print(N)

function1()
'''

# EXAMPLE: 2
'''
def function2():
    N2 = "Pakka Local"

function2()

print(N2)
'''


# 2. GLOBAL VARIABLE:
'''
- The global variables are those which are defined outside any function and which are accessible throughout the program 
  i.e. inside and outside of every function.
'''

# EXAMPLE: 1
'''
X = "Easy Language."             # Global variable

def My_Function():
  print("Python is " + X)

My_Function()
'''

'''# EXAMPLE OF LOCAL AND GLOBAL VARIABLE IN SAME PROGRAM # '''

# EXAMPLE: 2
'''
Y = "Dynamically typed."                  # Global variable

def My_Function1():

  Y = "Interepreter based language."      # Local variable
  print("Python is " + Y)

My_Function1()

print("Python is " + Y)
'''

# EXAMPLE: 3
'''
Score = 5                                   # Global variable

def CalculateScore():

	Score = 10                              # Local variable
	print("Final Score is:", Score)

CalculateScore()

print("Initial Score was:", Score)
'''


''' # GLOBAL KEYWORD # '''

# EXAMPLE: 1
'''
def My_Function2():

  global X
  X = "interpreter based language."

My_Function2()

print("Python is " + X)
'''

# Example 2-
'''
Y = "Platform Independent"

def My_Function3():

  global Y
  Y = "High level language"

My_Function3()

print("Python is " + Y)
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻


# WHAT IS RECURSION ?
'''
- Recursion is the process of defining something in terms of itself.
- A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be
  reflected recursively.
- In Python, we know that a function can call other functions. It is even  possible for the function to call itself. This 
  type of construct are termed as recursive function. 
'''

# EXAMPLE: 1
'''
def factorial(x):

  if x == 1:
      return 1
  else:
      return (x * factorial(x-1))

Num = int(input("Enter the no.: "))
print("The factorial of", Num, "is", factorial(Num))

- In the above example, factorial() is a recursive function as it calls itself.
- When we call this function with a positive integer, it will recursively call itself by decreasing the number.
- Each function multiplies the number with the factorial of the number below it until it is equal to one.
- Our recursion ends when the number reduces to 1. This is called the base condition.
- Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.
- By default, the maximum depth of recursion is 1000. If limit is crossed, it results in RecursionError.
'''

# EXAMPLE: 2
'''
def recursor():
    recursor()
recursor()
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

# LAMBDA FUNCTION OR EXPRESSION
'''
- Lambda is a keyword in Python used to define functions, more specifically Anonymous Functions and such functions are 
  known as Lambda Functions or Lambda Expressions.
- A lambda function is a small anonymous function, anonymous means that the function is without name.
- While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda 
  keyword. Hence, anonymous functions are also called lambda functions.
- Generally lambda used in dataframe
- This function can have any number of arguments but only one expression, which is evaluated and returned.
'''

# SYNTAX:
'''
lambda arguments: expression
# a, b = 5, 25
# print(a+b)
'''
# EXAMPLE: 1
'''
x = (lambda a, b: a + b)(5, 25)
print(x)

# or

print((lambda a, b: a + b)(5, 25))
'''


# EXAMPLE: 2
'''
x = "Water bottle"

(lambda x: print(x))(x)
'''

# EXAMPLE: 3
'''
double = lambda x: x * 2

print(double(5))
'''

# EXAMPLE: 4
'''
Maximum = lambda x, y: x if x > y else y

print(Maximum(4, 6))
'''

# EXAMPLE: 5
'''
def multiplier(n):
    return lambda a: a * n

my_multiplier = multiplier(5)

print(my_multiplier(25))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# LAMBDA generally used with -
''' 
1. map          # These three are code optimization techniques.
2. filter       
3. reduce
'''

# 1. LAMBDA USED WITH MAP:
'''
- The map() function in a python takes in function and an iterable (list, tuple, set, frozenset).
- The function is called with all the items in the list and a new list returned which contains items returned by that 
  function for each item.
'''

# Syntax:
'''
map(function, iterable)
'''

# EXAMPLE: 1
'''
def square(n):

  return n ** 2

Squares = map(square, range(1, 10))

print(list(Squares))
'''

# In better way

'''
print(list(map(lambda n: n ** 2, range(1, 10))))

print(tuple(map(lambda n: n ** 2, range(1, 10))))

print(set(map(lambda n: n ** 2, range(1, 10))))

print(frozenset(map(lambda n: n ** 2, range(1, 10))))
'''

# EXAMPLE: 2
'''
list1 = [5, 10, 15]
list2 = [20, 40, 60]

print(list(map(lambda x, y: x + y, list1, list2)))
'''

# EXAMPLE: 3
'''
ANIMALS = ['Guinea Pig', 'Panda', 'Chicken', 'Friends']

animal_uppercase = list(map(lambda x: x.upper(), ANIMALS))

print(animal_uppercase)
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 2. LAMBDA USED WITH FILTER:
'''
- The filter() function in python takes in a function and a list, tuple as a arguments.
- The function is called with all the items in the list and a new list is returned which contains items for which the 
  function evaluates to TRUE.
- Filter offers an elegant way to filter out all the elements of a list and tuple, for which the function returns TRUE.
'''

# Syntax:
'''
filter(function, sequence)
'''

# EXAMPLE: 1
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Even = list(filter(lambda x: x % 2 == 0, list1))

print(Even)
'''

# EXAMPLE: 2
'''
AGE = [18, 17, 25, 27, 26, 30, 27]

ADULTS = list(filter(lambda x: x > 18, AGE))

ADULTS1 = tuple(filter(lambda x: x > 18, AGE))

# ADULTS3 = set(filter(lambda x: x > 18, AGE))
# ADULTS = frozenset(filter(lambda x: x > 18, AGE))
'''

# EXAMPLE: 3
'''
Fibonacci_2 = [0,1,1,2,3,5,8,13,21,34,55,89]

Duplicate = set(filter(lambda x: x, Fibonacci_2))

print(Duplicate)
'''

# EXAMPLE: 4
'''
info = ['i','n','f','o','r','m','a','t','i','o','n']

Result = list(filter(lambda x: x!='o', info))

print(Result)
'''

# -------------------------------------------------------------------------------------------------------------------- #

# 3. LAMBDA USED WITH REDUCE:
'''
- The reduce() function in python takes in a function and a list as an argument.
- The function is called with a lambda function and an iterable and a new reduced result is returned.
- This performs a repetitive operation over the pairs of the iterable.
'''
# Syntax:
'''
reduce(function, iterable)
'''
from functools import reduce
# EXAMPLE: 1
'''
ADD = [1, 4, 9, 16, 25]
print(reduce(lambda x, y: x + y, ADD))
'''

# EXAMPLE: 2
'''
MAX = [1, 4, 9, 25, 10]
print(reduce(lambda x, y: x if x > y else y, MAX))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# FUNCTION ALIASING
'''
- In python programming, the second name given to a piece of data is known as an alias. 
- Aliasing happens when the value of one variable is assigned to another variable because variables are just names 
  that store references to actual value.
'''

# EXAMPLE: 1
'''
first_variable = "PYTHON"
print("Value of first:", first_variable)
print("Reference of first:", id(first_variable))

print("--------------")

second_variable = first_variable                    # making an alias

print("Value of second:", second_variable)
print("Reference of second:", id(second_variable))
'''

'''
# In the example above, first_variable is created first and then string ‘PYTHON’ is assigned to it. 
Statement first_variable = second_variable creates an alias of first_variable because 
first_variable = second_variable copies reference of first_variable to second_variable.
'''

# EXAMPLE: 2
'''
class Car:

    def change_oil(self):
        print('oil changed')

    def drive_to_cinema(self):
        print('movie watched')

    # Alias Method Names
    oil = change_oil
    cinema = drive_to_cinema


# Create new car object

porsche = Car()

# Test original and alias method calls

porsche.change_oil()

porsche.oil()

porsche.drive_to_cinema()

porsche.cinema()
'''

'''
You create one Car object porsche. The original method change_oil() may be too lengthy, so you decide to add an alias 
method to the class definition "oil = change_oil". Now, you can access the same method in two different ways: 
porsche.change_oil() or simply porsche.oil().
'''


# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○