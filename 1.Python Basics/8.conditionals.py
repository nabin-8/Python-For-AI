# conditionals in Python
'''
In conditions there is two thing 
if there true or false
'''

is_Loggid_in=True

# if(is_Loggid_in):
#     print("Logid IN")

# x=int(input("Enter the number: "))

# if-else
# if x>15 :
#     print("Number is greater than 15")

# if x>15 :
#     print("Number is greater than 15")
# else :
#     print("Number is less than 15")


# Multiple Conditionals
# if x>15 :
#     print("Number is greater than 15")
# elif x==15:
#     print("Number is equal to 15")
# else :
#     print("Number is less than 15")

# Simple Example
# marks=int(input("Enter your Marks: "))

# if marks>=90 :
#     print("A")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# elif marks>=50:
#     print("D")
# else :
#     print("E")

'''
Truthy value
Non-Empty=True
Non-Zero-Numerical value= True

falsy value
Empty=False
Numerical value which is zero=False
'''


# Nested Conditions
# x=8
# if x>5:
#     print("X is Greater than 5")
#     if x%2==0 :
#         print("x is also even")
#     else :
#         print("x is odd")

# else:
#     print("x is less than 5")

# Ternary operator

# num=5
# if num >=0:
#     print("Number is positive")
# else:
#     print("Number is negative")


# Using ternary operator
# result="Positive" if num>=0 else "Negative"
# print("Number is ",result)

# match and case statement
# Like switch in other programming languages

day_num=5

match day_num:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Invalid Number")
