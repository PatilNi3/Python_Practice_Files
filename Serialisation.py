### 02/06/2022 # Thursday # 08:00PM to 09:30PM ###

# WHAT IS SERIALISATION ?
'''
- Object serialization is the process of converting state of an object into byte stream.
- We also call this ‘serialization’, ‘marshalling’, or ‘flattening’.
'''

# WHAT IS DE-SERIALISATION ?
'''
- Deserialization is just a reverse process of serialization. Deserialization is the process of transforming a series of 
  bytes into a structured object.
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON # JSON #

import json

'''
- JSON stands for JavaScript Object Notation.
- JSON is a common undestandable language.
- It's a light weight and human understandable.

- The Python module JSON converts a Python dictionary object into JSON object:

    dict            --->>>      object
    list, tuple     --->>>      array
    str             --->>>      string
    int, float      --->>>      number
    True            --->>>      true
    False           --->>>      false
    None            --->>>      null
    
- Syntax: json.dump(dict, file_pointer)
'''

# Python data to JSON format by using the methods:
'''
1. Dump() - Python object to json file
2. Dumps() - Python object to json string
'''

# JSON format to Python data by using the methods:
'''
1. load() - json formatted stream to a Python object
2. loads() - json document to a python object
'''

# EXAMPLE: 1 -SERIALISATION
'''
dictionary = {'Name':'Neha', 'Age':27, 'City':'Mumbai', 'Email':'nehabendalep29@gmail.com', 'True':True, 'None':None}

with open('JSON_Dump.json', 'w') as fp:
    data = json.dump(dictionary, fp)
    print(data)
    print(type(data))
'''

# EXAMPLE: 2 -SERIALISATION
'''
dictionary = {'Name':'Ruchita','Age':30,'City':'Panvel','Email':'ruchipatilp29@gmail.com','True':True,'None':None}

with open('JSON_DumpS.json', 'w') as fp:
    data = json.dumps(dictionary)
    print(data)
    print(type(data))
'''

# or

'''
dictionary = {'Name':'Ruchita','Age':30,'City':'Panvel','Email':'ruchipatilp29@gmail.com','True':True,'None':None}

data = json.dumps(dictionary)
print(data)
print(type(data))
'''

# EXAMPLE: 3 -DE-SERIALISATION
'''
with open('JSON_Dump.json', 'r') as fp:
    data = json.load(fp)
    print(data)
'''

# EXAMPLE: 4 -DE-SERIALISATION
'''
dt = json.loads(data)
print(dt)
'''

# or

'''
dictionary = '{"Name":"Pata Nahi", "Age":"Yaad Nahi", "City":"Galaxy", "Email":"Google se pucho", "True":"True"}'

data = json.loads(dictionary)
print(data)
print(type(data))
print(type(dictionary))
'''

# EXAMPLE: 5 -CREATE DICTIONARY USING "__dict__"
'''
class Student:

    def __init__(self, Name, Email, City):
        self.Name = Name
        self.Email = Email
        self.City = City

    def show(self):
        print(self.Name)
        print(self.Email)
        print(self.City)

boy = Student('Nitin', 'nitinpatilp29@gmail.com', 'Sangli')
print(boy.__dict__)
girl = Student('Neha', 'nehabendalep29@gmail.com', 'Mumbai')
print(girl.__dict__)
girl1 = Student('Ruchita', 'ruchitpatil.p29@gmail.com', 'Panvel')
print(girl1.__dict__)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE # PICKLE #

import pickle

'''
- It is also common understandable language.
- Python pickle module is used for serializing and de-serializing python object structures. 
- The process to converts any kind of python objects (list, dict, etc.) into byte streams(binary) (0s and 1s) is called 
  pickling or serialization or flattening or marshalling.
- We can converts the byte stream (generated through pickling) back into python objects by a process called as 
  unpickling or de-serialisation.
- Only after importing pickle module we can do pickling and unpickling.
  import pickle
'''

# METHODS

# Python data to Pickle format by using the methods:
'''
1. dump() − The dump() method serializes to an open file (file-like object).
2. dumps() − Serializes to a binary object.
'''

# Pickle format to Python data by using the methods:
'''
1. load() − Deserializes from an open file.
2. loads() − Deserializes from a binary object.
'''

# EXAMPLE: 1 -SERIALISATION
'''
dictionary = {'Name':'Nitin', 'Age':'26', 'Email':'nitinpatilp29@gmail.com', 'City':'Sangli'}

with open('PICKLE_dump.pickle', 'wb') as fp:
    data = pickle.dump(dictionary, fp)
    print(data)
'''

# EXAMPLE: 2 -SERIALISATION
'''
dictionary = {"Name":"Neha", "Age":"27", "Email":"nehabendalep29@gmail.com", "City":"Mumbai"}

data = pickle.dumps(dictionary)
print(data)
'''

# EXAMPLE: 3 -DE-SERIALISATION
'''
with open('PICKLE_dump.pickle', 'rb') as fp:
    data = pickle.load(fp)
    print(data)
'''

# EXAMPLE: 4 -DE-SERIALISATION
'''
data = pickle.loads(b'\x80\x04\x95Q\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04Name\x94\x8c\x04Neha\x94\x8c\x03Age\x94\x8c\x0227\x94\x8c\x05Email\x94\x8c\x18nehabendalep29@gmail.com\x94\x8c\x04City\x94\x8c\x06Mumbai\x94u.')
print(data)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

### 03/06/2022 # Friday # 07:30PM to 09:00PM ###

# YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML # YAML #

'''pip install pyyaml'''
import yaml
'''
- YAML stands for YAML Ain't Markup Language. 
- YAML a strict superset of JSON, so anything written in JSON can be parsed to YAML.
- The file extension for YAML files is .yaml or .yml
- Everything in the YAML is a key-value pair.
- Light in weight than JSON
- Install a Python module called the pyyaml to work with YAML files.
  pip install pyyaml
'''

# METHODS
'''
1. dump() - Python dict to yaml
2. load() - Yaml to Python dict
'''

# EXAMPLE: 1 -SERIALISATION
'''
py_dict = {
    'prd_name':'iron',
    'prd_id':100,
    'prd_qnty':1000
}

ys = yaml.dump(py_dict)
print(ys)
'''

# EXAMPLE: 2 -SERIALISATION
'''
d = """
- 'Nitin Patil'
- 26
- 'nitinpatilp29@gmail.com'
"""

About = yaml.safe_load(d)

with open('YAML_sl.yaml', 'w') as fp:
    yaml.dump(About, fp)
'''

# EXAMPLE: 3 -DE-SERIALISATION
'''
d = """
- 'Nitin Patil'
- 26
- 'nitinpatilp29@gmail.com'
"""

Serial = yaml.safe_load(d)
print(Serial)
'''

# EXAMPLE: 4 -DE-SERIALISATION
'''
with open('YAML_sl.yaml' 'r') as fp:
    data = yaml.safe_load(fp)
    print(data)
'''




# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻