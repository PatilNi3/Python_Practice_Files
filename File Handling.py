# # # DATE: 24/05/2022 # # #

# Temporary Storage-
'''1. Variable'''

# Permanent Storage-
'''
Depending on Size of Data
1. Small Size Data -> File
2. Medium Size Data -> DataBase
3. Huge Size Data -> BigData, Hadoop
'''

# FILE HANDLING IN PYTHON
'''
- Python too supports file handling and allows users to handle files i.e. to read and write files, along with many other 
  file handling options, to operate on files.
- Python treats files differently as Text or Binary and this is important.

• Text Files - Directly open and read -	.txt
                                        .log
                                        .py
                                        .csv

+ Binary File - Data always in binary format -	PDF
                                                Image
                                                Audio
                                                Video
'''

# Open() Function -
'''
- Before performing any operation on the file like reading or writing; first, we have to open that file.
- Python has a built-in open() function to open a file. This function returns a file object, also called a handle.
- Syntax : f = open(filename, mode)
'''

# Close( ) Function -
'''
- When we are done with performing operations on the file, we need to properly close the file. Closing a file will free 
  up the resources that were tied with the file.
- Syntax : f.close()
'''

# DIFFERENT MODES FOR OPENING THE FILE
'''
1. r: open an existing file for a read operation.
2. w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
3. a: Opens a file for appending at the end of the file without truncating/removing it. Creates a new file if it does not exist.
4. r+: To read and write data into the file. The previous data in the file will be overridden.
5. w+: To write and read data. It will override existing data.
6. a+: To append and read data from the file. It won’t override existing data.
7. X: Creates the specified file, returns an error if the file is already exist.
'''

# 1. READING MODE(r)
'''
- To read a file in Python, we must open the file in reading "r" mode.
- There are various methods available for this purpose. We can use the "read(size(n))" method to read in the size number 
  of data. If the size parameter is not specified, it reads and returns up to the end of the file.
- If you need to fetch all characters in the file then we can use "file.read()".
'''
'''
- We can see that the read() method returns a newline as '\n'. Once the end of the file is reached, we get an empty 
  string on further reading.
'''

# EXAMPLE: 1
'''
f1 = open('Read.txt', 'r')
print(f1.read())                   # FileNotFoundError
'''

# EXAMPLE: 1.1
'''
f11 = open('C:\\Users\\91960\\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Read.txt', 'r')
print(f11.read())
'''

# EXAMPLE: 1.2
'''
f111 = open('C:\\Users\\91960\\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Read.txt', 'r')
r = f111.read()
print(r)
print(type(r))
'''

# EXAMPLE: 1.3
'''
f1111 = open('C:\\Users\\91960\\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Read.txt', 'r')
print(f1111.read(25))
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f2 = open('Nitin.csv', 'r')
print(f2.readlines())               # LIST OF LINES
'''

# EXAMPLE: 2.1
'''
f22 = open('C:\\Users\\91960\\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Read.txt', 'r')
r = f22.readlines()
print(r)
print(type(r))
'''

# EXAMPLE: 2.2
'''
f222 = open('Nitin.csv', 'r')
r = f222.readlines()
print(r)
s = r[-1]
print(s)
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 3
'''
f3 = open('Nitin.csv', 'r')
print(f3.readline())                   # SINGLE LINE
'''

# EXAMPLE: 3.1
'''
f33 = open('Nitin.csv', 'r')
print(f33.readline())
print(f33.readline())
'''

# EXAMPLE: 3.2
'''
f333 = open('Nitin.csv', 'r')
print(f333.readline(), end='')
print(f333.readline())
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 4
'''
def FetchEmail():
    f4 = open('Nitin.csv', 'r')
    r = f4.readlines()
    print(r)
    s = r[-1]
    return s
print(FetchEmail())
'''

# EXAMPLE: 4.1
'''
def FetchEmail(filename):
    f41 = open(filename, 'r')
    r = f41.readlines()
    print(r)
    email = r[-1]
    return email
print(FetchEmail('Nitin.csv'))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# # # DATE: 25/05/2022 # # #

# 2. WRITING MODE(w)
'''
- In order to write into a file in Python, we need to open it in write "w".
- We need to be careful with the "w" mode, as it will overwrite into the file if it already exists. Due to this, all the 
  previous data are erased.
- Writing a string or sequence of bytes (for binary files) is done using the write() method. This method returns the 
  number of characters written to the file.
- This program will create a new file named test.txt in the current directory if it does not exist. If it does exist, it 
  is overwritten.
- We must include the newline characters ourselves to distinguish the different lines.
'''

# EXAMPLE: 1
'''
f5 = open('Nitin.txt', 'w')
print(f5.write("Hello, Peter Parker"))
f5.close()
'''

# EXAMPLE: 1.1
'''
f55 = open('Nitin.txt', 'w')
w = f55.write("I'm Iron Man")       # CONTENT OVERRIDE OR WRITING NEW LINE IN GIVEN FILE
print(w)
f55.close()
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f6 = open("C:\\Users\\91960\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Write.txt", "w")
w = f6.write('Stonekeeper, does this chattering animal speaks for you?.\n Certainly not, I speaks for myself.')
print(w)
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 3
'''
f7 = open('Nitin.txt', 'w')
print(f7.writelines('Writing new line'))          # WRITE THE NEW LINE IN GIVEN FILE
'''

# EXAMPLE: 3.1
'''
f77 = open('Nitin.txt', 'w')
print(f77.writelines('\nWriting new line on new line'))
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 4
'''
f8 = open('Nitin.txt', 'w')
print(f8.writeline())           # ATTRIBUTE ERROR; BECAUSE WRITE MODE (W) DOES NOT HAVE THIS FUNCTION
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. APPEND MODE(a)
'''
- With file access mode ‘a’, open() function first checks if file exists or not. If the file doesn’t exist, then it 
  creates an empty file and opens it. 
- Whereas, if the file already exists then it opens it. In both cases, it returns a file object, and it has write cursor, 
  which points to the end of the opened file. 
- Now, if you write anything to the file using this file object, then it will be appended to the end.
'''

# EXAMPLE: 1
'''
f9 = open("C:\\Users\\91960\\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Append.txt", 'a')
print(f9.write('\nNew line in append file'))
'''

# EXAMPLE: 1.1
'''
f99 = open("C:\\Users\\91960\\OneDrive\\Desktop\\KuchBhi\\users.advance.py.txt\\File Handling\\Append.txt", 'a')
print(f99.write('\nSecond line in append file'))
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f10 = open('Append.txt', 'a')
a = f10.writelines(['Like attracts Like' '\nAlways think positive'])
print(a)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 4. READ+ MODE (r+)
'''
- r+ means reading and writing
- The r+ throws an error FileNotFound exception if the file does not exist or opens an existing file without truncating 
  it for reading and writing; the file pointer position at the beginning of the file.
'''

# EXAMPLE: 1
'''
f11 = open('Nitin.txt', 'r+')
rf = f11.read()
print(rf)
rw = f11.write("\nI'm Peter Parker")
print(rw)
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f12 = open('Nitin.txt', 'r+')
rp = f12.read()
print(rp)
dialogue = f12.writelines(['\nAvengers, assemble!'  '\nI can do this all day.'  '\nOn your left.'])
print(dialogue)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 5. WRITE+ MODE (w+)
'''
- w+ means writing and reading
- The w+ creates a new file or truncates an existing file, then opens it for reading and writing; the file pointer position at the beginning of the file.
'''

# EXAMPLE: 1
'''
f13 = open('Practice.txt', 'w+')
ww = f13.write("I'm Unstoppable")
print(ww)
wr = f13.read()
print(wr)
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f14 = open('Practice.txt', 'w+')
ww = f14.writelines(['\nFirst Line' '\nSecond Line'])
print(ww)
wr = f14.read()
print(wr)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 6. APPEND+ MODE (a+)
'''
- a+ means append and read
- Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
'''

# EXAMPLE: 1
'''
f15 = open('Practice.txt', 'a+')
ar = f15.read()
print(ar)          # We get blank output, because of append the pointer is at last and we trying to read no data after this
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f16 = open('Practice.txt', 'a+')
aw = f16.write("practice makes me perfect")
print(aw)                                       # counts the character
ar = f16.read()
print(ar)                                       # blank output
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 7. EXCLUSIVE MODE(X)
'''
- The "x" mode opens the file for exclusive creation, throwing FileExistError if the file with that name is already exist.
'''

# EXAMPLE: 1
'''
f17 = open("Nitin.txt", "x")
xr = f17.read()
print(xr)                     # FileExistError
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 2
'''
f18 = open("NitinN.txt", "x")
xr = f18.write("Family")
print(xr)
'''

#  ------------------------------------------------------------------------------------------------------------------- #

# EXAMPLE: 3
'''
f19 = open("NitinNi.txt", "x")
xr = f19.writelines(['\nline1' '\nline2'])
print(xr)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SEEK and TELL

# TELL Method:
'''
- The tell() method returns the current file position in a file stream.
- Syntax: file.tell()
'''

# EXAMPLE:
'''
f20 = open('NitinN.txt')
t = f20.tell()
print(t)
'''

#----------------------------------------------------------------------#

# SEEK Method:
'''
- We can change the current file position with the seek() method.
- Syntax: file.tell()
'''

# EXAMPLE:
'''
f21 = open('NitinN.txt')
t1 = f21.seek(5)
print(t1)
t2 = f21.read()
print(t2)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# EXAMPLE: 1
'''
with open('Nitin.csv', 'r') as file:
    r = file.read()
    print(r)
'''

# EXAMPLE: 2
'''
with open('Nitin.csv', 'r') as file:
    r = file.read()
    print(r)
    print(file.closed)
print(file.closed)
'''
# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻