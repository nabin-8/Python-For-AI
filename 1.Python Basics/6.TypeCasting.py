'''
Type Casting In Python
There are two types of casting
Convert type 1 to Type 2
1. Implicit
2. Expelict


1. Implicit
Implicit is the condition where python itself change the type

2. Expelict
Expelict is the condition where developer forcefully change the type of datatype
'''

# Example:
# 1. Implicit

x=5 # integer
y=6.5 # float
result=x+y #integer + float
print(result)
# Outpute: 11.5 # float



# Example:
# 2. Expelict
y='10' #string
print(type(y))
# Output: '10'
# <class 'str'>

int_y=int(y)
print(type(int_y))
# Output: 10
# <class 'int'>

'''
Expelect Typecasting
Methods to Typecasting

str() //For String
int() //For Integer
float() //For float

Note: some data cannot be typecaste like
data="one"
print(int(data))
'''