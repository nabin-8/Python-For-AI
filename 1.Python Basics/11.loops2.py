'''
Loops means something you have to repeat multiple times

There is two standard loop in python:
1.for-loop
2.while-loop
'''



fruits=["apple", "banana", "cherry", "date"]

# for fruit in fruits:
#     print(fruit)

'''
output:
apple
banana
cherry
date
'''

name="Nabin Acharya"

# for ch in name:
#     print
#     print(ch)

'''
output:
N
a
b
i
n
 
A
c
h
a
r
y
a
'''

#if i have to run fro loop in 100 times

# for i in range(10):
#     print(i)

# Output: 0,1,2,3,4,5,6,7,8,9

# for i in range(6,10):
#     print(i)
# Output: 6,7,8,9


# for i in range(2,10,2):
#     print(i)

# Output: 2,4,6,8 last 2 is increment value in argument
    
'''
range(n) -> n elements
'''

# for i in range(10,0,-1):
#     print(i)

# -1 reverse the range
    
# for i in range(12,0,-3):
#     print(i)
# -1 reverse the range
    
'''
controlling the flow of loop
1. break
it will take outof loop
2. continue
skip that line
'''

# for i in range(1,13):
#     if(i%4==0):
#         print(i, "is divisible by 4")
#         break
#     print(i)



# continue
# for i in range(11):
#     if(i%2 !=0):
#         continue
#     print(i)


# Nested loops
# for i in range(10):
#     for j in range(5):
#         print("Hello World")


for i in range(4):
    for j in range(1,13):
        if j%4==0:
            break

        print(j)


# While loop
# basde on the conditions
num=10
while num>0:
    print(num,"Hello")
    num -=1

'''
Output:
10 Hello
9 Hello
8 Hello
7 Hello
6 Hello
5 Hello
4 Hello
3 Hello
2 Hello
1 Hello
'''