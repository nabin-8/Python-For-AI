'''
arguments are passed using two types:
passby value and passby reference

passby value is activate if the arguments are immutable datatypes:

Immutable DatatYpes:
1. Numbers,
2. String,
3. tuple
pass by value

passby value => passing the copy
passby reference => 
def is used to define function
it will change orginal datatype
# Mutable DataTypes:
1. List,
2. Dictionary


func(argument)
'''

# pas by value
num=5
# def modify_num(num):
#     num+=1
#     print(num)

# modify_num(num)
# print("Orginal num", num)
'''
Output:
6
Orginal num 5
'''

# Passby reference:
my_list=[1,2,3,4]
def modify_list(li):
    li.append(5)
    print(li)
# modify_list(my_list)
# print("Orginal list", my_list)

'''
Output:
[1, 2, 3, 4, 5]
Orginal list [1, 2, 3, 4, 5]
'''

'''
Lamda Function
lamda fn is another way of defining function
Lamda fn is also:
1. Anonomus Function : which have no name
2. It can take any numbers of arguments
3. It can have only one expression

lamda is keyword
'''

func=lambda x: x+10
# lamda is a keyword
# x is a argument
# x+10 is a expression

# print(func(5)) # 15

# another example
add=lambda a,b: a+b

# print(add(5,5)) # 10

def myFunc():
    # Return a new function
    return lambda msg:print(msg)

myFunc()("Hello World")