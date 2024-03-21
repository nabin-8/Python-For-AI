'''
Functions Basics, Parameter Passing, Iterators.
Generator Functions
Lambda Functions
Map, Reduce, Filter Functions.
'''
'''
What is Function?
Function is a block of code which can be re-use or re-call
'''

#creating function
'''
def is a keyword to create function in python

def myfunc():
    print("hello i am function")
'''

# function defination
def firstFunction():
    print("Hello Students")

# Function calling
# firstFunction()

# passing parameters in function
def addNumbers(a,b):
    sum=a+b
    return sum


# print(addNumbers(5,10))
# the passing value 5,10 are arguments


'''
concept of global and local variable
the variable declare outside the function/block is global variable and 

the variable declare inside function has function scope

after the execution of function all the variables inside the function are destroyed
'''

x=101 #Global Variable/Scope

def func():
    x=102
    print(x)

# func() #102
# print(x) #101

# Different Types of arguments in the functions:
# 1. Default argument
# 2. Keyword Argument
# 3. Positional arguments



# 1. Default argument
# message="Good Morning" is default argument


def greet(name,message="Good Morning"):
    print(name,message)

# greet("Nabin","Hello") # Nabin Hello
# greet("Nabin") # Nabin Good Morning



# 2. Keyword Argument
# Advantage of keyword argument is you can change the order of passing argument like: age=99,message="Hello", name="Nabin"
def greeet(name,age,message):
    print(message,name,"Your age is",age)

# greeet("Nabin",99,"Hello") #Hello Nabin Your age is 99
# greeet(name="Nabin",age=99,message="Hello") #Keyword argument



# 3. Positional arguments
def add_numbers(x,y):
    print("x ", x)
    print("y ", y)
    print(x+y)

# add_numbers(5,6)
'''
output:
x  5
y  6
11
'''

'''
variable number of arc
variable number of key value arguments
'''

def sum_numbers(*args):
    print(type(args))
    print(args)

    sum=0
    for num in args:
        sum+=num
        return sum
    
# print(sum_numbers(1,2,3,4,5,6))
'''
output:
<class 'tuple'>
(1, 2, 3, 4, 5, 6)
1
'''

# passing normal function
def fn(a,b,*args):
    print(a)
    print(b)
    print(args)
    print(*args)

# fn(5,6,7,8,9)
'''
output:
5
6
(7, 8, 9)
7 8 9
'''

def fn2(*args,a,b):
    print(a)
    print(b)
    print(args)
    print(*args)

# fn2(5,6,7,a=8,b=9)
'''
output:
8
9
(5, 6, 7)
5 6 7
'''


def display_info(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for key,value in kwargs.items():
        print(key, '->', value)

display_info(name="Nabin",age=99)
'''
Output:
<class 'dict'>
{'name': 'Nabin', 'age': 99}
name -> Nabin
age -> 99
'''