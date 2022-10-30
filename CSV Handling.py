# # # DATE: 26/05/2022 # # #

# WHAT IS CSV ?
'''
- CSV is nothing but Comma Separated Values.
- A CSV format is one of the most simple and common ways to store tabular data. To represent a CSV file, it must be
  saved with the .csv file extension.
- Each line of the CSV file is a data record. Each record consists of one or more fields, separated by commas.
- Comma is delimiter; no need to define this
- Similarly we can use TAB as delimiter; but we need to define this by -> delimiter = '\t'
'''

# CSV MODULE DEFINES THE FOLLOWING FUNCTIONS
import csv

'''
1. csv.reader()
2. csv.writer()
3. csv.DictReader()
4. csv.DictWriter()
'''

# NOTE:
'''
- First of all we have to create file and save as .csv
- The content inside the file is(suppose):

Sr, Name, Age, Email, City
1, Nitin Patil, 26, nitinpatilp29@gmail.com, Sangli
2, Neha Bendale, 27, nehabendalep92gmail.com, Mumbai
3, Ruchita Patil, 30, ruchitapatilp29@gmail.com, Mumbai
4, Ankita Dhote, 27, ankitadhotep29@gmail.com, Pune
5, Timish Bendale, 25, timishbendale@gmail.com, Mumbai
6, Tejashree Bendale, 26, tejashreebendale@gmail.com, Mumbai
7, Vaibhav Salunkhe, 30, vaibhavsalunkhe@gmail.com, Pune

'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. CSV.READER()

# EXAMPLE: 1 -READING CSV FILE
'''
with open('Nitin.csv', 'r') as fp:
    r = csv.reader(fp)
    print(r)                      # GIVES OBJECT ID
    print(list(r))                # GIVES FILE CONTENT IN LIST
'''

# EXAMPLE: 2 -CSV FILE HAVING COMMA AS A DELIMITER
'''
with open('Nitin.csv', 'r') as fp:
    r = csv.reader(fp)
    for i in r:
        print(i)
'''

# EXAMPLE: 3 -CSV FILE HAVING TAV AS A DELIMITER
'''
import csv

with open('NitinTab.csv', 'r') as fp:
    r = csv.reader(fp, delimiter='\t')
    for i in r:
        print(i)
'''

# EXAMPLE: 4 -CSV FILE CONTENT AS ITERABLE
'''
with open('Nitin.csv', 'r') as fp:
    r = csv.reader(fp)
    i = r.__next__()                # FIRST ITERATIVE VALUE FROM CSV FILE
    print(i)
    j = r.__next__()                # SECOND ITERATIVE VALUE FROM CSV FILE
    print(j)

- Similarly we can do the same for more no. of iterations
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. CSV.WRITER()

# EXAMPLE: 1 -WRITING SINGLE ROW USING WRITEROW ()
'''
with open('NitinWrite.csv', 'w') as fp:
    w = csv.writer(fp)
    print(w)                                      # GIVES OBJECT ID
    w.writerow(['1, Nitin, 26, Sangli'])          # for single row
'''

# EXAMPLE: 2 -WRITING CSV FILE HAVING TAB AS A DELIMITER
'''
with open('NitinWriteTab.csv', 'w') as fp:
    w = csv.writer(fp, delimiter='\t')
    print(w)                                       # GIVES OBJECT ID
    w.writerow(['1  Nitin   26  Sangli'])          # FOR SINGLE ROW
'''

# EXAMPLE: 3 -WRITING MULTIPLE ROW USING WRITEROW()
'''
with open('NitinWriteRow.csv', 'w') as fp:
    w = csv.writer(fp)
    w.writerow(['Sr, Name, Age, City'],
               ['1, Nitin, 26, Sangli'])                # TypeError
'''

# EXAMPLE: 3.1 -WRITING MULTIPLE ROW USING WRITEROW ()
'''
with open('NitinWriteRow1.csv', 'w') as fp:  # it will automatically create 'NitinWrite1.csv' file
    w = csv.writer(fp)
    w.writerow(['Sr, Name, Age, City'])
    w.writerow(['1, Nitin, 26, Sangli'])
    w.writerow(['2, Neha, 27, Mumbai'])
    w.writerow(['3, Rucha, 30, Mumbai'])
'''

# EXAMPLE: 4 -WRITING MULTIPLE ROWS USING WRITEROWS ()
'''
with open('NitinWriteRows2.csv', 'w') as fp:
    w = csv.writer(fp)
    w.writerows(['Sr, Name, Age, City'],
                ['1, Nitin, 26, Sangli'],
                ['2, Neha, 27, Mumbai'],
                ['3, Rucha, 30, Mumbai'])           # TypeError
'''

# EXAMPLE: 4.1 -WRITING MULTIPLE ROWS USING WRITEROWS ()
'''
rows = (['Sr, Name, Age, City'],
        ['1, Nitin, 26, Sangli'],
        ['2, Neha, 27, Mumbai'],
        ['3, Rucha, 30, Mumbai'])

with open('NitinWriteRows2.csv', 'w') as fp:
    w = csv.writer(fp)
    w.writerows(rows)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. CSV.DICTREADER()
'''
The objects of a csv.DictReader() class can be used to read a CSV file as a dictionary.
'''

# EXAMPLE: 1 -READING CSV FILE IN DICT MODE
'''
with open('NitinDict.csv', 'r') as fp:
    r = csv.DictReader(fp)
    print(r)                            # GIVES OBJECT ID
    for i in r:
        print(dict(i))
'''

# EXAMPLE: 2 -READING CSV FILE IN DICT MODE AS ITERABLE
'''
with open('NitinDict.csv', 'r') as fp:
    r = csv.DictReader(fp)
    print(r)                  # gives <class 'csv.DictReader'>
    i = r.__next__()
    print(i)
    j = r.__next__()
    print(j)
    k = r.__next__()
    print(k)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 4. CSV.DICTWRITER()
'''
The objects of csv.DictWriter() class can be used to write to a CSV file from a Python dictionary.
'''

# EXAMPLE: 1 -WRITING CSV FILE IN DICT MODE
'''
with open('DictWrite.csv', 'w') as fp:
    d = csv.DictWriter(fp)                      # TypeError
    w = d.writer(fp)
    p = d.writerow(['one, two, three'])
'''

# EXAMPLE: 1.1
'''
Header = ['Name', 'Age', 'Company', 'Package']

Data = [{'Name' : 'Nitin', 'Age' : '26', 'Company' : 'Apple', 'Package' : '18LPA'},
        {'Name' : 'Neha', 'Age' : '27', 'Company' : 'Google', 'Package' : '22LPA'},
        {'Name' : 'Rucha', 'Age' : '30', 'Company' : 'Microsoft', 'Package' : '22LPA'}]

with open('DictWrite.csv', 'w') as fp:
    d = csv.DictWriter(fp, fieldnames=Header)
    d.writeheader()
    d.writerows(Data)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# USING THE PANDAS LIBRARY TO HANDLE THE CSV FILE #

import csv
import pandas as pd

# EXAMPLE: 1 -READING THE CSV FILE USING PANDAS LIBRARY
'''
p = pd.read_csv('Nitin.csv')
print(list(p))
'''

# EXAMPLE: 2 -WRITING TO CSV FILE USING PANDAS LIBRARY
'''
df = pd.DataFrame([['Nitin', 26], ['Neha', 27], ['Rucha', 50]])
df.to_csv('Pandas.csv')
'''



# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻