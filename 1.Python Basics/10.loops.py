# Python For Loop and While Loop
# 1. For-Loop
# 2. While-Loop

# For-loop iterates over the  individual elements of the object you feed it

# 1. For-Loop

# for letter in 'Hello':
    # print(letter)

'''
output:
H
e
l
l
o

for <variable> in <iterable>:
    ... do something with variable
'''

mylist=[1,'a','Hello']
# for item in mylist:
#     print(item)

'''
Output:
1
a
Hello
'''

# 2. While-Loop
'''
while <expression evaluates to True>:
    do something
'''

i=1
while i<=4:
    print(i)
    i=i+1

'''
Output:
1
2
3
4

Infinite loop
'''

# while True:
#     print("Hello i am ",i)
#     i+=1