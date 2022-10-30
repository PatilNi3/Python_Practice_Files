# DICTIONARY DATA STRUCTURE #
'''
- Dictionary is an unordered collection of elements.
- It is a Mutable datastructure.
- Dictionary is nothing but key value pairs.
- Value in dictionary can be duplicated, whereas keys can't be repeated.
- Key = Key is always immutable and unique.
    For Eg.:- number, tuple, string, frozenset
- Value = Value can be mutable or immutable.
    For Eg.:- number, tuple, string, frozenset or list, set, dictionary
'''

# EXAMPLE: 1
'''
DICTIONARY = {}
print(DICTIONARY)
print(type(DICTIONARY))
'''

# EXAMPLE: 2
'''
DICTIONARY1 = {"Name" : "Nitin", "Branch" : "Mechanical", "Age" : "Doesn't Matter"}
print(DICTIONARY1)
print(type(DICTIONARY1))
print(len(DICTIONARY1))
'''

# EXAMPLE: 3
'''
DICTIONARY2 = {[1, 2, 3] : "List", 555 : "Integer"}             # TypeError
print(DICTIONARY2)
'''

# EXAMPLE: 4
'''
DICTIONARY3 = {0 : "Zero", 1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 0 : "Ghanta"}             # Value Override
print(DICTIONARY3)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# FETCHING VALUES USING KEY

# EXAMPLE: 1
'''
D1 = {"language" : "python", "course" : "data science", "duration" : "8 months"}

print(D1["language"])
print(D1["course"])
print(D1["duration"])
'''

# EXAMPLE: 2
'''
D2 = {"maharashtra" : "mumbai", "goa" : "panji", "karnataka" : "banglore", "Pune" : {"ganpati" : "DagduSheth", "food" : "Misal"}}

print(D2["goa"])
print(D2["Pune"])
print(D2["Pune"]["food"])
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

'''
D3 = {"Name" : "Nitin", "Age" : 27, "Batch" : "Python", "Started On" : "March"}

D3["Batch"] = 29
print(D3)

D3["Started On"] = "13 March 2022"
print(D3)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# KEYS
'''
It will gives keys of dictionary.
'''

# EXAMPLE: 1
'''
D4 = {"Car name" : "Mercedes", "Varient" : "C-Class", "Price" : "61 lakh"}

print(D4.keys())
'''

# EXAMPLE: 2
'''
D5 = {23 : "Day", 11 : "Month", 1995 : "Year"}

print(D5.keys())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# VALUES
'''
It will return values of dictionary.
'''

# EXAMPLE: 1
'''
D4 = {"Car name" : "Mercedes", "Varient" : "C-Class", "Price" : "61 lakh"}

print(D4.values())
'''

# EXAMPLE: 2
'''
D5 = {23 : "Day", 11 : "Month", 1995 : "Year"}

print(D5.values())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# ITEMS
'''
ReturnS key and value of dictioary.
'''

# EXAMPLE: 1
'''
D4 = {"Car name" : "Mercedes", "Varient" : "C-Class", "Price" : "61 lakh"}

print(D4.items())
'''

# EXAMPLE: 2
'''
D5 = {23 : "Day", 11 : "Month", 1995 : "Year"}

print(D5.items())
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# UPDATE
'''
Update existing key with new value or Update dictionary with new key value pair.
'''

# EXAMPLE: 1
'''
D6 = {"Bollywood" : "3-Idiots", "Hollywood" : "Marvel Series", "YouTube" : "Rom-Com Series"}

D6["Bollywood"] = "Chicchore"
print(D6)
'''

# EXAMPLE: 2
'''
D6 = {"Bollywood" : "3-Idiots", "Hollywood" : "Marvel Series", "YouTube" : "Rom-Com Series"}

D6.update({"YouTube" : "Data Science"})
print(D6)

D6.update({"Genre" : "Thriller"})
print(D6)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# GET
'''
Return the value for key if key is in the dictionary, else default.
'''

# EXAMPLE: 1
''' 
D7 = {"Car name" : "Mercedes", "Varient" : "C-Class", "Price" : "61 lakh"}

print(D7.get("Varient"))
print(D7.get("ABC"))   # DEFAULT = NONE
print(D7.get("AB", 0))
print(D7.get("A", "No key present"))

GET = D7.get("X", "No key present")
print(GET)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# SET DEFAULT
'''
Insert key with a value of default if key is not in the dictionary. Return the value for key if key is in the dictionary, else default.
'''

# EXAMPLE: 1
'''
D8 = {1 : "Sugar", 2 : "Tea powder", 3 : "Cooking oil"}

print(D8.setdefault(1, "Poha"))

print(D8.setdefault(4, "Poha"))

print(D8.setdefault(5))

print(D8)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# FROMKEYS
'''
When we creat dictionary without values then we use fromkeys.
'''

# EXAMPLE: 1
'''
D9 = {"Car name", "Varient", "Price"}

print(dict.fromkeys(D9))

print(dict.fromkeys(D9, 0))
'''

# EXAMPLE: 2
'''
D10 = {1, 2, 3}
D11 = "Integer"

print(dict.fromkeys(D10, D11))
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# POP
'''
- Remove specified key and return the corresponding value.
- If the key is not found, return the default if given; otherwise, raise a KeyError.
'''

# EXAMPLE: 1
'''
D12 = {"Jalgaon" : "Neha", "Nandurbar" : "Ruchita", "Sangli" : "Nitin"}
print(D12)

print(D12.pop("Sangli"))
print(D12)

print(D12.pop("Kolhapur", 0))               # DEFAULT = 0
print(D12)

print(D12.pop("Mumbai"))                # KeyError
print(D12)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# POPITEM
'''
Remove and return a (key, value) pair in a tuple.
Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.
'''

# EXAMPLE: 1
'''
D13 = {"Jalgaon" : "Neha", "Nandurbar" : "Ruchita", "Kolhapur" : "Priyanka", "Aurangabad" : "Tushar", "Sangli" : "Nitin"}

print(D13.popitem())
print(D13.popitem())
print(D13.popitem())
print(D13.popitem())
print(D13.popitem())
print(D13.popitem())

print(D13)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# COPY
'''
Return a shallow copy dictionary.
'''

# EXAMPLE: 1
'''
D14 = {"Alphabet" : "Sundar Pichai", "Microsoft" : "Satya Nadella", "Twitter" : "Parag Agarwal"}
D15 = D14
D15.update({"IBM" : "Arvind Krishna"})
print(D14)
'''

# EXAMPLE: 2
'''
D16 = {'Alphabet': 'Sundar Pichai', 'Microsoft': 'Satya Nadella', 'Twitter': 'Parag Agarwal', 'IBM': 'Arvind Krishna'}
D17 = D16.copy()
D17.update({"Adobe" : "Shantanu Narayen"})
print(D16)
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# CLEAR
'''
Remove all items from Dictionary and gives empty dictionary.
'''

# EXAMPLE: 1
'''
D18 = {"A" : "Apple", "B" : "Bada Apple", "C" : "Chota Apple"}

D18.clear()

print(D18)
print(type(D18))
'''

# help(dict)
