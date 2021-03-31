#DAY-009 - PYTHON DECORATORS


def multiply(a, b):
    return a * b

product = multiply  # assigning the function multiply to variable product
print(product(5, 6))  # calling the function using product



#passing a function as argument to another function
def display(func):
    print("This is the display function")
    func()
	
def message():
    print("Welcome everyone!")
	
display(message)


#Defining a Function inside another Function (Nested Function)

def outer():
    def inner():  # defining nested function
        print("This is nested function")

    print("This is outer function")
    inner()  # calling nested function

outer()  # calling outer function


#Returning a Nested Function from its Parent Function

def outer():
    def inner():  # defining nested function
        print("Welcome everyone!")
	
    return inner  # returning nested function

message = outer()  # calling outer function
message()


def outer(x):
    def inner():
        print(x)

    return inner  # returning inner function

message = outer("Hey there!")
message()




def decorator_func(func):
    def inner():
        print("****")
        func()
        print("****")

    return inner  # returning inner function

def normal():
    print("I am a normal function")

decorated_func = decorator_func(normal)
decorated_func()


#assigning decorator function to normal()will modify the normal( ) as shown below

def decorator_func(func):
    def inner():
        print("****")
        func()
        print("****")

    return inner  # returning inner function

def normal():
    print("I am a normal function")

normal = decorator_func(normal)
normal()



#decorator converts text returned by a function to lowercase

def decorator_lowercase(func):
    def to_lower():
        text = func()
        lowercase_text = text.lower()
        return lowercase_text

    return to_lower  # returning inner function

@decorator_lowercase
def message():
    return "I Am a Normal Function"

print(message())


#Passing Parameterized Functions to Decorators


def decorator_division(func):
    def division(a, b):
        if b == 0:
            return "Can't divide!"
        else:
            return a/b

    return division  # returning inner function

@decorator_division
def divide(num1, num2):
    return num1/num2

print(divide(10, 2))


#Python Chaining Decorators

def decorator_star(func):
    def inner():
        print("****")
        func()
        print("****")

    return inner  # returning inner function

def decorator_hash(func):
    def inner():
        print("####")
        func()
        print("####")

    return inner  # returning inner function

@decorator_star
@decorator_hash
def normal():
    print("I am a normal function")

normal()



#end of day 9 