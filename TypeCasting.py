# TYPECASTING
'''
Typecasting is a method used to change the variable/values declared in a
certain data type into a different data type to match the operation required

• Int = int() function take float or string as an argument and return int type object.

• Float = float() function take int or string as an argument and return float type object.

• Str = str() function take int or float as an argument and return str type object.
'''

# EXAMPLE: 1
'''
STRING = '2609'
print(STRING)
print(type(STRING))
'''

# EXAMPLE: 2
'''
INTEGER = 2500
print(INTEGER)
print(type(INTEGER))
'''

# EXAMPLE: 3
'''
FLOAT = 25.25
print(FLOAT)
print(type(FLOAT))
'''

# EXAMPLE: 4
'''
T1 = INTEGER + FLOAT
print(T1)
print(type(T1))
'''

# EXAMPLE: 5
'''
T2 = INTEGER * FLOAT
print(T2)
print(type(T2))
'''

# EXAMPLE: 6
'''
T3 = 'STRING' + 'INTEGER'
print(T3)
print(type(T3))
'''

# EXAMPLE: 7
'''
T4 = 5 * STRING
print(T4)
print(type(T4))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXAMPLE: 8
'''
T6 = "50"
T7 = "5"

print(T6+T7)

print(int(T6)+int(T7))
'''

# EXAMPLE: 9
'''
T8 = 2
print(T8)

print(type(T8))

print(str(T8))

print(float(T8))

print(bool(T8))
'''

# EXAMPLE: 10
'''
T9 = 5+5j
print(T9)

print(type(T9))

print(str(T9))

print(type(str(T9)))
'''

# EXAMPLE: 11
'''
T10 = int(1)
print(T10)

T11 = int(2.8)
print(T11)

T12 = int("3")
print(T12)
print(type(T12))
'''

# EXAMPLE: 12
'''
T13 = float(1)
print(T13)

T14 = float(2.8)
print(T14)

T15 = float("3")
print(T15)
'''

# EXAMPLE: 13
'''
T16 = [1, 1, 1, 2, 3, 4, 5]
print(T16)
print(type(T16))

print(tuple(T16))
print(type(tuple(T16)))

T17 = set(T16)
print(T17)
print(type(T17))

T18 = str(T16)
print(T18)
print(type(T18))

T19 = frozenset(T16)
print(T19)
print(type(T19))

T20 = dict(T16)
print(T20)
print(type(T20))
'''
