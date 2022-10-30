# STRING DATA STRUCTURE #
'''
- It is a collection of characters. 
- It is a immutable type datastructure.
- We can define string in single quote(' '), double quote(" "), triple single quote('''  '''), triple double quote("""  """)
- Highest priority is given to the string.
'''

# EXAMPLE:
'''
s = 'PYTHON'
print(s)

print(type(s))

print("KGF",'\n',"KGF2")
'''

# DIFFERENT  TYPES OF QUOTES
"""
single = 'Python'
print("String by using single quote:")
print(single)

double = "Python"
print("String by using double quote:")
print(double)

triple_single = '''Python'''
print("String by using triple single quote:")
print(triple_single)

print("Example showing use of triple single quote that is used in multiline string:")

EgTSQ = '''According to Thomas Edison,
        "Genius is one per cent inspiration
        and
        ninety-nine per cent perspiration."'''
print(EgTSQ)
"""
'''
triple_double = """Python"""
print("String by using triple double quote:")
print(triple_double)

print("Example showing use of triple double quote that is used in multiline string:")

EgTDQ = """Python is a dynamically typed language.
        Dynamic means, We don't have to declare the type of variable
        while assigning a value to a variable in Python.
        Other languages like C, C++, Java, etc.., there is a strict declaration of
        variables before assigning values to them."""
print(EgTDQ)
'''

#If data having single quote then we should use double quote and vice versa
#Triple single quote and triple double quote used in multiline string.

# EXAMPLE:
'''
s0 = 'Python is a Dynamically typed language, it's also extensible language'
print(s0)
# # It is throwing "SyntaxError" because data having single quote and we enclosing string with also single quote.
'''
'''
# Updated s0 is,

s1 = "Python is a Dynamically typed language, it's also extensible language."
print("Updated string s0 is:")
print(s1)
'''
# EXAMPLE:

# Taking input from user
'''
s2 = input("Enter a number: ")
print(s2)

print(type(s2))

print(int(s2))
print(type(int(s2)))

print(float(s2))
print(type(float(s2)))
'''

# DOCSTRING
"""
Doc string means documented string, informative string.

print("It is used to inform other developer that whats going on in this program. The docstrings are declared using 
'''triple single quote''' or “””triple double quotes””” just below the class, method or function declaration.")
"""

# STRING FUNCTIONS #

# CAPITALIZE
'''
Make the first character have upper case and the rest lower case.
'''
# EXAMPLE: 1
'''
s1 = "python"
print(s1.capitalize())
'''
# EXAMPLE: 2
'''
s101 = "capitalizing"
s102 = " first"
s103 = " letter"
print(s101.capitalize() + s102.capitalize() + s103.capitalize())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# UPPER
'''
Return a copy of the string converted to uppercase.
'''
# EXAMPLE: 1
'''
s2 = "python is a begginer level language."
print(s2.upper())
'''
# EXAMPLE: 1
'''
s201 = "PYTHON IS A BEGGINER LEVEL LANGUAGE."
print(s201.isupper())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# LOWER
'''
Return a copy of the string converted to lowercase.
'''
# EXAMPLE: 1
'''
s3 = "PYTHON IS HIGH LEVEL LANGUAGE THAT IS, ITS A USER UNDERSTANDABLE."
print(s3.lower())
'''
# EXAMPLE: 1
'''
s301 = "python is high level language means its a user understandable."
print(s301.islower())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SPLIT
'''
Return a list of the words in the string, using sep as the delimiter string.
'''
# EXAMPLE: 1
'''
s4 = "Python is interpreter based language."
print(s4)

print(s4.split(' '))

print(s4.split('t'))
'''
# EXAMPLE: 2
'''
s401 = "Python is very good language for ml, its also used in visualization."
print(s401.split('ml')[0] + 'ML' + s401.split('ml')[1])
'''
# EXAMPLE: 3
'''
s402 = "nitinpatilnp260923.np@gmail.com"
print(s402.split('@'))

print(s402.split('@')[0])
print(s402.split('@')[1])
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# TITLE
'''
Return a version of the string where each word is titlecased.
'''
# EXAMPLE: 1
'''
s5 = "nitin patil is mechanical engineer."
print(s5.title())
'''
# EXAMPLE: 2
'''
s501 = "Nitin Patil Is Mechanical Engineer"
print(s501.istitle())
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# STRIP
'''
Return a copy of the string with leading and trailing whitespace removed.
'''
# EXAMPLE: 1
'''
s6 = "   Why   "
print(s6.strip())
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# LSTRIP
'''
Return a copy of the string with leading whitespace removed.
'''
# EXAMPLE: 1
'''
s7 = "   Why   "
print(s7.lstrip())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# RSTRIP
'''
Return a copy of the string with trailing whitespace removed.
'''
# EXAMPLE: 1
'''
s8 = "   Why   "
print(s8.rstrip())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# STARTSWITH
'''
Return True if string starts with the specified prefix, False otherwise.
'''
# EXAMPLE: 1
'''
s9 = 'According to Thomas Edison, "Genius is one per cent inspiration and ninety-nine per cent perspiration."'

print(s9.startswith("Acc"))

print(s9.startswith('"Genius'))
'''
# EXAMPLE: 2
'''
s901 = "nitinpatilnp260923.np@gmail.com"

print(s901.split('@')[0].startswith('nitin'))

print(s901.split('@')[1].startswith('g'))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ENDSWITH
'''
Return True if string ends with the specified suffix, False otherwise.
'''
# EXAMPLE: 1
'''
s10 = 'According to Thomas Edison, "Genius is one per cent inspiration and ninety-nine per cent perspiration."'

print(s10.endswith('ion."'))

print(s10.endswith("Acc"))
'''
# EXAMPLE: 2
'''
s1001 = "nitinpatilnp260923.np@gmail.com"

print(s1001.split('.')[0].endswith('23'))
print(s1001.split('.')[1].endswith('l'))
print(s1001.split('.')[2].endswith('com'))
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# FIND
'''
Return the lowest index in string where substring sub is found.
'''
# EXAMPLE: 1
'''
s11 = "Python is procedure oriented & object oriented"

print(s11.find('is'))
print(s11.find('&'))
print(s11.find('in'))
'''
# EXAMPLE: 2
'''
Adv_Python = "Python is procedure oriented & object oriented"
to_find = input("Enter a string: ")

if Adv_Python.find(to_find)!= -1:
    print("Given string present in statement.")
else:
    print("Given string is not present in statement.")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# FORMAT
'''
Return a formatted version of string.

Syntax       = { }.format(value)    <value can be intefer, float, string, characters or even variable>
             = { } { }.format(value1, value2)
             = {0} {1}.format(positional_argument, keyword_argument)
             = {key}.format(**{key:value})
             
'''
# EXAMPLE: 1
'''
print("{} is an integrated development environment used in {}.".format("PyCharm", "computer programming"))
'''

# EXAMPLE: 2
'''
s11 = "We are learning {} now."
print(s11.format("Python"))
'''

# EXAMPLE: 3
'''
print("My self {}, I'm from {}. I completed my bachelor's in {}.".format("Nitin Patil", "Sangli", 2018))

print("My self {}, I'm from {}. I completed my bachelor's in {}".format("Nitin Patil", "Sangli"))
'''

# EXAMPLE: 4
'''
print("{0} loves {1}.".format("Nitin", "Mercedes"))
print("{1} loves {0}.".format("Nitin", "Mercedes"))
'''
# EXAMPLE: 5
'''
Dialogue = {"love" : 3000}

Morgan = "Tony loves his daughter {love} times"

print(Morgan.format(**Dialogue))
'''

# EXAMPLE: 6
'''
Nitin = {"Branch" : "Mechanical", "Course" : "CAD"}

About = "Nitin is from {Branch} Engineering and having knowledge of {Course}"

print("Nitin is from {N[Branch]} Engineering and having knowledge of {N[Course]}.".format(N=Nitin))
'''

# EXAMPLE: 7
'''
x = 25
y = 125
z = x+y
# print(z)

print("Addition of {} & {} is {}.".format(x, y, z))
print("Addition of {} & {} is {}.".format(x, z, y)) # x + y = z , 25 + y = 150 , y = 150 - 25 , y = 125
'''

# EXAMPLE: 8
'''
u = 555
v = 55
w = u-v
# print(w)

print("Substraction of {} & {} is {}.".format(u, v, w))
print("Substraction of {} & {} is {}.".format(u, w, v))
'''

# EXAMPLE: 9
'''
r = 25
s = 5
t = r*s
# print(t)

print("Multiplication of {} & {} is {}.".format(r, s, t))
'''

# EXAMPLE: 10
'''
p = r/s
print(p)
print("The Division of {} & {} is {}.".format(r, s, p))
'''

# EXAMPLE: 11
'''
a1 = 'python'
a2 = 'c'
a3 = 'Cython'

b2 = 'java'
b3 = 'Jython'

c2 = '.net'
c3 = 'Iron python'

d2 = 'ruby'
d3 = 'Ruby python'

print("Addition of {} & {} is {}.".format(a1, a2, a3))
print("Addition of {} & {} is {}.".format(a1, b2, b3))
print("Addition of {} & {} is {}.".format(a1, c2, c3))
print("Addition of {} & {} is {}.".format(a1, d2, d3))
'''

# EXAMPLE: 12
'''
date and time in Format String Function. Import date and datetime.
'''
from datetime import date
'''
today = date.today()
print("Todays date:", today)
'''
from datetime import datetime
'''
cdt = datetime.now()
print(cdt)
'''
import datetime
'''
f = datetime.datetime.now()
print(f)
'''
import datetime
'''
j = datetime.date.today()
print(j)

print("Year:", end = "")
print(j.year)
print(j.month)
print(j.day)
'''
from datetime import date
'''
today = date.today()

s11 = today.strftime("%d/%m/%y")
print("A:", s11)

s12 = today.strftime("%b %d, %y")
print("B:", s12)

s13 = today.strftime("%B-%d-%y")
print("C:", s13)

s14 = today.strftime("%y/%m/%d")
print("D:", s14)
'''
from datetime import datetime
'''
Now = datetime.now()
DMY = Now.strftime("%d/%m/%y %H:%M:%S")
print("date and time is:", DMY)
'''
from datetime import date
'''
image = "pic_{}.jpg".format(date.today())
print(image)
'''
import datetime
'''
f = datetime.datetime.now()
image1 = "pic_{}.png".format(f.year)
print(image1)
print(f"pic_{f}.img")
'''
# EXAMPLE: 13
'''
x = 25
y = 125
z = x+y
print(z)

print(f"Addition of {x} & {y} is {z}")
'''

# A-Z or a-z - Alphabetic - isalpha
# 54321 - Numeric - isnumeric
# Python29startsat13Mar - AlphaNumeric - isalnum

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISALPHA
'''
Return True if the string is an alphabetic string, False otherwise.
'''
# EXAMPLE: 1
'''
s17 = "Nitin"

print(s17.isalpha())
print(s17.isnumeric())
print(s17.isalnum())
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISNUMERIC
'''
Return True if the string is a numeric string, False otherwise.
'''
# EXAMPLE: 1
'''
s18 = '9604332227'

print(s18.isalpha())
print(s18.isnumeric())
print(s18.isalnum())
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISALNUM
'''
- Return whether the string is Alphabetic or Numeric, if anyone of them then True; else False.
- It is a combination of Alhabetic and Numeric.
'''
# EXAMPLE: 1
'''
s19 = "Ni3"

print(s19.isalpha())
print(s19.isnumeric())
print(s19.isalnum())
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SWAPCASE
'''
Convert uppercase characters to lowercase and lowercase characters to uppercase.
'''
# EXAMPLE: 1
'''
s20 = "UNOFFICIAL PYTHON"
print(s20.swapcase())

s211 = "unofficial python"
print(s211.swapcase())

s212 = "UnOfficial Python"
print(s212.swapcase())
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# REPLACE
'''
Return a copy with all occurrences of substring old replaced by new.
'''
# EXAMPLE:
'''
s21 = "We is preparing for Data Science to get higher package."

print(s21.replace('is', 'are'))
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

# STRING SLICING #
'''
- String slicing in Python is about obtaining a sub-string from the given string by slicing it respectively from start to end. 
'''
# EXAMPLE: 1
'''
S1 = "nitinpatilp29@gmail.com"

print(S1[0:23:1])           # to see full string [ start (including) : stop (including) : step (default 1) ]

print(S1[1:23:2])

print(S1[1:15:1])

print(S1[1:15])

print(S1[-1:23:1])

print(S1[1:23:-1])          # no output

print(S1[-2:23])

print(S1[-2:-1])

print(S1[ : :1])            # to see full string

print(S1[::-1])             # to reverse the string
'''

# EXAMPLE: 2
'''
USER_STR = input("Enter STRING here: ")

if USER_STR == USER_STR[::-1]:
    print(f"Entered STRING {USER_STR} is palindrom")
else:
    print(f"Entered STRING {USER_STR} is not palindrom")
'''


# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

# CREATING DICTIONARY USING TWO TUPLES
'''
T1 = (1, 2, 3, 4, 5)
T2 = ("ONE", "TWO", "THREE", "FOUR", "FIVE")

Dictionary = dict(zip(T1, T2))
print(Dictionary)
'''

# CREATING DICTIONARY USING TWO LIST
'''
L1 = [1, 2, 3, 4, 5]
L2 = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

Dictionary = dict(zip(L1, L2))
print(Dictionary)
'''

# CREATING TUPLE OF TUPLE USING TWO TUPLE
'''
T11 = (1, 2, 3, 4, 5)
T12 = ("ONE", "TWO", "THREE", "FOUR", "FIVE")

Tuple = tuple(zip(T11, T12))
print(Tuple)
'''

# CREATING TUPLE OF TUPLE USING TWO LIST
'''
L11 = [1, 2, 3, 4, 5]
L12 = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

Tuple = tuple(zip(L11, L12))
print(Tuple)
'''

# CREATING LIST OF TUPLE USING TWO TUPLE
'''
T11 = (1, 2, 3, 4, 5)
T12 = ("ONE", "TWO", "THREE", "FOUR", "FIVE")

List = list(zip(T11, T12))
print(List)
'''

# CREATING LIST OF TUPLE USING TWO LIST
'''
L11 = [1, 2, 3, 4, 5]
L12 = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

List = list(zip(L11, L12))
print(List)
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻


