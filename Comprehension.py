# What is Comprehension ?
'''
- We can create new sequences using a given python sequence. This is called comprehension.
- It basically a way of writing a short and concise code block to generate a new sequence which can be a list,
  dictionary, set or a generator by using already defined sequence.
'''

# Types of Comprehension
'''
1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Generator Comprehension
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. LIST COMPREHENSION
'''
- List comprehension is an elegant way to define and create lists based on exixting lists.
'''

# Syntax
'''
New_list = [<expression> for <item> in <iterable> if <condition>]
'''

# NOTE:
'''
- expression = item, when you want to leave the 'item' unchanged.
- expression != item, when you want to apply some logic to modify 'item'.
- condition is optional. Only use it when you want to do filter.
'''

# EXAMPLE: 1
'''
Old_list = [1,2,3,4,5,6,7,8,9,10]
New_list = []

for number in Old_list:
    if number % 2 == 0:
        New_list.append(number+1)
print(New_list)
'''

# By list comprehension #

'''
Old_list = [1,2,3,4,5,6,7,8,9,10]

New_list = [number + 1 for number in Old_list if number % 2 == 0]

print(New_list)
'''

# or

'''
Old_list = [1,2,3,4,5,6,7,8,9,10]

print([number + 1 for number in Old_list if number % 2 == 0])
'''

# EXAMPLE: 2
'''
for i in range(10):
    print(i)
'''

# By list comprehension #

'''
print([i for i in range(10)])
'''

# EXAMPLE: 3
'''
Y = []

for i in range(10):
    if i % 2 == 0:
        Y.append(i)
print(Y)
'''

# By list comprehension #

'''
print([i for i in range(10) if i % 2 == 0])
'''

# EXAMPLE: 4
'''
Aspirant = ['Patience', 'Focus', 'Consistency', 'Hard work', 'Smart work']

for i in Aspirant:
    print(i)
    if i == 'Consistency':
        break
'''

# By list comprehension #

'''
print([i for i in Aspirant if i == 'Consistency'])
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. DICTIONARY COMPREHENSION
'''
- The name, “Something” Comprehension, is actually depending on the output object type rather than the iterable that is 
  used in the comprehension. Therefore, a Dictionary Comprehension will generate a Dictionary.
'''

# Syntax
'''
output_dict = {<key>:<value> for <item> in <iterable> if <condition>}
'''

# EXAMPLE: 1
'''
list = [1, 2, 3, 4, 5, 6, 7]

dictionary = { }

for x in list:
    if x % 2 != 0:
        dictionary[x] = x ** 3

print(dictionary)
'''

# By dictionary comprehension #

'''
list = [1, 2, 3, 4, 5, 6, 7]

print({x : x**3 for x in list if x % 2 != 0})
'''

# EXAMPLE: 2
'''
State = ['Karnataka', 'Maharashtra', 'Goa']
Capital = ['Banglore', 'Mumbai', 'Panaji']

Output_Dict = { }

for (key, value) in zip(State, Capital):
    Output_Dict[key] = value

print(Output_Dict)
'''

# By dictionary comprehension #

'''
print({key : value for (key, value) in zip(State, Capital)})
'''

# EXAMPLE: 3
'''
Given_list = [x for x in range(5)]
print(Given_list)

New_list = [y+3 for y in Given_list]
print(New_list)

New_dictionary = {x : y for (x, y) in zip(Given_list, New_list)}
print(New_dictionary)
'''

# EXAMPLE: 4
'''
list1 = [x for x in range(7)]
print(list1)
list2 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(list2)

print({key:value for (key, value) in zip(list1, list2)})
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. SET COMPREHENSION
'''
- Set comprehensions are pretty similar to list comprehensions. The only difference between them 
  is that set comprehensions use curly brackets { }.
- Create new set from existing set or list.
'''

# Syntax
'''
New_Set = {<expression> for <item> in <iterable> if <condition>}
'''

# EXAMPLE: 1
'''
Input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

Output_set = set()

for i in Input_list:
    if i % 2 == 0:
        Output_set.add(i)

print(Output_set)
'''

# By set comprehension #

'''
print({i for i in Input_list if i % 2 == 0})
'''

# EXAMPLE: 2
'''
print({x for x in range(5)})
'''

# EXAMPLE: 3
'''
print({x for x in range(11) if x % 2 == 0})
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 4. GENERATOR COMPREHENSION
'''
- Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator 
  comprehensions use parentheses whereas list comprehensions use square brackets. 
- The major difference between them is that generators don’t allocate memory for the whole list. Instead, they 
  generate each value one by one which is why they are memory efficient.
'''

# EXAMPLE: 1
'''
list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

Generator = (x for x in list if x % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for y in Generator:
    print(y, end=' ')
'''

# EXAMPLE: 2
'''
list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

Generator = (x for x in list if x % 2 == 0)

print(next(Generator))

print(next(Generator))

print(next(Generator))

print(next(Generator))
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻
