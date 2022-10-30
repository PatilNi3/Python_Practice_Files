# LOOPING STATEMENT #
'''
- Looping statement are used to repeat a single statement or a set of statementas long as the desired condition is TRUE.
- Statements used to control loops and change the course of iteration are called control statements.
'''

# Why we use loops in python ?
'''
- The looping simplyfies the complex problems into the easy ones. 
- It enables us to alter the flow of the program so that instead of writting the same code for a finite number of times.
'''

# There are Two types of Loops Statements in Python
'''
1. For loop
2. While loop
'''

# Three Control Statements in Python
'''
1. Break
2. Continue
3. Pass
'''

# Content in Looping Statement:
'''
1. For loop
    1.1 The range() function
    1.2 For loop with else
    1.3 Nested for loop
    1.4 Break statement in for loop
    1.5 Continue statement in for loop
    1.6 Pass statement in for loop
2. While loop
    2.1 While loop with else
    2.2 Nested while loop
    2.3 Break statement in while loop
    2.4 Continue statement in while loop
    2.5 Pass statement in while loop
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. FOR LOOP :
'''
- The FOR LOOP used in the case where we need to execute some part of the code until the given condition is satisfied. 
- It is better to use FOR LOOP if the number of iteration is known in advance.
'''

# SYNTAX:
'''
FOR <iterating_variable> IN <sequence>:
    (statement)
'''
# Syntax Explained:
'''
- Here, iterating_variable is the variable that takes the value of the item inside the sequence on each iteration.
- Loop continues until we reach the last item in the sequence.
- The body of for loop is separated from the rest of the code using indentation.
'''

# EXAMPLE: 1
'''
Aspirants = ['Patience', 'Focus', 'Hard work', 'Smart work']

for iterating_variable in Aspirants:
    print(iterating_variable)
'''
# or
'''
for i in Aspirants:
    print(i)
'''

# EXAMPLE: 2
'''
for i in 'Mock':
    print(i)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1.1 The range() function
'''
- We can generate a sequence of numbers using range() function. 
- Range(10) will generate numbers from 0 to 9 (10 numbers).
- We can also define the start, stop and step size as range (start, stop, step_size). 
- Step_size defaults to 1 if not provided.
- To force this function to output all the items, we can use the function list().
  For Eg.: print(list(range(10)))
'''

# EXAMPLE: 1
'''
for i in range(10):
    print(i)
'''

# EXAMPLE: 2
'''
for x in range(5, 10):
    print(x)
'''

# EXAMPLE: 3
'''
for x in range(2, 11, 2):       # default step size is 1
    print(x)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1.2 For loop with else
'''
- A for loop can have an optional else block as well. 
- The else part is executed if the items in the sequence used in for loop exhausts.
- The break keyword can be used to stop a for loop. In such cases, the else part is ignored.
- Hence, a for loop's else part runs if no break occurs.
'''

# EXAMPLE: 1
'''
for y in range(0, 6) or range(6):
    print(y)
else:
    print("This prints when loop is finite")
'''

# EXAMPLE: 2
'''
string = "Python Loop"  

for s in string:
    if s == "o":  
        print("If block") 
    else:  
        print(s)
'''

# EXAMPLE: 3
'''
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)  
 
for value in tuple_:  
    if value % 2 != 0:  
        print(value)   
else:  
    print("These are the odd numbers present in the tuple") 
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1.3 Nested For loop
'''
- We know, Nested loop is a loop inside a loop.
- The "inner loop" will be executed one time for each iteration of the "outer loop"
'''

# EXAMPLE: 1
'''
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adjective:
    for b in fruits:
        print(a, b)
'''

# EXAMPLE: 2
'''
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print( )
'''

# EXAMPLE: 3
'''
for i in range(6):
    for j in range(i):
        print('*', end='')
    print('')
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1.4 Break statement in for loop
'''
- Break is used to terminate the loop or we can say iteration.
- With the break statement we can stop the loop before it has looped through all the items.
- Based on the given condition, the break statement stops the execution and brings the control out of the loop.
'''

# EXAMPLE: 1

District = ['Sangli', 'Kolhapur', 'Jalgaon', 'Nandurbar']
'''
for x in District:
    print(x)
    if x == 'Kolhapur':
        break
'''
# or
'''
for x in District:
    if x == 'Kolhapur':
        break
    print(x)
'''

# EXAMPLE: 2
'''
for y in 'Nitin':
    print(y)
    if y == 'i':
        break
'''
# or
'''
for y in 'Nitin':
    if y == 'i':
        break
    print(y)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1.5 Continue statement in for loop
'''
- Conitune is used to skip the iteration.
- Continue statement is used to skip the current iteration when the condition is met and allows the loop to continue 
  with the next iteration.
'''

# EXAMPLE: 1
'''
Laptop = ['Apple', 'Acer', 'HP', 'Asus']

for z in Laptop:
    if z == 'HP':
        continue
    print(z)
'''

# EXAMPLE: 2
'''
for n in 'Java':
    if n == 'v':
        continue
    print(n)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1.5 Pass statement in for loop
'''
- Pass statement is used when we want to do nothing when the condition is met. 
- It doesn’t skip or stop the execution, it just passes to the next iteration.
- We use pass statement to write empty loops. 
- Pass is also used for empty control statement.
'''

# EXAMPLE: 1
'''
List = [0, 1, 2, 3, 4]

for m in List:
    if m == 2:
        pass
    print(m)
'''

# EXAMPLE: 2
'''
List = [0, 1, 2, 3, 4]

for c in List:
    if c == 2:
        pass
print("The last element of List is: ", c)
'''

# EXAMPLE: 3
'''
for d in "Nitin":
    if d == 't':
        pass
    print(d)
'''

# EXAMPLE: 4
'''
for e in "Nitin":
    pass
print("The last letter in string is: ", e)
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

# 2 WHILE LOOP:
'''
- The while loop is used in the scenario where we don't know the iteration in advance. 
- The block of statement is executed in the while loop until the condition specified in the while loop is satisfied.
'''

# SYNTAX:
'''
WHILE <test expression>:
    (body of while)
'''
# Syntax Explaned:
'''
- In the while loop, test expression is checked first. The body of the loop is entered only if the test_expression 
  evaluates to TRUE.
- After one iteration, the test expression is checked again.
- This process continues until the test_expression evaluates to FALSE.
- In Python, the body of the while loop is determined through indentation.
- The body starts with indentation and the first unindented line marks the end.
'''

# EXAMPLE: 1
'''
counter = 0

while counter < 3: 
    print("Inside loop")
    counter = counter + 1
'''

# EXAMPLE: 2
'''
n = 10 
sum = 0
i = 1

while i <= n:
    sum = sum + 1
    i = i+1

print("The sum is", sum)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2.1 While loop with else
'''
- Same as with for loops, while loops can also have an optional else block.
- The else part is executed if the condition in the while loop evaluates to False.
- The while loop can be terminated with a break statement. In such cases, the else part is ignored. 
- Hence, a while loop's else part runs if no break occurs and the condition is false.
'''

# EXAMPLE: 1
'''
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Outside loop")
'''

# EXAMPLE: 2
'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''

# EXAMPLE: 3
'''
a = ['good', 'better', 'best']
s = 'ok'

i = 0
while i < len(a):
    print(i)
    i += 1
else:
    print('not found in list.')
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2.2 Nested While loop

# EXAMPLE: 1
'''
num = 1

even_numbers = []

while num <= 10:
    if num % 2 == 0:
        even_numbers.append(num)
    num += 1
print(even_numbers)
'''

# EXAMPLE: 2
'''
a = ['Zero', 'One', 'Two']
while len(a):
    print(a.pop(0))
    b = ['Three', 'Four']
    while len(b):
        print('>', b.pop(0))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2.3 Break statement in while loop

# EXAMPLE: 1
'''
count = 0

while count < 10:
    count += 1
    if count == 5:
        break
    print("inside loop", count)

print("out of while loop")
'''

# EXAMPLE: 2
'''
num = 1
odd_nums =[]

while num:
    if num % 2 != 0:
        odd_nums.append(num)
    if num >= 20:
        break
    num += 1
print("Odd numbers: ", odd_nums)
'''

# EXAMPLE: 3
'''
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2.4 Continue statement in while loop

# EXAMPLE: 1
'''
num = 0
while num < 10:
    num += 1
    if num == 6:
        continue
    print(num)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2.5 Pass statement in while loop
'''
num = 1
while num <= 10:
    if num == 6:
        pass
    print(num)
    num += 1
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

# PRACTICE VARIOUS PATTERNS

# EXAMPLE:
'''
N = 5
for i in range(N):
    print("*")
'''

# EXAMPLE:
'''
N = 5
for i in range(N):
    print("*", end="")
'''

# EXAMPLE:
'''
N = 5
for i in range(N):
    for j in range(N):
        print("*", end="  ")
    print()
'''

# EXAMPLE: INCREASING STAR TRIANGLE PATTERN
'''
N = 5
for i in range(N):
    for j in range(i+1):
        print("*", end=" ")
    print()
'''

# EXAMPLE: DECREASING STAR TRIANLE PATTERN
'''
N = int(input("Enter the number of rows here: "))
for i in range(N):
    for j in range(i, N):
        print("*", end=" ")
    print()
'''

# EXAMPLE: RIGHT SIDED TRIANGLE
'''
N = int(input("Enter the no. of rows here: "))
for i in range(N):
    for j in range(i, N):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
'''

# EXAMPLE: RIGHT SIDED TRIANGLE
'''
N = int(input("Enter the no. of rows here: "))
for i in range(N):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, N):
        print("*", end=" ")
    print()
'''

# EXAMPLE: HILL PATTERN
'''
N = int(input("Enter the no. of rows here: "))
for i in range(N):
    for j in range(i, N):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
'''

# EXAMPLE: REVERSE HILL PATTERN
'''
N = int(input("Enter the no. of rows here: "))
for i in range(N):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, N-1):
        print("*", end=" ")
    for j in range(i, N):
        print("*", end=" ")
    print()
'''

# EXAMPLE: DIAMOND PATTERN
'''
N = int(input("Enter the no. of rows here: "))
for i in range(N-1):
    for j in range(i, N):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(N):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(N-i):
        print("*", end=" ")
    for j in range(i, N-1):
        print("*", end=" ")
    print()
'''

# EXAMPLE: STRING PATTERN
'''
String = input("Enter the string here: ")
Length = len(String)

for i in range(Length):
    for j in range(i+1):
        print(String[j], end=" ")               # try String[i]
    print()
'''

# EXAMPLE: ALPHABET PATTERN
'''
N = int(input("Enter the no. of rows here: "))
Alpa = ord("A")

for i in range(N):
    for j in range(i+1):
        print(chr(Alpa), end=" ")
        Alpa = Alpa+1
    print()
'''

# EXAMPLE: ALPHABET PATTERN
'''
N = int(input("Enter the no. of the rows here: "))

for i in range(N):
    Alpha = ord("A")+i
    for j in range(i+1):
        print(chr(Alpha), end=" ")
    print()
'''

# EXAMPLE: ALPHABET PATTERN
'''
N = int(input("Enter the no. of the rows here: "))

for i in range(N):
    Alpha = ord("A")+i
    for j in range(i+1):
        print(chr(Alpha), end=" ")
        Alpha = Alpha+1
    print()
'''

# EXAMPLE: NUMBER PATTERN
'''
N = int(input("Enter the no. of rows here: "))

for i in range(N):
    for j in range(i+1):
        print(j, end=" ")
    print()
'''

# EXAMPLE: NUMBER PATTERN
'''
N = int(input("Enter the no. of rows here: "))

for i in range(1, N+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
'''

# EXAMPLE: PRIME NO. USING FOR LOOP
'''
START = int(input("Enter the starting no. : "))
END = int(input("Enter the ending no. : "))

for i in range(START, END+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
'''

# EXAMPLE: STAR TRIANGLE PATTERN
'''
N = int(input("Enter the no. of rows here: "))

for ROW in range(1, N+1):
    for COLUMN in range(1, N*2):
        if ROW==N or ROW+COLUMN==N+1 or COLUMN-ROW==N-1:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# EXAMPLE: STAR TRIANGLE PATTERN
'''
N = int(input("Enter the no. of rows here: "))
P = 2
for ROW in range(1, N+1):
    for COLUMN in range(1, N*2):
        if ROW+COLUMN==N+1 or COLUMN-ROW==N-1:
            print("*", end=" ")
        elif ROW==N and COLUMN!=P:
            print("*", end=" ")
            P = P+2
        else:
            print(" ", end=" ")

    print()
'''

# EXAMPLE: STAR TRIANGLE PATTERN
'''
N = int(input("Enter the no. of rows here: "))

for i in range(N):
    for j in range(N-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
'''


# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻
import csv

# with open("C:\\Users\\91960\\PycharmProjects\\MACHINE LEARNING\\ML\\Ecommerce Customers.csv") as file:
#     csv_file = csv.DictReader(file)
#     fname = []
#     for row in csv_file:
#         dict_converter = dict(row)
#         print(dict_converter)
#         f = dict_converter["fname"]
#         fname.append(f)
#         print(fname)




