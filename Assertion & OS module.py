
# WHAT IS ASSERTION IN PYTHON ?
'''
- In python, the assert statement is used to continue the execution; if the condition evaluates to TRUE.
  If the assert condition evaluates to FALSE, then it raises the AssertionError exception with the specified error message.
- The assert keyword is used when debugging code.
'''

# SYNTAX:
'''
assert "condition", Error_message(optional)
.
.
.
condition = The boolean condition returning TRUE or FALSE.
Error_message = The optional argument to be printed in console in case of AssertionError
'''

# EXAMPLE: 1
'''
x = 'You'

assert x == 'You'
print("Kuch nahi")
'''

# or

'''
x = 'You'

assert x == 'Me'
print("Kuch Bhi")               # AssertionError
'''

# EXAMPLE: 2
'''
def add(x, y):
    return x + y

add(10, 20) == 30
print(add(10, 20) == 30)                # Shows True
print('You are Genious')
'''

# EXAMPLE: 3
'''
A = 'Alphabet'

assert A == 'Alphabet'
print('Corerct')
'''

# or

'''
assert A == 'Alpha', 'It should be Alphabet'          # AssertionError
'''

# EXAMPLE: 4
'''
Team = [40, 26, 39, 30, 25, 21]

for i in Team:
    assert i >= 26, "Team is Rejected"
    print(str(i) + " is O.K")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# OS MODULE - OS MODULE - OS MODULE - OS MODULE - OS MODULE

# WHAT IS OS MODULE ?
'''
- The OS module in Python provides functions for interacting with the operating system.
- The OS comes under Python's standard utility modules. This module offers a portable way of using operating system 
  dependent functionality.
'''

# EXAMPLE: 1
'''
import os

print(os.name)
'''

# EXAMPLE: 2 -To make/create new directory
'''
import os

print(os.mkdir('C:\\Users\91960\OneDrive\Desktop\ABC'))
'''

# EXAMPLE: 3 -To get Current Working Diretory of the file
'''
import os

print(os.getcwd())
'''

# EXAMPLE: 4 -To change the current working directory
'''
import os

os.chdir('C:\\Users\91960\OneDrive\Desktop')
print(os.getcwd())
'''

# EXAMPLE: 5 -Remove the specified directory
'''
import os

os.rmdir('C:\\Users\91960\OneDrive\Desktop\ABC')
'''

# EXAMPLE: 6 -To make nested directory
'''
import os

os.chdir('C:\\Users\91960\OneDrive\Desktop')
os.makedirs('N\P\A\T\I\L')
'''

# EXAMPLE: 7 -To remove nested directory
'''
import os

os.chdir('C:\\Users\91960\OneDrive\Desktop')
os.removedirs('N\P\A\T\I\L')
'''

# EXAMPLE: 8 -Rename file or directory
'''
import os

os.chdir('C:\\Users\91960\OneDrive\Desktop')
os.rename('A', 'B')
'''

# EXAMPLE: 9 -To get the list of all files and directories in the specified directory.
'''
import os

os.chdir('C:\\Users\91960\OneDrive\Desktop')
print(os.listdir('KuchBhi'))
'''

# EXAMPLE: 10 -Import shutil to remove tree
'''
import os
import shutil

os.chdir('C:\\Users\91960\OneDrive\Desktop')
shutil.rmtree('B')
'''

# EXAMPLE: 11 -Walk
'''
import os

os.chdir('C:\\Users\91960\PycharmProjects')
for path, dirname, files in os.walk('BasicPython'):
    print(path)
    print(dirname)
    print(files)
'''

# EXAMPLE: 12 -Using Generator operation
'''
import os

os.chdir('C:\\Users\91960\PycharmProjects')
Gen = os.walk('BasicPython')

print(next(Gen))

print(next(Gen))

print(next(Gen))

print(next(Gen))

# Similarly we can iterate this for no. of times
'''

# EXAMPLE: 13 -Accessing System
'''
import os

os.system('Notepad')

# or

os.system('Control Panel')

# or

# # os.system('Shutdown')
'''
# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻