# 07/04/2022 # Thursday

# WHAT IS DECORATOR ?
'''
- If we have a function and we want to enhance or add functionality of it without changing its original structure
  then we use docorators.
'''

# EXAMPLE: 1

def decor(func):
    def inner():
        print("☺" * 25)
        func()
        print("☺" * 25)
    return inner
'''
def show():
    print("Nitin Patil")

obj = decor(show)
obj()
'''

# EXAMPLE: 2
'''
@ decor

def f1():
    print('Checking for Decorator Function.')

f1()
'''

# EXAMPLE: 3
''''''
def decor1(func):
    def inner():
        print("☻☻☻☻☻☺☺☺☺☺☻☻☻☻☻")

        inside = func()

        print("☻☻☻☻☻☺☺☺☺☺☻☻☻☻☻")

        return inside

    return inner


# EXAMPLE: 4
'''
@ decor1

def show():
    print("    ♥ Smile Please ♥")

show()
'''

## ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○#

# WHAT IS GENERATOR ?
'''
- Generator is function which generates sequence of number.
- Generator generates data on the fly.
- At a time only one number is store in the memory that's why it is known for memory efficient.
- If a function contains at least one yield statement, it becomes a generator function.
- If Both yield and return then it will return some value from a function.
- The difference is that while a return statement terminates a function entirely, yield statement pauses the function 
  saving all its states and later continues from there on successive calls.
'''

# EXAMPLE: 1
'''
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

g = my_gen()

next(g)

next(g)

next(g)

# next(g)
'''

# EXAMPLE: 1.1
'''
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')

    n += 1
    print('This is printed at last')
    yield n

g = my_gen()

next(g)

next(g)

# next(g)
'''

# EXAMPLE: 2
'''
def my_gen():
    n = 1
    print('This is printed First')
    yield n

    n += 1
    print('This is printed Second')
    yield n

    n += 1
    print('This is printed Last')
    yield n

for i in my_gen():
    print(i)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# WHAT IS ITERATOR ?
'''
- Iterator is a function which generates sequence of number.
- It will work on Datastructure that is work on already stored data in the RAM.
- We can not control the loop but we can control the iterator.
- iter() keyword is used to create an iterator containing an iterable object.
- next() keyword is used to call the next element in the iterable object.
'''

# EXAMPLE: 1
'''
my_iter = [1, 2, 3, 4, 5]

iterate = iter(my_iter)

print(next(iterate))

print(next(iterate))

print(next(iterate))

print(next(iterate))

print(next(iterate))

# print(next(iterate))
'''

# EXAMPLE: 2
'''
loop_iteration = iter([5, 10, 15, 20, 25])

for i in loop_iteration:
    print(i)
'''


# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻