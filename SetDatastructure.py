# SET DATA STRUCTURE #
'''
- Set is a collection of unordered and unindexed elements.
- Every element in a Set is always unique, It means it does not allow any duplication of element.
- Set is mutable type data structure.
- At least have 1 element should be there otherwise it will consider as dictionary.
'''

# EXAMPLE: 1
'''
SET = {0}
print(SET)
print(type(SET))
'''

# EXAMPLE: 2
'''
SET1 = {"python", 4, "sql", 1, "java", 9}
print(SET1)
'''

# EXAMPLE: 3
'''
SET2 = {1, 1, 1, 2, 3, 4, 4, 5}
print(SET2)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ADD
'''
Add an element to a set.
'''

# EXAMPLE: 1
'''
S1 = {2, 4, 6, 8, 10}
print(S1)

S1.add(25)
print(S1)

S1.add(50)
print(S1)

S1.add(100)
print(S1)
'''

# EXAMPLE: 2
'''
S2 = {"python", "java", "angular"}
print(S2)

S2.add("HTML")
print(S2)

S2.add("JS")
print(S2)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# UPDATE
'''
Update a set with other element
'''

# EXAMPLE: 1
'''
S3 = {1, 3, 5, 7, 9}
print(S3)

S3.update({25, 50, 75, 100})
print(S3)
'''

# EXAMPLE: 2
'''
S4 = {"python", "java", "angular"}
print(S4)

S4.update({"html", "sql"})
print(S4)
'''

# EXAMPLE: 3
'''
S5 = {5, 10, 15, 20}
S6 = {25, 30, 35, 40}

S6.update(S5)
print(S6)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# REMOVE
'''
Remove an element from a set; it is must be a member.
'''

# EXAMPLE: 1
'''
S7 = {2, 4, 6, 8, 10}
print(S7)

S7.remove(6)
print(S7)
'''

# EXAMPLE: 2
'''
S8 = {"python", "java", "angular"}
print(S8)

S8.remove("java")
print(S8)
'''

# EXAMPLE: 3
'''
S9 = {2, 4, 6, 8, 10}
print(S9)

S9.remove(12)               # KeyError
print(S9)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# DISCARD
'''
Remove an element from a set if it is a member.
'''

# EXAMPLE: 1
'''
S10 = {1, 3, 5, 7, 9}
print(S10)

S10.discard(5)
print(S10)

S10.discard(11)
print(S10)
'''

# EXAMPLE: 2
'''
S11 = {"python", "java", "angular"}
print(S11)

S11.discard("java")
print(S11)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# POP
'''
Remove and return an arbitrary set element.
'''

# EXAMPLE: 1
'''
S12 = {2, 4, 6, 8, 10}
print(S12)

print(S12.pop())
print(S12)

print(S12.pop())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# UNION
'''
Return the union of sets as a new set.
'''

# EXAMPLE: 1
'''
S13 = {5, 10, 15, 25}
S14 = {25, 30, 35, 40}

print(S13.union(S14))

print(S14.union(S13))
'''

# EXAMPLE: 2
'''
S15 = {"Apple", "Microsoft", "Google"}
S16 = {"Twitter", "Facebook", "Whatsapp"}

print(S15.union(S16))
'''

# EXAMPLE: 3
'''
S17 = {"Apple", "Microsoft", "Google"}
S18 = {"Apple", "Windows", "Google"}

print(S17.union(S18))
'''

# EXAMPLE: 4
'''
S19 = {"Apple", "Google"}

print(S19.union("Hiii"))
'''

# EXAMPLE: 5
'''
S20 = {"Apple", "Google"}

print(S20.union({"Hiii"}))
'''

# EXAMPLE: 6
'''
S21 = {5, 10, 15, 20, 25}

print(S21.union({100, 200, 300}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# INTERSECTION
'''
Return the intersection of two sets as a new set.
'''

# EXAMPLE: 1
'''
S22 = {1, 2, 3, 4, 5}
S23 = {2, 4, 6, 8}

print(S22.intersection(S23))
'''

# EXAMPLE: 2
'''
S24 = {"Apple", "Microsoft", "Google"}
S25 = {"Apple", "Windows", "Google"}

print(S24.intersection(S25))
'''

# EXAMPLE: 3
'''
S26 = {"Apple", "Microsoft", "Google"}
S27 = {"Twitter", "Facebook", "Whatsapp"}

print(S26.intersection(S27))
'''

# EXAMPLE: 3
'''
S28 = {"Microsoft", "Facebook", "NVDIA"}

print(S28.intersection({"NVDIA"}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISDISJOINT
'''
Return True if two sets have a null intersection.
'''

# EXAMPLE: 1
'''
S29 = {1, 4, 9, 16, 25}
S30 = {36, 49, 64, 81, 100}

print(S29.isdisjoint(S30))
'''

# EXAMPLE: 2
'''
S31 = {1, 4, 9, 16, 25}
S32 = {25, 49, 64, 81, 100}

print(S31.isdisjoint(S32))
'''

# EXAMPLE: 3
'''
S33 = {1, 4, 9, 16, 25}

print(S33.isdisjoint({49}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# INTERSECTION UPDATE
'''
Update a set with the intersection of itself and another.
'''

# EXAMPLE: 1
'''
S34 = {1, 2, 3, 4, 5}
S35 = {2, 4, 6, 8}

S34.intersection_update(S35)
print(S34)

S35.intersection_update(S34)
print(S35)
'''

# EXAMPLE: 2
'''
S36 = {"Apple", "Microsoft", "Google"}
S37 = {"Apple", "Windows", "Google"}

S36.intersection_update(S37)
print(S36)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# DIFFERENCE
'''
Return the difference of two or more sets as a new set.
'''

# EXAMPLE: 1
'''
S38 = {1, 2, 3, 4, 5}
S39 = {2, 4, 6, 8}

print(S38.difference(S39))
'''

# EXAMPLE: 2
'''
S40 = {"Apple", "Microsoft", "Google"}
S41 = {"Apple", "Windows", "Google"}

print(S40.difference(S41))

print(S41.difference(S40))
'''

# EXAMPLE: 3
'''
S42 = {0, 1, 2, 3, 4}
S43 = {0, 1, 2, 3, 4}

print(S42.difference(S43))
'''

# EXAMPLE: 4
'''
S44 = {10, 9, 8, 7, 6}

print(S44.difference({2, 4, 6, 8, 10}))
'''

# EXAMPLE: 5
'''
S45 = {10, 9, 8, 7, 6}

print(S45.difference({6, 7, 8, 9, 10}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# DIFFERENCE UPDATE
'''
Remove all elements of another set from first set.
'''

# EXAMPLE: 1
'''
S46 = {1, 2, 3, 4, 5}
S47 = {2, 4, 6, 8}

S46.difference_update(S47)
print(S46)

S47.difference_update(S46)
print(S47)
'''

# EXAMPLE: 2
'''
S48 = {"Apple", "Microsoft", "Google"}
S49 = {"Apple", "Windows", "Google"}

S48.difference_update(S49)
print(S48)
'''

# EXAMPLE: 3
'''
S50 = {0, 1, 2, 3, 4}

S50.difference_update({0, 2, 4})
print(S50)
'''

# EXAMPLE: 4
'''
S51 = {0, 1, 2, 3, 4}

S51.difference_update({0, 1, 2, 3, 4})
print(S51)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SYMMETRIC DIFFERENCE
'''
Return the symmetric difference of two sets as a new set.
'''

# EXAMPLE: 1
'''
S52 = {1, 2, 3, 4, 5}
S53 = {2, 4, 6, 8}

print(S52.symmetric_difference(S53))
'''

# EXAMPLE: 2
'''
S54 = {"Apple", "Microsoft", "Google"}
S55 = {"Apple", "Windows", "Google"}

print(S54.symmetric_difference(S55))
'''

# EXAMPLE: 3
'''
S56 = {1, 2, 3, 4, 5}
S57 = {6, 7, 8, 9, 10}

print(S56.symmetric_difference(S57))
'''

# EXAMPLE: 4
'''
S58 = {1, 2, 3, 4, 5}
S59 = {1, 2, 3, 4, 5}

print(S58.symmetric_difference(S59))
'''

# EXAMPLE: 5
'''
S60 = {1, 2, 3, 4, 5}

print(S60.symmetric_difference({2, 4, 6, 8}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SYMMETRIC DIFFERENCE UPDATE
'''
Update a set with the symmetric difference of itself and another.
'''

# EXAMPLE: 1
'''
S61 = {1, 2, 3, 4, 5}
S62 = {2, 4, 6, 8}

S61.symmetric_difference_update(S62)
print(S61)
'''

# EXAMPLE: 2
'''
S62 = {"Apple", "Microsoft", "Google"}
S63 = {"Apple", "Windows", "Google"}

S62.symmetric_difference_update(S63)
print(S62)
'''

# EXAMPLE: 3
'''
S64 = {2, 4, 6, 8}
S65 = {2, 4, 6, 8}

S65.symmetric_difference_update(S64)
print(S65)
'''

# EXAMPLE: 3
'''
S66 = {1, 2, 3, 4, 5}

S66.symmetric_difference_update({2, 4, 6, 8})
print(S66)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISSUBSET
'''
Report whether another set contains this set.
'''

# EXAMPLE: 1
'''
S67 = {1, 3, 5, 7, 9, 11, 13, 15}
S68 = {3, 9, 15}

print(S67.issubset(S68))

print(S68.issubset(S67))
'''

# EXAMPLE: 2
'''
S69 = {1, 3, 5, 7, 9, 11, 13, 15}

print({3, 9, 15}.issubset(S69))

print(S69.issubset({3, 9, 15}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ISSUPERSET
'''
Report whether this set contains another set.
'''

# EXAMPLE: 1
'''
S70 = {3, 6, 9, 12, 15, 18, 21}
S71 = {3, 6, 9, 12, 15}

print(S70.issuperset(S71))

print(S71.issuperset(S70))

print(S71.issubset(S70))

print(S70.issuperset({3, 6, 9, 12, 15}))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# COPY
'''
Return a shallow copy of a set.
'''

# EXAMPLE: 1
'''
S71 = {100, 200, 300, 400, 500}
S72 = S71
S72.add(1000)
print(S71)
'''

# EXAMPLE: 2
'''
S73 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
S74 = S73.copy()
print(S74)
'''

# EXAMPLE: 3
'''
S75= {"Apple", "Microsoft", "Google"}
S76 = S75.copy()
print(S76)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# CLEAR
'''
Remove all elements from this set.
'''

# EXAMPLE: 1
''''''
S77 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(S77)
print(type(S77))

# help(set)