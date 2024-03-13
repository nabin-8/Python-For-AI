# Operators in Python
'''
    What is operator in Python?
    An operator is a symbol that performs an operation on one or more operands.

    Different Types of Operators in Python:
    1. Arithmetic Operators.
    2. Comparison Operators.
    3. Logical Operators.
    4. Assignment Operators.
    5. Bitwise Operators.
    6. Membership Operators.
    7. Identity Operators.
'''

'''
 1. Arithmetic Operators.
 +, -, *, /, % (modulo), // (floor division), ** (exponentiation).
'''

a=10
b=20
c=a+b
# print(c) # 30
c=a-b
# print(c) # -10
c=a*b
# print(c) # 200
c=a/b
# print(c) # 0.5
# print(23//3) # 7
c=a%b
# print(c) # 10
# print(10%10) # 0
c=a**b
# print(c) # 100000000000000000000

# num=int(input("Enter the number: "))
# print(num%2==0) #True


'''# To definr positive and negative infinity we use in python called as float'''
# Positive infinity
post_inf=float('inf') #inf
# print(post_inf)
# Negative infinity
nge_inf=float('-inf') #-inf
# print(nge_inf)
# ###############
# Nan (Not a number)
nan=float('nan') #nan
# print(nan) 

'''
2. Comparison Operators.
 == (equal to), != (not equal to), < (less than), > (greater than), <= (less than or equal to), >= (greater than or equal to).
'''

num1=10
num2=20
# print(num1==num2) #False
# print(num1!=num2) #True
# print(num1>num2) #False
# print(num1<num2) #True
# print(num1>=num2) #False
# print(num1<=num2) #True


'''
3. Logical Operators.
and (logical AND), or (logical OR), not (logical NOT).
1.AND
2.OR
3.NOT
'''
log1=True
log2=False
# print(log1 and log2) #False
# print(log1 or log2) #True
# print(not log1) #False
# print(not log2) #True

'''
4. Assignment Operators.
= (assign),
+= (add and assign),
-= (subtract and assign),
*= (multiply and assign),
/= (divide and assign),
%= (modulo and assign),
//= (floor divide and assign),
**= (exponentiate and assign).
'''
a=10
b=10
a=a+b #10+10=20
# print(a) #output: 20
a+=b # both are same
# print(a) #output: 30

a-=b
# print(a) #20
a*=b
# print(a) #200
a/=b
# print(a) #20.0
a%=b
# print(a) #0.0

num1=2
num2=5
num1//=num2
# print(num1)
# num1**=num2
# print(num1) #32

'''
5. Bitwise Operators.
& (bitwise AND),
| (bitwise OR),
^ (bitwise XOR),
~ (bitwise NOT),
<< (left shift),
>> (right shift).
'''
bnum1=5
bnum2=3
# print(bnum1 | bnum2) #7
# print(bnum1 & bnum2) #1
# print(bnum1 ^ bnum2) #6
# print(~ bnum2) #-4
# print(bnum1 <<1) #10
# print(bnum1 >>1) #2

'''
6. Membership Operators.
in (checks if a value is present in a sequence),
not in (checks if a value is not present in a sequence).
'''
my_arr=[1,2,3,5,9,8,6,]
print(5 in my_arr) #True
print(4 in my_arr) #False


'''
7. Identity Operators.
 is (checks if two variables refer to the same object), 
 is not (checks if two variables do not refer to the same object).
'''

x=5
y=5

# print(x is y) #True
# print(x is not y) #False

arr1=[1,2,3]
arr2=[1,2,3]
# print(arr1 is arr2) #False



'''
Operator Precidence
'''
result=4+5*6/6
print(result)
result=4+(5*6)/6
print(result)