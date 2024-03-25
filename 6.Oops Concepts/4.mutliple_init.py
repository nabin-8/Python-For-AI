# In python multiple init is not allowed but we can achive it using

class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
        # This will ignored
    
    def __init__(self,name):
        self.name=name
        # This will executed


per=Person("Nabin Acharya")
print(per.name)