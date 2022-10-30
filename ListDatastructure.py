# LIST DATA STRUCTURE #
'''
- List means collection of elements.
- List is mutable type datastructure (The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.).
- It is ordered data structure (It means that the items have a defined order, and that order will not change.).
- Lists can accepts duplicate values.
'''

# EXAMPLE:
'''
LIST = ['NITIN', 2311, 'NEHA', 1704, 'RUCHITA', 702, 'ANKITA', 1009]

print(LIST)

print(len(LIST))            # len() - length of list

print(type(LIST))           # type() - type of data structure
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# INSERT
'''
To insert element at desired location using index number.
'''

# EXAMPLE: 1
'''
L1 = ["Python", 555, "Java", 777, 'HTML', 'CSS', 'PHP', 'JavaScript']
print(L1)

L1.insert(2, "Nitin")          # (index position, element)
print(L1)                      

L1.insert(7, "Nitin")
print(L1)
'''

# EXAMPLE: 2
'''
L2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(L2)

L2.insert(3, 25)
print(L2)

L2.insert(-1, 555)
print(L2)

L2.insert(1, [1, 3, 5])
print(L2)                   # WE GET NESTED LIST (LIST INSIDE LIST)

print(L2[5])                # ELEMENT AT THE INDEX NO. 5

print(L2.index(555))        # INDEX NO. OF ELEMENT 555
'''

# EXAMPLE: 3
'''
print(list(range(11)))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# APPEND
'''
To add element at the end of the list.
'''
# EXAMPLE: 1
'''
L3 = ["Python", "Selenium", "Java"]
print(L3)

L3.append("Angular")
print(L3)

L3.append(555)
print(L3)
'''

# EXAMPLE: 2
'''
L4 = []
print(L4)

L4.append(5)
print(L4)

L4.append("word")
print(L4)

L4.append(55)
print(L4)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXTEND
'''
- To add multiple element at the end of the list. 
- In append we can add only 1 element at the end but in extend we can add multiple element at the end.
'''
# EXAMPLE: 1
'''
L5 = ["Python", "Selenium", "Java"]
print(L5)

L5.extend("PHP")
print(L5)                       # PROBLEM 

L5.extend(["PHP"])
print(L5)
'''

# EXAMPLE: 2
'''
L6 = []
print(L6)

L6.extend([5, 25, "ONE TWO FIVE", 625, 3125])
print(L6)
'''

# EXAMPLE: 3
'''
L7= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
L8= [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

L7.extend(L8)
print(L7)

L7.sort()           # SORT OUT LIKE ASCENDING ORDER
print(L7)
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# REMOVE
'''
We can delete 1 element from the list by using Element itself.
'''
# EXAMPLE: 1
'''
L8 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(L8)

L8.remove(6)
print(L8)
'''
# EXAMPLE: 2
'''
L9 = ["Python", "Selenium", "Java", "JavaScript"]
print(L9)

L9.remove("Python", "Selenium")           # TypeError
print(L9)
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# POP
'''
This method removes item at given index from the list.
'''

# EXAMPLE: 1
'''
L10 = ["Python", "Selenium", "Java", "Angular"]
print(L10)

L10.pop(1)
print(L10)

L10.pop(0)
print(L10)

L11 = L10.pop(1)                # STORING THE RESULT IN THIRD VARIABLE
print(L11)                      # PRINTING THAT THIRD VARIABLE GIVES ELEMENT WHICH IS GOIN TO REMOVE FROM LIST

L10.pop(2)
print(L10)                      # IndexError
'''

# EXAMPLE: 2
'''
L12 = ["Python", "Java", "Selenium", "PHP"]
print(L12)

L12.pop(1, 2)                   # TypeError
print(L12)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# INDEX
''' 
It returns index value of the element.
'''
# EXAMPLE: 1
'''
L13 = ["Python", "Java", "Basic"]
print(L13)

print(L13.index("Java"))

print(L13.index("Python"))

print(L13.index("Basic"))
'''
# EXAMPLE: 2
'''
L131 = [10, 20, [100, 'python', 200, 300]]
print(L131)

print(L131[2][0])               # TO GET THE ELEMENT 100

print(L131[2].index(100))       # TO GET THE INDEX NO. OF 100
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# COUNT
''' 
It gives occurance of duplicate value.
'''
# EXAMPLE: 1
'''
L14 = [1, 1, 1, 1, 1, 3, 3, 5, 5, 5, 8, 9, 4, 2]
print(L14)

print(L14.count(1))

print(L14.count(3))

print(L14.count(8))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SORT
'''
- Sort the list element in ascending order.
- Sort(reverse=True) = Sort the list element in descending order'
'''
# EXAMPLE: 1
'''
L15 = [2, 4, 16, 256, 8, 64, 32, 128]
print(L15)

L15.sort()
print(L15)

L15.sort(reverse=True)
print(L15)
'''

# EXAMPLE: 2
'''
L16 = ["Physics", "Chemistry", "Maths", "Stat"]
print(L16)

L16.sort()
print(L16)
'''

# EXAMPLE: 3
'''
L17 = ["PHYSICS", 0, "Chemistry", 3, "Maths", 7]
print(L17)

L17.sort()              # TypeError
print(L17)
'''

# EXAMPLE: 4
'''
L18 = ["PHYSICS", "0", "Chemistry", "3", "Maths", "7"]
print(L18)

L18.sort()
print(L18)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# REVERSE
'''
It reverse the content of the list.
'''
# EXAMPLE: 1
'''
L19 = [2, 4, 8, 16, 32, 64, 128, 256]
print(L19)

L19.reverse()
print(L19)
'''

# EXAMPLE: 2
'''
L20 = ["Physics", "Chemistry", "Maths", "Stat"]
print(L20)

L20.reverse()
print(L20)
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# COPY
import copy
'''
Returs the shallow copy (like shadow of object) of the list.
'''
# EXAMPLE: 1
'''
L21 = [1, 2, 3, 4, 5]
L22 = L21                   # SHALLOW COPY -> A = B
L22.append(25)
print(L21)
'''

# EXAMPLE: 2
'''
L23 = [1, 2, 3, 4]
L24 = copy.copy(L23)        # DEEP COPY
L24.append(5)
print(L23)
print(L24)
'''

# EXAMPLE: 3
'''
L25 = [1, 2, 3, 4, 5]
L26 = L25.copy()
L26.append(50)
print(L26)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# CLEAR
'''
This method removes all items from list.
'''
# EXAMPLE: 1
'''
j = [2, 4, 8, 16]
print(j)

j.clear()
print(j)
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# CHR()
'''
chr() used for converting an Integer to a Character.
'''
# EXAMPLE:
'''
print(chr(105))

print(chr(108))

print(chr(117))
'''
# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ORD()
'''
ord() used for converting an Character to Integer.
'''
# EXAMPLE:
'''
print(ord("r"))
print(ord("R"))

print(ord("N"))
print(ord("I"))
print(ord("T"))
print(ord("I"))
print(ord("N"))
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺