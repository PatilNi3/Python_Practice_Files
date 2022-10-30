# # # DATE: 28/05/2022 # # #

# TYPES OF ERROR:
'''
Error means a mistake or the state of being wrong.
1. SYNTAX ERROR: A error which occurs because of invalid syntax.
2. RUNTIME ERROR: While executing the program if something goes wrong because of end user input or programming logic or
   memory problems etc then we will get runtime error.
   Also known as exception.
   Exception handling concept applicable for Runtime Errors but not for syntax errors.
'''

# WHAT IS EXCEPTION ?
'''
- An unwanted and unexpected event that disturbs normal flow of program is called Exception.
- Whenever an exception occurs, the program stops the execution, and thus the further code is not executed.
'''

# WHAT IS EXCEPTION HANDLING ?
'''
- Exception Handling does not mean repairing exception. We have to define alternative way to continue rest of the 
  program notmally.
- For Example: Our programming requirement is reading data from remote file locating at London. At runtime if london 
  file is not available then the program should not be terminated bnormally. We have to provide local file to continue 
  rest of the proram normally. This way of defining alternative is nothing but Exception Handling.
'''

# DIFFERENCE BETWEEN ERROR & EXCEPTION

# 1. Syntax Error:
'''
- A error which occurs because of invalid syntax. 
- It leads to the termination of the program. 
'''

# 2. Exception:
'''
- Exceptions are raised when the program is syntactically correct, but the code resulted in an error. 
- This error does not stop the execution of the program, however, it changes the normal flow of the program.
'''

# DIFFERENCE BETWEEN THE COMPILE ERROR ABD RUNTIME ERROR

# 1. Compile Error:
'''
Compiler errors are due to inaccuracies in code, where the compiler throws an error to alert you to 
something which will not compile, and therefore cannot be run.
Incomplete code or Inaccuracy in code
'''

# 2. Runtime Error:
'''
A runtime error in a program is an error that occurs while the program is running after being successfully compiled.
'''

# -------------------------------------------------------------------------------------------------------------------- #

# TRY - EXCEPT - ELSE - FINALLY
'''            
The "try" block lets you test a block of code for errors.

The "except" block lets you handle the error.

The "else" block lets you execute code when there is no error.

The "finally" block lets you execute code, regardless of the result of the try and except blocks.
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. TRY - EXCEPT
'''
- In Python, exceptions can be handled using a try statement.
- Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions 
  are kept inside the try clause and the statements that handle the exception are written inside except clause.
'''

# EXAMPLE: 1 -WITHOUT EXCEPTION HANDLING
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

z = x/y

print(z)
'''

# NOTE:
'''
- In above program, if we put x=5 and y=0 then we get error, "ZeroDivisionError: division by zero" and the further 
  program will stop from execution. So here we can try Exception Handling concept
'''

# EXAMPLE: 1.1 -WITH EXCEPTION HANDLING
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

try:
    z = x/y

except:
    print("Please enter correct number.")
'''

# EXAMPLE: 2
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

try:
    z = x/y
    print(z)

except:
    print("No need of except block")
'''

# BUILT IN EXCEPTION
'''
- Python has many built-in exceptions that enable our program to run without interruption and give the output. These 
  exceptions are given below:(MOST FREQUENT)

1. ZeroDivisionError
2. NameError
3. IndentationError
4. TypeError
5. SyntaxError and so on
'''

# EXAMPLE: 3 -CATCHING SPECIFIC EXCEPTIONS FROM ABOVE
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

try:
    z = x/y

except ZeroDivisionError:
    print("Please enter correct number.")
except SyntaxError:
    print("Please rewrite the code.")
'''

# EXPLANATION:
'''
- In the above program, we catched a specific error that we are expecting from the program.
- After passing the expected error in except block, we will not get any error in the output.
'''

# EXAMPLE: 4 -printing the error message(exception variable)
'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

try:
    z = x/y

except ZeroDivisionError as msg:
    print("Please enter correct number because,", msg)
'''

# EXPLANATION:
'''
- In above program, we passed an error in except block with msg.
- So after excution of except block, programmer like you get that msg; so that he/she can know where the exception/error 
  is occured.
'''

# EXAMPLE: 5
'''
try:
    print(z)

except SyntaxError:
    print("Please enter correct number.")

except:
    print("Please provide proper input.")
'''

# EXPLANATION:
'''
- In the above program, The exception occurs which does not matches with the exception block then other exception block is 
  executed.
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. TRY - EXCEPT - ELSE
'''
- In python, we can also use the else block on the try-except block which must be present after all the except block. 
- The code enters the else block only if the try clause does not raise an exception.
'''

# EXAMPLE: 1
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = (a+b)/(a-b)

except:
    print("Please enter correct no.")

else:
    print(c)
'''

# EXAMPLE: 2
'''
try:
    number = int(input("Please enter any no.: "))
    assert number % 2 == 0

except:
    print("Not a Even number")

else:
    print(number)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. TRY - FINALLY
'''
- The try statement in Python can have an optional finally block. This block is executed no matter what, and is generally 
  used to release external resources.
'''

# EXAMPLE: 1
'''
import csv
try:
    with open('Nitin.csv', 'r') as fp:
        r = csv.reader(fp)
        for i in r:
            print(i)

finally:
    print("Successful Excuation of try-finally")
'''

# NOTE:
'''
- In the above program, no matter weather try block and except block excuted or not but finally block will always execute.
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# RAISE EXCEPTION
'''
- As a Python developer you can choose to throw an exception if a condition occurs.
- We can also manually raise exceptions using the raise keyword.
'''

# EXAMPLE: 1 -WITHOUT USING TRY-EXCEPT
'''
x = int(input("Enter positive no.: "))

if x < 0:
    raise IOError("You have entered a no. below zero")
else:
    print(x)
'''

# EXAMPLE: 2 -WITH TRY EXCEPT
'''
try:
    Age = int(input("Enter your age for verification: "))
    if Age < 18:
        raise ValueError("You are underage")
    else:
        if Age >= 18 and Age < 60:
            print("You are eligible")
        else:
            print("You are simply not eligible.")

except ValueError as msg:
    print("Because,", msg)
    raise
'''

# EXAMPLE: 3 -TRY-EXCEPT WITH FOR LOOP
'''
list = ['Neha', 'Ruchita', 'Nitin']

try:
    for i in list:
        if i == 'Ruchita':
            raise NameError("KUCHKI")
except NameError as msg:
    print("Status:", msg)
    raise
'''



# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○