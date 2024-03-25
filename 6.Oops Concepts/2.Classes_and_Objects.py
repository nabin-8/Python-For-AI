# Lets make person class

class Person:
    name="Nabin"
    age=99
    # this are class variables / fields


per=Person()
print(per.name)
print(per.age)
# Nabin
# 99

# add attributes to object
per.hobby="Programming"
per.collage="TU"
print(per.hobby)
print(per.collage)
'''
Output:
Nabin
99
Programming
TU
'''

per1=Person()
per2=Person()
per3=Person()
per4=Person()

print(per1.name)
print(per2.name)
print(per3.name)
print(per4.name)
'''
Output:
Nabin
Nabin
Nabin
Nabin
'''