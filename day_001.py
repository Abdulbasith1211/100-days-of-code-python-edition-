 
# Python code for "Hello World"
print("Hello World")      



# Python program to declare variables
myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber ="helloworld"
print(myNumber)




# Python program to illustrate a list 

# creates a empty list
nums = [] 

# appending data in list
nums.append(22)
nums.append(23)
nums.append("String")

print(nums)



# Python program to illustrate
# getting input from user
name = input("Enter your name: ") 

# user entered the name 'Basith'
print("hello", name)


# Python3 program to get input from user

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)



# Python program to illustrate
# selection statement

num1 = 34
if(num1>12):
    print("Num1 is good")
elif(num1>35):
    print("Num2 is not good....")
else:
    print("Num2 is great")



# Python program to illustrate
# functions
def hello():
    print("hello")
    print("hello again")
hello()

# calling function
hello()               


#Python program to illustrate 
#Function with  main 
def getInteger():
    result = int(input("Enter integer: "))
    return result

def main():
    print("Started")
    #calling the getInteger function and 
    #storing its returned value in the output variable
    output = getInteger()
    print(output)
#now we are required to tell python
# for 'Main' function existence 
if __name__=="__main__": 
    main()


#Python program to illustrate
# a simple for loop 
for step in range(5):
    print(step) 


#Python program to illustrate 
# math module 
import math 

def main():
    num = -85
    #fabs is used to get the absolute 
    #value of a decimal 
    num = math.fabs(num)
    print(num)

if __name__=="__main__":
 main() 


#Python program to illustrate  Examples of Arithmetic Operator 
a = 8
b = 6

# Addition of numbers 
add = a + b 

# Subtraction of numbers 
sub = a - b 

# Multiplication of number 
mul = a * b 

# Division(float) of number 
div1 = a / b 

# Division(floor) of number 
div2 = a // b 

# Modulo of both number 
mod = a % b 

# Power
p = a ** b

# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod)
print(p)



# Python program to illustrate examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)


#Python program to illustrate examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)



#python program to illustrate examples of Bitwise operators
a = 20
b = 14

# Print bitwise AND operation  
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation 
print(~a)

# print bitwise XOR operation 
print(a ^ b)

# print bitwise right shift operation 
print(a >> 2)

# print bitwise left shift operation 
print(a << 2)


#python program to illustrate examples of Identity operators
a1 = 3
b1 = 3
a2 = 'AbdulBasith'
b2 = 'AbdulBasith'
a3 = [1,2,3]
b3 = [1,2,3]


print(a1 is not b1)


print(a2 is b2)

# Output is False, since lists are mutable.
print(a3 is b3)



#python program to illustrate examples of Membership operator
x = 'Coding is Fun'
y = {3:'a',13:'b'}


print('C' in x)

print('Fun' not in x)

print('Coding' not in x)

print(3 in y)

print('b' in y)


#python program to illustrate examples of Operator Precedence

# Precedence of '+' & '*' 
expr = 10 + 20 * 30
print(expr) 

# Precedence of 'or' & 'and' 
name = "Malen"
age = 24
  
if name == "Malen" or name == "John" and age >= 2 :  
    print("Hello! Welcome.") 
else : 
    print("Good Bye!!")


#python program to illustrate examples of Operator Associativity

# Left-right associativity 
# 100 / 10 * 10 is calculated as  
# (100 / 10) * 10 and not  
# as 100 / (10 * 10) 
print(100 / 10 * 10) 
  
# Left-right associativity 
# 5 - 2 + 3 is calculated as  
# (5 - 2) + 3 and not  
# as 5 - (2 + 3) 
print(5 - 2 + 3) 
  
# left-right associativity 
print(5 - (2 + 3)) 
  
# right-left associativity 
# 2 ** 3 ** 2 is calculated as  
# 2 ** (3 ** 2) and not  
# as (2 ** 3) ** 2 
print(2 ** 3 ** 2)



#Python program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)



# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
print({True: a, False: b} [a < b])

# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())



# Python program to demonstrate ternary operator
a, b = 22, 66

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
print({True: a, False: b} [a < b])

# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())


# Python program to demonstrate nested ternary operator
a, b = 12, 23

print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")



# Python program to demonstrate nested ternary operator
a, b = 10, 20

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")


    
# Program to demonstrate conditional operator
a, b = 19, 30

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't 
# work if a is 0.
min = a < b and a or b

print(min)


# A Python program to demonstrate the use of 
# "//" for integers
print (7//3)
print (-3//3)



# A Python program to demonstrate use of 
# "/" for floating point numbers
print (14.0/2)
print (-14.0/2)



# A Python program to demonstrate use of 
# "//" for both integers and floating points
print (5//2)
print (-5//2)
print (5.0//2)
print (-5.0//2)




# A Python program to demonstrate that we can store
# large numbers in Python

x = 1234555666777888888888766888
x = x + 1
print(x)


# A Python program to show that there are two types in
# Python 2.7 : int and long int
# And in Python 3 there is only one type : int

x = 10
print(type(x))

x = 10000000000000000000000000000000000000000000
print(type(x))




# Printing 100 raise to power 100
print(100**100)





# This Python program must be run with
# Python 3 as it won't work with 2.7.

# ends the output with '@'
print("Python" , end = '@') 
print("GeeksforGeeks")



# This Python program must be run with
# Python 3 as it won't work with 2.7.

# ends the output with a <space> 
print("Welcome to" , end = ' ') 
print("Wakanda", end = ' ')



x = 112

print("x is of type:",type(x))

y = 1033.6
print("y is of type:",type(y))

x = x + y

print(x)
print("x is of type:",type(x))




# Python code to demonstrate Type conversion
# using int(), float()

# initializing string
s = "10010"

# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)

# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)



# Python code to demonstrate Type conversion
# using  ord(), hex(), oct()

# initializing integer
s = 's'

# printing character converting to integer
c = ord(s)
print ("After converting character to integer : ",end="")
print (c)

# printing integer converting to hexadecimal string
c = hex(56)
print ("After converting 56 to hexadecimal string : ",end="")
print (c)

# printing integer converting to octal string
c = oct(56)
print ("After converting 56 to octal string : ",end="")
print (c)



# Python code to demonstrate Type conversion
# using  tuple(), set(), list()

# initializing string
s = 'sikee'

# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c)

# printing string converting to set
c = set(s)
print ("After converting string to set : ",end="")
print (c)

# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c)



# Python code to demonstrate Type conversion
# using  dict(), complex(), str()

# initializing integers
a = 12
b = 24

# initializing tuple
tup = (('a', 12) ,('f', 24), ('g', 3))

# printing integer converting to complex number
c = complex(12,24)
print ("After converting integer to complex number : ",end="")
print (c)

# printing integer converting to string
c = str(a)
print ("After converting integer to string : ",end="")
print (c)

# printing tuple converting to expression dictionary
c = dict(tup)
print ("After converting tuple to dictionary : ",end="")
print (c)



# Convert ASCII value to characters
a = chr(79)
b = chr(87)
c = chr(79)
print(a)
print(b)
print(c)




#typecasting input to int

# input
num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))

# printing the sum in integer
print(num1 + num2)


#typecasting input to float

# input
num1 = float(input("Enter input:"))
num2 = float(input("Enter input:"))

# printing the sum in float
print(num1 + num2)

#typecasting input  to float

# input
num1 = float(input("Enter input:"))
num2 = float(input("Enter input:"))

# printing the sum in float
print(num1 + num2)


#typecasting input to string

# input
string = str(input("Enter input:"))

# output
print(string)


#