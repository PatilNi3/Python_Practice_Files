# FROZENSET
'''
- It is a immutable, unordered collection of unique elements.
- We can not have duplicate values in the frozenset
'''

# EXAMPLE: 1
'''
FROZENSET = {1, 1, 1, 2, 3, 4, 5}

print(frozenset(FROZENSET))

print(type(FROZENSET))
'''

# EXAMPLE: 2
'''
FROZENSET1 = frozenset({"List", "Tuple", "Set", "Dict", "String", "Frozenset"})

print(FROZENSET1)

print(type(FROZENSET1))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

'''
F1 = frozenset({2, 3, 5, 7, 11, 13, 17, 19})
print(F1)

F1.add(23)                  # AttributeError
print(F1)

F1.remove(1, 0)             # AttributeError
print(F1)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# UNION
'''
Return the union of sets as a new set.
'''

# EXAMPLE: 1
'''
F2 = frozenset({1, 2, 2, 3, 3, 3, 4, 4, 4, 4})
F3 = frozenset({5, 6, 7, 8, 9, 10})

print(F2.union(F3))
'''

# EXAMPLE: 2
'''
F4 = frozenset({"Int", "Float", "Str", "Bool", "Complex"})
F5 = frozenset({"List", "Tuple", "Set", "Dict", "Str", "Frozenset"})

F6 = F4.union(F5)
print(F6)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# INTERSECTION
'''
Return the intersection of two sets as a new set.
'''

# EXAMPLE: 1
'''
F7 = frozenset({2, 4, 6, 8, 10})
F8 = frozenset((1, 2, 3, 4, 5))

print(F7.intersection(F8))
'''

# EXAMPLE: 2
'''
F9 = frozenset({"Amol", "Babu", "Shona", "Kiran", "Shital"})
F10 = frozenset({"Archana", "Pratima", "Shital", "Kiran"})

F11 = F9.intersection(F10)
print(F11)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISDISJOINT
'''
Return True if two sets have a null intersection.
'''

# EXAMPLE: 1
'''
F12 = frozenset({"Harley Davidson", "Ducati", "BMW"})
F13 = frozenset({"Activa", "Access125", "Jupiter"})

print(F12.isdisjoint(F13))
'''

# EXAMPLE: 2
'''
F14 = frozenset({"Harley Davidson", "Ducati", "BMW", "Mercedes car"})
F15 = frozenset({"Activa", "Access125", "Jupiter", "Mercedes car"})

print(F14.isdisjoint(F15))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISSUBSET
'''
Report whether another set contains this set.
'''

# EXAMPLE: 1
'''
F16 = frozenset({2, 3, 5, 7, 11, 13})
F17 = frozenset({3, 5, 7, 11, 13})

print(F17.issubset(F16))

print(F16.issubset(F17))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISSUPERSET
'''
Report whether this set contains another set.
'''

# EXAMPLE: 1
'''
F18 = frozenset({2, 3, 5, 7, 11, 13})
F19 = frozenset({3, 5, 7, 11, 13})

print(F18.issuperset(F19))

print(F19.issuperset(F18))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# DIFFERENCE
'''
Return the difference of two or more sets as a new set.
'''

# EXAMPLE: 1
'''
F20 = frozenset({"Accenture", "Infosys", "TCS", "Wipro", "Oracle"})
F21 = frozenset({"TCS", "Wipro", "M&M", "Infosys" })

F22 = F20.difference(F21)
print(F22)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SYMMETRIC DIFFERENCE
'''
Return the symmetric difference of two sets as a new set.
'''

# EXAMPLE: 1
'''
F23 = frozenset({"python", "Django", "sql", "mongoDB", "ML", "deep learning", "statistics"})
F24 = frozenset({"python", "Django", "sql", "mongoDB", "eda", "power BI", "etl"})

F25 = F23.symmetric_difference(F24)
print(F25)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# COPY
'''
Return a shallow copy of a set.
'''

# EXAMPLE: 1
'''
F26 = frozenset({"25 lakh", "30lakh", "35 lakh"})

F27 = F26.copy()
print(F27)
'''

# help(frozenset)