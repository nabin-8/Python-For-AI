# constructor 

class Person:
    # initilizer/coonstructor for objects
    def __init__(self, name, age):
        self.name=name
        self.age=age

'''
def is a keyword
__init__ is used create constructor
constructor first argument in this case self represents the object to be create

self.name=name
self.age=age
initilizing the state of the object
'''

per=Person("Nabin", 99)
per2=Person("santosh", 25)
per3=Person("suraj", 36)
per4=Person("anish", 56)

print(per.name,per.age)
print(per2.name,per2.age)
print(per3.name,per3.age)
print(per4.name,per4.age)

'''
Nabin 99
santosh 25
suraj 36
anish 56
'''