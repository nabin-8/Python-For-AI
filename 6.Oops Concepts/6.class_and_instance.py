class Person:
    country="Nepal"
    # class attribute should be initilize
    # class attribute
    # this same for all object
    def __init__(self,name, age):
        self.name=name
        self.age=age
    # instance attribute
    # this keeps changing for all object
        

per1=Person("Nabin",99)
per2=Person("santosh",35)

print(per1.name, per1.age, per1.country)
print(per2.name, per2.age, per2.country)
'''
Nabin 99 Nepal
santosh 35 Nepal
'''

print(Person.country)