
# Function for checking the divisibility
# Notice the indentation after function declaration
# and if and else statements
def checkDivisibility(a, b):
    if a % b == 0 :
        print ("a is divisible by b")
    else:
        print ("a is not divisible by b")
# program to test the above function
checkDivisibility(4, 2)


# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)





# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1

    # An Infinite loop to generate squares 
    while True:
        yield i*i                
        i += 1  # Next execution resumes 
                # from this point     

# Driver code to test above generator 
# function
for num in nextSquare():
    if num > 100:
         break    
    print(num)



# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))



#  Import built-in module  random
from random import *

print(dir(random))



#  Import built-in module  random
import  random
print(dir(random))


# importing built-in module math
import math

# using square root(sqrt) function contained 
# in math module
print(math.sqrt(25)) 

# using pi function contained in math module
print(math.pi) 

# 2 radians = 114.59 degreees
print(math.degrees(2))  

# 60 degrees = 1.04 radians
print(math.radians(60))  

# Sine of 2 radians
print(math.sin(2))  

# Cosine of 0.5 radians
print(math.cos(0.5))  

# Tangent of 0.23 radians
print(math.tan(0.23)) 

# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))  

# importing built in module random
import random

# printing random integer between 0 and 5
print(random.randint(0, 5))  

# print random floating point number between 0 and 1
print(random.random())  

# random number between 0 and 100
print(random.random() * 100)  

List = [1, 4, True, 800, "python", 27, "hello"]

# using choice function in random module for choosing 
# a random element from a set such as a list
print(random.choice(List)) 


# importing built in module datetime
import datetime
from datetime import date
import time

# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())  

# Converts a number of seconds to a date object
print(date.fromtimestamp(454554))  


 
# A Python program to demonstrate inheritance 

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"
class Person(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is employee
    def isEmployee(self):
        return False


# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Weeb1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Weeb2") # An Object of Employee
print(emp.getName(), emp.isEmployee())





# Python example to check if a class is
# subclass of another

class Base(object):
    pass   # Empty Class

class Derived(Base):
    pass   # Empty Class

# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))


# Python example to show working of multiple 
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Weeb1"
        print ("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Weeb2"        
        print ("Base2")

class Derived(Base1, Base2):
    def __init__(self):
        
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print ("Derived")
        
    def printStrs(self):
        print(self.str1, self.str2)
       

ob = Derived()
ob.printStrs()



# Python example to show that base
# class members can be accessed in
# derived class using base class name
class Base(object):

    # Constructor
    def __init__(self, x):
        self.x = x    

class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        Base.x = x 
        self.y = y

    def printXY(self):
     
       # print(self.x, self.y) will also work
       print(Base.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()



 
class X(object):
    def __init__(self, a):
        self.num = a
    def doubleup(self):
        self.num *= 2

class Y(X):
    def __init__(self, a):
        X.__init__(self, a)
    def tripleup(self):
        self.num *= 3

obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)



# Base or Super class
class Person(object):
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    def __init__(self, name, eid):

        ''' In Python 3.0+, "super().__init__(name)"
            also works''' 
        super(Employee, self).__init__(name)
        self.empID = eid
        
    def isEmployee(self):
        return True
        
    def getID(self):
        return self.empID

# Driver code
emp = Employee("Weeb boi", "E101") 
print(emp.getName(), emp.isEmployee(), emp.getID())



# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:

    # Hidden member of MyClass
    __hiddenVariable = 10

# Driver code
myObject = MyClass()     
print(myObject._MyClass__hiddenVariable)




class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s," \
              "b is %s" % (self.a, self.b)

# Driver Code        
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()




class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Driver Code        
t = Test(1234, 5678)
print(t) 




# Python program to show that the variables with a value 
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
    stream = 'cse'                  # Class Variable
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable

# Objects of CSStudent class
a = CSStudent('Weeb', 1)
b = CSStudent('Normie', 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)    # prints "Geek"
print(b.name)    # prints "Nerd"
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'

# To change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'mech'
print(b.stream) # prints 'mech'




def create_cycle():

    # create a list x
    x = [ ]

    # A reference cycle is created
    # here as x contains reference to
    # to self.
    x.append(x)
 
create_cycle()




x = []
x.append(1)
x.append(2)

# delete the list from memory or 
# assigning object x to None(Null)
del x 
# x = None






# loading gc
import gc

# get the current collection 
# thresholds as a tuple
print("Garbage collection thresholds:",
                    gc.get_threshold())




# Importing gc module
import gc

# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()

# Prints Garbage collector 
# as 0 object
print("Garbage collector: collected",
          "%d objects." % collected)



import gc
i = 0 

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = { }
    x[i+1] = x
    print (x)

# lists are cleared whenever a full collection or 
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print ("Garbage collector: collected %d objects." % (collected))

print ("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()

print ("Garbage collector: collected %d objects." % (collected))


# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y

# using the normally
# defined function
print(cube(5))

# using the lamda function
print(lambda_cube(5))




# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))

print(adults)



# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)



# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'komodo', 'python']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)


# Python code to illustrate 
# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)



# python code to demonstrate working of reduce() 
# with a lambda function

# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 410 , 3333, 52, 611, 234, ] 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 



#end of day 4 code
