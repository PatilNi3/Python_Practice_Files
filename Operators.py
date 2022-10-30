# OPERATORS
'''
- Operators are used to perform operations on variables and values.
- Python defines the operators in the following groups:
   1. Arithmetic Operator
   2. Logical Operator
   3. Comparison Operator
   4. Assignment Operator
   5. Membership Operator
   6. Identity Operator
   7. Bitwise Operator
   8. Ternary Operator
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. ARITHMETIC OPERATOR:
'''
+ = Addition
- = Substraction
* = Multiplication
/ = Division (gives float)
% = Modulus (gives remainder)
** = Exponential (gives power)
// = Floor Division (gives floor)
'''
# EXAMPLES:
'''
print("Examples of Arithmetic Operator:")

a = 25
b = 5
c = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a % c)
print(a ** b)
print(a // b)
print(a // c)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. LOGICAL OPERATOR:
'''
and = Returns True if both statements are True. (x<5 and x<10)
or = Returns True if one of the statement is True. (x<5 or x<4)
not = Reverse the result, returns False if the result is True. (not(x<5 and x<10))

# EXAMPLES:

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. COMPARITIVE OPERATOR:
'''
# == Equal
# != Not Equal
# > Greater than
# < Less than
# >= Greater than or Equal to
# <= Less than or Equal to
'''
# EXAMPLES:
'''
a = 100
b = 50

print(a == b)
print(a != b)
print(a > b)
print(b > a)
print(a < b)
print(b < a)
print(a >= b)
print(b >= a)
print(a <= b)
print(b <= a)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 4. ASSIGNMENT OPERATOR:
'''
=   Eg. x = 25 (assign value)
+=  Eg. x += 5 or x = x+5 (add and assign value to the left operand)
-=  Eg. x -= 5 or x = x-5 (substract and assign value to the left operand)
*=  Eg. x *= 5 or x = x*5 (multiply and assign value to the left operand)
/=  Eg. x /= 5 or x = x/5 (devide and assign value to the left operand)
%=  Eg. x %= 5 or x = x%5 (modulus and assign value to the left operand)
//= Eg. x //= 5 or x = x//5 (devide(floor) and assign value to the left operand)
**= Eg. x **= 5 or x = x**5 (power and assign value to the left operand)
'''
# EXAMPLES:
'''
a = 25

b = a
# print(b)

# b = b+5
# print(b)
# b += 5
# print(b)

# b = b-5
# print(b)
# b -= 5
# print(b)

# b = b*5
# print(b)
# b *= 5
# print(b)

# b = b/5
# print(b)
# b /= 5
# print(b)

# b = b%5
# print(b)
# c = b%3
# print(c)

# b = b//5
# print(b)
# c = b//3
# print(c)

# b = b**5
# print(b)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 5. MEMBERSHIP OPERATOR:
'''
in = Returns True if the sequence of the secified value is present in the object. (x in y)
not in = Returns True if the sequence of the secified value is not present in the object. (x not in y)
'''
# EXAMPLES:
'''
a = 50
b = 25

list1 = [50, 100, 200, 400, 800]

print(a in list1)
print(b in list1)

print(a not in list1)
print(b not in list1)
'''

# EXAMPLES:
'''
dictionary = {'M' : 'Male', 'F' : 'Female', 'DoB' : 'Date of Birth'}
print('DoB' in dictionary)
print('F' in dictionary.keys())
print('Male' in dictionary.values())
'''

# EXAMPLES:
'''
o1 = 'Python'
print('P' in o1)
print('P' not in o1)

#

o2 = 'Python is better than c++, java'
print('is' in o2)
print('+' in o2)
'''

# EXAMPLES:
'''
if a in list1:
    print("Yes. a is in list1")
else:
    print("a is not in list")

#

if b not in list1:
    print("b not in list1")
else:
    print("Yes. b is in list1")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 6. IDENTITY OPERATOR
'''
is = Returns True if both variables are the same object. (x is y)
is not = Returns True if both variables are not the same object. (x is not y)
'''
# EXAMPLES:
'''
a = 50
b = 25
c = 50

print(a is b)
print(a is c)

print(a is not b)
print(a is not c)

print(a == c)
'''

# EXAMPLES:
'''
m = 50000
n = 50000

print(id(m))
print(id(n))

print(m is n)
print(id(m) == id(n))
print(id(m) is id(n))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 7. BITWISE OPERATOR
'''
& = AND = Sets each bit to 1 if both bits are 1.
| = OR = Sets each bit to 1 if one of two bits is 1.
~ = NOT = Inverts all the bits.
'''
# EXAMPLES:
'''
a = 1
b = 1
c = 0

print(a & b)
print(a & c)

print(a | b)
print(a | c)

print(~c)
print(not c)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 8. TERNARY OPERATOR
'''
Ternary operators are also known as conditional expressions are operators that evaluate something based on a condition 
being true or false.
[true] if [expression] else [false]
'''
# EXAMPLES:
'''
a, b = 10, 20

# or

a = 10
b = 20

Ans = a if a < b else b
print(Ans)
'''

# EXAMPLES:
'''
a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

print(a, "is greater") if (a>b) else print(b, "is greater")
'''


# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻