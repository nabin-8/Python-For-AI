'''
    DataTypes in Python
    1. Numbers(Numirical)
     i. Integer
     ii. Float
     iii.Complex numbers
    
     2. Sequence
      i.string
      ii.List
      iii.Tuple
    3. Boolean
    4. Dictionary
    5. Set
'''


# Numerical
# Integer
i=5
# print(i)
# print(type(i))

# Float
f=26.25
# print(f)
# print(type(f))

# Float
c=3e6
# print(c)
# print(type(c))


#complex
z=4+5j
# print(z)
# print(type(z))

'''
5
<class 'int'>

26.25
<class 'float'>

3000000.0
<class 'float'>

(4+5j)
<class 'complex'>
'''

# abs() is in build method which converts negative number to positive
# Example:
# print(abs(-55))
# Output: 55

# Like Wise to make power of any Number
# print(pow(2,3))
# Output: 8

# Likw Wise round the number
# print(round(4.75))
# print(round(4.5))
# Output: 5, 4

nums=[15,6,7,8,9,1,2]
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# Output: 1, 15, 48

# Sequence dataType
# Sequence datatype is a group of element

# Sequence dataTypes:
# 1. String
# String is the sequence ofcharacters
name="This is String variable"
city='KTM'
country='''This is used for multi line
            string
'''

# print(name)
# print(type(name))
# Output: This is String variable
# <class 'str'>
# print(city)
# print(country)
# OUTPUT:
'''
    KTM
This is used for multi line
            string

'''

# Indexing in string
name="NABIN"
#     01234
# This is how indexing looks like
#  Indexing starts with 0
# print(name)
# print(name[0])
# Output:
# NABIN N
# print(name[-3])
# print(name[1:4])
# Output:
# B
# ABI

# String is immutable in Python
# Let's check it is true or not 
str="Nepal"
# str[0]='x'

''' It gives Error:
        str[0]='x'
    ~~~^^^
    TypeError: 'str' object does not support item assignment
'''
# String concatination
fit_name="Nabin"
last_name="Acharya"

full_name=fit_name+last_name
# print(full_name)
# Output: NabinAcharya

# Find the length of string
# print(len(full_name))
# Output: 12


# String Slicing
# print(full_name[2:5])
# Output: bin
# print(full_name[2:])
# Output: binAcharya
# print(full_name[:7])
# Output: NabinAc
# print(full_name[:])
# Output: NabinAcharya

# print(name.upper())
# print(name.lower())
# Output: NABIN
# nabin

str="nabin"
# print(str.capitalize())
# Nabin it will make first charactter capatalize

str2="  name    "
# remove front and last spaces
# print(str2.strip())
# Output:   nabin

# //Replace Method
strname="Hello, I am It student"
# print(strname.replace("I am", "We are"))
# Output: Hello, We are It student

# Escape Character

# print("Hello \nNabin")
# Hello
# Nabin

# Tab Character
# print("Hello \tNabin")
# print("Hello \"Nabin\"")
# Output
# Hello   Nabin
# Hello "Nabin"


'''
``````````````````````````````````````````````````````````````````` LIST
'''
# List DataType
# List is a collection of elements
# In list you can put different type of dataTypes
# It have order and index
# It is mutable 
# It is array itself

students=["Mohan", "Shivani", "Nabin"]
# print(students)
# Output: ['Mohan', 'Shivani', 'Nabin']


# Another Ways of creating list is:
# From another list
# From string
# From tuple

list2=list(students)
# print(list2)
# Using constructor
# Output: ['Mohan', 'Shivani', 'Nabin']

list3=list("Nabin")
# print(list3)
# Output: ['N', 'a', 'b', 'i', 'n']

list4=list((3,4,"Nabin"))
# print(list4)
# Two way of creating the list
# 1.Bracket notation
# 2.constructor

# Acessing the elements of the list
l1=[1,3,9,2,5,6,8,7]
# print(l1[3])  #Output: 2
# print(l1[-6]) #Output: 9

# Inserting elements
'''
Insert at the end append()
AT secific index insert()
extend existing list extend()
'''

arr=[3,2,1,5,9]
arr.append(11)
# print(arr)
# Output: [3, 2, 1, 5, 9, 11]

arr.insert(3,43)
# print(arr)
# Output: [3, 2, 1, 43, 5, 9, 11]

# Array is mutable

arr1=[1,2]
arr2=["Python", "Java"]
# print("Array1 Before: ",arr1)
arr1.extend(arr2)
# print("Array1 After: ",arr1)
'''
    Array1 Before:  [1, 2]
    Array1 After:  [1, 2, 'Python', 'Java']
'''

# Remove elemments from the list

arr3=[3,5,2,1,9]
arr3.remove(1)
# print(arr3)
# Output: [3, 5, 2, 9]

arr3=[3,1,5,1,2,1,9]
arr3.remove(1)
# print(arr3)
# Output: [3, 5, 1, 2, 1, 9]
# It remove first occrunce of the list

# POP
# print(arr3.pop())
# print(arr3)
# Output: 9
# [3, 5, 1, 2, 1]

# Replace the value at the index
# Replace the value at a range

student=['a','b','c','d','e','f']
student[3]='g'
# print(student)
# Output: ['a', 'b', 'c', 'g', 'e', 'f']

student[1:4]='m','n','o'
# print(student)
# Output: ['a', 'm', 'n', 'o', 'e', 'f']


# Array Other Methods


lone=[1,2,3,4,5,6]
lone.reverse()
# print(lone)
# Output: [6, 5, 4, 3, 2, 1]

lone_copy=lone.copy()
# print(lone_copy)

# print(id(lone_copy),id(lone))
# There address are totally different
# 2221298823744 2221298823872

lone.sort()
# print(lone)
# Output: [1, 2, 3, 4, 5, 6]

'''
```````````````````````````````````````````````````````````
            --------    Tuple   ---------
Tule is also similar to list
1. ordered element
2. differnt type of data

Main Difference is
Tuple is immutable
'''
# Define tuple
tup1=(3,6,1,9,10)
# print(tup1)
# print(type(tup1))
# Output 
# (3, 6, 1, 9, 10)
# <class 'tuple'>

# Define/Create tuple using constructor
t1=tuple([1,2,4,5,6])
# print(t1)
# Output: (1, 2, 4, 5, 6)

t2=tuple("Nabin")
t3=tuple(tup1)
# print(t2,t3)
# Output: ('N', 'a', 'b', 'i', 'n') (3, 6, 1, 9, 10)

t=(22)
# print(type(t))
# <class 'int'>

t=(22,)
# print(type(t))
# <class 'tuple'>

fruits=("apple", "mango", "apple", "mango", "apple")
# print(fruits.count('apple'))
# print(fruits.count('jackfruit'))
# Output: 3 0

# find the index 
# print(fruits.index('mango'))
# Output: 1

# find the length
# print(len(fruits))
# Output: 5

'''
Access the elements of tuple
'''

# print(fruits[3])
# print(fruits[-3])
# Output: mango
# apple

# Tuple is immutable? lets check this
# fruits[3]="Jackfrute"
# TypeError: 'tuple' object does not support item assignment
# There is error while changing the tuple elements

# print(fruits[2:7])
# Output: ('apple', 'mango', 'apple')


'''
```````````````````````````````````````````````````````````
Boolean
Either it is true or false
'''

# print(True)
# print(type(True))
# print(False)
# print(type(False))
'''
True
<class 'bool'>
False
<class 'bool'>
'''

'''
```````````````````````````````````````````````````````````
Dictionary
1. Stores elements in (key,value)
2. There is unordered
3. It is Mutable
4. Key has to be unique
5. Heterogeneous data
Heterogeneous means you can store multiple datatypes

All immutable dadaTypes can store in the dictionary
'''

students_details={'name':'nabin','age':21,'city':'KTM'}
# print(students_details)
# print(type(students_details))
# Output: {'name': 'nabin', 'age': 21, 'city': 'KTM'}
# <class 'dict'>

dict1={1:"Nabin",2:"Acharya",True:"Student"}
# print(dict1)
# Output: {1: 'Student', 2: 'Acharya'}
# Where is True:"Student" 
# This is happen because 1 and true are same in python
# Lets modify 1 with 3 then see what happens

dict1={3:"Nabin",2:"Acharya",True:"Student"}
# print(dict1)
# Now the OUTPUT IS: {3: 'Nabin', 2: 'Acharya', True: 'Student'}

# Making dict using constructor methods

dict2=dict(name="Nabin", age=22)
# print(dict2)
# Output {'name': 'Nabin', 'age': 22}


# Methods of Dictionary
# Accessing the elements of the dict

# print(students_details['name'])
# print(students_details['age'])
# print(students_details['city'])
'''
Output
nabin
21
KTM
'''

# print(students_details.keys())
# print(students_details.values())
# dict_keys(['name', 'age', 'city'])
# dict_values(['nabin', 21, 'KTM'])

# All these values togetger
# print(students_details.items())
# dict_items([('name', 'nabin'), ('age', 21), ('city', 'KTM')])
# It gives the list of tuples of key value pair


# How do we add elements in the dictionary | Key,Value
students_details['country']="Nepal"
# print(students_details)
# Output: {'name': 'nabin', 'age': 21, 'city': 'KTM', 'country': 'Nepal'}


marks_details={'English':100,'Maths':88,"Science":95}
students_details.update(marks_details)
# print(students_details)
'''
Output:
{'name': 'nabin', 'age': 21, 'city': 'KTM', 'country': 'Nepal', 'English': 100, 'Maths': 88, 'Science': 95}
'''

# Remove the elements from the dictionary
students_details.pop('city')
# print(students_details)
'''
Output:
{'name': 'nabin', 'age': 21, 'country': 'Nepal', 'English': 100, 'Maths': 88, 'Science': 95}
'''

# print(students_details.popitem())
# print(students_details)
'''
Output:
('Science', 95)
{'name': 'nabin', 'age': 21, 'country': 'Nepal', 'English': 100, 'Maths': 88}
'''

# Delete keyword
del students_details['age']
# print(students_details)
# Output: {'name': 'nabin', 'country': 'Nepal', 'English': 100, 'Maths': 88, 'Science': 95}

students_details.clear()
# print(students_details)
'''
{}
'''


'''
```````````````````````````````````````````````````````````
SETS
1. No Duplicates elements are unique
2. mutable
3. un-ordered
4. Heterogeneous data
Heterogeneous means you can store multiple datatypes
'''

# se datatype

my_set={1,2,3,4}
# print(my_set)
# print(type(my_set))
# output:{1, 2, 3, 4}
# <class 'set'>

# check unique
s1={1,2,1,3,4,2,4}
# print(s1)
# OUTPUT: {1, 2, 3, 4}
# Sets ensures that there are no duplicates

# Create Sets Using Constructor
s2=set()
# print(s2)
# Output: set()

s3=set({5,6,17,5,9,8,7,2})
# print(s3)
'''
{2, 67, 5, 6, 7, 8, 9}

{17, 2, 5, 6, 7, 8, 9}
'''


# Add Elwmwnts in Sets
s=set()
s.add(6)
s.add(7)
s.add(6)
s.add(9)
s.add(10)
s.add(11)

# print(s)
# Output: {6, 7, 9, 10, 11}


# Remove
# print(s.discard(7))
# print(s)
# Output:
# None
# {6, 9, 10, 11}

# print(s.remove(12))
# print(s)
# OUTPUT: KeyError: 12

'''
Immutable Sets
Python has support of this kind of sets
This sets called FROZEN SETS

FROZEN SETS
Immutable: Set
'''

fs=frozenset([1,2,3])
print(fs)
print(type(fs))
# Outputz: frozenset({1, 2, 3})
# <class 'frozenset'>

fs2=frozenset({1,2,3})
print(fs2)
# frozenset({1, 2, 3})

# Dictionary keys have to immutable
# sets cannot be used in dict
# To use sets in dict you have to make it frozenset

# Example:

dict1={fs2:"Nabin"}
print(dict1)
# Output: {frozenset({1, 2, 3}): 'Nabin'}