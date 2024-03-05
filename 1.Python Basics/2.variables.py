# Variables in Python

# Python is Dynamically typed programming language

name="Nabin"
x=5

# print(name,x)
# read basic python md

## refrence count
print(id(name))
# Output: 2977135351184 refrence count

# Mutable and immutable
age=22
myAge=age
print(age, " ", myAge)
# Output : 22 22
myAge=25
print(age, " ", myAge)
# Output : 22 25

# Immutable data types
# int float bool chr str tuple None

# Mutable Data Types
# list set dictionary dict frozenset

# Rules for  variable naming
# 1. Variable name must start with a letter (a-zA-Z) or underscore (_).
# 2. Variable name can contain letters (a-zA-Z), digits (0-9), or underscores.
# 3. Variable names are case sensitive i.e., Name and name are different.
# 4. A valid variable name cannot be a keyword of the Python language. 

# Example of invalid variable name
# if = 5
# na%me="myname"

# Example  of valid variable name
# my_variable = 5
# my_Name= "My Name Is Nabin"

# Keywords in python
#  Keywords are the reserved words used by python. you cannot use it as a variable
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

