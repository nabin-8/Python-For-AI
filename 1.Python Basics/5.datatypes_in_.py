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
print(i)
print(type(i))

# Float
f=26.25
print(f)
print(type(f))

# Float
c=3e6
print(c)
print(type(c))


#complex
z=4+5j
print(z)
print(type(z))

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
print(abs(-55))
# Output: 55

# Like Wise to make power of any Number
print(pow(2,3))
# Output: 8

# Likw Wise round the number
print(round(4.75))
print(round(4.5))
# Output: 5, 4

nums=[15,6,7,8,9,1,2]
print(min(nums))
print(max(nums))
print(sum(nums))
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

print(name)
print(type(name))
# Output: This is String variable
# <class 'str'>
print(city)
print(country)
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
print(name)
print(name[0])
# Output:
# NABIN N
print(name[-3])
print(name[1:4])
# Output:
# B
# ABI