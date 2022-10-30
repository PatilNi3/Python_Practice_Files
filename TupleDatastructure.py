# TUPLE DATA STRUCTURE #
'''
- Python Tuple is a collection of objects separated by commas.
- A Tuple represents a collection of objects that are ordered.
- Tuple is immutable type datastructure. (The Tuple cannot be changed, which means you cannot update or change the values, not even delete the tuple elements)
- Tuples are more memory efficient than lists.
- Tuple allows duplicate elements and are indexed.
'''

# EXAMPLE:
'''
TUPLE = ('NITIN', 2311, 'NEHA', 1704, 'RUCHITA', 702, 'ANKITA', 1009)

print(TUPLE)

print(len(TUPLE))           # len() - length of tuple

print(type(TUPLE))          # type() - type of data structure
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# INDEX
'''
Find out the index no. of element by using element itself.
'''

# EXAMPLE: 1
'''
T1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(T1)

print(T1.index(36))

print(T1.index(64))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# COUNT
'''
Gives the count of repeating elements.
'''

# EXAMPLE: 1
'''
T2 = (4, 4, 4, 9, 16, 25, 25, 25, 25, 25, 36, 49, 64, 81, 81)
print(T2)

print(T2.count(25))

print(T2.count(4))

print(T2.count(36))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# CONCAT
'''
We can add elements in tuple by using concat.
'''

# EXAMPLE: 1
'''
T3 = (5, 25, 125)
T4 = (125, 100, 1000)
T41 = (500,)

print(T3+T4)

print(T3+T41)

print(T3*3)
'''

# EXAMPLE: 2
'''
T5 = (23, 11, 19.95)
T6 = ('Nitin', 'Patil')

T7 = T5+T6
print(T7)

print(len(T7))

print(type(T7))
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

'''
T8 = ()

print(T8)

print(len(T8))

print(type(T8))
'''

# TUPLE OF TUPLE
'''
T9 = ((1, 2), (23.11, 19.95), ('Python', 'Tuple'), ('Integer', 1), ('Float', 25.5))
print(T9)

print(len(T9))

print(type(T9))
'''

# help(tuple)